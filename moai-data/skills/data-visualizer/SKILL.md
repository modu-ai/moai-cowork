---
name: data-visualizer
description: >
  데이터 시각화와 차트 생성을 수행합니다.
  '차트 만들어줘', '그래프 그려줘', '시각화해줘', '대시보드 만들어줘'라고 요청할 때 사용하세요.
  Mermaid 다이어그램, Chart.js HTML 차트, 인터랙티브 대시보드를 생성하고 moai-office로 PPT/Word 변환합니다.
user-invocable: true
metadata:
  version: "1.1.3"
  category: "domain"
  status: "active"
  updated: "2026-04-10"
  tags: "차트, 그래프, 시각화, Mermaid, 대시보드, PPT, Chart.js"
---

# 데이터 시각화 (Data Visualizer)

> MoAI-Cowork v1.0.0 하네스 참고자료

## 역할
데이터를 시각적으로 표현하는 전문가. Mermaid, Chart.js, HTML 기반 차트/대시보드를 생성하고 PPT/Word로 변환합니다.

## 시각화 전략 (자동 판단)

### 방식 1: Mermaid 다이어그램 (간단 차트)
- pie chart, bar chart, flowchart, gantt
- Cowork Artifacts에서 직접 렌더링
- 빠르고 가벼움, 별도 파일 불필요

### 방식 2: HTML/JS 인터랙티브 차트 (상세 분석)
- Chart.js 기반 HTML 파일 생성
- 막대, 선, 파이, 도넛, 레이더, 버블 차트
- 필터, 호버 툴팁, 줌 지원
- Cowork Artifacts에서 렌더링 가능

### 방식 3: 마크다운 테이블 (텍스트 기반)
- 간단한 비교표, 순위표
- 별도 파일 불필요

## 판단 기준

| 조건 | 방식 |
|------|------|
| 데이터 5행 이하 | 마크다운 테이블 |
| 단순 비율/분포 | Mermaid pie/bar |
| 시계열/트렌드 | Chart.js 선 차트 |
| 다차원 비교 | Chart.js 레이더/버블 |
| 인터랙티브 필요 | HTML 대시보드 |

## PPT/Word 변환 플로우

사용자가 "PPT로 만들어줘" 요청 시:
1. HTML/Chart.js 차트 → 스크린샷/이미지 추출
2. 데이터 테이블 + 차트 이미지 → moai-office:pptx-designer로 전달
3. PPT 슬라이드 생성

Word 보고서 요청 시:
1. 차트 이미지 + 분석 텍스트 → moai-office:docx-generator로 전달
2. Word 문서 생성 (차트 임베드)

## 산출물
- Mermaid 다이어그램 (인라인)
- Chart.js HTML 파일 (인터랙티브)
- 마크다운 보고서 (테이블 + 인사이트)

## 이 스킬을 사용하지 말아야 할 때
- **데이터 탐색/프로파일링** → moai-data:data-explorer 사용
- **공공데이터 조회** → moai-data:public-data 사용
