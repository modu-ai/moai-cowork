# 특허 검색 가이드

## KIPRIS Plus 호출 — MCP 도구로

직접 URL을 조립하지 않고 `moai-mcp-ip` 도구를 씁니다. 서버가 `ServiceKey` 인증, XML 해석, HTTP 200으로 오는 오류 판정을 처리합니다.

| 도구 | 공식 오퍼레이션 (2026-09-13 확인) | 주요 인자 |
|---|---|---|
| `kipris_patent_search` | `patUtiModInfoSearchSevice/getAdvancedSearch` | `word` · `invention_title` · `abstract` · `claim` · `ipc_number` · `applicant` · `inventors` · `status` · `sort_spec` · `page_no` · `num_of_rows`(최대 500) · `extra_params` |
| `kipris_patent_detail` | `patUtiModInfoSearchSevice/getBibliographyDetailInfoSearch` | `application_number` |
| `kipris_trademark_search` | `trademarkInfoSearchService/getAdvancedSearch` | `trademark_name` · `classification` · `similarity_code` · `applicant_name` · `statuses` 등 |
| `kipris_trademark_detail` | `trademarkInfoSearchService/getBibliographyDetailInfoSearch` | `application_number` |

`getWordSearch`는 공식 명세에 "폐기 예정"으로 표시되어 있어 쓰지 않습니다.

## IPC 주요 분류코드

| 코드 | 분야 |
|------|------|
| A | 생활필수품 |
| B | 처리조작, 운수 |
| C | 화학, 야금 |
| G | 물리학 |
| H | 전기 |

## 검색 팁
- 키워드 + IPC 조합으로 정확도 향상
- 출원인 검색: 경쟁사 특허 포트폴리오 파악
- 등록번호 검색: 정확한 특허 1건 조회
