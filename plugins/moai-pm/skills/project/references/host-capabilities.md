# 호스트·Project 적용 계약

앱 이름만으로 기능을 확정하지 않는다. 현재 세션의 도구·프로젝트 종류·폴더 접근·설치 스킬·에이전트 기능을 관찰한다. 관찰하지 못한 값은 `unknown` 또는 `null`이며, 가능한 것으로 표시하지 않는다.

## 시작 시 확인

- 현재 실행 위치: 호스팅 환경, 로컬 컴퓨터, 연결된 컴퓨터 중 무엇인가.
- Project 종류: 계정 Project, 로컬 폴더 Project, 연결된 실행인가.
- 실제 읽고 쓸 폴더·업로드 소스·커넥터와 접근 범위.
- 읽히는 지침 파일·Project UI 지침·사용자/조직 상위 지침.
- 노출된 스킬과 도구, 하위 에이전트, 질문 채널과 그 스키마.
- 실제 동시 실행 한도와 이 요청에서 허용된 분업. 기본은 순차다.

이 관측은 `.moai/config.json`의 `host`에 실행 위치·관측 근거와 함께 기록한다. 모델·비용·권한 설정을 임의로 바꾸지 않는다.

ChatGPT에서도 질문 도구를 사용할 수 있으므로 지원 여부를 앱 이름으로 부정하지 않는다. 현재 질문 채널이 노출되면 `question-protocol.md`에 따라 사용한다. 화면에서 확인한 선택지·직접 답변·건너뛰기와 실제 호출 스키마·응답 수신은 각각 관측 근거를 기록한다.

## 환경별 적용

| 환경 | 확인·적용 방식 |
|---|---|
| ChatGPT Work 계정 Project | Project 지침과 업로드/연결 소스를 확인한다. 로컬 폴더 자동 접근을 가정하지 않는다 |
| OpenAI 로컬 Project/Codex | 실제 작업 루트와 `AGENTS.md` 발견 체인을 확인한다. 지원되는 `.codex/agents/*.toml`만 생성·검증한다 |
| 연결된 컴퓨터에서 Work | 부모·하위 작업의 실행 위치·폴더·도구 차이를 각각 기록한다 |
| Claude 계정/폴더 Project | 현재 Project 화면의 지침·소스·폴더 연결을 확인한다. Code 파일 발견 규칙과 구분한다 |
| Claude Code | 버전·설정에 따른 `AGENTS.md` 직접 읽기 또는 `CLAUDE.md`의 `@AGENTS.md` import를 확인한다 |

프로젝트별 커스텀 에이전트를 발견하지 못하면 파일 생성과 호출 가능을 구분하고, 해당 전문가 계약을 부모가 순차 실행한다. 독립 검수 기능을 사용하지 못했으면 이를 기록한다. 동일 대화의 후속 검토를 독립 에이전트 검수라고 부르지 않는다.

## 적용 상태

1. `file_created`: 로컬 파일을 생성하고 다시 읽었다.
2. `project_applied`: 지원되는 호스트 도구 또는 사용자가 Project 지침·소스를 반영했다. 근거를 기록한다.
3. `read_confirmed`: 새 대화/실행에서 프로젝트 목적·제약·체인이 읽히는지 확인했다.
4. 위 단계를 관찰하지 못했다면 그 상태를 `unverified`로 남긴다.

UI 쓰기 도구가 없으면 프로젝트 지침에 붙여 넣을 완성된 본문·첨부할 자료·구체적인 적용 경로를 제공한다. 요청하지 않은 메시지 전송·공개 게시·관리자 설정 변경을 하지 않는다. 파일을 만들었다는 이유만으로 Project 적용 완료라고 보고하지 않는다.

## 완료 확인

현재 스킬 인벤토리에서 대표 체인 하나를 선택해 프로젝트 제약을 반영한 작은 산출물을 만든다. 파일·입력 사실·실제 도구 결과를 대조한다. 새 대화에서 답변·유예 질문·스킬 binding을 복원한다. 못 실행한 앱·인증·업무 단계는 미실행으로 기록한다.

## 공식 근거

- [OpenAI Projects](https://learn.chatgpt.com/docs/projects)
- [OpenAI AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenAI Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [OpenAI Plugins](https://learn.chatgpt.com/docs/plugins)
- [Claude Projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Claude Code 지침 읽기](https://code.claude.com/docs/en/memory)

기능·화면 안내는 위 문서와 현재 호스트를 대조한다. cloud-orchestrated Work의 플러그인 훅을 핵심 완료 조건으로 사용하지 않는다. 로컬 에이전트 파일과 Work 호스팅 에이전트는 같은 설치 기능이 아니다.
