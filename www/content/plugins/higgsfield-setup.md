---
title: "Higgsfield 연결 설정"
weight: 20
description: "Claude Cowork의 Higgsfield MCP와 ChatGPT Work의 공식 Higgsfield 플러그인 연결, 계정 승인과 크레딧 확인 안내."
geekdocBreadcrumb: true
date: 2026-09-25T00:00:00+09:00
lastmod: 2026-09-25T00:00:00+09:00
---

[Higgsfield](https://higgsfield.ai)는 이미지·영상 등의 생성 서비스를 제공합니다.
Claude Cowork는 공식 MCP 연결을, ChatGPT Work는 공식 Higgsfield 플러그인을
사용합니다. 계정 연결 뒤에도 실제로 사용할 기능은 현재 대화에 노출된 도구로
확인합니다.

Higgsfield 연결을 사용하는 스킬은 다음과 같습니다.

- `moai-media`: `media-higgsfield-image`, `media-higgsfield-video`,
  `media-higgsfield-identity`, `media-higgsfield-assets`,
  `media-higgsfield-explainer`, `media-higgsfield-product`.
  호출 계약과 비용 고지는 `media-higgsfield-core`를 따릅니다.
- `moai-story`: `story-webtoon-art`, `story-conti`,
  `story-character-sheet`, `story-cover-art`, `story-previz`.
  생성 실행은 `moai-media`에 맡깁니다.
- `moai-designer`: `design-brand-visual`, `design-logo`,
  `design-landing-motion`. 생성 실행은 `moai-media`에 맡깁니다.

## 1. 앱에서 연결

**Claude Cowork:** Settings → Connectors → Add custom connector에서 이름을
Higgsfield로 정하고 공식 주소 `https://mcp.higgsfield.ai/mcp`를 입력한 뒤
Connect를 선택합니다. 플러그인의 `.mcp.json`도 이 주소를 가리키지만,
설치만으로 연결·인증이 끝났다고 가정하지 마세요.

**ChatGPT Work:** 앱에서 Plugins Directory를 열어 공식 Higgsfield 플러그인을
추가합니다. 이 경로에서는 MCP 주소를 직접 입력하지 않습니다. Plugins가
보이지 않거나 연결할 수 없다면 계정·워크스페이스에서 제공하는 앱 기능을
확인하세요.

## 2. Higgsfield 계정 승인

두 앱 모두 Higgsfield 로그인 창에서 사용할 계정을 확인하고 접근을 승인합니다.
API 키를 플러그인 문서나 대화에 붙여 넣을 필요는 없습니다. 연결 뒤
이미지·영상·Soul·오디오·설명 영상 등 요청한 기능의 도구가 현재 세션에
실제로 있는지 확인하세요. 도구가 보이지 않으면 해당 기능을 실행할 수
있다고 안내하지 않습니다.

## 3. 크레딧 안내

Higgsfield 생성 작업은 계정의 크레딧을 소모합니다. 생성 전에 현재 연결에서
요청한 모델·옵션의 견적과 잔액을 확인하고, 사용자에게 비용을 보여준 뒤
승인을 받습니다. 크레딧 잔액은 [Higgsfield 웹](https://higgsfield.ai)에서도
확인할 수 있습니다.

견적은 실제 차감액의 확정값이 아닙니다. 작업이 끝나면 반환된 차감 정보와
견적 차이를 확인합니다. ChatGPT 공식 플러그인에서 HTTPS 참조 이미지를
견적 도구에 넘기면 계정 미디어 라이브러리로 가져올 수 있으므로,
외부 전송 허용을 견적 전에 확인합니다.

비용과 제공 기능은 모델·옵션·연결 방식에 따라 달라집니다. 고정 예시
가격으로 결제 여부를 판단하지 말고, 현재 세션에서 받은 견적을 확인하세요.

## 4. 연결 또는 기능이 없을 때

Higgsfield 연결이 없거나 요청한 도구가 노출되지 않았다면 실제 생성은
진행하지 않고 연결 상태와 빠진 기능을 알립니다. 원하는 경우
[Higgsfield 웹](https://higgsfield.ai)에서 사용할 프롬프트를 작성합니다.
사용자가 Higgsfield 모델을 지정했다면 다른 이미지 제공자로 조용히
바꾸지 않습니다.

---

### 참고 자료

- [Higgsfield 공식 연결 안내](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent)
- [Higgsfield 공식 MCP와 플랫폼 안내](https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms)
- [OpenAI 플러그인 설치·연결 안내](https://help.openai.com/en/articles/20001256/)
- 마켓플레이스 진실 원본: [`/.claude-plugin/marketplace.json`](https://github.com/modu-ai/moai-cowork/blob/main/.claude-plugin/marketplace.json)
