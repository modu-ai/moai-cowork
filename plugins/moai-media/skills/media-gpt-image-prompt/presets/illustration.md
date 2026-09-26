# Preset: 일러스트·아트 (Illustration)

카드뉴스 일러스트, 책 표지, 컨셉 아트, 브랜드 캐릭터, 인포그래픽용 일러스트.

## Round 2 슬롯 정의

### Q1 — 주제·소재

| 옵션 | 예시 매핑 |
|---|---|
| 동물·자연 (권장) | "a sleeping fox curled in autumn leaves, bushy tail wrapped around its paws" |
| 인물·캐릭터 | "a young illustrator at a wooden desk, surrounded by books and a single lamp" |
| 사물·정물 | "a still life of a coffee cup, an open notebook, and a brass fountain pen" |
| 추상·상징 | "an abstract composition of geometric shapes representing growth and renewal" |

### Q2 — 그림체·매체

| 옵션 | 예시 매핑 |
|---|---|
| 수채화 (권장) | "hand-drawn watercolor illustration, soft washes, visible paper texture" |
| 플랫 디지털 | "flat vector illustration, clean shapes, minimal shading, modern editorial style" |
| 펜&잉크 | "pen and ink line drawing, crosshatched shading, vintage book plate aesthetic" |
| 디지털 페인팅 | "digital painting, painterly brushstrokes, warm hand-painted animation palette" |

### Q3 — 색감·무드

| 옵션 | 예시 매핑 |
|---|---|
| 가을 따뜻 (권장) | "warm autumn palette — burnt orange, mustard yellow, deep red, dusty olive" |
| 파스텔 부드러움 | "soft pastel palette — blush pink, mint, lavender, cream" |
| 모노톤 | "monochromatic grayscale, ink black on cream paper" |
| 비비드 컨트라스트 | "high-contrast vivid palette — electric blue, magenta, lime green" |

### Q4 — 구도·시점

| 옵션 | 예시 매핑 |
|---|---|
| 정면 클로즈업 (권장) | "centered close-up composition, subject filling 70% of the frame" |
| 와이드 환경 | "wide environmental shot, subject small within a detailed scene" |
| 탑다운 플랫 | "top-down flat composition, isometric or perfectly orthogonal" |
| 사선·동적 | "dynamic diagonal composition, off-center subject, sense of motion" |

## 모델별 어조 변환 가이드

### GPT Image 2.5 (라벨 섹션 — 공식 가이드 원칙)
```
Create a <Q2> illustration of <Q1> for <use>.
Subject: <character or object details, expression, action>.
Style: <Q2 medium details: e.g. hand-painted watercolor look, soft outlines>, <Q3 palette>.
Composition: <Q4 composition>.
Constraints: original artwork, illustrated not photographic, no text, no watermark.
```
권장: `model=gpt-image-2.5-flare`, `quality=medium`.

### Gemini 3 Pro Image (5-component)
```
<Q1> rendered in <Q2 style>. <Q4 composition>. <Q3 palette>.
Illustrated, not photographic.
```

### Midjourney V8 (기본 V8.2)
```
<Q2 매체 키워드>, <Q1 키워드>, <Q4 키워드>, <Q3 팔레트 키워드>,
illustration not photograph --ar [Round 3] --s 400
```

(일러스트의 기본 스타일이 과할 때만 `--raw`를 사용자가 선택합니다.)

## 자주 쓰이는 보조 키워드

매체별 어조:
- watercolor: paper texture · wet-on-wet · soft edges · visible brushstrokes
- vector: clean shapes · solid fills · minimal gradients · editorial flat
- ink: crosshatch · stippling · vintage plate · woodcut feel
- digital paint: painterly · warm hand-painted animation · expressive digital painting

분위기:
- whimsical · serene · melancholic · dreamy · bold · playful

## 브랜드 캐릭터 일관성

여러 장에 같은 캐릭터를 등장시킬 때:

- GPT Image 2.5: 1장에서 `Character:` `Style:` `Constraints:` 섹션으로 캐릭터를 정의하고 단순한 배경으로 만든 뒤, 2장부터 그 이미지를 입력으로 넣고 `Character Consistency:` 섹션에 의상·얼굴·비율·팔레트를 다시 적습니다. 제약에 `Do not redesign the character`. (`references/editing-patterns.md` §캐릭터 일관성)
- Gemini 3 Pro Image: reference 이미지 첨부 가능 (최대 14장). "Maintain the exact character design from the reference."
- Midjourney V8: Edit Model에 참조 이미지를 첨부하고 유지할 얼굴·의상·색을 프롬프트에 적습니다. 웹은 Attach to prompt, Discord는 `--edit IMAGE_URL`을 사용합니다.
