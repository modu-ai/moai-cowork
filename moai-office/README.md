# moai-office

문서 생성 플러그인 — PPT 디자인(PPTX), Word(DOCX), Excel(XLSX), 한글(HWPX).

Pretendard+명조 기반 한국형 디자인과 OWPML 표준을 지원합니다.

## 스킬

| 스킬 | 설명 | 상태 |
|------|------|:----:|
| [pptx-designer](./skills/pptx-designer/) | PPT 디자인 — pptxgenjs 코드 생성. 발표자료, 보고서, 기안서 슬라이드 | ✅ 완성 |
| [hwpx-writer](./skills/hwpx-writer/) | 한글 문서 — python-hwpx + lxml 기반 OWPML HWPX 파일 생성. 공문서, 기안서 | ✅ 완성 |
| [docx-generator](./skills/docx-generator/) | 워드 문서 — DOCX 형식 보고서, 계약서, 공문서, 제안서 생성 | 📝 초안 |
| [xlsx-creator](./skills/xlsx-creator/) | 엑셀 문서 — XLSX 형식 데이터 표, 차트, 수식 포함 스프레드시트 생성 | 📝 초안 |

## 에이전트

| 에이전트 | 모델 | 설명 |
|---------|:----:|------|
| document-generator | Sonnet | 500단어 이상 장문 비즈니스 문서 생성. moai-business, moai-legal 등에서 공유 호출 가능 |
| format-converter | Sonnet | HWPX/PPTX/DOCX/XLSX 파일 형식 변환 및 템플릿 기반 생성. 전 플러그인에서 공유 호출 가능 |

## 사용 예시

```
2025년 상반기 성과 발표 PPT 12장 만들어줘. 깔끔한 미니멀 디자인.
```

```
행정기관 제출용 사업 제안서 한글(hwpx) 파일로 만들어줘
```
