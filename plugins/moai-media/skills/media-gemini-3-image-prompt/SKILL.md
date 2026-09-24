---
name: media-gemini-3-image-prompt
description: |
  Google Gemini 3 Pro Image (a.k.a. Nano Banana Pro) 전용 이미지 프롬프트 빌더. 사용자 자연어 한 줄과 현재 런타임의 질문 채널로 프리셋·미세조정 정보를 수집해 Google 공식 가이드의 장면·구도·조명 원칙을 참고한 5-component 내부 템플릿([Subject+Adj] doing [Action] in [Location]. [Composition]. [Lighting]. [Style]. [Constraint/Text])으로 변환합니다. Google AI Studio · Vertex AI · Gemini 앱에 복붙 가능한 프롬프트를 만들고 GPT Image 2.5·Midjourney 프롬프트도 비교용으로 출력합니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "Gemini 이미지 프롬프트 만들어줘", "나노바나나 프롬프트"
  - "Nano Banana Pro 프롬프트", "Gemini 3 Pro Image 프롬프트"
  - "Google AI Studio 이미지 프롬프트", "Vertex AI 이미지 프롬프트"
  - "/media-gemini-3-image-prompt" (직접 호출)

  실제 이미지 생성은 media-production에서 현재 앱의 기본 도구를 선택하고, 사용자가 Higgsfield를 지정했을 때만 Higgsfield 경로를 사용합니다. 본 스킬은 프롬프트 텍스트 산출 전용입니다.
version: "1.1.5"
---

# Gemini 3 Pro Image Prompt Builder — 5-Component + 3-모델 동시 출력

> moai-media | 이미지 프롬프트 빌더 (텍스트 산출 전용)

## 개요

Gemini 3 Pro Image (Nano Banana Pro)는 Google DeepMind의 reasoning-driven 이미지 생성·편집 모델로, **Thinking Mode**, **Perfect Text Rendering**, **Search Grounding** (Google Search 연동), **Few-Shot Design** (최대 14개 reference 이미지)을 지원합니다. 자연어 프롬프트 어조는 **Creative Director가 장면을 지시하는 톤**이 가장 잘 동작합니다.

본 스킬은 사용자 요청을 Google 공식 가이드의 장면·구도·조명 지침을 참고한 내부 5-component 템플릿으로 변환합니다:

```
[Subject + Adjectives] doing [Action] in [Location/Context].
[Composition/Camera]. [Lighting/Atmosphere]. [Style/Media].
[Specific Constraint/Text]
```

각 component는 영문 문장으로 끝나며 마침표로 구분합니다. 키워드 나열식은 동작하지만 결과 품질이 떨어집니다.

특히 본 스킬은:

- **3개 모델 동시 출력**: Gemini 5-component 메인 + GPT Image 2.5(공식 가이드 원칙) + 현재 Midjourney V8(기본 V8.2)
- **프리셋 + 미세조정**: 4개 프리셋(제품샷·인물·일러스트·풍경) × 4 슬롯
- **Thinking vs Fast 모드 안내**: 복잡 구도·텍스트는 Thinking, 빠른 탐색은 Fast (Gemini 3.1 Flash Image)
- **카메라 하드웨어 지정**: GoPro · Fujifilm · disposable · iPhone 등 시각적 DNA를 결정하는 하드웨어 지시

실제 생성은 `media-production`에서 현재 앱의 기본 이미지 도구로 연결합니다. 사용자가 Higgsfield를 지정하면 `media-higgsfield-image`를 사용합니다. 본 스킬은 **프롬프트 텍스트만** 산출합니다.

## 트리거 키워드

Gemini 이미지 프롬프트 나노바나나 프롬프트 Nano Banana Pro 프롬프트 Gemini 3 Pro Image 프롬프트 Google AI Studio 이미지 Vertex AI 이미지 프롬프트 SynthID

## 워크플로우

```
사용자 자연어 한 줄
    ↓
[Round 1] 현재 런타임의 질문 채널 — 프리셋 선택 (제품샷·인물·일러스트·풍경)
    ↓
[Round 2] 현재 런타임의 질문 채널 — 프리셋별 미세조정 (3~4 슬롯)
    ↓
[Round 3] 현재 런타임의 질문 채널 — 화면비 + 이미지 내 텍스트 유무 + 카메라 하드웨어(선택)
    ↓
[내부] 슬롯 → 5-component 매핑
    ↓
[내부] 같은 슬롯 → GPT Image 2.5 공식 원칙 + MJ 키워드+파라미터 변환
    ↓
출력: 3개 모델 프롬프트 코드블록 + 권장 파라미터 + 한국어 해설
```

## 실행 규칙

### Round 1 — 프리셋 선택 (필수)

현재 노출된 질문 도구로 4개 프리셋 중 1개를 선택받습니다. 질문 도구가 없는 하위 실행에서는 필요한 선택을 blocker로 반환합니다. 비동기 질문 도구의 즉시 반환을 사용자의 답으로 간주하지 않습니다.

프리셋 슬롯 정의는 3개 이미지 프롬프트 빌더(gpt-image·gemini·midjourney)가 **공유하는 단일 원본**을 사용합니다. 원본은 `media-gpt-image-prompt` 스킬에 있으며, 각 프리셋 파일 안에 GPT·Gemini·Midjourney 세 모델의 어조 변환 가이드가 모두 포함되어 있습니다.

| 프리셋 | 적용 케이스 | 공유 슬롯 원본 |
|---|---|---|
| 제품샷 (권장) | 커머스 상품, 패키지 컷, 보석·시계 클로즈업 | `${CLAUDE_PLUGIN_ROOT}/skills/media-gpt-image-prompt/presets/product-shot.md` |
| 인물·캐릭터 | 인물 포트레이트, 페르소나, 광고 모델 | `${CLAUDE_PLUGIN_ROOT}/skills/media-gpt-image-prompt/presets/portrait.md` |
| 일러스트·아트 | 카드뉴스 일러스트, 책 표지, 컨셉 아트 | `${CLAUDE_PLUGIN_ROOT}/skills/media-gpt-image-prompt/presets/illustration.md` |
| 풍경·환경 | 배경 이미지, 시네마틱 배경, 여행 컷 | `${CLAUDE_PLUGIN_ROOT}/skills/media-gpt-image-prompt/presets/landscape.md` |

### Round 2 — 프리셋별 미세조정 (3-4 질문)

위 공유 슬롯 원본(`${CLAUDE_PLUGIN_ROOT}/skills/media-gpt-image-prompt/presets/<name>.md`)의 슬롯 정의를 따릅니다. 슬롯 데이터는 세 모델이 동일하게 사용하며, 본 스킬은 그중 Gemini Creative Director 어조 변환 가이드 섹션을 적용합니다.

### Round 3 — 화면비 + 텍스트 + 카메라 하드웨어(선택)

| 화면비 | Gemini 매핑 | 용도 |
|---|---|---|
| 1:1 (권장) | `aspect_ratio="1:1"` | SNS 정사각, 일반 |
| 16:9 | `"16:9"` | 와이드, 유튜브 |
| 9:16 | `"9:16"` | 릴스·쇼츠 |
| 4:5 | `"4:5"` | 인스타 피드 |
| 21:9 | `"21:9"` | 시네마틱 울트라와이드. GPT Image 2.5 API와 Midjourney에서도 지원 범위 안의 비율 |

Gemini는 추가로 `3:2`, `2:3`, `3:4`, `4:3`, `5:4`를 지원합니다. Gemini 3.1 Flash Image는 `1:4`, `4:1`, `1:8`, `8:1`도 추가 지원.

**카메라 하드웨어 옵션** (Gemini Creative Director 어조의 핵심):

| 옵션 | 시각적 DNA |
|---|---|
| 기본 (DSLR 50mm) | 깨끗·중성·표준 |
| Fujifilm X-T5 | 따뜻한 색감, film simulation 어조 |
| GoPro HERO12 | 광각, 액션·몰입감, 약간 distortion |
| Disposable film camera | 거친 입자, nostalgic flash, raw 무드 |
| iPhone 15 Pro | 깨끗 디지털, computational photography |

### 내부 처리 — 슬롯 → 5-Component 매핑

```
Component 1 — [Subject + Adjectives] doing [Action] in [Location]
Component 2 — [Composition/Camera Angle/Lens/Hardware]
Component 3 — [Lighting/Atmosphere]
Component 4 — [Style/Media]
Component 5 — [Specific Constraint/Text]
```

각 component는 영문 문장 1-2개. 마침표로 구분. 상세 규칙은 `references/prompt-blocks.md`.

### 내부 처리 — GPT Image 2.5 + MJ 변환

페어 스킬 media-gpt-image-prompt / media-midjourney-v8-prompt와 동일 로직.

### 출력 — 3개 모델 코드블록

```markdown
## 🎨 생성된 프롬프트 (3개 모델)

### 1) Gemini 3 Pro Image — Nano Banana Pro (메인)
```
<5-component 영문 문장>
```
**권장 파라미터**: `aspect_ratio=1:1`, `resolution=2K`, `mode=Thinking`
**Reference 이미지**: 최대 14개 첨부 가능 (`references/reference-images.md`)
**Search Grounding**: 데이터 시각화·지도·통계 그래프는 활성화 권장

### 2) GPT Image 2.5 — 모델을 지정할 수 있는 OpenAI API 또는 확인된 Higgsfield 연결
```
<공식 원칙 프롬프트 (단락 또는 라벨 섹션)>
```
**권장 파라미터**: `quality=medium`, `size=1024x1024`, `moderation=auto`

### 3) Midjourney V8.2 (사용자가 V8.1을 지정했다면 V8.1)
```
<키워드, 키워드, ... --ar 1:1 --raw --s 300>
```

### 📝 한국어 해설
- Gemini는 Creative Director 어조에 가장 잘 반응합니다 (chiaroscuro · golden hour backlighting · three-point softbox 등)
- Thinking Mode는 복잡 구도·텍스트·데이터 시각화에 유리, latency 증가
- 모든 출력 이미지에 SynthID 워터마크 자동 삽입 (imperceptible)

### 🔗 페어 스킬 (실제 이미지 생성)
- `media-production` — 현재 앱의 기본 이미지 생성 경로
- `media-higgsfield-image` — 사용자가 Higgsfield를 지정했을 때의 생성 경로
- `media-gpt-image-prompt` — GPT 어조 프롬프트 빌더 (sibling)
- `media-midjourney-v8-prompt` — MJ 어조 프롬프트 빌더 (sibling)
```

### 텍스트-우선 (Text-First) 워크플로우

이미지에 들어갈 텍스트가 길거나 복잡할 때 Google이 공식 권장하는 2-step 패턴:

1. 먼저 모델과 대화로 텍스트 컨셉을 다듬는다 ("이런 분위기에 어울리는 짧은 카피 추천해줘").
2. 그 다음 확정된 텍스트를 이미지 프롬프트에 verbatim으로 넣는다.

본 스킬은 Round 3에서 텍스트 길이가 30자 이상이면 Text-First 패턴을 사용하라고 자동 권고합니다.

## 사용 예시

**예시 1: 제품샷**
> "Gemini 이미지 프롬프트, 매트 블랙 머그 'MONDAY' 글자 들어간 제품샷"

→ Round 1: 제품샷 → Round 2: 머그/슬레이트/창문/3-4분 → Round 3: 1:1 + verbatim "MONDAY" + Fujifilm → Gemini 메인 + GPT + MJ 동시 출력.

**예시 2: 인포그래픽 (Search Grounding)**
> "나노바나나 프롬프트로 2026년 한국 SNS 사용자 수 비교 인포그래픽"

→ 일러스트 프리셋 선택 → Round 2 슬롯 → Search Grounding 활성화 안내 + Thinking Mode 권장.

**예시 3: 시네마틱 풍경 21:9**
> "Gemini 3 Pro Image 시네마틱 풍경 프롬프트, 한강 일몰 21:9"

→ 풍경 프리셋 → Round 2 → 21:9 + GoPro 와이드 → Gemini에는 `aspect_ratio=21:9`를 권장하고, GPT Image 2.5 API와 Midjourney의 별도 화면비 설정은 해당 서비스에서 지정하도록 안내.

## 출력 형식

| 산출물 | 형식 | 설명 |
|---|---|---|
| Gemini 3 Pro Image 프롬프트 | 영문 5-component 단락 | Google AI Studio / Vertex AI / Gemini 앱 복붙 |
| GPT Image 2.5 프롬프트 | 영문 단락 또는 라벨 섹션 | 정확한 2.5 모델 지정은 OpenAI API 또는 확인된 Higgsfield 연결에서만 가능. ChatGPT Work 기본 도구는 데스크톱 공식 문서상 `gpt-image-2` |
| Midjourney V8 프롬프트 | 짧은 설명 + 지원되는 `--파라미터` | Midjourney 웹 또는 Discord `/imagine` |
| 권장 파라미터 | 모델별 aspect/quality/mode | API/UI 설정 시 함께 입력 |
| 한국어 해설 | 마크다운 | 어조 차이·Thinking 모드·SynthID·비용 주의 |

## 주의사항

- 본 스킬은 **프롬프트 텍스트만** 출력합니다. 실제 이미지 생성은 페어 스킬을 사용하세요.
- Gemini 3 Pro Image의 모든 출력에는 SynthID 워터마크가 imperceptible하게 삽입됩니다 (Google 정책, 변경 불가).
- Thinking Mode는 latency가 증가하지만, 복잡 구도·다중 객체·데이터 시각화·정확한 텍스트가 필요할 때 필수입니다.
- Search Grounding으로 사실 기반 인포그래픽을 생성하더라도, 결과는 항상 별도 검증 필요 (모델이 정보를 잘못 해석할 가능성).
- 입력 토큰: Gemini 3 Pro Image 65,536 tokens, Flash 131,072 tokens. 출력 토큰: 32,768 (둘 다).
- Reference 이미지 첨부 시 첫 2-3개에 핵심 요소(스타일·캐릭터·구도)를 배치하고, 나머지는 부수적 스타일로 사용 권장.
- 마스킹 편집·낮↔밤 변환·다중 이미지 블렌딩은 가끔 비자연스럽거나 아티팩트 발생.

## 관련 스킬

| 스킬 | 관계 | 설명 |
|---|---|---|
| media-gpt-image-prompt | sibling | 동일 입력으로 GPT Image 2.5 공식 원칙 프롬프트 |
| media-midjourney-v8-prompt | sibling | 동일 입력으로 MJ 키워드+파라미터 프롬프트 |
| media-production | after | 현재 앱의 기본 이미지 도구로 생성 |
| media-higgsfield-image | after | 사용자가 Higgsfield를 지정했을 때 생성 |

## 출처

1차 권장 출처 (공식):

- [Google AI for Developers — Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Google DeepMind — Gemini 3 Pro Image product page](https://deepmind.google/models/gemini-image/pro/)
- [Google Cloud Documentation — Gemini 3 Pro Image (Vertex AI)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image)
- [Google Cloud Blog — Ultimate Prompting Guide for Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Google AI Studio — Gemini 3 Pro Image (Nano Banana Pro)](https://aistudio.google.com/models/gemini-3-pro-image)

업계 참고:

- [Atlabs AI — Ultimate Nano Banana Pro Prompting Guide 2026](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image)
- [WaveSpeed Blog — Google Nano Banana Pro: Complete Guide for 2026](https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026/)
- [Medium — Testing Gemini 3 Pro Image](https://medium.com/google-cloud/testing-gemini-3-pro-image-f585236ae411)

위 출처의 피사체·동작·장소·구도·스타일 지침을 바탕으로 5-component 내부 템플릿을 구성했습니다. 모델 ID·화면비·참조 이미지·Search Grounding 지원과 사용량은 실행 시점의 공식 문서에서 다시 확인합니다.

## References

| 파일 | 로드 조건 |
|------|-----------|
| references/search-grounding.md | 인포그래픽·지도·통계 그래프 등 실시간 사실 데이터가 필요한 이미지에서 Search Grounding 사용 여부를 판단할 때 |
