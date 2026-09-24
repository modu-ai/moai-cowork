# universal-rules.md — 벤더 교차 공통 규칙 (R1–R5)

> `media-higgsfield-core` | 여러 벤더의 공식 자료를 바탕으로 정리한 공통 프롬프트 크래프트 규칙.
> 계열별 예외·상세는 각 `references/prompt-craft/*.md`. 여기 있는 규칙이 그 파일들의 공통 토대다.

**Evidence tier:** 1차 (Google · Black Forest Labs · Kling · ByteDance · Alibaba · Higgsfield 공식 문서에서 교차 확인)

규칙마다 확인된 공식 자료의 수와 적용 범위가 다르다. Soul·Grok처럼 공식 프롬프트 공식이 없는 계열은 해당 `prompt-craft` 파일에서 적용 가능한 R1–R5로 폴백한다.

---

## R1–R5 규칙 정의

**R1 — 선택한 모델의 스키마에 없는 negative prompt 필드는 보내지 않는다.**

Higgsfield의 [공식 프롬프트 안내](https://github.com/higgsfield-ai/skills/blob/main/higgsfield-generate/references/prompt-engineering.md)는 **대부분 모델**에서 `negative_prompt`를 노출하지 않는다고 설명한다. 선택 모델의 현재 입력 스키마를 조회해 필드 유무를 확인한다. 벤더의 저술 예시는 다음과 같다:

| 벤더 | 공식 문구 |
|---|---|
| Google (Veo) | *"describe what you wish to exclude … 'a desolate landscape with no buildings or roads' instead of 'no man-made structures'."* |
| Black Forest Labs (FLUX.2) | negative prompt를 아예 지원하지 않음 — *"sharp focus throughout"* / *"an empty scene."* |
| Kling | *"supplement negative prompt via negative sentences within positive prompts."* (자체 API에 필드가 있어도 이 방식을 권장) |
| Higgsfield (`prompt-engineering.md`) | *"tack sharp"* (not *"not blurry"*) |

**적용**: 조회한 스키마에 `negative_prompt`가 없으면 파라미터를 보내지 않고, 제외하려는 대상은 긍정적 장면 요소로 전환한다("empty street"). 스키마에 필드가 있다면 그 모델의 지침과 사용자 요청에 맞춰 사용 여부를 결정한다.
출처: https://ai.google.dev · https://docs.bfl.ai

**R2 — image-to-video에서는 시작 이미지가 이미 담고 있는 것을 프롬프트에서 뺀다.**

이 규칙을 명시한 벤더는 둘뿐이고, 서로 일치한다:
- **Wan (Alibaba, 공식)**: image-to-video 공식은 문자 그대로 `Motion + Camera movement` — *"Focus prompt on movement descriptions and specific camera directions rather than static elements."*
- **Higgsfield (`prompt-engineering.md`)**: 입력 이미지에 이미 있는 정적 시각 정보를 다시 서술하지 말고, 동작 동사로 움직임을 이끈다.

**적용**: `medias[].role`에 `start_image`/`image`가 포함되면, 조립되는 프롬프트는 주제·장면 재서술을 버리고 motion + camera로 시작한다.
출처: https://help.aliyun.com/zh/model-studio · https://github.com/higgsfield-ai/skills

**R3 — 이미지 속 리터럴 텍스트는 따옴표로 감싸고 폰트를 함께 지정한다.**

Google·OpenAI·Black Forest Labs·Recraft에서 독립 확인. Google 공식 예시(verbatim):
> *"For the top line, the word 'GLOW' in a flowing, elegant Brush Script font. For the middle line, the text '10% OFF' in a heavy, blocky Impact font."*

**적용**: 리터럴 텍스트는 반드시 큰따옴표 + 명시적 font/weight/placement로 지정한다. 텍스트 렌더링 모델(`gpt_image_2_5`, `gpt_image_2`, `openai_hazel`, `nano_banana_pro`)에서 단일 최고 레버리지 규칙이다.
출처: https://ai.google.dev

**R4 — 편집 프롬프트는 바꿀 것과 반드시 보존할 것을 함께 명시한다.**

- **OpenAI**: *"Change only X"* + *"keep everything else the same"*; 반복마다 보존 목록을 다시 적어 드리프트를 막는다.
- **BFL Kontext**: `Replace '[original text]' with '[new text]'`. 동사 선택이 핵심 — *"change"*는 정체성 보존, *"transform"*은 전면 교체 신호. 주체를 명시적으로 앵커링한다.
- **ByteDance Seedream**: *"Replace the largest bread man with a croissant man, keeping the action and expression unchanged."*
- **Google (Gemini Omni)**: 역방향 경고 — *"Simple prompts work best for video editing. Overly descriptive prompts can lead to unintended changes."*

**적용**: 편집 프롬프트는 짧게, 단일 변경을 명시하고, 불변항(invariants)을 열거한다.
출처: https://platform.openai.com · https://docs.bfl.ai

**R5 — 프롬프트 길이의 보편 상한은 없다. 벤더별로 다르고 대개 미명시다.**

| 계열 | 공식 길이 가이드 | Tier |
|---|---|---|
| Higgsfield (일반) | 약 200 토큰 소프트 상한 — *"lengthier requests cause model distortion"* | 1차 |
| OpenAI GPT Image | 32,000자 하드캡, 권장 길이 없음 | 1차 |
| FLUX.2 | 10–30 words(탐색) / **30–80 words(권장)** / 80–300+(복잡). 32K 토큰 캡 | 1차 |
| Kling | 2,500자(`negative_prompt` 기준, `prompt` 대칭 가정) | 1차-relayed |
| MiniMax | 2,000자 | 1차 |
| Google Veo / Nano Banana | 상한 명시 없음 | 1차 |
| Wan | 상한 명시 없음(의도적으로 규정하지 않음) | 1차 |
| ByteDance Seedance / Seedream | 상한 명시 없음(직접 검색으로 부재 확인) | 1차 |

**Higgsfield 자체 자료의 내부 모순**: `prompt-engineering.md`의 약 200-토큰 상한은 Higgsfield 자신의 Cinema Studio 예시(500+ 단어)에서 위반된다. 있는 그대로 보고하며, 억지로 화해시키지 않는다.

**적용**: 길이는 대상 모델의 계열 파일이 정한 값을 따른다. 공통 규칙으로는 상한을 강제하지 않는다.
출처: https://docs.bfl.ai · https://ai.google.dev

---

## 이 규칙들이 core에 있는 이유

여러 계열에서 재사용하는 규칙이므로 계열 파일에 중복 배치하지 않고 여기 한 곳에 둔다. 계열별로 R1–R5와 **충돌**하는 벤더 지침이 있으면 해당 `prompt-craft` 파일에서 예외를 명시한다. 입력 파라미터의 최종 기준은 현재 연결에서 조회한 선택 모델의 스키마다.
