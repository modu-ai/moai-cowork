---
name: card-news
description: >
  인스타그램 카드뉴스와 캐러셀을 만들어주는 스킬입니다. "카드뉴스 만들어줘", "인스타 슬라이드 기획해줘",
  "캐러셀 콘텐츠 구성해줘"처럼 말하면 됩니다. AI 이미지 생성 기반 캐러셀 카드뉴스 제작,
  잡지 SOP 적용, 디자인 가이드, AI 글쓰기 방지 기법을 지원합니다.
user-invocable: true
metadata:
  version: "1.1.3"
  status: "stable"
  updated: "2026-04-09"
---

# 카드뉴스 (Card News)

> moai-content | 카드뉴스 전문 스킬

## 지원 영역

- 인스타그램 캐러셀 카드뉴스 기획·제작
- AI 이미지 생성 기반 비주얼 콘텐츠
- 잡지 SOP 적용 편집 디자인
- AI 글쓰기 방지 기법으로 오리지널 문체 구현

참조 가이드: `references/card-news/guide.md`, `references/card-news/anti-ai-writing.md`, `references/card-news/magazine-sop.md`, `references/card-news/design-guide.md`

**이미지 생성**: `moai-media` 플러그인의 `google-media` 스킬 호출 또는 직접 스크립트 실행:
`${MOAI_MEDIA_PLUGIN_ROOT}/scripts/generate_image.py` (v1.1.0 이관, Gemini 3 Image Preview 기반)

## AI 이미지 생성 (moai-media 연동)

이미지 생성은 **`moai-media` 플러그인의 `google-media` 스킬**이 담당합니다. card-news는 프롬프트만 생성하고 실제 렌더링은 moai-media에 위임합니다.

### API 키 필수 (Gemini API)

```
IF GEMINI_API_KEY (또는 레거시 NANO_BANANA_API_KEY) 미설정:
  "AI 이미지 생성을 위해 Gemini API 키가 필요합니다.

   발급 방법:
   1. https://ai.google.dev/ 접속 → Google 계정 로그인
   2. API 키 생성 (Nano Banana 계열 이미지 모델은 Pay-as-you-go 유료 플랜 필수)

   API 키를 입력해 주세요:"

  → 키 입력 후 ${CLAUDE_PLUGIN_DATA}/moai-credentials.env에 저장
```

### 모델/해상도 미지정 시 선택 요청

config.json에 복수 모델/비율/해상도가 설정되어 있고
사용자가 명시하지 않은 경우:

AskUserQuestion (1질문, 3옵션):
```
"어떤 모델로 이미지를 생성할까요?"
○ Nano Banana Pro — gemini-3-pro-image-preview (2K, 텍스트 렌더링 SOTA, 권장)
○ Nano Banana 2 — gemini-3.1-flash-image-preview (1K, 빠름, 저비용)
+ Other
```

AskUserQuestion (1질문, 4옵션):
```
"이미지 해상도를 선택하세요"
○ 1K — 기본, 빠른 생성 (권장)
○ 2K — 고해상도, 인쇄용
○ 4K — 최고 해상도 (비용 2배)
○ 512 — 미리보기/썸네일
+ Other
```

AskUserQuestion (1질문, 4옵션):
```
"이미지 비율을 선택하세요"
○ 3:4 — 인스타그램 피드 (권장)
○ 1:1 — 정사각형
○ 9:16 — 세로형 (스토리/릴스)
○ 16:9 — 가로형 (블로그/PT)
+ Other
```

### 지원 해상도 (공식 문서 기준)

| 해상도 | 크기 | 토큰 비용 | 용도 |
|--------|------|----------|------|
| 512 | ~0.25MP | 낮음 | 미리보기, 썸네일 |
| 1K | ~1MP | 1120 토큰 | 기본 (웹용) |
| 2K | ~4MP | 1120 토큰 | 고해상도 (인쇄) |
| 4K | ~16MP | 2000 토큰 | 최고 해상도 (프리미엄) |

참고: 해상도 파라미터는 대문자 K 필수 (1K, 2K, 4K). 소문자 거부됨.
512는 K 접미사 없이 사용. Gemini 3.1 Flash Image에서만 지원.

## 트리거 키워드

카드뉴스, 캐러셀, 인스타그램 카드, 슬라이드, AI 이미지, 카드 디자인, 인포그래픽 카드

## 사용 예시

- "스타트업 투자 유치 방법을 카드뉴스로 만들어줘"
- "인스타 캐러셀 10장 기획해줘 (주제: 시간 관리)"
- "제품 소개 슬라이드 콘텐츠 구성해줘"
- "AI 이미지로 카드뉴스 만들어줘"
- "잡지 스타일 인포그래픽 카드 만들어줘"

## 독립 실행 워크플로우

참조 가이드(`references/`)를 사용할 수 없는 경우 다음 단계로 실행합니다.

### 1단계: 목적 및 주제 파악
- 카드뉴스 목적: 정보 전달 / 브랜드 인지 / 제품 소개 / 리드 수집
- 주제와 핵심 메시지 1가지 확정
- 타겟 독자 정의

### 2단계: 카드 구성 설계 (표준 10장)
```
1장: 표지 (Cover) — 제목 + 후킹 문구 (1초 내 시선 고정)
2~8장: 본문 (Body) — 핵심 정보 1가지/장, 텍스트 최소화
9장: 요약 (Summary) — 핵심 내용 3가지 불릿
10장: CTA — "저장하기", "팔로우", "링크 클릭" 중 1가지만
```

### 3단계: 카드별 카피 작성
- 장당 텍스트: 15~30자 이내 (모바일 가독성)
- 숫자·통계 강조: "3가지", "10분", "87%" 등 시각적 강조
- AI 문체 방지: 나열식 설명 금지, 구어체·직접 화법 사용

### 4단계: 디자인 가이드
```
레이아웃: 9:16 세로 (인스타 최적화) 또는 1:1 정방형
폰트: 제목 굵게(Bold), 본문 Regular, 최대 2가지 폰트
색상: 브랜드 컬러 + 1가지 포인트 컬러 (과다 사용 금지)
여백: 콘텐츠 면적의 30% 이상 여백 확보 (숨 쉬는 디자인)
이미지: 전체 배경 또는 우측 50% 배치
```

### 5단계: 이미지 생성 (AI)
- `moai-media/scripts/generate_image.py` (moai-media 플러그인 설치 필요) 활용
- 또는 이미지 프롬프트 생성 후 Midjourney/Firefly에서 생성

### 6단계: 산출물 전달
- 카드별 텍스트 + 디자인 가이드
- 이미지 생성 프롬프트 (AI 도구용)
- 인스타그램 캡션 + 해시태그 세트

## 실행 규칙

1. 사용자 요청 수신 → 카드뉴스 요청 확인
2. `references/card-news/guide.md` 로드 → SOP에 따라 실행
3. AI 이미지 생성 필요 시 → `moai-media/scripts/generate_image.py` (moai-media 플러그인 설치 필요) 활용
4. `--deepthink` 또는 복잡 작업 → `mcp__sequential-thinking__sequentialthinking` 호출
5. 결과물 생성 후 사용자 검토 요청

⚠️ **AI 생성 콘텐츠 주의**: AI가 생성한 카드뉴스 내용은 사실 확인 후 게시하세요. 통계, 수치, 인물 정보는 반드시 원출처를 검증하세요.

## 문제 해결

- **플랫폼 규격 변경**: 인스타그램 캐러셀 규격은 변경될 수 있습니다. 최신 규격은 인스타그램 공식 채널에서 확인하세요.
- **브랜드 가이드 미제공**: 브랜드 컬러, 폰트, 톤앤매너 정보를 제공하면 더 일관된 디자인 가이드를 작성할 수 있습니다.
- **이미지 생성 실패**: Python 스크립트 실행이 불가한 환경에서는 이미지 생성 프롬프트만 제공하고 Midjourney, DALL-E, Adobe Firefly 등에서 직접 생성하세요.
- **텍스트 분량 초과**: 카드 1장당 30자 초과 시 핵심 키워드만 남기고 나머지는 이미지 설명이나 캡션으로 이동하세요.

## 공유 에이전트

이 플러그인에서 활용할 수 있는 다른 플러그인의 에이전트:

| 에이전트 | 소속 | 용도 |
|---------|------|------|
| quality-evaluator | moai-core | 산출물 품질 PASS/FAIL 판정 |
| format-converter | moai-office | HWPX/PPTX/DOCX/XLSX 파일 변환 |

## 이 스킬을 사용하지 말아야 할 때

- **SNS 텍스트 포스팅**: 인스타그램 캡션, 링크드인 포스트 등 텍스트 중심 콘텐츠는 `social-media` 스킬이 더 적합합니다.
- **블로그 포스팅**: 장문 텍스트 콘텐츠는 `blog` 스킬을 사용하세요.
- **이메일 뉴스레터**: 구독자 대상 뉴스레터는 `newsletter` 스킬을 사용하세요.
- **유튜브·영상 기획**: 영상 스크립트와 채널 전략은 `media-production` 스킬을 사용하세요.
