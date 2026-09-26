"""USPTO 클라이언트 — Open Data Portal(특허)·TSDR(상표 상태).

확인한 사실 (2026-09-13, data.uspto.gov 공식 문서·키 가이드 PDF·키 없는 호출)
- ODP: `https://api.uspto.gov`, 헤더 `X-API-KEY`, JSON.
  검색 `POST /api/v1/patent/applications/search`, 메타데이터 `GET .../{출원번호}/meta-data`.
  같은 키로 동시 호출은 1건. 429 를 받으면 **5초 이상** 기다린다.
- TSDR: `https://tsdrapi.uspto.gov`, 헤더 `USPTO-API-KEY`(표기 그대로).
  `GET /ts/cd/casestatus/{sn|rn|ref|ir}{번호}/info` → ST.96 XML.
- USPTO는 상표 **문자 검색** API를 공개하지 않는다. 유사표장 발굴은 웹 화면 몫이다.
"""

from __future__ import annotations

import re
import time
from collections.abc import Callable
from typing import Any

import httpx

from moai_mcp_core import HttpClient, McpToolError, RateLimited, UpstreamError

from . import xmlutil

ODP_BASE_URL = "https://api.uspto.gov"
TSDR_BASE_URL = "https://tsdrapi.uspto.gov"

#: ODP 429 이후 최소 대기 (공식 rate limit 안내).
ODP_MIN_WAIT_SECONDS = 5.0
MAX_ODP_LIMIT = 100


def _certificate_hint(exc: McpToolError) -> McpToolError:
    if "CERTIFICATE_VERIFY_FAILED" in exc.message or "certificate" in exc.message.lower():
        return UpstreamError(
            "USPTO 서버의 TLS 인증서를 검증하지 못했습니다(인증서 만료 등 서버 측 문제일 수 있습니다). "
            "보안상 검증을 끄지 않습니다 — 잠시 뒤 다시 시도하거나 TSDR 웹 화면으로 확인하고 LIMITED로 기록하세요.",
        )
    return exc


class OdpClient:
    def __init__(
        self,
        api_key: str,
        *,
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        self._sleep = sleep
        # 429 대기는 여기서 직접 다룬다 (코어 기본 백오프는 5초보다 짧다).
        self._http = HttpClient(
            ODP_BASE_URL,
            transport=transport,
            max_retries=0,
            sleep=sleep,
            default_headers={"X-API-KEY": api_key, "Accept": "application/json"},
        )

    def close(self) -> None:
        self._http.close()

    def _request_json(self, method: str, path: str, **kwargs: Any) -> Any:
        attempts = 0
        while True:
            try:
                response = self._http.request(method, path, **kwargs)
                return response.json() if response.content else None
            except RateLimited as exc:
                if attempts >= 2:
                    raise
                self._sleep(max(ODP_MIN_WAIT_SECONDS, exc.retry_after or 0.0))
            except UpstreamError as exc:
                if not (exc.status and exc.status >= 500) or attempts >= 1:
                    raise _certificate_hint(exc) from None
                self._sleep(ODP_MIN_WAIT_SECONDS)
            except McpToolError as exc:
                raise _certificate_hint(exc) from None
            except ValueError as exc:
                raise UpstreamError("USPTO 응답을 JSON으로 해석하지 못했습니다.") from exc
            attempts += 1

    def patent_search(
        self,
        *,
        q: str = "",
        filters: list[dict[str, Any]] | None = None,
        range_filters: list[dict[str, Any]] | None = None,
        sort: list[dict[str, Any]] | None = None,
        fields: list[str] | None = None,
        offset: int = 0,
        limit: int = 25,
    ) -> dict[str, Any]:
        if not 1 <= limit <= MAX_ODP_LIMIT:
            raise McpToolError(f"limit 은 1~{MAX_ODP_LIMIT} 사이로 넣어 주세요.")
        if offset < 0:
            raise McpToolError("offset 은 0 이상이어야 합니다.")
        body: dict[str, Any] = {"pagination": {"offset": offset, "limit": limit}}
        if q:
            body["q"] = q
        if filters:
            body["filters"] = filters
        if range_filters:
            body["rangeFilters"] = range_filters
        if sort:
            body["sort"] = sort
        if fields:
            body["fields"] = fields
        data = self._request_json("POST", "/api/v1/patent/applications/search", json=body)
        return {"ok": True, "source": "uspto-odp", "request": body, "data": data}

    def patent_application(self, application_number: str) -> dict[str, Any]:
        number = re.sub(r"[^0-9A-Za-z]", "", str(application_number))
        if not number:
            raise McpToolError("출원번호가 비어 있습니다 (예: 16123456).")
        data = self._request_json("GET", f"/api/v1/patent/applications/{number}/meta-data")
        return {"ok": True, "source": "uspto-odp", "application_number": number, "data": data}


TSDR_TYPES = {
    "sn": re.compile(r"^\d{8}$"),
    "rn": re.compile(r"^\d{6,8}$"),
    "ref": re.compile(r"^[0-9A-Za-z-]+$"),
    "ir": re.compile(r"^\d+$"),
}


class TsdrClient:
    def __init__(self, api_key: str, *, transport: httpx.BaseTransport | None = None) -> None:
        self._http = HttpClient(
            TSDR_BASE_URL,
            transport=transport,
            max_retries=2,
            default_headers={"USPTO-API-KEY": api_key},
        )

    def close(self) -> None:
        self._http.close()

    def trademark_status(self, number: str, number_type: str = "sn") -> dict[str, Any]:
        number_type = number_type.lower().strip()
        raw = str(number).strip()
        if raw[:3].lower() in TSDR_TYPES and not raw[:3].isdigit():
            number_type, raw = raw[:3].lower(), raw[3:]
        elif raw[:2].lower() in TSDR_TYPES and not raw[:2].isdigit():
            number_type, raw = raw[:2].lower(), raw[2:]
        if number_type not in TSDR_TYPES:
            raise McpToolError("number_type 은 sn·rn·ref·ir 중 하나여야 합니다.")
        cleaned = raw if number_type == "ref" else re.sub(r"\D", "", raw)
        if not TSDR_TYPES[number_type].match(cleaned):
            raise McpToolError(
                f"{number_type} 번호 형식이 올바르지 않습니다 (일련번호 sn 은 8자리 숫자).",
                details={"received": raw},
            )
        case_id = f"{number_type}{cleaned}"
        try:
            response = self._http.request("GET", f"/ts/cd/casestatus/{case_id}/info")
        except McpToolError as exc:
            raise _certificate_hint(exc) from None
        root = xmlutil.parse(response.text)
        return {
            "ok": True,
            "source": "uspto-tsdr",
            "case_id": case_id,
            "status": xmlutil.element_to_data(root),
        }
