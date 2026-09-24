---
name: media-gpt-image-prompt
description: |
  OpenAI GPT Image 2.5(Flare·Sunburst) 전용 이미지 프롬프트 텍스트 빌더. 사용자 자연어 요청에서 필요한 맥락을 수집하고, OpenAI 공식 이미지 프롬프팅 가이드의 8가지 원칙에 맞춰 ChatGPT·OpenAI API·Higgsfield에서 쓸 프롬프트를 출력합니다. 모델·품질·크기·배경 파라미터는 API나 Higgsfield에서 지정할 때만 별도로 표시합니다. 같은 입력으로 Gemini 3 Pro Image · Midjourney V8 프롬프트도 만들 수 있습니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "GPT 이미지 프롬프트 만들어줘", "ChatGPT 이미지 프롬프트"
  - "GPT Image 2.5 프롬프트", "gpt-image-2.5 프롬프트 작성", "Flare·Sunburst용 프롬프트"
  - "GPT-image-2 프롬프트"(사용자가 지목한 모델을 유지하고 2.5 이전은 선택지로 안내)
  - "OpenAI 이미지 프롬프트", "GPT용 이미지 편집 프롬프트"
  - "/media-gpt-image-prompt" (직접 호출)

  이미지 자동 생성은 페어 스킬 media-higgsfield-image(Higgsfield) 또는 media-codex-image(ChatGPT 기본 이미지 도구)를 사용하세요. 본 스킬은 프롬프트 텍스트 산출 전용입니다.
version: "2.0.4"
---

# GPT Image 2.5 Prompt Builder — 공식 가이드 8원칙 + 3-모델 동시 출력

> 이미지 프롬프트 빌더 (텍스트 산출 전용)

## 개요

GPT Image 2.5는 모델이 둘입니다.

| 모델 ID | 성격 | 먼저 고르는 경우 |
|---|---|---|
| `gpt-image-2.5-flare` | 작은 모델, 속도 우선. 화질은 GPT Image 2와 비슷한 수준 | 새 워크플로에서 속도가 중요할 때, 기존 GPT Image 2 품질로 충분할 때 |
| `gpt-image-2.5-sunburst` | 기본 모델, 품질 우선. GPT Image 2보다 화질이 높음 | 품질 요구가 까다로울 때, GPT Image 2로 품질이 모자랐던 복잡한 작업 |

두 모델 모두 생성·편집·투명 배경을 지원하고, 정밀 편집과 피사체 보존이 좋아졌습니다. 본 스킬은 사용자 한 줄 요청을 OpenAI 공식 가이드의 프롬프팅 원칙에 맞춰 풀어 쓰고, 모델 선택과 파라미터까지 함께 권합니다.

- **공식 원칙 기반**: 결과물의 용도·구도를 먼저 정하고, 보이는 디테일을 적고, 텍스트는 따옴표로 정확히, 편집은 "바꿀 것"과 "지킬 것"을 분리합니다.
- **3개 모델 동시 출력**: GPT Image 2.5 메인 프롬프트와 함께 같은 의도를 Gemini 3 Pro Image(5-component)와 현재 Midjourney V8(기본 V8.2)의 어조로 변환합니다.
- **프리셋 + 미세조정**: 제품샷·인물·일러스트·풍경 프리셋과 프리셋별 미세조정 질문으로 디테일을 모읍니다.

프롬프트 텍스트만 산출합니다. 정확한 GPT Image 2.5 생성은 해당 모델을 지정할 수 있는 OpenAI API 또는 Higgsfield의 현재 연결로 이어 갑니다. ChatGPT Work의 기본 이미지 도구는 데스크톱 공식 문서상 `gpt-image-2`이므로, 같은 프롬프트를 거기에 입력해도 2.5 생성으로 표시하지 않습니다. 실제 생성은 `media-codex-image` 또는 `media-higgsfield-image`의 경로 판단을 따릅니다.

## 트리거 키워드

GPT 이미지 프롬프트 ChatGPT 이미지 프롬프트 GPT Image 2.5 프롬프트 gpt-image-2.5 Flare Sunburst OpenAI 이미지 프롬프트 GPT 이미지 편집 프롬프트 gpt-image-2 프롬프트

## 워크플로우

```
사용자 자연어 한 줄
    ↓
[Round 1] 사용 가능한 질문 경로 — 작업 유형(생성/편집) + 프리셋 선택
    ↓
[Round 2] 사용 가능한 질문 경로 — 프리셋별 미세조정 (필요한 슬롯만)
    ↓
[Round 3] 사용 가능한 질문 경로 — 화면비 · 이미지 내 텍스트 · API 모델(필요할 때만)
    ↓
[내부] 슬롯 → 공식 원칙에 맞춘 프롬프트 (짧은 단락 또는 라벨 섹션)
    ↓
[내부] 같은 슬롯 → Gemini 5-component 변환 + MJ 키워드+파라미터 변환
    ↓
출력: 3개 모델 프롬프트 + 권장 파라미터 + 결과 검수 체크리스트 + 한국어 해설
```

사용자가 이미 구체적으로 적은 슬롯은 다시 묻지 않습니다. 결과를 바꾸는 정보만 확인합니다.

## 실행 규칙

### Round 1 — 작업 유형과 프리셋 (필수)

이미 주어진 요청에서 생성인지 편집인지, 어떤 프리셋이 맞는지 확인합니다. 결과를 바꾸는 필수 정보가 비어 있으면 현재 앱에서 제공하는 질문 수단을 사용합니다. 구조화 질문 도구가 없는 앱에서는 일반 대화로 필요한 정보만 묻습니다. 편집이면 Round 2 대신 [편집 워크플로우](#편집-워크플로우)로 갑니다.

| 프리셋 | 적용 케이스 | references |
|---|---|---|
| 제품샷 (권장) | 커머스 상품 사진, 패키지 컷, 보석·시계 클로즈업 | `presets/product-shot.md` |
| 인물·캐릭터 | 인물 포트레이트, 페르소나 일러스트, 광고 모델 | `presets/portrait.md` |
| 일러스트·아트 | 카드뉴스 일러스트, 책 표지, 컨셉 아트 | `presets/illustration.md` |
| 풍경·환경 | 배경 이미지, 공간 사진, 시네마틱 배경 | `presets/landscape.md` |

인포그래픽·다이어그램·슬라이드·UI 목업·로고·만화 컷처럼 프리셋에 맞지 않는 용도는 `references/workflow-recipes.md`의 해당 레시피를 슬롯 정의로 씁니다.

### Round 2 — 프리셋별 미세조정 (3-4 질문)

선택된 프리셋의 `presets/<name>.md`에 정의된 슬롯 중 결과에 필요한 것만 확인합니다. 구조화 질문 도구가 있으면 그 도구의 선택지 형식을 쓰고, 없으면 짧은 일반 질문으로 묻습니다. 이미 받은 정보는 다시 묻지 않습니다.

### Round 3 — 화면비 · 텍스트 · 모델 (최대 3 질문)

**화면비** — GPT Image 2.5의 `size`는 `WIDTHxHEIGHT` 자유 지정입니다. 조건: 각 변 3,840px 이하, 두 변 모두 16의 배수, 긴 변:짧은 변 3:1 이하, 총 픽셀 655,360~8,294,400. 총 픽셀이 3,686,400(`2560x1440`)을 넘으면 공식적으로 실험 단계입니다.

| 화면비 옵션 | 용도 | GPT Image 2.5 `size` | Gemini | MJ |
|---|---|---|---|---|
| 1:1 (권장) | SNS 정사각, 일반 | `1024x1024` | `1:1` | `--ar 1:1` |
| 16:9 | 유튜브 썸네일, 슬라이드 | `1536x864` (2K: `2048x1152`) | `16:9` | `--ar 16:9` |
| 9:16 | 인스타 릴스·쇼츠 | `864x1536` | `9:16` | `--ar 9:16` |
| 4:5 | 인스타 피드 | `1024x1280` | `4:5` | `--ar 4:5` |
| 2:3 · 3:2 | 포스터·인쇄 · 가로 사진 | `1024x1536` · `1536x1024` | `2:3` · `3:2` | `--ar 2:3` · `--ar 3:2` |

**텍스트** — 이미지 안에 글자가 들어가면 정확한 문자열을 따로 받습니다(한 글자도 바꾸지 않기 위해).

**모델** — ChatGPT 기본 이미지 도구를 쓸 때는 Flare/Sunburst를 묻거나 선택됐다고 표시하지 않습니다. OpenAI API 또는 Higgsfield에서 모델을 직접 지정하는 경우에만 `gpt-image-2.5-flare`(속도)와 `gpt-image-2.5-sunburst`(품질)를 비교합니다. 사용자가 특정 모델을 지목했다면 그 선택을 유지합니다. 판단 흐름은 `references/parameter-cheatsheet.md` §모델 선택.

### 내부 처리 — 프롬프트 작성 (공식 8원칙)

상세 규칙과 예시는 `references/prompting-fundamentals.md`. 요점만:

1. **결과를 정의한다** — 피사체와 용도(제품 사진·광고·다이어그램)를 첫 문장에. 구도·화면비·배치 제약을 적는다.
2. **읽기 쉬운 형식을 고른다** — 단순한 요청은 서술형 단락, 복잡한 요청은 `Scene:` `Subject:` `Details:` `Constraints:` 같은 **라벨 섹션**. 특수 문법에 기대지 않는다.
3. **보이는 디테일을 적는다** — 재질·조명·색·매체. 사진이 목표면 "photorealistic"을 명시. 카메라 사양은 외형 단서일 뿐 물리 시뮬레이션 보장이 아니다. 분위기 단어만 쓰지 말고 규모·대기·색을 적는다.
4. **인물과 동작을 구체화한다** — 프레이밍("full body visible, feet included"), 시선, 사물과의 상호작용.
5. **텍스트는 정확히** — 따옴표로 감싸고 위치·서체를 적는다. 몇 번 나오는지("exactly once"), 추가 텍스트 금지. 특이한 단어·브랜드명은 한 글자씩 풀어 쓴다. → `references/text-rendering.md`
6. **변경과 제약을 분리한다**(편집) — "change only X" + 지킬 항목 나열 + 제외 항목(워터마크·로고). → `references/editing-patterns.md`
7. **레퍼런스에 역할을 준다** — 입력 이미지마다 번호와 역할(피사체·스타일·의상·배경), 합치는 방식.
8. **한 번에 하나씩 반복한다** — 이전 결과를 다음 입력으로, 한 가지만 바꾸고 지킬 항목은 다시 적는다.

라벨 섹션 기본 골격:

```
Create <deliverable: a photorealistic product photograph / an infographic / ...> of <subject> for <use>.
Scene: <place, time, atmosphere>
Subject: <form, material, distinctive features; people: framing, gaze, action>
Details: <composition and camera cues, lighting, color palette, medium and finish>
Text (verbatim): "<exact copy>" — <position, typography>, rendered exactly once
Constraints: <what must not appear: no extra text, no watermark, no unrelated logos>
```

### 내부 처리 — Gemini 5-component 변환

동일 슬롯을 Gemini 3 Pro Image의 5-component 영문 문장형으로 변환합니다 (각 component는 마침표로 구분, Creative Director 어조).

```
[Subject + Adjectives] doing [Action] in [Location/Context].
[Composition/Camera]. [Lighting/Atmosphere]. [Style/Media].
[Specific Constraint/Text]
```

### 내부 처리 — Midjourney v8 키워드+파라미터 변환

동일 슬롯을 콤마 구분 키워드 + `--파라미터` 형식으로 변환합니다.

```
[subject], [scene keywords], [composition], [lighting], [style] --ar W:H [--raw] [--hd] [--s 0~1000] [--sref CODE|URL --sw N] [--edit IMAGE_URL] [--p PROFILE] [--no NEGATIVE]
```

Midjourney 파라미터 상세는 페어 스킬 `media-midjourney-v8-prompt`를 따릅니다. 현재 V8에는 `--q` Quality 파라미터와 `--oref`·`--cw`가 없으므로 출력하지 않습니다. 이미지 참조는 Edit Model 경로를 안내합니다.

### 출력 — 3개 모델 코드블록 + 권장 파라미터 + 검수 + 해설

````markdown
## 생성된 프롬프트 (3개 모델)

### 1) GPT Image 2.5 — OpenAI API 또는 지원 모델이 확인된 Higgsfield 연결
```text
<공식 원칙에 맞춘 프롬프트 (단락 또는 라벨 섹션)>
```
**OpenAI API에서 지정할 때의 권장 파라미터**: `model=gpt-image-2.5-flare`, `quality=medium`, `size=1024x1024` (투명 배경이면 `background=transparent`, `output_format=png`). ChatGPT Work 기본 이미지 도구에서는 이 값을 직접 설정할 수 없고, 데스크톱 공식 문서는 기본 모델을 `gpt-image-2`로 안내합니다.
**Higgsfield로 생성 시**: `model=gpt_image_2_5`, `variant=flare`, `quality=medium`, `aspect_ratio=1:1`

### 2) Gemini 3 Pro Image — Nano Banana Pro
```text
<5-component 영문 문장>
```
**권장 파라미터**: `aspect_ratio=1:1`, `resolution=2K`

### 3) Midjourney V8.2 (사용자가 V8.1을 지정했다면 V8.1)
```text
<키워드, 키워드, ... --ar 1:1 --raw --s 300>
```

### 결과 검수 체크리스트
- 필요한 텍스트가 정확하고 읽히는가? (다이어그램이면 라벨과 관계까지)
- 인물 정체성·제품 형태·라벨 등 지켜야 할 디테일이 그대로인가?
- (편집) 요청한 부분만 바뀌었는가?
- (투명 배경) 파일에 실제 알파 채널이 있는가? 체크무늬를 그린 배경은 투명이 아니다.

### 한국어 해설
- 모델 선택 이유, 품질 설정을 올리거나 내릴 조건
- 3개 프롬프트의 어조 차이 (서술/라벨 섹션 · 5-component 문장 · 키워드+파라미터)
````

### 편집 워크플로우

사용자가 기존 이미지를 편집하려 하면 편집 모드로 진입합니다. 공식 원칙 6·7·8을 적용한 3블록 형식을 씁니다.

```
Change only: <바꿀 요소 한두 가지, 바뀐 뒤 상태를 구체적으로>
Preserve: <identity·face·pose·geometry·layout·labels·lighting·camera angle·background 중 지킬 항목>
Constraints: <no extra text, no logos, no watermark, do not restyle>
```

여러 이미지를 넣을 때는 `Image 1: <역할>` `Image 2: <역할>`로 번호를 붙이고, 무엇을 어디로 옮기는지 적습니다. 반드시 픽셀 단위로 동일해야 하는 영역이 있으면 프롬프트만 믿지 말고, 승인된 편집 결과를 원본에 합성하도록 안내합니다. 상세 패턴(번역·스타일 전이·의상 교체·레퍼런스 결합·투명 누끼·스케치→실사·객체 제거·인물 삽입·다회차 정제)은 `references/editing-patterns.md`.

편집 모드에서는 GPT Image 2.5 프롬프트만 출력합니다(Gemini·MJ는 편집 메커니즘이 달라 별도 안내).

### 구 모델 요청 처리

"GPT-image-2 프롬프트"처럼 이전 모델을 지목하면 요청 모델을 유지해 작성하고 파라미터 차이를 알립니다: `gpt-image-2`는 `quality`가 `low/medium/high/auto`까지이고 `input_fidelity`는 생략합니다. 2.5 이전은 별도 선택지로 제안합니다. 이전 절차는 `references/parameter-cheatsheet.md` §이전 절차.

## 사용 예시

**예시 1: 제품샷 한 줄 요청**
> "GPT 이미지 프롬프트 만들어줘. 매트 블랙 머그 'MONDAY' 글자 들어간 제품샷"

→ Round 1: 생성·제품샷 → Round 2: 머그/슬레이트 카운터/창문 조명/3-4분 앵글 → Round 3: 1:1 + "MONDAY" → 3개 모델 프롬프트 출력. API로 만들 때만 Flare/Sunburst를 고릅니다.

**예시 2: 발표 슬라이드용 차트**
> "시장 규모 TAM/SAM/SOM 슬라이드 이미지 프롬프트, 16:9"

→ `references/workflow-recipes.md` §슬라이드·차트 레시피 → 숫자·라벨을 프롬프트에 직접 넣고 `size=1536x864`, `quality=high`(작은 글자·범례) 권장.

**예시 3: 편집 모드**
> "기존 머그 이미지에서 머그 색만 빨강으로 바꾸는 GPT 프롬프트"

→ 편집 모드 → Change only / Preserve / Constraints → GPT Image 2.5 편집 프롬프트만 출력.

## 출력 형식

| 산출물 | 형식 | 설명 |
|---|---|---|
| GPT Image 2.5 프롬프트 | 영문 단락 또는 라벨 섹션 | OpenAI API `prompt` / Higgsfield `prompt`. ChatGPT Work 기본 도구에 입력하면 2.5 모델 지정은 유지되지 않음 |
| 권장 파라미터 | `model`·`quality`·`size`·`background` | API 호출 시 프롬프트와 **별도로** 설정 |
| Gemini 3 Pro Image 프롬프트 | 영문 5-component 단락 | Google AI Studio / Vertex AI |
| Midjourney V8 프롬프트 | 짧은 설명 + 지원되는 `--파라미터` | Discord `/imagine` 또는 웹 |
| 결과 검수 체크리스트 | 마크다운 | 공식 가이드의 결과 확인 항목 |

## 주의사항

- 본 스킬은 **프롬프트 텍스트만** 출력합니다. 실제 이미지 생성은 페어 스킬을 사용하세요.
- 파라미터는 프롬프트 안에 쓰지 않고 API 설정으로 따로 넘깁니다(공식 가이드).
- `quality`는 먼저 모델을 고른 뒤 조정합니다. 결과가 모자라면 한 단계 올리고, 충분하면 낮춰서 속도를 확인합니다. `xhigh`·`max`는 채워지지 않은 품질 요구가 있고 지연을 감당할 수 있을 때만. 같은 품질 이름이라도 모델마다 화질·속도가 같지 않습니다.
- 투명 배경은 `background=transparent` + PNG 또는 WebP. `output_compression`은 JPEG·WebP에만 씁니다. 머리카락·유리·그림자·가장자리의 알파를 직접 확인합니다.
- 속도·비용은 작업마다 다릅니다. 빠른 모델이 더 싸다고 가정하지 말고 현재 요금표를 확인합니다.
- 실존 인물·브랜드·저작권 캐릭터는 권리 확인이 필요합니다. 로고·캐릭터 요청은 "original, non-infringing"을 명시합니다. 모든 프롬프트는 사용자의 책임 하에 사용됩니다.
- Gemini 3 Pro Image 출력에는 SynthID 워터마크가 눈에 보이지 않게 삽입됩니다 (Google 정책).

## 관련 스킬

| 스킬 | 관계 | 설명 |
|---|---|---|
| media-gemini-3-image-prompt | sibling | 동일 입력으로 Gemini 어조 최적화 프롬프트 산출 |
| media-midjourney-v8-prompt | sibling | 동일 입력으로 MJ 키워드+파라미터 프롬프트 산출 |
| media-higgsfield-image | after | Higgsfield MCP로 생성 — `gpt_image_2_5`(Flare/Sunburst) 모델 지원 |
| media-codex-image | after | ChatGPT Work 기본 이미지 도구로 직접 생성·편집 (앱에서 API 모델 ID 지정 불가) |

## 출처

- [OpenAI — Image prompting (GPT Image 2.5 prompting guide)](https://developers.openai.com/api/docs/guides/image-prompting) — 모델 선택, 파라미터, 프롬프팅 원칙, 생성·편집 예시, 이전 절차, 결과 확인 (2026-09-13 확인)
- [OpenAI — Image generation guide](https://developers.openai.com/api/docs/guides/image-generation) — API 설정·마스크 편집
- [openai-cookbook — image-gen-models-prompting-guide.ipynb (고정 커밋)](https://github.com/openai/openai-cookbook/blob/d310dfa05d20fb653caa9c1c4b89ac1a4aeeeae4/examples/multimodal/image-gen-models-prompting-guide.ipynb) — GPT Image 2 원본 예제
