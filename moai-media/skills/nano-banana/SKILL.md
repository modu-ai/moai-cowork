---
name: nano-banana
description: >
  Google Gemini API 기반 AI 이미지 생성 스킬. Nano Banana Pro(gemini-3-pro-image-preview),
  Nano Banana 2(gemini-3.1-flash-image-preview), 원조 Nano Banana(gemini-2.5-flash-image)를
  단일 GEMINI_API_KEY로 사용. 카드뉴스·인스타 피드·썸네일·포스터에 최적.
  한국어 텍스트 렌더링 SOTA, 최대 4K 해상도, 14종 화면비 지원.
  '나노바나나 이미지', '구글 이미지 생성', '카드뉴스 이미지', '인스타 썸네일',
  '/moai-media nano-banana'로 호출하세요.
user-invocable: true
metadata:
  version: "1.1.1"
  status: "stable"
  updated: "2026-04-14"
  tags: "image,nano-banana,gemini,google,card-news,instagram,korean,4k"
---

# Nano Banana — Google Gemini AI 이미지 생성

> moai-media v1.1.1 | Gemini 3 Image Preview 공식 모델

## 개요

Google의 공식 AI 이미지 브랜드 **"Nano Banana"**는 2026년 Q1에 Imagen 4 계열에서 **Gemini 3 Image Preview 계열로 재정의**되었습니다.
본 스킬은 공식 문서(`ai.google.dev/gemini-api/docs/image-generation`) 스펙 기준 최신 모델 ID를 사용합니다.

## 모델 카탈로그 (공식)

| Alias | 공식 모델 ID | 용도 | 출력 해상도 | 이미지당 비용 |
|---|---|---|---|---|
| `nano-banana-pro` (기본) | `gemini-3-pro-image-preview` | 카드뉴스·포스터·광고, 텍스트 렌더링 SOTA | 1K/2K/4K | $0.134 (1K/2K), $0.24 (4K) |
| `nano-banana-2` | `gemini-3.1-flash-image-preview` | 초안·대량 A/B, 비용 효율 | 512/1K | $0.045 (0.5K), $0.067 (1K) |
| `nano-banana` | `gemini-2.5-flash-image` | 원조 버전, 최저가 | 기본 | **$0.039** |
| `nano-banana-ultra` | `gemini-3-pro-image-preview` + `image_size="4K"` | 대형 인쇄·광고 마스터 | 4K | $0.24 |

**레거시 Imagen 4 별칭** (`imagen-4.0-*`)은 자동으로 Gemini 3 계열로 전환됩니다 (스크립트 MODEL_MAP).

⚠️ **무료 티어 불가**: 세 모델 모두 Free Tier에서 호출 불가, Pay-as-you-go 유료 플랜 필수 (공식 문서 명시).

## 영상은 `kling` 스킬 사용

**이 스킬은 이미지 전용입니다.** 영상 생성은 별도 스킬 [`kling`](../kling/SKILL.md)을 사용하세요.

| 용도 | 스킬 |
|---|---|
| 이미지 (카드뉴스, 썸네일, 포스터) | **nano-banana** (본 스킬) |
| 한국어 대형 타이포 이미지 | `ideogram` |
| **모든 영상 (숏폼·광고·브랜드)** | **`kling`** |

## 호출 방식

### CLI (간편 스크립트)

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_image.py" \
  "평온한 아침 책상, 커피잔과 노트북, 자연광" \
  output/slide_01.png 3:4 nano-banana-pro
```

### Python SDK (공식, 권장)

```python
from google import genai

client = genai.Client()  # GEMINI_API_KEY 환경변수 자동 인식

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",  # 또는 gemini-3-pro-image-preview
    contents=["Create a picture of a minimal cafe interior with warm lighting"],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

### REST (camelCase)

```bash
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent
Content-Type: application/json

{
  "contents": [{"role": "user", "parts": [{"text": "..."}]}],
  "generationConfig": {
    "responseModalities": ["TEXT", "IMAGE"],
    "imageConfig": {
      "aspectRatio": "3:4",
      "imageSize": "2K"
    }
  }
}
```

응답: `candidates[0].content.parts[].inlineData.data` (base64 인코딩된 이미지)

**주의 — 네이밍 컨벤션**:
- **Python SDK**: snake_case (`response_modalities`, `image_config`, `aspect_ratio`, `image_size`, `inline_data`)
- **REST/JS SDK**: camelCase (`responseModalities`, `imageConfig`, `aspectRatio`, `imageSize`, `inlineData`)

## 지원 화면비 (공식 14종)

`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`,
`1:4`, `4:1`, `1:8`, `8:1`

- 카드뉴스: `3:4` (인스타 세로)
- 인스타 피드: `1:1`
- 릴스/스토리: `9:16`
- 유튜브: `16:9`
- 시네마틱: `21:9`
- 배너: `8:1`, `4:1`

## 지원 해상도 (`image_size`)

| 값 | 실제 크기 | 권장 용도 |
|---|---|---|
| `"512"` | 512px | 썸네일·시안 (gemini-3.1-flash-image-preview만) |
| `"1K"` | ~1024px | 일반 SNS 포스트 |
| `"2K"` | ~2048px | **카드뉴스 권장 (기본)** |
| `"4K"` | ~4096px | 대형 인쇄·광고 마스터 |

## 프롬프트 팁 (한국어 텍스트 렌더링)

Nano Banana Pro는 한국어 타이포그래피 렌더링 품질이 매우 우수합니다:

- 텍스트는 **큰따옴표**로 명확히: `"완벽한 주말" 이라는 제목`
- 폰트 스타일: `깔끔한 고딕`, `진한 세리프`, `손글씨 느낌 한글`
- 위치 지시: `상단 중앙에 큰 글씨로`, `하단 우측 작게`
- 줄바꿈: `두 줄로 나눠서 중앙 정렬`
- 배경 분리: `파스텔 배경, 텍스트는 검정색`

## API 키 설정

- 환경변수: **`GEMINI_API_KEY`** (권장)
  - 레거시 호환: `NANO_BANANA_API_KEY`도 인식 (v1.0.x 사용자 무중단)
- 발급처: [ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)
- **Pay-as-you-go 결제 활성화 필수** (무료 티어에서 호출 불가)

## 비용 예시

| 시나리오 | 모델 | 해상도 | 비용 |
|---|---|---|---|
| 카드뉴스 10장 시리즈 (권장) | nano-banana-pro | 2K | $1.34 |
| 썸네일 100장 대량 | nano-banana | 기본 | $3.90 |
| A/B 초안 50장 | nano-banana-2 | 1K | $3.35 |
| 광고 마스터 1장 | nano-banana-ultra | 4K | $0.24 |

**월 예산 예시**: 포트폴리오 3 브랜드 × 주 1편 카드뉴스 × 한 달 = 약 $16

## 이관 이력 (v1.1.0 → v1.1.1)

- **v1.1.1 (2026-04-14)**: 스킬명 `google-media` → `nano-banana` (image-only로 스코프 축소)
- v1.1.0: 기존 Imagen 4 → Gemini 3 Image Preview 마이그레이션
- 영상 생성(Veo 3.1)은 **`kling` 스킬**로 통합 (본 플러그인 영상 단일 경로)

## 연계 스킬

- [`kling`](../kling/SKILL.md) — **영상 생성 전담** (숏폼·광고·립싱크)
- [`ideogram`](../ideogram/SKILL.md) — 한국어 대형 타이포 특화 (본 스킬 보완)
- [`elevenlabs`](../elevenlabs/SKILL.md) — 음성·TTS (이미지 + 내레이션 조합)
- [`fal-gateway`](../fal-gateway/SKILL.md) — Flux·Recraft 등 non-Google 모델
- `card-news` (moai-content) — 본 스킬 호출로 카드뉴스 이미지 생성

## 공식 참고 문서

- [Gemini API Image Generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Gemini 3 Pro Image Preview 모델 카드](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview)
- [Gemini API 가격](https://ai.google.dev/gemini-api/docs/pricing)
- [Nano Banana Pro 공식 소개 블로그](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-pro-image-developers/)
