---
name: media-codex-image
description: |
  ChatGPT Work에서 현재 대화의 기본 이미지 도구로 이미지를 직접 만듭니다.
  OpenAI의 데스크톱 문서는 이 도구의 모델을 gpt-image-2로 명시합니다.
  GPT Image 2.5를 정확히 지정한 요청은 별도 API 경로가 있는지 확인합니다.
  기존 스킬 이름과의 호환을 위해 media-codex-image 이름을 유지합니다. Higgsfield 계정의
  모델로 생성하라는 요청은 media-higgsfield-image에 맡깁니다.

  다음 요청에 사용하세요:
  - "ChatGPT로 이미지 만들어줘", "GPT Image 2.5로 이미지 생성해줘"
  - "이미지를 직접 만들어줘", "이 사진을 ChatGPT에서 편집해줘"
  - "codex 이미지 생성" (기존 호출 호환)
version: "2.0.2"
---

# ChatGPT 이미지 직접 생성

## 실행 경로

1. 사용자가 **Higgsfield 계정·모델·크레딧**을 지정하면 `media-higgsfield-image`를 사용한다. Higgsfield의 공식 연결과 라이브 모델 조회·비용 확인 절차를 따른다.
2. 사용자가 **GPT Image 2.5를 정확히 지정**했다면 현재 연결에서 `gpt-image-2.5-flare` 또는 `gpt-image-2.5-sunburst`를 명시할 수 있는 OpenAI API 경로가 있는지 확인한다. 없으면 기본 도구로 조용히 바꾸지 않고 2.5 지정 생성은 미완료라고 알린다. API 키를 채팅이나 ChatGPT 로그인 토큰에서 받지 않는다.
3. ChatGPT Work에서 모델을 지정하지 않은 OpenAI 이미지 요청은 **현재 대화에 제공된 이미지 생성 도구**로 생성하거나 편집한다. 복잡한 장면·정확한 문구는 `media-gpt-image-prompt`의 프롬프트 원칙을 적용한다. 완성된 프롬프트만 돌려주고 생성을 끝낸 척하지 않는다.
4. 이미지 도구가 이 세션에 없으면 도구가 없다는 사실을 알리고, 앱 대화 입력창에서 사용할 완성된 프롬프트를 제공한다. 도구가 없는 상태에서 `codex exec` 설치나 별도 로그인을 비개발자에게 요구하지 않는다.
5. Claude Cowork에서 Higgsfield 연결이 있으면 `media-higgsfield-image`를 사용한다. 연결이 없으면 프롬프트와 연결 방법을 제공하고 실제 생성 여부를 분명히 밝힌다.

## 모델 표기의 한계

OpenAI의 [ChatGPT 데스크톱 이미지 생성 문서](https://learn.chatgpt.com/docs/image-generation)는 기본 도구의 모델을 `gpt-image-2`로 명시한다. [ChatGPT Images 2.5 안내](https://help.openai.com/en/articles/11084440)는 웹·모바일의 Images 기능을 설명한다. 따라서 데스크톱 기본 도구 결과에 2.5 모델명을 붙이지 않는다. 정확한 2.5 모델 지정은 OpenAI Image API의 별도 인증·과금 경로가 필요하다. ChatGPT 로그인 토큰을 API 키처럼 사용하거나 `~/.codex/auth.json`을 읽어 넘기지 않는다.

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
| ChatGPT Work 데스크톱의 기본 이미지 생성·편집 | 이 스킬과 현재 세션의 이미지 생성 도구 (`gpt-image-2`, 공식 문서 기준) |
| 정확한 API 모델 ID 지정 | OpenAI Image API (`gpt-image-2.5-flare` 또는 `gpt-image-2.5-sunburst`), 별도 API 인증 필요 |
| Higgsfield 계정의 이미지 모델 | `media-higgsfield-image`와 공식 Higgsfield 연결 |
| 프롬프트만 작성 | `media-gpt-image-prompt` |

## 공식 문서

- [OpenAI — Images in ChatGPT](https://help.openai.com/en/articles/11084440)
- [OpenAI — ChatGPT 데스크톱 이미지 생성](https://learn.chatgpt.com/docs/image-generation)
- [OpenAI — Image generation API](https://developers.openai.com/api/docs/guides/image-generation)
- [Higgsfield — 공식 플랫폼과 MCP 주소](https://higgsfield.ai/creator-hub/help-center/getting-started/official-higgsfield-platforms)
