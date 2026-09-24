---
name: content-sns-content
description: 인스타그램·카카오 채널·Threads·X·LinkedIn·Facebook·YouTube Shorts용 원고와 캡션을 실제 브랜드 자료와 채널 규격에 맞춰 작성합니다. 이미지 생성, 초안, 예약, 게시 상태를 구분합니다.
version: "1.1.2"
---

# SNS 콘텐츠

사용자가 지정한 채널, 대상 계정, 독자, 목적, 브랜드 말투, 원본 자료와 게시 권한을 확인한다. 사용자가 한 채널만 요청했다면 다른 채널용 산출물을 강제하지 않는다. 사실·후기·수치·기간·할인은 확인한 자료에서만 가져온다.

## 제작

1. 게시물에서 독자에게 전달할 한 가지 핵심 내용과 출처를 정한다.
2. 채널별 편집 화면과 [공식 규격 확인표](references/platform-specs.md)를 확인한다. 글자 수·이미지·영상·태그 제한은 계정 유형과 기능에 따라 달라질 수 있다. 고정된 최적 게시 시각·빈도·알고리즘 가중치를 근거 없이 적용하지 않는다.
3. 플랫폼별 문체를 조정하되 원문의 사실과 제한 조건은 보존한다. 네이버 블로그 단일 글은 content-blog, 카드뉴스는 content-card-news, 광고 문구는 content-copywriting을 사용한다.
4. 이미지가 필요한 ChatGPT 기본 요청은 moai-media:media-codex-image, 사용자가 Higgsfield를 지정한 요청은 moai-media:media-higgsfield-image로 연결한다. 생성된 이미지의 글자·로고·권리·크롭을 직접 확인한다. 숏폼 영상 제작은 해당 미디어 스킬의 실제 도구·모델과 결과를 확인한다.
5. [원본 재활용](references/content-repurposer.md)은 사용 권리와 현재성을 확인하고 채널에 맞게 편집한다. 원본이 없으면 실제 내용을 보지 못한 상태로 변환했다고 하지 않는다.

## 연결과 게시

이 플러그인의 Typefully MCP가 현재 앱에서 연결되면 X·LinkedIn·Threads 등의 초안·예약 기능을 [공식 Typefully MCP 안내](https://support.typefully.com/en/articles/13128440-typefully-mcp-server)에 따라 사용할 수 있다. 다른 채널은 실제로 확인한 공식 연결이나 앱 화면을 사용한다. 도구를 찾지 못하면 복사 가능한 초안을 준다.

계정, 게시물, 예약 시간대, 공개 범위를 확인한다. 초안 저장과 예약·공개 게시를 다른 상태로 기록하고, 게시·예약은 사용자의 승인 범위 안에서 실행한다. 실행 뒤 도구 응답과 게시 URL 또는 예약 목록에서 결과를 확인한다. 광고 계정의 예산·활성화 여부는 별도 요청과 현재 계정 자료로 판단한다. 일정 시간은 절대 변경하지 말라는 일률적 규칙을 적용하지 않는다.

## 결과

채널별 원고, 캡션·태그, 사용한 자료, 이미지·영상 제작 상태, 초안·예약·게시 상태, 미확인 조건을 적는다. 채널별 세부 질문은 아래 참고문서에서 필요한 것만 읽는다.

## References

- [플랫폼 규격 확인표](references/platform-specs.md)
- [종합 제작 점검](references/sns-content/guide.md)
- [인스타그램](references/instagram.md) · [카카오](references/kakao.md) · [Threads](references/threads.md)
- [X](references/x-twitter.md) · [LinkedIn](references/linkedin.md) · [Facebook](references/facebook.md) · [YouTube Shorts](references/youtube-shorts.md)
- [브랜드 보이스](references/brand-voice-guide.md) · [원본 재활용](references/content-repurposer.md)
- [브랜드 아이덴티티](references/brand-identity.md) · [개인 브랜딩](references/personal-branding.md) · [콘텐츠 제작](references/content-creator.md)
