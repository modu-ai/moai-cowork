# Gemini 3 Pro Image — Reference Image Strategy (Up to 14)

Gemini 3 Pro Image는 한 프롬프트에 참조 이미지를 **총 최대 14개** 섞을 수 있습니다. [Google의 공식 이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation#use-up-to-14-reference-images)의 유형별 표는 객체 최대 6개, 캐릭터 일관성 최대 5개, 스타일 참조 최대 3개를 구분합니다. 같은 가이드의 제한 절에는 고충실도 이미지 5개라고도 적혀 있으므로, 복잡한 입력은 5개 이하로 시작하고 실행 경로의 현재 한도를 확인합니다.

## 핵심 원칙

**적을수록 좋다.** 14개 슬롯이 있다고 모두 채우면 모델이 어떤 reference를 우선 따라야 할지 혼란스러워합니다. 권장:

- 단순 스타일 전이: 1-2개
- 브랜드 캐릭터 + 스타일: 3-4개
- 복잡 캠페인 (캐릭터 + 환경 + 색 팔레트 + 텍스처): 5-8개
- 14개 가까이 사용: 광고 시리즈처럼 매우 복잡한 case에서만

## 역할 지정 예시

| 역할 | Gemini 3 Pro Image 한도 | 예시 |
|---|---:|---|
| 고충실도 객체·제품 | 최대 6개 | 제품 형태·재질·라벨 |
| 캐릭터 일관성 | 최대 5개 | 얼굴·의상·비율 |
| 스타일 참조 | 최대 3개 | 그림체·팔레트·매체 |
| 구도·레이아웃 | 총량 14개 안에서 사용 | 카메라 앵글·여백·구성 영감 |

첨부 순서가 우선순위를 결정한다는 공식 보장은 없습니다. 객체·캐릭터·스타일 이미지를 실제 역할대로 세어 유형별 한도를 지킵니다.

## 프롬프트에서 reference 참조 방법

첨부 순서와 각 이미지의 역할을 프롬프트에 `Image 1`, `Image 2`처럼 명시합니다. 앱이나 API가 이 라벨을 자동 부여한다고 가정하지 않습니다.

```
Using the attached reference images:
- Image 1: main style reference — soft watercolor illustration aesthetic.
- Image 2: character reference — preserve the woman's face, hair, and outfit.
- Image 3: composition reference — three-quarter angle with subject off-center.

Generate <component 1>. <component 2>. <component 3>. <component 4>.
```

## 자주 쓰이는 패턴

### 패턴 A — 브랜드 캐릭터 일관성

```
Image 1: brand mascot reference (front view).
Image 2: brand color palette swatches.

Generate the same mascot in a new scene: <subject doing action in
location>. <composition>. <lighting>. <style>. Maintain the
mascot's exact face, body proportions, and color scheme from
Image 1. Use only the colors shown in Image 2.
```

### 패턴 B — 제품 + 스타일 전이

```
Image 1: product reference — sneaker side view, all logos and
colorways visible.
Image 2: lifestyle scene reference — wet city street at night,
neon reflections.

Generate the sneaker from Image 1 placed in a similar wet city
street setting as Image 2. <composition>. <lighting matching
Image 2>. Cinematic product photography. Maintain exact logo
placement and colorway from Image 1.
```

### 패턴 C — 시리즈 일관성 (광고 캠페인 5장)

```
Image 1: master style reference (mood + palette + lighting).
Image 2: model reference (face + outfit).
Image 3: typography reference (Hangul serif headline style).
Image 4: brand element reference (logo + tagline placement).

Generate scene 3 of 5 in the campaign series: <subject doing
action in location>. Match Image 1 style. Use the same model
as Image 2. Place a Hangul headline reading "<text>" in the
typography style of Image 3. Position the logo from Image 4 in
the top-right corner.
```

## 캐릭터·인물 일관성 팁

- 같은 인물을 여러 장에 등장시킬 때 첫 장의 frontal portrait를 reference 1번 슬롯에 고정.
- 프롬프트에 "preserve the face, hair, expression, and outfit from Image 1" 명시.
- 의상이 다를 경우 "same person, different outfit: <new outfit>" 형식.
- Gemini는 GPT Image 2.5의 Preserve list 어조를 그대로 이해합니다.

## 한계와 회피 방법

| 한계 | 회피 |
|---|---|
| 총 14개 또는 유형별 한도를 넘김 | 공식 한도를 확인하고 필요한 역할의 이미지만 첨부 |
| 작은 얼굴은 detail loss 가능 | reference에 얼굴 클로즈업 추가 |
| 마스킹 편집 가끔 unnatural | 단순 교체·합성으로 분할 |
| 낮↔밤 변환 artifact | 단계적 변환 (낮 → 황혼 → 밤) |
| 다중 이미지 블렌딩 disjointed | reference 슬롯 명시적 분리 |

## 출처

- [Google AI for Developers — Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Google Cloud Blog — Ultimate Prompting Guide for Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
- [Atlabs AI — Ultimate Nano Banana Pro Prompting Guide](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image)
