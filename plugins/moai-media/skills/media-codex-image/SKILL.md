---
name: media-codex-image
description: |
  ChatGPT Work에서 ChatGPT Images 2.5의 기본 이미지 생성 기능으로 이미지를 직접 만듭니다.
  기존 스킬 이름과의 호환을 위해 media-codex-image 이름을 유지합니다. Higgsfield 계정의
  모델로 생성하라는 요청은 media-higgsfield-image에 맡깁니다.

  다음 요청에 사용하세요:
  - "ChatGPT로 이미지 만들어줘", "GPT Image 2.5로 이미지 생성해줘"
  - "이미지를 직접 만들어줘", "이 사진을 ChatGPT에서 편집해줘"
  - "codex 이미지 생성" (기존 호출 호환)
version: "2.0.0"
---

# ChatGPT 이미지 직접 생성

## 실행 경로

1. 사용자가 **Higgsfield 계정·모델·크레딧**을 지정하면 `media-higgsfield-image`를 사용한다. Higgsfield의 공식 연결과 라이브 모델 조회·비용 확인 절차를 따른다.
2. ChatGPT Work에서 OpenAI 이미지 생성을 요청하면 **현재 대화에 제공된 이미지 생성 도구**로 바로 생성하거나 편집한다. 복잡한 장면·정확한 문구는 `media-gpt-image-prompt`의 프롬프트 원칙을 적용한다. 완성된 프롬프트만 돌려주고 생성을 끝낸 척하지 않는다.
3. 이미지 도구가 이 세션에 없으면 도구가 없다는 사실을 알리고, ChatGPT 앱의 **More → Images**에서 바로 실행할 수 있도록 완성된 프롬프트를 제공한다. 도구가 없는 상태에서 `codex exec` 설치나 별도 로그인을 비개발자에게 요구하지 않는다.
4. Claude Cowork에서 Higgsfield 연결이 있으면 `media-higgsfield-image`를 사용한다. 연결이 없으면 프롬프트와 연결 방법을 제공하고 실제 생성 여부를 분명히 밝힌다.

## 모델 표기의 한계

OpenAI는 ChatGPT의 이미지 기능을 **ChatGPT Images 2.5**라고 안내한다. 앱의 기본 이미지 도구는 API의 `model` 인자를 이 스킬에 노출하지 않을 수 있다. 따라서 기본 도구로 생성한 결과를 `gpt-image-2.5-flare` 또는 `gpt-image-2.5-sunburst`로 **임의 판정하지 않는다**. 특정 API 모델 ID를 지정해야 하는 작업은 OpenAI Image API의 모델 선택 기능과 별도 API 인증이 필요하다. ChatGPT 로그인 토큰을 API 키처럼 사용하거나 `~/.codex/auth.json`을 읽어 넘기지 않는다.

## 생성과 검수

- 사용자의 목적, 화면비, 참조 이미지, 이미지 속 정확한 문구를 이미 받은 경우 다시 묻지 않는다.
- 이미지 안 글자는 따옴표로 정확히 적고 위치·서체·등장 횟수를 지정한다. 결과의 철자와 수량을 확인한다.
- 편집은 바꿀 부분과 유지할 부분을 분리해 지시한다. 참조 이미지가 도구에 실제 첨부됐는지 확인한다.
- 생성 후 결과 이미지를 사용자에게 보여주고, 파일 저장이 필요한 경우 실제 저장 경로를 확인해 전달한다. 프롬프트 작성, 도구 호출, 파일 저장을 각각 별도 완료 사실로 보고한다.
- 생성 호출이 애매하게 실패하면 결과 목록이나 작업 상태를 확인한 뒤 재시도한다. 중복 생성이 확인되지 않은 상태에서 무조건 다시 생성하지 않는다.

## 관련 경로

| 요청 | 경로 |
|---|---|
| ChatGPT의 기본 이미지 생성·편집 | 이 스킬과 현재 세션의 이미지 생성 도구 |
| 정확한 API 모델 ID 지정 | OpenAI Image API (`gpt-image-2.5-flare` 또는 `gpt-image-2.5-sunburst`), 별도 API 인증 필요 |
| Higgsfield 계정의 이미지 모델 | `media-higgsfield-image`와 공식 Higgsfield 연결 |
| 프롬프트만 작성 | `media-gpt-image-prompt` |

## 공식 문서

- [OpenAI — Images in ChatGPT](https://help.openai.com/en/articles/11084440)
- [OpenAI — Image generation API](https://developers.openai.com/api/docs/guides/image-generation)
- [Higgsfield — 공식 플랫폼과 MCP 주소](https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms)
