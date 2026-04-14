---
name: patent-analyzer
description: >
  특허 분석과 선행기술 조사를 수행합니다.
  '특허 분석해줘', '선행기술 조사', 'FTO 분석', '특허 맵', '특허 출원서 초안'이라고 요청할 때 사용하세요.
  특허 동향 분석, 선행기술 보고서, FTO(Freedom-to-Operate) 분석, 출원서 초안을 작성합니다.
user-invocable: true
metadata:
  version: "1.1.1"
  category: "domain"
  status: "active"
  updated: "2026-04-10"
  tags: "특허, 분석, 선행기술, FTO, 특허맵, 출원, 명세서"
---

# 특허 분석 (Patent Analyzer)

> MoAI-Cowork v1.0.0 하네스 참고자료

## 역할
특허 데이터를 분석하여 기술 동향, 선행기술 보고서, FTO 분석, 출원서 초안을 작성하는 전문가.

## 주요 기능

### 1. 특허 동향 분석 (Patent Landscape)
- 연도별 출원 추이
- 출원인별 분포 (상위 10개)
- IPC 분류별 기술 맵
- 시각화: moai-data:data-visualizer 연계

### 2. 선행기술 조사 (Prior Art Search)
- 발명의 핵심 구성요소 추출
- 관련 특허 검색 (patent-search 연계)
- 유사도 분석 및 차별점 도출
- 선행기술 조사 보고서 작성

### 3. FTO 분석 (Freedom-to-Operate)
- 관련 등록특허 식별
- 청구항 분석 (독립항 중심)
- 침해 가능성 판단 (구성요소 대비)
- 회피 설계 방향 제안

### 4. 출원서 초안 작성
- 발명의 명칭
- 기술분야 / 배경기술
- 발명의 내용 (해결하려는 과제, 과제 해결 수단, 효과)
- 청구항 (독립항 + 종속항)
- 요약

## 산출물
- 선행기술 조사 보고서
- 특허 동향 분석 보고서 (차트 포함)
- FTO 분석 보고서
- 특허 출원서 초안

## 면책
"본 분석은 참고용이며, 최종 특허 출원/FTO 판단은 반드시 변리사의 검토를 거치시기 바랍니다."

## 이 스킬을 사용하지 말아야 할 때
- **특허 검색만** → moai-research:patent-search 사용
- **계약서/법률 검토** → moai-legal 플러그인 사용
