# GPT Image 2.5 — 프롬프팅 기본 원칙

OpenAI 공식 이미지 프롬프팅 가이드가 제시하는 8가지 원칙을 실제 작성 절차로 풀었습니다. 출발점은 늘 같습니다. **필요한 이미지부터 정하고, 피사체·구도·스타일·제약을 적는다. 편집이면 바뀔 것과 그대로 둘 것을 가른다. 한 번에 하나씩 고치고 결과를 본다.**

## 1. 결과를 정의한다

피사체와 **용도**를 첫 문장에 둡니다. 용도가 제품 사진인지 광고인지 다이어그램인지에 따라 모델이 고르는 구도·질감·정보 밀도가 달라집니다. 화면비와 중요한 배치 제약도 여기서 밝힙니다.

- 약함: `a coffee mug`
- 강함: `Create a photorealistic product photograph of a matte black ceramic coffee mug for an online store listing, centered, with generous negative space on the right for copy.`

요청이 복잡하면 **장면(scene) → 피사체(subject) → 디테일(details) → 제약(constraints)** 순서의 라벨 섹션으로 나눕니다.

## 2. 읽고 고치기 쉬운 형식을 고른다

짧은 프롬프트, 서술형 단락, JSON 비슷한 구조, 지시문, 태그 — 모두 같은 의도를 표현할 수 있습니다. 특수 문법은 없습니다. **요구사항을 읽고 고치기 가장 쉬운 형식**을 고릅니다.

| 상황 | 권장 형식 |
|---|---|
| 사진 한 장, 요구가 단순 | 서술형 단락 3~5문장 |
| 텍스트·레이아웃·여러 요소가 얽힘 | `Scene:` `Subject:` `Style:` `Constraints:` 라벨 섹션 |
| 여러 컷(만화·스토리보드) | `Panel 1:` … `Panel N:` 컷별 한 줄 |
| 슬라이드·차트 | 산출물 사양서처럼 목록(`*`)으로 숫자·라벨 나열 |
| 캐릭터 연속 | `Character:` `Scene:` `Character Consistency:` `Constraints:` |

## 3. 보이는 디테일을 적는다

재질, 조명, 색, 시각 매체를 적습니다.

- 사진이 목표면 **"photorealistic" 또는 "real photograph"를 명시**하고 프레이밍과 질감을 적습니다.
- 카메라 사양(35mm film, 50mm lens)은 **외형을 이끄는 단서**이지 물리적으로 정확한 시뮬레이션을 보장하지 않습니다.
- 넓은 풍경·시네마틱·저조도·비·네온 장면은 "moody" 같은 분위기 단어만 쓰지 말고 **규모·대기·색**을 구체적으로 적습니다.
- 과한 보정이 싫으면 제외 조건으로 적습니다: `No glamorization, no heavy retouching.`

예 (공식 가이드의 사진 예시 구조):

```text
Create a photorealistic candid photograph of <subject> <doing what>.
<visible texture details: skin, materials, wear>.
Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed. No glamorization, no heavy retouching.
```

## 4. 인물과 동작을 구체화한다

몸의 프레이밍, 상대적 크기, 시선, 사물과의 상호작용을 적습니다.

- `full body visible, feet included`
- `looking down at the open book`
- `hands naturally gripping the handlebars`
- `She is centered in the image but looking away from the camera`

## 5. 텍스트는 정확히

필요한 문구는 따옴표 안에 넣고 위치와 서체를 적습니다. 몇 번 나와야 하는지, 다른 텍스트는 넣지 말라는 것도 적습니다. 특이한 단어·브랜드명은 한 글자씩 풀어 씁니다. 작은 글자·정보가 많은 이미지·여러 서체는 `quality=medium`과 `high`를 비교합니다. 상세: `text-rendering.md`.

## 6. 변경과 제약을 분리한다 (편집)

"change only X"라고 쓰고 지킬 항목(정체성·형태·레이아웃·조명·라벨)을 나열합니다. 원치 않는 텍스트·로고·워터마크를 제외 조건으로 적습니다. 정밀한 부분 편집이면 채도·대비·화살표·카메라 앵글·주변 사물까지 "그대로"라고 적습니다. 상세: `editing-patterns.md`.

## 7. 레퍼런스에 역할을 준다

입력 이미지마다 **번호와 역할**(피사체·스타일·의상·배경)을 붙이고, 어떻게 합칠지와 어떤 요소를 어디로 옮길지 적습니다.

```text
Place the dog from the second image into the setting of image 1, right next to the woman,
use the same style of lighting, composition and background. Do not change anything else.
```

## 8. 한 번에 하나씩 반복한다

이전 결과를 다음 편집 입력으로 넣고, **한 가지만** 바꾸고, 지킬 항목을 다시 적습니다. "same style as before" 같은 표현이 맥락을 이어 주기도 하지만, 결과가 흔들리면 핵심 제약을 다시 명시합니다. 지시를 더 얹기 전에 결과부터 비교합니다.

## 작성 전 점검표

- [ ] 첫 문장에 산출물 종류와 용도가 있는가
- [ ] 화면비·배치 제약이 있는가 (크기 자체는 API `size`로 따로 넘긴다)
- [ ] 재질·조명·색·매체 중 목표에 필요한 것을 적었는가
- [ ] 사진이 목표면 photorealistic을 명시했는가
- [ ] 인물이 있으면 프레이밍·시선·동작이 있는가
- [ ] 텍스트는 따옴표 + 위치 + 서체 + 횟수 + "no extra text"인가
- [ ] 제외할 것(워터마크·무관한 로고·추가 텍스트)을 적었는가
- [ ] 편집이면 "change only"와 지킬 항목을 분리했는가
- [ ] 레퍼런스가 여럿이면 번호와 역할을 붙였는가

## 완성 예시 — 제품샷 (라벨 섹션)

```text
Create a photorealistic product photograph of a matte black ceramic coffee mug for an online store listing.
Scene: a minimalist Scandinavian kitchen at sunrise, the mug on a wet slate countertop next to a folded linen napkin.
Subject: the mug has a subtle ridge texture and a matte finish, three-quarter angle.
Details: 50mm lens look, shallow depth of field, soft directional window light with a cool morning tone and a gentle rim highlight, editorial product photography, subtle film grain.
Text (verbatim): "MONDAY" printed once on the side of the mug in thin uppercase sans-serif, clearly legible.
Constraints: no extra text, no watermark, no unrelated logos.
```

권장 파라미터: `model=gpt-image-2.5-flare`, `size=1024x1024`, `quality=medium`.

## 출처

- [OpenAI — Image prompting: Prompting fundamentals](https://developers.openai.com/api/docs/guides/image-prompting#prompting-fundamentals) (2026-09-13 확인)
