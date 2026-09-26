# HWPX 문서 작성·편집 가이드

## 먼저 확인할 것

1. 요청 형식이 `.hwpx`인지, 기존 바이너리 `.hwp`를 변환해야 하는지 구분합니다.
2. 원본 문서와 제출처 양식을 읽고, 원본을 수정하지 않는 별도 출력 경로를 정합니다.
3. 이 플러그인의 `kordoc` MCP가 연결됐는지 확인합니다. 현재 버전에는 `generate_document`·`fill_form`·`patch_document`·`parse_document`·`render_document`가 있습니다. 연결되지 않았다면 호스트의 HWPX 출력 또는 이미 설치된 HWPX 라이브러리·변환 기능을 확인합니다.
4. 사용할 경로가 없으면 `.hwpx`가 만들어졌다고 말하지 않습니다. 형식 변경은 사용자 선택을 받습니다.

## HWPX 구조

한컴의 [HWPX 포맷 구조 설명](https://tech.hancom.com/hwpxformat/)에 따르면 HWPX는 OWPML 기반 ZIP입니다. ZIP에는 `mimetype`, `version.xml`, `Contents/content.hpf`(패키지 목록), `Contents/header.xml`(서식), `Contents/section0.xml`(본문) 등의 파일이 들어갑니다. `.docx`의 `word/document.xml` 구조와 다르므로 DOCX XML 예시를 HWPX에 복사하지 않습니다.

기존 바이너리 `.hwp`는 다른 형식입니다. `.hwp`의 확장자만 바꿔 HWPX로 만들 수 없습니다. 변환 기능이 확인된 호스트나 한컴 도구를 사용하고, 결과 파일을 다시 엽니다.

## 현재 설치된 python-hwpx를 사용할 때

이 절은 `kordoc` MCP와 호스트 출력 기능을 사용할 수 없을 때의 대체 경로입니다.

[python-hwpx 공식 README](https://github.com/airmang/python-hwpx)의 새 문서 예시:

```python
from hwpx import HwpxDocument

doc = HwpxDocument.new()
doc.add_heading("문서 제목", level=1)
doc.add_paragraph("본문")
doc.save_to_path("output.hwpx")
```

기존 HWPX는 `HwpxDocument.open("source.hwpx")`으로 읽습니다. 서식 수정, 표, 이미지, 템플릿 채우기는 설치된 버전의 실제 API를 확인한 뒤 사용합니다. 사용자에게 의존성 설치를 필수 절차로 요구하지 않습니다.

## 양식 채우기

- 템플릿에서 실제 필드와 표 구조를 확인합니다. `{{필드명}}`은 예시 표기일 뿐 HWPX의 내장 필드 문법이 아닙니다.
- 이름·금액·날짜 등 입력값은 행마다 검증하고, 결측값이나 중복 필드는 자동으로 채운 척하지 않습니다.
- 계약 조건, 발신 기관, 결재자, 법적 효력 같은 내용은 사용자 또는 원본 근거를 우선합니다.
- 각 문서의 출력 경로를 구분하고 원본과 결과의 텍스트·표·필드를 비교합니다. 일괄 생성 속도는 환경과 문서 복잡도에 따라 달라지므로 고정 성능을 약속하지 않습니다.

## 검증

- 저장한 파일이 실제로 존재하고 ZIP 무결성·필수 XML 파싱을 통과하는지 확인합니다. 이 검사는 패키지 구조의 일부만 확인합니다.
- 사용한 도구로 파일을 다시 열어 제목, 본문, 표, 필드값이 요청과 맞는지 확인합니다.
- 가능하면 대상 한컴오피스에서 열림, 줄바꿈, 폰트, 표 배치, 인쇄 결과를 확인합니다. 실행하지 않은 호환성 검사는 `미실행`으로 보고합니다.
- 다른 OS에 없는 서체가 포함됐다면 폴백 또는 PDF 배포본의 표시를 확인합니다.
- 바이너리 HWP 변환에서는 텍스트만 비교하지 말고 표, 이미지, 머리글과 페이지 수의 손실도 확인합니다.

## 범위

이 문서는 문서 작성 절차를 안내합니다. HWPX 변환기, 일괄 병합기, 한컴 호환성 시험기가 이 스킬에 포함되어 있다는 뜻은 아닙니다. 사용 가능한 기능은 실행 환경에서 확인합니다.
