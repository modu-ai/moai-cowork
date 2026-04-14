---
name: fal-gateway
description: >
  fal.ai 통합 MCP 게이트웨이 — 1개 API 키로 1000+ AI 미디어 모델 접근.
  Flux 1.1 Pro(이미지), Ideogram 3.0(텍스트 렌더), Recraft V3(벡터·로고),
  Kling 3.0(영상), Hailuo 2.3(저가 영상), Luma Ray3, Pika 2.2, MiniMax Music 등.
  'fal.ai로 Flux 이미지', 'Recraft 로고', 'Hailuo 영상', 'MiniMax 음악 생성',
  '/moai-media fal-gateway'로 호출하세요.
user-invocable: true
metadata:
  version: "1.1.1"
  status: "stable"
  updated: "2026-04-14"
  tags: "fal,gateway,flux,recraft,hailuo,luma,pika,music,multi-model"
---

# fal.ai Gateway — 통합 미디어 모델 접근

> moai-media v1.1.1 | hosted MCP (`https://mcp.fal.ai/mcp`)

## 개요

[fal.ai](https://fal.ai)는 1000+ AI 미디어 모델을 **단일 API·단일 결제·단일 키**로 통합 제공합니다.
`moai-media`의 `ideogram`, `kling` 스킬은 fal.ai를 내부적으로 사용하지만, 본 스킬은
**그 외 모델에 범용 접근**할 때 사용합니다.

## 이 스킬 vs 전용 스킬

| 모델 | 사용할 스킬 |
|---|---|
| Ideogram 3.0 | `ideogram` (전용, 한국어 팁 포함) |
| Kling 3.0 | `kling` (전용, 립싱크·숏폼 가이드) |
| Imagen 4 (Nano Banana) | `nano-banana` (전용) |
| **Flux 1.1 Pro** | **fal-gateway** |
| **Recraft V3** (벡터·로고) | **fal-gateway** |
| **Hailuo 2.3** (저가 영상) | **fal-gateway** |
| **Luma Ray3** | **fal-gateway** |
| **Pika 2.2** | **fal-gateway** |
| **MiniMax Music 2.5** (Suno 대체) | **fal-gateway** |

## 주요 모델 카탈로그

### 이미지

| 모델 ID | 특징 | 비용/장 |
|---|---|---|
| `fal-ai/flux-pro/v1.1` | 범용 최고 품질 사실적 | $0.04 |
| `fal-ai/flux-pro/v1.1-ultra` | 4K·고해상도 | $0.06 |
| `fal-ai/recraft-v3` | 벡터·로고·일관된 브랜드 컬러 | $0.04 (래스터) / $0.08 (벡터) |
| `fal-ai/stable-diffusion-v35-large` | 오픈소스 베이스라인 | $0.04 |

### 영상

| 모델 ID | 특징 | 비용 |
|---|---|---|
| `fal-ai/minimax/hailuo-02/standard/text-to-video` | 최저가 시안용 (768p) | $0.045/sec |
| `fal-ai/minimax/hailuo-02/pro/text-to-video` | 1080p 고품질 | $0.08/sec |
| `fal-ai/luma-dream-machine/ray-2` | 숏폼 부드러운 모션 | $0.32/MP |
| `fal-ai/pika/v2.2/text-to-video` | 스타일라이즈 · VFX | ~$0.05/영상 |

### 음악·오디오

| 모델 ID | 특징 | 비용 |
|---|---|---|
| `fal-ai/minimax-music` | Suno 합법 대체 (공식 API) | $0.035/곡 |
| `fal-ai/stable-audio` | BGM·효과음 생성 | $0.02/클립 |

## 호출 방식

MCP 서버는 `moai-media/.mcp.json`에 자동 등록되어 있습니다:

```
MCP tool: fal-ai
operation: run_model
arguments:
  model_id: "fal-ai/flux-pro/v1.1"
  inputs:
    prompt: "미니멀한 카페 인테리어, 따뜻한 조명, 원목 가구"
    aspect_ratio: "3:4"
    num_images: 1
```

Claude에게 자연어로 요청하면 MCP가 자동으로 모델 선택·파라미터 구성합니다.

## 추천 워크플로우

### 카드뉴스 10장 시리즈

1. **표지 슬라이드**: `ideogram` 스킬 (제목 텍스트 렌더링)
2. **본문 슬라이드 8장**: `fal-gateway` + Flux 1.1 Pro (일관된 화풍)
3. **엔딩 CTA**: `ideogram` 스킬 (행동 유도 텍스트)

### 브랜드 숏폼 패키지

1. **로고**: `fal-gateway` + Recraft V3 (벡터 출력)
2. **키비주얼**: `fal-gateway` + Flux Pro Ultra
3. **15초 영상**: `kling` 또는 `fal-gateway` + Hailuo (비용 우선 시)
4. **내레이션**: `elevenlabs`
5. **BGM**: `fal-gateway` + MiniMax Music

## API 키 설정

- 환경변수: `FAL_KEY`
- 발급처: [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys)
- 가입 시 **$5 무료 크레딧** 제공 (약 이미지 125장 또는 영상 60초 분량)
- 결제: 해외카드 필수 (트래블월렛·우리카드 권장)

## 비용 관리 팁

- **시안 단계**: Hailuo Standard ($0.045/sec), Flux 초안용
- **최종 단계**: Kling Pro / Flux Ultra / Recraft 벡터
- fal.ai 대시보드에서 월 예산 한도 설정 가능
- `num_images: 1` 기본 유지, A/B 테스트 시만 증가

## 연계 스킬

- `ideogram`, `kling`, `nano-banana`, `elevenlabs` (모두 moai-media)
- 크리에이티브 캠페인 스킬 (`campaign-planner` in moai-marketing)

## 참고

- [fal.ai MCP 런칭 블로그](https://blog.fal.ai/connect-your-ai-to-1-000-models-with-the-fal-mcp-server/)
- [fal.ai 모델 카탈로그](https://fal.ai/models)
- [fal.ai 가격](https://fal.ai/pricing)
