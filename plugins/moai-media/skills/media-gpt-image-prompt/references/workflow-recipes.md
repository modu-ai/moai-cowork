# GPT Image 2.5 — 용도별 레시피

프리셋(제품샷·인물·일러스트·풍경)에 맞지 않는 용도의 슬롯 정의입니다. 각 레시피는 공식 가이드 예시의 **구조**를 따르며, 권장 파라미터는 공식 예시의 설정을 그대로 옮겼습니다. 예시 문장은 출발점일 뿐이니 사용자 자료로 바꿔 씁니다.

## 1. 사진 — 스타일과 조명 제어

- **슬롯**: 피사체와 행동 · 보이는 질감 · 촬영 방식(필름·프레이밍·렌즈 단서) · 빛 · 원치 않는 보정
- **형식**: 서술형 단락
- **파라미터**: `size=1024x1536`, `quality=medium`

```text
Create a photorealistic candid photograph of <subject> <action>.
<Skin, material, and wear details that should be visible>.
Shot like a 35mm film photograph, <framing> at eye level, using a 50mm lens.
<Light source>, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed. No glamorization, no heavy retouching.
```

## 2. 과정 설명 인포그래픽

- **슬롯**: 설명할 과정 · 대상 독자 · 전달할 정보(단계 순서) · 기술적 이해 수준
- **형식**: 서술형 2~3문장
- **파라미터**: `size=1024x1536`, `quality=medium` (라벨이 많으면 `high`)
- **검수**: 외형뿐 아니라 **라벨과 사실 관계**를 확인

```text
Create a detailed infographic of how <process> works, from <first step> to <last step>.
It should help <audience> understand the flow both technically and visually.
```

## 3. 정확한 텍스트가 들어간 광고

- **슬롯**: 브랜드·대상 고객 · 장면 · 태그라인(원문) · 시각 방향
- **파라미터**: `size=1024x1536`, `quality=medium`

```text
Create a <campaign type> image for a brand called <Brand>, a <brand description>.
The ad shows <scene> with the tagline "<exact tagline>".
Make it feel like a polished campaign image for <audience>: <tone adjectives>.
Use clean composition, strong color direction, natural poses, and premium <genre> photography cues.
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos.
```

## 4. 재사용 로고

- **슬롯**: 회사명·업종 · 느낌 · 형태 원칙(단순·실루엣·여백) · 투명 배경
- **파라미터**: `size=1024x1536`(정사각 로고면 `1024x1024`), `quality=medium`, `background=transparent`, `output_format=png`, `n`으로 변형 수
- **검수**: 작은 크기에서도 읽히는지, 알파 가장자리

```text
Create an original, non-infringing logo for a company called <Name>, <business>.
The logo should feel <tone>. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Fully transparent background. Deliver a single centered logo with generous padding, clean alpha edges, and no solid backdrop, scenery, checkerboard, or watermark.
```

## 5. 역사·실제 맥락 장면

- **슬롯**: 장소 · 날짜 · 사진 여부
- **파라미터**: `size=1024x1536`, `quality=medium`
- **검수**: 의상·무대·주변 환경의 시대 고증

```text
Create a realistic <scene type> in <place> on <date>.
Photorealistic, period-accurate clothing, staging, and environment.
```

## 6. 이야기를 만화 컷으로

- **슬롯**: 컷 수 · 컷별 시각적 비트(한 컷에 한 순간) · 방향(세로 릴스 등)
- **형식**: `Panel N:` 한 줄씩, 구체적인 행동 위주
- **파라미터**: `size=1024x1536`, `quality=medium`

```text
Create a short vertical comic-style reel with <N> panels.
Panel 1: <concrete action, framing, and emotion>
Panel 2: ...
Panel N: <payoff>
```

## 7. 인터페이스 미리보기

- **슬롯**: 제품 종류 · 화면 구성(헤더·목록·섹션) · 톤 · 기기 프레임
- **요령**: 이미 출시된 제품처럼 설명한다. "concept art" 같은 표현을 피해 스케치가 아닌 실사용 화면처럼 보이게 한다.
- **파라미터**: `size=1024x1536`, `quality=medium`

```text
Create a realistic mobile app UI mockup for <product>.
Show <screen content: header, list items with small photos and categories, a section, basic info>.
Design it to be practical and easy to use. <Background>, <accent colors>, clear typography, and minimal decoration.
It should look like a real, well-designed app. Place the UI mockup in an iPhone frame.
```

## 8. 과학·교육 자료

- **슬롯**: 대상 학습자 · 학습 목표 · 시각 형식 · 필수 구성요소 · 필수 라벨 · 넣지 말 것
- **요령**: 교수설계 브리프처럼 쓴다. 평면적이고 일관된 아이콘, 명확한 화살표, 읽기 쉬운 라벨, 충분한 여백.
- **파라미터**: `size=1536x1024`, `quality=high`

```text
Create a simple <subject> diagram titled "<Title>" for <audience>.
Show <concept>. Include <required stages>.
Use arrows to connect the steps, and label the main <items>: <label list>.
Make it look like a clean classroom handout or slide, with a white background, simple icons, clear labels, and easy-to-read text.
Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand.
```

## 9. 슬라이드 · 다이어그램 · 차트

- **슬롯**: 산출물 종류(슬라이드 1장·워크플로 다이어그램·차트) · 캔버스와 위계 · **실제 숫자와 라벨** · 시각 언어 · 금지 요소
- **요령**: 그림 요청이 아니라 **산출물 사양서**처럼 쓴다. 숫자·라벨·각주를 프롬프트에 직접 넣는다. 예시 숫자는 반드시 검증된 데이터로 바꾼다.
- **파라미터**: `size=1536x864`, `quality=high`

```text
Create one <deck type> slide titled "<Title>".
Use <background>, modern sans-serif typography like Inter, and a crisp, minimal layout. The slide should include:
* <Chart or diagram type> in <colors>
* <Exact figures with labels>
* <Second visual with axis range>
* Small footnotes: "<source 1>" and "<source 2>"
* <Logo placeholder position>
The design should look professional: highly readable text, clear data hierarchy, polished spacing.
Avoid clip art, stock photography, gradients, shadows, decorative elements, or anything generic or overdesigned.
```

## 10. 시즌 카드

- **슬롯**: 장면 · 감정 톤 · 재질 · 조명 · 카드 문구(원문)
- **파라미터**: `size=1024x1536`, `quality=medium`

```text
Create a <holiday> card illustration.
Scene: <scene with specific objects and story cues>
Mood: <tone words>
Style: <premium photography or paper pop-up cues: paper layers, fibers, folds, soft studio lighting>
Constraints:
- Original artwork only
- No trademarks, no watermarks, no logos
Include ONLY this card text (verbatim):
"<card copy>"
```

## 11. 굿즈·패키지 콘셉트

- **슬롯**: 제품 형태 · 콘셉트 · 재질·인쇄 선명도 · 패키지 문구(원문)
- **파라미터**: `size=1024x1536`, `quality=medium`

```text
Create a collectible <item> of <design description>, in <packaging type>.
Concept: <story behind the product>
Style: premium toy photography, realistic <material> textures, studio lighting, shallow depth of field, sharp label printing, high-end retail presentation.
Constraints:
- Original design only
- No trademarks, no watermarks, no logos
Include ONLY this packaging text (verbatim):
"<packaging copy>"
```

## 12. 광고판 목업 → 조건 하나씩 바꾸기

- 1턴: 제품 이미지를 입력으로 광고판 장면 생성, 문구는 원문·서체·횟수 명시
- 2턴: 1턴 결과를 입력으로 `Make it look like a winter evening with snowfall.`처럼 한 조건만 변경
- **파라미터**: `size=1024x1536`, `quality=medium`

## 출처

- [OpenAI — Image prompting: Generate images / More workflows / Refine an image across turns](https://developers.openai.com/api/docs/guides/image-prompting) (2026-09-13 확인)
