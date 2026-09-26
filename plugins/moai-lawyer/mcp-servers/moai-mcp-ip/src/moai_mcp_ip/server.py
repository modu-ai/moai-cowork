"""moai-mcp-ip MCP 서버 — stdio 진입점.

도구 이름 접두어가 데이터 소스를 나타낸다.

- `ip_check_access` : 자격증명 게이트. 조사 전에 반드시 먼저 부른다. 값은 절대 싣지 않는다.
- `kipris_*`        : 한국 특허·실용신안·상표 (KIPRIS Plus)
- `uspto_*`         : 미국 특허(ODP)·상표 상태(TSDR)
- `jpo_*`           : 일본 특허·상표 번호 기반 조회
- `epo_*`           : 유럽·국제 특허 검색·서지·패밀리·법적 상태

자격증명이 없으면 서버는 크래시하지 않고 `setup_required` 오류와 등록 안내를 돌려준다.
"""

from __future__ import annotations

import json
import logging
from collections.abc import Callable
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

from moai_mcp_core import McpToolError, SetupRequired, to_tool_result

from . import access
from .redact import redact
from .epo import EpoAuth, EpoClient
from .jpo import JpoAuth, JpoClient
from .kipris import KiprisClient
from .uspto import OdpClient, TsdrClient

_INSTRUCTIONS = (
    "특허·상표 공식 데이터 MCP. 조사를 시작하기 전에 ip_check_access 로 필요한 소스의 자격증명을 확인하고, "
    "missing 이면 검색하지 말고 registration_url 로 등록 절차를 먼저 안내한다. 키 값을 채팅으로 받지 않는다. "
    "USPTO는 상표 문자 검색 API가 없고(상태 조회만), JPO는 번호 기반 조회만 가능하다 — 그 부분은 공개 웹 화면으로 "
    "보완하고 LIMITED로 기록한다. 결과 0건은 '등록 가능'이나 '침해 없음'의 근거가 아니다."
)

mcp: FastMCP = FastMCP("moai-mcp-ip", instructions=_INSTRUCTIONS)

# @MX:WARN: [AUTO] httpx 는 INFO 로 요청 URL 전체를 로그에 남긴다
# @MX:REASON: KIPRIS Plus 는 키를 쿼리 파라미터(ServiceKey)로 받으므로, 이 줄이 없으면 호스트 로그 파일에 키가 남는다
for _noisy in ("httpx", "httpcore"):
    logging.getLogger(_noisy).setLevel(logging.WARNING)

#: 테스트에서 네트워크를 갈아 끼우는 주입점.
_TRANSPORT: httpx.BaseTransport | None = None
#: 도구 응답 최대 길이(문자). 넘으면 잘라서 안내한다 — 호스트가 긴 응답을 버리는 것을 막는다.
MAX_RESPONSE_CHARS = 120_000

# 토큰 캐시를 살리기 위해 인증 객체는 자격증명이 바뀌기 전까지 재사용한다.
_auth_cache: dict[str, tuple[tuple[str, ...], Any]] = {}


def _reset_for_tests() -> None:
    _auth_cache.clear()


# ------------------------------------------------------------------ 공통
# @MX:ANCHOR: [AUTO] 모든 조회 도구가 지나는 자격증명 게이트
# @MX:REASON: 여기서 SetupRequired 를 올리지 않으면 키 없이 외부 호출이 나가고, 값이 응답에 섞일 여지가 생긴다
def _require(source_id: str) -> dict[str, str]:
    """소스 자격증명을 해석한다. 없으면 SetupRequired."""
    source = access.SOURCES[source_id]
    store = access.credential_store()
    option = access.satisfied_option(source, store)
    if option is None:
        raise SetupRequired(
            f"{source.label} 자격증명이 설정되지 않아 조회하지 않았습니다. 공식 등록 후 키를 설정하세요 "
            "(키 값은 채팅에 붙여 넣지 말고 플러그인 설정 화면 또는 자격증명 파일에 넣으세요).",
            missing=[" + ".join(o) for o in source.alternatives],
            guide=source.registration_url,
        )
    return {name: store.get(name) for name in option}


def _bounded(result: dict[str, Any]) -> dict[str, Any]:
    text = json.dumps(result, ensure_ascii=False)
    if len(text) <= MAX_RESPONSE_CHARS:
        return result
    return {
        "ok": True,
        "truncated": True,
        "message": (
            f"응답이 {len(text):,}자로 길어 앞부분만 싣습니다. 페이지 크기(num_of_rows·limit·범위)를 줄여 다시 조회하세요."
        ),
        "partial_json": text[:MAX_RESPONSE_CHARS],
    }


def _secrets() -> list[str]:
    """설정된 모든 자격증명 값. 응답 가림에만 쓰고 밖으로 내보내지 않는다."""
    store = access.credential_store()
    values = {store.get(name) for source in access.SOURCES.values() for option in source.alternatives for name in option}
    return [v for v in values if v]


# @MX:ANCHOR: [AUTO] 모든 도구 응답이 지나는 자격증명 가림 경계
# @MX:REASON: 성공 응답·오류 본문·예외 문자열 어디에든 기관이 키를 반사할 수 있다 — 클라이언트별 가림은 빠지는 곳이 생긴다
def _run(fn: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    try:
        result = _bounded(fn())
    except Exception as exc:  # 도구는 예외로 서버를 죽이지 않는다.
        result = to_tool_result(exc)
    return redact(result, _secrets())


def _kipris() -> KiprisClient:
    return KiprisClient(_require("kipris-plus")["KIPRIS_API_KEY"], transport=_TRANSPORT)


def _odp() -> OdpClient:
    creds = _require("uspto-odp")
    return OdpClient(creds.get("USPTO_ODP_API_KEY") or creds["USPTO_API_KEY"], transport=_TRANSPORT)


def _tsdr() -> TsdrClient:
    creds = _require("uspto-tsdr")
    return TsdrClient(creds.get("USPTO_TSDR_API_KEY") or creds["USPTO_API_KEY"], transport=_TRANSPORT)


def _cached_auth(source_id: str, creds: dict[str, str], factory: Callable[[], Any]) -> Any:
    fingerprint = tuple(sorted(creds.items()))
    cached = _auth_cache.get(source_id)
    if cached and cached[0] == fingerprint:
        return cached[1]
    auth = factory()
    _auth_cache[source_id] = (fingerprint, auth)
    return auth


def _jpo_auth(creds: dict[str, str]) -> JpoAuth:
    return _cached_auth(
        "jpo",
        creds,
        lambda: JpoAuth(
            username=creds.get("JPO_API_USER", ""),
            password=creds.get("JPO_API_PASSWORD", ""),
            static_token=creds.get("JPO_ACCESS_TOKEN", ""),
            transport=_TRANSPORT,
        ),
    )


def _jpo() -> JpoClient:
    return JpoClient(_jpo_auth(_require("jpo")), transport=_TRANSPORT)


def _epo_auth(creds: dict[str, str]) -> EpoAuth:
    return _cached_auth(
        "epo-ops",
        creds,
        lambda: EpoAuth(creds["EPO_OPS_KEY"], creds["EPO_OPS_SECRET"], transport=_TRANSPORT),
    )


def _epo() -> EpoClient:
    return EpoClient(_epo_auth(_require("epo-ops")), transport=_TRANSPORT)


def _with(client_factory: Callable[[], Any], call: Callable[[Any], dict[str, Any]]) -> dict[str, Any]:
    def job() -> dict[str, Any]:
        client = client_factory()
        try:
            return call(client)
        finally:
            client.close()

    return _run(job)


# ------------------------------------------------------------------ 게이트
def _outcome(fn: Callable[[], Any]) -> dict[str, str]:
    """최소 호출 하나의 결과. 인증 오류·상품 기간 만료·서버 오류를 코드로 구분한다."""
    try:
        fn()
        return {"result": "ok"}
    except McpToolError as exc:
        return {"result": exc.code, "message": exc.message}
    except Exception as exc:  # noqa: BLE001 — 확인 단계는 무엇이 나든 보고만 한다.
        return {"result": "internal_error", "message": type(exc).__name__}


def _closing(client_factory: Callable[[], Any], call: Callable[[Any], Any]) -> Callable[[], Any]:
    def job() -> Any:
        client = client_factory()
        try:
            return call(client)
        finally:
            client.close()

    return job


def _verify(source_id: str) -> dict[str, Any]:
    """설정된 소스에 최소 호출을 보내 실제 연결을 확인한다. 값은 싣지 않는다."""
    if source_id == "kipris-plus":
        # 특허 상품과 상표 상품은 이용 신청·기간이 따로다 — 둘 다 확인한다.
        return {
            "patent_product": _outcome(_closing(_kipris, lambda c: c.patent_search(word="battery", num_of_rows=1))),
            "trademark_product": _outcome(
                _closing(_kipris, lambda c: c.trademark_search(trademark_name="test", num_of_rows=1))
            ),
        }
    if source_id == "uspto-odp":
        return _outcome(_closing(_odp, lambda c: c.patent_search(q="battery", limit=1)))
    if source_id == "uspto-tsdr":
        return _outcome(_closing(_tsdr, lambda c: c.trademark_status("78787878", "sn")))
    if source_id == "jpo":
        return _outcome(lambda: _jpo_auth(_require("jpo")).access_token())
    if source_id == "epo-ops":
        return _outcome(lambda: _epo_auth(_require("epo-ops")).access_token())
    return {"result": "unknown_source"}


@mcp.tool()
def ip_check_access(sources: list[str] | None = None, verify: bool = False) -> dict[str, Any]:
    """조사 전에 데이터 소스별 자격증명 설정 여부를 확인한다 (값은 절대 돌려주지 않음).

    Args:
        sources: 확인할 소스 ID 목록. kipris-plus · uspto-odp · uspto-tsdr · jpo · epo-ops.
            비우면 전부.
        verify: true면 설정된 소스에 최소 호출을 보내 실제 연결(인증 성공·상품 이용 기간 만료·서버 오류)을
            확인한다. 사용자가 "설정 완료"라고 한 뒤에 쓴다.

    Returns: ready, missing, 소스별 status(configured/missing)·registration_url·coverage·limits·tools,
        credential_file, how_to_set. verify=true면 소스별 verification 추가.
    """
    try:
        payload = access.status(sources)
        if verify:
            for entry in payload["sources"]:
                if entry["status"] == "configured":
                    entry["verification"] = _verify(entry["source"])
        return redact(payload, _secrets())
    except Exception as exc:  # noqa: BLE001
        return redact(to_tool_result(exc), _secrets())


# ------------------------------------------------------------------ KIPRIS
@mcp.tool()
def kipris_patent_search(
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
    """한국 특허·실용신안 검색 (KIPRIS Plus getAdvancedSearch).

    Args:
        word: 전체 필드 자유 검색어.
        invention_title / abstract / claim: 발명의 명칭·요약·청구범위 검색어.
        ipc_number: IPC 분류 (예: G06N).
        applicant / inventors / right_holder: 출원인·발명자·권리자.
        patent / utility: 특허·실용신안 포함 여부.
        status: 행정상태. 빈 값=전체, A=공개, C=취하, F=소멸, G=포기, I=무효, J=거절, R=등록.
        sort_spec: PD·AD·GD·OPD·FD·FOD·RD 중 하나 (공식 명세 값).
        page_no / num_of_rows: 페이지(1부터)·페이지 크기(최대 500).
        extra_params: 공식 명세에 있으나 여기서 따로 받지 않는 파라미터 (예: 날짜 범위 YYYYMMDD~YYYYMMDD).

    Returns: total_count(전체 건수), returned_count, items(발명의 명칭·출원번호·출원일·등록상태·IPC·요약 등), query.
    """
    return _with(
        _kipris,
        lambda c: c.patent_search(
            word=word, invention_title=invention_title, abstract=abstract, claim=claim,
            ipc_number=ipc_number, applicant=applicant, inventors=inventors, right_holder=right_holder,
            patent=patent, utility=utility, status=status, sort_spec=sort_spec, desc_sort=desc_sort,
            page_no=page_no, num_of_rows=num_of_rows, extra_params=extra_params,
        ),
    )


@mcp.tool()
def kipris_patent_detail(application_number: str) -> dict[str, Any]:
    """한국 특허·실용신안 서지 상세 (출원번호 기준, 하이픈 허용)."""
    return _with(_kipris, lambda c: c.patent_detail(application_number))


@mcp.tool()
def kipris_trademark_search(
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
    """한국 상표 검색 (KIPRIS Plus trademarkInfoSearchService getAdvancedSearch).

    Args:
        trademark_name: 상표명칭 검색. trademark_name_match: 상표명칭 일치 검색.
        free_search: 자유 검색. classification: 니스 류 (예: 35). similarity_code: 유사군 코드 (KIPRIS 유사군 코드표 기준).
        designated_goods: 지정상품. applicant_name / agent_name / right_holder: 출원인·대리인·등록권자.
        vienna_code: 도형 분류. application_date / registration_date: YYYYMMDD~YYYYMMDD.
        statuses: 권리상태 필터 — application·registration·refused·expiration·withdrawal·publication·cancel·abandonment.
            비우면 전부 포함 (공식 규칙상 하나 이상 true 필요).
        mark_types: trademark·serviceMark·trademarkServiceMark·businessEmblem·collectiveMark·geoOrgMark·
            internationalMark·certMark·geoCertMark. 비우면 전부.
        compositions: character·figure·compositionCharacter·figureComposition·sound·fragrance·color·dimension·
            colorMixed·hologram·motion·visual·invisible. 비우면 전부.
        page_no / num_of_rows: 페이지·페이지 크기(최대 500).
        extra_params: 공식 명세의 나머지 파라미터 (예: publicationDate, sortSpec).

    Returns: total_count, items(title·applicationNumber·applicationStatus·classificationCode·applicantName·
        regPrivilegeName·출원/등록일·drawing 이미지 주소 등), query.
    """
    return _with(
        _kipris,
        lambda c: c.trademark_search(
            trademark_name=trademark_name, trademark_name_match=trademark_name_match,
            free_search=free_search, classification=classification, similarity_code=similarity_code,
            designated_goods=designated_goods, applicant_name=applicant_name, agent_name=agent_name,
            right_holder=right_holder, vienna_code=vienna_code, application_date=application_date,
            registration_date=registration_date, statuses=statuses, mark_types=mark_types,
            compositions=compositions, page_no=page_no, num_of_rows=num_of_rows, extra_params=extra_params,
        ),
    )


@mcp.tool()
def kipris_trademark_detail(application_number: str) -> dict[str, Any]:
    """한국 상표 서지·행정처리 이력 상세 (출원번호 기준)."""
    return _with(_kipris, lambda c: c.trademark_detail(application_number))


# ------------------------------------------------------------------ USPTO
@mcp.tool()
def uspto_patent_search(
    q: str = "",
    filters: list[dict[str, Any]] | None = None,
    range_filters: list[dict[str, Any]] | None = None,
    sort: list[dict[str, Any]] | None = None,
    fields: list[str] | None = None,
    offset: int = 0,
    limit: int = 25,
) -> dict[str, Any]:
    """미국 특허 출원 검색 (USPTO Open Data Portal).

    Args:
        q: 검색식. 불리언(AND/OR/NOT)·와일드카드·`필드:값`·범위 `[a TO b]` 지원.
        filters: [{"name": 필드, "value": [값...]}]. range_filters: [{"field", "valueFrom", "valueTo"}].
        sort: [{"field", "order": "asc"|"desc"}]. fields: 돌려받을 필드 목록.
        offset / limit: 페이지 시작·크기(1~100).

    Returns: request(보낸 본문), data(ODP 원본 JSON — 총 건수와 출원 목록).
    """
    return _with(
        _odp,
        lambda c: c.patent_search(
            q=q, filters=filters, range_filters=range_filters, sort=sort, fields=fields, offset=offset, limit=limit
        ),
    )


@mcp.tool()
def uspto_patent_application(application_number: str) -> dict[str, Any]:
    """미국 특허 출원 메타데이터 (출원번호 기준, 예: 16123456 또는 16/123,456)."""
    return _with(_odp, lambda c: c.patent_application(application_number))


@mcp.tool()
def uspto_trademark_status(number: str, number_type: str = "sn") -> dict[str, Any]:
    """미국 상표 사건 상태 (USPTO TSDR, ST.96 XML을 구조화해 반환).

    USPTO는 상표 문자 검색 API를 제공하지 않는다. 후보는 USPTO Trademark Search 웹 화면에서 찾고,
    찾은 번호로 이 도구를 불러 상태·소유자·지정상품을 확인한다.

    Args:
        number: 사건 번호. 접두어 포함(sn78787878)도 허용.
        number_type: sn(일련번호·8자리) · rn(등록번호) · ref(참조번호) · ir(국제등록번호).
    """
    return _with(_tsdr, lambda c: c.trademark_status(number, number_type))


# ------------------------------------------------------------------ JPO
@mcp.tool()
def jpo_patent_progress(application_number: str, simple: bool = False) -> dict[str, Any]:
    """일본 특허 경과 정보 (출원번호 10자리: 서기 4자리+6자리, 예: 2020008423). simple=true면 간이 경과."""
    return _with(_jpo, lambda c: c.progress("patent", application_number, simple=simple))


@mcp.tool()
def jpo_patent_registration(application_number: str) -> dict[str, Any]:
    """일본 특허 등록 정보 (출원번호 10자리)."""
    return _with(_jpo, lambda c: c.registration("patent", application_number))


@mcp.tool()
def jpo_trademark_progress(application_number: str) -> dict[str, Any]:
    """일본 상표 경과 정보 (출원번호 10자리). 표시용 상표·음역·지정상품·권리자 포함."""
    return _with(_jpo, lambda c: c.progress("trademark", application_number))


@mcp.tool()
def jpo_trademark_registration(application_number: str) -> dict[str, Any]:
    """일본 상표 등록 정보 (출원번호 10자리)."""
    return _with(_jpo, lambda c: c.registration("trademark", application_number))


@mcp.tool()
def jpo_case_number_reference(right: str, kind: str, number: str) -> dict[str, Any]:
    """일본 사건 번호 상호 참조 — 공개·등록번호로 출원번호 등을 찾는다.

    Args:
        right: patent 또는 trademark.
        kind: patent는 application·publication·registration, trademark는 application·registration.
        number: 번호(숫자).
    """
    return _with(_jpo, lambda c: c.case_number_reference(right, kind, number))


@mcp.tool()
def jpo_applicant_lookup(right: str, name: str) -> dict[str, Any]:
    """일본 출원인·대리인 코드 조회 (정확한 이름 기준). right: patent 또는 trademark."""
    return _with(_jpo, lambda c: c.applicant_lookup(right, name))


# ------------------------------------------------------------------ EPO
@mcp.tool()
def epo_search(cql: str, start: int = 1, end: int = 25, with_biblio: bool = False) -> dict[str, Any]:
    """유럽·국제 공개 특허 검색 (EPO OPS, CQL).

    Args:
        cql: CQL 검색식. 예: ta="solid state battery" and pa="samsung" and pd>=2020
            (ta=명칭·요약, pa=출원인, ic/cpc=분류, pd=공개일).
        start / end: 결과 범위 (한 번에 최대 100건, 끝 값 2,000 이하).
        with_biblio: true면 서지 요약을 함께 받는다(응답이 커진다).
    """
    return _with(_epo, lambda c: c.search(cql, start=start, end=end, with_biblio=with_biblio))


@mcp.tool()
def epo_biblio(reference_type: str, number: str, input_format: str = "docdb") -> dict[str, Any]:
    """EPO 서지 정보. reference_type: publication·application·priority. input_format: docdb(EP.1000000.A1) 또는 epodoc(EP1000000)."""
    return _with(_epo, lambda c: c.biblio(reference_type, number, input_format))


@mcp.tool()
def epo_family(
    reference_type: str, number: str, input_format: str = "docdb", constituent: str = ""
) -> dict[str, Any]:
    """INPADOC 특허 패밀리. constituent: 빈 값·biblio·legal (legal이면 패밀리 구성원별 법적 상태 포함)."""
    return _with(_epo, lambda c: c.family(reference_type, number, input_format, constituent))


@mcp.tool()
def epo_legal(reference_type: str, number: str, input_format: str = "docdb") -> dict[str, Any]:
    """INPADOC 법적 상태 이력. 공식 법적 상태 표시는 지연될 수 있으므로 중요한 권리는 원등록부로 재확인한다."""
    return _with(_epo, lambda c: c.legal(reference_type, number, input_format))


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
