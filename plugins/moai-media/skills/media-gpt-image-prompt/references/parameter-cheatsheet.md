# GPT Image 2.5 — 파라미터 · 모델 선택 · 이전 절차

API 파라미터는 **프롬프트와 따로** 설정합니다. ChatGPT 웹 화면에서는 일부가 자동으로 정해지고, OpenAI API(`images.generate`, `images.edit`)와 Higgsfield에서는 직접 지정합니다.

## 모델 선택

| 모델 ID | 성격 |
|---|---|
| `gpt-image-2.5-flare` | 작은 모델. 속도 우선. 화질은 GPT Image 2와 비슷한 수준 |
| `gpt-image-2.5-sunburst` | 기본 모델. 품질 우선. GPT Image 2보다 높은 화질 |

**새 워크플로**

1. 속도가 우선이면 Flare, 품질 요구가 까다로우면 Sunburst로 시작한다.
2. 결과가 요구를 채우면, 그다음에 지연을 줄일 여지를 찾는다.

**기존 GPT Image 2에서 옮길 때**

| 지금 상황 | 먼저 시험할 모델 |
|---|---|
| 검증된 GPT Image 2 워크플로가 이미 품질 요구를 채움 | Flare — 품질을 유지하면서 지연이 줄어드는지 확인 |
| GPT Image 2로 품질이 모자랐던 복잡한 작업 | Sunburst — 필요한 품질이 나오는지 먼저 확인 |

Sunburst가 품질을 채우면 같은 프롬프트·입력으로 Flare를 시험합니다. Flare도 요구를 채우고 지연이 줄면 Flare로 바꾸고, 아니면 Sunburst를 유지합니다. 속도 개선은 프롬프트·레퍼런스·해상도·품질 설정에 따라 달라지므로 **자기 작업으로 측정**합니다.

## quality

| 값 | 쓰는 경우 |
|---|---|
| `auto` (기본값) | 모델이 정함 |
| `low` | 빠른 시안, 대량 A/B |
| `medium` | 공식 예시 대부분의 기본값. 일반 사진·광고·일러스트 |
| `high` | 작은 글자·범례·축·각주가 있는 슬라이드·차트, 라벨 많은 다이어그램, 교재 |
| `xhigh` · `max` | 채워지지 않은 품질 요구가 있고 지연을 감당할 수 있을 때만 |

- 품질 조정은 **모델을 고른 뒤**에 합니다.
- 결과가 모자라면 한 단계 올려 시험하고, 요구를 채우면 한 단계 낮춰 품질이 유지되는지 봅니다.
- 높은 설정이 모든 프롬프트에서 더 나은 결과를 보장하지 않습니다.
- 같은 이름의 품질이라도 모델끼리 화질·응답 시간이 같다는 뜻이 아닙니다. 모델 비교 시에는 품질·프롬프트·레퍼런스·해상도를 고정합니다.

## size

`auto` 또는 `WIDTHxHEIGHT`. 사용자 지정 해상도 조건:

- 각 변 3,840px 이하
- 두 변 모두 16의 배수
- 긴 변 : 짧은 변 ≤ 3:1
- 총 픽셀 655,360 ~ 8,294,400
- 총 픽셀 3,686,400(`2560x1440`) 초과 출력은 **실험 단계**

| 화면비 | 권장 size | 총 픽셀 | 비고 |
|---|---|---|---|
| 1:1 | `1024x1024` | 1,048,576 | 가장 무난 |
| 1:1 (2K) | `2048x2048` | 4,194,304 | 실험 단계 구간 |
| 3:2 · 2:3 | `1536x1024` · `1024x1536` | 1,572,864 | 공식 예시 다수가 `1024x1536` |
| 16:9 | `1536x864` | 1,327,104 | 슬라이드 예시 크기 |
| 16:9 (2K) | `2048x1152` | 2,359,296 | 실험 구간 아님 |
| 16:9 (4K) · 9:16 (4K) | `3840x2160` · `2160x3840` | 8,294,400 | 실험 단계 구간 |
| 9:16 | `864x1536` | 1,327,104 | 릴스·쇼츠 |
| 4:5 | `1024x1280` | 1,310,720 | 인스타 피드 |

## background · output_format · output_compression

| 파라미터 | 값 | 메모 |
|---|---|---|
| `background` | `auto` · `opaque` · `transparent` | 투명이 필요하면 `transparent`를 **명시** |
| `output_format` | `png` · `jpeg` · `webp` | 투명은 PNG 또는 WebP |
| `output_compression` | 0~100 | JPEG·WebP 전용. PNG에는 쓰지 않는다 |

투명 에셋은 디코딩한 이미지의 알파 채널을 직접 확인합니다(머리카락·유리·그림자·가장자리). 체크무늬를 그린 배경은 투명이 아닙니다. 후속 편집에서도 "투명 배경 유지"를 다시 요청합니다.

## n

같은 프롬프트로 변형 여러 장이 필요할 때 사용합니다(공식 로고 예시가 `n`으로 변형을 요청).

## input_fidelity

GPT Image 2·2.5 경로에서는 **생략**합니다. 입력 이미지는 항상 높은 충실도로 처리됩니다. (`gpt-image-1`·`1.5`에만 있던 파라미터)

## Higgsfield MCP 매핑 (`media-higgsfield-image`)

Higgsfield 모델 ID는 `gpt_image_2_5`입니다 (2026-09-13 모델 목록 조회 기준).

| OpenAI API | Higgsfield 파라미터 |
|---|---|
| `model=gpt-image-2.5-flare` / `-sunburst` | `variant=flare` / `sunburst` (기본 `flare`) |
| `quality` | `quality`: `low`·`medium`·`high`·`xhigh`·`max` (기본 `low`) |
| `size` | `aspect_ratio`(예: `1:1`, `16:9`, `9:16`, `4:5`) + `resolution`: `1k`·`2k`·`4k` |
| `background` | `background`: `auto`·`opaque`·`transparent` |
| `images.edit`의 입력 이미지 | `medias` (역할 `image_references`) |

Higgsfield 기본 품질이 `low`이므로 결과물 용도면 `medium` 이상을 명시합니다.

## API 호출 예 (Python)

```python
from openai import OpenAI

client = OpenAI()

result = client.images.generate(
    model="gpt-image-2.5-flare",
    prompt=prompt,
    size="1024x1024",
    quality="medium",
)
```

투명 로고:

```python
result = client.images.generate(
    model="gpt-image-2.5-flare",
    prompt=logo_prompt,
    size="1024x1024",
    quality="medium",
    background="transparent",
    output_format="png",
    n=4,
)
```

편집 (여러 레퍼런스):

```python
result = client.images.edit(
    model="gpt-image-2.5-sunburst",
    image=[open("person.png", "rb"), open("jacket.png", "rb")],
    prompt=edit_prompt,
    size="1024x1536",
    quality="medium",
)
```

## 이전 절차 (기존 워크플로 → 2.5)

1. **기준선 저장** — 대표 프롬프트와 레퍼런스(어려운 편집·정확한 텍스트·얼굴·제품 형태·투명 에셋 포함), 현재 모델·설정·결과를 기록한다.
2. **첫 후보 선택** — 위 모델 선택 표를 따른다. 첫 비교에서는 프롬프트·레퍼런스·해상도·출력 형식을 바꾸지 않는다.
3. **결과 전체 확인** — 지시 이행, 정체성·제품 보존, 텍스트 정확도, 원치 않는 변경, 투명도. 반복 요청으로 일관성도 본다. 편집 워크플로는 단계별과 전체 연속 편집을 모두 시험한다.
4. **품질 통과 후 지연 시험** — Sunburst로 시작했다면 Flare를 같은 기준으로 평가한다.
5. **설정은 하나씩** — 프롬프트를 고치기 전에 품질 단계부터 비교한다. 일반·느린 응답, 실패, 재시도, 채택 이미지당 비용을 잰다. 요금은 현재 요금표로 확인한다.
6. **워크플로 단위로 배포** — 작은 비중부터 옮기고 같은 지표를 보며 넓힌다. 지원되는 동안 이전 모델로 되돌릴 수 있게 둔다.

반복 편집은 지키려던 디테일을 여전히 바꿀 수 있습니다. 제약을 다시 적고 매번 확인합니다. 픽셀 단위로 같아야 하는 영역은 승인된 편집 결과를 원본에 합성합니다.

## 구 모델 참고

| 모델 | quality | size | 상태 |
|---|---|---|---|
| `gpt-image-2` | `low`·`medium`·`high`·`auto` | `auto` 또는 지원 해상도 | 유지보수용. 투명 배경은 프리뷰 |
| `gpt-image-1.5` | `low`·`medium`·`high`·`auto` | `1024x1024`·`1024x1536`·`1536x1024`·`auto` | 2026-12-01 종료 예정 |
| `gpt-image-1` | 위와 같음 | 위와 같음 | 2026-10-23 종료 예정 |

## 출처

- [OpenAI — Image prompting: Choose a model / Model parameters / Migrate an existing workflow](https://developers.openai.com/api/docs/guides/image-prompting) (2026-09-13 확인)
- [OpenAI — Image generation pricing](https://developers.openai.com/api/docs/pricing#image-generation)
- Higgsfield MCP `models_explore` 조회 결과 (`gpt_image_2_5`, 2026-09-13)
