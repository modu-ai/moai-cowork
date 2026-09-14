# openai.md — GPT Image 계열 크래프트 (OpenAI)

> 대상 모델(라이브 카탈로그 기준, 2026-09-13 `models_explore` 조회): `gpt_image_2_5`, `gpt_image_2`, `openai_hazel`
> 파라미터·aspect·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** GPT Image는 1차 (OpenAI developers docs — [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting)). `openai_hazel` 매핑은 **unverified assumption**.
출처: https://developers.openai.com/api/docs/guides/image-prompting

## 모델 고르기 — `gpt_image_2_5` 우선

| Higgsfield | OpenAI 모델 | 쓰는 경우 |
|---|---|---|
| `gpt_image_2_5` + `variant=flare` (기본) | `gpt-image-2.5-flare` | 속도 우선. 화질은 GPT Image 2와 비슷한 수준 |
| `gpt_image_2_5` + `variant=sunburst` | `gpt-image-2.5-sunburst` | 품질 우선. GPT Image 2보다 높은 화질 |
| `gpt_image_2` | `gpt-image-2` | 이미 검증된 기존 워크플로 유지 시 |

`gpt_image_2_5` 파라미터: `quality` `low`·`medium`·`high`·`xhigh`·`max`(기본 `low` — 결과물이면 `medium` 이상 명시), `resolution` `1k`·`2k`·`4k`, `background` `auto`·`opaque`·`transparent`, `aspect_ratio` 다수. 프롬프트 작성 규칙 전체는 `moai-media:media-gpt-image-prompt`를 따른다.

---

## 공식 구조 (1차, OpenAI Image prompting 가이드)

`background/scene → subject → key details → constraints`. 의도한 용도(ad / UI mock / infographic)를 앞에 밝혀 완성도 수준을 설정한다. 복잡한 요청은 하나의 빽빽한 단락 대신 라벨 붙인 세그먼트나 줄바꿈으로 나눈다.

**길이**: 32,000자 하드캡. 권장 길이 없음. 공식 조언: *"Long prompts can work well, but debugging is easier when you start with a clean base prompt and refine with small, single-change follow-ups."*

## 텍스트 렌더링 (1차, R3)

리터럴 텍스트는 **따옴표**로 감싸고 위치·서체를 지정한다. 몇 번 나오는지("exactly once")와 추가 텍스트 금지를 적는다. 까다로운 단어는 **철자를 하나씩** 나열한다. 작은 텍스트/조밀한 레이아웃은 `quality: medium|high`. OpenAI caveat: *"Although significantly improved, the model can still struggle with precise text placement and clarity."*

## 편집 (1차, R4)

*"Change only X"* + 지킬 항목(정체성·형태·레이아웃·조명·라벨) 나열 + 제외 조건(워터마크·로고). 여러 입력은 **번호와 역할**(피사체·스타일·의상·배경)로 참조한다. 투명 누끼는 프롬프트와 `background=transparent`를 함께 쓴다.

**Do**: 구체적 재질·질감·매체; 프레이밍·시점·조명/무드; 사실성엔 사진 언어.
**Don't**: UI 목업에 컨셉아트 언어; 카메라 스펙이 문자 그대로 시뮬레이션된다는 가정; 한 프롬프트 과적재.

---

## `openai_hazel`은 그 이름으로 문서화되지 않음 (unverified)

**GAP — `openai_hazel`은 그 이름으로 어디에도 문서화돼 있지 않다.** "Hazel"은 OpenAI 자체 문서 **어디에도 나오지 않는다.** OpenAI가 공개한 이름은 `gpt-image-1`, `gpt-image-1.5`, `gpt-image-1-mini`, `gpt-image-2`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`뿐이다. 서드파티 트래커가 Hazel ≈ `gpt-image-1.5`라 주장하지만 **이는 unverified(미검증)**다.

**규칙**: 스킬은 GPT Image 컨벤션을 `openai_hazel`에 적용하되, 이를 벤더 확인된 사실이 아니라 **명시적으로 플래그된 unverified 가정**으로 다룬다. 실제 파라미터는 언제나 `models_explore`로 확인한다.
