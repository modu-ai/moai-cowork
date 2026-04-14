---
name: patent-search
description: >
  특허를 검색하고 분석합니다.
  '특허 찾아줘', 'KIPRIS 검색', '선행기술 조사', '특허 출원 현황'이라고 요청할 때 사용하세요.
  KIPRIS Plus API로 특허/실용신안/디자인/상표를 검색하고 서지정보를 정리합니다.
user-invocable: true
metadata:
  version: "1.1.1"
  category: "domain"
  status: "active"
  updated: "2026-04-10"
  tags: "특허, KIPRIS, 검색, IPC, 선행기술, 실용신안, 상표"
---

# 특허 검색 (Patent Search)

> MoAI-Cowork v1.0.0 하네스 참고자료

## 역할
KIPRIS Plus API를 활용하여 특허/실용신안/디자인/상표를 검색하고 서지정보를 체계적으로 정리하는 전문가.

## KIPRIS Plus API

- Base URL: http://plus.kipris.or.kr/openapi/rest/
- 인증: KIPRIS_API_KEY (ServiceKey 파라미터)
- 발급: https://plus.kipris.or.kr/ 또는 data.go.kr 경유 (무료, 1,000회/월)
- 개발가이드: https://plus.kipris.or.kr/portal/bbs/view.do?nttId=1060&bbsId=B0000001

## 워크플로우

### Step 0: API 키 확인 (필수)

KIPRIS Plus API 키가 없으면 검색을 진행하지 않는다.

```
IF KIPRIS_API_KEY 미설정:
  "특허 검색을 위해 KIPRIS Plus API 키가 필요합니다.

   발급 방법:
   1. https://plus.kipris.or.kr/ 접속 → 회원가입
   2. 마이페이지 → 인증키 발급
   3. 또는 https://www.data.go.kr/data/15065437/openapi.do 에서 활용신청 (무료)

   API 키를 입력해 주세요:"

  → 사용자가 키 입력
  → ${CLAUDE_PLUGIN_DATA}/moai-credentials.env에 KIPRIS_API_KEY 저장
  → Step 1로 진행
```

### Step 1: 검색 전략 수립
- 핵심 키워드 추출 (한국어 + 영어)
- IPC 분류코드 매핑
- 검색 범위 (국내/해외, 연도, 상태)

### Step 2: KIPRIS API 검색
- API 키 확인 → WebFetch로 REST API 호출
- 결과 파싱 (XML)

### Step 3: 결과 정리
- 특허 목록 (출원번호, 제목, 출원인, 등록일, 상태)
- 핵심 청구항 요약
- 기술 분류별 분포

### Step 4: 후속 작업 제안
- "선행기술 조사" → moai-research:patent-analyzer
- "특허 맵" → moai-research:patent-analyzer
- "출원서 작성" → moai-research:patent-analyzer

## 이 스킬을 사용하지 말아야 할 때
- **특허 분석/FTO** → moai-research:patent-analyzer 사용
- **논문 검색** → moai-research:paper-search 사용
