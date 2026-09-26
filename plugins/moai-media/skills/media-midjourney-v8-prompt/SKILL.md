---
name: media-midjourney-v8-prompt
description: |
  Midjourney V8 이미지 프롬프트 빌더. 현재 기본 V8.2를 기준으로 짧은 이미지 설명과 지원되는 파라미터를 만들고, 사용자가 V8.1을 지정하면 그 버전을 유지합니다. 참조 이미지는 Edit Model, 스타일 참조는 `--sref`를 안내합니다. GPT Image 2.5·Gemini 이미지 프롬프트도 함께 출력합니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "미드저니 프롬프트 만들어줘", "MJ 프롬프트"
  - "Midjourney 프롬프트", "/imagine 프롬프트 작성"
  - "Midjourney v8 프롬프트", "미드저니 8.1 프롬프트", "미드저니 8.2 프롬프트"
  - "--sref 프롬프트", "--oref 프롬프트", "스타일 코드 프롬프트"
  - "/media-midjourney-v8-prompt" (직접 호출)

  본 스킬은 프롬프트 텍스트만 산출합니다. 실제 생성은 사용자가 Midjourney 웹 또는 Discord에서 실행합니다.
version: "2.0.4"
---

# Midjourney V8 Prompt Builder — 현재 버전의 파라미터 + 3개 모델 프롬프트

> moai-coworker | 이미지 프롬프트 빌더 (텍스트 산출 전용)

## 개요

Midjourney 공식 문서의 현재 기본 버전은 V8.2입니다. 사용자가 V8.1을 지정했다면 해당 버전을 유지합니다. 피사체와 장면을 짧고 구체적으로 묘사하고, 필요한 파라미터만 끝에 붙입니다. 현재 V8에서는 `--q` Quality 파라미터와 Omni Reference의 `--oref`·`--cw`를 사용하지 않습니다.

```
[subject], [scene keywords], [composition], [lighting], [style]
--ar W:H [--raw] [--hd] [--s 0~1000]
[--sref CODE|URL --sw N] [--edit IMAGE_URL]
[--p PROFILE] [--no NEGATIVE] [--c 0~100]
```

특히 본 스킬은:

- **3개 모델 동시 출력**: Midjourney 메인 + GPT Image 2.5(공식 가이드 원칙) + Gemini 3 Pro Image(5-component)
- **프리셋 + 미세조정**: 4 프리셋 × 4 슬롯
- **호환성 검사**: V8에서 지원하지 않는 `--q`·`--oref`·`--cw`·`--cref`를 그대로 출력하지 않고 현재 대체 경로를 설명
- **Personalization 통합**: `--p PROFILE_ID` 또는 `--profile PROFILE_ID` 안내
- **Style Code 라이브러리**: `--sref CODE` 자주 쓰이는 코드 참조

## 트리거 키워드

미드저니 프롬프트 MJ 프롬프트 Midjourney 프롬프트 imagine 프롬프트 Midjourney v8 미드저니 8.1 sref 프롬프트 oref 프롬프트 스타일 코드 프롬프트 personalization 프로파일

## 워크플로우

```
사용자 자연어 한 줄
    ↓
[Round 1] 현재 앱의 질문 경로 — 프리셋 선택
    ↓
[Round 2] 현재 앱의 질문 경로 — 필요한 프리셋 슬롯만 확인
    ↓
[Round 3] 현재 앱의 질문 경로 — 화면비·텍스트·고급 옵션(--sref·--edit·--p·--no)
    ↓
[내부] 슬롯 → 키워드 콤마 + --파라미터 매핑
    ↓
[내부] 같은 슬롯 → GPT Image 2.5 공식 원칙 + Gemini 5-component 변환
    ↓
[내부] 현재 V8 지원 여부와 공식 GPU 시간 안내 확인
    ↓
출력: 3개 모델 프롬프트 + 필요한 비용 안내 + 한국어 해설
```

## 실행 규칙

### Round 1 — 프리셋 선택 (필수)

4개 프리셋 (제품샷·인물·일러스트·풍경) 중 선택. 프리셋 슬롯 정의는 3개 이미지 프롬프트 빌더(gpt-image·gemini·midjourney)가 공유하는 단일 원본을 사용하며, 원본은 `media-gpt-image-prompt` 스킬에 있습니다:

사용자가 이미 제공한 정보는 다시 묻지 않습니다. 필요한 정보가 비어 있으면 직접 실행에서만 현재 앱의 질문 채널을 사용합니다. 하위 에이전트에서는 질문 도구가 보여도 상위에 blocker를 반환하고, 직접 실행에 질문 채널이 없어도 필요한 입력을 명시한 blocker를 반환합니다. 응답을 받기 전에 임의로 프리셋을 확정하지 않습니다.

- 제품샷 — `../media-gpt-image-prompt/presets/product-shot.md`
- 인물·캐릭터 — `../media-gpt-image-prompt/presets/portrait.md`
- 일러스트·아트 — `../media-gpt-image-prompt/presets/illustration.md`
- 풍경·환경 — `../media-gpt-image-prompt/presets/landscape.md`

### Round 2 — 프리셋별 미세조정 (3-4 질문)

위 경로는 이 `SKILL.md`가 있는 디렉터리를 기준으로 해석합니다. 공유 슬롯 원본 `../media-gpt-image-prompt/presets/<name>.md`에는 세 모델의 어조 변환 가이드가 있으며, 본 스킬은 Midjourney 섹션을 적용합니다.

### Round 3 — 화면비 + 텍스트 + 고급 옵션

#### Q1 — 화면비 (`--ar`)

| 화면비 | `--ar` | 용도 |
|---|---|---|
| 1:1 (권장) | `--ar 1:1` | SNS 정사각 |
| 16:9 | `--ar 16:9` | 와이드, 유튜브 |
| 9:16 | `--ar 9:16` | 릴스·쇼츠 |
| 4:5 | `--ar 4:5` | 인스타 피드 |
| 3:2 | `--ar 3:2` | 사진 표준 |
| 2:3 | `--ar 2:3` | 책 표지 |
| 21:9 | `--ar 21:9` | 울트라와이드. V8 SD·HD의 최대 화면비 안에 들어감 |

#### Q2 — 해상도·스타일 (`--hd`, `--raw`, `--s`)

| 옵션 | 동작 |
|---|---|
| 기본 | SD, 모델의 기본 스타일 |
| `--raw` | 자동으로 더하는 스타일을 줄여 프롬프트 영향력 확대 |
| `--hd` | 2K 이미지. 사용자가 고해상도를 요청했을 때만 추가 |
| `--s 0~1000` | 스타일 강도. 기본값 100 |

V8.1·V8.2에는 `--q` Quality 파라미터가 없습니다. GPU 시간은 작업·계정 설정에 따라 확인합니다. 공식 표의 일반 이미지 프롬프트 예시는 SD 약 0.8분, HD 약 1.3분이며 이를 다른 옵션의 고정 배수로 곱하지 않습니다. 자세한 내용은 `references/cost-traps.md`.

#### Q3 — 텍스트 (이미지 내 글자가 있을 때)

이미지 속 글자는 결과에서 직접 검수합니다. 권장:

- 텍스트는 따옴표로 정확히: `"MONDAY"`
- 짧은 단어/단문 위주 (긴 문장은 깨질 위험)
- 영문이 한글보다 안정적

#### Q4 — 고급 옵션 (선택)

필요할 때 현재 앱의 질문 경로로 추가 옵션을 확인합니다:

| 옵션 | 사용 | 메모 |
|---|---|---|
| Style Reference (`--sref`) | 특정 스타일 코드 또는 참조 이미지 URL | 강도 조절이 필요하면 `--sw 0~1000` |
| Edit Model (`--edit`) | 캐릭터·객체 참조나 기존 이미지 편집 | 웹에서는 Attach to prompt, Discord에서는 `--edit IMAGE_URL` |
| Personalization (`--p`) | 사용자가 잠금을 푼 프로필 | 현재 계정에서 사용 가능 여부 확인 |
| Negative (`--no`) | 제외할 요소 | 예: `--no people, --no text` |
| Chaos (`--c 0~100`) | 결과 다양성 | 시안용 |

상세 사용법은 `references/style-references.md`.

### 내부 처리 — 키워드 콤마 + --파라미터 매핑

```
[subject], [scene keywords], [composition keywords],
[lighting keywords], [style/medium keywords] --ar W:H
--raw --s 250 [--hd]
```

`references/prompt-blocks.md`의 키워드 분류 가이드를 참조.

### 내부 처리 — 함정 검사

본 스킬은 출력 전에 다음을 자동 검사하고 경고를 한국어 해설에 포함:

1. `--q`·`--oref`·`--cw`·`--cref`가 V8 프롬프트에 남지 않았는지 확인하고 Edit Model 등 대체 경로를 설명합니다. 사용자가 이전 버전을 명시하면 그 버전의 문서를 따로 확인합니다.
2. `--hd`를 요청하면 공식 GPU 시간 안내와 현재 계정의 남은 시간을 확인하도록 합니다. 근거 없는 비용 배수를 계산하지 않습니다.
3. `--sref random`을 쓰면 결과에서 정해진 스타일 코드를 저장하도록 안내합니다.

### 출력 — 3개 모델 코드블록

아래의 꺾쇠괄호 자리표시는 출력 전에 요청 내용으로 채웁니다. 화면비를 지정하지 않았다면 각 제공자의 기본값을 명시합니다.

```markdown
## 생성된 프롬프트 (3개 모델)

### 1) Midjourney V8.2 (메인, 사용자가 V8.1을 지정하면 V8.1)
```
<subject>, <scene>, <composition>, <lighting>, <style>
--ar <요청 비율> [--raw] --s 300
```
**해상도·비용**: 고해상도를 요청했을 때만 `--hd`를 붙이고 공식 GPU 시간 표와 계정 잔여 시간을 확인합니다.
**Personalization 활용**: `--p YOUR_PROFILE_ID` 추가 시 일관된 스타일

### 2) GPT Image 2.5 — 모델을 지정할 수 있는 OpenAI API 또는 확인된 Higgsfield 연결
```
<공식 원칙 프롬프트 (단락 또는 라벨 섹션)>
```
**OpenAI API에서 지정할 때의 권장 파라미터**: `quality=medium`, `size=<요청 비율에 맞는 유효한 WIDTHxHEIGHT>` (비율 미지정 시 `1024x1024`; 21:9 예시 `1792x768`). ChatGPT 기본 이미지 도구의 내부 모델이나 API 파라미터를 설정했다고 표시하지 않습니다.

### 3) Gemini 3 Pro Image — Nano Banana Pro
```
<5-component 영문 문장>
```
**Gemini Interactions API에서 지정할 때의 권장값**: 이미지 `response_format`의 `type=image`, `aspect_ratio=<요청 비율>`, `image_size=2K`. GenerateContent API는 요청 형식이 다릅니다. Pro 모델에 `mode=Thinking`을 API 값으로 넘기지 않습니다.

### 한국어 해설
- Midjourney 프롬프트는 필요한 시각적 단서와 지원되는 파라미터만 담았습니다.
- 이미지 안의 글자·참조 이미지 유지 여부는 생성 후 직접 확인합니다.
- 사용자가 `--oref`·`--cref`를 요청했다면 V8 Edit Model의 참조 이미지 경로를 안내합니다.

### 페어 스킬
- `media-gpt-image-prompt` — GPT 어조 (sibling)
- `media-gemini-3-image-prompt` — Gemini 어조 (sibling)
- Midjourney 실행은 Midjourney 웹 또는 Discord에서 직접
```

## 사용 예시

**예시 1: 제품샷**
> "Midjourney 프롬프트, 매트 블랙 머그 'MONDAY' 글자 제품샷, 1:1, --hd"

→ Round 1: 제품샷 → Round 2: 머그/슬레이트/창문/3-4분 → Round 3: 1:1 + "MONDAY" + `--hd` 활성화 → 3개 모델 출력 + 공식 GPU 시간 안내.

**예시 2: 캐릭터 일관성 (Edit Model)**
> "미드저니 프롬프트로 같은 캐릭터 다른 장면, --oref [URL] --cw 50"

→ 인물·캐릭터 프리셋 → Round 2 → 사용자가 적은 이전 `--oref`·`--cw` 옵션은 V8에 그대로 복사하지 않고, 웹의 Attach to prompt 또는 Discord의 `--edit URL` 경로로 바꿔 안내. 참조 이미지에서 지킬 얼굴·의상·색을 문장으로 명시합니다.

**예시 3: Style Reference**
> "MJ 프롬프트 --sref 1234567890 --sw 200"

→ Round 1·2 → Round 3에서 sref 코드 + sw 입력 → `--sref`·`--sw`를 보존하고 현재 계정의 GPU 시간 확인을 안내합니다.

## 출력 형식

| 산출물 | 형식 | 설명 |
|---|---|---|
| Midjourney V8 프롬프트 | 짧은 설명 + 지원되는 `--파라미터` | Midjourney 웹 또는 Discord 입력 |
| GPT Image 2.5 프롬프트 | 영문 단락 또는 라벨 섹션 | Flare·Sunburst API 모델 지정은 OpenAI API 또는 확인된 Higgsfield 연결에서 가능. ChatGPT Work Images 2.5는 별도 배포 경로 |
| Gemini 3 Pro Image 프롬프트 | 영문 5-component 단락 | Google AI Studio / Vertex AI 복붙 |
| 비용 안내 | 공식 GPU 시간 표·계정 잔여 시간 | 고정 배수 계산 없이 확인 |
| 한국어 해설 | 마크다운 | 지원 옵션·참조 이미지 경로·검수 항목 |

## 주의사항

- 본 스킬은 **프롬프트 텍스트만** 출력합니다. 실제 이미지는 Midjourney 웹 또는 Discord에서 사용자가 생성합니다.
- V8.1·V8.2의 Quality 파라미터는 미지원입니다. `--q 4`를 출력하지 않습니다.
- 캐릭터·객체 참조는 Edit Model을 사용합니다. V8 프롬프트에 `--oref`·`--cw`·`--cref`를 자동 삽입하지 않습니다.
- 고해상도 작업의 GPU 시간은 공식 문서와 현재 계정에서 확인합니다. Relax 사용 가능 여부도 계정 설정을 확인합니다.
- `--sref random`은 결과 재현 불가. 마음에 드는 결과가 나오면 실제 코드 확인·저장.
- Personalization (`--p`)은 현재 계정에서 Global Profile의 잠금 해제 여부를 확인합니다.
- 모든 출력 이미지는 사용자 책임으로 사용 (저작권·초상권·브랜드).

## 관련 스킬

| 스킬 | 관계 | 설명 |
|---|---|---|
| media-gpt-image-prompt | sibling | 동일 입력으로 GPT Image 2.5 공식 원칙 프롬프트 |
| media-gemini-3-image-prompt | sibling | 동일 입력으로 Gemini 5-component 어조 프롬프트 |
| Higgsfield MCP (Soul) | alternative | API 자동 생성 (시네마틱 이미지·캐릭터 단일 통합, MJ는 미포함) |

## 출처

1차 권장 출처 (공식):

- [Midjourney Documentation — Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List)
- [Midjourney Documentation — Style Reference (`--sref`)](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference)
- [Midjourney Documentation — Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)
- [Midjourney Documentation — Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)
- [Midjourney Documentation — GPU Speed](https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo)
- [Midjourney Documentation Hub](https://docs.midjourney.com/hc/en-us/categories/32013335627533-Documentation)

버전과 기능 지원 여부는 공식 Version 표를 우선합니다. 실제 출력 비용은 계정과 작업 조건에 따라 달라지므로 고정 배수로 계산하지 않습니다.
