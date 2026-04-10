# MoAI Connectors Guide

MoAI 플러그인은 Cowork 공식 커넥터와 연동하여 외부 도구와 직접 상호작용할 수 있습니다.
커넥터는 무료이며, 한 번 인증하면 모든 세션에서 유지됩니다.

## 커넥터 설정 방법

1. Claude Cowork 좌측 메뉴 > Settings > Connectors
2. 원하는 도구 선택 > "Connect" 클릭
3. 해당 도구 계정으로 인증 (OAuth)
4. 연결 완료 — MoAI 스킬에서 즉시 사용 가능

## 플러그인별 권장 커넥터

### moai-content (콘텐츠)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **WordPress** | 블로그 포스트 직접 발행, 기존 글 수정 | 공식 커넥터 |
| **Canva** | 카드뉴스, SNS 이미지, 프레젠테이션 디자인 | 공식 커넥터 |
| post-bridge | 다중 플랫폼 동시 발행 (네이버, 티스토리) | 커스텀 MCP |
| typefully | 트위터/X 스레드 예약 발행 | 커스텀 MCP |

### moai-marketing (마케팅)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **Gmail** | 이메일 캠페인 발송, 시퀀스 관리 | 공식 커넥터 |
| **HubSpot** | CRM 연동, 리드 관리, 캠페인 추적 | 공식 커넥터 |
| **Canva** | SNS 이미지, 광고 소재 제작 | 공식 커넥터 |

### moai-schedules (스케줄)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **Google Calendar** | 일정 생성/조회, 자동 예약, 리마인더 | 공식 커넥터 |

### moai-product (제품)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **Notion** | 로드맵, PRD, 스프린트 보드 관리 | 공식 커넥터 |
| **Figma** | UX 리서치, 디자인 피드백, 핸드오프 | 공식 커넥터 |
| **Asana** / **Linear** / **Jira** | 이슈 트래킹, 스프린트 관리 | 공식 커넥터 |

### moai-office (문서)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **Google Drive** | Google Docs/Sheets 저장, 공유, 실시간 편집 | 공식 커넥터 |
| **Gmail** | 문서 이메일 발송, 첨부파일 관리 | 공식 커넥터 |
| **Notion** | 보고서/회의록/제안서를 Notion 페이지로 발행 | 공식 커넥터 |
| **Microsoft 365** | Outlook, OneDrive, SharePoint, Teams | 공식 커넥터 |

### moai-support (고객지원)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **Slack** | 티켓 알림, 팀 소통, 에스컬레이션 | 공식 커넥터 |
| **HubSpot** | 고객 이력 조회, 지원 티켓 관리 | 공식 커넥터 |

### moai-operations (운영)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| **Slack** | 결재 알림, 프로세스 소통 | 공식 커넥터 |
| **Notion** | SOP 문서, 운영 매뉴얼 관리 | 공식 커넥터 |
| **Asana** / **Jira** | 업무 트래킹, KPI 보고 | 공식 커넥터 |

### moai-business (비즈니스 전략)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| dart (DART OpenAPI) | 기업 공시 조회, 재무제표 분석 | 커스텀 MCP (API 키 필요) |

### moai-legal (법률)

| 커넥터 | 활용 | 유형 |
|--------|------|------|
| korean-law | 법령 검색, 판례 조회 | 커스텀 MCP (API 키 필요) |

### moai-finance, moai-hr, moai-education, moai-lifestyle, moai-career

현재 외부 커넥터 불필요. 향후 필요 시 추가.

---

## 커스텀 MCP 서버 설정

공식 커넥터가 아닌 커스텀 MCP 서버는 각 플러그인의 `.mcp.json`에 정의되어 있습니다.
API 키가 필요한 경우 환경변수로 설정합니다.

### DART API (moai-business)

1. [DART OpenAPI](https://opendart.fss.or.kr/) 가입 및 API 키 발급
2. `/moai apikey`로 등록 (글로벌 저장 — 모든 프로젝트에서 공유)
   - 또는 `/moai init` 시 Phase 3에서 입력

### 법령 정보 (moai-legal)

1. [국가법령정보센터 Open API](https://www.law.go.kr/LSO/main.do) 인증코드 발급
2. `/moai apikey`로 등록 (글로벌 저장)

### 이미지 생성 (moai-content)

1. Nano Banana API 키 발급
2. `/moai apikey`로 등록 (글로벌 저장)

---

## 공식 커넥터 전체 목록

Cowork에서 제공하는 50+개 커넥터 전체 목록은 아래에서 확인:
- Cowork 좌측 메뉴 > Settings > Connectors
- https://claude.com/connectors

---

Version: 1.0.0
Last Updated: 2026-04-10
