---
name: marketing-workflow
description: |
  캠페인·콘텐츠·광고·성과 보고서가 함께 필요한 마케팅 요청에서 목표와 근거를 확인하고 moai-marketer의 marketing-*·content-* 스킬로 작업을 연결합니다. 미디어 생성은 moai-media로 연결합니다.
version: "1.0.0"
---

# 마케팅 작업 경로

1. 제품·브랜드, 채널, 대상 고객, 예산, 기간, 성공 지표와 필요한 산출물을 확인한다. 필수 입력이 없으면 현재 런타임의 질문 채널로 묻고, 질문할 수 없는 하위 실행에서는 누락 자료를 blocker로 반환한다.
2. 캠페인·광고·SEO·성과 분석은 해당 `marketing-*` 스킬을, 블로그·뉴스레터·SNS·카피·발행 계획은 해당 `content-*` 스킬을 따른다. 이미지·영상·음성 생성은 `moai-media:media-production`으로 연결한다.
3. CPC·CTR·ROAS·CAC·벤치마크 등 수치는 실제 조회 결과나 현재 출처와 기준 시점을 붙인다. 가정과 추정치는 실측치와 구분한다. 예산 배분과 기대 성과의 산식을 표시한다.
4. 외부 게시와 광고 계정의 생성·수정·활성화는 사용자의 해당 작업 승인 범위를 확인한 뒤 수행한다. 승인된 신규 광고는 PAUSED로 만든다. 인증 정보는 산출물에 기록하지 않는다.
5. 광고 주장과 메시지 발송의 국내 규정 검수는 `moai-seller:commerce-ad-claim-compliance-kr`와 `moai-seller:commerce-message-compliance-kr` 지침을 확인한다. 제출 전 `marketing-evidence-audit` 기준으로 수치·카피·채널 제한을 대조한다. 같은 주체의 자기 검수는 독립 감사라고 부르지 않는다.

Claude의 `campaign-strategist` 에이전트와 목적이 겹친다. ChatGPT 플러그인에서는 이 스킬이 발견 가능한 진입점이다.
