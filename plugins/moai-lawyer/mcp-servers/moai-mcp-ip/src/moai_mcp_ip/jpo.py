"""JPO 特許情報取得API 클라이언트 (일본 특허·상표).

확인한 사실 (2026-09-13, ip-data.jpo.go.jp 공식 OpenAPI 명세·접속 방법 PDF·키 없는 호출)
- 토큰: `POST https://ip-data.jpo.go.jp/auth/token`, 폼 인코딩 `grant_type=password` +
  `username`/`password`. 갱신은 `grant_type=refresh_token`. 액세스 1시간, 리프레시 8시간.
- 호출: `Authorization: Bearer`, 기본 주소 `https://ip-data.jpo.go.jp/api`, JSON.
- 응답 봉투: `result.statusCode`(문자열 3자리), `errorMessage`, `remainAccessCount`, `data`.
  **일일 한도 초과(203)도 HTTP 200** 으로 온다.
- 번호로만 조회한다. 키워드 검색은 없다.
- 토큰은 메모리에만 둔다 — 파일에 오래 남기지 않는다.
"""

from __future__ import annotations

import re
import time
import urllib.parse
from collections.abc import Callable
from typing import Any

import httpx

from moai_mcp_core import (
    AuthError,
    HttpClient,
    McpToolError,
    QuotaExhausted,
    RateLimited,
    UpstreamError,
)

TOKEN_URL = "https://ip-data.jpo.go.jp/auth/token"
API_BASE_URL = "https://ip-data.jpo.go.jp/api"

STATUS_MESSAGES = {
    "107": "해당 데이터가 없습니다.",
    "108": "해당 서류 실체가 없습니다.",
    "111": "제공 대상이 아닌 사건 번호입니다.",
    "204": "파라미터가 올바르지 않습니다.",
    "205": "일본 출원이 아닌 서류입니다.",
    "208": "파라미터 값에 쓸 수 없는 문자(탭·쉼표·콜론·파이프)가 있습니다.",
    "302": "JPO 서버 응답 시간이 초과됐습니다.",
    "999": "JPO 서버에서 예상하지 못한 오류가 났습니다.",
}
#: 오류가 아니라 '결과 없음'으로 돌려줄 코드.
NOT_FOUND_CODES = {"107", "108", "111"}

APPLICATION_NUMBER_RE = re.compile(r"^\d{10}$")
CASE_KINDS = {
    "patent": ("application", "publication", "registration"),
    "trademark": ("application", "registration"),
}
FORBIDDEN_CHARS = ("\t", ",", ":", "|")


class JpoAuth:
    """비밀번호 방식 토큰 공급자. `moai_mcp_core.http.TokenProvider` 를 만족한다."""

    def __init__(
        self,
        *,
        username: str = "",
        password: str = "",
        static_token: str = "",
        transport: httpx.BaseTransport | None = None,
        clock: Callable[[], float] = time.time,
    ) -> None:
        self._username = username
        self._password = password
        self._static_token = static_token
        self._clock = clock
        self._client = httpx.Client(transport=transport, timeout=30.0)
        self._access = ""
        self._access_expiry = 0.0
        self._refresh = ""
        self._refresh_expiry = 0.0

    def access_token(self, *, force: bool = False) -> str:
        now = self._clock()
        if self._username and self._password:
            if not force and self._access and now < self._access_expiry:
                return self._access
            if self._refresh and now < self._refresh_expiry:
                try:
                    return self._issue({"grant_type": "refresh_token", "refresh_token": self._refresh})
                except AuthError:
                    pass  # 리프레시가 거절되면 비밀번호로 새로 받는다.
            return self._issue(
                {"grant_type": "password", "username": self._username, "password": self._password}
            )
        if self._static_token and not force:
            return self._static_token
        raise AuthError(
            "JPO 액세스 토큰이 없거나 만료됐습니다. JPO_API_USER·JPO_API_PASSWORD 를 설정하면 자동으로 발급합니다."
        )

    def _issue(self, form: dict[str, str]) -> str:
        try:
            response = self._client.post(TOKEN_URL, data=form)
        except httpx.HTTPError as exc:
            raise UpstreamError(f"JPO 토큰 발급 요청이 실패했습니다: {type(exc).__name__}") from exc
        try:
            payload = response.json()
        except ValueError:
            payload = {}
        token = payload.get("access_token") if isinstance(payload, dict) else None
        if response.status_code != 200 or not token:
            raise AuthError(
                "JPO 토큰을 발급받지 못했습니다. ID·비밀번호와 이용 등록 상태를 확인하세요.",
                details={"status": response.status_code},
            )
        now = self._clock()
        self._access = token
        self._access_expiry = now + max(60.0, float(payload.get("expires_in") or 3600) - 60.0)
        self._refresh = payload.get("refresh_token") or ""
        self._refresh_expiry = now + max(60.0, float(payload.get("refresh_expires_in") or 28800) - 60.0)
        return token

    def close(self) -> None:
        self._client.close()


class JpoClient:
    def __init__(self, auth: JpoAuth, *, transport: httpx.BaseTransport | None = None) -> None:
        self._auth = auth
        self._http = HttpClient(API_BASE_URL, auth=auth, transport=transport, max_retries=2)

    def close(self) -> None:
        self._http.close()

    def _get(self, path: str) -> dict[str, Any]:
        payload = self._http.get_json(path)
        result = (payload or {}).get("result") if isinstance(payload, dict) else None
        if not isinstance(result, dict):
            raise UpstreamError("JPO 응답에 result 가 없습니다.")
        code = str(result.get("statusCode", ""))
        remain = result.get("remainAccessCount")
        if code == "100":
            return {"ok": True, "found": True, "source": "jpo", "remain_access_count": remain, "data": result.get("data")}
        if code in NOT_FOUND_CODES:
            return {
                "ok": True,
                "found": False,
                "source": "jpo",
                "status_code": code,
                "message": STATUS_MESSAGES[code],
                "remain_access_count": remain,
            }
        if code == "203":
            raise QuotaExhausted("JPO API 일일 호출 상한을 넘었습니다. 한도는 매일 0시에 초기화됩니다.")
        if code == "210":
            raise AuthError("JPO 토큰이 유효하지 않습니다.")
        if code == "303":
            raise RateLimited("JPO 서버에 접속이 몰려 있습니다. 잠시 뒤 다시 시도하세요.")
        raise UpstreamError(
            f"JPO가 요청을 처리하지 못했습니다 (statusCode {code}: {STATUS_MESSAGES.get(code, result.get('errorMessage', ''))}).",
        )

    @staticmethod
    def _application_number(value: str) -> str:
        number = re.sub(r"\D", "", str(value))
        if not APPLICATION_NUMBER_RE.match(number):
            raise McpToolError(
                "JPO 출원번호는 서기 4자리 + 0으로 채운 6자리, 모두 10자리 숫자입니다 (예: 2020008423).",
                details={"received": value},
            )
        return number

    @staticmethod
    def _right(right: str) -> str:
        if right not in CASE_KINDS:
            raise McpToolError("right 는 patent 또는 trademark 여야 합니다.")
        return right

    def progress(self, right: str, application_number: str, *, simple: bool = False) -> dict[str, Any]:
        right = self._right(right)
        number = self._application_number(application_number)
        if simple and right != "patent":
            raise McpToolError("간이 경과 조회(simple)는 특허만 지원합니다.")
        endpoint = "app_progress_simple" if simple else "app_progress"
        return self._get(f"/{right}/v1/{endpoint}/{number}")

    def registration(self, right: str, application_number: str) -> dict[str, Any]:
        right = self._right(right)
        number = self._application_number(application_number)
        return self._get(f"/{right}/v1/registration_info/{number}")

    def case_number_reference(self, right: str, kind: str, number: str) -> dict[str, Any]:
        right = self._right(right)
        if kind not in CASE_KINDS[right]:
            raise McpToolError(f"{right} 의 kind 는 {', '.join(CASE_KINDS[right])} 중 하나입니다.")
        cleaned = re.sub(r"\D", "", str(number))
        if not cleaned:
            raise McpToolError("번호가 비어 있습니다.")
        return self._get(f"/{right}/v1/case_number_reference/{kind}/{cleaned}")

    def applicant_lookup(self, right: str, name: str) -> dict[str, Any]:
        right = self._right(right)
        name = str(name).strip()
        if not name or any(ch in name for ch in FORBIDDEN_CHARS):
            raise McpToolError("출원인 이름이 비어 있거나 쓸 수 없는 문자(탭·쉼표·콜론·파이프)가 들어 있습니다.")
        return self._get(f"/{right}/v1/applicant_attorney/{urllib.parse.quote(name, safe='')}")
