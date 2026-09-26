---
name: marketing-landing-page
description: |
  캠페인·이벤트·리드 수집용 랜딩페이지의 구조와 카피를 설계하고, 요청 시 기존 프로젝트에 맞춰 구현합니다.
  확인되지 않은 후기·성과·가격·혜택을 만들지 않으며 이미지 생성 경로와 게시 상태를 구분합니다.
version: "1.1.3"
---

# 랜딩페이지 제작

이 스킬은 하나의 캠페인 행동을 돕는 페이지를 설계합니다. 기존 페이지 진단은 marketing-landing-page-conversion-audit, 카탈로그 상품 상세페이지는 moai-seller의 상세페이지 스킬을 사용합니다.

## 먼저 확인할 것

- 목표 행동, 대상 고객, 상품·서비스와 실제 가격·기간·신청 조건
- 브랜드 자료, 기존 사이트·프레임워크·호스팅·디자인 시스템, 제공된 이미지와 권리
- 폼·결제·분석 연동의 실제 접근 권한과 개인정보 처리 조건
- 사용자가 요청한 결과가 카피 초안, 화면 설계, 구현 파일, 배포 중 어디까지인지

브랜드나 기술 선택이 비어 있으면 이미 제공된 자료를 우선 사용하고 필요한 질문만 묶어 확인합니다. 질문 도구가 없는 호스트에서는 일반 대화로 묻거나 명시적인 임시 가정으로 초안을 만듭니다. 색·모서리·모션을 네 문항으로 반드시 고르게 하지 않습니다.

## 제작 순서

1. 핵심 약속과 행동 문구를 확인된 상품 조건에 맞춰 씁니다. 근거 없는 사용자 수, 후기, 할인, 기간 한정, 무료 체험을 넣지 않습니다.
2. 필요한 섹션만 구성합니다. 히어로·혜택 설명·사용 방법·확인된 증거·FAQ·신청 경로 중 목표에 필요한 것을 고릅니다.
3. 브랜드 자료와 기존 코드베이스의 구성 요소·스타일을 재사용합니다. 새 프로젝트가 필요하고 사용자가 shadcn/ui를 원하면 공식 설치 문서를 확인하고 현재 버전에 맞춰 구성합니다.
4. 일반 이미지는 ChatGPT Work의 현재 대화에 제공된 이미지 도구로 만듭니다. ChatGPT Images 2.5 요청도 현재 대화의 기본 이미지 도구로 생성·편집합니다. 모델 표시가 없으면 개별 호출의 정확한 모델은 미확인으로 보고합니다. Flare·Sunburst API 모델 ID 지정은 설치된 `moai-media:media-codex-image`의 별도 API 경로와 비용·승인 절차를 따릅니다. Higgsfield 지정 요청은 공식 연결의 실제 모델을 확인하고 설치된 경우 moai-media:media-higgsfield-image를 사용합니다. Claude Cowork에서는 설치·인증된 이미지 도구를 확인합니다. 생성하지 않았으면 이미지 완료라고 표시하지 않습니다.
5. 요청 범위에 따라 카피, 설계, 구현 파일을 만듭니다. 코드의 폼 제출·결제·분석은 실제 연동 전까지 미구현 또는 미검증으로 표시합니다.
6. 구현한 화면을 가능한 기기 크기에서 열어 내용·대비·키보드·링크·폼·이미지 잘림을 점검합니다. 실행하지 못한 검사는 통과로 기록하지 않습니다.

## 프레임워크와 테마

기존 프로젝트가 있으면 그 스택을 따릅니다. 새 React 프로젝트에서 shadcn/ui를 선택한 경우 [공식 설치 안내](https://ui.shadcn.com/docs/installation)와 [테마 문서](https://ui.shadcn.com/docs/theming)를 확인합니다. components.json은 CLI를 쓰는 경우에 필요하며, Tailwind CSS v4에서는 tailwind.config.ts 생성을 기본 파일 목록으로 강제하지 않습니다. 단일 HTML을 요청받았으면 React 도입 없이 구현할 수 있습니다. 테마 선택은 references/landing-page/shadcn-theme-interview.md를 참고하되 브랜드 결정을 대체하지 않습니다.

## 품질 기준

- 광고와 랜딩의 가격·혜택·신청 조건이 의미상 일치해야 합니다.
- 카피·후기·수치·보증 문구는 원본 근거와 대조합니다. 카피 변경이 필요하면 승인된 내용도 함께 수정합니다.
- 모바일과 데스크톱에서 글과 주요 행동이 읽히고 조작 가능해야 합니다. 접근성 준수는 실제 검사 범위와 결과로 보고합니다.
- 실제 배포·측정 없이 전환율 상승이나 SEO 순위 향상을 약속하지 않습니다.
- 한국어 서술 검수 스킬이 설치돼 있으면 활용하고 원문과 대조합니다. 없으면 직접 사실·의미·문장을 검수합니다.

## 참고문서

| 파일 | 용도 |
|---|---|
| references/landing-page/brand-context-template.md | 브랜드와 상품 정보 수집 |
| references/landing-page/shadcn-theme-interview.md | shadcn/ui를 선택한 경우의 테마 확인 |
| references/landing-page/design-principles.md | 화면 디자인 결정과 접근성 |
| references/landing-page/copywriting-rules.md | 카피 사실 확인 |
| references/landing-page/ab-testing-guide.md | 변경 효과 검증 설계 |
| references/landing-page/evaluation-checklist.md | 제작·실행 결과 점검 |
| references/landing-page/guide.md | 산출물 범위와 연결 상태 |
