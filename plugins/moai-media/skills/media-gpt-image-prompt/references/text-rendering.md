# GPT Image 2.5 — 이미지 안 텍스트 규칙

광고 카피·포스터 문구·다이어그램 라벨·슬라이드 숫자처럼 **글자가 정확해야 하는 이미지**에 적용합니다. 공식 가이드의 텍스트 원칙을 규칙으로 정리했습니다.

## 규칙 1 — 문구는 따옴표 안에, 원문 그대로

넣어야 할 문구를 큰따옴표로 감쌉니다. 한글·영문 모두 같습니다.

```text
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
```

## 규칙 2 — 위치와 서체를 적는다

| 속성 | 예 |
|---|---|
| 위치 | centered at the top third · bottom-right corner · along the left margin |
| 서체 | bold sans-serif · serif · handwritten · modern sans-serif like Inter |
| 굵기·색 | thin · bold · white · deep charcoal |
| 조판 | high contrast · clean kerning · centered |

```text
Typography: bold sans-serif, high contrast, centered, clean kerning.
```

## 규칙 3 — 몇 번 나오는지, 다른 글자는 없는지

공식 예시는 문구가 **정확히 한 번** 나오도록 요청하고, 추가 텍스트를 금지합니다.

```text
Render the tagline exactly once, clearly and legibly, integrated into the ad layout.
No extra text, no watermarks, no unrelated logos.
```

카드·패키지처럼 문구가 하나뿐이면 "ONLY"를 씁니다.

```text
Include ONLY this packaging text (verbatim):
"Christmas Memories Edition"
```

## 규칙 4 — 특이한 단어는 한 글자씩

브랜드명·조어·흔치 않은 철자는 필요할 때 글자 단위로 풀어 줍니다.

```text
The brand name is spelled T-H-R-E-A-D.
```

## 규칙 5 — 작은 글자·밀도 높은 정보는 품질을 비교

작은 글자, 정보가 많은 이미지, 여러 서체는 `quality=medium`과 `high`를 비교합니다. 슬라이드·차트·교재처럼 범례·축·각주가 있으면 공식 예시도 `high`를 씁니다.

## 규칙 6 — 결과에서 반드시 확인

생성 뒤 철자와 가독성을 직접 확인합니다. 다이어그램은 라벨이 맞는지뿐 아니라 **라벨 사이의 관계**(화살표 방향, 순서)도 확인합니다. 번역 편집이면 원래 언어로 남은 단어가 없는지 봅니다.

## 한글 텍스트

공식 가이드는 언어별 정확도 수치를 제시하지 않습니다. 한글 문구는 위 규칙을 그대로 적용하고, 결과를 음절 단위로 확인합니다. 짧은 문구일수록 안정적이므로 긴 본문은 이미지 밖(HTML·SVG·편집 툴)에서 얹는 편이 안전합니다.

```text
Poster headline (verbatim, Korean): "신선한 시작"
Typography: bold modern Korean sans-serif, deep charcoal, centered across the top third.
Render the headline exactly once. Every Hangul syllable must match the quoted text.
No extra text, no watermark.
```

## 자주 생기는 문제

| 증상 | 대응 |
|---|---|
| 글자 하나가 틀림 | 따옴표 + "verbatim, no extra characters" + 글자 단위 철자 |
| 문구가 두 번 나옴 | "exactly once" 추가 |
| 모르는 문구가 끼어듦 | "No extra text" / "Include ONLY this text" |
| 작은 글자가 뭉개짐 | 문구 줄이기, 위치·크기 명시, `quality=high` 비교 |
| 위치가 다름 | 위치를 구체적으로(top third, bottom-right) |

## 출처

- [OpenAI — Image prompting: Prompting fundamentals #5, Render exact text, Build slides, diagrams, and charts](https://developers.openai.com/api/docs/guides/image-prompting) (2026-09-13 확인)
