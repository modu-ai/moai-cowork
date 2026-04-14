---
name: paper-search
description: >
  학술 논문을 통합 검색합니다.
  '논문 찾아줘', '선행연구 조사', 'RISS 검색', 'KCI 논문', '문헌 검토'라고 요청할 때 사용하세요.
  RISS, KCI, DBpia, Google Scholar에서 논문을 검색하고 인용 정보를 정리합니다.
user-invocable: true
metadata:
  version: "1.2.0"
  category: "domain"
  status: "active"
  updated: "2026-04-10"
  tags: "논문, 검색, RISS, KCI, DBpia, Google Scholar, 학술, 문헌검토"
---

# 논문 검색 (Paper Search)

> MoAI-Cowork v1.0.0 하네스 참고자료

## 역할
RISS, KCI, DBpia, Google Scholar 등에서 학술 논문을 통합 검색하고 결과를 체계적으로 정리하는 전문가.

## 지원 검색 소스

| 소스 | URL | 특징 | API |
|------|-----|------|-----|
| RISS | riss.kr | 학위논문, 해외 DB 연계 | 웹검색 |
| KCI | kci.go.kr | 인용색인, 학술지 평가 | REST API (KCI_API_KEY) |
| DBpia | dbpia.co.kr | 전 분야 학술지 | 웹검색 |
| Google Scholar | scholar.google.com | 글로벌 학술 검색 | 웹검색 |

## 워크플로우

### Step 0: API 키 확인 (필수)

KCI 논문 검색 API 키가 없으면 API 기반 검색을 진행하지 않는다.
(RISS, DBpia, Google Scholar는 웹검색으로 키 없이 사용 가능)

```
IF KCI_API_KEY 미설정:
  "KCI 논문 검색을 위해 API 키가 필요합니다.

   발급 방법 (간편):
   1. https://www.data.go.kr/data/3049042/openapi.do 접속
   2. 활용신청 → 자동승인 → 키 발급

   API 키를 입력해 주세요 (또는 '건너뛰기'로 웹검색만 사용):"

  → '건너뛰기' 시: RISS/DBpia/Google Scholar 웹검색으로 진행
  → 키 입력 시: ${CLAUDE_PLUGIN_DATA}/moai-credentials.env에 KCI_API_KEY 저장
```

### Step 1: 검색 전략 수립
- 핵심 키워드 추출 (한국어 + 영어)
- 검색 범위 결정 (국내/해외, 연도)
- 분야 필터 (KCI 분류코드)

### Step 2: 통합 검색
- KCI API (키 있을 때): WebFetch로 REST API 호출
- RISS/DBpia/Google Scholar: WebSearch로 검색

### Step 3: 결과 정리
- 논문 목록 (제목, 저자, 학술지, 연도, 인용수)
- 핵심 논문 3-5편 초록 요약
- 연구 동향 분석

### Step 4: 후속 작업 제안
- "논문 작성" → moai-research:paper-writer
- "참고문헌 정리" → APA/KCI 포맷 자동 생성

## KCI API 호출 (키 있을 때)

```
GET https://open.kci.go.kr/po/openapi/openApiSearch.kci
  ?apiCode=articleSearch
  &key={KCI_API_KEY}
  &title={검색어}
```

발급: https://www.data.go.kr/data/3049042/openapi.do (data.go.kr 경유 권장)

## 이 스킬을 사용하지 말아야 할 때
- **논문 작성** → moai-research:paper-writer 사용
- **특허 검색** → moai-research:patent-search 사용
- **강의 자료용 리서치** → moai-education:research-assistant 사용
