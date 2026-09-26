# Gemini 3 Pro Image — Parameter Cheatsheet

Google AI Studio·Vertex AI·Gemini API의 설정 화면과 요청 형식은 다릅니다. 이 문서는 값의 뜻을 설명하며, 필드 경로는 아래 API별 항목을 따릅니다.

## 모델 선택

| 모델 ID | 별명 | 용도 |
|---|---|---|
| `gemini-3-pro-image` | Nano Banana Pro | 복잡한 이미지 작업, 최대 4K |
| `gemini-3.1-flash-image` | Nano Banana 2 | 일반 이미지 작업, 최대 4K |

## aspect_ratio

| 값 | 용도 | 두 모델 지원 |
|---|---|---|
| `1:1` (권장) | SNS 정사각 | ✅ Pro · ✅ Flash |
| `16:9` | 와이드, 유튜브 | ✅ · ✅ |
| `9:16` | 릴스·쇼츠 | ✅ · ✅ |
| `4:5` | 인스타 피드 | ✅ · ✅ |
| `5:4` | 인스타 가로 | ✅ · ✅ |
| `3:2` | 사진 표준 | ✅ · ✅ |
| `2:3` | 책 표지 | ✅ · ✅ |
| `4:3` | TV 클래식 | ✅ · ✅ |
| `3:4` | 모바일 세로 | ✅ · ✅ |
| `21:9` | 시네마틱 울트라와이드 | ✅ · ✅ |
| `1:4`·`4:1`·`1:8`·`8:1` | 극단 비율 (배너·스트립) | ❌ Pro · ✅ Flash 전용 |

## image_size

Gemini 이미지 요청의 크기는 `1K`·`2K`·`4K` 중에서 고릅니다. 아래 `512`는 Gemini 3.1 Flash Image 전용입니다. 실제 필드 경로는 Interactions API와 GenerateContent API가 다르며, 앱 UI의 이름도 현재 화면에서 확인합니다.

| 값 | 픽셀 어림 | Pro | Flash |
|---|---|---|---|
| `512` (0.5K) | 약 0.5K | ❌ | ✅ |
| `1K` (권장 초안) | 약 1024 | ✅ | ✅ |
| `2K` (권장 production) | 약 2048 | ✅ | ✅ |
| `4K` | 약 4096 | ✅ | ✅ |

## 모델과 추론 설정

| 선택 | 동작 | 권장 |
|---|---|---|
| Gemini 3.1 Flash Image | 처리량·속도 우선 | 초안 탐색, A/B |
| Gemini 3 Pro Image | 복잡한 제작에 적합 | 최종 자산, 복잡 구도, 텍스트 검수 |

두 모델을 공통 `mode=Thinking` API 값으로 전환하지 않습니다. Gemini 3.1 Flash Image의 추론 수준은 API에서 `generation_config.thinking_level`의 `minimal`·`high`로 조절할 수 있습니다. Pro의 추론은 모델 특성으로 설명하고 지원되지 않은 전환 값을 만들지 않습니다.

## reference images

- 총 최대 **14개**를 섞을 수 있습니다. Gemini 3 Pro Image는 그중 고충실도 객체 이미지 최대 6개, 캐릭터 일관성 이미지 최대 5개, 스타일 참조 이미지 최대 3개까지 지원합니다. Gemini 3.1 Flash Image의 유형별 한도는 객체 10개·캐릭터 4개이며 공식 표에 별도의 스타일 참조 칸은 없습니다.
- 지원 MIME: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`.
- 권장 사용: 각 이미지에 피사체·캐릭터·스타일·구도 중 맡길 역할을 적고, 유형별 한도를 넘기지 않습니다. 이미지 순서 자체의 우선순위는 공식 보장으로 취급하지 않습니다.

상세는 `references/reference-images.md`.

## Search Grounding

데이터 시각화·인포그래픽·지도·통계 그래프에 활성화 권장. Gemini가 Google Search를 사용해 사실 데이터를 가져옴.

활성화 방법: 현재 앱의 Google Search 도구 지원을 확인합니다. API에서는 이미지 프롬프트와 별도로 `google_search` 도구를 설정합니다. 기준 날짜와 확인할 공식 출처를 프롬프트에 적습니다.

주의: 결과는 항상 별도 검증. 모델이 정보를 잘못 해석할 수 있음.

## 토큰 제한

| 모델 | 입력 토큰 | 출력 토큰 |
|---|---|---|
| Gemini 3 Pro Image | 65,536 | 32,768 |
| Gemini 3.1 Flash Image | 131,072 | 32,768 |

긴 텍스트 + 다중 reference 이미지를 함께 사용할 때 토큰 budget 주의.

## API 호출

이 스킬은 프롬프트 텍스트만 만듭니다. 다음은 **서로 다른 요청 형식**의 설정 위치입니다.

| 경로 | 16:9·2K 이미지 설정 예 | 공식 문서 |
|---|---|---|
| Interactions API | `response_format={"type":"image","aspect_ratio":"16:9","image_size":"2K"}` | [이미지 생성 가이드](https://ai.google.dev/gemini-api/docs/image-generation#aspect-ratios-and-image-size) |
| GenerateContent REST | `generationConfig.responseFormat.image={"aspectRatio":"16:9","imageSize":"2K"}` | [GenerateContent 이미지 가이드](https://ai.google.dev/gemini-api/docs/generate-content/image-generation#generate-images-up-to-4k-resolution) |

SDK 언어별 필드 이름과 Vertex AI 설정은 해당 경로의 현재 공식 문서에서 확인합니다. 한 경로의 설정을 다른 경로에 그대로 복사하지 않습니다.

## SynthID 워터마크

- 모든 출력 이미지에 **자동 imperceptible 워터마크 삽입** (Google 정책).
- 워터마크 비활성화 불가.
- SynthID 검증 도구로 "Gemini로 생성·편집됐는지" 판별 가능.
- 사용권과 공개 조건은 현재 서비스 약관·계정 조건에서 확인합니다.

## 비용

모델·해상도·입력 이미지·서비스에 따라 현재 가격이 달라집니다. 생성 전에 해당 계정의 공식 가격 화면에서 확인합니다.

## 출처

- [Google AI for Developers — Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Google Cloud Documentation — Gemini 3 Pro Image (Vertex AI)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image)
- [Google AI Studio — Gemini 3 Pro Image](https://aistudio.google.com/models/gemini-3-pro-image)
