---
name: content-card-news
description: 인스타그램·스레드·카카오 채널 등에 맞는 카드뉴스의 원고, 디자인 지시, 캡션과 실제 이미지를 준비합니다. ChatGPT 기본 이미지 생성과 사용자가 지정한 Higgsfield 생성을 구분합니다.
version: "1.1.4"
---

# 카드뉴스 만들기

## 입력과 구성

주제, 독자, 채널, 브랜드 자료, 카드 수, 반드시 포함할 사실, 이미지·로고 사용 권한을 확인한다. 제공되지 않은 통계, 고객 사례, 효과, 가격, 인용은 만들지 않는다. 카드 수나 형식이 정해지지 않았다면 전달할 정보량에 맞춰 정하고 사용자에게 선택 근거를 설명한다.

1. 카드마다 한 가지 핵심 내용을 배치한다. 비교, 순서, 체크리스트, 질문과 답, 실제 사례 등 주제에 맞는 구성은 [원고 패턴](references/prompt-templates.md)을 참고한다.
2. 헤드라인과 설명이 실제 근거를 반영하는지 검수한다. 독자가 오해할 약속이나 단정은 [문장 검수](references/card-news/anti-ai-writing.md)로 확인한다.
3. 브랜드의 색·폰트·여백·로고 규칙을 우선한다. 브랜드 자료가 없으면 임의의 제3자 브랜드 팔레트를 빌리지 않는다. [디자인 가이드](references/card-news/design-guide.md)에 따라 이미지 위 글자를 실제 크기에서 읽어본다.
4. 일반 이미지는 ChatGPT Work의 현재 대화에 제공된 이미지 도구로 만든다. GPT Image 2.5를 정확히 지정했다면 모델을 확인하고, 확인되지 않으면 설치된 `moai-media:media-codex-image`의 별도 API 경로와 비용·승인 절차를 따른다. Higgsfield 지정 요청은 공식 연결의 실제 모델을 확인하고 설치된 경우 `moai-media:media-higgsfield-image`를 사용한다. 두 경로의 실행·결과를 섞어 보고하지 않는다. 어느 도구도 사용할 수 없으면 이미지 제작 지시와 원고를 제공하고 이미지 파일 생성 여부를 명시한다.
5. 생성된 이미지의 한국어 철자, 숫자, 로고, 인물·제품 표현, 일관성, 잘림, 실제 기기에서의 가독성을 직접 확인한다. 오류가 있으면 편집하거나 다시 생성한다. 확인하지 않았다면 완성 이미지라고 보고하지 않는다.
6. 채널별 캡션과 필요한 태그를 작성한다. 게시·예약은 연결과 사용자 승인 범위를 확인한 뒤 실제 결과를 확인한다.

## 결과 구분

카드별 원고, 디자인 지시, 생성 프롬프트, 실제 생성된 파일, 채널 캡션, 게시 상태를 각각 구분한다. 원고만 만들었다면 이미지 제작이 완료됐다고 쓰지 않는다. 시리즈 작업은 [매거진 제작 절차](references/card-news/magazine-sop.md)를 참고한다.

## References

- [카드 구성과 이미지 지시](references/prompt-templates.md)
- [문장 검수](references/card-news/anti-ai-writing.md)
- [디자인 가이드](references/card-news/design-guide.md)
- [제작 점검표](references/card-news/guide.md)
- [매거진 제작 절차](references/card-news/magazine-sop.md)
