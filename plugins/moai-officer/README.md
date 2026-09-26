# 사무관 (moai-officer)

사무 문서 전담 AI 코워커입니다. 한국형 오피스 문서(HWPX·DOCX·XLSX·PPTX·PDF)와 HTML 리포트/슬라이드 생성, 공문서 파싱, 노션 템플릿·생산성 루틴을 위한 스킬을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

> **분리 안내**: 공공데이터 조회·데이터 분석·시각화는 `moai-analyst` 플러그인으로, 라이프스타일·자기계발 루틴은 `moai-coworker`로 분리되었습니다.

**이런 분께 추천**: 사무직 · 기획자 · 자영업 운영자

## 설치

Claude Cowork와 ChatGPT Work는 마켓플레이스 등록 권한과 경로가 다릅니다.

- **Claude Cowork**: Cowork 탭 → Customize → Plugins → Personal plugins의 **+** → Add marketplace → Add from a repository에서 `modu-ai/moai-cowork`를 추가한 뒤 **moai-officer**를 설치하세요.
- **ChatGPT Work**: 워크스페이스 관리자가 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져와야 합니다. 이용자는 권한이 부여된 뒤 Plugins에서 **moai-officer**를 찾아 Install plugin을 누르세요. 외부 서비스 연결은 별도 인증이 필요합니다.

> 앱별 정확한 클릭 경로와 잘 안 될 때 대처법은 [플러그인 설치와 관리](https://cowork.mo.ai.kr/plugins/install/)에 정리해 두었습니다.

## 스킬

호출 형식: `/moai-officer:<스킬명>` — 예: `/moai-officer:doc-hwp`. 자연어 요청("주간 보고서 HWPX로 만들어줘")으로도 자동 매칭됩니다.

### 문서 생성·파싱

| 스킬 | 역할 |
|------|------|
| `doc-hwp` | 아래아한글(.hwpx) 공문서·기안서·품의서·보고서 작성, HWP→HWPX 변환 |
| `doc-docx` | 워드(.docx) 보고서·계약서·제안서·공문서 생성 |
| `doc-xlsx` | 엑셀(.xlsx) KPI 대시보드·매출 분석표·예산표·간트차트 생성 |
| `doc-pptx` | 파워포인트(.pptx) 발표 슬라이드 디자인 |
| `doc-pdf` | HTML/Markdown/JSON/텍스트 → PDF 변환 (디자인 보존) |
| `doc-html-report` | 마크다운 보고서 → 단일 파일 HTML 리포트 |
| `doc-html-slide` | 자체 완결형 단일 파일 HTML 슬라이드 덱 (인라인 SVG 인포그래픽) |
| `doc-reader` | 한국 공문서(HWP·HWPX·PDF·XLSX·DOCX) 마크다운 파싱 — kordoc MCP |

### 문서 지원·생산성

| 스킬 | 역할 |
|------|------|
| `doc-design-library` | 설치된 `moai-designer`의 브랜드 디자인 시스템 토큰을 HTML 산출물에 적용 |
| `doc-notion-template` | 노션 업무관리·목표·회고 템플릿 구조 설계 |
| `setup-mcp-connector` | Drive·Notion·Higgsfield 등 외부 앱의 연결·인증 상태와 실제 도구 호출 확인 |
| `productivity-time` | 하루·주간 시간 설계 (블록식스·우선순위) |
| `productivity-briefing` | 업계 뉴스·시장 동향·오늘 할 일 아침 브리핑 |
| `doc-workflow` | 문서 입력·형식 확인과 전담 스킬 연결 |
| `doc-data-audit` | 문서 수치·표·차트·형식과 개인정보 검수 |

## MCP 연동

플러그인 루트 `.mcp.json`에 `kordoc` 서버가 선언되어 있습니다. 서버 선언, 앱에서의 도구 노출, 실제 문서 파싱 성공은 각각 확인해야 합니다.

| 서버 | 역할 | 키 발급 | 비고 |
|------|------|---------|------|
| `kordoc` | 제3자 한국 문서 파서. 지원 형식과 기능은 현재 연결의 도구 목록에서 확인 | 불필요 | `.mcp.json`에 `npx -y kordoc mcp`가 선언됨. 로컬 실행기와 실제 문서 파싱 성공은 앱에서 별도 확인. 관련 스킬: `doc-reader` |

> 공공데이터 MCP(korean-stats KOSIS · archhub 건축물대장 · dart 전자공시)는 `moai-analyst` 플러그인으로 이관되었습니다.

## Claude 에이전트

ChatGPT Work에서는 복합 문서 작업과 원자료 검수를 `doc-workflow`·`doc-data-audit` 스킬로 제공합니다.

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `doc-producer` | worker | 보고서·슬라이드·양식 문서·공문서 파싱 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → doc-* 문서 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 공공데이터 조사는 moai-analyst의 data-analyst로, 라이프스타일·자기계발은 moai-coworker로 인계. 문서 내 수치는 출처 인용 필수, 조회 실패 시 `[NOT_FOUND]` 명시 |
| `data-auditor` | read-only audit | 오피스 문서·포함 수치·표/차트-원데이터 정합·공문서 규격·계산을 회의적으로 재검증하는 감사 에이전트. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음. 공공데이터 출처 중심 감사는 moai-analyst의 data-provenance-auditor로 인계 |

## 라이선스

Apache-2.0 · © 2026 modu-ai (email@mo.ai.kr) — 산출물은 이용자 소유([LICENSE-OUTPUT.md](../../LICENSE-OUTPUT.md))
