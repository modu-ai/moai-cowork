# 셀러 (moai-seller)

이커머스 셀러 전담 AI 코워커입니다. 스마트스토어·아임웹·카페24 MCP 연동과 상세페이지·마켓플레이스·광고·CRM 등 커머스 실무 스킬을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다. VOC 분류(`cs-voc-triage`)와 채널 메시지(`cs-channel-message`)는 `moai-cs`(CS매니저)로 이관되었습니다.

**이런 분께 추천**: 온라인 셀러 · 이커머스 운영자 · 1인 브랜드 대표

## 설치

Claude Cowork와 ChatGPT Work는 마켓플레이스 등록 권한과 경로가 다릅니다.

- **Claude Cowork**: Cowork → Customize → Plugins → Personal plugins → **+** → Add marketplace → Add from a repository에서 `modu-ai/moai-cowork`를 추가한 뒤 **moai-seller**를 설치하세요.
- **ChatGPT Work**: 워크스페이스 관리자가 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져와야 합니다. 이용자는 권한이 부여된 뒤 Plugins에서 **moai-seller**를 찾아 Install plugin을 누르세요. 외부 서비스 연결은 별도 인증이 필요합니다.

> 앱별 정확한 클릭 경로와 잘 안 될 때 대처법은 [플러그인 설치와 관리](https://cowork.mo.ai.kr/plugins/install/)에 정리해 두었습니다.

이미지 생성은 현재 앱의 이미지 도구를 확인합니다. [OpenAI는 Images 2.5가 ChatGPT Work에 제공된다고 안내](https://openai.com/index/introducing-chatgpt-images-2-5/)하지만, 현재 호출에서 정확히 어떤 모델을 썼는지는 도구에 표시될 때만 확정합니다. Higgsfield를 요청하면 Claude Cowork에서는 공식 MCP 연결과 계정 인증을, ChatGPT Work에서는 **Higgsfield 공식 플러그인의 별도 설치·인증**과 도구 노출을 확인합니다. Higgsfield는 생성 시 크레딧을 차감하므로 비용을 알리고 승인받은 뒤 호출합니다. 상품 참조 사진은 채팅 첨부만으로 생성 도구에 전달되지 않으므로 공식 업로드 창의 완료를 확인합니다. [Higgsfield 공식 연결 안내](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent)를 따릅니다.

## 스킬

호출 형식: `/moai-seller:commerce-<스킬명>` — 예: `/moai-seller:commerce-detail-page-planner`. 자연어 요청("우리 제품 상세페이지 기획해줘")으로도 자동 매칭됩니다.

### 상세페이지

| 스킬 | 역할 |
|------|------|
| `commerce-detail-page-planner` | 상세페이지 구조·설득 흐름 기획 |
| `commerce-detail-page-copy` | 상세페이지 카피라이팅 |
| `commerce-detail-page-image` | 상세페이지 이미지 구성 설계 |
| `commerce-product-detail` | 상품 상세 정보 구성 |
| `commerce-product-naming` | 상품명·검색 키워드 네이밍 |
| `commerce-product-image-pipeline` | 상품 이미지 제작 파이프라인 |
| `commerce-product-photo-brief` | 상품 촬영 브리프 작성 |

### 마켓플레이스

| 스킬 | 역할 |
|------|------|
| `commerce-marketplace-naver` | 네이버 스마트스토어 입점·운영 |
| `commerce-marketplace-coupang` | 쿠팡 입점·운영 |
| `commerce-marketplace-crowdfunding` | 와디즈 등 크라우드펀딩 론칭 |
| `commerce-marketplace-curation` | 큐레이션 커머스(카카오 등) 입점 |
| `commerce-marketplace-d2c` | 자사몰(D2C) 구축·운영 전략 |

### 광고·프로모션

| 스킬 | 역할 |
|------|------|
| `commerce-marketplace-coupang-ads` | 쿠팡 광고 운영 |
| `commerce-marketplace-naver-ads` | 네이버 검색광고(쇼핑검색·파워링크·브랜드검색·GFA) 운영 |
| `commerce-coupang-ad-optimizer` | 쿠팡 광고 최적화 |
| `commerce-promotion-planner` | 프로모션·할인 기획 |
| `commerce-live-commerce` | 라이브커머스 기획·운영 |
| `commerce-influencer-collab` | 인플루언서 협업 설계 |
| `commerce-early-fan-builder` | 초기 팬덤 구축 |
| `commerce-season-calendar` | 시즌·이벤트 캘린더 운영 |

### CRM·구독

| 스킬 | 역할 |
|------|------|
| `commerce-repurchase-timer` | 재구매 주기 기반 리텐션 설계 |
| `commerce-subscription-strategist` | 구독 모델 전략 |

> 채널 메시지(`cs-channel-message`)·VOC 분류(`cs-voc-triage`)는 `moai-cs`(CS매니저)로 이관되었습니다.

### 전략·분석

| 스킬 | 역할 |
|------|------|
| `commerce-integrated-strategy` | 커머스 통합 전략 수립 |
| `commerce-market-research` | 시장·경쟁 조사 |
| `commerce-jtbd-persona` | JTBD 기반 고객 페르소나 |
| `commerce-ltv-cac-architect` | LTV/CAC 단위경제 설계 |
| `commerce-margin-calculator` | 마진·손익 계산 |
| `commerce-morning-brief` | 셀러 모닝 브리프 |
| `commerce-automation-audit` | 운영 자동화 진단 |
| `commerce-message-compliance-kr` | 정통망법 메시지 발송 규제(스팸) 게이트 |
| `commerce-ad-claim-compliance-kr` | 표시광고법·식약처·전상법 광고 문구 검증 게이트 |
| `commerce-workflow` | 상품·채널 자료 확인과 복합 판매 작업 연결 |
| `commerce-margin-audit` | 비용·할인·마진·채널 제약 재검산 |

## MCP 연동

플러그인 루트 `.mcp.json`에는 판매자 운영용 자체 MCP 서버 세 개와 카페24 공식 카탈로그, Higgsfield 공식 연결이 선언돼 있습니다. 자체 서버의 자격증명은 앱의 연결 설정에 입력하고 파일에는 적지 않습니다. 공식 연결은 해당 서비스의 계정 인증을 완료해야 사용할 수 있습니다.

| 서버 | 플랫폼 | 필요 환경변수 | 상태 |
|------|--------|---------------|------|
| `moai-mcp-smartstore` | 네이버 스마트스토어 | `NAVER_COMMERCE_CLIENT_ID`, `NAVER_COMMERCE_CLIENT_SECRET`, `NAVER_COMMERCE_ACCOUNT_ID`, `NAVER_COMMERCE_TYPE` | 소스 포함, 앱 연결은 미검증 |
| `moai-mcp-imweb` | 아임웹 OPEN API v3 | `IMWEB_CLIENT_ID`, `IMWEB_CLIENT_SECRET`, `IMWEB_ACCESS_TOKEN`, `IMWEB_REFRESH_TOKEN`, `IMWEB_UNIT_CODE` | 소스 포함, 앱 연결은 미검증 |
| `moai-mcp-cafe24` | 카페24 Admin API + Analytics | `CAFE24_MALL_ID`, `CAFE24_CLIENT_ID`, `CAFE24_CLIENT_SECRET`, `CAFE24_ACCESS_TOKEN`, `CAFE24_REFRESH_TOKEN` | 소스 포함, 앱 연결은 미검증 |

- MCP 실행에는 `uv`가 필요합니다. 실제 앱 설치·인증·기동은 운영체제별로 확인해야 합니다.
- 자격증명 발급 절차: 각 서버 디렉토리의 `CONNECTORS.md` / `README.md` 참고
- 경로는 `${CLAUDE_PLUGIN_ROOT}` 기준이므로 marketplace 설치(캐시 복사) 환경에서도 동작합니다

## Claude 에이전트

ChatGPT Work에서는 복합 상품 운영과 수익성 검수를 `commerce-workflow`·`commerce-margin-audit` 스킬로 제공합니다.

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `listing-builder` | worker | 상세페이지·리스팅·광고·CRM 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → commerce-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 외부 발신·플랫폼 상태 변경은 사용자 승인 없이 절대 수행하지 않음 |
| `margin-auditor` | read-only audit | 마진 계산·리스팅·캠페인 플랜을 회의적으로 재검산하는 감사 에이전트. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 라이선스

Apache-2.0 · © 2026 modu-ai (email@mo.ai.kr) — 산출물은 이용자 소유([LICENSE-OUTPUT.md](../../LICENSE-OUTPUT.md))
