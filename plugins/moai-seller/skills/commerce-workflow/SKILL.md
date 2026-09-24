---
name: commerce-workflow
description: |
  상품 상세페이지·마켓 등록·가격·프로모션·재구매 계획을 함께 준비할 때 상품 사실과 채널 조건을 확인하고 moai-seller의 commerce-* 스킬로 연결합니다.
version: "1.0.0"
---

# 셀러 작업 경로

1. 상품 사실, 판매 채널, 목표 고객, 가격·원가·수수료, 예산과 필요한 산출물을 확인한다. 필수 입력이 없으면 현재 런타임의 질문 채널로 묻고, 질문할 수 없는 하위 실행에서는 누락 자료를 blocker로 반환한다.
2. 상세페이지는 `commerce-detail-page-*`, 마켓 운영은 해당 `commerce-marketplace-*`, 마진은 `commerce-margin-calculator`, 프로모션은 `commerce-promotion-planner`, 광고는 해당 광고 스킬을 따른다. 고객 응답·VOC·채널 메시지는 `moai-cs`의 해당 스킬로 연결한다.
3. 마진율·광고 비용·전환 기준값은 실제 상품 원가와 현재 채널 자료로 계산하고 출처·기준 시점을 표시한다. 불확실한 수치는 추정으로 구분한다.
4. 상세페이지의 강한 상품 주장은 `commerce-ad-claim-compliance-kr`, 메시지 발송 계획은 `commerce-message-compliance-kr` 기준을 확인한다. 외부 메시지 발송과 판매 플랫폼의 상품·주문·프로모션 변경은 사용자의 해당 작업 승인 범위 안에서만 수행한다.
5. 제출 전 `commerce-margin-audit` 기준으로 가격·비용·주장·채널 제약을 검수한다. 같은 주체의 자기 검수는 독립 감사라고 부르지 않는다.

Claude의 `listing-builder` 에이전트와 목적이 겹친다. ChatGPT 플러그인에서는 이 스킬이 발견 가능한 진입점이다.
