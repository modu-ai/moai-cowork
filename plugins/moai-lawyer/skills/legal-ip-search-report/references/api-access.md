# API 접근 게이트

조사할 소스를 정한 뒤 자격증명부터 확인합니다. 확인은 `moai-mcp-ip` 서버의 `ip_check_access` 도구로 하며, 이 도구는 값이 아니라 `configured` / `missing`만 돌려줍니다. 기관의 등록 정책·요금·호출 한도는 바뀔 수 있으니 실제 신청 전에 공식 안내를 다시 확인합니다.

상세 등록 절차와 자격증명 파일 형식의 정본은 플러그인 안의 `mcp-servers/moai-mcp-ip/CONNECTORS.md`입니다.

## 확인 순서

1. `ip_check_access(sources=["kipris-plus", "uspto-odp", "uspto-tsdr", "jpo", "epo-ops"])` — 필요한 것만 넣습니다.
2. `ready: false`면 `missing` 소스의 조사를 멈추고 아래 누락 안내를 합니다.
3. 사용자가 "설정 완료"라고 하면 `ip_check_access(sources=[...], verify=true)`로 연결을 확인합니다.
4. `verification.result` 판정:

| result | 뜻 | 할 일 |
|---|---|---|
| `ok` | 인증 성공 | 조사 시작 |
| `auth_error` | 키 오류, 권한 없음, KIPRIS 상품 이용 기간 만료 | 조사 결과가 아님. 기관 마이페이지에서 키·상품 신청 상태 확인 안내 |
| `upstream_error` | 기관 서버 오류, TLS 인증서 문제 | 잠시 뒤 재시도. 계속되면 해당 소스를 미조사로 기록 |
| `rate_limited` · `quota_exhausted` | 호출 한도 | 대기 또는 다음 날 재개. 결과 0건으로 취급하지 않음 |
| `setup_required` | 값이 없음 | 누락 안내 |

KIPRIS Plus는 `patent_product`와 `trademark_product`를 따로 돌려줍니다. 같은 키로 상표는 되고 특허는 기간 만료일 수 있습니다.

## 소스 표

| 소스 ID | 용도 | 자격증명 키 | 공식 등록 |
|---|---|---|---|
| `kipris-plus` | 한국 특허·실용신안·상표 검색·상세 | `KIPRIS_API_KEY` | [KIPRIS Plus 가입·신청](https://plus.kipris.or.kr/portal/main/contents.do?menuNo=210104) |
| `uspto-odp` | 미국 특허 검색·출원 메타데이터 | `USPTO_ODP_API_KEY` 또는 `USPTO_API_KEY` | [USPTO ODP Getting Started](https://data.uspto.gov/apis/getting-started) |
| `uspto-tsdr` | 미국 상표 사건 상태 | `USPTO_TSDR_API_KEY` 또는 `USPTO_API_KEY` | [USPTO API Key Manager](https://account.uspto.gov/api-manager/) |
| `jpo` | 일본 특허·상표 번호 기반 조회 | `JPO_API_USER` + `JPO_API_PASSWORD` | [JPO API 제공 안내](https://www.jpo.go.jp/system/laws/sesaku/data/api-provision.html) |
| `epo-ops` | 유럽·국제 특허 검색·패밀리·법적 상태 | `EPO_OPS_KEY` + `EPO_OPS_SECRET` | [EPO OPS](https://www.epo.org/en/searching-for-patents/data/web-services/ops) |

## API가 없는 영역

아래는 공식 무료 API가 없어 공개 웹 화면이 유일한 경로입니다. 키 부재를 우회하는 것이 아니므로 등록 안내 없이 진행하고, 보고서에 `LIMITED — 공식 API 미제공, 웹 화면 기반`으로 표시합니다.

| 영역 | 웹 화면 |
|---|---|
| 미국 상표 문자 검색 | [USPTO Trademark Search](https://tmsearch.uspto.gov/) — 찾은 일련번호는 `uspto_trademark_status`로 상태 확인 |
| 일본 키워드 검색(특허·상표) | [J-PlatPat](https://www.j-platpat.inpit.go.jp/) — 찾은 출원번호는 `jpo_*` 도구로 확인 |
| 국제 상표(마드리드) | [WIPO Madrid Monitor](https://www.wipo.int/madrid/monitor/) · WIPO Global Brand Database (자동 조회는 약관상 금지 — 사람이 직접 조회) |
| 유럽연합 상표 | [EUIPO eSearch](https://euipo.europa.eu/eSearch/) |

## 기관별 등록 요약

### KIPRIS Plus (한국)
1. 개인 또는 단체 회원으로 가입합니다.
2. Open API에서 특허 상품과 상표 상품을 **각각** 이용 신청합니다.
3. 승인·결제가 필요한 상품은 절차를 마칩니다. 월 1,000회까지 무료이고 이후 유료입니다.
4. 마이페이지 → APIKEY 관리에서 인증키를 확인합니다.

### USPTO (미국)
- **ODP(특허)**: USPTO.gov 계정 + 다중 인증 → ID.me 신원 확인(미국 밖 거주자는 영상 통화) → API 키 발급. 무료.
- **TSDR(상표 상태)**: USPTO.gov 계정으로 API Key Manager 로그인 → TSDR 키 신청.
- 두 키는 서로 다릅니다.

### JPO (일본)
1. JPO API 제공 안내에서 약관과 신청서를 확인하고 메일로 신청합니다. 무료입니다.
2. 발급받은 ID·비밀번호를 설정합니다. 조직당 ID는 하나이며, 개인 ID는 개인 용도로만 씁니다.

### EPO OPS (유럽·국제)
1. developers.epo.org에 가입하고 앱을 만들어 consumer key·secret을 받습니다.
2. 무료 등급은 주당 4GB까지입니다.

## 자격증명 넣는 곳

- **Claude 앱**: 플러그인 설정 화면의 입력 칸. 민감 항목은 운영체제 키체인에 보관됩니다.
- **Codex 앱·CLI (모든 환경 공통)**: 자격증명 파일
  - macOS: `~/.moai/mcp/ip.json`
  - Windows: `C:\Users\<사용자>\.moai\mcp\ip.json`
  - 쓰는 기관의 키 이름과 값만 JSON으로 적습니다. 형식은 CONNECTORS.md를 봅니다.

## 누락 안내 템플릿

> `[기관명]` API 자격증명이 설정되지 않아 `[국가·권리]` 조사를 시작하지 않았습니다.
> 1. `[공식 등록 주소]`에서 가입 → API 이용 신청 → 키 발급을 마쳐 주세요.
> 2. 키는 채팅에 붙여 넣지 말고, Claude 앱이면 플러그인 설정 화면의 `[키 이름]` 칸에, Codex 앱이면 자격증명 파일에 넣어 주세요.
> 3. "설정 완료"라고 알려 주시면 값은 보여 드리지 않은 채 연결만 확인하고 조사를 이어 가겠습니다.
> 4. 등록 없이 공개 웹 화면으로 제한 조사를 할 수도 있습니다. 이 경우 결과에 `LIMITED — API 미사용`이 붙고, 검색 재현·일괄 검증 범위가 줄어듭니다.

## 보안 규칙

- 키 값을 출력하는 명령을 실행하지 않고, 환경변수 목록을 통째로 출력하지 않습니다.
- 키 값을 보고서·증거대장·셸 기록·소스 코드·문서 속성에 적지 않습니다.
- 키는 있다/없다(`configured` / `missing`)로만 보고합니다.
- 인증 오류와 결과 0건을 구분합니다. 401·403·토큰 만료·상품 기간 만료는 조사 결과가 아닙니다.
- 사용자가 채팅에 키를 붙여 넣었다면 그 값을 어디에도 옮기지 않고, 설정 화면이나 자격증명 파일로 옮기도록 안내하며 필요하면 재발급을 권합니다.
