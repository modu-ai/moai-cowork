---
title: "설치와 관리"
weight: 10
description: "마켓플레이스 등록 → 필요한 코워커 설치 → 확인 → 업데이트·비활성화·제거, 그리고 MCP 자격증명 준비까지 따라 하기."
geekdocBreadcrumb: true
date: 2026-08-07T00:00:00+09:00
lastmod: 2026-09-25T10:10:00+09:00
---

플러그인 설치는 크게 두 단계입니다. 먼저 **마켓플레이스를 등록**하고,
그다음 **필요한 코워커 플러그인을 골라 설치**합니다.
Claude Cowork는 앱에서 등록하고, ChatGPT Work는 워크스페이스 관리자가
GitHub 마켓플레이스를 가져옵니다.

이 페이지는 **Claude Cowork 또는 ChatGPT Work 데스크톱 앱**을 기준으로 안내합니다.
두 앱의 플러그인 설치 상태는 공유되지 않습니다.
MCP 연동에 필요한 자격증명은 [API 키 넣는 법](mcp/credentials/)을 확인하세요.

두 앱 모두 macOS와 Windows에서 제공됩니다. Linux에서는
[Claude Desktop의 Cowork가 베타](https://support.claude.com/en/articles/10065433-install-claude-desktop)이며
Ubuntu 22.04 LTS 이상 또는 Debian 12 이상(x64·arm64)을 안내합니다.
[ChatGPT 데스크톱은 공개 미리보기](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)로
Ubuntu 24.04/26.04 LTS, Debian 13, Fedora 43/44를 안내합니다.
앱이 설치되더라도 각 플러그인의 로컬 도구·외부 계정 연결은 별도로 확인해야 합니다.

![마켓플레이스 등록에서 설치, 확인, 업데이트로 이어지는 네 단계 흐름](/infographics/install-manage-flow.png)

## 1. 마켓플레이스 등록

### Claude Cowork 앱에서 등록

Claude Cowork 앱의 **Customize → Plugins**에서 개인 마켓플레이스를 추가합니다.
[Claude의 현재 설치 안내](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)에
따른 경로입니다.

1. 앱의 **Cowork** 탭을 열고 **Customize → Plugins**로 이동
2. **Personal plugins**의 **+** → **Add marketplace** →
   **Add from a repository** 선택
3. `modu-ai/moai-cowork`를 입력하고 추가

{{< screenshot-request "Claude Cowork의 Customize → Plugins에서 저장소를 추가하는 화면" >}}

등록이 완료되면 **moai-cowork** 마켓플레이스가 목록에 보이고, 이제 이 가게의 플러그인 목록을 앱에서 볼 수 있습니다.

### ChatGPT Work 워크스페이스에서 가져오기

ChatGPT의 GitHub 마켓플레이스 가져오기는 **워크스페이스 관리자**가 진행합니다.
[OpenAI의 가져오기 안내](https://help.openai.com/en/articles/20001504)에 따른 경로입니다.

1. **Workspace settings → Plugins → Add → Import marketplace**로 이동
2. **Source**에 `https://github.com/modu-ai/moai-cowork` 입력
3. 저장소 루트의 마켓플레이스를 가져오므로 **Path**는 비우고 가져오기 완료

{{< screenshot-request "ChatGPT 관리자: Plugins → Add → Import marketplace" >}}

관리자가 가져온 뒤에는 설치 권한이 있는 사용자가 ChatGPT Work의
**Plugins Directory**에서 해당 마켓플레이스를 선택해 코워커를 설치합니다.
관리자 권한이 없거나 워크스페이스에서 가져오기를 허용하지 않으면
관리자에게 등록을 요청하세요. 개인 계정에서 GitHub 저장소를 직접 추가하는
앱 화면은 여기서 확인하지 못했습니다.

> **잘 안 될 때** — ChatGPT에서 목록이 비어 있다면 관리자에게 가져오기 상태와
> 본인의 설치 권한을 확인해 달라고 요청하세요. Claude에서 목록이 비어 있다면
> 앱을 다시 열고 저장소 등록 상태를 확인하세요.

## 2. 코워커 설치

### 앱 UI에서 설치

마켓플레이스 등록 후에는 Plugins 화면에서 코워커를 선택하고 설치할 수 있습니다.

1. Claude는 **Cowork → Customize → Plugins**, ChatGPT Work는 계정에
   표시되는 **Plugins** 또는 **Apps** 열기
2. **moai-cowork** 마켓플레이스에서 원하는 코워커 선택 (예: `moai-marketer`, `moai-seller`, `moai-coworker`)
3. **+** 또는 **Install** 선택

{{< screenshot-request "Claude Cowork 또는 ChatGPT Work 앱의 Plugins 화면 — moai-cowork 마켓플레이스의 코워커 목록에서 moai-marketer를 선택하고 + 버튼을 누르는 화면" >}}

전부 설치할 필요는 없습니다. 지금 필요한 직무만 골라 설치하세요. 어떤 코워커가 있는지는 [플러그인 설치·운용 개요](../)의 코워커 표를, 각 코워커가 무엇을 하는지는 [에이전트 팀 소개](/moai-agents/)를 참고하세요.

> **추천 설치 순서** — 먼저 `moai-pm` (진입 허브) 과 `moai-coworker` (범용 실무 코어) 를 설치한 뒤, 진행할 작업에 맞는 직무 코워커를 추가하세요. 설치 직후 목록에 보이지 않으면 앱을 재시작해 보세요. 마켓플레이스 등록 (1단계) 을 건너뛴 경우에도 코워커가 보이지 않습니다.

## 3. 설치 확인

### 앱 UI에서 확인

Plugins 화면에서 설치된 코워커 목록을 확인할 수 있습니다. 방금 설치한 코워커가 **enabled** (활성화) 상태로 보이면 성공입니다. 코워커 카드를 누르면 버전·포함된 스킬·MCP 서버 등 상세 정보도 함께 볼 수 있습니다.

{{< screenshot-request "앱의 Plugins 화면 — 설치된 코워커 목록에서 moai-seller가 enabled 상태로 보이고, 카드를 눌러 버전·스킬·MCP 서버 상세 정보가 펼쳐진 화면" >}}

> **잘 안 될 때** — Plugins 화면에 코워커가 보이는데 Claude Cowork 또는 ChatGPT Work 세션 안에서 스킬이 동작하지 않으면, 실행 중이던 세션을 종료하고 새로 시작해 보세요. 플러그인은 세션 시작 시점에 로드됩니다.

## 4. 업데이트·비활성화·제거

### 앱 UI에서 관리

Plugins 화면에서 각 코워커별로 업데이트·비활성화·제거를 할 수 있습니다.

- **업데이트**: 코워커 카드의 **Update** 버튼
- **비활성화/활성화**: **Enable/Disable** 토글
- **제거**: **Remove** 버튼

{{< screenshot-request "앱의 Plugins 화면 — 설치된 코워커 카드에서 Update/Disable/Remove 버튼이 보이는 화면" >}}

비활성화는 설치를 유지한 채 로드만 막는 것이라, 여러 코워커를 설치해 두고 프로젝트에 따라 켜고 끄는 운용에 좋습니다. 제거 후에도 마켓플레이스 등록은 남아 있으므로 언제든 다시 설치할 수 있습니다.

> **잘 안 될 때** — 업데이트 후 동작이 이상하면 앱에서 버전이 실제로 올라갔는지 확인하고, 세션을 재시작하세요. 문제가 계속되면 제거 후 재설치가 가장 확실한 초기화입니다.

## 5. MCP 자격증명 준비 (외부 서비스 연동 코워커)

일부 코워커는 외부 서비스에 직접 접속해 일합니다. 이런 연동을 **MCP** (Model Context Protocol — 앱이 외부 서비스의 도구를 표준 방식으로 부르는 규약) 라고 부르는데, 서비스에 따라 **API 키**가 있어야 실제로 동작합니다.

| 코워커 | 연동 서비스 | 준비물 |
|------|------------|--------|
| `moai-seller` | 네이버 스마트스토어 | 커머스API센터 애플리케이션 ID·시크릿 |
| `moai-seller` | 카페24 | 개발자센터 앱 클라이언트 ID·시크릿 |
| `moai-seller` | 아임웹 | OPEN API 클라이언트 ID·시크릿·토큰 |
| `moai-threads-poster` | Threads·Instagram | Meta 개발자센터 액세스 토큰 |
| `moai-marketer` | Meta Ads | 브라우저 로그인 (키 불필요) |
| `moai-marketer` | 게시 채널 (typefully·wordpress) | 브라우저 로그인 (키 불필요) |
| `moai-media` | Higgsfield·ElevenLabs | Higgsfield는 브라우저 로그인 ([설정 가이드](higgsfield-setup/)) · ElevenLabs는 API 키 |
| `moai-story` · `moai-designer` · `moai-seller` | Higgsfield | Claude는 공식 MCP, ChatGPT는 Higgsfield 공식 플러그인을 연결·인증 ([설정 가이드](higgsfield-setup/)) |
| `moai-accountant` · `moai-analyst` · `moai-coworker` | DART 전자공시 | OpenDART 인증키 |
| `moai-analyst` | KOSIS·건축물대장(archhub) | 없음 (공용키 탑재) |
| `moai-lawyer` | 국가법령정보 | 법제처 OC 키 |
| `moai-officer` | kordoc | 없음 (로컬 처리) |

자격증명이 없어도 코워커의 일반 스킬 (상세페이지 작성, 캠페인 기획 등) 은 그대로 쓸 수 있습니다. 연동 도구를 쓰려는 시점에 넣으면 됩니다.

**키를 넣는 방법은 두 가지입니다.** Claude Cowork는 키가 필요한 코워커를 켤 때
**입력 폼**을 제공합니다. ChatGPT Work에서는 서비스별
**자격증명 파일**(`~/.moai/mcp/<서비스>.json`)을 본인 컴퓨터에 직접 만듭니다.
키를 채팅에 적지 마세요. 서비스별 항목 이름과 안전 수칙은
[API 키 넣는 법](mcp/credentials/)에 정리해 두었습니다.

**API 키는 비밀번호와 같습니다.** 채팅창에 그대로 붙여 넣지 말고, 앱 입력창이나 자격증명 파일로만 넘기세요.

## 다음 단계

설치가 끝났다면, 이 코워커들이 실제로 어떻게 일하는지 — 일하는 에이전트와 검수하는 에이전트가 왜 나뉘어 있는지 — 를 [전문가 에이전트 이해](../agents/)에서 이어서 읽으세요.

---

### Sources

- Claude Cowork 플러그인 설치: <https://support.claude.com/en/articles/13837440-use-plugins-in-claude>
- Claude 조직용 마켓플레이스: <https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization>
- OpenAI 플러그인 빌드 가이드: <https://developers.openai.com/plugins/build/plugins>
- OpenAI GitHub 마켓플레이스 가져오기: <https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github>
- OpenAI 플러그인 사용 가이드: <https://learn.chatgpt.com/docs/plugins?surface=app>
- OpenAI 서브에이전트 설정: <https://learn.chatgpt.com/docs/agent-configuration/subagents>
- 마켓플레이스 진실 원본: [`/.claude-plugin/marketplace.json`](https://github.com/modu-ai/moai-cowork/blob/main/.claude-plugin/marketplace.json)
