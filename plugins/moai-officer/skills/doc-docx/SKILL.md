---
name: doc-docx
description: |
  편집 가능한 워드(.docx) 문서를 만들어 드립니다 — 보고서, 계약서, 제안서, 공문서, 기획서를 한국형 디자인 톤으로 바로 쓸 수 있게 출력합니다.
  다음과 같은 요청 시 사용하세요:
  - "보고서 워드 파일로 만들어줘"
  - "계약서 DOCX로 작성해줘"
  - "공문서 양식대로 써줘"
  - "제안서 워드 문서 만들어줘"
  - "사업 기획서 docx로 정리해줘"
  - "협조 공문 한 장 작성해줘"
  - "분기 보고서를 깔끔한 톤으로 워드로 뽑아줘"
  사용자 브랜드와 제출처 서식을 우선하고, 요청받은 경우 Claude 톤 예시도 참고할 수 있습니다.
  보고서·문서를 워드(.docx) 파일로 만들 때 사용 가능한 문서 생성 기능을 확인하고 결과 파일을 검증합니다.
version: "1.1.2"
---

# 워드 문서 생성기 (DOCX Generator)

## 개요

현재 호스트의 문서 생성 기능으로 DOCX를 만듭니다. 실행 환경에 `python-docx`가 이미 있으면 아래 코드 패턴을 사용할 수 있습니다.
한국 공문서·기업 보고서·계약서·제안서를 지원하며, 결과물이 "AI가 만든 듯한 진부한 디자인"이 아닌
요청한 브랜드와 문서 목적에 맞춰 색·타이포·간격을 정합니다.

## 트리거 키워드

워드, docx, Word 문서, 계약서, 공문서, 보고서 생성, 문서 편집, 기안문, 제안서, 공문, 협조문, 기획서

## 디자인 시스템 — 사용자 브랜드 우선

사용자가 제공한 브랜드 지침과 제출처 양식이 우선입니다. 없으면 읽기 쉬운 중립 서식을 고릅니다. Claude 톤을 요청한 경우에만 `references/modern-design-system.md`의 예시 색·타이포·간격을 참고합니다.

### 색 팔레트 (Claude 톤을 요청한 경우의 예시)

| 역할 | 색 | hex | 사용처 |
|---|---|---|---|
| Primary | Anthropic Orange | `#d97757` | 강조 헤딩·차트 highlight·구분선 |
| Secondary | Anthropic Blue | `#6a9bcc` | 보조 강조·인용·표 헤더 |
| Background | Light Beige | `#faf9f5` | 본문 배경 (대신 #ffffff도 가능) |
| Surface | White | `#ffffff` | 표·코드 블록 배경 |
| Text Primary | Dark | `#141413` | 본문 텍스트 (#000 대체) |
| Text Secondary | Mid Gray | `#b0aea5` | 캡션·메타 정보 |
| Border | Light Gray | `#e8e6dc` | 표 보더·구분선 |

### 타이포그래피 — 한국·영문 페어링

| 위계 | 한국 폰트 | 영문 폰트 | 사이즈 | weight |
|---|---|---|---|---|
| 본문 표지 | Pretendard | Inter | 28pt | Bold |
| H1 | Pretendard | Inter | 22pt | Bold |
| H2 | Pretendard | Inter | 18pt | SemiBold |
| H3 | Pretendard | Inter | 14pt | SemiBold |
| 본문 | Pretendard | Inter / Lora* | 11pt | Regular |
| 캡션 | Pretendard | Inter | 9pt | Regular |
| 코드/모노 | 구름 산스 코드 | 구름 산스 코드 (Goorm Sans Code) | 10pt | Regular |

\* Lora는 영문 인용문에 선택할 수 있는 서체 예시입니다. 실제 설치·대체 서체를 확인합니다.

### 간격·여백

- 페이지: A4 (210×297 mm)
- 여백: 상하 30mm · 좌우 25mm (공문서 표준) / 상하 25mm · 좌우 22mm (모던 보고서)
- 줄 간격: 본문 1.5배 · 캡션 1.2배
- 헤딩 상하: H1 상 24pt 하 12pt · H2 상 18pt 하 9pt · H3 상 12pt 하 6pt
- 단락 간 여백: 6pt
- 표 셀 패딩: 좌우 6pt 상하 4pt

## 워크플로우

### 1단계: 문서 유형 결정

| 유형 | 디자인 톤 | 권장 팔레트 변형 |
|---|---|---|
| 한국 공문서 | 제출처 서식·문서 목적 | 기관 양식 또는 중립색 |
| 기업 보고서 | 사용자 브랜드·가독성 | 중립색, 요청 시 Claude Classic 예시 |
| 계약서 | 조항 구분·가독성 | 중립색 |
| 제안서 | 사용자 브랜드·독자 | 브랜드색, 요청 시 Claude Coral 예시 |
| 기획서 | 사용자 브랜드·독자 | 브랜드색, 요청 시 Claude Blue 예시 |
| 사업계획서 | 실제 제출 요건·브랜드 | 브랜드색, 요청 시 Claude Bold 예시 |

### 2단계: 내용 수집 및 구조화

문서 유형별 표준 구조 (references/modern-templates.md 참고):

**공문서**: 실제 제출처 양식을 먼저 확인하고, 수신처·제목·본문·발신자·붙임 등 필요한 항목을 채웁니다. 일반 서식 참고는 `doc-hwp`의 `references/kr-official-forms.md`와 이 스킬의 한국형 레이아웃 예시를 사용합니다. 기관 양식이 없는데 모든 공문서에 동일한 결재란·번호 체계를 강제하지 않습니다.
**계약서**: 갑·을 표시·계약 목적·범위·기간·대금·지적재산권·비밀유지·해지·분쟁 해결·서명란
**제안서**: 표지·요약(Executive Summary)·현황·제안·기대효과·일정·예산·팀
**보고서**: 요약·배경·분석·결론·권고·부록
**기획서**: 배경·목표·전략·실행안·KPI·리스크

### 3단계: 사용 가능한 문서 도구로 생성

현재 호스트의 문서 생성 도구가 있으면 그 도구를 사용하고, 실제 DOCX 저장·열기 가능 여부를 확인합니다. `python-docx`가 이미 설치된 실행 환경에서는 아래 예시를 사용할 수 있습니다. 도구가 없으면 설치를 사용자에게 요구하지 않고 문서 내용과 구조를 제공하며 DOCX 파일을 만들었다고 표시하지 않습니다.

```python
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# 페이지 설정 — A4 + 모던 여백
section = doc.sections[0]
section.page_height = Cm(29.7)
section.page_width = Cm(21.0)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(2.2)
section.right_margin = Cm(2.2)

# 중립 예시. 사용자 브랜드·제출처 지정값이 있으면 그것을 적용한다.
INK = RGBColor(0x14, 0x14, 0x13)

# H1 스타일
h1 = doc.styles['Heading 1']
h1.font.size = Pt(22)
h1.font.bold = True
h1.font.color.rgb = INK

# 제목 내용은 실제 자료로 채우고, 색은 브랜드 지정값을 우선한다.
title = doc.add_heading('{문서 제목}', level=0)
for run in title.runs:
    run.font.color.rgb = INK
    run.font.size = Pt(28)
```

전체 코드 패턴은 `references/modern-templates.md` 참고.

### 4단계: 서식 적용 및 파일 출력

- 단락 스타일 (제목 1-3·본문·인용·캡션)
- 표 (헤더 음영 Light Beige, 보더 Light Gray, 줄 변경 시 zebra striping)
- 이미지 (로고·차트·서명) + 캡션 자동 배치
- 머리글/바닥글 (페이지 번호 우측 하단, 발행처 좌측 하단)
- 플레이스홀더 일괄 치환 (`{변수명}` → 실제 값)

### 5단계: 검수 (10단계 체크리스트)

`references/qa-checklist.md`의 10단계를 자동/반자동 점검:

1. 빈 플레이스홀더 없음 (`{변수명}` 패턴 잔존 확인)
2. 페이지 번호 모든 페이지에 표기
3. 헤딩 위계 연속 (H1 → H3 건너뛰기 없음)
4. 표 경계선 일관 (보더 색·두께 통일)
5. 폰트 깨짐 없음 (Pretendard·맑은 고딕 시스템 폰트 확인)
6. 실제 적용한 본문색과 배경색의 대비를 계산해 4.5:1 이상인지 확인
7. 이미지 캡션 일관 (위치·형식)
8. 단락 간 여백 일관 (수동 빈 줄 사용 금지)
9. 표 셀 텍스트 줄바꿈 정상 (overflow 없음)
10. AI 슬롭 표현 없음 (혁신적인·차세대·재정의하는 등 — `moai-designer:design-slop-check` 체이닝 권장)

## 모던 디자인 패턴 6종

### Pattern 1 — Executive Summary Box

보고서·제안서 첫 페이지에 1-page 요약 박스.

```
┌────────────────────────────────────────┐
│ Executive Summary                      │  ← Orange 강조선
│ ──────────────────────────────────     │
│ [4-5줄 핵심 요약 — 본문보다 약간 큰   ]│
│ [폰트, 좌측 Orange 강조선 4pt]         │
└────────────────────────────────────────┘
```

### Pattern 2 — Pull Quote

본문 중간의 인용 강조.

```
        ┃ "[인용문 — Lora 세리프 16pt 이탤릭]"
        ┃   — 출처 (Mid Gray, 11pt)
```

Anthropic Blue `#6a9bcc` 좌측 보더 4pt + Lora 이탤릭.

### Pattern 3 — Stat Callout

숫자 강조 영역.

```
   [{증감률}]      [{효율}]         [{절감액}]
   매출 증가      ROI 개선         예상 절감
```

숫자: Orange 36pt Bold · 라벨: Mid Gray 11pt.

### Pattern 4 — Comparison Table

좋은/나쁜·기존/제안 비교.

```
| 기준        | 기존        | 제안         |
| ---        | ---        | ---         |
| Beige 헤더 | White cell | Orange tint |
```

### Pattern 5 — Sidebar Note

본문 옆 메모·주석 박스 (Light Beige 배경).

### Pattern 6 — Section Divider

섹션 사이 시각 구분.

```
─── ⬢ ────────────────────────────────
      Section 2 — 시장 분석
```

Orange 작은 도형 + Mid Gray 가로선 + 섹션 번호.

## 사용 예시

- "용역 계약서 DOCX를 작성해 줘 (갑: A사, 을: B사, 계약금 1,000만 원)" → Mono Strict 팔레트
- "Q1 분기 보고서를 모던 톤으로 만들어 줘" → 브랜드 지침을 확인하고 필요한 요약·수치 블록만 구성
- "스타트업 사업계획서 30페이지" → 제출 목적·자료에 맞춰 분량과 구조를 정함
- "행정기관 협조 공문" → Classic Mono 팔레트 + 공문서 표준 양식
- "내부 기획서를 발표용으로도 쓸 수 있게" → 발표용 화면과 문서용 페이지 배치를 각각 검토

## 출력 형식

- **파일 형식**: `.docx` (Microsoft Word 2007+ 호환)
- **페이지 설정**: A4 (210mm × 297mm)
- **여백**: 상하 25-30mm, 좌우 22-25mm (문서 유형별)
- **폰트**: 사용자 브랜드·제출처 서체를 우선하고, 실제 열람 환경의 설치·대체 상태를 확인
- **색 인코딩**: sRGB
- **인코딩**: UTF-8

## 주의사항

### Claude 톤 색 사용 규칙

- Primary Orange는 강조에만 — 본문 전체에 도배 금지
- 한 문서에 Primary + Secondary + Background = 3색 + Dark/Light 무채색만
- 색 사용은 의미가 있을 때만 (장식 X)

### HWPX 대안 사용

한컴오피스 없는 환경에서 공문서가 필요한 경우 DOCX로 대체 가능합니다. 한컴 변환이 필요한 경우 `moai-officer:doc-hwp` 스킬 참조.

### 공문서 규정 준수

제출처의 현재 양식과 관련 지침을 확인합니다. 격식 공문서에는 사용자·기관 서식에서 허용하지 않은 브랜드 강조색을 임의로 넣지 않습니다.

### 폰트 및 배포

서체 이름을 DOCX에 지정하는 것과 글꼴 파일을 문서에 내장하는 것은 다릅니다. 내장을 요청받았다면 현재 도구가 이를 지원하는지와 결과 파일을 확인한 경우에만 완료로 표시합니다. 공유용 PDF도 실제 변환·열람한 경우에만 제공하고, 대체 글꼴과 줄바꿈을 확인합니다.

### 전자서명

전자서명이 필요하면 현재 사용 가능한 도구가 실제 서명 필드를 만들 수 있는지, 제출처가 어떤 형식을 받는지 확인합니다. 서명 필드나 법적 효력을 생성했다고 확인 없이 보고하지 않습니다.

### 보안

계약서 등 민감 문서는 전달 대상과 보관 방식을 확인합니다. 암호 보호를 요청받으면 현재 도구에서 실제로 설정·재열람할 수 있을 때만 완료로 표시합니다.

## 문제 해결

| 상황 | 해결 방법 |
|---|---|
| 파일 생성 실패 | 현재 호스트의 문서 도구와 파일 쓰기 권한을 확인하고, 생성할 수 없으면 초안만 제공 |
| 색이 안 나옴 | RGBColor 사용 여부 확인 (`docx.shared.RGBColor`) |
| 폰트 깨짐 | 시스템에 Pretendard 설치 또는 PDF 변환 |
| Heading 스타일 안 먹힘 | `doc.styles['Heading 1']` 직접 수정 |
| 한글 호환 | 굴림·맑은 고딕 fallback 권장 |
| 표 셀 색 안 바뀜 | `_tc.get_or_add_tcPr()` + `OxmlElement('w:shd')` 사용 |
| 페이지 번호 안 들어감 | 머리글·바닥글 영역에 `field` 객체 삽입 |

자세한 트러블슈팅·코드 예시는 `references/modern-templates.md` 참고.

## 관련 스킬 / 자체 검수

문서 생성이 끝나면 `.docx`를 다시 열어 플레이스홀더·문구·수치·표 내용을 확인합니다. 페이지 배치·글꼴 대체·표 넘침은 실제 렌더링 또는 문서 미리보기로 따로 확인합니다. 확인하지 못한 항목은 `미검증`으로 남기고 최종 PASS에 포함하지 않습니다(`references/qa-checklist.md` 참고).

| 스킬 | 사용 시점 |
|---|---|
| `moai-officer:doc-pptx` | 발표용 슬라이드 생성 (사용자 브랜드를 별도로 확인) |
| `moai-officer:doc-hwp` | 한컴 한글 문서 생성 (HWPX) |
| `moai-officer:doc-xlsx` | 엑셀 데이터 시트 |
| `moai-officer:doc-pdf` | PDF 변환·다국어 PDF |
| `moai-writer:korean-humanize` | 카피 AI 슬롭 자연화 |
| `moai-coworker:ai-slop-reviewer` | 텍스트 산출물 슬롭 검수 |
| `moai-designer:design-slop-check` | Claude Design 톤과 일관성 검수 |

## 기술 참조

- **python-docx 공식**: https://python-docx.readthedocs.io/
- **행정안전부 공문서 작성 규정**: https://www.mois.go.kr/
- **Claude 톤 예시**: `references/modern-design-system.md`의 색·타이포는 선택형 예시이며 현재 공식 브랜드 규격으로 검증되지 않음
- **Microsoft Word 파일 형식**: ECMA-376 Office Open XML

## 상세 레퍼런스

| 파일 | 로드 조건 |
|------|-----------|
| references/modern-design-system.md | 색·타이포·간격 디자인 토큰 전문이 필요할 때 |
| references/modern-templates.md | 6대 문서 유형별 모던 템플릿 구조·코드 패턴이 필요할 때 |
| references/qa-checklist.md | 5단계 검수 시 (10단계 체크리스트) |
| references/document-generator.md | 한국 비즈니스 문서 생성 가이드가 필요할 때 (기존 자료, 유지) |
| references/templates/korean-report.md | 한국형 보고서 DOCX 레이아웃(여백·폰트·구조)이 필요할 때 |
| references/templates/korean-proposal.md | 한국형 제안서 DOCX 레이아웃이 필요할 때 |
