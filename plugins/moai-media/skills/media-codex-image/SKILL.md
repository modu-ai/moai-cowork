---
name: media-codex-image
description: |
  ChatGPT Work에서 현재 대화의 기본 이미지 도구로 이미지를 직접 만듭니다.
  OpenAI는 ChatGPT Images 2.5를 데스크톱에도 배포한다고 안내합니다.
  Flare·Sunburst API 모델 ID를 정확히 지정한 요청은 moai-mcp-openai 도구로 생성합니다.
  기존 스킬 이름과의 호환을 위해 media-codex-image 이름을 유지합니다. Higgsfield 계정의
  모델로 생성하라는 요청은 media-higgsfield-image에 맡깁니다.

  다음 요청에 사용하세요:
  - "ChatGPT로 이미지 만들어줘", "GPT Image 2.5로 이미지 생성해줘"
  - "이미지를 직접 만들어줘", "이 사진을 ChatGPT에서 편집해줘"
  - "codex 이미지 생성" (기존 호출 호환)
version: "2.1.2"
---

# ChatGPT 이미지 직접 생성

## 실행 경로

1. 사용자가 **Higgsfield 계정·모델·크레딧**을 지정하면 `media-higgsfield-image`를 사용한다. Higgsfield의 공식 연결과 라이브 모델 조회·비용 확인 절차를 따른다.
2. 사용자가 **Flare·Sunburst의 정확한 API 모델 ID**를 지정했다면 `moai-mcp-openai` 연결의 `openai_image_generate` 도구를 확인한다. 사용자가 지정한 모델을 유지한다. 이 도구는 별도 OpenAI API 키와 API 과금이 필요하다. 생성 전에 그 사실과 선택 모델·크기를 알리고 유료 호출에 대한 명시적인 승인을 받는다. 도구나 키가 없으면 기본 도구로 조용히 바꾸지 않고 해당 모델 지정 생성은 미완료라고 알린다. API 키를 채팅이나 ChatGPT 로그인 토큰에서 받지 않는다. **원본 이미지를 넣는 정확한 API 모델 지정 편집 요청에는 이 생성 도구를 호출하지 않는다.** 해당 API 편집 경로는 아직 제공되지 않으므로 미지원이라고 알린다.
3. 사용자가 **ChatGPT Images 2.5**를 명시하면 ChatGPT Work의 현재 대화에 기본 이미지 도구가 있는지 확인하고, 있으면 그 도구로 생성하거나 편집한다. [OpenAI의 배포 안내](https://openai.com/index/introducing-chatgpt-images-2-5/)는 Work 데스크톱의 Images 2.5 제공을 명시하지만, 도구가 모델을 표시하지 않으면 이번 호출의 정확한 모델은 **미확인**으로 보고한다. 도구가 다른 모델을 명시하거나 사용자가 호출별 모델 증명을 요구하면 2.5 사용을 보장하지 말고 정확한 Flare·Sunburst API 모델 ID를 지정할지 확인한 뒤 2번의 별도 인증·과금 경로를 따른다. 기본 도구가 없으면 4번을 따른다. 모델을 지정하지 않은 OpenAI 이미지 요청도 현재 대화의 이미지 도구로 생성하거나 편집한다. 복잡한 장면·정확한 문구는 `media-gpt-image-prompt`의 프롬프트 원칙을 적용한다. 완성된 프롬프트만 돌려주고 생성을 끝낸 척하지 않는다.
4. 이미지 도구가 이 세션에 없으면 도구가 없다는 사실을 알리고, 앱 대화 입력창에서 사용할 완성된 프롬프트를 제공한다. 도구가 없는 상태에서 `codex exec` 설치나 별도 로그인을 비개발자에게 요구하지 않는다.
5. Claude Cowork에서 Higgsfield 연결이 있으면 `media-higgsfield-image`를 사용한다. 연결이 없으면 프롬프트와 연결 방법을 제공하고 실제 생성 여부를 분명히 밝힌다.

## 모델 표기의 한계

[OpenAI의 Images 2.5 발표](https://openai.com/index/introducing-chatgpt-images-2-5/)는 ChatGPT Work·Codex의 데스크톱 배포를 안내한다. 한편 [Codex 이미지 생성 문서](https://learn.chatgpt.com/docs/image-generation)는 내장 도구에 `gpt-image-2`를 명시한다. 이 제품 배포 안내만으로 개별 호출의 모델 메타데이터를 증명할 수는 없다. 모델 표시가 없으면 기본 도구의 생성·편집 결과와 정확한 모델 미확인을 함께 보고하며, 특정 API 모델 ID를 사용했다고 적지 않는다. `gpt-image-2.5-flare`·`gpt-image-2.5-sunburst`를 정확히 지정해야 하면 `moai-mcp-openai`의 별도 인증·과금 경로를 따른다. ChatGPT 로그인 토큰을 API 키처럼 사용하거나 `~/.codex/auth.json`을 읽어 넘기지 않는다.

## 생성과 검수

- 보호되는 캐릭터·로고·실존 인물의 식별 가능한 재현은 원본 자료와 요청한 사용 범위의 허락 근거를 생성 전에 확인한다. 확인할 수 없으면 해당 재현을 생성하지 않고 독창적인 대안을 제안한다. 이름만으로 권리 침해를 단정하지 않는다.
- 사용자의 목적, 화면비, 참조 이미지, 이미지 속 정확한 문구를 이미 받은 경우 다시 묻지 않는다.
- 이미지 안 글자는 따옴표로 정확히 적고 위치·서체·등장 횟수를 지정한다. 결과의 철자와 수량을 확인한다.
- 편집은 바꿀 부분과 유지할 부분을 분리해 지시한다. 참조 이미지가 도구에 실제 첨부됐는지 확인한다.
- 생성 후 결과 이미지를 사용자에게 보여주고, 파일 저장이 필요한 경우 실제 저장 경로를 확인해 전달한다. 프롬프트 작성, 도구 호출, 파일 저장을 각각 별도 완료 사실로 보고한다.
- 생성 호출이 애매하게 실패하면 결과 목록이나 작업 상태를 확인한 뒤 재시도한다. 중복 생성이 확인되지 않은 상태에서 무조건 다시 생성하지 않는다.

## 관련 경로

| 요청 | 경로 |
|---|---|
| ChatGPT Work 데스크톱의 Images 2.5 생성·편집 | 이 스킬과 현재 세션의 기본 이미지 도구. 모델 표시가 없으면 개별 호출의 정확한 모델은 미확인 |
| Flare·Sunburst API 모델 ID를 지정한 이미지 한 장 생성 | `moai-mcp-openai`의 `openai_image_generate` (`gpt-image-2.5-flare` 또는 `gpt-image-2.5-sunburst`), 별도 API 인증·과금 필요 |
| Higgsfield 계정의 이미지 모델 | `media-higgsfield-image`와 공식 Higgsfield 연결 |
| 프롬프트만 작성 | `media-gpt-image-prompt` |

## 공식 문서

- [OpenAI — Images in ChatGPT](https://help.openai.com/en/articles/11084440)
- [OpenAI — Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)
- [OpenAI — ChatGPT 데스크톱 이미지 생성](https://learn.chatgpt.com/docs/image-generation)
- [OpenAI — Image generation API](https://developers.openai.com/api/docs/guides/image-generation)
- [Higgsfield — 공식 플랫폼과 MCP 주소](https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms)
