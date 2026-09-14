# CONNECTORS — 특허·상표 공식 API 등록과 자격증명 설정

`moai-mcp-ip` 가 쓰는 네 기관의 공식 API를 등록하고 자격증명을 넣는 방법입니다. 필요한 나라만 등록해도 됩니다 — 등록하지 않은 소스의 도구는 크래시 없이 `setup_required` 와 등록 주소를 돌려줍니다.

> 기관의 가입 절차·요금·호출 한도는 바뀔 수 있습니다. 아래 내용은 2026-09-13에 공식 페이지에서 확인한 것이며, 신청 전에 링크의 최신 안내를 다시 확인하세요.

## 한눈에 보기

| 소스 ID | 기관 | 할 수 있는 것 | 못 하는 것 | 자격증명 키 |
|---|---|---|---|---|
| `kipris-plus` | KIPRIS Plus (한국) | 특허·실용신안 검색·상세, 상표 검색(표장명·류·유사군·출원인·권리상태)·상세 | — | `KIPRIS_API_KEY` |
| `uspto-odp` | USPTO Open Data Portal (미국) | 특허 출원 검색·메타데이터 | 상표 검색 | `USPTO_ODP_API_KEY` (또는 `USPTO_API_KEY`) |
| `uspto-tsdr` | USPTO TSDR (미국) | 번호로 상표 사건 상태 조회 | 상표 **문자 검색** (USPTO가 API를 제공하지 않음) | `USPTO_TSDR_API_KEY` (또는 `USPTO_API_KEY`) |
| `jpo` | 일본 특허청 特許情報取得API | 출원번호 기반 특허·상표 경과·등록 정보, 번호 참조, 출원인 코드 | 키워드 검색 | `JPO_API_USER` + `JPO_API_PASSWORD` |
| `epo-ops` | EPO Open Patent Services (유럽·국제) | CQL 검색, 서지, INPADOC 패밀리, 법적 상태 | 상표 | `EPO_OPS_KEY` + `EPO_OPS_SECRET` |

WIPO(PATENTSCOPE·Global Brand Database)는 무료 공개 API가 없습니다. PATENTSCOPE 웹 서비스는 유료 계약이고, Global Brand Database는 자동 조회를 약관으로 금지합니다. 그래서 이 서버에 포함하지 않았습니다.

## 1. KIPRIS Plus (한국)

1. [KIPRIS Plus](https://plus.kipris.or.kr/portal/main/contents.do?menuNo=210104)에서 개인 또는 단체 회원으로 가입합니다.
2. Open API 메뉴에서 필요한 데이터 상품을 **각각** 이용 신청합니다.
   - 특허: 「특허·실용신안 공개·등록공보」 계열 상품 (서비스 `patUtiModInfoSearchSevice`)
   - 상표: 「상표 출원 속보」 상품 (서비스 `trademarkInfoSearchService`)
3. 승인·결제가 필요한 상품은 절차를 마칩니다. 월 1,000회까지 무료이고 그 이상은 유료입니다([요금 안내](https://plus.kipris.or.kr/portal/use/paymentMmg.do?menuNo=210112)).
4. 마이페이지 → APIKEY 관리에서 인증키를 확인합니다.

**주의 — 상품마다 이용 기간이 따로입니다.** 같은 키라도 상표 상품은 되고 특허 상품은 `DEADLINE_HAS_EXPIRED_ERROR`(기간 만료)가 날 수 있습니다. `ip_check_access(verify=true)` 가 두 상품을 따로 확인해 줍니다.

## 2. USPTO (미국)

두 API의 키가 다릅니다.

### Open Data Portal — 특허

1. USPTO.gov 계정을 만들고 다중 인증(MFA)을 켭니다.
2. ID.me 신원 확인을 연결합니다. 미국 밖 거주자는 영상 통화로 확인합니다.
3. [ODP Getting Started](https://data.uspto.gov/apis/getting-started) 안내대로 API 키를 받습니다. 무료입니다.
4. 2026-08-18부터 계정 프로필 필수 항목이 늘었습니다. 빠지면 키가 막힐 수 있으니 프로필을 채워 두세요.

호출 한도: 같은 키로 동시 호출 1건, 429를 받으면 5초 이상 쉬었다가 재시도(서버가 자동 처리).

### TSDR — 상표 상태

1. USPTO.gov 계정으로 [API Key Manager](https://account.uspto.gov/api-manager/)에 로그인합니다.
2. TSDR API 키를 신청합니다.

호출 한도: 분당 60회(미 동부 밤 10시~새벽 5시는 120회).

**상표 문자 검색은 API가 없습니다.** 유사표장 후보는 [USPTO Trademark Search](https://tmsearch.uspto.gov/) 웹 화면에서 찾고, 찾은 일련번호로 `uspto_trademark_status` 를 불러 상태를 확인합니다.

## 3. JPO 特許情報取得API (일본)

1. [JPO API 제공 안내](https://www.jpo.go.jp/system/laws/sesaku/data/api-provision.html)에서 이용 약관과 신청서를 확인합니다.
2. 신청서를 안내된 메일 주소로 보냅니다. 무료입니다(통신비 제외).
3. JPO가 발급한 ID·비밀번호를 받습니다.

알아 둘 점:
- **조직당 ID는 하나**이고 개인 ID는 개인 용도로만 쓸 수 있습니다. 한 ID를 여러 사람이 나눠 쓰지 마세요.
- 번호로만 조회합니다. 후보 발굴은 [J-PlatPat](https://www.j-platpat.inpit.go.jp/) 웹 화면에서 합니다.
- 조회 종류마다 일일 상한이 있고 매일 0시에 초기화됩니다.
- 토큰은 서버가 메모리에서 발급·갱신합니다. 파일로 저장하지 않습니다.

## 4. EPO Open Patent Services (유럽·국제)

1. [EPO OPS 안내](https://www.epo.org/en/searching-for-patents/data/web-services/ops)에서 이용 조건을 확인합니다.
2. developers.epo.org에 가입하고 앱을 만들어 consumer key·secret을 받습니다.
3. 무료 등급은 주당 4GB까지입니다. 응답의 사용량 헤더를 `quota` 필드로 돌려줍니다.

## 자격증명 넣기

**키 값은 채팅에 붙여 넣지 마세요.** 대화 기록에 남습니다. 아래 두 방법 중 하나를 씁니다.

### 방법 1 — Claude 앱 설정 화면

Claude 데스크톱에서 플러그인 설정을 열면 입력 칸이 뜹니다. 민감 항목은 운영체제 키체인에 보관됩니다. 쓰지 않는 기관의 칸은 비워 둡니다.

### 방법 2 — 자격증명 파일 (Codex 앱·CLI 포함 모든 환경)

파일 위치:
- macOS: `~/.moai/mcp/ip.json`
- Windows: `C:\Users\<사용자>\.moai\mcp\ip.json`

내용 (쓰는 기관의 줄만 남깁니다):

```json
{
  "KIPRIS_API_KEY": "<KIPRIS Plus 인증키>",
  "USPTO_ODP_API_KEY": "<ODP API 키>",
  "USPTO_TSDR_API_KEY": "<TSDR API 키>",
  "JPO_API_USER": "<JPO ID>",
  "JPO_API_PASSWORD": "<JPO 비밀번호>",
  "EPO_OPS_KEY": "<EPO consumer key>",
  "EPO_OPS_SECRET": "<EPO consumer secret>"
}
```

파일 경로를 바꾸려면 환경변수 `IP_CREDENTIALS_FILE` 로 지정합니다.

### 확인

설정을 마친 뒤 코워커에게 "설정 완료"라고 말하면 `ip_check_access(verify=true)` 로 **값은 보여 주지 않은 채** 연결만 확인합니다. 결과는 `ok`(성공)·`auth_error`(키 오류나 상품 기간 만료)·`upstream_error`(기관 서버 문제)로 구분됩니다. 인증 오류와 "검색 결과 0건"은 다른 것입니다.

## 알려진 제약 (2026-09-13 확인)

- USPTO TSDR 서버의 TLS 인증서가 2026-09-12에 만료된 상태를 관측했습니다. 서버는 보안상 검증을 끄지 않으므로, USPTO가 갱신하기 전까지 `uspto_trademark_status` 가 인증서 오류를 돌려줄 수 있습니다.
- KIPRIS Plus는 오류도 HTTP 200으로 보냅니다. 서버가 응답 본문의 `successYN`·`resultCode` 로 판정합니다.
