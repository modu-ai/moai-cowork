---
name: marketing-campaign-planner
description: |
  광고·SNS·이메일을 묶은 캠페인 기획안과 A/B 테스트, 인플루언서 협업, 고객 여정·CRM 전략을 작성합니다.
  확인된 사업 자료와 가정을 구분하고, 예산·성과 수치를 임의로 확정하지 않습니다.
version: "1.1.4"
---

# 캠페인 플래너

광고·SNS·이메일·인플루언서 활동을 하나의 목표에 맞춰 계획합니다. 사업 전체 전략이나 상세페이지·전문 미디어 제작까지 요청받으면 설치된 경우 moai-consultant·moai-seller·moai-media의 해당 스킬을 활용합니다. 없어도 이 스킬에서 캠페인 계획과 제작 브리프를 제공합니다.

## 입력 확인

- 목표, 대상 고객, 상품·서비스의 확인된 정보, 진행 기간과 예산 상한
- 기존 채널 성과의 집계 기간·출처·분모, 측정 가능한 전환 정의
- 브랜드 가이드, 광고 계정 권한, 협찬 조건, 고객 연락 동의 범위
- 빠진 정보는 질문하거나 명시적 가정으로 두고, 가정을 실제 성과처럼 쓰지 않습니다.

## 계획

1. 목표에 맞는 하나의 주요 성과 지표와 보조·안전 지표를 정합니다.
2. 채널별 고객 접점과 선택 근거를 적습니다. 채널별 예산 비율은 기존 데이터와 목표를 보고 제안하며 고정 공식을 적용하지 않습니다.
3. 메시지·크리에이티브 가설, 필요한 자산, 실행 주체와 검토 지점을 정합니다.
4. 표와 수치의 출처를 적고, 검증되지 않은 할인·재고·후기·효과·성과를 광고 문구에 넣지 않습니다.
5. 게시·발송·광고 집행은 기획안과 별도 상태입니다. 연결 도구의 실제 권한과 사용자 요청을 확인하고 결과 상태를 구분해 보고합니다.

## A/B 테스트

가설, 주요 지표, 무작위 배정 단위, 기준선, 최소 검출 효과, 필요 표본, 분석·중지 기준을 사전에 정합니다. 기준선과 표본이 없으면 숫자나 유의성을 만들어 내지 않고 측정 계획을 제시합니다. 여러 지표나 중간 확인이 있다면 결과 해석의 한계를 적습니다. 설계 방법은 references/ab-testing.md를 참고합니다.

## 인플루언서·CRM·고객 여정

- 인플루언서: 실제 후보의 오디언스 적합성, 협업 조건, 광고 표시와 사용권, 측정 가능한 결과를 확인합니다. references/influencer-strategy.md를 참고합니다.
- CRM: 수집 목적, 보유 데이터, 연락 동의와 수신 거부를 확인한 뒤 세그먼트와 메시지 후보를 설계합니다. references/crm-strategy.md를 참고합니다.
- 고객 여정: 실제 접점과 관찰 자료를 따라 단계를 그립니다. 정해진 퍼널 단계에 고객을 억지로 맞추지 않습니다. references/customer-journey-map.md를 참고합니다.
- 성장 실험과 영업 지원 요청은 각각 references/growth-hacking.md, references/sales-enablement.md를 참고합니다.

## 이미지·상세페이지 요청

- ChatGPT Work에서 일반 이미지는 현재 대화의 이미지 도구로 생성합니다. ChatGPT Images 2.5 요청도 현재 대화의 기본 이미지 도구로 생성·편집합니다. 모델 표시가 없으면 개별 호출의 정확한 모델은 미확인으로 보고합니다. Flare·Sunburst API 모델 ID 지정은 설치된 `moai-media:media-codex-image`의 별도 API 경로와 비용·승인 절차를 따릅니다.
- 사용자가 Higgsfield를 지정하면 공식 연결의 실제 모델을 확인하고, 설치된 경우 moai-media:media-higgsfield-image를 사용합니다. 영상은 사용 가능한 도구와 설치된 경우 media-higgsfield-video 스킬을 확인합니다.
- 이커머스 상세페이지 제작은 moai-seller의 상세페이지 스킬로 연결합니다.
- 이 폴더의 references/imagegen/guide.md와 references/product-detail/guide.md는 제작 요청을 정리하는 참고자료입니다. 사실·규격·권리 조건은 해당 도구와 판매 채널에서 확인합니다.

## 산출물·검수

요청 범위에 맞는 캠페인 한 장 요약, 채널·예산·일정 표, KPI 정의, 실험 설계, 메시지 방향을 제공합니다. 실제 집행·분석은 수행 여부와 근거를 따로 기록합니다. 서술 부분은 필요한 경우 ai-slop-reviewer와 korean-humanize로 다듬되, 원문과 대조해 수치·조건·의미가 바뀌지 않았는지 확인합니다. 관련 스킬이 설치되지 않았으면 직접 같은 점검을 합니다.

## 참고 파일

| 파일 | 사용 시점 |
|---|---|
| references/ab-testing.md | 실험 설계 |
| references/crm-strategy.md | 고객 연락 전략 |
| references/customer-journey-map.md | 실제 접점과 고객 여정 정리 |
| references/growth-hacking.md | 성장 가설과 실험 우선순위 |
| references/influencer-strategy.md | 협찬·협업 설계 |
| references/sales-enablement.md | 영업 자료와 프로세스 |
