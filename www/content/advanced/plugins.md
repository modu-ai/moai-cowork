---
title: "패키지와 설치 경로"
description: "휴대 가능한 패키지와 호스트별 설치·권한·도구 노출을 확인합니다"
weight: 10
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-06
geekdocBreadcrumb: true
---


<!--more-->


## 저장소의 구성

`plugins/<이름>/plugin.json`과 `mcp.json`은 휴대 가능한 패키지 정의입니다. Claude와 기존 Codex 호스트의 manifest도 함께 유지합니다. 실제 설치는 계정·조직·호스트가 지원하는 경로를 사용합니다.

## 등록과 실제 사용은 다릅니다

1. 패키지 정의를 검증합니다.
2. 호스트가 허용하는 마켓플레이스·패키지 경로로 설치합니다.
3. 현재 작업에 스킬과 도구가 노출되는지 확인합니다.
4. 연결 계정으로 읽기 작업을 시험합니다.
5. 대표 결과물을 검토합니다.

Claude Code 터미널 설치는 해당 CLI의 현재 `plugin` 도움말과 공식 문서를 따릅니다. ChatGPT Work의 계정 설치와 로컬 Codex 설정도 별도로 확인합니다. 로컬 개발 패키지를 검증했다고 공용 디렉터리에 게시됐다고 표시하지 않습니다.

## 생성된 목록과 원본

스킬·에이전트 목록은 manifest와 frontmatter에서 생성됩니다. 문서에 숫자를 직접 복제하지 않고 `www/data/agent_teams.json`을 사용합니다. 패키지 자체의 `agents/*.md`가 모든 호스트에서 자동 등록된다는 전제를 두지 않습니다.

## 공식 문서와 참고 자료

- [OpenAI 패키지 작성](https://developers.openai.com/plugins/build/plugins)
- [Claude 플러그인](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Claude Code 플러그인](https://code.claude.com/docs/en/plugins)
