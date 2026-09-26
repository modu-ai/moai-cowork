"""데이터 소스별 자격증명 게이트.

조사를 시작하기 전에 "필요한 키가 있는가"를 먼저 판정한다. 판정 결과는
`configured` / `missing` 두 값뿐이며, **키 값 자체는 어디에도 싣지 않는다.**

자격증명은 `moai_mcp_core.CredentialStore` 로 해석한다 — 환경변수 →
`~/.moai/mcp/ip.json` 순서. Claude·Codex 데스크톱 앱이 `${KEY}` 자리표시자를
그대로 넘기는 문제는 코어가 '값 없음'으로 처리한다.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from moai_mcp_core import CredentialStore

#: 자격증명 파일 슬러그 — `~/.moai/mcp/ip.json`.
SERVICE = "ip"
#: 자격증명 파일 경로를 바꿀 때 쓰는 환경변수.
CREDENTIALS_FILE_ENV = "IP_CREDENTIALS_FILE"


@dataclass(frozen=True)
class Source:
    """공식 데이터 소스 하나."""

    source_id: str
    label: str
    #: 허용되는 키 조합. 조합 하나라도 전부 채워지면 설정 완료로 본다.
    alternatives: tuple[tuple[str, ...], ...]
    registration_url: str
    #: 이 소스로 할 수 있는 것과 할 수 없는 것. 검색 계획을 세울 때 그대로 쓴다.
    coverage: str
    limits: str = ""
    tools: tuple[str, ...] = field(default_factory=tuple)


SOURCES: dict[str, Source] = {
    "kipris-plus": Source(
        source_id="kipris-plus",
        label="KIPRIS Plus (한국 특허청 산하 한국특허정보원)",
        alternatives=(("KIPRIS_API_KEY",),),
        registration_url="https://plus.kipris.or.kr/portal/main/contents.do?menuNo=210104",
        coverage=(
            "한국 특허·실용신안 검색과 서지 상세, 한국 상표 검색(표장명·류·유사군·출원인·권리상태)과 "
            "상표 서지·행정처리 이력. 데이터 상품별로 따로 이용 신청하므로 특허 상품과 상표 상품의 "
            "이용 기간이 다를 수 있다."
        ),
        limits="월 1,000회까지 무료, 이후 유료(요금은 KIPRIS Plus 안내 기준). 응답은 XML.",
        tools=(
            "kipris_patent_search",
            "kipris_patent_detail",
            "kipris_trademark_search",
            "kipris_trademark_detail",
        ),
    ),
    "uspto-odp": Source(
        source_id="uspto-odp",
        label="USPTO Open Data Portal (미국 특허)",
        alternatives=(("USPTO_ODP_API_KEY",), ("USPTO_API_KEY",)),
        registration_url="https://data.uspto.gov/apis/getting-started",
        coverage="미국 특허 출원 검색(불리언·필드·범위 조건)과 출원 메타데이터. 상표 문자 검색은 제공하지 않는다.",
        limits="동시 호출 1건. 429를 받으면 5초 이상 기다린 뒤 재시도. 주간 호출 한도 있음.",
        tools=("uspto_patent_search", "uspto_patent_application"),
    ),
    "uspto-tsdr": Source(
        source_id="uspto-tsdr",
        label="USPTO TSDR (미국 상표 사건 상태)",
        alternatives=(("USPTO_TSDR_API_KEY",), ("USPTO_API_KEY",)),
        registration_url="https://account.uspto.gov/api-manager/",
        coverage=(
            "일련번호·등록번호로 미국 상표 사건 상태 조회. USPTO는 상표 문자 검색 API를 공개하지 않으므로 "
            "유사표장 검색은 USPTO Trademark Search 웹 화면으로 수행하고 LIMITED로 기록한다."
        ),
        limits="분당 60회(야간 120회).",
        tools=("uspto_trademark_status",),
    ),
    "jpo": Source(
        source_id="jpo",
        label="JPO 特許情報取得API (일본 특허청)",
        alternatives=(("JPO_API_USER", "JPO_API_PASSWORD"), ("JPO_ACCESS_TOKEN",)),
        registration_url="https://www.jpo.go.jp/system/laws/sesaku/data/api-provision.html",
        coverage=(
            "일본 특허·상표의 출원번호 기반 경과·등록 정보, 번호 상호 참조, 출원인 코드 조회. "
            "키워드 검색은 제공하지 않으므로 후보 발굴은 J-PlatPat 웹 화면으로 하고 LIMITED로 기록한다."
        ),
        limits="ID별 일일 호출 상한(조회 종류마다 다름). 조직당 ID 1개.",
        tools=(
            "jpo_patent_progress",
            "jpo_patent_registration",
            "jpo_trademark_progress",
            "jpo_trademark_registration",
            "jpo_case_number_reference",
            "jpo_applicant_lookup",
        ),
    ),
    "epo-ops": Source(
        source_id="epo-ops",
        label="EPO Open Patent Services (유럽·국제 특허)",
        alternatives=(("EPO_OPS_KEY", "EPO_OPS_SECRET"),),
        registration_url="https://www.epo.org/en/searching-for-patents/data/web-services/ops",
        coverage="CQL 검색, 서지, INPADOC 패밀리, 법적 상태. 다수 국가의 공개 특허를 다룬다.",
        limits="무료 등급 주당 4GB. 검색은 페이지당 최대 100건, 누적 2,000건까지.",
        tools=("epo_search", "epo_biblio", "epo_family", "epo_legal"),
    ),
}


def credential_store() -> CredentialStore:
    return CredentialStore(SERVICE, env_var=CREDENTIALS_FILE_ENV)


def satisfied_option(source: Source, store: CredentialStore) -> tuple[str, ...] | None:
    """채워진 키 조합을 돌려준다. 없으면 None."""
    for option in source.alternatives:
        if all(store.get(name) for name in option):
            return option
    return None


def status(source_ids: list[str] | None = None) -> dict:
    """선택한 소스들의 설정 여부. 값은 절대 싣지 않는다."""
    store = credential_store()
    wanted = source_ids or list(SOURCES)
    unknown = [s for s in wanted if s not in SOURCES]
    results = []
    for source_id in wanted:
        if source_id not in SOURCES:
            continue
        source = SOURCES[source_id]
        results.append(
            {
                "source": source_id,
                "label": source.label,
                "status": "configured" if satisfied_option(source, store) else "missing",
                "accepted_keys": [" + ".join(option) for option in source.alternatives],
                "registration_url": source.registration_url,
                "coverage": source.coverage,
                "limits": source.limits,
                "tools": list(source.tools),
            }
        )
    missing = [r["source"] for r in results if r["status"] == "missing"]
    payload: dict = {
        "ready": not missing and not unknown,
        "missing": missing,
        "sources": results,
        "credential_file": str(store.path),
        "how_to_set": (
            "Claude 앱: 플러그인 설정 화면의 입력 칸(민감 항목은 키체인에 보관). "
            f"Codex 앱·CLI: 자격증명 파일 {store.path} 에 키 이름과 값을 JSON으로 저장. "
            "키 값은 채팅에 붙여 넣지 마세요."
        ),
    }
    if unknown:
        payload["unknown_sources"] = unknown
        payload["known_sources"] = list(SOURCES)
    return payload
