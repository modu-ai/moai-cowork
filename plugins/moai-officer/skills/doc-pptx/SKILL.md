---
name: doc-pptx
description: |
  발표자료의 내용과 디자인을 설계하고 실제 지원되는 도구로 PPTX 파일을 만듭니다.
  요청 예: "발표자료 PPT로", "보고서를 슬라이드로", "교육자료 PPT 만들어줘".
  결과 파일의 내용·글꼴·그림·차트를 다시 열어 검수합니다.
version: "1.1.1"
---

# PPTX 발표자료 작성

## 입력 확인

청중, 발표 목적, 원고·데이터의 출처, 필요한 슬라이드 수와 화면 비율, 사용자 브랜드 요소를 확인한다. 조직의 색·로고·폰트가 있으면 이를 우선한다. 특정 AI 회사의 브랜드색을 일반 비즈니스 문서의 기본값으로 쓰지 않는다. 수치·고객 사례·팀 경력은 원본 근거가 없으면 만들지 않는다.

## 생성 경로

1. 현재 호스트에 PPTX 생성·편집·내보내기 기능이 있는지 확인한다.
2. 없다면 실행 환경에 [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) 같은 PPTX 도구가 이미 설치됐는지 확인한다. 아래 참고 코드는 설치된 환경에서만 사용한다. 비개발자 사용자의 컴퓨터에 npm 설치를 필수 절차로 요구하지 않는다.
3. HTML·Markdown·NotebookLM 원고는 PPTX 파일과 다르다. 실제 PPTX 변환 기능을 확인하기 전에는 이 형식을 PPTX 산출물로 제시하지 않는다.
4. 출력 경로가 없으면 현재 작성할 수 있는 원고·디자인 지침만 제공하고 파일 생성은 `미실행`으로 보고한다.

## 구성

- 각 슬라이드의 주장 하나와 근거를 정한다. 표지·문제·해법·데이터·마무리 중 필요한 유형만 사용한다.
- `references/slide-archetypes.md`는 와이어프레임 예시다. 정해진 장수·시퀀스를 강제하지 않는다.
- `references/curated-palettes.md`와 `references/typography-pairings.md`는 참고 색·폰트 예시다. 조직 브랜드와 실제 발표 PC의 서체를 확인한다.
- 차트에는 분모·기간·단위·출처를 표시한다. 값이 없는 경우 예시 수치를 채운 채로 전달하지 않는다.
- 이미지·로고·인용은 사용 권한과 출처를 확인한다. ChatGPT 기본 이미지 생성 또는 사용자가 지정한 Higgsfield 경로를 사용하며, 어떤 경로로 만들었는지 기록한다.

## 출력과 검수

1. PPTX를 실제로 저장하고 다시 열어 슬라이드 수, 텍스트, 표·차트 데이터, 그림·링크를 확인한다.
2. 가능한 발표 앱에서 전체 슬라이드를 미리 보며 잘림, 겹침, 줄바꿈, 대체 폰트, 명도 대비를 확인한다. `references/qa-checklist.md`는 수동 검수 항목이다.
3. 사용 가능한 경우 PDF 미리보기도 비교한다. PDF의 표시가 PPTX의 PowerPoint·Keynote 표시와 같다는 보장은 없다.
4. 실행하지 않은 시각·앱·OS 검사는 `미실행`으로 표시한다. ZIP 구조 검사만으로 완성도를 PASS 처리하지 않는다.

## 참고 파일

| 파일 | 쓰임 |
|---|---|
| `references/pptxgen-code-patterns.md` | 설치된 PptxGenJS의 기본 작성 예시 |
| `references/qa-checklist.md` | 원본·PPTX·화면 검수 |
| `references/curated-palettes.md` | 사용자 브랜드가 없을 때 검토할 색상 예시 |
| `references/typography-pairings.md` | 사용 가능한 서체 조합 |
| `references/slide-archetypes.md` | 내용 유형별 레이아웃 예시 |
| `references/templates/minimal-business.md` | 간결한 비즈니스 레이아웃 예시 |
| `references/guide.md` | 디자인 시스템 설계 항목 |
| `references/report-generator.md` | 근거 있는 보고서형 덱 구성 |
