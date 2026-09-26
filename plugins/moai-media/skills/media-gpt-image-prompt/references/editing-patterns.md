# GPT Image 2.5 — 편집 패턴

GPT Image 2.5는 두 모델 모두 정밀 편집과 피사체 보존이 좋아졌습니다. 그래도 **무엇을 바꾸고 무엇을 지킬지** 적지 않으면 얼굴·로고·텍스트·구도가 흔들립니다. API는 `images.edit`에 입력 이미지를 넘기고, 마스크가 필요한 부분 편집은 [image generation 가이드의 마스크 편집](https://developers.openai.com/api/docs/guides/image-generation#edit-an-image-using-a-mask)을 따릅니다.

## 기본 형식 — Change only / Preserve / Constraints

```text
Change only: <바꿀 요소. 바뀐 뒤 상태를 구체적으로>
Preserve: <지킬 항목>
Constraints: <제외 조건>
```

세 줄을 꼭 이 라벨로 쓸 필요는 없습니다. 공식 예시처럼 한 단락에 자연스럽게 풀어도 됩니다. 중요한 것은 **변경과 제약이 섞이지 않는 것**입니다.

| 지킬 항목 | 표현 예 |
|---|---|
| 정체성 | face, facial features, skin tone, body shape, pose, identity, expression, hairstyle, proportions |
| 제품 | product geometry, label legibility, proportions |
| 장면 | background, camera angle, framing, image quality |
| 조명 | lighting, shadows, color temperature, contact shadows |
| 레이아웃 | layout, labels, arrows, saturation, contrast |
| 주변 | surrounding objects |

| 제외 조건 예 |
|---|
| do not add accessories, text, logos, or watermarks |
| do not add new elements or text |
| do not restyle the product |
| do not redesign the character |

## 패턴 1 — 레이아웃을 지키며 번역

```text
Translate the text in the infographic to Spanish. Do not change any other aspect of the image.
```

권장: `quality=high`. 번역이 맞는지, 원래 언어로 남은 단어가 없는지 확인합니다.

## 패턴 2 — 스타일 전이

레퍼런스 이미지에 **팔레트·질감·매체** 같은 구체적 역할을 주고, 새 피사체는 따로 설명합니다.

```text
Use the same style from the input image and generate a man riding a motorcycle on a white background.
```

## 패턴 3 — 정체성은 지키고 의상만 교체

사람 사진 + 의상 레퍼런스 여러 장. 사람에서 고정할 것을 모두 적고 의상만 바꾸게 합니다. 제품·사물이 알아볼 수 있게 남아야 하는 편집에도 같은 구조를 씁니다.

```text
Edit the image to dress the woman using the provided clothing images.
Do not change her face, facial features, skin tone, body shape, pose, or identity in any way.
Preserve her exact likeness, expression, hairstyle, and proportions.
Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior.
Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on.
Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

## 패턴 4 — 여러 레퍼런스 결합

이미지에 번호를 붙이고 **무엇을, 어디로** 옮기는지와 그대로 둘 것을 적습니다.

```text
Place the dog from the second image into the setting of image 1, right next to the woman,
use the same style of lighting, composition and background. Do not change anything else.
```

## 패턴 5 — 투명 누끼(제품 컷아웃)

프롬프트에서 분리를 요청하고, API에서도 `background=transparent`를 지정합니다. PNG 또는 WebP, PNG에는 `output_compression`을 쓰지 않습니다. 후속 편집마다 투명 배경 유지를 다시 요청합니다.

```text
Extract the product from the input image and isolate it on a fully transparent background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing. Do not add a solid backdrop, checkerboard, scenery, or shadow.
Do not restyle the product; remove the background and preserve clean alpha transparency.
```

## 패턴 6 — 스케치를 실사로

레이아웃과 원근은 지키고, 재질·조명·환경으로 사실감을 더합니다. 새 요소를 넣지 말라고 적어 창작적 재해석을 막습니다.

```text
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

## 패턴 7 — 객체 하나 제거

없앨 것을 정확히 이름으로 부르고 나머지를 지킵니다.

```text
Remove the flower from man's hand. Do not change anything else.
```

## 패턴 8 — 사물 교체(인테리어)

한 물건만 바꾸고 카메라 앵글·조명·그림자·주변을 지켜 "재디자인"이 아닌 실제 사진처럼 보이게 합니다.

```text
In this room photo, replace ONLY the white chairs with chairs made of wood.
Preserve camera angle, room lighting, floor shadows, and surrounding objects.
Keep all other aspects of the image unchanged.
Photorealistic contact shadows and fabric texture.
```

## 패턴 9 — 인물을 새 장면에 삽입

정체성을 지키면서 조명·디테일·프레이밍·시선·장면과의 상호작용을 적습니다. 과한 영화 톤을 원치 않으면 명시적으로 뺍니다.

```text
Generate a highly realistic scene where this person is <action> in <place>. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
<Body framing, gaze, clothing, interaction with the scene>.
<Place, time of day, natural lighting, realistic colors>.
Preserve the person's facial features and proportions. Avoid cinematic lighting, dramatic color grading, or stylized composition.
```

## 여러 턴에 걸친 정제

1. 첫 결과를 만들고 확인한다.
2. 그 결과를 다음 편집 입력으로 넣고 **조건 하나만** 바꾼다. 예: `Make it look like a winter evening with snowfall.`
3. 결과가 흔들리면 지킬 항목을 다시 적는다.

### 캐릭터 일관성 (그림책·연재)

- **1장**: 캐릭터의 외형·비율·의상·성격을 라벨 섹션(`Character:` `Theme:` `Style:` `Constraints:`)으로 정의하고, 캐릭터가 잘 보이는 단순한 배경으로 만든다.
- **2장부터**: 1장 이미지를 입력으로 넣고 새 장면을 설명하되, `Character Consistency:` 섹션에 의상·얼굴·비율·팔레트를 **다시** 적는다. `Do not redesign the character`를 제약에 넣는다.

## 픽셀 단위로 같아야 할 때

반복 편집은 지키려던 디테일을 여전히 바꿀 수 있습니다. 특정 영역이 원본과 **완전히 같아야** 하면 프롬프트만 믿지 말고, 승인된 편집 결과를 원본 이미지에 합성합니다.

## 자주 생기는 문제

| 증상 | 대응 |
|---|---|
| 얼굴이 조금 달라짐 | 정체성 항목(face, facial features, skin tone, proportions, identity)을 모두 나열 |
| 텍스트·라벨이 사라짐 | 라벨을 지킬 항목에 넣고 원문을 따옴표로 다시 적음 |
| 새 소품이 생김 | "Do not add new elements" / "Do not change anything else" |
| 로고가 변형됨 | 제품 형태·라벨 가독성 보존을 명시 |
| 투명 배경이 흰 배경으로 | API `background=transparent` 재지정 + 프롬프트에 투명 유지 재요청 |

## 출처

- [OpenAI — Image prompting: Edit images / Refine an image across turns / More workflows](https://developers.openai.com/api/docs/guides/image-prompting) (2026-09-13 확인)
