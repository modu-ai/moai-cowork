---
name: ideogram
description: >
  Ideogram 3.0으로 한국어·영문 타이포그래피가 포함된 AI 이미지를 생성합니다.
  카드뉴스 제목·인스타 썸네일·포스터·광고 카피 이미지처럼 **텍스트 렌더링 품질이 중요한 이미지**에 최적.
  '카드뉴스 제목 이미지', '타이포 포스터 만들어줘', '텍스트 들어간 썸네일',
  '/moai-media ideogram'으로 호출하세요.
  Imagen 대비 한국어 글자 렌더링이 우수합니다. fal.ai MCP 경유.
user-invocable: true
metadata:
  version: "1.2.0"
  status: "stable"
  updated: "2026-04-14"
  tags: "image,ideogram,typography,korean-text,card-news,poster,thumbnail"
---

# Ideogram 3.0 — 한국어 타이포 특화 이미지 생성

> moai-media v1.2.0 | fal.ai MCP 경유

## 개요

[Ideogram 3.0](https://about.ideogram.ai)은 **이미지 내 텍스트 렌더링 품질이 업계 최고**인 모델입니다.
제목·슬로건·로고 풍 카피처럼 글자가 중요한 이미지에는 Nano Banana보다 Ideogram을 우선 사용하세요.

### 언제 이 스킬을 쓰나?

| 상황 | 권장 스킬 |
|---|---|
| 카드뉴스 **제목 슬라이드** (큰 한글 헤드라인 포함) | **ideogram** ⭐ |
| 일반 배경·이미지 (텍스트 없음) | nano-banana |
| 인스타 썸네일 (제목 텍스트 포함) | **ideogram** ⭐ |
| 포스터·광고 크리에이티브 | **ideogram** ⭐ |
| 제품 사진·풍경 사진 | nano-banana |

## 호출 방식

### fal.ai MCP 경유 (권장)

`.mcp.json`에 등록된 `fal-ai` MCP 서버를 통해 호출:

```
model: fal-ai/ideogram/v3
inputs:
  prompt: "'오늘의 인사이트' 라는 한글 타이틀, 미니멀 배경, 파스텔 톤"
  rendering_speed: TURBO | DEFAULT | QUALITY
  aspect_ratio: 3:4 | 1:1 | 9:16 | 16:9
  style: AUTO | GENERAL | REALISTIC | DESIGN
```

### 렌더링 속도(비용) 가이드

| 모드 | 품질 | 비용/장 | 용도 |
|---|---|---|---|
| TURBO | 낮음 | $0.03 | 시안·A/B 테스트 |
| DEFAULT (권장) | 중간 | $0.06 | 일반 제작물 |
| QUALITY | 높음 | $0.08 | 최종 납품·인쇄 |

## 프롬프트 팁 (한국어 텍스트)

- 텍스트는 **큰따옴표**로 감싸기: `"완벽한 주말" 이라는 제목`
- 폰트 스타일 명시: `깔끔한 고딕 폰트` / `손글씨 느낌의 한글` / `진한 세리프`
- 배경 요소와 분리: `상단에 제목, 하단에 제품 이미지`
- 줄바꿈 지시: `두 줄로 나눠서`

## API 키 설정

fal.ai MCP 공통 키 1개 사용:
- 환경변수: `FAL_KEY`
- 발급처: [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys) ($5 무료 크레딧 제공)

## 연계 스킬

- `nano-banana` (moai-media) — 텍스트 없는 배경 이미지 보완
- `kling` (moai-media) — 이미지 → 영상 변환 시 소스로 사용
- `card-news` (moai-content) — 제목 슬라이드는 ideogram, 본문 이미지는 nano-banana 혼합

## 참고

- [Ideogram 3.0 공식 블로그](https://about.ideogram.ai/3.0)
- [fal.ai Ideogram 모델 페이지](https://fal.ai/models/fal-ai/ideogram/v3)
