---
name: public-data
description: >
  공공데이터포털과 KOSIS 통계청 데이터를 조회합니다.
  '통계 찾아줘', '공공데이터 조회해줘', '인구 통계', 'KOSIS 검색'이라고 요청할 때 사용하세요.
  data.go.kr API와 KOSIS OpenAPI로 실시간 데이터를 조회하고 분석합니다.
user-invocable: true
metadata:
  version: "1.0.0"
  category: "domain"
  status: "active"
  updated: "2026-04-10"
  tags: "공공데이터, 통계, KOSIS, data.go.kr, 인구, 물가, 경제"
---

# 공공데이터 조회 (Public Data)

> MoAI-Cowork v1.0.0 하네스 참고자료

## 역할
공공데이터포털(data.go.kr)과 KOSIS 통계청의 데이터를 실시간으로 조회하고 분석하는 전문가.

## 지원 데이터 소스

### data.go.kr (공공데이터포털)
- API URL: https://apis.data.go.kr/
- 인증: DATA_GO_KR_API_KEY 환경변수
- 발급: https://www.data.go.kr/ 회원가입 → 활용신청 → 자동승인
- 일일 제한: 1,000회 (개발계정)

### KOSIS (통계청)
- API URL: https://kosis.kr/openapi/Param/statisticsParameterData.do
- 인증: KOSIS_API_KEY 환경변수
- 발급: https://kosis.kr/openapi/ 회원가입 → 자동승인
- 일일 제한: 1,000회
- 응답 포맷: JSON, XML, SDMX

## 워크플로우

### Step 1: API 키 확인
- ${CLAUDE_PLUGIN_DATA}/moai-credentials.env에서 키 로드
- 키 없으면 발급 방법 안내

### Step 2: 데이터 검색
- 사용자 요청에서 키워드 추출
- WebFetch로 API 호출
- 결과 파싱 (JSON/XML)

### Step 3: 결과 정리
- 마크다운 테이블로 데이터 표시
- 시각화 필요 시 moai-data:data-visualizer 연계

## 주요 KOSIS 통계 분류

| 분류 | 코드 | 예시 |
|------|------|------|
| 인구 | MT_ZTITLE | 인구총조사, 주민등록인구 |
| 경제 | MT_ZTITLE | GDP, 경제성장률 |
| 물가 | MT_ZTITLE | 소비자물가지수 |
| 고용 | MT_ZTITLE | 경제활동인구, 실업률 |

## API 키 없이 사용 가능한 기능
- KOSIS 통계 목록 조회 (키 불필요)
- 웹 검색으로 최신 통계 수치 확인

## 이 스킬을 사용하지 말아야 할 때
- **CSV/Excel 분석** → moai-data:data-explorer 사용
- **차트 생성** → moai-data:data-visualizer 사용
- **기업 공시** → moai-business 플러그인의 DART 연동 사용
