# moai-data

데이터 분석 플러그인 — CSV/Excel 탐색, 공공데이터 조회, 시각화, 대시보드.

3개 스킬로 데이터 수집부터 분석, 시각화까지 전 과정을 지원합니다. Mermaid, Chart.js 기반 차트 생성 후 moai-office로 PPT/Word 변환이 가능합니다.

## 스킬

| 스킬 | 설명 | 레퍼런스 | 상태 |
|------|------|:--------:|:----:|
| [data-explorer](./skills/data-explorer/) | CSV/Excel 프로파일링, 이상값 탐지, 상관 분석 | 1 | ✅ |
| [data-visualizer](./skills/data-visualizer/) | Mermaid/Chart.js 차트, HTML 대시보드, PPT/Word 변환 | 1 | ✅ |
| [public-data](./skills/public-data/) | 공공데이터포털, KOSIS 통계 실시간 조회 | 1 | ✅ |

## 커넥터

| 커넥터 | 활용 |
|--------|------|
| Airtable | 구조화된 데이터 조회/분석 |
| Google Sheets | 스프레드시트 분석, 결과 출력 |
| Google Drive | CSV/Excel 파일 저장/공유 |
| Notion | 분석 결과 보고서 발행 |

## API 키 (선택)

| 서비스 | 환경변수 | 발급처 |
|--------|---------|--------|
| 공공데이터포털 | DATA_GO_KR_API_KEY | [data.go.kr](https://www.data.go.kr/) |
| KOSIS 통계 | KOSIS_API_KEY | [kosis.kr/openapi](https://kosis.kr/openapi/) |

## 설치

Settings > Plugins > moai-cowork-plugins에서 `moai-data` 선택

## 참고자료

| 항목 | URL | 용도 |
|------|-----|------|
| [공공데이터포털](https://www.data.go.kr/) | 공식 API | 공공데이터 조회 |
| [KOSIS OpenAPI](https://kosis.kr/openapi/) | 공식 API | 통계청 데이터 |
| [data-go-mcp-servers](https://github.com/Koomook/data-go-mcp-servers) | 오픈소스 | 공공데이터 MCP |
| [KOSIS 개발가이드](https://kosis.kr/openapi/file/openApi_manual_v1.0.pdf) | 공식 문서 | API 사용법 |
