---
title: "PM — 프로젝트 구성 담당"
description: "내 업무의 맥락과 실제 기능을 확인해 지침과 전문가 순서를 구성합니다"
weight: 10
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-06
geekdocBreadcrumb: true
aliases: ["/agent-teams/pm/"]
---

**PM은 프로젝트의 목표·자료·기준을 정리하고 사용할 스킬과 업무 순서를 연결합니다.** 아직 설치하지 않은 플러그인은 추천 상태로 남기며, 지침 파일 생성과 앱 Projects 적용을 구분합니다.


<!--more-->

## 프로젝트 지침은 첫 실행으로 확인합니다

{{< concept-diagram pm-setup >}}

## 첫 요청

```text
내 프로젝트를 시작해 줘. 현재 환경과 자료를 확인하고 부족한 정보는 질문해 줘.
업무에 맞는 전문가 스킬, 입력·출력, 순차·병렬 순서와 완료 기준을 정리해 줘.
지침 생성, 적용, 새 작업에서 읽기 확인, 첫 업무 실행 상태를 따로 알려 줘.
```

## 프로젝트 구성 흐름

맥락 수집 → 기능 확인 → 업무 설계 → 빠진 정보 확인 → 지침 생성 → 지원되는 역할 구성 → 필요한 연결 → 지침 적용 확인과 첫 실행.

앱 Projects에는 현재 화면이 지원하는 지침·자료 경로를 사용합니다. 로컬 Codex의 `AGENTS.md`, Claude Code의 `CLAUDE.md`와 에이전트 설정은 해당 호스트에서만 생성·발견 여부를 확인합니다. 파일이 생겼다는 이유로 모든 앱에서 자동 적용됐다고 표시하지 않습니다.

## 사용하면서 바꾸기

- “프로젝트 상태를 확인해 줘”: 답변·미정 정보·단계별 상태 확인.
- “현재 설치된 스킬에 맞춰 업데이트해 줘”: 기능 변경을 확인하고 지침 동기화.
- “반복 수정 원인을 찾아 개선해 줘”: 실제 문제를 확인하고 지침을 최소 수정.
- “환경을 진단해 줘”: 지원 기능·연결·지침 적용 상태 확인.

명령이 표시되는 환경에서는 `/project`, `/project update`, `/project evolve`, `/project doctor`를 사용할 수도 있습니다. 자연어가 공통 진입 경로입니다.

## 포함된 기능

{{< employee-skills "moai-pm" >}}
{{< employee-agents "moai-pm" >}}

[첫 프로젝트 실습](/workflows/first-project/) · [프로젝트 지침](/getting-started/projects/) · [전문가 분업](/workflows/experts/)

## 공식 문서와 참고 자료

- [PM 스킬 원본](https://github.com/modu-ai/moai-cowork/tree/main/plugins/moai-pm/skills/project)
- [ChatGPT 프로젝트](https://learn.chatgpt.com/docs/projects)
- [Claude 프로젝트](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
