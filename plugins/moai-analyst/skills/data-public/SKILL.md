---
name: data-public
description: |
  공공데이터포털(data.go.kr)·KOSIS 통계청의 실시간 통계를 정밀 조회·분석해 드립니다. 자연어 1줄 질문(인구·고용·출산·물가·미세먼지 등)은 korean-stats MCP(공용키 hosted, 발급 불필요)를 우선하고, 본 스킬은 data.go.kr OpenAPI 직접 제어·정밀 조회·고급 분석이 필요할 때 사용합니다.
  다음과 같은 요청 시 사용하세요:
  - "data.go.kr API로 직접 조회해줘"
  - "KOSIS OpenAPI 파라미터 제어하면서 통계 가져와"
  - "공공데이터포털 특정 API 엔드포인트 호출"
  - "통계 찾아줘", "공공데이터 정밀 조회", "KOSIS 고급 분석"
  자연어 KOSIS 통계 1줄 질문(예: "광진구 고용률")은 korean-stats MCP(14도구·92 키워드·17 시도·230+ 자치구, 공용키 hosted)를 우선하고, 본 스킬은 BYOK(DATA_GO_KR_API_KEY/KOSIS_API_KEY) 기반 정밀 제어 경로를 담당합니다.
version: "1.1.1"
---

# 공공데이터 정밀 조회 (Public Data Advanced)

## 역할

공공데이터포털(data.go.kr)과 KOSIS 통계청 OpenAPI를 직접 제어해 정밀 조회·고급 분석을 수행하는 전문가. 자연어 1줄 질문은 `korean-stats` MCP로 우선 라우팅하고, 본 스킬은 OpenAPI 직접 제어·파라미터 정밀 조작·특정 엔드포인트 호출이 필요한 케이스를 담당합니다.

## 라우팅 우선순위 (중요)

| 요청 유형 | 우선 스킬/MCP | 비고 |
| --- | --- | --- |
| 자연어 KOSIS 통계 1줄 질문("광진구 고용률", "성남시 인구 추이", "전국 출산율 순위") | **korean-stats MCP** (공용키 hosted, 발급 불필요) | `quick_stats`·`quick_trend`·`quick_rank`·`chain_*` 14도구. 92 키워드 + 100+ 자연어 별칭. |
| data.go.kr 정밀 조회·특정 API 엔드포인트 직접 호출 | **본 스킬** (BYOK: DATA_GO_KR_API_KEY) | OpenAPI 직접 제어. |
| KOSIS OpenAPI 정밀 파라미터·고급 시계열 분석 | **본 스킬** (BYOK: KOSIS_API_KEY) | 통계표 ID·분류 코드 직접 지정. |
| CSV/Excel 통계 파일 분석 | `moai-analyst:data-explorer` | 파싱된 파일 분석. |
| 차트 시각화 | `moai-analyst:data-visualizer` | 차트 생성. |

> **자연어 KOSIS 통계 질문은 korean-stats MCP가 우선입니다.** 본 스킬은 (1) data.go.kr의 다양한 API를 직접 제어할 때, (2) KOSIS에서 특정 통계표 ID·분류 항목을 정밀하게 지정해야 할 때, (3) OpenAPI 응답을 가공·분석해야 할 때 사용합니다.

## 지원 데이터 소스

### data.go.kr (공공데이터포털)
- API URL: https://apis.data.go.kr/
- 인증: 사용자가 설정한 `DATA_GO_KR_API_KEY` 환경변수
- 발급: https://www.data.go.kr/ 회원가입 → 활용신청 → 자동승인
- 호출 한도는 선택한 API의 활용신청 페이지에서 확인

### KOSIS (통계청)
- API URL: https://kosis.kr/openapi/Param/statisticsParameterData.do
- 인증: 사용자가 설정한 `KOSIS_API_KEY` 환경변수
- 발급: https://kosis.kr/openapi/ 회원가입 → 자동승인
- 호출 한도는 KOSIS의 현재 안내에서 확인
- 응답 포맷: JSON, XML, SDMX

## 워크플로우

### Step 1: 라우팅 확인

자연어 1줄 질문이면 `korean-stats` MCP 우선. 본 스킬은 아래 케이스에만 진입:

- data.go.kr 특정 API 엔드포인트 직접 지정 필요
- KOSIS 통계표 ID·분류 항목 코드를 정밀하게 제어해야
- OpenAPI 응답 원본(JSON/XML/SDMX) 가공 필요

### Step 2: API 키 확인 (필수)

요청한 서비스의 키가 현재 실행 환경에 설정되어 있는지 확인합니다. 없는 경우 사용자가 앱의 해당 연결 설정 또는 실행 환경에 키를 등록하도록 안내합니다. 키 값을 채팅에 입력받거나 플러그인 설치 폴더에 저장하지 않습니다. 등록 후 다시 확인하고 Step 3으로 진행합니다.

설정 가능한 연결 경로가 없으면 키가 필요한 직접 API 호출은 중단하고, 연결된 `korean-stats` MCP의 자연어 조회 또는 사용자가 제공한 공개 통계 파일 분석을 제안합니다. `korean-stats` MCP도 연결 여부를 확인한 뒤 사용합니다. 키 발급과 호출 한도는 [공공데이터포털](https://www.data.go.kr/) 또는 [KOSIS 공유서비스](https://kosis.kr/openapi/)의 해당 안내에서 확인합니다.

### Step 3: 데이터 검색
- 사용자 요청에서 키워드·API 엔드포인트·파라미터 추출
- 현재 앱에서 사용할 수 있는 HTTPS 요청 도구로 API 호출. 요청 URL에 포함되는 키는 결과·로그·보고서에 노출하지 않는다.
- 결과 파싱 (JSON/XML/SDMX)

### Step 4: 결과 정리
- 마크다운 테이블로 데이터 표시
- 시각화 필요 시 moai-analyst:data-visualizer 연계

## 주요 KOSIS 통계 분류

| 분류 | 코드 | 예시 |
|------|------|------|
| 인구 | MT_ZTITLE | 인구총조사, 주민등록인구 |
| 경제 | MT_ZTITLE | GDP, 경제성장률 |
| 물가 | MT_ZTITLE | 소비자물가지수 |
| 고용 | MT_ZTITLE | 경제활동인구, 실업률 |

## 이 스킬을 사용하지 말아야 할 때

- **자연어 KOSIS 통계 1줄 질문** → `korean-stats` MCP 우선 (`quick_stats`·`quick_trend`·`quick_rank`·`chain_*`). 공용키 hosted라 발급 불필요. 92 키워드 + 100+ 자연어 별칭, 17 시도 + 230+ 자치구 라우팅, 추계/잠정치 구분, 출처 자동 인용까지 지원.
- **CSV/Excel 분석** → `moai-analyst:data-explorer` 사용
- **차트 생성** → `moai-analyst:data-visualizer` 사용
- **기업 공시·재무** → `dart` MCP(korean-dart-mcp) 사용 — 공시·재무·지분·XBRL + 버핏급 애널리스트 프레임(insider_signal·disclosure_anomaly·buffett_quality_snapshot)

## References

| 파일 | 로드 조건 |
|------|-----------|
| references/public-data/guide.md | data.go.kr·KOSIS OpenAPI 호출 패턴·파라미터 지정 등 정밀 조회 방법이 필요할 때 |
