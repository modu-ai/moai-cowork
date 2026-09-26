---
name: doc-hwp
description: |
  아래아한글(.hwpx) 문서를 만들어 드립니다 — 한컴오피스에서 열리는 공문서·기안서·품의서·보고서를 작성하고, 기존 HWP 파일을 HWPX로 변환합니다.
  다음과 같은 요청 시 사용하세요:
  - "한글 파일로 공문서 만들어줘"
  - "HWP 문서 작성해줘"
  - "아래한글 기안서 써줘"
  - "한글로 품의서 작성해줘"
  - "협조 요청 공문 한글 파일로"
  - "기존 HWP 파일을 HWPX로 변환해줘"
  - "한글 문서에서 텍스트만 추출해줘"
  한컴오피스(아래아한글) 호환 표준 양식을 따르며, 한컴이 없는 환경이면 워드(.docx) 생성으로 대체할 수 있습니다.
  아래아한글(.hwpx) 문서를 만들 때는 현재 앱의 실제 문서 생성 기능을 확인하고 이 스킬의 검수 절차를 적용하세요.
  [책임 경계] vs moai-officer:doc-docx: 이 스킬=한컴 .hwpx 한글 파일, 저 스킬=MS 워드 .docx 파일.
version: "1.1.2"
---

# 한글 문서 작성자 (HWPX Writer)

## 개요

HWPX 문서의 작성·편집을 돕습니다. HWPX는 OWPML XML을 담은 ZIP 형식이지만, ZIP 안에 XML 조각 몇 개만 넣는 것으로 한컴에서 열리는 문서가 되지는 않습니다. 문서를 실제로 저장할 수 있는 호스트 기능이나 현재 설치된 HWPX 도구를 확인한 뒤 사용합니다. 기존 바이너리 `.hwp` 파일의 변환은 별도 변환 기능이 있어야 합니다.

## 트리거 키워드

한글, hwpx, 아래한글, 한컴, 공문서, 기안서, HWP 변환, 한글 문서 생성, HWPX 편집

## 워크플로우

### 1단계: 작업과 입력 확인

- 새 HWPX, 기존 HWPX 수정, HWP→HWPX 변환, 텍스트 추출 중 작업 유형을 정합니다.
- 원본 파일·사용자 서식·출력 경로를 확인하고 원본은 보존합니다.
- 공문·기안문·품의서에는 실제 제출처 양식과 `references/kr-official-forms.md`를 대조합니다. 기관별 서식이 있으면 그 서식을 우선합니다.

### 2단계: 현재 호스트의 생성 경로 확인

1. 이 플러그인의 `kordoc` MCP가 연결돼 있으면 새 문서는 `generate_document`, 기존 양식 채우기는 `fill_form`, 원본 수정은 `patch_document`의 실제 도구 설명을 확인하고 사용합니다. 생성 결과는 `parse_document`로 읽고 `render_document`로 화면 배치를 점검합니다. 렌더링은 한컴오피스의 실제 열림 검증을 대신하지 않습니다.
2. MCP가 없으면 호스트가 HWPX 생성·편집·내보내기를 실제로 제공하는지 확인합니다.
3. 실행 환경에 `python-hwpx`가 이미 있으면 현재 버전의 공식 API를 확인한 뒤 사용합니다. 이 스킬이 사용자의 앱에 라이브러리 설치를 요구하지 않습니다.
4. 경로가 모두 없으면 유효한 HWPX 파일을 만들었다고 주장하지 않습니다. DOCX 대안은 사용자가 형식 변경을 선택한 경우에만 제공합니다.

바이너리 HWP를 HWPX로 바꾸는 작업은 현재 호스트의 변환 기능 또는 한컴의 변환 도구가 실제로 있을 때만 진행합니다. `python-hwpx`의 HWPX 읽기 기능을 HWP 변환 기능으로 간주하거나 확장자만 바꾸지 않습니다.

### 3단계: 파일 작성

`kordoc` MCP가 없는 상태에서 `python-hwpx`가 이미 설치된 경우, 공식 README의 새 문서 예시는 다음과 같습니다. 표·각주·기존 양식 편집은 현재 설치 버전의 API를 확인합니다.

```python
from hwpx import HwpxDocument

doc = HwpxDocument.new()
doc.add_heading("문서 제목", level=1)
doc.add_paragraph("본문")
doc.save_to_path("output.hwpx")
```

직접 ZIP을 조립할 때는 `mimetype` 외에도 매니페스트(`Contents/content.hpf`), 헤더(`Contents/header.xml`), 본문과 서식 참조 등 OWPML 패키지 전체가 필요합니다. 이 스킬은 완전한 생성기를 포함하지 않으므로 부분 ZIP 예시로 `.hwpx`를 만들지 않습니다.

### 4단계: 출력 검증

- 파일이 생겼는지 확인하고, ZIP 무결성·필수 항목·XML 파싱을 검사합니다.
- 사용한 라이브러리나 호스트 기능으로 다시 열어 제목·본문·표·플레이스홀더를 원본과 대조합니다.
- 가능하면 한컴오피스에서 열림·페이지·서체·표 배치를 확인합니다. 앱을 사용할 수 없으면 그 검증은 `미실행`이라고 보고합니다. ZIP 검사나 XML 파싱만으로 한컴 호환성을 PASS 처리하지 않습니다.
- 변환 작업에서는 원본과 결과의 텍스트·표 개수·주요 서식을 비교합니다.

## 사용 예시

- "공문서 양식으로 협조 요청 한글 파일을 만들어줘"
- "기존 HWP 파일을 HWPX로 변환해줘"
- "아래한글 기안서 형식으로 품의서를 작성해줘"
- "HWPX 파일에서 텍스트를 추출해줘"
- "한글 문서 내용이 올바른 OWPML 구조인지 검증해줘"

## 출력 형식과 한계

- 생성 경로가 확인되고 검증된 경우에만 `.hwpx`를 제공합니다.
- HWPX는 OWPML 기반 ZIP 문서입니다. [한컴의 형식 설명](https://tech.hancom.com/hwpxformat/)과 [공개 문서 형식 안내](https://license.hancom.com/support/downloadCenter/hwpOwpml)를 참고합니다.
- 한컴오피스 버전별 실제 열림·레이아웃은 테스트한 버전에 대해서만 보고합니다.
- 사용자 환경에 한컴오피스가 없어도 `python-hwpx`가 있는 실행 환경에서는 HWPX 생성이 가능하지만, 화면 배치 검증은 별개입니다.
- 사용한 서체가 수신자의 OS에 없을 수 있으므로 전달 전에 폰트·인쇄 결과를 확인합니다.

## 관련 스킬 / 자체 검수

한글 문서를 생성했다면 산출된 `.hwpx` 파일을 사용한 도구로 다시 열어 플레이스홀더 잔존·OWPML 구조·한글 인코딩 깨짐·표 깨짐을 검수합니다. 발견한 문제를 수정하고 다시 검사합니다. 한컴오피스의 실제 열림이나 화면 배치를 확인하지 못했다면 그 항목은 `미실행`으로 보고합니다.

- `moai-officer:doc-docx` - DOCX(Word) 문서 생성
- `moai-officer:doc-pptx` - 발표용 PPT 슬라이드 생성
- `moai-officer:doc-xlsx` - 엑셀 데이터 시트 생성

## 기술 참조

- **python-hwpx GitHub**: https://github.com/airmang/python-hwpx
- **kordoc 생성·파싱·렌더 MCP**: https://github.com/chrisryugj/kordoc
- **OWPML 스펙**: 한글과컴퓨터 OWPML 1.5 명세서
- **한컴오피스 API**: HwpObject 프로그래밍 가이드


## 한국어 문구 검수

배포 전 원본 자료와 대조해 이름·숫자·날짜·권리·의무·결재 문구를 확인합니다. 아래 스킬이 설치돼 있으면 문장 검수에 추가로 사용할 수 있습니다:

1. `moai-coworker:ai-slop-reviewer` — 1차 일반 AI 슬롭 검수 (금지어, 구조 패턴, 리듬)
2. `moai-writer:korean-humanize` — 2차 한국어 정밀 윤문 (40+ 패턴 SSOT, 의미 불변)

스킬 검수 결과만으로 공문서의 의미나 제출처 서식이 맞는다고 단정하지 않습니다. 두 스킬이 없더라도 직접 대조와 문서 검수는 수행합니다.
> **정형 서식 보호** — 이 스킬의 산출물은 정형 문서다. 슬롭 검수는 금지어 치환만 수행하고, 구조(개조식·항목 번호 체계·두문/본문/결문)는 재작성하지 않는다.


## 상세 레퍼런스

| 파일 | 로드 조건 |
|------|-----------|
| references/kr-official-forms.md | 공문·기안문·품의서 등 정형 문서 작성 시 참고. 현재 법령과 제출처 양식을 우선 확인 |
| references/guide.md | HWPX 생성 전반의 상세 가이드가 필요할 때 (라이브러리 활용·문서 조립 절차) |
| references/owpml-spec.md | HWPX 편집 시 OWPML XML 네임스페이스·섹션 파일 구조 등 스펙 참조가 필요할 때 |
| references/format-converter.md | 문서 형식 간 변환 경로와 검증 조건을 확인할 때 |
| references/templates/base.md | HWPX 문서의 공통 서식 확인 항목이 필요할 때 |
| references/templates/gonmun.md | 공문서(시행문) 생성 시 참고. 제출처 양식·현행 별지 서식 확인 |
| references/templates/report.md | 보고서 HWPX 생성 시 |
| references/templates/minutes.md | 회의록 HWPX 생성 시 |
| references/templates/proposal.md | 제안서 HWPX 생성 시 |
