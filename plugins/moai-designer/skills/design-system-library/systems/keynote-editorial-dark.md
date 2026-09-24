---
version: alpha
name: keynote-editorial-dark
description: An opinionated premium editorial keynote recipe on a near-black canvas (never pure black). This is a compositional contract, not just a dark color theme. Signature moves — no filled gray cards (surface ladder + alpha-white hairline instead), one accent per slide, giant-number value>label>context three-tier hierarchy, four-corner chrome, hierarchy built from size and tracking (never weight-spam). A single azure accent does all the signal work; Pretendard carries CJK-safe editorial type. Token values are our own; the recipe follows widely-used premium-keynote conventions.

colors:
  canvas: "#0A0B0D"
  surface-1: "#121419"
  surface-2: "#1B1E24"
  surface-3: "#262A31"
  ink: "#F4F5F7"
  body: "#AAB0B8"
  muted: "#6E747D"
  faint: "#40454C"
  hairline: "rgba(255,255,255,.08)"
  hairline-strong: "rgba(255,255,255,.16)"
  accent: "#5E9BFF"
  accent-2: "#8FBAFF"
  accent-soft: "rgba(94,155,255,.12)"
  glow: "#3E7BE0"
  positive: "#45C08A"
  negative: "#E56B62"
  on-accent: "#0A0B0D"
  on-canvas: "#F4F5F7"

typography:
  stat-display:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 160px
    fontWeight: 600
    lineHeight: 0.92
    letterSpacing: -0.04em
    fontFeature: "tnum 1"
  display-xl:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 112px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.03em
  action-title:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -0.03em
  display-md:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.03em
  title-lg:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.02em
  subhead:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.01em
  lead:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: -0.005em
  body:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  label:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Pretendard, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  eyebrow:
    fontFamily: "Goorm Sans Code, monospace"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.16em
    textTransform: uppercase
  mono-meta:
    fontFamily: "Goorm Sans Code, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  micro-label:
    fontFamily: "Goorm Sans Code, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  nano-label:
    fontFamily: "Goorm Sans Code, monospace"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase

rounded:
  sm: 8px
  md: 12px
  lg: 16px
  pill: 9999px

spacing:
  gap-s: 20px
  gap-m: 40px
  gap-l: 64px
  margin-x: 128px
  margin-y: 88px
---

## Overview

`keynote-editorial-dark`는 다른 다크 시스템(clickhouse·vercel·linear.app)과 **팔레트가 어둡다는 점만 같고 성격이 다릅니다**. 저들이 "브랜드 다크 팔레트"라면, 이것은 **의견이 담긴 프리미엄 에디토리얼 키노트 레시피** — 색 토큰이 아니라 **구성 계약(compositional contract)**입니다. 프리미엄 키노트에서 흔히 관찰되는 절제된 다크 편집 미학(넓은 여백·거대숫자·단일 강조)을 슬라이드에 손으로 구현하기 위한 규율의 집합이며, 아래 토큰 값은 우리가 이 레시피용으로 직접 정한 값입니다.

캔버스는 순흑(#000)이 아닌 **near-black `{colors.canvas}`**. 이 미세한 밝기가 "검은 화면"과 "프리미엄 다크"를 가릅니다. surface는 채우기가 아니라 **래더(`{colors.surface-1/2/3}`)**로 한 단씩 올리고, 구분선은 오직 **알파화이트 hairline `{colors.hairline}`**입니다.

**시그니처 (다른 다크 시스템과 구별되는 지점):**
- **채운 박스 금지** — 채운 회색 카드 금지. 배경은 surface 래더, 구분은 알파화이트 hairline. 그림자·스포트라이트·대기그라디언트 없음.
- **거대숫자 value>label>context 3단** — Label(11px muted) > Value(140~160px, weight 600, tnum) > context(한 문장). 실제 수치를 쓰면 본문이나 각주에 출처·기준 기간을 붙인다.
- **4모서리 크롬** — 좌상 브랜드, 우상 파트/날짜, 좌하 저자, 우하 페이지(`05 / 12`). 전 슬라이드 공통.
- **슬라이드당 accent 1곳** — 시그널 색 `{colors.accent}`을 eyebrow·metric·rule 중 딱 한 곳에만. 다색 칩 남발이 가장 촌스럽다.
- **surface 래더 + 알파화이트 hairline** — 다크에서 유일한 테두리는 hairline. 카드 배경은 래더에서 한 단 올린 것.
- **크기·트래킹으로 위계** — 굵기 남발 금지. 한 슬라이드 폰트 크기 종류 ≤3. display 음수 트래킹 -0.03em, 스탯 -0.04em.

## Colors

### Surface Ladder
- **Canvas** (`{colors.canvas}`): near-black 기본 바닥. **순흑 금지**.
- **Surface 1/2/3** (`{colors.surface-1}` · `{colors.surface-2}` · `{colors.surface-3}`): 채우기가 아니라 한 단씩 올린 래더. 카드는 이 래더 위에 얹는다.
- **Hairline** (`{colors.hairline}`) / **Hairline Strong** (`{colors.hairline-strong}`): 다크의 유일한 테두리.

### Text
- **Ink** (`{colors.ink}`): 제목·주요 텍스트.
- **Body** (`{colors.body}`): 본문.
- **Muted** (`{colors.muted}`): 라벨·캡션·크롬 텍스트.
- **Faint** (`{colors.faint}`): 3차 텍스트·미세 구분.

### Accent & Signal
- **Accent** (`{colors.accent}`) / **Accent-2** (`{colors.accent-2}`): 단일 azure 시그널. 슬라이드당 1곳. `{colors.accent-soft}`는 활성 노드 그라디언트.
- **Glow** (`{colors.glow}`): 저조도 글로우.
- **Positive / Negative** (`{colors.positive}` · `{colors.negative}`): delta 값. 슬라이드당 ≤2종.

## Typography

### Font Family
sans/display는 **Pretendard**(한글 포함 전 위계), 코드/mono(eyebrow·메타·코드)는 **구름 산스 코드(Goorm Sans Code)** 단독. 폴백 스택은 `-apple-system, "Segoe UI"` / mono는 generic `monospace`.

### Scale
스케일(px): **11·14·16·18·22·28·40·56·80·112·160**. 한 슬라이드에서 크기 종류 ≤3. display 음수 트래킹 `-0.03em`, 스탯 숫자 `-0.04em`. mono 라벨은 양수 트래킹 `.1em` + uppercase. 숫자에는 `font-feature-settings: "tnum" 1`(tabular) — 자릿수 흔들림 방지.

### CJK 안전
body에 `word-break: keep-all; overflow-wrap: normal; line-break: strict;` 필수 — 없으면 한글이 음절로 깨진다.

### 폰트 라이선스
**Pretendard**는 SIL Open Font License 1.1(github.com/orioncactus/pretendard)로 상업 사용·수정·재배포 자유(폰트 단독 판매만 금지), 웹폰트 CDN 제공. 한국 스타트업 UI의 사실상 표준이라 "익숙한 프리미엄" 무드를 준다. 코드/mono 폰트는 **구름 산스 코드(Goorm Sans Code)** 단독 사용(SIL OFL, © goorm — 사용·수정·재배포 자유, 폰트 단독 판매만 금지).

## Layout

### Four-Corner Chrome
`.slide` 안에 `.frame` 형제로 4모서리 절대배치. safe margin `{spacing.margin-x}` 좌우 / `{spacing.margin-y}` 상하. 콘텐츠는 세로 정중앙이 아니라 **광학적 위 1/3~중앙** 앵커.

### Rhythm
`{spacing.gap-s}` · `{spacing.gap-m}` · `{spacing.gap-l}`로 수직 리듬. radius는 `{rounded.sm}` chip / `{rounded.md}` swatch·번호칩 / `{rounded.lg}` 코드·타일·목업.

## Component Catalog (note)

지배 오브젝트는 **8종**의 표준 컴포넌트로 고정하고, 슬라이드 1장 = 지배 오브젝트 1개입니다(새 컴포넌트 발명 금지):

**stat**(빅넘버 3단) · **flow**(파이프라인 단계, 활성 노드 accent-soft) · **bento**(타일 그리드, 유일하게 radius 박스 허용) · **timeline**(그라디언트 rail + glow dot) · **code**(mono, cmd/flag/str/cmt 토큰 컬러) · **steps**(각진 번호칩 절차) · **before-after**(neg/pos cap 미니 목업) · **gauge**(반원 게이지 단일 점수).

각 컴포넌트의 실제 CSS는 위 토큰(`{colors.*}`·타이포 스케일)을 바탕으로 이 스킬 안에서 구현합니다.

## Do's and Don'ts

### Do
- 모든 슬라이드를 near-black `{colors.canvas}` 위에 앉힌다. 순흑이 아니라 near-black.
- 구분은 알파화이트 hairline으로만. 카드가 필요하면 surface 래더에서 한 단 올린다.
- accent `{colors.accent}`는 슬라이드당 1곳(eyebrow·metric·rule 중 하나).
- 스탯은 거대숫자 3단(value>label>context)으로 표현하되, 실제 수치에는 출처·기준 기간을 연결한다.
- 위계는 크기·트래킹으로. 애매하면 굵기 대신 크기를 키운다.

### Don't
- 채운 회색 카드·그림자·스포트라이트·대기그라디언트 금지.
- 다색 칩 남발 금지 — accent는 슬라이드당 한 곳.
- 순흑(#000) 캔버스 금지 — near-black을 쓴다.
- 굵기 남발 금지(한 슬라이드 폰트 크기 종류 ≤3).
- 명사 나열 제목 금지 — 마침표로 끝나는 액션타이틀을 쓴다.

## Known Gaps
- 이 시스템은 **1920×1080 슬라이드 프레젠테이션** 문맥을 겨냥해 설계됐다. 일반 웹 랜딩/문서 렌더에 그대로 적용하면 margin(128/88px)·스케일(최대 160px)이 과할 수 있어 축소 프로파일이 필요하다.
- 라이트 프로파일은 값만 갈아끼우는 변형(canvas #F7F4EC / ink #1A1A1A / hairline rgba(0,0,0,.08))으로 지원하나, 본 엔트리는 다크 정본만 문서화한다.
- 색·타이포 토큰 값은 이 프리셋용으로 직접 정한 것이며, 프로젝트 브랜드에 맞춰 accent·surface 래더를 재정의할 수 있다.
