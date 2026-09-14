# 이미지 백엔드 정책 — 허용 백엔드: Higgsfield + codex

doc-html-slide의 비트맵 이미지(실사 히어로·일러스트 컨셉 등 SVG로 표현 불가능한 영역) 생성 백엔드 정책입니다. **인포그래픽(차트·다이어그램·KPI)은 이미지 백엔드를 쓰지 않고 인라인 SVG로 직접 저작**합니다 (`references/inline-svg-infographics.md`).

## 정책 요약 (2026-06-17 기준)

| 백엔드 | 상태 | 모델 | 인증 | 권장 용도 |
|--------|------|------|------|-----------|
| **`higgsfield`** | ✅ 1순위 (기본) | GPT Image 2.5·Nano Banana Pro·Soul·Seedream·Flux 등 여러 모델 | Higgsfield MCP(API 키) | 프로덕션·멱등·CI 무인 |
| **`codex`** | ✅ 공식 추가 (2026-06-17) | GPT Image (버전은 서비스 측 결정, 지정 불가) | codex CLI + ChatGPT OAuth(구독 한도, API 키 불필요) | 로컬·개발자·구독 한도 재사용 |
| `antigravity` | ⚠️ 비권장 | Imagen·Nano Banana (agy -p) | Google OAuth 브라우저 + 구독 quota | 로컬 단발 프로토타입 only |
| `svg-only` | ✅ 폴백 | (이미지 없음) | — | 오프라인·비용 민감·빠른 폴백 |

> 허용 백엔드는 위 4개뿐입니다. 그 외 외부 이미지 백엔드(MCP·API·게이트웨이)는 사용하지 않습니다. moai-coworker MCP 번들은 higgsfield + elevenlabs 2종만 유지(codex는 CLI 별도 설치).

## codex 공식 추가 배경

2026-06-17 GOOS 결정으로 codex가 공식 백엔드로 추가됐습니다. 기술 검증 결과:
- codex exec의 내장 `image_gen` 도구가 GPT Image 모델을 호출해 디스크에 파일로 저장 (모델 버전은 codex·ChatGPT 서비스가 결정)
- ChatGPT OAuth 세션(~/.codex/auth.json) 라우팅으로 **API 키 없이 구독 한도**로 동작 (wjb127/codex-image 실증)
- 한국어 텍스트 렌더링 강점 (품질 medium/high 권장)
- 비대화형 `--json`/`--output-last-message`/`--output-schema`로 자동화 파이프라인 통합 가능

> GPT Image 계열은 Higgsfield MCP 경로(`gpt_image_2_5`, variant `flare`/`sunburst`)로도 사용 가능하며, 모델·품질·투명 배경을 직접 지정할 수 있습니다. 백엔드 선택은 인증·환경·비용 선호에 따라: 프로덕션/CI는 Higgsfield, 로컬 개발/구독 한도 재사용은 codex.

## 백엔드 1: Higgsfield MCP (기본)

`moai-media:media-higgsfield-image` 스킬 또는 Higgsfield MCP 툴 직접 호출. 11개 모델을 API 키 하나로 통합 제공.

```text
# 자연어 호출 (media-higgsfield-image 스킬)
"키노트 히어로 배너, 짙은 남색 그라데이션 + 산하 실루엣, 4K 가로"
```

```text
# 한국어 텍스트 포함 시 — media-gpt-image-prompt로 프롬프트 작성 후 전달
moai-media:media-gpt-image-prompt → 산출 프롬프트 → media-higgsfield-image(gpt_image_2_5 모델)
```

**권장 모델 선택**:
- 텍스트가 들어간 비주얼 → GPT Image 2.5 (`gpt_image_2_5`; 작은 글자·범례가 있으면 `quality=high`)
- 실시간 정확 데이터(날씨·주가) → Nano Banana 2 (Google Search grounding)
- 고품질 표지·전문가 비주얼 → Nano Banana Pro

## 백엔드 2: codex (GPT Image)

`moai-media:media-codex-image` 스킬 또는 codex CLI의 `image_gen` 도구 직접 호출. 최초 1회 `codex login` 필요.

```bash
# 비대화형 — 자연어, API 키 없이 ChatGPT 구독 한도
codex exec "Use \$imagegen to create a 2048x1152 hero banner, warm coral palette, save to ./assets/hero.png"

# 구조화 출력 + 경로 제어 (파이프라인 통합)
codex exec --json --output-last-message ./last.txt --dangerously-bypass-approvals-and-sandbox \
  "Generate a 1536x1024 productivity-visual slide hero, save under output/imagegen/hero.png"
```

**한국어 텍스트 이미지** (따옴표·등장 횟수·추가 텍스트 금지 명시, 결과는 음절 단위로 확인):
```bash
codex exec "Use \$imagegen. Text (verbatim, 한글): '2026년 분기 실적'. Typography: bold sans 한글, 검정, 상단 중앙. Render the text exactly once, verbatim, no extra text. quality high, size 1536x1024, save to ./slide-q1.png"
```

**주의**:
- `--dangerously-bypass-approvals-and-sandbox`는 외부 샌드박스/CI에서만. 로컬은 `-s workspace-write`로 범위 제한 권장
- 이미지 생성 턴은 일반 턴 대비 한도를 3~5배 빨리 소모 (공식 문서)
- 투명 PNG가 필요하면 Higgsfield `gpt_image_2_5` + `background=transparent`를 쓴다 (GPT Image 2.5는 투명 배경 지원, codex 도구의 전달 여부는 미확인). 결과의 알파 채널을 확인한다
- 텍스트/레이아웃 중심 슬라이드는 HTML/CSS 코드 경로 우선 (imagegen "When not to use" 권고)

## 백엔드 3 (비권장): antigravity (agy -p)

agy 1.0.2 실측으로 이미지 생성(1024×1024 PNG, 한국어 히어로 배너)이 동작함은 확인됐으나 **공식 비권장**:

- 인증 = Google OAuth 브라우저 플로우 → 서버/CI 무인 자동화 불가
- quota가 사용자 Google 구독에 묶임 (무료 ~3/일, Pro 5시간 단위)
- 산출물이 stdout 바이너리가 아닌 워크스페이스 파일 → 경로 파싱·GC 오버헤드
- 가끔 multi-day lockout 리포트 → SLA 불안정

```bash
# 로컬 단발 프로토타이핑 only (artifactReviewPolicy: always-proceed 전제)
agy -p "Generate a 1024x1024 hero banner, teal-to-navy gradient. Save to ./hero.png"
```

동일 Imagen/Nano Banana 백엔드를 Higgsfield MCP로 호출하는 것이 정책·멱등성·CI 면에서 우월합니다.

## 하이브리드 오버레이 패턴 (강제)

래스터 이미지(GPT Image/Nano Banana)는 숫자·라벨 환각 리스크가 있으므로, **정확한 수치가 필요한 영역은 래스터에 비주얼만 맡기고 숫자·라벨은 SVG 텍스트 계층으로 별도 배치**합니다:

```html
<div class="slide">
  <img src="hero.png" class="bg"/>           <!-- 래스터: 비주얼만 -->
  <svg class="overlay">                       <!-- SVG: 정확한 숫자·라벨 -->
    <text x="640" y="360">1,234억 원</text>   <!-- 100% 정확 -->
  </svg>
</div>
```

## 허용 백엔드 외 사용 금지

Higgsfield·codex·svg-only 외의 외부 이미지 백엔드는 사용하지 않습니다. moai-coworker MCP 번들은 higgsfield + elevenlabs 2종만 유지합니다.

산출물 검증 (허용 백엔드만 사용했는지 확인):
```bash
# 산출 디렉토리의 이미지 경로가 허용 백엔드(higgsfield/codex/svg)에서 왔는지 확인
ls reports/*-slides-*/assets/ 2>/dev/null
```

## 백엔드 결정 트리

```
이미지가 정확한 숫자/라벨/한국어 텍스트를 담는가?
├─ YES → 인라인 SVG로 직접 저작 (image-backend 사용 안 함)
└─ NO (히어로·실사·장식)
   ├─ CI/프로덕션/멱등 필요 → Higgsfield MCP (기본)
   ├─ 로컬 개발 + ChatGPT 구독 한도 재사용 → codex (GPT Image)
   └─ 오프라인/비용 민감 → svg-only 폴백 (장식 SVG로 대체)
```
