# 채점 엔진 브리지 — gan-loop Must-Pass 4항목 + 미가용 폴백

> `story-webtoon-qc` Step 4-2에서 로드한다. 가용할 때 `moai-designer:design-iteration-loop`의 반복 채점(`rubric-image.md`)에 제출할 Must-Pass 항목과, 미가용 시 자체 폴백 절차. **채점 엔진은 선택 확장이지 필수 의존이 아니다.**

## 실행 경로

```
story-webtoon-qc 실행 경로
├─ 기본(항상 동작): 자체 defect-checklist.md 1패스 판정
└─ 선택(가용 시): moai-designer:design-iteration-loop + rubric-image.md 반복 채점
   → 미가용/호출 실패 시 기본 경로로 전환하고 검수 범위를 고지
```

## gan-loop에 제출하는 Must-Pass 4항목

채점 엔진이 가용하면 `rubric-image.md`의 Must-Pass로 다음 4항목을 제출한다.

| # | Must-Pass 항목 | 판정 기준 |
|---|----------------|-----------|
| 1 | **캐릭터 동일성** | 일관성 앵커 위반 0건(`defect-checklist.md` 앵커 판정) |
| 2 | **컷 간 톤·화풍 일치** | 스타일 앵커(7토큰)가 컷마다 유지 |
| 3 | **말풍선 대비·최소 글자 크기** | 축소 상태에서도 대비·가독 확보(`story-webtoon-lettering` 기준) |
| 4 | **세로 스크롤 원고 규격 적합** | 캔버스 폭·여백 띠 존치(`story-webtoon-spec:manuscript-specs.md`) |

## 미가용 시 폴백 절차

`design-iteration-loop`은 현재 Desktop 환경에서 동작하지 않을 수 있다(`.moai/config/sections/design.yaml` 의존·`user-invocable:false`·영문). 필수 의존으로 걸지 않는다.

1. 채점 도구가 없으면 자체 체크리스트로 **실제 접근 가능한 이미지**를 확인한다.
2. 사용자에게 사용한 경로와 확인하지 못한 항목을 알린다. 이미지가 없으면 검수 완료로 표시하지 않는다.
3. 위 네 항목 중 직접 확인한 것만 판정하고 나머지는 미검증으로 남긴다.

## 경계 요약

- **루브릭 항목(Must-Pass 4)** = `story-webtoon-qc` 제공.
- **채점 엔진(반복 루프)** = `moai-designer` 소유(선택).
- 이미지에 접근할 수 있으면 자체 점검을 수행한다. 이미지가 없으면 결함 판정은 보류한다.

## 출처

- Must-Pass 4항목·실행 경로·폴백 규약: `moai-designer:design-iteration-loop` 위임 설계 핸드오프(내부 자산).
