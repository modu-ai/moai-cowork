# 데스크톱 앱 현장 확인표

기준 브랜치: `WT-cowork-desktop-portability`. 정적 조사와 OS별 MCP 자동 테스트는 `reports/desktop-portability-audit-20260924.md`에 있다. 아래 항목은 **실제 앱에서 아직 실행하지 않았다**. 결과를 적을 때 앱 버전·운영체제·플러그인 버전·화면에 보인 도구 이름과 실행 시각을 함께 남긴다.

[검사 SHA `dfb32cbc`의 MCP 교차 플랫폼 CI](https://github.com/modu-ai/moai-cowork/actions/runs/36086427714)는 macOS·Windows·Ubuntu 작업 30개가 성공했다. 이 결과는 아래 앱 현장 확인을 대체하지 않는다.

| 호스트 | macOS | Windows | Linux |
|---|---|---|---|
| Claude Cowork | 미실행 — UI 도구에서 창 확인 불가 | 미실행 — 기기 없음 | 미실행 — 기기 없음, 베타 |
| ChatGPT Work | 미실행 — UI 도구 접근 제한 | 미실행 — 기기 없음 | 미실행 — 기기 없음, 공개 미리보기 |

Linux 지원 배포판과 기능 제한은 [Claude Desktop 설치 안내](https://support.claude.com/en/articles/10065433-install-claude-desktop) 및 [ChatGPT 릴리스 노트](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)의 현재 내용을 확인한다. 앱 지원은 이 저장소 플러그인의 설치·도구 호출 성공을 보장하지 않는다.

ChatGPT 쪽은 데스크톱 앱의 **Work 모드 새 대화**에서 검사한다. Codex 모드에서 보인 스킬·도구나 이미지 생성 결과를 Work 모드의 `PASS`로 옮기지 않는다. [OpenAI 플러그인 안내](https://learn.chatgpt.com/docs/plugins)는 두 모드의 플러그인 사용을 설명하지만, 실제 설치·연결 상태는 각 대화에서 확인해야 한다.

## 플러그인별 앱 검사

아래 목록은 `.claude-plugin/marketplace.json`에 등록된 플러그인과 각 플러그인의 `skills/*/SKILL.md`, `.mcp.json`, 두 호스트의 `plugin.json`을 읽어 만든 2026-09-25 정적 스냅샷이다. 버전 열은 이 작업 트리의 마켓플레이스 값이며, 앱 검사 직전 다시 대조한다. `예시 스킬`은 설치 후 목록에서 찾을 항목이며, 여기 적혔다는 사실만으로 앱에서 실행된 것은 아니다. MCP 열은 플러그인 선언에 포함된 서버 키다. `—`는 선언이 없다는 뜻이다. ChatGPT의 `moai-seller`에서 Higgsfield를 쓰려면 별도 공식 플러그인 설치·인증이 필요하다.

| 플러그인 | 버전 | 예시 스킬 | Claude MCP | ChatGPT MCP |
|---|---|---|---|---|
| `moai-coworker` | 1.2.27 | `ai-diagnostic` | `dart` | `dart` |
| `moai-writer` | 1.5.13 | `book-author-bio` | — | — |
| `moai-story` | 1.2.4 | `story-ad-conti` | `higgsfield` | `higgsfield` |
| `moai-marketer` | 1.2.22 | `content-blog` | `meta-ads`, `typefully`, `wordpress` | 동일 |
| `moai-media` | 3.3.12 | `media-asset-production` | `ElevenLabs`, `higgsfield`, `moai-mcp-openai` | 동일 |
| `moai-seller` | 1.4.31 | `commerce-ad-claim-compliance-kr` | `moai-mcp-smartstore`, `moai-mcp-imweb`, `moai-mcp-cafe24`, `cafe24-catalog-mcp`, `higgsfield` | 앞의 네 서버 |
| `moai-officer` | 1.3.7 | `doc-data-audit` | `kordoc` | `kordoc` |
| `moai-analyst` | 1.3.6 | `data-building-ledger` | `korean-stats`, `archhub`, `dart` | 동일 |
| `moai-lawyer` | 1.4.16 | `legal-compliance-check` | `korean-law`, `moai-mcp-ip` | 동일 |
| `moai-accountant` | 1.3.8 | `finance-audit` | `dart` | `dart` |
| `moai-recruiter` | 2.0.8 | `hr-draft-offer` | — | — |
| `moai-cs` | 1.2.8 | `cs-channel-message` | — | — |
| `moai-consultant` | 1.2.7 | `consult-brief` | — | — |
| `moai-career` | 1.2.6 | `career-claim-audit` | — | — |
| `moai-tutor` | 1.3.4 | `education-assessment-audit` | — | — |
| `moai-designer` | 1.4.70 | `design-brand-system` | `higgsfield` | `higgsfield` |
| `moai-pm` | 1.6.7 | `project` | — | — |
| `moai-threads-poster` | 2.0.5 | `instagram-comments` | `moai-mcp-threads-poster` | 동일 |

각 칸은 **설치 화면의 플러그인 버전 확인 → 예시 스킬 노출 확인 → 선언된 MCP 또는 연결 앱의 도구 노출 확인**을 한 앱·OS에서 마쳤을 때만 `PASS`로 바꾼다. 서버가 없는 플러그인은 마지막 단계가 해당 없음이다. 연결 도구의 실제 동작은 별도 호출 결과로 기록한다. 앱 설치·로그인부터 막혔다면 `BLOCKED`와 사유를 적는다. 지금까지 아래 칸은 모두 `NOT-RUN`이다.

| 플러그인 | Claude macOS | Claude Windows | Claude Linux | ChatGPT Work macOS | ChatGPT Work Windows | ChatGPT Work Linux |
|---|---|---|---|---|---|---|
| `moai-coworker` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-writer` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-story` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-marketer` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-media` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-seller` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-officer` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-analyst` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-lawyer` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-accountant` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-recruiter` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-cs` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-consultant` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-career` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-tutor` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-designer` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-pm` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |
| `moai-threads-poster` | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN | NOT-RUN |

`moai-media`의 ChatGPT 선언에는 `higgsfield` 서버 키가 있고, 사용 안내에는 Higgsfield 공식 플러그인의 별도 설치가 나온다. 앱에서 어느 경로가 실제로 인증·도구 노출까지 되는지 확인한 뒤 기록한다. 두 선언의 존재만으로 중복 설치 필요 여부나 결함을 판정하지 않는다.

## 각 앱·OS에서 기록할 항목

1. 앱 UI에서 `moai-story`와 `moai-seller`를 설치한다. Claude는 Cowork, ChatGPT는 Work 모드의 새 대화를 연다. 플러그인 카드에 표시된 버전과 스킬·MCP 또는 연결 앱 목록을 기록한다. Claude와 ChatGPT의 설치 절차는 [설치와 관리](../www/content/plugins/install.md)에 있다.
2. 해당 새 대화에서 `story-webtoon-art`에 **가상 캐릭터의 단일 컷 프롬프트**를 요청한다. 이미지 도구를 사용했다면 실제 파일·도구 이름·화면에 표시된 모델을 기록한다. 모델이 숨겨져 있으면 “이미지 생성 확인, Images 2.5 정확한 모델 미확인”으로 기록한다. 이미지 도구가 없으면 프롬프트만 나왔는지 확인한다.
3. 같은 대화에서 `commerce-product-image-pipeline`에 **가상 무지 제품 상자 한 장**을 요청한다. `moai-media`를 추가 설치하지 않은 상태에서 현재 앱의 기본 이미지 도구로 진행하는지, 실제 파일이 생성됐는지 기록한다. 실물 상품·후기·인증 표시를 테스트 자료로 사용하지 않는다.
4. Higgsfield를 쓰는 검사는 계정·크레딧 잔액과 비용을 확인하고 사용자가 해당 유료 호출을 승인한 뒤에만 진행한다. Claude는 공식 MCP, ChatGPT는 Higgsfield 공식 플러그인을 각각 설치·인증한다. 비용 조회와 이미지 도구가 실제 노출되는지 기록한다. 참조 이미지 검사는 공식 업로드 창에서 **업로드 완료된** 가상 자산만 사용하고, 채팅 첨부만으로 전달됐다고 간주하지 않는다. 생성 ID·결과 파일·실제 차감 크레딧을 기록한다.
5. `moai-seller`의 `commerce-detail-page-image`에서 합성 실행 환경을 확인한다. Python·Pillow가 없으면 섹션 파일과 합성 명세를 받되 단일 PNG는 미완료로 표시하는지 확인한다. 도구가 있으면 더미 섹션 13장의 합성 파일을 다시 열어 1080×12720과 누락 섹션 0개를 확인한다.
6. 나머지 플러그인을 위 표의 순서로 설치하고 각 버전·예시 스킬·선언된 MCP 도구 노출을 확인한다. `moai-media`는 3번의 기본 이미지 도구 경로를 기록한 뒤 설치한다. 로컬 MCP가 뜨지 않으면 앱 화면의 시작 오류와 `uv`·`npx` 실행 파일 관련 표시를 그대로 기록한다. 런처 실패와 서비스 인증 실패를 구분한다. 설치와 도구 노출 결과를 앱·OS별 칸에 남기고, 실제 MCP 호출을 했다면 입력·결과·인증 상태를 별도 기록한다.

각 단계의 상태는 `PASS`·`FAIL`·`NOT-RUN`·`BLOCKED` 중 하나로 기록한다. 설치 화면만 봤거나 CI만 통과한 경우에는 앱 이미지 생성 `PASS`를 주지 않는다. 로그인·권한·유료 생성으로 중단되면 어느 단계에서 무엇이 표시됐는지 남긴다.
