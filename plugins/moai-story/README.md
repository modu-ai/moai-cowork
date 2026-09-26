# 스토리 크리에이터 (moai-story)

스토리/IP 창작 전담 AI 코워커입니다. 웹툰·웹소설·시나리오·콘티·표지·캐릭터 시트·IP 사업화(story-*) 스킬을 하나의 플러그인으로 제공합니다. 슬래시 명령을 외울 필요 없이 자연어로 요청하면 매칭되는 스킬이 자동 호출됩니다.

> **분리 안내**: 본 플러그인의 스토리 스킬들은 `moai-writer`에서 분리되었습니다(출판 book-* 스킬은 moai-writer에 잔류). 신규 호출은 `moai-story:<스킬명>` 네임스페이스를 사용하세요. 이미지 생성은 현재 앱의 기본 도구를 확인하고, Higgsfield를 지정했다면 이 플러그인의 공식 연결을 확인합니다.

**이런 분께 추천**: 웹툰/웹소설 창작자 · 시나리오 작가 · IP 콘텐츠 기획자

## 설치

Claude Cowork와 ChatGPT Work는 마켓플레이스 등록 권한과 경로가 다릅니다.

- **Claude Cowork**: Cowork → Customize → Plugins → Personal plugins → **+** → Add marketplace → Add from a repository에서 `modu-ai/moai-cowork`를 추가한 뒤 **moai-story**를 설치하세요.
- **ChatGPT Work**: 워크스페이스 관리자가 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져와야 합니다. 이용자는 권한이 부여된 뒤 Plugins에서 **moai-story**를 찾아 Install plugin을 누르세요. 외부 서비스 연결은 별도 인증이 필요합니다.

> 앱별 정확한 클릭 경로와 잘 안 될 때 대처법은 [플러그인 설치와 관리](https://cowork.mo.ai.kr/plugins/install/)에 정리해 두었습니다.

## 스킬 (계층별)

호출 형식: `/moai-story:<스킬명>` — 예: `/moai-story:story-webtoon-episode`. 자연어 요청("웹툰 회차 대본 써줘")으로도 자동 매칭됩니다.

### L0 — 진입 라우터

| 스킬 | 역할 |
|------|------|
| `story-project` | 작품 유형 분류 후 알맞은 story-* 파이프라인으로 라우팅하는 진입점 |

### L1 — 연재 상태 관리

| 스킬 | 역할 |
|------|------|
| `story-series-bible` | 연재 상태 원장 — 마스터 기획서 소유·에피소드 현황표 갱신으로 다회차 연속성 복원 |

### L2 — 규격 SSOT

| 스킬 | 역할 |
|------|------|
| `story-webtoon-spec` | 한국 웹툰 플랫폼 규격 단일 진실 원천 — 데뷔 경로·원고 규격·회차 분량·수익화 훅·용어 사전 |

### L3 — 서사 설계·집필

| 스킬 | 역할 |
|------|------|
| `story-webtoon-planner` | 웹툰 기획 — 세계관·연재구조 3분류·시리즈 아크·관통 주제·훅 전략 설계 |
| `story-webtoon-episode` | 웹툰 회차 — 회차 플롯·세로 스크롤 컷 분할·컷별 프레임 연출 지시 |
| `story-webnovel-planner` | 웹소설 기획 — 6개 플랫폼 회차 분량·결제·태그·독점 비교로 타깃 확정 |
| `story-webnovel-writer` | 웹소설 회차 집필 — 장르별 문법·회차 절단(클리프행어) 등급 설계 |
| `story-synopsis` | 영상 시놉시스 — 로그라인·기획의도·인물·구성, 편성/공모 제출 규격 |
| `story-screenplay` | 시나리오 대본 — S# 넘버·지문·대사를 한국 드라마·영화 관행으로 작성 |
| `story-ip-pitch` | IP 사업화 — 2차 저작 피칭 문서·판권 제안서, 표준계약·저작권 등록 개요 |

### L4 — 연출·작화·식자

| 스킬 | 역할 |
|------|------|
| `story-character-sheet` | 캐릭터 시트 — 비주얼 시트(외형 8항목)·일관성 앵커·Soul ID 참조 세트 사양 |
| `story-webtoon-lettering` | 웹툰 식자 — 말풍선 종류·서체 통일·SFX 스타일·2패스 오버레이 워크플로우 |
| `story-webtoon-art` | 웹툰 작화 프롬프트 — 화풍 앵커 고정·컷별 복붙 프롬프트·내용물 가드 |
| `story-conti` | 영상 콘티·스토리보드 — 프레임 분해·화각/앵글/전환, 드라마·영화·광고 프리셋 |
| `story-previz` | 시네마틱 프리비즈 — 카메라 무빙·렌즈·조명 지정 숏 리스트 |
| `story-cover-art` | 표지·썸네일 — 단행본/웹툰/웹소설 3분기 구도·시선 유도·제목 자리 |

### L5 — 검수 QC

| 스킬 | 역할 |
|------|------|
| `story-webtoon-qc` | 웹툰 산출 이미지 검수 — 결함 7종 점검·세로 스크롤 규격·일관성 앵커 위반 판정 |
| `story-continuity-audit` | 회차 간 인물·사건·설정, 플랫폼 규격과 IP 주장 검수 |

> **비고**: 이전 `story-ad-conti`(광고 콘티)는 `story-conti`의 광고 프리셋으로 통합되었습니다.

## 이미지·영상 생성 경로

생성 스킬은 프롬프트 조립과 연출 설계를 담당합니다. 이미지가 필요하면 현재 앱에 노출된 기본 이미지 도구를 먼저 확인합니다. OpenAI는 [ChatGPT Images 2.5가 ChatGPT Work에 제공된다](https://openai.com/index/introducing-chatgpt-images-2-5/)고 안내하지만, 현재 호출의 모델이 보이지 않으면 정확한 모델 사용을 단정하지 않습니다. Higgsfield 지정 시에는 현재 호스트의 공식 연결에서 이미지·영상 도구와 비용·권한을 확인합니다. [Higgsfield 안내](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-higgsfield-mcp)에 따르면 Claude는 공식 MCP를, ChatGPT는 Higgsfield 공식 플러그인을 사용하며, MCP 생성은 요금제와 관계없이 크레딧을 차감합니다. 영상 생성은 현재 앱 또는 연결에서 실제 도구가 제공될 때만 실행합니다.

ChatGPT Work에서 Higgsfield를 쓰려면 **Higgsfield 공식 플러그인을 별도로 설치하고 계정을 연결**한 뒤 생성 도구가 노출되는지 확인합니다. Story 플러그인의 `.mcp.json` 등록만으로 ChatGPT의 Higgsfield 인증·도구 사용이 완료되지는 않습니다. Claude Cowork에서는 Higgsfield 공식 MCP 연결과 계정 인증을 확인합니다.

- Higgsfield 등 유료 외부 생성은 현재 표시되는 비용을 알리고 필요한 승인을 받은 뒤 실행합니다.
- 선택한 도구가 없으면 생성 프롬프트만 제공하고 실제 이미지·영상이 만들어졌다고 표시하지 않습니다.

## Claude 에이전트

ChatGPT Work에서는 `story-project`가 작품 작업을 연결하고 `story-continuity-audit`이 서사·권리 근거를 검수합니다.

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `story-director` | worker | 웹툰·웹소설 에피소드, 시나리오, 콘티/프리비즈, 표지, IP 피칭 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → story-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 표절 금지·캐릭터/Soul-ID 연속성 보존·플랫폼/제작사 정보 출처 필수·생성 크레딧 사전 고지를 HARD 가드레일로 준수 |
| `story-continuity-auditor` | read-only audit | 스토리 산출물을 회의적으로 검증하는 **서사 연속성 검수** 에이전트 — 캐릭터·플롯·설정 연속성(Soul-ID 포함), 플랫폼 포맷 적합성, 표절/AI 티 위험, IP 권리/피칭 완결성. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 후속 검수 체인

모든 텍스트 산출물은 다음 검수 체인으로 마무리를 권장합니다.

- AI 티 제거 → `moai-coworker:ai-slop-reviewer` → `moai-writer:korean-humanize` → 최종 검수

## 라이선스

Apache-2.0 · © 2026 modu-ai (email@mo.ai.kr) — 산출물은 이용자 소유([LICENSE-OUTPUT.md](../../LICENSE-OUTPUT.md))
