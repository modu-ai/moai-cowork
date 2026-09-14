---
name: legal-patent-search
description: |
  KIPRIS Plus로 한국 특허·실용신안·상표를 검색해 출원 현황과 서지정보를 정리해 드립니다. 이 플러그인의 moai-mcp-ip 서버로 조회하며, API 키가 없으면 등록 방법부터 안내합니다.
  다음과 같은 요청 시 사용하세요:
  - "딥러닝 이미지 분류 관련 특허 검색해줘"
  - "삼성전자 반도체 등록특허 찾아줘"
  - "최근 5년간 배터리 기술 출원 현황 조사해줘"
  - "자율주행 LiDAR 선행기술 조사해줘"
  - "이 키워드로 특허 출원 추이 알려줘"
  - "KIPRIS에서 상표 검색해줘"
  - "이 분야 출원인별 경쟁 현황 정리해줘"
  특허 목록·핵심 청구항 요약·IPC 분류별 분포를 정리하고, 선행기술 조사·FTO·출원서가 필요하면 moai-lawyer:legal-patent-analyzer로, 해외(미국·일본·유럽) 조사나 상표 등록 가능성 보고서는 moai-lawyer:legal-ip-search-report로 이어집니다.
version: "1.2.0"
---

# 특허 검색 (Patent Search)

## 개요

KIPRIS Plus(한국특허정보원) 공식 API를 `moai-mcp-ip` MCP 서버로 호출해 특허·실용신안·상표를 검색하고 서지정보를 체계적으로 정리하는 전문 스킬입니다. 디자인권은 이 서버가 다루지 않으므로 KIPRIS 웹 화면으로 확인합니다. 선행기술 조사, 출원 현황 파악, 기술 동향 분석을 지원합니다.

## 트리거 키워드

- 특허 검색, 특허 찾아줘, 특허 조사
- KIPRIS 검색, 한국 특허
- 선행기술 조사, prior art search
- 특허 출원 현황, 등록 특허
- 실용신안, 상표 검색

## 워크플로우

### 1단계: API 접근 확인 (필수)

검색 전에 `ip_check_access(sources=["kipris-plus"])`를 부릅니다. 이 도구는 키 값이 아니라 `configured` / `missing`만 돌려줍니다.

- **missing**: 검색하지 않고 등록 방법을 안내합니다.
  1. [KIPRIS Plus](https://plus.kipris.or.kr/portal/main/contents.do?menuNo=210104)에서 회원 가입
  2. Open API에서 **특허 상품과 상표 상품을 각각** 이용 신청 (월 1,000회 무료, 이후 유료)
  3. 마이페이지 → APIKEY 관리에서 인증키 확인
  4. 키는 **채팅에 붙여 넣지 않고** Claude 앱은 플러그인 설정 화면의 `KIPRIS_API_KEY` 칸에, Codex 앱은 자격증명 파일(macOS `~/.moai/mcp/ip.json`, Windows `C:\Users\<사용자>\.moai\mcp\ip.json`)에 넣도록 안내
- 사용자가 "설정 완료"라고 하면 `ip_check_access(sources=["kipris-plus"], verify=true)`로 연결만 확인합니다. `patent_product`가 `auth_error`면 특허 상품의 이용 기간이 끝났거나 신청되지 않은 것이며, 검색 결과 0건과 다릅니다.
- 사용자가 키를 채팅에 붙여 넣었다면 그 값을 파일·보고서에 옮기지 않고, 설정 화면이나 자격증명 파일로 옮기도록 안내합니다.

### 2단계: 검색 전략 수립

- 핵심 키워드 추출 (한국어 + 영어 동시 검색)
- IPC 분류코드 매핑 (국제특허분류)
- 검색 범위 결정 (국내/해외, 연도, 상태: 출원/등록/공개)
- 출원인/발명자 필터

### 3단계: KIPRIS 검색 (MCP 도구)

| 하려는 일 | 도구 호출 예 |
|---|---|
| 넓은 키워드 검색 | `kipris_patent_search(word="딥러닝 이미지 분류", num_of_rows=50)` |
| 청구항·IPC 결합 | `kipris_patent_search(claim="합성곱 신경망", ipc_number="G06N")` |
| 출원인 등록특허 | `kipris_patent_search(applicant="삼성전자", status="R")` |
| 기간 지정 | `extra_params={"applicationDate": "20210101~20251231"}` |
| 서지 상세 | `kipris_patent_detail(application_number="1020200012345")` |
| 상표 검색 | `kipris_trademark_search(trademark_name="...", classification="35")` |

- `status`: 빈 값=전체, `A`=공개, `R`=등록, `J`=거절, `F`=소멸, `G`=포기, `C`=취하, `I`=무효
- `sort_spec`: `PD`·`AD`·`GD`·`OPD`·`FD`·`FOD`·`RD`
- 한 번에 최대 500건입니다. 응답의 `total_count`(전체 건수)와 `returned_count`(받은 건수)를 함께 보고, 모자라면 `page_no`로 이어 받습니다.
- 도구가 `setup_required`·`auth_error`·`rate_limited`를 돌려주면 검색 결과가 아니라 접근 문제입니다. 0건으로 보고하지 않습니다.

### 4단계: 검색 결과 정리

- 특허 목록 (출원번호, 제목, 출원인, 발명자, 출원일, 등록일, 상태)
- 핵심 청구항 요약 (독립항 중심)
- IPC/CPC 분류별 기술 분포
- 출원인별 경쟁 현황 (상위 10개)
- 연도별 출원 추이

### 5단계: 후속 작업 제안

- "선행기술 조사" → moai-lawyer:legal-patent-analyzer 스킬 연계
- "특허 맵 분석" → moai-lawyer:legal-patent-analyzer 스킬 연계
- "출원서 작성" → moai-lawyer:legal-patent-analyzer 스킬 연계
- "FTO 분석" → moai-lawyer:legal-patent-analyzer 스킬 연계

## 사용 예시

```
"딥러닝 기반 이미지 분류 관련 특허를 검색해줘."
"삼성전자의 반도체 관련 등록특허를 찾아줘."
"최근 5년간 배터리 기술 출원 현황을 조사해줘."
"자율주행 선행기술을 조사해줘. LiDAR 관련 특허야."
```

## 출력 형식

- 특허 목록 테이블 (출원번호, 제목, 출원인, 출원일, 상태)
- 핵심 특허 요약 (청구항 기반)
- IPC 분류별 기술 분포
- 출원인별 경쟁 현황
- 연도별 출원 추이 (데이터)

## 주의사항

- KIPRIS Plus API 키가 없으면 검색하지 않고 등록 방법을 먼저 안내합니다. 키는 KIPRIS Plus에서 상품별로 이용 신청해 받습니다(data.go.kr 목록은 KIPRIS Plus로 연결만 합니다).
- 월 1,000회까지 무료이고 초과 시 유료입니다.
- 해외 특허·상표 조사나 등록 가능성 보고서는 moai-lawyer:legal-ip-search-report로 연계합니다.
- 일부 특허는 전문 텍스트를 확인하지 못할 수 있습니다. 이 경우 서지정보와 청구항 요약만 제공됩니다.
- 선행기술 조사, FTO 분석, 출원서 작성이 필요한 경우 moai-lawyer:legal-patent-analyzer 스킬로 연계합니다.

## 관련 스킬

- **moai-lawyer:legal-patent-analyzer** - 선행기술 조사, FTO 분석, 출원서 작성
- **moai-lawyer:legal-ip-search-report** - 한국·미국·일본·유럽 특허·상표 선행조사 보고서
- **moai-tutor:education-grant-writer** - 연구비 신청서 선행기술 섹션 작성
- **moai-analyst:data-visualizer** - 특허 동향 시각화 (연도별 추이, IPC 분포 차트)

## KIPRIS Plus API 안내

**발급처**
- [KIPRIS Plus](https://plus.kipris.or.kr/) — 회원 가입 후 데이터 상품별 이용 신청, 마이페이지에서 인증키 확인

**API 스펙 (2026-09-13 확인)**
- 비용: 월 1,000회 무료, 이후 유료
- 인증: 쿼리 파라미터 `ServiceKey` (moai-mcp-ip가 처리하며 로그·응답에 남기지 않음)
- 응답 형식: XML (오류도 HTTP 200 + `successYN=N`으로 옴 — 서버가 판정)
- 등록 절차 상세: 플러그인 안 `mcp-servers/moai-mcp-ip/CONNECTORS.md`

**IPC 분류코드**
- A부: 생활필수품 (농업, 식품, 의약)
- B부: 처리조작, 운수 (분리, 혼합, 운수)
- C부: 화학, 야금
- D부: 섬유, 종이
- E부: 고정구조물 (건축, 광산)
- F부: 기계공학, 조명, 가열
- G부: 물리학 (전기, 통신, 컴퓨터)
- H부: 전기

## References

| 파일 | 로드 조건 |
|------|-----------|
| references/patent-search/guide.md | 검색식 설계 요령(키워드·IPC 조합)과 MCP 도구 파라미터가 필요할 때 |
