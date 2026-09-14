---
name: media-codex-image
description: |
  codex CLI의 내장 image_gen 도구로 OpenAI GPT Image 이미지를 생성합니다 — ChatGPT OAuth 인증으로 **API 키 불필요**, ChatGPT Plus/Team/Enterprise 구독 한도로 동작합니다. 어떤 GPT Image 버전을 쓸지는 codex·ChatGPT 서비스가 정하며, 이 스킬에서 모델을 지정할 수 없습니다.

  다음과 같은 요청 시 사용하세요:
  - "codex로 이미지 만들어줘", "codex 이미지 생성", "codex image"
  - "GPT 이미지로 만들어줘", "GPT Image로 생성"
  - "API 키 없이 이미지 생성해줘"
  - "로컬에서 이미지 생성", "ChatGPT 구독 한도로 이미지"
  - "/media-codex-image" (직접 호출)

  프롬프트가 복잡하거나 한국어 텍스트가 들어가면 `moai-media:media-gpt-image-prompt`(GPT Image 2.5 공식 가이드 기반 프롬프트 빌더)로 먼저 프롬프트를 만든 뒤 이 스킬로 생성하세요. Higgsfield MCP가 연결돼 있지 않거나 로컬 개발·ChatGPT 구독 한도 재사용이 목적이면 이 스킬을 사용합니다. 모델(Flare·Sunburst)·품질 단계·투명 배경을 확실히 지정해야 하면 `media-higgsfield-image`의 `gpt_image_2_5` 경로를 권장합니다.
version: "1.2.0"
---

# media-codex-image — codex CLI(GPT Image) 이미지 생성기

> moai-coworker | 로컬 이미지 생성 (codex CLI OAuth, API 키 불필요)

## 개요

`codex CLI`의 내장 `image_gen` 도구를 호출해 OpenAI GPT Image 모델로 이미지를 생성합니다. **모델 버전은 서비스 측이 결정**하며 codex 명령에 모델을 지정하는 옵션은 없습니다. 핵심은 **OpenAI REST API를 직접 호출하지 않고 `codex exec` 브릿지를 경유**한다는 점 — ChatGPT OAuth 세션 토큰(`~/.codex/auth.json`)을 이미지 생성 서비스로 라우팅해 **API 키(`sk-*`) 없이 ChatGPT 구독 한도**로 동작합니다.

특히 본 스킬은:

- **API 키 불필요** — `codex login` 1회 OAuth로 ChatGPT 구독(Plus/Team/Enterprise) 한도 사용. `OPENAI_API_KEY` 관리 부담 없음.
- **프롬프트 빌더 연동** — `media-gpt-image-prompt`가 OpenAI 공식 이미지 프롬프팅 가이드 원칙(산출물·용도 먼저, 보이는 디테일, 따옴표 텍스트, 제외 조건)으로 만든 프롬프트를 그대로 codex에 전달.
- **한국어 문구 정확도** — 이미지 안 한글은 따옴표 + 위치·서체 + "exactly once" + 추가 텍스트 금지로 지시하고, 결과를 음절 단위로 확인.
- **media-higgsfield-image 대체 경로** — 모델을 명시해야 하면 Higgsfield MCP의 `gpt_image_2_5`(variant `flare`/`sunburst`)로 생성. 백엔드 선택은 환경·비용·제어 필요성에 따라.

## 트리거 키워드

codex 이미지 codex image GPT Image 생성 API 키 없이 이미지 로컬 이미지 생성 ChatGPT 구독 한도 이미지 codex exec image_gen

## 핵심 인사이트 — OAuth 브릿지 (왜 codex exec인가)

OpenAI의 모든 인증 경로를 테스트한 결과 (참고: [wjb127/codex-image](https://github.com/wjb127/codex-image) MIT):

| 방식 | 동작 | 비고 |
|---|---|---|
| `OPENAI_API_KEY` → REST API | ✅ | 표준이지만 API 키 관리 부담 |
| **OAuth 토큰 → REST API 직접** | ❌ **401** | OAuth 토큰은 세션 토큰이지 API 키가 아님 |
| **OAuth 토큰 → `codex exec` → `image_gen`** | ✅ **본 스킬** | codex exec 내부 브릿지가 OAuth를 이미지 생성 서비스로 라우팅 |

```
codex login (최초 1회)
  → OAuth 토큰이 ~/.codex/auth.json에 저장
    → codex exec가 토큰을 자동 읽기
      → 내장 image_gen 도구가 OAuth로 인증
        → 서비스 측 GPT Image 모델이 이미지 생성
          → 프로젝트 디렉토리에 저장
```

> **주의**: OAuth 토큰으로 OpenAI REST API를 직접 호출하면 HTTP 401. 반드시 `codex exec` 브릿지를 거쳐야 합니다.

## 전제 — codex CLI 설치 + 로그인

| 요구사항 | 명령 | 비고 |
|---|---|---|
| **codex CLI** | `npm install -g @openai/codex` | 이미지 생성 엔진 |
| **codex login** | `codex login` | ChatGPT로 최초 1회 OAuth |

```bash
# 설치·인증 확인
codex --version          # OpenAI Codex v0.1xx.x
codex login status       # "Logged in using ChatGPT"
```

> Cowork 환경에서 Bash가 제한되면 codex CLI 호출이 차단될 수 있습니다. 이 스킬은 **로컬 Claude Code(터미널) 또는 Bash 허용 Cowork 환경**에서 동작합니다. Bash 제한 시 사용자에게 codex 명령어를 안내만 하고 수동 실행을 유도하세요.

## 워크플로우

```
1. 컨텍스트 수집 — 주제·화면비·품질·출력 경로·장수
   (복잡한 프롬프트/한국어 텍스트 → media-gpt-image-prompt로 프롬프트 작성 선행)
    ↓
2. 인자 조립 — --size · --quality · --out · -n + 프롬프트
    ↓
3. codex exec 호출 — image_gen 도구가 GPT Image로 생성
    ↓
4. 이미지 수집 — ~/.codex/generated_images/<session>/ → --out 디렉토리로 복사
    ↓
5. 출력 — 타임스탬프 파일명(codex-image-YYYYMMDD-HHMMSS.png) + 인라인 표시
```

## 옵션

| 플래그 | 값 | 기본값 | 설명 |
|---|---|---|---|
| `--size` | `1024x1024` · `1024x1536` · `1536x1024` · `auto` | `1024x1024` | 이미지 크기 (정사각·세로·가로) |
| `--quality` | `low` · `medium` · `high` · `auto` | `auto` | 생성 품질 (높을수록 느리고 비쌈) |
| `--out` | 디렉토리 경로 | 프로젝트 루트 | 저장 위치 |
| `-n` | 1–10 | `1` | 생성 장수 |

> 위 값은 codex 프롬프트에 자연어로 넣는 힌트입니다. GPT Image 2.5의 `xhigh`·`max` 품질, 자유 해상도(`WIDTHxHEIGHT`), `background=transparent`가 codex 도구에서 그대로 적용되는지는 확인되지 않았습니다. 이 설정이 결과에 꼭 필요하면 Higgsfield `gpt_image_2_5` 경로를 쓰세요.

## 호출 패턴

### 기본 — 자연어 한 줄

```bash
codex exec "Use \$imagegen to create a 1024x1024 image: a red apple on white background, studio lighting. Save to ./apple.png"
```

### 고품질 + 특정 폴더

```bash
codex exec "Use \$imagegen. Generate a 1536x1024 aerial view of jeju island coastline, golden hour. quality high, save to ./public/images/jeju.png"
```

### 여러 변형

```bash
# -n 3 처럼 루프 — codex exec를 3회 호출하거나 한 턴에 3장 지시
codex exec "Use \$imagegen. Create 3 logo variations for a tech startup, minimal, geometric. size 1024x1024, save to ./logos/"
```

### 구조화 출력 + 파이프라인 통합

```bash
codex exec --json --output-last-message ./last.txt \
  "Generate a 1536x1024 productivity-visual hero, save under output/imagegen/hero.png"
```

### 한국어 텍스트 이미지 ★

이미지 안 한글 문구는 **따옴표 + 위치·서체 + 등장 횟수 + 추가 텍스트 금지**를 명시하고, 결과를 음절 단위로 확인합니다:

```bash
codex exec "Use \$imagegen. Text (verbatim, 한글): '2026년 분기 실적'. Typography: bold sans 한글, 검정, 상단 중앙. Render the text exactly once, verbatim, no extra text. quality high, size 1536x1024, save to ./slide-q1.png"
```

> 텍스트 규칙은 `moai-media:media-gpt-image-prompt`의 `references/text-rendering.md`와 같은 원칙을 따릅니다.

## 프롬프트 빌더 체이닝 (권장)

복잡한 장면이나 에디토리얼 품질이 필요하면 `media-gpt-image-prompt`로 먼저 프롬프트를 만드세요:

```
사용자 자연어 → moai-media:media-gpt-image-prompt (공식 가이드 원칙으로 프롬프트 작성)
                    ↓ 산출: 단락 또는 라벨 섹션 프롬프트
              moai-media:media-codex-image (해당 프롬프트로 codex exec 호출 → GPT Image 생성)
```

이 흐름은 `media-higgsfield-image` 경로와 동일한 프롬프트 SSOT를 공유합니다 — 같은 프롬프트로 Higgsfield(`gpt_image_2_5`) 또는 codex 백엔드를 선택해 생성할 수 있습니다.

## 백엔드 선택 — higgsfield vs codex

GPT Image 계열은 두 경로 모두로 생성할 수 있습니다. 환경·비용·제어 필요성에 따라 선택:

| 기준 | `media-higgsfield-image` (Higgsfield MCP) | `media-codex-image` (codex CLI) |
|---|---|---|
| 인증 | Higgsfield API 키 (MCP) | ChatGPT OAuth (API 키 불필요) |
| 비용 | Higgsfield 크레딧 | ChatGPT 구독 한도 |
| 적합 | 프로덕션·CI·멱등·무인 자동화 | 로컬 개발·구독 한도 재사용·API 키 회피 |
| 모델 범위 | 여러 계열(Soul·Nano Banana Pro·GPT Image 2.5·Seedream 등) | GPT Image 단일 (버전 지정 불가) |
| 모델·품질·투명 배경 지정 | 가능 (`variant`·`quality`·`background`) | 프롬프트 힌트만 |
| MCP 의존 | 필요 (`moai-coworker/.mcp.json`) | 불필요 (codex CLI 별도 설치) |

상세 백엔드 정책은 [`moai-officer:doc-html-slide` references/image-backend-policy.md](../../../moai-officer/skills/doc-html-slide/references/image-backend-policy.md) 참조.

## 출력

이미지는 타임스탬프 파일명으로 저장돼 덮어쓰기를 방지합니다:

```
codex-image-20260619-143052.png        # 단일
codex-image-20260619-143052-1.png      # 복수: 첫 번째
codex-image-20260619-143052-2.png      # 복수: 두 번째
```

생성된 이미지는 Claude Code에서 즉시 확인할 수 있도록 인라인으로 표시합니다.

## 프롬프트 팁

OpenAI 공식 이미지 프롬프팅 가이드의 원칙을 따릅니다.

- **결과부터**: 첫 문장에 산출물 종류와 용도(제품 사진·광고·인포그래픽), 구도·배치 제약
- **복잡하면 라벨 섹션**: Scene → Subject → Details → Constraints
- **보이는 디테일**: 재질·조명·색·매체. 사진이면 "photorealistic" 명시. 카메라 사양은 외형 단서일 뿐
- **분위기 단어만 쓰지 않기**: 규모·대기·색을 구체적으로
- **제외 조건은 명시**: "No extra text, no watermark, no unrelated logos"
- **한 번에 하나씩**: 결과를 보고 한 가지만 바꿔 다시 요청

상세는 `media-gpt-image-prompt`의 `references/prompting-fundamentals.md` 참조.

## 주의사항

- **Bash 의존** — codex CLI는 터미널 도구. Claude Code 메인 세션 또는 Bash 허용 환경에서만 동작. Bash 제한 Cowork에서는 codex 명령어 안내만 하고 수동 실행 유도.
- **구독 한도 소모** — 이미지 생성 턴은 일반 턴 대비 한도를 3~5배 빨리 소모 (OpenAI 공식). 대량 생성 시 주의.
- **투명 배경** — GPT Image 2.5 모델은 투명 배경을 지원하지만, codex 도구가 `background=transparent`를 넘기는지는 확인되지 않았습니다. 투명 PNG가 필요하면 Higgsfield `gpt_image_2_5` + `background=transparent`를 쓰고, 결과 파일에 실제 알파 채널이 있는지 확인하세요.
- **승인 정책** — `--dangerously-bapprovals-and-sandbox`는 CI/샌드박스만. 로컬은 `-s workspace-write`로 범위 제한 권장.
- **텍스트/레이아웃 중심 슬라이드** — HTML/CSS 코드 경로 우선 (imagegen "When not to use" 권고). 인포그래픽 숫자·라벨은 인라인 SVG가 정확.

## 비용

이미지 생성 비용은 ChatGPT 구독(Plus/Team/Enterprise) 한도로 청구:

구독 한도에서 차감되는 양은 요금제·크기·품질에 따라 다르며 OpenAI가 공지하는 기준을 따릅니다. API로 직접 생성할 때의 요금은 [OpenAI 이미지 생성 요금표](https://developers.openai.com/api/docs/pricing#image-generation)에서 확인하세요. 빠른 모델이 더 싸다고 가정하지 않습니다.

## 보안

- **API 키 저장/전송 없음** — OAuth only
- **텔레메트리 없음** — 추적·에러 리포팅 없음
- **이미지 로컬 저장** — 프로젝트 디렉토리에만, 외부 업로드 없음
- **단일 외부 연결** — codex CLI를 통한 `api.openai.com`만

## 문제 해결

| 문제 | 해결 |
|---|---|
| `NOT_FOUND` (codex 없음) | `npm install -g @openai/codex` |
| 인증 만료 | `codex login` 재실행 |
| Trust 오류 | 프로젝트를 `~/.codex/config.toml` 신뢰 목록 추가 또는 `--skip-git-repo-check` |
| 타임아웃 (>2분) | `--quality low`로 속도 향상 |
| 401 on REST API | 예상 동작 — OAuth 토큰은 REST 직접 호출 불가. `codex exec` 사용. |
| `image_gen` 도구 없음 | `npm update -g @openai/codex` |

## 관련 스킬

| 스킬 | 관계 | 설명 |
|---|---|---|
| media-gpt-image-prompt | before | GPT Image 2.5 프롬프트 빌더 — 복잡한 장면·한국어 텍스트 시 선행 |
| media-higgsfield-image | alternative | Higgsfield MCP 경로 (프로덕션/CI). `gpt_image_2_5` Flare·Sunburst 지정 가능 |
| media-gemini-3-image-prompt | sibling | Gemini 어조 프롬프트 (Nano Banana Pro) |

## 출처

1차 (공식):
- [OpenAI Codex CLI — GitHub](https://github.com/openai/codex) — codex CLI 공식, `image_gen` 내장 도구
- [OpenAI — Image prompting (GPT Image 2.5 prompting guide)](https://developers.openai.com/api/docs/guides/image-prompting) — 프롬프팅 원칙·파라미터 (2026-09-13 확인)

참고 스킬 (MIT):
- [wjb127/codex-image](https://github.com/wjb127/codex-image) — Claude Code 스킬, OAuth 브릿지 패턴·옵션·출력 파일명 규약 참고. 본 스킬은 wjb127의 핵심 인사이트(OAuth→REST 401, codex exec 브릿지)를 채택하고 moai-media 정책(프롬프트 빌더 체이닝·한국어 문구 규칙·higgsfield 백엔드 선택)으로 확장했습니다.
