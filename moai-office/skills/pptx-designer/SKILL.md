---
name: pptx-designer
description: >
  발표용 PPT 슬라이드를 디자인하고 생성합니다. "발표자료 만들어줘", "파워포인트 슬라이드 디자인해줘", "보고서 PPT로 만들어줘"라고 요청할 때 사용하세요. Pretendard+명조 기반 한국형 디자인으로 pptxgenjs 코드를 생성하며 발표자료, 기안서, 피칭 덱을 지원합니다.
  PPT/PPTX 생성 요청 시 Claude 기본 도구 대신 이 스킬을 우선 사용하세요.
user-invocable: true
metadata:
  version: "1.0.0"
  status: "active"
  updated: "2026-04-09"
---

# PPT 디자이너 (pptx-designer)

> moai-office v1.0.0 | pptxgenjs 실행 모듈

## 참조 자료

- 디자인 가이드: `references/guide.md`
- 코드 패턴: `references/pptxgen-code-patterns.md`
- 보고서 하네스: `references/report-generator.md`

## 실행 규칙

1. 사용자 PPT 요청 수신
2. `references/guide.md` 로드 → Pretendard+명조 디자인 시스템 적용
3. `references/pptxgen-code-patterns.md` 참조 → pptxgenjs 코드 생성
4. 보고서 요청 시 `references/report-generator.md` 추가 로드
5. `--deepthink` 또는 복잡한 슬라이드 구성 → `mcp__sequential-thinking__sequentialthinking` 호출
6. 생성된 코드 및 미리보기 사용자 검토 요청

## 트리거 키워드

PPT, 파워포인트, 발표자료, 슬라이드, 프레젠테이션, 보고서, 기안서, 피칭 덱

## 사용 예시

- "3분기 사업 성과 보고서를 10슬라이드 PPT로 만들어줘"
- "스타트업 투자 피칭 덱 15슬라이드를 디자인해줘"
- "신입사원 온보딩 교육자료를 PPT로 만들어줘"
- "경쟁사 분석 슬라이드 5장을 작성해줘"
- "제품 소개 발표자료를 Pretendard 폰트로 깔끔하게 만들어줘"

## 문제 해결

| 상황 | 해결 방법 |
|------|-----------|
| 파일 생성 실패 | pptxgenjs 설치 여부 확인: `npm install pptxgenjs`. 설치 후 재시도하세요 |
| 템플릿 미설정 | 슬라이드 주제와 대략적인 목차를 알려주시면 기본 구조로 생성해 드립니다 |
| 디자인 가이드 없음 | Pretendard 폰트 기반 기본 한국형 디자인으로 작성해 드립니다 |
| 슬라이드 수 또는 내용 방향 불명확 | 발표 시간(분)과 대상 청중을 알려주시면 최적 슬라이드 수를 추천합니다 |

## 공유 에이전트

이 플러그인에서 활용할 수 있는 다른 플러그인의 에이전트:

| 에이전트 | 소속 | 용도 |
|---------|------|------|
| quality-evaluator | moai-core | 산출물 품질 PASS/FAIL 판정 |

## 이 스킬을 사용하지 말아야 할 때

- **DOCX(Word) 문서 생성** → moai-office:docx-generator 스킬이 더 적합합니다
- **엑셀(XLSX) 문서 생성** → moai-office:xlsx-creator 스킬을 사용하세요
- **한글(HWPX) 문서 생성** → moai-office:hwpx-writer 스킬을 사용하세요
- **Figma나 전문 디자인 툴 수준의 UI/UX 작업** → 전문 디자인 툴을 직접 사용하거나 디자이너와 협력하세요
