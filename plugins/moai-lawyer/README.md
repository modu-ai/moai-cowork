# 법무 담당 (moai-lawyer)

법무 전담 AI 코워커입니다. 계약 검토·NDA 트리아지·컴플라이언스 점검·법령/판례 리서치·특허 검색/분석·식약처 안전 기준 ·국내외 특허/상표 선행조사 등 법무 실무 스킬과 국가법령정보 MCP(korean-law)·특허/상표 공식 데이터 MCP(moai-mcp-ip) 연동을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

**이런 분께 추천**: 1인 사업자 · 스타트업 운영자 · 법무 담당자 없는 소규모 팀

> ⚠️ **법률 자문이 아닙니다.** 본 플러그인의 모든 산출물은 참고 자료이며 변호사의 법률 자문을 대체하지 않습니다. 계약 체결·소송 등 구속력 있는 의사결정 전에는 반드시 변호사와 상담하세요.

## 설치

Claude Cowork와 ChatGPT Work는 마켓플레이스 등록 권한과 경로가 다릅니다.

- **Claude Cowork**: Settings(또는 Plugins) → Marketplace → +에서 `modu-ai/moai-cowork`를 추가한 뒤 Plugins에서 **moai-lawyer**를 설치하세요.
- **ChatGPT Work**: 워크스페이스 관리자가 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져와야 합니다. 이용자는 권한이 부여된 뒤 Plugins에서 **moai-lawyer**를 찾아 Install plugin을 누르세요. 외부 서비스 연결은 별도 인증이 필요합니다.

> 앱별 정확한 클릭 경로와 잘 안 될 때 대처법은 [플러그인 설치와 관리](https://cowork.mo.ai.kr/plugins/install/)에 정리해 두었습니다.

## 스킬

호출 형식: `/moai-lawyer:legal-<스킬명>` — 예: `/moai-lawyer:legal-contract-review`. 자연어 요청("이 계약서 검토해줘")으로도 자동 매칭됩니다.

### 계약·문서 검토 (2종)

| 스킬 | 역할 |
|------|------|
| `legal-contract-review` | 계약서·이용약관·개인정보처리방침 분석/작성 — 민법·상법 기반 10대 리스크 패턴 + 수정 권고안 |
| `legal-nda-triage` | NDA(비밀유지계약서) 신속 검토 — 조항별 위험도 평가 + 수정 권고안 |

### 컴플라이언스·리스크 (2종)

| 스킬 | 역할 |
|------|------|
| `legal-compliance-check` | 규제 준수 점검·내부 감사·ESG 보고·인허가 서류 — 갭 분석 + 시정 계획 |
| `legal-legal-risk` | 기업 법적 리스크 분석·IP 전략 — 리스크 매트릭스 + 대응 액션 플랜 |

### 법령·판례 리서치 (1종)

| 스킬 | 역할 |
|------|------|
| `legal-law-research` | 법령·판례·행정규칙·조약·해석례 원문 조회 + 인용 검증(환각방지)·판례 생사 확인·행위시법 판단 (korean-law MCP) |

### 특허·상표

| 스킬 | 역할 |
|------|------|
| `legal-ip-search-report` | 한국·미국·일본·유럽 공식 DB로 상표 선행검색·특허 선행기술/권리상태 조사 → 검색 로그·위험 평가·출원 전략 보고서. API 키 확인이 먼저, 없으면 등록 안내 |
| `legal-patent-search` | KIPRIS Plus 한국 특허·실용신안·상표 검색 + 출원 현황 정리 (moai-mcp-ip) |
| `legal-patent-analyzer` | 특허 동향 보고서·선행기술 조사·FTO(침해 가능성) 분석·출원서 초안 |

### 행정·안전 기준 (2종)

| 스킬 | 역할 |
|------|------|
| `legal-mfds-safety` | 식약처(MFDS) 의약품·식품 공식 안전 정보 조회 (인정현황·회수·판매중지 등) |
| `legal-iros-registry-automation` | 인터넷등기소(IROS) 등기부등본 일괄 발급 보조 — 열람·저장·종합 리포트 |

## MCP 연동: korean-law (국가법령정보)

Claude Cowork는 플러그인 루트 `.mcp.json`의 공식 hosted 서버를 사용합니다. ChatGPT Work는 `.codex-plugin/plugin.json`의 공식 `korean-law-mcp` 패키지를 로컬에서 실행합니다. 법령·판례·행정규칙·자치법규·조약·해석례 조회와 인용 검증 도구를 사용할 수 있으며, 사용 가능한 도구는 현재 연결에서 확인합니다.

| 앱 | 실행 경로 | 키 입력 |
|------|-----------|---------|
| Claude Cowork | 공식 hosted 서버 `mcp.gomdori.app/law` | 플러그인 설치 화면의 `KOREAN_LAW_OC` 입력란 |
| ChatGPT Work | 공식 `korean-law-mcp` 패키지 (`uv`·Node.js 20.19 이상 필요) | `~/.moai/mcp/korean-law.json`의 `LAW_OC` |

**OC 키 발급**: [law.go.kr](https://www.law.go.kr) 국가법령정보 Open API에서 발급합니다. Claude에서는 앱의 민감정보 입력란에 넣으세요. ChatGPT Work에서는 본인 컴퓨터의 `korean-law.json`에 `{"LAW_OC":"발급받은_키"}`를 저장합니다. Windows 경로는 `C:\\Users\\사용자이름\\.moai\\mcp\\korean-law.json`입니다. 키를 채팅이나 저장소에 넣지 마세요. 연결 후 법령 검색 도구가 실제로 응답하는지 확인하세요.

## MCP 연동: moai-mcp-ip (특허·상표 공식 데이터)

특허청·USPTO·일본 특허청·EPO 모두 공식 MCP를 제공하지 않아 직접 만든 서버입니다(`mcp-servers/moai-mcp-ip`). 조사 전에 `ip_check_access`로 기관별 자격증명을 확인하며, 키 값은 어떤 응답·로그에도 남기지 않습니다.

| 소스 | 할 수 있는 것 | 자격증명 |
|------|---------------|----------|
| KIPRIS Plus (한국) | 특허·실용신안·상표 검색과 상세 | `KIPRIS_API_KEY` |
| USPTO ODP (미국) | 특허 출원 검색·메타데이터 | `USPTO_ODP_API_KEY` |
| USPTO TSDR (미국) | 상표 사건 상태 (문자 검색 API는 USPTO가 제공하지 않음) | `USPTO_TSDR_API_KEY` |
| JPO (일본) | 출원번호 기반 특허·상표 경과·등록 정보 | `JPO_API_USER` + `JPO_API_PASSWORD` |
| EPO OPS (유럽·국제) | 특허 검색·서지·패밀리·법적 상태 | `EPO_OPS_KEY` + `EPO_OPS_SECRET` |

필요한 기관만 등록하면 됩니다. 키는 채팅에 붙여 넣지 말고 Claude 앱은 플러그인 설정 화면에, Codex 앱은 자격증명 파일(macOS `~/.moai/mcp/ip.json`, Windows `C:\Users\<사용자>\.moai\mcp\ip.json`)에 넣습니다. 기관별 가입 절차는 [CONNECTORS.md](mcp-servers/moai-mcp-ip/CONNECTORS.md)에 있습니다.

## Claude 에이전트

ChatGPT Work에서는 복합 법무 조사와 근거 검수를 `legal-workflow`·`legal-evidence-audit` 스킬로 제공합니다. 법령·판례 도구가 연결되지 않으면 검증되지 않은 인용을 확정하지 않습니다.

| ChatGPT 스킬 | 역할 |
|-------------|------|
| `legal-workflow` | 문서·관할·적용 시점을 확인하고 전담 법무 스킬을 연결 |
| `legal-evidence-audit` | 인용 기록·적용 법령·위험 등급을 원자료와 대조 |

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `legal-researcher` | worker | 계약 검토·컴플라이언스·법령/판례 리서치·특허 분석 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → legal-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 모든 법령·판례 인용은 korean-law MCP로 검증하며, 산출물에 "법률 자문 아님" 고지를 항상 포함 |
| `risk-auditor` | read-only audit | 인용 실존·판례 생사·리스크 등급 논리·누락 쟁점·고지 문구를 회의적으로 재검증하는 감사 에이전트. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 이관 안내

본 플러그인의 법무 스킬은 기존 통합 플러그인(moai-coworker)의 legal 카테고리에서 전담 플러그인으로 이관되었습니다. 기존 `moai-lawyer:legal-*` 호출 경로 대신 `moai-lawyer:legal-*` 네임스페이스를 사용하세요.

## 라이선스

Apache-2.0 · © 2026 modu-ai (email@mo.ai.kr) — 산출물은 이용자 소유([LICENSE-OUTPUT.md](../../LICENSE-OUTPUT.md))
