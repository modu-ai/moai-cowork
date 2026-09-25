---
name: doc-html-report
description: |
  마크다운 보고서를 브라우저에서 열리는 단일 HTML 파일로 구성합니다. 선택한 폰트·디자인 시스템에 따라 인터넷 연결이 필요할 수 있으므로 오프라인 결과를 확인합니다.
  다음과 같은 요청 시 사용하세요:
  - "이 보고서 HTML 파일로 만들어줘"
  - "주간 현황 보고서를 하나의 HTML로 렌더해줘"
  - "재무제표를 HTML 보고서로 변환해줘"
  - "인시던트 리포트를 HTML로 정리해줘"
  - "프린트 가능한 사업계획서 HTML로 만들어줘"
  - "이메일에 붙일 수 있는 HTML 리포트 만들어줘"
  현황·인시던트·사업계획·설명서·재무·PR 6종 서식 중 보고서 내용에 맞는 것을 고릅니다.
  PDF 파일이 필요하면 현재 사용 가능한 변환 기능을 확인하고 실제 변환 결과의 내용·레이아웃을 검사하세요.
version: "1.2.2"
---

# doc-html-report: 단일 파일 HTML 보고서 렌더러

## 목적과 범위

`moai-officer:doc-html-report`는 보고서용 HTML 서식과 작성 절차를 제공합니다.
`moai-coworker:collab-exec-summary`, `moai-accountant:finance-financial-statements`, `moai-consultant:consult-sbiz365` 등이 생성한 마크다운 보고서를 참고해 단일 HTML 파일을 작성합니다. 이 스킬에는 자동 변환 실행기가 포함되어 있지 않습니다.

**핵심 원칙**:
- 외부 JS 라이브러리(Chart.js, D3, htmx) 0 의존
- 외부 CSS 프레임워크(Tailwind, Bootstrap) 0 의존
- 인라인 SVG로 차트 직접 렌더링
- 한국어 폰트 CDN은 선택 사항으로 두고, 연결되지 않을 때 시스템 서체로 읽을 수 있게 한다

**이 스킬은 마크다운 출력을 대체하지 않습니다.** 마크다운은 단일 진실(source of truth)로 유지되며, HTML 렌더링은 추가 분기로만 작동합니다.

---

## 입력

| 인자 | 필수 | 기본값 | 설명 |
|------|------|--------|------|
| `markdown` | ✓ | — | 변환할 마크다운 본문 |
| `mode` | ✓ | — | `status` \| `incident` \| `plan` \| `explainer` \| `financial` \| `pr` |
| `design_system` | — | 기본 템플릿 | `moai-designer:design-system-library`에서 현재 확인한 브랜드 시스템. 외부 CDN을 쓰는 구현은 인터넷 연결 필요 |
| `slug` | — | 제목에서 정함 | 출력 파일명 prefix |
| `output_path` | — | `<cwd>/reports/<slug>-<YYYYMMDD>.html` | 출력 경로 |
| `font_stack` | — | 모드별 기본값 | 폰트 매핑 오버라이드 |

템플릿의 `{{변수}}`는 작성용 슬롯 표기다. 렌더러가 제공되지 않으므로 슬롯을 채운 뒤 `{{...}}` 잔류 여부를 확인한다. 사용자가 제공한 문구는 HTML로 이스케이프하고, 링크는 허용한 `https:` URL인지 확인한다. `*_html`처럼 이름에 HTML이 있어도 일반 텍스트 슬롯이다. SVG·HTML 구조가 필요하면 검증된 데이터로 직접 작성하고 스크립트·이벤트 속성·외부 참조가 없는지 확인한다. 확인할 수 없으면 텍스트나 표로 표현한다.

차트와 지표는 원본에 있는 값만 사용한다. 시계열 중간값, 증감률, 원인 설명이 원본에 없으면 그려 넣지 않고 해당 칸을 비우거나 차트를 생략한다. 전체 보고서 변환 요청에서는 템플릿에 없는 원본 섹션도 별도 표·섹션으로 보존한다. 사용자가 요약본을 요청해 생략할 때만 빠진 범위를 산출물에 밝힌다. 저장된 `references/samples/`와 `references/integration-tests/`는 가상 서식 자료이며 새 문서의 사실 출처나 현재 호스트의 품질 판정으로 쓰지 않는다.

---

## 출력

단일 `.html` 파일 (`<cwd>/reports/<slug>-<YYYYMMDD>.html`):
- 크기: 본문과 포함된 이미지·스타일에 따라 달라짐
- 외부 의존성: 선택한 폰트·디자인 시스템에 따라 달라짐. 외부 리소스가 있다면 자체 완결형이라고 표시하지 않음
- 오프라인 사용: 파일을 네트워크 없이 열어 내용과 스타일을 확인한 경우에만 표시

---

## 6개 모드

### 제공하는 템플릿 모드

| 모드 | 구조 섹션 | 대상 스킬 |
|------|-----------|-----------|
| **`status`** | 메트릭 카드 4개 · 하이라이트 · 완료 테이블 · Velocity SVG 막대 차트 · Carryover | `moai-coworker:collab-exec-summary`, `moai-officer:productivity-briefing` |
| **`incident`** | TL;DR 다크 배너 · 타임라인 · 로그 발췌 `<details>` · 코드 diff 패널 · 영향 테이블 · 액션 체크리스트 | `moai-lawyer:legal-compliance-check` |
| **`plan`** | 요약 KPI 스트립 · 마일스톤 수직 타임라인 · 데이터 플로우 SVG · 슬라이스 테이블 · 리스크 그리드 · 성공 지표 | `moai-consultant:consult-sbiz365` |
| **`explainer`** | 사이드 네비 · `<details>` 접이식 단계 · 탭 코드 블록(vanilla JS) · FAQ 아코디언 · 콜아웃 박스 | 설명형 문서 |
| **`financial`** | KPI 카드 4개 · 손익계산서 테이블(항목/당기/전기/증감/증감률) · Variance SVG 수평 막대 차트 · 주석 패널 | `moai-accountant:finance-financial-statements` |
| **`pr`** | TL;DR · PR 메타 행(파일수·+/−·브랜치) · Before/After 2단 카드 · 파일 투어 `<details>` · 핵심 포인트 · 테스트 체크리스트 · 롤아웃 단계 | `moai-accountant:finance-investor-relations` |

#### 모드별 입력 항목 요약

각 서식이 채우는 주요 항목입니다(템플릿 내부 변수명 기준).

| 모드 | 주요 입력 항목 |
|------|-------------------|
| `status` | `{{title}}`, `{{#metrics}}`, `{{#highlights}}`, `{{#completed_rows}}`, `{{#chart_bars}}` |
| `incident` | `{{inc_id}}`, `{{severity}}`, `{{title}}`, `{{#tl_entries}}`, `{{#impact_rows}}`, `{{#actions}}` |
| `plan` | `{{title}}`, `{{#kpis}}`, `{{#milestones}}`, `{{diagram_svg}}`, `{{#slices}}`, `{{#risks}}`, `{{#metrics}}` |
| `explainer` | `{{title}}`, `{{lead}}`, `{{#steps}}`, `{{#config_tabs}}`, `{{#faq_items}}` |
| `financial` | `{{title}}`, `{{period}}`, `{{#kpis}}`, `{{#statement_rows}}`, `{{chart_height}}`, `{{#variance_bars}}` |
| `pr` | `{{pr_ref}}`, `{{title}}`, `{{author}}`, `{{branch}}`, `{{files_changed}}`, `{{additions}}`, `{{deletions}}`, `{{#focus_items}}`, `{{#test_items}}`, `{{#rollout_steps}}` |

---

## 한국어 폰트 정책

한국어 폰트 CDN은 선택 사항입니다. 외부 폰트를 쓰면 연결 없이 서체가 달라질 수 있습니다.

시스템 서체는 OS마다 다를 수 있습니다. CDN을 선택했다면 연결 실패 시에도 읽을 수 있는 폴백을 지정하고, 오프라인 품질은 실제 파일을 열어 확인합니다.

### 모드별 폰트 매핑

| 모드 | sans (본문) | serif (제목) | mono (코드) |
|------|-------------|--------------|-------------|
| `status` / `financial` / `pr` | Pretendard | Pretendard 700 | JetBrains Mono |
| `incident` | Pretendard | Pretendard 700 | JetBrains Mono |
| `plan` | Pretendard | Noto Serif KR | JetBrains Mono |
| `explainer` | Noto Sans KR | Noto Serif KR | JetBrains Mono |

상세 CDN URL 및 preconnect 패턴: [`references/fonts.md`](references/fonts.md)

---

## 디자인 토큰 (CSS 변수 계약)

템플릿은 `:root`의 CSS 변수를 참고합니다. 실제로 사용한 변수와 대비는 산출 파일에서 확인합니다.

```css
:root {
  /* 팔레트 */
  --ivory: #FAF9F5;   /* 배경 warm off-white */
  --paper: #FFFFFF;   /* 카드·패널 배경 */
  --slate: #141413;   /* 본문 텍스트 warm black */
  --clay:  #D97757;   /* 강조·링크 terracotta */
  --clay-d:#B85C3E;   /* clay hover 상태 */
  --oat:   #E3DACC;   /* 보조 배경·구분선 light tan */
  --olive: #788C5D;   /* 보조 강조 sage green */

  /* 폰트 */
  --sans:  "Pretendard", system-ui, -apple-system, sans-serif;
  --serif: "Pretendard", ui-serif, Georgia, serif;
  --mono:  "JetBrains Mono", ui-monospace, "SF Mono", monospace;

  /* 레이아웃 */
  --max-width:    860px;
  --radius-panel: 12px;
  --radius-row:   8px;
  --border:       1.5px solid var(--g300);
}
```

그레이 스케일: `--g100: #F0EEE6`, `--g300: #D1CFC5`, `--g500: #87867F`, `--g700: #3D3D3A`

상세 명도 대비 검증표 및 인쇄 토큰: [`references/design-tokens.md`](references/design-tokens.md)

---

## 디자인 시스템 적용 (`design_system` 파라미터)

`design_system` 입력을 지정하면 현재 설치된 `moai-designer:design-system-library`에서 사용할 수 있는 토큰을 확인합니다. Tailwind Play CDN을 쓰는 예시 템플릿은 인터넷 연결이 필요합니다.

**작성 방식**:

| `design_system` | 방식 | 외부 의존 | 산출물 특성 |
|-----------------|------|-----------|-------------|
| **미지정** | 기본 템플릿 | 사용한 폰트 링크에 따라 다름 | 브라우저에서 오프라인 결과 확인 |
| **지정한 브랜드** | 실제 사용 가능한 템플릿 확인 | CDN 사용 여부 확인 | 브라우저에서 온라인·오프라인 결과 구분 |

브랜드 시스템은 사용자 지침에 지정된 경우에 적용한다. 모드 이름만으로 Claude·ClickHouse 등 다른 회사의 브랜드를 선택하지 않는다.

### 적용 절차

1. 실제 설치된 디자인 시스템에서 지정한 브랜드의 토큰을 읽는다.
2. 사용할 색과 서체를 HTML의 CSS 변수에 적용한다.
3. 필요한 경우에만 외부 CDN을 추가하고, 최종 HTML에서 해당 URL을 확인한다.
4. 온라인 및 오프라인에서 실제 파일을 열어 결과를 확인한다.

> **주의**: 브랜드 예시에 Tailwind Play CDN이 포함되었다면 오프라인에서 스타일이 달라질 수 있습니다. 오프라인·인쇄·이메일 첨부 용도에는 필요한 CSS를 문서 안에 포함하고 실제 파일을 확인하세요.

---

## 체인 통합 권장

```
[텍스트 스킬] → moai-coworker:ai-slop-reviewer → moai-writer:korean-humanize → moai-officer:doc-html-report (서식 선택)
```

최소 체인 (빠른 렌더링):
```
[텍스트 스킬] → moai-officer:doc-html-report (서식 선택)
```

브랜드 디자인 시스템 적용 체인:
```
[텍스트 스킬] → ai-slop-reviewer → doc-html-report (design_system: clickhouse)
```

> 디자인 시스템을 지정했으면 해당 플러그인과 토큰이 현재 호스트에 있는지 확인합니다. 없다면 사용자 지정 색·서체를 일반 CSS에 적용합니다.

---

## 사용 예시

**예시 1: 주간 현황 보고서**
```
경영 요약 결과를 받아서 한울 엔지니어링 11주차 현황 보고서 HTML로 만들어줘.
```

**예시 2: 재무제표 HTML 보고서**
```
재무제표 결과를 HTML 보고서로 변환해줘.
```

**예시 3: 인시던트 리포트**
```
결제 게이트웨이 502 장애 내용을 정리해서 인시던트 리포트 HTML로 만들어줘. 심각도는 SEV-2.
```

**예시 4: PR 설명 문서**
```
PR #312 실시간 알림 채널 통합 내용을 HTML 리뷰 문서로 만들어줘.
```

---

## 시각 품질 게이트 (필수)

**[HARD] 렌더가 끝나면 산출 HTML을 브라우저에서 열어 아래 4축을 실측하고 PASS/FAIL을 보고한다.** 과거 샘플은 이 기준의 통과 증거가 아니다. 실제 열람·실측이 불가능하면 `미검증`으로 기록하고 PASS라고 쓰지 않는다.

인쇄용 또는 PDF 변환용 요청이면 인쇄 미리보기나 실제 PDF를 열어 페이지 잘림·표 누락·차트 가독성을 별도로 확인한다. 이 결과가 없으면 화면 검사가 통과해도 인쇄/PDF 품질은 `미검증`으로 남긴다.

**공통 4축** — 렌더 후 DOM 실측으로 판정한다. 눈으로 훑는 것으로 갈음하지 않는다.

| 축 | 측정 | 기준 | 등급 |
|---|---|---|---|
| **본문 크기** | 본문 노드 computed `font-size` | ≥16px (화면 읽기 기준). 부연·캡션 ≥14px | hard |
| **명도대비** | 상대 휘도 기반 WCAG 대비비 | 본문 ≥4.5:1 · 큰 텍스트 ≥3:1 | hard |
| **텍스트 오버플로** | `scrollHeight > clientHeight` | 0건 | hard |
| **산출물 밖 요소** | 본문 컨테이너 바깥의 렌더되는 텍스트 노드 | 0개 — 장수·해상도·사용 폰트 같은 **제작 메타는 화면에 찍지 않는다**(HTML 주석으로) | hard |

**아이콘을 쓸 때** — 아이콘은 레이아웃상 빈 자리로 보여서, 근거를 요구하지 않으면 손에 잡히는 몇 개를 돌려쓰게 된다.

- 문구의 **동사**에서 고른다 (적는다 → 메모, 멈춘다 → 정지). 명사가 아니라 그 자리가 시키는 행동에 맞춘다.
- 한 문서에서 같은 아이콘을 **3회 넘게 쓰지 않는다**.
- 마땅한 것이 없으면 **비운다**. 빈 자리가 틀린 아이콘보다 낫다.
- **[HARD] 아이콘을 썼으면 PASS/FAIL 증거표에 넣는다.** 슬롯 문구·아이콘·고른 이유를 나란히 적어 보고한다. "아이콘이 필요해서" 같은 동어반복은 근거가 아니며, 근거를 한 줄로 못 쓰면 비운다.

> 이 4축은 [`doc-html-slide/references/deck-quality-rubric.md`](../../../moai-officer/skills/doc-html-slide/references/deck-quality-rubric.md)의 hard-fail에서 **문서형(연속 스크롤)에 해당하는 것만** 옮겨온 것이다. 프로젝터 투사 기준인 pt 하한(24pt)은 문서형에 적용하지 않고 화면 읽기 기준(16px)으로 대체한다.

---

## 하지 않는 것

- 마크다운 기본 출력을 대체하지 않습니다 — HTML은 추가 렌더링 분기입니다.
- 기본 템플릿은 React / Vue / Chart.js / D3를 요구하지 않습니다. 브랜드 예시에서 Tailwind CDN을 썼다면 외부 의존성을 명시합니다.
- 빌드 단계(webpack, vite, esbuild)를 도입하지 않습니다.
- 슬라이드는 `moai-officer:doc-pptx`, 독립 차트는 `moai-analyst:data-visualizer`가 맡습니다.
- 여러 파일로 나누지 않습니다 — 모든 산출물은 단일 `.html` 파일입니다.

---

## 참고 문서

### 설계 문서
- [`references/design-tokens.md`](references/design-tokens.md) — CSS 변수 계약·팔레트·접근성
- [`references/fonts.md`](references/fonts.md) — 폰트 매핑·CDN URL·preconnect 패턴

### 템플릿
- [`references/templates/status.html.tmpl`](references/templates/status.html.tmpl) — status 모드
- [`references/templates/incident.html.tmpl`](references/templates/incident.html.tmpl) — incident 모드
- [`references/templates/plan.html.tmpl`](references/templates/plan.html.tmpl) — plan 모드
- [`references/templates/explainer.html.tmpl`](references/templates/explainer.html.tmpl) — explainer 모드
- [`references/templates/financial.html.tmpl`](references/templates/financial.html.tmpl) — financial 모드
- [`references/templates/pr.html.tmpl`](references/templates/pr.html.tmpl) — pr 모드

### 샘플 출력
- [`references/samples/status-sample.html`](references/samples/status-sample.html) — status 모드 렌더링 예시
- [`references/samples/incident-sample.html`](references/samples/incident-sample.html) — incident 모드 렌더링 예시
- [`references/samples/plan-sample.html`](references/samples/plan-sample.html) — plan 모드 렌더링 예시
- [`references/samples/explainer-sample.html`](references/samples/explainer-sample.html) — explainer 모드 렌더링 예시
- [`references/samples/financial-sample.html`](references/samples/financial-sample.html) — financial 모드 렌더링 예시
- [`references/samples/pr-sample.html`](references/samples/pr-sample.html) — pr 모드 렌더링 예시

설계 참고: [Thariq Shihipar, "The Unreasonable Effectiveness of HTML"](https://thariqs.github.io/html-effectiveness/) — 외부 라이브러리 없이 HTML 한 파일로 끝내는 접근의 출처.

---

## P1 컨슈머 통합

다음 파일은 과거에 저장한 입력·출력 예시입니다. 현재 호스트의 통합 테스트 결과로 간주하지 않고, 새 산출물은 별도로 렌더링해 확인합니다.

| 컨슈머 스킬 | 적합 모드 | 입력 파일 | 렌더링 출력 | 호환성 |
|-------------|-----------|-----------|-------------|--------|
| `moai-coworker:collab-exec-summary` | `status` | [`references/integration-tests/executive-summary-input.md`](references/integration-tests/executive-summary-input.md) | [`references/integration-tests/executive-summary-rendered.html`](references/integration-tests/executive-summary-rendered.html) | 과거 예시 |
| `moai-accountant:finance-financial-statements` | `financial` | [`references/integration-tests/financial-statements-input.md`](references/integration-tests/financial-statements-input.md) | [`references/integration-tests/financial-statements-rendered.html`](references/integration-tests/financial-statements-rendered.html) | 과거 예시 |
| `moai-consultant:consult-sbiz365` | `plan` | [`references/integration-tests/sbiz365-analyst-input.md`](references/integration-tests/sbiz365-analyst-input.md) | [`references/integration-tests/sbiz365-analyst-rendered.html`](references/integration-tests/sbiz365-analyst-rendered.html) | 과거 예시 |
| `moai-officer:productivity-briefing` | `status` (daily variant) | [`references/integration-tests/daily-briefing-input.md`](references/integration-tests/daily-briefing-input.md) | [`references/integration-tests/daily-briefing-rendered.html`](references/integration-tests/daily-briefing-rendered.html) | 과거 예시 |

상세 호환성 분석: [`references/integration-tests/COMPATIBILITY.md`](references/integration-tests/COMPATIBILITY.md)
