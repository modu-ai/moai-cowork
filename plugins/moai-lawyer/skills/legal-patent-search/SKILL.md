---
name: legal-patent-search
description: KIPRIS Plus MCP가 연결되면 한국 특허·실용신안·상표를 조회하고, 연결되지 않으면 공식 KIPRIS 검색 화면에서 확인 가능한 범위의 결과를 정리합니다. 선행기술·특허 동향 요청에도 사용합니다.
version: "1.2.1"
---

# 한국 특허 검색

## 검색 경로

1. 현재 앱에 moai-mcp-ip 도구가 실제로 보이면 스키마를 확인한다. ip_check_access가 제공되면 kipris-plus의 설정·인증 상태를 확인한다. 키 값은 채팅이나 보고서에 적지 않는다.
2. 도구가 없거나 인증되지 않았으면 [KIPRIS 공식 검색](https://www.kipris.or.kr/) 화면으로 조사한다. 사용자의 앱에 공식 화면 접근이 없으면 사용자가 결과 링크나 파일을 제공하도록 요청한다. API 등록을 검색의 필수 조건으로 만들지 않는다.
3. 요청한 권리 유형(특허·실용신안·상표·디자인), 키워드, 출원인, 기간, 공개·등록 상태를 정한다. 한글·영문 동의어와 IPC 분류는 실제 관련성이 있을 때만 추가한다.

## 도구 사용 시

kipris_patent_search, kipris_patent_detail, kipris_trademark_search 등은 현재 연결된 스키마가 허용하는 경우에만 사용한다. setup_required, auth_error, rate_limited는 검색 결과가 아니다. 페이지가 나뉘면 전체 건수와 실제 조회 건수를 구분한다. API가 제공하지 않는 디자인권이나 원문은 KIPRIS 웹 화면에서 별도로 확인한다.

## 보고

- 검색 경로, 검색식, 검색일, 권리 유형·국가·기간, 실제 열람 건수와 누락 범위를 기록한다.
- 문헌별 번호·제목·출원인·출원일·공개 또는 등록 상태를 출처 링크와 함께 적는다. 청구항 원문을 열람하지 않았다면 청구항 분석이라고 부르지 않는다.
- 출원인별 건수·연도별 추이는 조회 범위 전체가 확보된 경우에만 집계한다. 검색 결과 0건은 해당 검색식과 DB 범위에서의 결과로만 표현한다.
- 선행기술 비교나 실시 자유 검토 자료는 legal-patent-analyzer, 해외 조사와 패밀리 확인은 legal-ip-search-report로 이어간다.

## References

- [검색 기록 및 도구 가이드](references/patent-search/guide.md)
