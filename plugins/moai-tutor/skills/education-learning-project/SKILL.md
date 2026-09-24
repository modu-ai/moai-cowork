---
name: education-learning-project
description: |
  학습자가 자기 목표를 관리할 프로젝트 폴더와 로드맵·진도 기록을 만듭니다.
  요청 예: "파이썬 입문 학습 프로젝트", "영어 회화 진도 추적", "기존 공부 계획 정리".
  Claude Cowork·ChatGPT Work에서 같은 AGENTS.md 지침을 사용합니다.
version: "1.1.1"
---

# 자기주도 학습 프로젝트

## 입력

학습 주제, 이미 아는 것, 도달 목표, 가용 학습 시간, 자료와 도구 제약을 확인한다. 정식 평가 자료가 없다면 현재 수준은 사용자의 자기 보고로 표시한다. 목표가 넓으면 첫 단계의 범위를 좁혀 제안한다.

## 생성 순서

1. 사용자가 원하는 폴더 위치를 확인한다. 기존 파일을 읽고 충돌 여부를 확인한 뒤 새 파일만 만든다.
2. 목표를 관찰 가능한 행동과 산출물로 적고, 선수 지식 순서로 학습 단계를 배치한다. 단계 수를 고정하지 않는다.
3. `AGENTS.md`에 학습 맥락과 작업 방법을 적는다. Claude용 `CLAUDE.md`가 필요하면 내용은 `@AGENTS.md` 한 줄만 둔다.
4. `roadmap.md`에는 단계별 목표·자료·완료 기준을, `progress.md`에는 현재 상태·학습 기록·다음 행동을 적는다.
5. 사용자가 자료 파일을 원할 때만 `materials/`를 만들고, `education-tutor-research`와 `education-learning-material`의 실제 사용 결과를 넣는다.
6. 생성한 각 파일을 다시 읽어 경로·내용을 확인하고, 아직 조사하거나 공부하지 않은 단계를 완료로 표시하지 않는다.

## 최소 구조

```text
<학습주제>-학습/
  AGENTS.md
  CLAUDE.md
  roadmap.md
  progress.md
  materials/  # 자료 파일을 요청한 경우
```

생성 후 사용자가 첫 단계의 질문을 조사하거나 직접 연습하도록 안내한다. 조사·HTML 자료 제작·진도 갱신은 각각 실행했을 때만 완료로 보고한다.

강사용 커리큘럼은 `education-curriculum-designer`, 시험 문항은 `education-assessment-creator`를 사용한다.
