---
name: doc-pdf
description: |
  HTML·Markdown·JSON·일반 텍스트를 PDF로 만들거나 기존 문서를 PDF로 변환할 때 사용합니다.
  현재 호스트의 PDF 출력 기능을 확인하고, 결과 파일의 내용·글꼴·페이지 배치를 검수합니다.
  요청 예: "PDF로 만들어줘", "HTML 보고서를 PDF로", "한글 PDF 출력", "Markdown을 PDF로".
version: "1.1.2"
---

# PDF 생성 (doc-pdf)

## 범위

입력 형식과 원하는 결과를 먼저 확인한다. HTML의 화면 디자인, 종이 인쇄 레이아웃, 편집 가능한 원본은 서로 다르다. PDF가 필요하면 실제 출력 기능을 사용하고 생성된 파일을 다시 검사한다.

## 경로 선택

1. 호스트에 문서·브라우저의 PDF 내보내기 기능이 있으면 입력 형식과 지원 범위를 확인하고 사용한다.
2. HTML 출력이고 실행 환경에 WeasyPrint가 이미 있으면 [공식 사용법](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)에 따라 렌더할 수 있다. CSS 지원과 결과는 브라우저 화면과 다를 수 있으므로 비교한다.
3. 위 경로가 없으면 PDF 생성 완료를 주장하지 않는다. HTML 또는 원본 문서 대안은 사용자가 형식 변경을 선택한 경우에만 제공한다.

WeasyPrint를 사용할 때의 최소 예시는 다음과 같다. 입력 경로와 출력 경로는 실제 파일로 바꾼다. 외부 CSS·이미지·폰트가 있으면 상대경로와 네트워크 접근을 확인한다.

```python
from pathlib import Path
from weasyprint import HTML

source = Path("input.html").resolve()
output = Path("output.pdf").resolve()
HTML(filename=str(source), base_url=source.parent.as_uri()).write_pdf(str(output))
```

Markdown·JSON·일반 텍스트는 먼저 제목·단락·표·이미지와 특수문자를 올바르게 이스케이프한 HTML 또는 호스트 문서로 구성한다. 이 스킬에는 자동 입력 감지기나 JSON→HTML 렌더러가 포함돼 있지 않다. 구조화 JSON은 실제 필드·자료 출처를 확인하고 문서 구조로 옮긴다.

## 글꼴과 플랫폼

`assets/fonts/`에는 라이선스와 안내문만 있으며 폰트 바이너리는 없다. 폰트 다운로드 스크립트도 없다. 번들 Noto Sans CJK가 있다고 가정하거나 CJK 글리프를 무조건 보장하지 않는다. 현재 호스트의 사용 가능한 글꼴을 확인하고 한국어·일본어·중국어·기호가 들어간 시험 문구로 결과를 눈으로 본다. 누락된 글자는 대체 글꼴 또는 접근 가능한 폰트 소스로 다시 출력한다.

WeasyPrint의 시스템 의존성은 OS마다 다르다. [공식 설치 안내](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html)를 확인하되, 비개발자 사용자의 컴퓨터에 Python 패키지·시스템 라이브러리 설치를 필수 절차로 요구하지 않는다. 현재 호스트에서 사용할 수 없는 경우 다른 실제 PDF 출력 경로를 확인한다.

## 검수와 보고

- 출력 파일이 존재하고 PDF로 다시 열리는지 확인한다.
- 제목·본문·표·이미지·페이지 수를 입력과 대조한다. 마크다운 표와 긴 단락은 페이지 경계에서 잘림이 없는지 확인한다.
- CJK·기호·숫자·인용부호의 실제 화면 표시를 확인한다. PDF 텍스트 추출만으로 글리프 표시를 판정하지 않는다.
- 원본 HTML과 비교할 때 화면과 인쇄의 차이, 외부 리소스 누락, 대체 글꼴을 기록한다.
- 미실행 검사는 `미실행`으로 보고한다. 생성 성공만으로 디자인 보존이나 다른 OS의 동일 표시를 선언하지 않는다.

## 관련 스킬

- `moai-officer:doc-html-report`: 보고서 HTML
- `moai-officer:doc-html-slide`: 슬라이드 HTML
- `moai-officer:doc-docx`: 편집 가능한 Word 문서
