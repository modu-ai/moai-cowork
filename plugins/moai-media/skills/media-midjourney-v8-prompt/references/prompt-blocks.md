# Midjourney V8 — 짧은 설명과 지원되는 파라미터

[공식 Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)는 짧고 구체적인 문구를 권합니다. 피사체·장면·구도·빛·매체 중 결과에 필요한 단서만 골라 쓰고 파라미터는 끝에 붙입니다.

## 표준 구조

```
[subject], [scene/setting], [composition], [lighting], [style/medium]
--ar W:H [--raw] [--hd] [--s 0~1000]
[--sref CODE_or_URL --sw 0~1000]
[--edit IMAGE_URL]
[--p PROFILE_ID]
[--no NEGATIVE_LIST]
[--c 0~100]
```

## Block 1 — Subject

가장 먼저 등장. 핵심 명사 + 형용사 2-3개.

예:
- `matte black ceramic coffee mug, ridge texture, MONDAY text`
- `30-year-old Korean woman, beige trench coat, gold earrings`
- `sleeping fox, autumn leaves, bushy tail`

## Block 2 — Scene / Setting

장소 + 시간대 + 공기감.

예:
- `wet slate countertop, Scandinavian kitchen, sunrise`
- `brick-walled Seoul cafe, late afternoon`
- `autumn maple forest, misty morning`

## Block 3 — Composition

앵글 + 렌즈 + 심도. MJ는 짧은 키워드를 잘 따름.

예:
- `three-quarter angle, 50mm, shallow DOF`
- `eye-level, 85mm portrait, blurred background`
- `top-down flat lay, 35mm, deep focus`

## Block 4 — Lighting

광원 + 방향 + 톤.

예:
- `soft window light, sunrise, cool tones, rim highlight`
- `chiaroscuro, single hard light from left, deep shadows`
- `golden hour backlight, warm tones, long shadows`

## Block 5 — Style / Medium

매체·장르·시각적 특징.

예:
- `editorial product photography, film grain`
- `editorial portrait, soft side light, cinematic framing`
- `warm hand-painted illustration, layered natural backgrounds`
- `anime cel-shading, thick lines, flat colors`

## 파라미터 순서 (관례)

```
--ar [필수]
--raw [선택, 자동 스타일을 줄이고 싶을 때]
--hd [선택, 2K 필요 시]
--s [선택, default 100, 0~1000]
--sref [선택, 스타일 참조. --sw로 영향력 조절]
--edit [선택, Discord에서 이미지 참조·편집]
--p [선택, profile 사용 시]
--no [선택, 제외 요소]
--c [선택, 시안 다양성]
```

## 완성 프롬프트 예시

### 예 1 — 제품샷 1:1

```
matte black ceramic coffee mug, ridge texture, "MONDAY" text,
wet slate countertop, Scandinavian kitchen, sunrise window
light, three-quarter angle, 50mm, shallow DOF, editorial product
photography, film grain --ar 1:1 --raw --s 250
```

고해상도가 필요하면 `--hd`를 추가하고 현재 계정의 GPU 시간을 확인합니다.

### 예 2 — 인물 9:16 캐릭터 일관성

```
30-year-old Korean woman, beige trench coat, gold earrings,
reading laptop, brick-walled Seoul cafe, late afternoon, warm
window light, eye-level, 85mm portrait, shallow DOF, editorial
candid, preserve the reference subject's face and coat --ar 9:16
--raw --edit https://example.com/ref.jpg --s 200
```

웹에서는 같은 이미지를 Attach to prompt에 넣습니다. 참조에서 지킬 얼굴·의상과 바꿀 배경을 문장으로 구분합니다.

### 예 3 — 일러스트 + Style Reference

```
watercolor illustration, sleeping fox, autumn leaves, soft
washes, paper texture, warm autumn palette, centered close-up
--ar 4:5 --sref 1234567890 --sw 300 --s 500
```

스타일 참조의 색·매체가 과하게 반영되면 `--sw`를 낮춥니다.

## V8 권장 시작점

| 케이스 | 권장 기본 |
|---|---|
| 제품샷 사진 | `--raw --s 250` (고해상도 요청이면 `--hd` 추가) |
| 인물 사진 | `--raw --s 200` (고해상도 요청이면 `--hd` 추가) |
| 일러스트 | `--s 500` (raw 없이) |
| 풍경·시네마틱 | `--raw --s 300` (고해상도 요청이면 `--hd` 추가) |
| 빠른 탐색 | 기본만 (--ar만) |

## 출처

- [Midjourney Documentation — Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List)
- [Midjourney Documentation — Prompt Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)
- [Midjourney Documentation — Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)
