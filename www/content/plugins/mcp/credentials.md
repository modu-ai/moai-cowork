---
title: "계정과 API 키 설정"
description: "로그인과 로컬 자격증명 파일을 구분하고 프로젝트별 계정을 확인합니다"
weight: 10
date: 2026-10-05T00:00:00+09:00
lastmod: 2026-10-06
geekdocBreadcrumb: true
---

**연결하려는 서비스의 계정과 인증 방식을 확인하세요.** 현재 앱이 비밀정보 입력란이나 로그인 절차를 제공하면 그 경로를 사용합니다. 앱 이름만으로 입력 폼의 존재나 저장 위치를 단정하지 않습니다.


<!--more-->

## 계정 선택부터 실제 조회 확인까지

{{< concept-diagram credentials >}}

## 로컬 서버의 자격증명 파일

MoAI 자체 서버 중 공통 자격증명 모듈을 사용하는 서버는 환경변수 또는 로컬 파일을 읽습니다. 기본 경로는 `~/.moai/mcp/<서비스>.json`입니다. 이 경로는 계정의 웹 Projects 저장소가 아닙니다. 파일을 읽을 수 있는 로컬 실행 환경에서만 사용합니다.

```json
{
  "DART_API_KEY": "본인 컴퓨터에서 입력"
}
```

키 값은 채팅·지침·Git 저장소에 넣지 않습니다. 실제 키 입력은 본인 컴퓨터의 지원되는 비밀정보 경로에서 진행합니다.

## 서비스별 항목

| 코워커 | 서비스 이름(파일명) | 항목 |
|---|---|---|
| `moai-accountant` · `moai-analyst` · `moai-coworker` | `dart` | `DART_API_KEY` |
| `moai-media` | `elevenlabs` | `ELEVENLABS_API_KEY` |
| `moai-media` (정확한 GPT Image 2.5 생성) | `openai` | `OPENAI_API_KEY` |
| `moai-seller` (스마트스토어) | `smartstore` | `NAVER_COMMERCE_CLIENT_ID` · `NAVER_COMMERCE_CLIENT_SECRET` · `NAVER_COMMERCE_ACCOUNT_ID` · `NAVER_COMMERCE_TYPE` |
| `moai-seller` (아임웹) | `imweb` | `IMWEB_CLIENT_ID` · `IMWEB_CLIENT_SECRET` · `IMWEB_ACCESS_TOKEN` · `IMWEB_REFRESH_TOKEN` · `IMWEB_UNIT_CODE` |
| `moai-seller` (카페24) | `cafe24` | `CAFE24_MALL_ID` · `CAFE24_CLIENT_ID` · `CAFE24_CLIENT_SECRET` · `CAFE24_ACCESS_TOKEN` · `CAFE24_REFRESH_TOKEN` |
| `moai-threads-poster` | `threads` | `THREADS_ACCESS_TOKEN` · `THREADS_USER_ID` · `IG_ACCESS_TOKEN` · `IG_USER_ID` |
| `moai-lawyer` (특허·상표) | `ip` | `KIPRIS_API_KEY` · `USPTO_ODP_API_KEY` · `USPTO_TSDR_API_KEY` · `JPO_API_USER` · `JPO_API_PASSWORD` · `EPO_OPS_KEY` · `EPO_OPS_SECRET` (쓰는 기관만) |
| `moai-lawyer` (국가법령정보, ChatGPT Work) | `korean-law` | `LAW_OC` |

## 프로젝트마다 계정이 다르면

지원되는 공통 모듈의 `<SERVICE>_CREDENTIALS_FILE` 설정으로 프로젝트·계정별 파일을 지정할 수 있습니다. 예를 들어 `SMARTSTORE_CREDENTIALS_FILE`은 스마트스토어 파일 경로를 선택합니다. 실제 키 환경변수와 파일 선택 설정을 함께 사용할 때는 서버의 우선순위를 확인합니다.

OAuth 로그인은 실제 인증된 사용자와 권한을 확인하세요. 토큰 저장과 갱신 방식은 서버별로 다릅니다. 전역 파일 하나에 서로 다른 업무 계정을 섞지 않습니다.

## 설정 후 확인

파일 생성은 인증 성공이 아닙니다. 읽기 전용 조회로 계정·권한·유효 기간을 확인합니다. API 이용료와 앱 구독은 각 서비스에서 확인하세요. 실패하면 [연결 문제 해결](/plugins/mcp/troubleshooting/)로 이동합니다.

## 공식 문서와 참고 자료

- [공통 자격증명 구현](https://github.com/modu-ai/moai-cowork/tree/main/plugins/_shared/moai-mcp-core)
- [ChatGPT 연결과 인증](https://learn.chatgpt.com/docs/plugins)
- [Claude 연결 범위](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
