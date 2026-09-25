---
name: doc-html-slide
description: |
  발표용 슬라이드 덱을 브라우저에서 바로 열리는 단일 HTML로 만듭니다. 인포그래픽은 정확한 숫자·라벨을 인라인 SVG로 렌더링합니다. 실사·일러스트는 앱의 기본 이미지 생성 도구 또는 사용자가 지정한 Higgsfield 연결로 만듭니다. 필요하면 doc-pptx 체이닝으로 편집 가능한 .pptx도 산출합니다.
  다음과 같은 요청 시 사용하세요:
  - "발표 슬라이드 HTML로 만들어줘"
  - "키노트 덱 단일 HTML 파일로 렌더해줘"
  - "사업계획서 슬라이드 10장, 브라우저에서 바로 열리게"
  - "데이터 시각화 인포그래픽 슬라이드 HTML로"
  - "슬라이드 만들고 PPTX로도 저장해줘"
  - "투자 피칭 덱 인터랙티브 HTML로"
  - "발표 자료를 HTML 슬라이드 + 편집 가능 PPTX 둘 다"
  현재 설치된 design-system-library 브랜드 토큰 중 테마를 고릅니다. getdesign.md 링크는 공식 브랜드 규격이 아닌 외부 참고 자료입니다.
  PDF 배포본이 필요하면 브라우저 `?print-pdf` 인쇄 모드를 쓰거나, 생성한 HTML을 moai-officer:doc-pdf로 넘겨 변환하세요 (weasyprint를 직접 설치·호출하지 말 것).
  [책임 경계] vs moai-officer:doc-pptx: 이 스킬=브라우저에서 바로 열리는 단일 .html 슬라이드 덱(편집 가능 .pptx는 doc-pptx 체이닝으로 산출). vs moai-media:media-notebooklm-slide-prompt: 저 스킬=NotebookLM 입력용 프롬프트(파일 생성 없음). vs moai-officer:doc-html-report: 저 스킬=연속 스크롤 문서/보고서(슬라이드 덱이 아님).
version: "1.2.5"
---

# doc-html-slide — 단일 파일 HTML 슬라이드 덱 생성기

## 목적과 범위

`moai-officer:doc-html-slide`는 발표용 슬라이드 덱을 **단일 HTML 파일**로 만듭니다. 이웃 스킬 `doc-html-report`의 "인라인 SVG·design-system-library 토큰 계약" 아키텍처를 계승하되, 연속 스크롤 문서가 아닌 **16:9 슬라이드 시퀀스 + 자체 vanilla JS 덱 런타임**(키보드 내비게이션·풀스크린·`?print-pdf` 인쇄 모드·speaker notes 토글)을 제공합니다.

**핵심 원칙**:
- 단일 `.html` 파일 — 외부 빌드 단계·런타임 SPA 의존 없이 `file://`로 즉시 오픈
- 인포그래픽은 인라인 SVG로 직접 작성 — 숫자·라벨은 원자료와 대조하고 확대 렌더를 확인
- 실사·일러스트 이미지는 앱 기본 이미지 도구 또는 사용자가 지정한 Higgsfield 연결로 생성 (`references/image-backend-policy.md`)
- 설치된 design-system-library 브랜드 토큰 적용 — getdesign.md 참고 링크 제공
- 편집 가능 PPTX 산출은 이 플러그인의 `doc-pptx` 지침과 현재 사용 가능한 생성 도구로 수행

**원고 SSOT**: 모든 덱은 구조화 원고 `deck.json`(title/bullets/chart-data/image-path/layout-key/notes)을 단일 진실 원천으로 둡니다. PPTX도 요청받았다면 같은 원고를 참고해 각 요소를 편집 가능한 객체로 만들고 실제 파일에서 확인합니다. 원고를 공유한다는 사실만으로 PPTX 편집 가능성이 보장되지는 않습니다.

---

## 입력

| 인자 | 필수 | 기본값 | 설명 |
|------|------|--------|------|
| `topic` / 자연어 주제 | ✓ | — | 덱 주제·대상 청중·발표 목적 |
| `design_system` | — | 미지정 | 사용자 브랜드 또는 현재 설치된 [`design-system-library`](../../../moai-designer/skills/design-system-library/SKILL.md)의 시스템. 실제 토큰과 외부 CDN 사용 여부를 확인. 참고 링크는 [`references/design-system-links.md`](references/design-system-links.md) |
| `slide_count` / 발표 시간 | — | 주제에서 추천 | 3분=5-7장 · 10분=10-15장 · 30분=20-30장 |
| `aspect_ratio` | — | `16:9` | `16:9`(프로젝터 표준) \| `1:1`(소셜/카드뉴스) |
| `locale` | — | `ko` | `ko` \| `en` — 헤드라인·카피 언어 |
| `image_backend` | — | `native` | `native`(앱 기본 이미지 생성) \| `higgsfield`(사용자가 지정한 Higgsfield 연결) \| `svg-only`(이미지 없이 SVG 장식만). 기존 `codex` 값은 `native`로 해석 |
| `export_pptx` | — | `false` | `true` 시 doc-pptx 체이닝으로 편집 가능 .pptx 병행 산출 |
| `output_path` | — | `<cwd>/reports/<slug>-slides-<YYYYMMDD>.html` | 출력 경로 |

---

## 출력

- **주 산출물**: 단일 `.html` 파일 (`<cwd>/reports/<slug>-slides-<YYYYMMDD>.html`)
  - 브라우저에서 열 수 있는 단일 파일. 외부 리소스를 썼다면 자체 완결형·오프라인 사용 가능이라고 표시하지 않음
  - 외부 의존: 최종 HTML의 폰트·이미지·CSS·JS URL을 확인하고 오프라인 파일을 직접 검사
- **병행 산출물** (`export_pptx: true` 시): 편집 가능 `.pptx` (doc-pptx 체이닝)
- **원고**: `deck.json` (HTML·PPTX 양쪽 공통 소스, 산출 디렉토리에 보존)

---

## 핵심 워크플로우 (9단계)

### 1. 컨텍스트 수집
현재 런타임에서 가능한 질문 경로로 사용할 브랜드·발표 시간(슬라이드 수)·이미지 필요 여부·PPTX 산출 여부를 확인합니다. design_system 선택 시 [`references/design-system-links.md`](references/design-system-links.md)의 getdesign.md 링크로 각 토큰 상세 페이지를 안내해 사용자가 미리보기로 확인할 수 있게 합니다. **강연/발표 맥락** — 비개발자 청중 다수·주간·프로젝터 환경에서는 라이트 테마(claude·notion·apple·stripe·mintlify)가 안전합니다. 다크는 발표 공간을 어둡게 조절할 수 있을 때만 권장.

### 2. 원고 SSOT 구축 (핵심)
`deck.json` 원고를 먼저 작성합니다 — title/bullets/chart-data/image-path/layout-key/notes. 이 원고가 HTML 렌더와 doc-pptx PPTX 렌더 양쪽의 공통 소스입니다. 스키마: [`references/deck-manuscript-schema.md`](references/deck-manuscript-schema.md). layout-key는 doc-pptx 9 아키타입(Title/Agenda/Problem/Solution/Features/Stats/Team/CTA/Closing)에 정합시킵니다.

### 3. 인포그래픽 = 인라인 SVG 직접 생성
차트·다이어그램·KPI 카드·타임라인은 LLM이 인라인 SVG로 직접 작성합니다. 한국어 숫자·라벨 100% 정확을 위해 비트맵 이미지로 우회하지 않습니다. 패턴 라이브러리: [`references/inline-svg-infographics.md`](references/inline-svg-infographics.md).

### 4. 비트맵 이미지 생성 (필요 시) — 이미지 백엔드 정책
포토 히어로·일러스트 컨셉 등 SVG로 표현 불가능한 비트맵이 필요한 슬라이드만 이미지 백엔드로 생성합니다. 정책: [`references/image-backend-policy.md`](references/image-backend-policy.md).

| 백엔드 | 모델 | 인증 | 권장 용도 |
|--------|------|------|-----------|
| **`native`** (기본) | 앱이 제공하는 이미지 모델 | 앱 로그인 | 일반 이미지 생성 |
| **`higgsfield`** | 연결에서 조회한 Higgsfield 모델 | Higgsfield 공식 플러그인 또는 MCP의 계정 인증 | 사용자가 Higgsfield를 지정한 경우 |
| `svg-only` | (이미지 없음) | — | 오프라인·비용 민감·빠른 폴백 |

> 생성 전에 현재 앱에서 해당 도구가 실제로 노출됐는지 확인합니다 — [`references/image-backend-policy.md`](references/image-backend-policy.md).

한국어 텍스트가 이미지에 들어가면 따옴표·등장 횟수·추가 텍스트 금지를 프롬프트에 명시합니다. `moai-media:media-gpt-image-prompt`가 설치돼 있으면 이를 참고할 수 있습니다. 정확해야 하는 문구는 HTML/SVG 텍스트로 올립니다.

### 5. design-system-library 토큰 적용
design_system을 지정했다면 현재 설치된 `systems/<name>.md`의 토큰을 확인해 CSS에 적용합니다. Tailwind Play CDN을 쓰면 연결이 필요하므로 사용 여부를 산출물에 명시합니다. 미지정이어도 폰트·이미지 URL이 남아 있을 수 있어 오프라인 파일을 별도로 확인합니다.

### 6. 단일 파일 HTML 덱 조립
16:9 슬라이드 컨테이너 + 자체 vanilla JS 덱 런타임(키보드 내비·풀스크린·`?print-pdf` 인쇄 모드·speaker notes 토글·progress bar)을 단일 `.html`로 산출. 런타임 구현: [`references/html-runtime.md`](references/html-runtime.md).

- **[HARD] 슬라이드 바깥에 제작 메타를 렌더하지 않는다.** 장수·해상도·도식 개수·사용 폰트 같은 **제작 메타는 산출물이 아니라 작업 메모**다. (카운터·진행바·발표자 노트 같은 덱 조작 UI는 여기 해당하지 않는다 — 루브릭 §제작 메타 판정.) 필요하면 HTML 주석(`<!-- -->`)이나 `deck.json`에 남기고, 화면에 찍히는 자리에는 두지 않는다 — 수강생·고객에게 그대로 보인다. 루브릭 #34가 이를 hard-fail로 검사한다.
- 아이콘은 `deck.json`의 `icon` + `icon_reason` 쌍을 그대로 따른다(스키마 §아이콘 슬롯 계약). 렌더 단계에서 임의로 대체하지 않는다.

### 7. 슬라이드 카피 검수
모든 슬라이드 카피·speaker notes를 원자료와 대조해 숫자·인용·고유명사·주장의 강도가 유지되는지 직접 확인합니다. `moai-coworker:ai-slop-reviewer`와 `moai-writer:korean-humanize`가 설치돼 있으면 문장 검수에 추가로 사용할 수 있습니다. 두 스킬이 없어도 원문 대조를 생략하지 않습니다.

**슬라이드 카피 QA 체크리스트 — 구조적 슬롭 S1 패턴 3종**: 헤드라인·카피를 직접 읽으며 아래 표현을 검토합니다. 문맥상 필요한 표현까지 기계적으로 삭제하지 않습니다.

| # | 패턴 | 탐지 신호 | [나쁜 예] | 수정 |
|---|------|----------|-----------|------|
| 1 | **대시 대비 헤드라인** | 대시(`—`)로 문장 분할 "X — Y" (대시 대비 헤드라인) | [나쁜 예] "복붙에서 위임으로 — 목표만 주면" | 대시 제거, 한 문장 통합 또는 두 문장 분리 |
| 2 | **조사·체언 종결 조각문** | 조사·체언 종결 조각문 (조사/체언으로 끝남) | [나쁜 예] "성공의 열쇠 — 자동화" (조사·체언 종결) | 서술어 포함 완전문으로 재작성 |
| 3 | **"A에서 B로" 전환 공식** | "X에서 Y로" 전환 공식 도입 | [나쁜 예] "엑셀에서 노션으로, 바뀐 것" (전환 공식) | 전환 공식 대신 구체적 사례로 시작 |

### 8. PPTX 산출 (선택, export_pptx: true 시)
`deck.json` 원고를 이 플러그인의 `doc-pptx` 작업에 전달합니다. 현재 호스트에서 실제 PPTX 생성 도구가 없으면 요청한 PPTX는 미완료로 표시합니다. 생성했다면 텍스트·차트·도형이 편집 가능한 객체인지 파일을 열어 확인합니다. 체이닝 규약: [`references/pptx-chaining.md`](references/pptx-chaining.md).

### 9. 정량 QA 채점 (의무)

**[HARD] 산출된 HTML을 브라우저에서 렌더해 [`references/deck-quality-rubric.md`](references/deck-quality-rubric.md)의 기준을 확인한다.** 이 단계는 §7의 원자료 대조와 함께 수행하며, 눈으로 훑어보는 것으로 갈음하지 않는다 — 루브릭은 DOM 실측(`getBoundingClientRect`·computed `font-size`·명도대비 계산)을 요구하고, 그 수치가 곧 증거다.

> 정량 검수는 실제 렌더링과 측정값이 있어야 수행했다고 보고할 수 있습니다. 브라우저 도구가 없어 측정하지 못한 항목은 `미실행`으로 남깁니다.

**hard 기준 9개(실패군 8종) — 한 건이라도 걸리면 반려하고 고쳐서 다시 렌더한다.** (#32와 #33은 둘 다 아이콘 문제라 하나의 실패군으로 보고하되 각각 확인한다.) 이 플러그인에는 자동 채점기나 `qa-config.json`이 포함되어 있지 않다. 현재 사용 가능한 브라우저 도구로 측정하고, 측정하지 못한 항목은 PASS로 표시하지 않는다.

| # | 기준 | DOM 측정 | 기본 임계값 |
|---|------|---------|------------|
| 9 | **본문 폰트 하한** | 본문 노드 computed `font-size`. **슬라이드 폭 → pt 환산 후 판정** (1280px 슬라이드 = 960pt, 즉 `1px = 0.75pt`) | ≥24pt (온라인 전용 덱 18pt로 하향 설정 가능) |
| 16 | **명도대비** | 상대 휘도 기반 WCAG 대비비 | 본문 ≥4.5:1 · 큰 텍스트 ≥3:1 |
| 17 | **3D 차트 효과** | SVG/CSS 원근·`rotateX/Y`·입체 그림자 | 검출 시 반려 |
| 20 | **그리드 정렬 편차** | 동일 역할 요소(제목/푸터) 좌표 표준편차 | 슬라이드 너비 1% 이내 |
| 24 | **수치 슬라이드 출처라인** | 숫자·차트·표 있는 슬라이드에 `출처:`/`자료:`/`Source:` 노드 | 부재 시 반려 |
| 28 | **텍스트 오버플로** | `scrollHeight > clientHeight` 또는 축소 후 하한 미만 | 발생 시 반려 |
| 32 | **아이콘 어휘 다양성** | 정규화된 icon ID별 **최대 사용 횟수**(`max_count_per_normalized_icon`) | 같은 아이콘 ≤3회 (역할 반복 예외는 루브릭 §아이콘 근거 판정) |
| 33 | **아이콘 의미 근거** | `icon_reason`이 그 문구의 동사·행동과 실제로 대응하는가 — 필드 존재만으로 통과시키지 않는다 | 대응 불명이면 반려 |
| 34 | **제작 메타 노출** | 슬라이드 바깥에 렌더되는 **제작 메타·디버그** 텍스트 | 0개 (런타임 UI는 허용 — §아래) |

- **[HARD] pt 환산을 생략하지 않는다.** #9는 px 값이 아니라 **투사 시 실제 크기**를 판정한다. 1280px 덱의 본문 18px는 13.5pt이며, 프로젝터 기준 하한(24pt)의 절반을 조금 넘는 수준이다. px로만 보면 "충분히 커 보이는" 값이 여기서 걸린다.
- **[HARD] 강의장·회의실 투사 덱은 온라인 완화(18pt)를 적용하지 않는다.** 완화는 화면으로만 볼 아카이브 덱에 한한다. 어느 쪽인지 불분명하면 §1에서 사용자에게 확인한다.
- soft 25개 기준도 측정 가능한 항목의 수치와 판정을 보고한다. 가중치와 합격선을 실제로 정하고 계산한 경우에만 종합 점수를 보고한다.

**렌더 검사 실무 주의**: 슬라이드가 많은 덱은 문서 전체 높이가 수만 px에 달해 브라우저 스크린샷이 빈 이미지를 반환하는 일이 있다. 측정은 스크린샷이 아니라 **DOM API(`getBoundingClientRect`·`getComputedStyle`·`elementFromPoint`)로 하고**, 시각 확인이 필요하면 대상 슬라이드만 남기고 나머지를 `display:none`으로 접은 뒤 촬영한다.

**그 밖의 기능 검수**: 단일 HTML 열기·`?print-pdf` 인쇄 미리보기·speaker notes 표시·이미지 broken link·한국어 폰트 렌더·이미지 백엔드 정책 준수(허용 백엔드만 사용)를 함께 확인한 뒤 PASS/FAIL 보고. PPTX 체이닝 시 doc-pptx QA 결과 통합 보고.

---

## 승인 요청 계약 (런타임 중립)

[HARD] 이 스킬의 게이트는 **특정 도구 이름에 묶이지 않는다.** `AskUserQuestion`은 Claude 런타임의 수단일 뿐이고, Codex를 비롯한 다른 런타임에는 그 도구가 없다. 도구 이름으로 계약을 쓰면 그 도구가 없는 런타임에서 게이트가 **영구 blocker**가 되어, 승인이 필요한 모든 작업이 그냥 멈춘다. 그건 안전이 아니라 고장이다.

승인은 아래 순서로 구한다. 위에서부터 **실제로 가능한 첫 번째**를 쓴다.

**승인의 정의는 수단이 아니라 결과다: 승인서를 사용자에게 그대로 보여주고, 그에 대한 명시적 응답을 받는 것.** 아래는 그 결과를 만드는 경로들이며, 위에서부터 가능한 첫 번째를 쓴다.

| 순위 | 경로 | 조건 |
|---|---|---|
| 1 | 런타임의 구조화 질문 도구 (`AskUserQuestion` 등) | 그 도구가 현재 세션에 노출돼 있을 때 |
| 2 | **일반 대화로 승인서를 제시하고 다음 턴에서 응답을 받는다** | 사용자와 직접 대화 중일 때. 도구가 없어도 이 경로는 언제나 열려 있다 |
| 3 | 구조화 blocker 반환 → 상위 오케스트레이터가 물어봄 | 서브에이전트로 실행 중일 때 |

**[HARD] 런타임의 도구 실행 권한 프롬프트는 승인이 아니다.** 그 프롬프트는 "이 도구를 호출해도 되는가"를 물을 뿐, 게이트가 보여주기로 한 인자·견적·동의 문항을 표시하지 않는다. 승인서 전체와 선택지를 실제로 표시하는 경우에만 2번 경로로 인정한다.

**[HARD] 2번 경로가 있으므로 "물을 수단이 없다"는 상황은 사실상 없다.** 대화가 가능한 곳에서는 언제나 승인서를 글로 제시할 수 있다. fail-closed는 **대화도 blocker 반환도 불가능한 완전 무인 실행**에만 해당한다 — 그 경우에만 실행하지 않고 멈춘다.

**[HARD] 3번을 쓸 때 blocker는 그 자체로 승인 요청서여야 한다.** 상위가 무엇을 물어야 할지 모르면 되물을 수 없고, 그러면 교착된다. 다음을 모두 담는다:

- 승인받을 **행위** 한 줄 (무엇이 되돌릴 수 없는지 / 얼마가 나가는지)
- 게이트가 요구하는 **인자 전부** (요약하지 않은 값)
- **선택지 목록** — 상위가 그대로 사용자에게 제시할 수 있는 형태
- **재개 방법** — 어떤 답을 받으면 무엇을 이어서 실행하는지

**[HARD] 세 경로가 모두 불가능한 무인 실행에서는 실행하지 않는다(fail-closed).** 물을 수단이 없다는 것은 승인을 받았다는 뜻이 아니다. 이때는 "승인 수단이 없어 진행하지 못했다"고 기록하고 멈춘다 — 조용히 진행하지 않는다. 반대로 **대화가 가능한데 도구가 없다는 이유로 멈추는 것도 잘못**이다. 2번 경로를 쓴다.

> 이 계약은 `CLAUDE.local.md` §범용성 원칙(OS 2종 × 런타임 2종에서 동일 동작)의 게이트 쪽 적용이다. 한 런타임에서만 도는 게이트는 미완성으로 본다.

---

## 디자인 시스템 적용 (`design_system` 파라미터)

`design_system` 입력으로 현재 설치된 [`moai-designer:design-system-library`](../../../moai-designer/skills/design-system-library/SKILL.md)의 브랜드 토큰을 확인해 적용합니다. 이 스킬에는 자동 테마 변환 실행기가 포함돼 있지 않습니다.

| `design_system` | 엔진 | 외부 의존 | 산출물 특성 |
|-----------------|------|-----------|-------------|
| **미지정** | 기본 서식 | 최종 HTML의 폰트·이미지 URL 확인 | 오프라인·인쇄 결과 직접 확인 |
| **지정한 브랜드** | 실제 토큰을 CSS에 적용 | CDN·이미지 사용 여부 확인 | 네트워크 필요 여부를 산출물에 기록 |

### 테마별 적합 슬라이드 (자동 추천)

| 발표 성격 | 추천 design_system |
|-----------|-------------------|
| 사업계획서·보고서·편집성 | `claude` (warm editorial, 크림+코랄) |
| 기술·데이터·엔지니어링·다크 프로젝터 | `clickhouse` (dark tech) |
| 제품 소개·SaaS·스타트업 | `notion`·`apple`·`stripe`·`mintlify` (light, 깔끔) |
| 마케팅·키노트·임팩트 | `spotify`·`nike`·`airbnb` (bold) |
| **비개발자 청중·주간·프로젝터 (라이트 안전)** | `claude`(예시) · `notion` · `apple` · `stripe` · `mintlify` |
| 다크 (방을 어둡게 조절 가능할 때) | `clickhouse` · `vercel` · `linear.app` · `supabase` · `binance` |

> 발표 공간·화면 밝기와 사용자 브랜드를 확인해 라이트·다크를 선택합니다. 외부 갤러리의 구성이나 현재 토큰 수를 고정된 값으로 전제하지 않습니다.

### getdesign.md 미리보기 링크
각 design_system 값에 대해 [`references/design-system-links.md`](references/design-system-links.md)의 `https://getdesign.md/<slug>` 목록 페이지를 참고할 수 있습니다. 사이트는 브랜드의 공식 규격이 아닌 독립 분석이며, 상세 분석은 목록에서 한 번 더 선택합니다. 시스템 링크 매핑표(저장소 시스템명 → getdesign.md slug)를 해당 파일에서 관리합니다.

---

## 체인 통합

```
[원고와 근거 확인] → 원문 대조·문장 검수 → moai-officer:doc-html-slide
                                                                            ↓ (export_pptx: true)
                                                                moai-officer:doc-pptx
```

이미지 필요 시 분기:
```
doc-html-slide → 현재 앱의 이미지 생성 도구 (기본)
           → 공식 Higgsfield 연결 (명시 요청 시)
           → 설치된 moai-media 스킬은 모델·프롬프트 세부 지침에 활용
```

design_system 적용은 design-system-library에서 자동 로드 — 별도 선행 스킬 호출 불필요.

---

## 사용 예시

**예시 1: 사업계획서 슬라이드 (기본 claude 테마)**
```
AI 슬라이드 스킬 스타트업 사업계획서 10장 슬라이드로 만들어줘. claude 테마로.
```

**예시 2: 데이터 인포그래픽 슬라이드 + PPTX**
```
3분기 매출 분석 슬라이드 HTML로 만들고, 편집 가능한 PPTX로도 저장해줘.
```

**예시 3: 다크 테마 기술 발표**
```
신규 API 아키텍처 기술 발표 15장, clickhouse 다크 테마로 슬라이드 HTML 만들어줘.
```

**예시 4: 앱 기본 이미지 생성**
```
제품 출시 슬라이드 만들어줘. 히어로 이미지는 기본 이미지 도구로 생성하고, notion 테마 적용.
```

**예시 5: 테마 미리보기 후 선택**
```
슬라이드 만들 건데, 디자인 토큰 후보들 getdesign.md 링크로 보여주고 내가 고를게.
```

---

## 하지 않는 것

- 연속 스크롤 문서는 `moai-officer:doc-html-report`가 맡습니다 — 본 스킬은 슬라이드 시퀀스(16:9 페이지) 전용입니다.
- 편집 가능 .pptx 생성 지침은 이 플러그인의 `doc-pptx`가 맡습니다.
- NotebookLM 입력용 프롬프트는 `moai-media:media-notebooklm-slide-prompt`가 맡습니다.
- React/Vue/webpack/vite 같은 빌드 단계·런타임 SPA 의존을 도입하지 않습니다 — `file://` 즉시 오픈이 원칙입니다.
- [`references/image-backend-policy.md`](references/image-backend-policy.md)의 이미지 생성 경로를 따릅니다.
- 여러 파일로 나누지 않습니다 — HTML 산출물은 단일 `.html` 파일입니다.

---

## 참고 문서

### 설계 문서
- [`references/deck-manuscript-schema.md`](references/deck-manuscript-schema.md) — deck.json SSOT 스키마 + doc-pptx 아키타입 매핑 규약
- [`references/html-runtime.md`](references/html-runtime.md) — 자체 vanilla JS 덱 런타임 (네비게이션·풀스크린·`?print-pdf`·speaker notes, 0의존)
- [`references/inline-svg-infographics.md`](references/inline-svg-infographics.md) — 인라인 SVG 인포그래픽 패턴 (차트·다이어그램·KPI, 한국어 숫자/라벨 정확 렌더)
- [`references/image-backend-policy.md`](references/image-backend-policy.md) — 앱 기본 이미지 생성과 Higgsfield 연결 선택 규칙
- [`references/pptx-chaining.md`](references/pptx-chaining.md) — PPTX 생성 가능 도구와 편집 가능성 확인 절차
- [`references/design-system-links.md`](references/design-system-links.md) — 시스템 → getdesign.md 링크 매핑표
- [`references/deck-quality-rubric.md`](references/deck-quality-rubric.md) — 슬라이드 정량 QA 루브릭 (6카테고리 가중합 + hard-fail, HTML/DOM 재해석, doc-pptx와 공유)
- [`references/editorial-deck-doctrine.md`](references/editorial-deck-doctrine.md) — 에디토리얼 덱의 레이아웃·문구·오버플로 점검 항목

### 샘플
- [`samples/deck-sample.json`](samples/deck-sample.json) — 8장 비즈니스 발표 원고 (deck.json SSOT)
- [`samples/deck-sample.html`](samples/deck-sample.html) — 완성 단일 파일 HTML 덱 (design_system: claude 적용)

### 이웃 스킬 (체이닝)
- `moai-officer:doc-design-library` — 브랜드 토큰 참고
- `moai-officer:doc-pptx` — 편집 가능 .pptx 생성 (체이닝)
- `moai-media:media-codex-image` — 설치돼 있으면 정확한 OpenAI 이미지 모델 선택 지침
- `moai-media:media-higgsfield-image` — 설치돼 있으면 Higgsfield 생성 지침
- `moai-media:media-gpt-image-prompt` — 설치돼 있으면 이미지 프롬프트 지침
- `moai-coworker:ai-slop-reviewer` · `moai-writer:korean-humanize` — 설치돼 있으면 보조 문장 검수

## 자체 검수

슬라이드 생성이 끝나면 산출된 단일 .html을 브라우저에서 열어 슬라이드 수·16:9 비율·네비게이션·`?print-pdf` 인쇄 모드·speaker notes·한국어 폰트 렌더·인포그래픽 SVG 정확도를 **자체 검수**하고, 이미지 백엔드 정책 준수(허용 백엔드만 사용)를 확인한 뒤 PASS/FAIL 결과를 보고합니다. PPTX 체이닝 시 doc-pptx QA(빈 플레이스홀더·overflow·색 대비 4.5:1) 결과를 통합 보고합니다. 문제가 있으면 자동 수정 후 재생성합니다.
