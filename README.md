# moai-cowork-plugins

Claude Cowork를 위한 도메인 전문가 AI 플러그인 마켓플레이스.

14개 독립 플러그인으로 비즈니스 전략, 마케팅, 법률, 재무, 인사, 콘텐츠, 운영, 교육, 라이프스타일, 제품, 고객지원, 문서생성, 스케줄 관리를 지원합니다.

## 플러그인 카탈로그

| 플러그인 | 설명 | 스킬 수 |
|---------|------|:-------:|
| [moai-core](./moai-core/) | 도메인 AI 라우터, 초기화, 자가학습 엔진 | 1 |
| [moai-business](./moai-business/) | 비즈니스 전략 — 사업계획서, 시장조사, 재무모델 | 4 |
| [moai-marketing](./moai-marketing/) | 마케팅 — 네이버/카카오 SEO, SNS, 캠페인 | 5 |
| [moai-legal](./moai-legal/) | 법률 — 계약서 검토, 컴플라이언스, NDA | 4 |
| [moai-finance](./moai-finance/) | 재무/세무 — 원천징수, 부가세, K-IFRS | 4 |
| [moai-hr](./moai-hr/) | 인사/노무 — 근로계약서, 4대보험, 채용 | 4 |
| [moai-content](./moai-content/) | 크리에이티브 콘텐츠 — 카드뉴스, 블로그, 뉴스레터 | 7 |
| [moai-operations](./moai-operations/) | 운영 — 결재, 조달, SOP, 벤더 관리 | 3 |
| [moai-education](./moai-education/) | 교육/연구 — 강의설계, 논문, 교육과정 | 3 |
| [moai-lifestyle](./moai-lifestyle/) | 라이프스타일 — 여행, 건강, 웨딩/이벤트 | 3 |
| [moai-product](./moai-product/) | 제품 혁신 — PM 로드맵, UX 리서치, 스펙 | 3 |
| [moai-support](./moai-support/) | 고객 지원 — 티켓 분류, KB 문서, 에스컬레이션 | 4 |
| [moai-office](./moai-office/) | 문서 생성 — PPT, DOCX, XLSX, HWPX | 4 |
| [moai-schedules](./moai-schedules/) | 스케줄 관리 — 반복 업무 자동 실행 | 3 |

## 설치

Claude Cowork에서 플러그인 설치:

1. Settings > Plugins에서 GitHub 저장소 URL 입력
2. 원하는 플러그인 선택하여 설치
3. `/moai init`으로 초기 설정

또는 `.plugin` 파일을 직접 설치:

1. [Releases](https://github.com/modu-ai/cowork-plugins/releases)에서 `moai-cowork.plugin` 다운로드
2. Claude Desktop → Cowork → 플러그인 관리 → **파일에서 설치**

## 에이전트 공유 호출

플러그인 간 에이전트를 공유 호출할 수 있습니다:

| 에이전트 | 소속 | 공유 대상 |
|---------|------|----------|
| quality-evaluator | moai-core | 전 플러그인 |
| korean-tone-reviewer | moai-hr | moai-support, moai-business 등 |
| document-generator | moai-office | moai-business, moai-legal 등 |
| format-converter | moai-office | 전 플러그인 |
| compliance-checker | moai-legal | moai-finance, moai-hr 등 |
| market-researcher | moai-business | moai-product 등 |
| content-creator | moai-marketing | moai-business 등 |

## 라이선스

MIT — [모두의AI (modu-ai)](https://github.com/modu-ai)
