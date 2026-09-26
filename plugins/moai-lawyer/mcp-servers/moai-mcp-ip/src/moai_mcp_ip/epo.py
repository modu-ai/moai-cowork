"""EPO Open Patent Services(OPS) v3.2 클라이언트.

확인한 사실 (2026-09-13, EPO OPS 공식 페이지·OpenAPI YAML·Reference Guide 1.3.20·키 없는 호출)
- 토큰: `POST https://ops.epo.org/3.2/auth/accesstoken`, `Authorization: Basic base64(key:secret)`,
  본문 `grant_type=client_credentials`. 약 20분 유효.
- 호출: `https://ops.epo.org/3.2/rest-services`, `Authorization: Bearer`, `Accept: application/json`.
  오류 본문은 항상 XML이다.
- 검색: `GET /published-data/search[/biblio]?q=<CQL>`, 범위는 헤더 `X-OPS-Range: 1-25`.
  한 번에 최대 100건, 누적 2,000건까지.
- 사용량 헤더: `X-Throttling-Control`, `X-RegisteredQuotaPerWeek-Used`.
"""

from __future__ import annotations

import base64
import time
import urllib.parse
from collections.abc import Callable
from typing import Any

import httpx

from moai_mcp_core import AuthError, HttpClient, McpToolError, UpstreamError

TOKEN_URL = "https://ops.epo.org/3.2/auth/accesstoken"
API_BASE_URL = "https://ops.epo.org/3.2/rest-services"

REFERENCE_TYPES = ("publication", "application", "priority")
INPUT_FORMATS = ("docdb", "epodoc")
FAMILY_CONSTITUENTS = ("", "biblio", "legal")
MAX_PAGE = 100
MAX_TOTAL = 2000
QUOTA_HEADERS = ("X-Throttling-Control", "X-RegisteredQuotaPerWeek-Used", "X-IndividualQuotaPerHour-Used")


class EpoAuth:
    def __init__(
        self,
        key: str,
        secret: str,
        *,
        transport: httpx.BaseTransport | None = None,
        clock: Callable[[], float] = time.time,
    ) -> None:
        self._basic = base64.b64encode(f"{key}:{secret}".encode()).decode()
        self._clock = clock
        self._client = httpx.Client(transport=transport, timeout=30.0)
        self._token = ""
        self._expiry = 0.0

    def access_token(self, *, force: bool = False) -> str:
        if not force and self._token and self._clock() < self._expiry:
            return self._token
        try:
            response = self._client.post(
                TOKEN_URL,
                data={"grant_type": "client_credentials"},
                headers={"Authorization": f"Basic {self._basic}"},
            )
        except httpx.HTTPError as exc:
            raise UpstreamError(f"EPO 토큰 발급 요청이 실패했습니다: {type(exc).__name__}") from exc
        try:
            payload = response.json()
        except ValueError:
            payload = {}
        token = payload.get("access_token") if isinstance(payload, dict) else None
        if response.status_code != 200 or not token:
            raise AuthError(
                "EPO OPS 토큰을 발급받지 못했습니다. consumer key·secret 과 앱 승인 상태를 확인하세요.",
                details={"status": response.status_code},
            )
        self._token = token
        self._expiry = self._clock() + max(60.0, float(payload.get("expires_in") or 1199) - 60.0)
        return token

    def close(self) -> None:
        self._client.close()


def _choice(value: str, allowed: tuple[str, ...], name: str) -> str:
    if value not in allowed:
        raise McpToolError(f"{name} 값은 {', '.join(a or '(빈 값)' for a in allowed)} 중 하나입니다.")
    return value


def _number(value: str) -> str:
    cleaned = str(value).strip()
    if not cleaned:
        raise McpToolError("문헌 번호가 비어 있습니다 (예: docdb 형식 EP.1000000.A1, epodoc 형식 EP1000000).")
    return urllib.parse.quote(cleaned, safe=".,")


class EpoClient:
    def __init__(self, auth: EpoAuth, *, transport: httpx.BaseTransport | None = None) -> None:
        self._auth = auth
        self._transport = transport
        self._http = self._client()

    def _client(self, extra_headers: dict[str, str] | None = None) -> HttpClient:
        # @MX:NOTE: [AUTO] 요청별 헤더(X-OPS-Range)는 기본 헤더로 싣는다. 코어 HttpClient 는 재시도할 때
        # 요청별 headers 인자를 다시 붙이지 않으므로, 401 재인증 뒤 범위가 조용히 사라질 수 있다.
        return HttpClient(
            API_BASE_URL,
            auth=self._auth,
            transport=self._transport,
            max_retries=2,
            default_headers={"Accept": "application/json", **(extra_headers or {})},
        )

    def close(self) -> None:
        self._http.close()

    def _get(self, path: str, *, client: HttpClient | None = None, **kwargs: Any) -> dict[str, Any]:
        response = (client or self._http).request("GET", path, **kwargs)
        try:
            data = response.json() if response.content else None
        except ValueError as exc:
            raise UpstreamError("EPO 응답을 JSON으로 해석하지 못했습니다.", body=response.text) from exc
        quota = {h: response.headers[h] for h in QUOTA_HEADERS if h in response.headers}
        return {"ok": True, "source": "epo-ops", "quota": quota, "data": data}

    def search(self, cql: str, *, start: int = 1, end: int = 25, with_biblio: bool = False) -> dict[str, Any]:
        if not cql.strip():
            raise McpToolError("CQL 검색식이 비어 있습니다 (예: ta=\"battery\" and pa=\"samsung\").")
        if start < 1 or end < start or end - start + 1 > MAX_PAGE or end > MAX_TOTAL:
            raise McpToolError(f"범위는 1 이상, 한 번에 {MAX_PAGE}건 이하, 끝 값 {MAX_TOTAL} 이하로 넣어 주세요.")
        path = "/published-data/search/biblio" if with_biblio else "/published-data/search"
        client = self._client({"X-OPS-Range": f"{start}-{end}"})
        try:
            result = self._get(path, client=client, params={"q": cql})
        finally:
            client.close()
        result["range"] = f"{start}-{end}"
        result["cql"] = cql
        return result

    def biblio(self, reference_type: str, number: str, input_format: str = "docdb") -> dict[str, Any]:
        rt = _choice(reference_type, REFERENCE_TYPES, "reference_type")
        fmt = _choice(input_format, INPUT_FORMATS, "input_format")
        return self._get(f"/published-data/{rt}/{fmt}/{_number(number)}/biblio")

    def family(
        self, reference_type: str, number: str, input_format: str = "docdb", constituent: str = ""
    ) -> dict[str, Any]:
        rt = _choice(reference_type, REFERENCE_TYPES, "reference_type")
        fmt = _choice(input_format, INPUT_FORMATS, "input_format")
        part = _choice(constituent, FAMILY_CONSTITUENTS, "constituent")
        suffix = f"/{part}" if part else ""
        return self._get(f"/family/{rt}/{fmt}/{_number(number)}{suffix}")

    def legal(self, reference_type: str, number: str, input_format: str = "docdb") -> dict[str, Any]:
        rt = _choice(reference_type, REFERENCE_TYPES, "reference_type")
        fmt = _choice(input_format, INPUT_FORMATS, "input_format")
        return self._get(f"/legal/{rt}/{fmt}/{_number(number)}")
