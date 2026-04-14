---
name: kling
description: >
  Kling 3.0으로 숏폼 영상(릴스/쇼츠/틱톡)을 AI 생성합니다. 텍스트→영상, 이미지→영상 지원.
  다국어 립싱크, 최대 15초 클립, SNS 캠페인 ROI 최강.
  **moai-media 플러그인의 유일한 영상 생성 스킬** (Veo는 v1.1.1에서 제거됨, Kling 단일화).
  '숏폼 영상 만들어줘', '이미지 움직여줘', '릴스 영상 생성', '립싱크 영상',
  '/moai-media kling'으로 호출하세요. fal.ai MCP 경유.
user-invocable: true
metadata:
  version: "1.1.2"
  status: "stable"
  updated: "2026-04-14"
  tags: "video,kling,short-form,reels,tiktok,lip-sync,fal"
---

# Kling 3.0 — 숏폼 영상 생성

> moai-media v1.1.1 | fal.ai MCP 경유

## 개요

[Kling 3.0](https://klingai.com)은 Kuaishou가 개발한 AI 영상 생성 모델로, **숏폼 영상 크리에이터의 ROI 최강 선택지**입니다.

- 최대 **15초** 클립 (5초 / 10초 / 15초 선택)
- **다국어 립싱크** 지원 (한국어 포함)
- Text-to-Video, Image-to-Video, Video Extension 모두 지원
- 외부 프리미엄 모델 대비 **약 1/5 가격**

## 언제 이 스킬을 쓰나?

| 용도 | 권장 스킬 |
|---|---|
| **인스타 릴스 / 유튜브 쇼츠 / 틱톡** | **kling** ⭐ |
| 프리미엄 광고 영상 (1080p + 립싱크) | **kling Pro 모드** |
| 스틸 이미지를 움직이게 | **kling** (Image-to-Video) |
| 립싱크 캐릭터 영상 | **kling** ⭐ |

## 호출 방식 (fal.ai MCP)

```
model: fal-ai/kling-video/v3/text-to-video
inputs:
  prompt: "한국 카페에서 커피를 내리는 바리스타의 손, 따뜻한 조명, 천천히 카메라 이동"
  duration: 5 | 10 | 15   # 초
  aspect_ratio: 9:16 | 1:1 | 16:9
  cfg_scale: 0.5           # 프롬프트 충실도 (0.0~1.0)
```

이미지→영상:
```
model: fal-ai/kling-video/v3/image-to-video
inputs:
  prompt: "제품이 서서히 회전하며 빛이 반사됨"
  image_url: "https://..."  # 출발 이미지
  duration: 10
```

## 비용 가이드 (2026-04 기준)

| 모드 | 비용 | 용도 |
|---|---|---|
| Standard 5초 | ~$0.42 | 시안·빠른 프로토타입 |
| Standard 10초 | ~$0.84 | 일반 릴스/쇼츠 |
| Pro 10초 (립싱크) | ~$1.68 | 브랜드 캠페인 |

## 프롬프트 팁

- **카메라 워크 명시**: `천천히 줌인`, `좌에서 우로 팬`, `정적 와이드샷`
- **움직임 구체화**: `바람에 흩날리는 머리카락`, `손 움직임`, `제품 회전`
- **한 장면 원칙**: 15초 안에 장면 전환 여러 번 넣지 말 것
- **립싱크**: `입 모양이 "안녕하세요"를 말하는` 식으로 명시

## API 키 설정

fal.ai 공통 키 1개 사용 (ideogram과 공유):
- 환경변수: `FAL_KEY`
- 발급처: [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys)

## 데이터 처리 주의사항 (한국 크리에이터)

- Kling API는 Kuaishou(중국) 인프라 기반. 민감 브랜드·개인정보 포함 프롬프트는 **사전 검토 필수**
- 업로드 이미지에 인물 얼굴이 포함된 경우 당사자 동의 확보
- 상업 이용 시 fal.ai 라이선스 약관 확인

## 연계 스킬

- `ideogram` (moai-media) — 제목 이미지 생성 → Kling으로 움직임 부여
- `elevenlabs` (moai-media) — AI 내레이션 생성 → 영상 포스트프로덕션에서 합성
- `card-news` (moai-content) — 카드뉴스 표지 슬라이드를 Kling으로 영상화

## 참고

- [fal.ai Kling 3.0 모델](https://fal.ai/models/fal-ai/kling-video)
- [Kling 공식 사이트](https://klingai.com)
