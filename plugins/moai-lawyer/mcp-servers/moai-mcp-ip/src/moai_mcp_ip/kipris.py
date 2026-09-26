"""KIPRIS Plus 클라이언트 (한국 특허·실용신안·상표).

확인한 사실 (2026-09-13, 공식 상품 페이지의 오퍼레이션 명세 + 실제 호출)
- 주소: `https://plus.kipris.or.kr/kipo-api/kipi/{서비스}/{오퍼레이션}`
- 인증: 쿼리 파라미터 `ServiceKey`
- 응답: XML만. **오류도 HTTP 200** 으로 오고, `header/successYN=N` 과 `resultCode` 로 구분한다.
- 검색 결과: `response/body/items/item[]`, 전체 건수는 `response/count/totalCount`
  (`count` 는 `body` 안이 아니라 옆에 있다).
- 서비스 경로 철자가 실제로 `patUtiModInfoSearchSevice` 다 (Service 아님).
- 데이터 상품별로 이용 신청·기간이 따로다. 기간이 끝난 상품은 `resultCode=31
  DEADLINE_HAS_EXPIRED_ERROR` 를 돌려준다.
"""

from __future__ import annotations

from typing import Any

import httpx

from moai_mcp_core import AuthError, HttpClient, McpToolError, UpstreamError

from . import xmlutil

BASE_URL = "https://plus.kipris.or.kr/kipo-api/kipi"
PATENT_SERVICE = "patUtiModInfoSearchSevice"
TRADEMARK_SERVICE = "trademarkInfoSearchService"

#: 상표 검색의 필수 그룹 — 그룹마다 하나 이상 true 여야 하며, 그룹 전체를 비우면 오류다.
TRADEMARK_STATUS_FLAGS = (
    "application", "registration", "refused", "expiration",
    "withdrawal", "publication", "cancel", "abandonment",
)
TRADEMARK_TYPE_FLAGS = (
    "trademark", "serviceMark", "trademarkServiceMark", "businessEmblem", "collectiveMark",
    "geoOrgMark", "internationalMark", "certMark", "geoCertMark",
)
TRADEMARK_COMPOSITION_FLAGS = (
    "character", "figure", "compositionCharacter", "figureComposition", "sound", "fragrance",
    "color", "dimension", "colorMixed", "hologram", "motion", "visual", "invisible",
)

#: 특허 검색 `lastvalue` — 빈 값은 전체.
PATENT_STATUS_CODES = {
    "": "전체", "A": "공개", "C": "취하", "F": "소멸", "G": "포기", "I": "무효", "J": "거절", "R": "등록",
}
PATENT_SORT_SPECS = ("PD", "AD", "GD", "OPD", "FD", "FOD", "RD")

MAX_ROWS = 500


def _pick_flags(selected: list[str] | None, allowed: tuple[str, ...], group: str) -> dict[str, str]:
    if not selected:
        chosen = list(allowed)
    else:
        unknown = [s for s in selected if s not in allowed]
        if unknown:
            raise McpToolError(
                f"{group} 값이 올바르지 않습니다: {', '.join(unknown)}",
                details={"allowed": list(allowed)},
            )
        chosen = selected
    return {flag: ("true" if flag in chosen else "false") for flag in allowed}


def _clean(params: dict[str, Any]) -> dict[str, str]:
    cleaned: dict[str, str] = {}
    for key, value in params.items():
        if value is None or value == "":
            continue
        if isinstance(value, bool):
            cleaned[key] = "true" if value else "false"
        else:
            cleaned[key] = str(value)
    return cleaned


def _rows(num_of_rows: int) -> int:
    if not 1 <= num_of_rows <= MAX_ROWS:
        raise McpToolError(f"num_of_rows 는 1~{MAX_ROWS} 사이여야 합니다.")
    return num_of_rows


class KiprisClient:
    def __init__(self, api_key: str, *, transport: httpx.BaseTransport | None = None) -> None:
        self._api_key = api_key
        self._http = HttpClient(BASE_URL, transport=transport, max_retries=2)

    def close(self) -> None:
        self._http.close()

    # ------------------------------------------------------------------ 공통
    def call(self, service: str, operation: str, params: dict[str, Any]) -> Any:
        query = _clean(params)
        try:
            response = self._http.request(
                "GET", f"{service}/{operation}", params={**query, "ServiceKey": self._api_key}
            )
        except McpToolError as exc:
            raise self._scrub(exc) from None

        root = xmlutil.parse(response.text)
        success = xmlutil.text_of(root, "successYN")
        code = xmlutil.text_of(root, "resultCode")
        message = xmlutil.text_of(root, "resultMsg")
        if success != "Y":
            if code == "31":
                raise AuthError(
                    "KIPRIS Plus에서 이 데이터 상품의 이용 기간이 끝났거나 이용 신청이 되어 있지 않습니다. "
                    "마이페이지에서 해당 상품(특허·실용신안 또는 상표)의 이용 신청·기간을 확인하세요.",
                    details={"result_code": code, "result_msg": message, "service": service},
                )
            raise UpstreamError(
                f"KIPRIS Plus가 요청을 처리하지 못했습니다 (resultCode {code or '?'}: {message or '메시지 없음'}).",
                body=f"service={service} operation={operation} resultCode={code} resultMsg={message}",
            )
        return root

    def _scrub(self, exc: McpToolError) -> McpToolError:
        """오류 메시지·세부에 키가 섞여 나가지 않게 가린다 (httpx 오류 문자열에 URL이 들어갈 수 있다)."""
        if not self._api_key:
            return exc
        exc.message = exc.message.replace(self._api_key, "***")
        for key, value in list(exc.details.items()):
            if isinstance(value, str):
                exc.details[key] = value.replace(self._api_key, "***")
        exc.args = (exc.message,)
        return exc

    @staticmethod
    def _search_result(root: Any, query: dict[str, Any]) -> dict[str, Any]:
        items = [xmlutil.element_to_data(item) for item in xmlutil.find_all(root, "item")]
        total = xmlutil.text_of(root, "totalCount")
        return {
            "ok": True,
            "source": "kipris-plus",
            "total_count": int(total) if total.isdigit() else None,
            "page_no": xmlutil.text_of(root, "pageNo"),
            "num_of_rows": xmlutil.text_of(root, "numOfRows"),
            "returned_count": len(items),
            "query": _clean(query),
            "items": items,
        }

    # ------------------------------------------------------------------ 특허
    def patent_search(
        self,
        *,
        word: str = "",
        invention_title: str = "",
        abstract: str = "",
        claim: str = "",
        ipc_number: str = "",
        applicant: str = "",
        inventors: str = "",
        right_holder: str = "",
        patent: bool = True,
        utility: bool = True,
        status: str = "",
        sort_spec: str = "",
        desc_sort: bool | None = None,
        page_no: int = 1,
        num_of_rows: int = 20,
        extra_params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if status not in PATENT_STATUS_CODES:
            raise McpToolError("status 값이 올바르지 않습니다.", details={"allowed": PATENT_STATUS_CODES})
        if sort_spec and sort_spec not in PATENT_SORT_SPECS:
            raise McpToolError("sort_spec 값이 올바르지 않습니다.", details={"allowed": list(PATENT_SORT_SPECS)})
        if not any([word, invention_title, abstract, claim, ipc_number, applicant, inventors, right_holder, extra_params]):
            raise McpToolError("검색 조건을 하나 이상 넣어 주세요 (word·invention_title·ipc_number·applicant 등).")
        query: dict[str, Any] = {
            "word": word,
            "inventionTitle": invention_title,
            "astrtCont": abstract,
            "claimScope": claim,
            "ipcNumber": ipc_number,
            "applicant": applicant,
            "inventors": inventors,
            "rightHoler": right_holder,  # 공식 명세의 철자 그대로
            "patent": patent,
            "utility": utility,
            "lastvalue": status,
            "sortSpec": sort_spec,
            "descSort": desc_sort,
            "pageNo": page_no,
            "numOfRows": _rows(num_of_rows),
            **(extra_params or {}),
        }
        root = self.call(PATENT_SERVICE, "getAdvancedSearch", query)
        return self._search_result(root, query)

    def patent_detail(self, application_number: str) -> dict[str, Any]:
        number = _digits(application_number)
        root = self.call(PATENT_SERVICE, "getBibliographyDetailInfoSearch", {"applicationNumber": number})
        body = xmlutil.find_first(root, "body")
        return {
            "ok": True,
            "source": "kipris-plus",
            "application_number": number,
            "detail": xmlutil.element_to_data(body) if body is not None else {},
        }

    # ------------------------------------------------------------------ 상표
    def trademark_search(
        self,
        *,
        trademark_name: str = "",
        trademark_name_match: str = "",
        free_search: str = "",
        classification: str = "",
        similarity_code: str = "",
        designated_goods: str = "",
        applicant_name: str = "",
        agent_name: str = "",
        right_holder: str = "",
        vienna_code: str = "",
        application_date: str = "",
        registration_date: str = "",
        statuses: list[str] | None = None,
        mark_types: list[str] | None = None,
        compositions: list[str] | None = None,
        page_no: int = 1,
        num_of_rows: int = 30,
        extra_params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        if not any([trademark_name, trademark_name_match, free_search, classification, similarity_code,
                    designated_goods, applicant_name, agent_name, right_holder, vienna_code, extra_params]):
            raise McpToolError("검색 조건을 하나 이상 넣어 주세요 (trademark_name·free_search·similarity_code 등).")
        query: dict[str, Any] = {
            "trademarkName": trademark_name,
            "trademarkNameMatch": trademark_name_match,
            "freeSearch": free_search,
            "classification": classification,
            "similarityCode": similarity_code,
            "asignProduct": designated_goods,
            "applicantName": applicant_name,
            "agentName": agent_name,
            "regPrivilegeName": right_holder,
            "viennaCode": vienna_code,
            "applicationDate": application_date,
            "registerDate": registration_date,
            **_pick_flags(statuses, TRADEMARK_STATUS_FLAGS, "statuses"),
            **_pick_flags(mark_types, TRADEMARK_TYPE_FLAGS, "mark_types"),
            **_pick_flags(compositions, TRADEMARK_COMPOSITION_FLAGS, "compositions"),
            "pageNo": page_no,
            "numOfRows": _rows(num_of_rows),
            **(extra_params or {}),
        }
        root = self.call(TRADEMARK_SERVICE, "getAdvancedSearch", query)
        return self._search_result(root, query)

    def trademark_detail(self, application_number: str) -> dict[str, Any]:
        number = _digits(application_number)
        root = self.call(TRADEMARK_SERVICE, "getBibliographyDetailInfoSearch", {"applicationNumber": number})
        body = xmlutil.find_first(root, "body")
        return {
            "ok": True,
            "source": "kipris-plus",
            "application_number": number,
            "detail": xmlutil.element_to_data(body) if body is not None else {},
        }


def _digits(value: str) -> str:
    number = "".join(ch for ch in str(value) if ch.isdigit())
    if not number:
        raise McpToolError("출원번호가 비어 있습니다. 숫자만 넣어 주세요 (예: 4020210124213).")
    return number
