---
title: "MCP 설치와 연결 확인"
description: "현재 앱과 서버 방식에 필요한 실행 도구만 준비합니다"
weight: 10
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-06
geekdocBreadcrumb: true
---

**모든 사용자가 uv와 Node.js를 설치할 필요는 없습니다.** 현재 작업이 로컬 서버를 실행하는지, 원격 커넥터를 연결하는지부터 확인하세요.


<!--more-->


## 설정 순서

1. **실행 환경 확인:** 데스크톱·웹·클라우드 중 어디서 실행하는지 확인합니다.
2. **서버 방식 확인:** 패키지의 MCP 설명과 앱의 연결 경로를 확인합니다.
3. **실행 도구 준비:** 로컬 Python 서버는 uv, Node 기반 서버는 Node.js 등이 필요할 수 있습니다.
4. **계정 인증:** 지원되는 로그인 또는 비밀정보 설정을 사용합니다.
5. **조회 검증:** 올바른 계정의 제한된 자료를 읽고 결과를 확인합니다.

## 로컬 실행 도구가 필요할 때

- [uv 공식 설치 안내](https://docs.astral.sh/uv/getting-started/installation/).
- [Node.js 공식 다운로드](https://nodejs.org/en/download).

설치 후에는 새 터미널에서 필요한 명령만 확인합니다.

```text
uv --version
node --version
npx --version
```

버전이 나온 것은 실행 도구 준비를 확인한 것입니다. 플러그인 로드·서버 실행·계정 인증을 모두 증명하지는 않습니다.

## 연결 시험 요청

```text
연결된 서비스와 계정을 확인하고, 필요한 범위의 자료를 읽기만 해 줘.
어느 계정·기간에서 가져왔는지와 실제 조회 결과를 알려 줘.
상품 변경, 게시, 발송은 하지 마.
```

조회 결과가 없으면 빈 결과와 인증 실패를 구분합니다. 키를 설정하는 방법은 [자격증명](/plugins/mcp/credentials/), 오류가 있다면 [연결 문제 해결](/plugins/mcp/troubleshooting/)에서 확인하세요.

## 공식 문서와 참고 자료

- [ChatGPT 연결 도구](https://learn.chatgpt.com/docs/plugins)
- [Claude 연결 실행 범위](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
