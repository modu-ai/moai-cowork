---
name: content-blog
description: 네이버 블로그·티스토리·브런치스토리·WordPress·Ghost 글을 독자와 발행 채널에 맞춰 작성합니다. 실제 자료와 출처를 확인하고, 검색 노출을 보장하지 않는 초안과 발행 준비 자료를 만듭니다.
version: "1.1.2"
---

# 블로그 글 작성

## 시작

사용자의 발행 채널, 글의 목적, 독자, 주제, 브랜드 문체와 제공 자료를 확인한다. 경험담·후기·사용 사례는 실제 작성자 자료가 있을 때만 쓴다. 통계·제품 효과·가격·일정·인용은 원출처와 기준일을 확인한다. 자료가 없으면 사실처럼 꾸미지 말고 필요한 확인 사항을 남긴다.

## 작성

1. 독자가 알고 싶어 하는 질문과 글에서 실제로 답할 수 있는 범위를 정한다.
2. 제목은 본문 내용과 맞춘다. 분량, 목차, FAQ, CTA는 글의 목적에 필요한 경우에만 넣는다.
3. 근거가 있는 설명과 작성자의 경험을 구분한다. 사진·표·이미지는 설명에 도움이 될 때 사용하고 저작권과 대체 텍스트를 확인한다.
4. 네이버는 [블로그 가이드](references/naver-blog.md), 티스토리는 [티스토리 가이드](references/tistory.md), 브런치스토리는 [브런치 가이드](references/brunch.md), WordPress는 [WordPress 가이드](references/wordpress.md), Ghost는 [Ghost 가이드](references/ghost.md)를 참고한다.
5. 검색과 생성형 검색 관련 요청은 [SEO·AI 검색 가이드](references/seo-geo.md)에 따라 공식 권고와 실측 성과를 분리한다. 검색 상위 노출·AI 인용·전환율을 약속하지 않는다.

## 결과와 발행

결과에는 제목, 본문, 확인한 출처, 미확인 사실을 적는다. 플랫폼이 지원하면 메타 제목·설명과 대표 이미지 설명을 함께 준비한다. 이미지 생성이 필요하면 ChatGPT의 기본 생성 요청은 moai-media의 media-codex-image 경로, 사용자가 Higgsfield를 지정하면 media-higgsfield-image 경로로 연결한다. 생성 도구를 실제 호출하지 않았다면 이미지를 만들었다고 하지 않는다.

연결된 WordPress MCP가 실제로 발견되고 대상 사이트가 확인되면 사용자가 요청한 범위 안에서 초안을 저장할 수 있다. 이 플러그인의 커넥터는 WordPress.com MCP이므로 지원 대상과 계정 접근을 [공식 안내](https://wordpress.com/support/mcp/)에서 확인한다. 게시 또는 뉴스레터 발송은 사용자 승인 범위와 대상 사이트를 확인한 뒤 실행하고, 결과 URL과 공개 상태를 확인한다. 다른 플랫폼은 사용 가능한 공식 연결을 확인하기 전에는 복사 가능한 글과 발행 준비 자료를 준다.

문장 다듬기 스킬을 쓰더라도 출처·인용·수치·유보 조건은 보존한다.

## References

- [네이버 블로그](references/naver-blog.md)
- [티스토리](references/tistory.md)
- [브런치스토리](references/brunch.md)
- [WordPress](references/wordpress.md)
- [Ghost](references/ghost.md)
- [SEO와 AI 검색](references/seo-geo.md)
