# MoAI-Cowork 개선 반영 보고서

작성일: 2026-10-05 · 세션: `01a10aae-6716-7681-b5d7-d558155d9f86`

## Claim — 반영 범위

앞선 전수조사의 F01–F17에 대응하는 소스·설정·생성 지침·검사·평가 정의를 현재 작업 트리에 반영했다. 18개 플러그인과 252개 스킬의 버전을 갱신했고, PM은 1.7.0, 공통 MCP 코어는 0.1.5다. 변경 이력은 [CHANGELOG.md](/Users/goos/.codex/worktrees/b0aa/moai-cowork/CHANGELOG.md)에 정리했다.

로컬 검사 묶음 15개가 통과했다. 해당 테스트는 **497개 통과·1개 제외**이며, 스킬 표준 검사는 **252개 모두 통과**했다. 자체 MCP 서버 6개의 실제 SDK 도구 목록에서 **154개 모두 동작 메타데이터를 확인**했다. 이 결과는 실제 앱의 Project 적용·계정 인증·전체 업무 실행 성공을 뜻하지 않는다.

### 개념을 반영한 업무 흐름

프로젝트의 실행 환경·폴더 접근·지침 적용 경로를 관찰한다 → 기존 자료와 실제 답을 먼저 읽는다 → 필요한 맥락만 질문하고 답·출처·유예·대기 상태를 저장한다 → 실제 노출된 스킬을 프로젝트 전문가에게 배정한다 → 선행 관계·쓰기 소유권·완료 기준을 설계한다 → 지침을 생성하고 Project 적용·새 작업 읽기를 확인한다 → 허용된 독립 업무는 병렬, 의존 업무·충돌 작업은 순차 실행한다 → 선행 결과를 검증한 뒤 합류하고 산출물과 증거를 전달한다.

계정 Projects, 로컬 폴더, Synced Work와 Claude Code의 적용 경로를 구분했다. 하위 에이전트 기능·분업 권한을 관찰하지 못하면 부모가 단계별로 순차 수행한다. 검수 역할이 실제 별도 실행되지 않았다면 독립 검수라고 보고하지 않는다.

### F01–F17 반영표

| 항목 | 반영 내용 | 소스·검증 범위 |
|---|---|---|
| F01 공통 스킬 형식 | 버전을 문자열 `metadata.version`으로 이동. 설명 길이·작성 템플릿 수정. 기존 내부 호출 의도 10개는 `metadata.invocation-scope: workflow`로 보존 | 표준 validator 252/252. 내부 호출 메타데이터는 실제 메뉴 숨김을 보장하지 않음 |
| F02 Projects 적용 | 호스트·Project 종류·실행 위치 관측과 `file_created / project_applied / read_confirmed` 상태 추가 | [호스트 계약](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/references/host-capabilities.md). 실제 앱 적용은 미실행 |
| F03 맥락 보존 | 실제 답·출처·유예·대기 질문을 설정과 요약에 보존. 빈 파일 초기화·기존 이력 덮어쓰기 지시 제거 | 설정 스키마·예시·맥락 출처 검사 및 PM 회귀 사례 |
| F04 PM 독립 설치 | PM 패키지 안에 버전·digest·소속을 가진 추천 카탈로그 포함. 현재 호스트 노출을 먼저 확인 | `skill-catalog.json`, 생성 정합 검사. 추천 자료와 호출 가능 상태 구분 |
| F05 스킬 매핑 | 현재 플러그인 소속의 qualified ID 사용. 옛 역할 분류·잘못된 예제 소속 정리 | 현재 plugin·사이트 Markdown의 구체적 스킬 참조 검사 |
| F06 순차·병렬 계약 | 의존성·상태·쓰기 소유권·외부 변경·합류·실패 후 재개 계약과 계획 검사기 추가 | PM 단위 테스트 19개. 계획 결과는 `executed: false`이며 업무 실행기는 아님 |
| F07 MCP 메타데이터 | 조회용 POST·실제 변경·로컬 작업·혼합 action을 구분. 생성 서버의 정본 생성기도 수정 | SDK 등록 도구 154개, 메타데이터 누락 0. 대표 경계 사례 6개 서버 모두 통과 |
| F08 질문 정책 | 현재 도구 스키마·자유 입력·묶음 질문·비동기 답 대기를 기준으로 통일 | [질문 계약](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/references/question-protocol.md). 빈 슬롯 채우기·반환값을 답으로 처리하는 지시 제거 |
| F09 행동 평가·CI | 스킬 표준·공통 패키지·스킬 참조·생성 정합·PM 계약·MCP 메타데이터를 CI에 연결. 기존 174개 사례와 PM 4개 사례를 eval 형식으로 준비 | 평가 정의 178개 파싱·합성 fixture 13개 확인. 실제 모델 평가 0회 |
| F10 최신 설치·에이전트 안내 | 자연어 공통 진입, 계정 Work와 로컬 Codex 에이전트 구분, Project 적용·읽기 확인 안내 | README·사이트 문서·생성 카탈로그 갱신. Hugo 빌드 통과 |
| F11 공통 패키지 | 18개 루트 `plugin.json / mcp.json` 생성. 전송 타입·OpenAI 확장 overlay 적용. 공통 형식에 없는 legacy `timeout` 제외 | Agent Plugins 1.0.0 스키마 검사, 기존 Claude 매니페스트 18개 CLI 검증 |
| F12 계정·큰 스키마 | 모든 공통 코어 서비스에 프로젝트 자격증명 파일 선택 추가. 계정 참조·키 환경변수 우선순위·OAuth 파일 분리 안내. 실제 입력 스키마 크기 측정 | 새 계정 파일·격리·우선순위 테스트 9개. 계정 인증·호스트의 도구 선택 성능은 미실행 |
| F13 지침 예산 | 500줄과 실제 발견 체인의 UTF-8 byte 예산 검사. 전체 워크플로우는 설정에 보존하고 주요 체인만 지침에 요약 | 다중 파일·한글 byte 초과 검사. 실제 호스트의 설정 한도는 별도 확인 |
| F14 안전한 복구 | 변경 전후 digest·원문을 기록하고 현재 내용이 적용 후 값과 같을 때만 복구. 후속 편집 보존 | 조건부 복구 함수의 충돌 테스트. 실제 파일 쓰기의 원자적 비교·교체를 구현했다고 주장하지 않음 |
| F15 링크·이름 | 패키지 밖 상대 링크를 qualified ID로 바꾸고 현재 cookbook의 옛 스킬 이름 수정 | 현재 카탈로그 참조 검사와 Hugo 빌드 |
| F16 전문가 계약 | 역할·스킬·입출력·쓰기 소유권·검증·부족한 맥락을 전문가별로 지정. 선택적 스킬 로드·검수 권한·부모 질문 중계 명시 | 전문가 binding·미배정 스킬 검사. 실제 하위 에이전트 호출은 미실행 |
| F17 긴 지침·유지보수 | PM의 개선 절차와 윤문의 실행 절차를 참조로 이동. 개발 진입점 17개의 외부 MoAI-ADK 의존성·대체 절차 및 생성 정본 추가 | PM 35,649 → 27,882 bytes. 윤문 40,795 → 16,514 bytes. 윤문 Phase 1–7은 원문 그대로 이동 |

### 주요 실행·유지보수 파일

- [PM 스킬](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/SKILL.md), [설정 스키마](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/references/templates/config.schema.json), [프로젝트 계약 검사기](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/scripts/project_contract.py)
- [전문가 계약](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/references/expert-contract.md), [실행 계약](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/references/execution-protocol.md), [계정 연결](/Users/goos/.codex/worktrees/b0aa/moai-cowork/plugins/moai-pm/skills/project/references/account-bindings.md)
- [표준·참조 검사](/Users/goos/.codex/worktrees/b0aa/moai-cowork/scripts/check-skill-contracts.py), [MCP 실제 도구 검사](/Users/goos/.codex/worktrees/b0aa/moai-cowork/scripts/check-mcp-annotations.py), [공통 패키지 생성기](/Users/goos/.codex/worktrees/b0aa/moai-cowork/scripts/sync-plugin-contracts.py)
- [업무 평가 실행 안내](/Users/goos/.codex/worktrees/b0aa/moai-cowork/docs/behavioral-evals.md), [CI](/Users/goos/.codex/worktrees/b0aa/moai-cowork/.github/workflows/mcp-cross-platform.yml)

## Evidence — 실행한 검사와 관찰 출력

### 변경 범위의 테스트

```text
python3 reports/20261005-work-cowork-update/run_checks.py
RESULT 15 checks; 15 passed
```

검사별 실제 명령·실행 폴더·HEAD·출력 파일은 [checks.json](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/checks.json)에 있다.

| 테스트 | 관찰 결과 |
|---|---:|
| MCP 런처 | 25 passed, 1 skipped |
| 한국어 윤문 | Ran 137 tests, OK |
| PM 계약 | Ran 19 tests, OK |
| 공통 MCP 코어 | 81 passed |
| IP / OpenAI / Cafe24 / Imweb / Smartstore / Threads | 32 / 6 / 12 / 34 / 28 / 123 passed |
| 합계 | 497 통과, 1 제외 |

제외된 1개는 `sys.platform != win32` 조건의 Windows `.cmd` 실행 검사다. 이번 실행은 macOS이며 Windows CI 결과를 포함하지 않는다.

### 표준·패키지·메타데이터

```text
uv run --no-project --python 3.11 --with skills-ref==0.1.1 python reports/20261005-work-cowork-update/validate_skills.py
"checked": 252, "passed": 252, "failed": 0, "error_classes": {}

uv run --no-project --python 3.11 --with skills-ref==0.1.1 --with jsonschema==4.25.1 --with pyyaml==6.0.3 python scripts/check-skill-contracts.py
"skills": 252, "packages": 18, "errors": [], "scope": "offline_contracts_only"

python3 reports/20261005-work-cowork-update/probe_runtime.py
{"registered_tools": 154, "without_annotations": 0, "servers": 6}

python3 scripts/check-plugin-runtimes.py
검사한 플러그인 18개 — 오류 0건, 참고 2건
```

검증 기록: [스킬별 결과](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/skills-ref-validation.json), [공통 계약](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/skill-contracts-final.log), [SDK 도구 목록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/runtime-probe-evidence.json), [동작 경계 검사](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/annotation-checks.json).

참고 2건은 media·seller의 Higgsfield 연결이 Claude와 OpenAI 호환 매니페스트에서 다른 기존 구성이다. OpenAI의 공식 플러그인 계정 연결 경로를 유지했으며, 이번 검사에서 그 계정 인증은 실행하지 않았다.

### 평가 정의·문서·구문

```text
uv run --no-project --with pyyaml python scripts/sync-skill-evals.py --check
{"cases": 174, "runnable_definitions": 174, "fixture_gaps": 0, "errors": [], "model_runs": 0}

uv run --no-project --python 3.11 --with pyyaml --with pillow python reports/20261005-work-cowork-update/verify_eval_definitions.py
{"definitions_parsed": 178, "png_fixtures_verified": 13, "native_claude_eval_runs": 0, "scope": "offline_yaml_and_fixture_checks"}

hugo --source <이 작업 트리>/www --destination <별도 임시 폴더> --quiet
Hugo exit: 0 HTML files: 264

git diff --check
exit 0, 출력 없음
```

Python 182개·실제 JSON 102개, YAML 219개·TOML 20개 구문 검사는 오류 0건이다. `www/layouts/_default/search.json`은 Go 템플릿이므로 일반 JSON 검사에서 제외하고 Hugo 빌드로 확인했다. [구문 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/syntax-evidence.json), [YAML·TOML 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/data-syntax-evidence.json), [Hugo 명령·결과](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/hugo-evidence.json).

Claude Code 2.1.289의 `claude plugin validate <각 플러그인 경로>`에서 기존 매니페스트 18개가 통과했다. [실제 출력](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/claude-package-validation.json). 별도 `skills / agents` 디렉터리 호출 32개는 exit 0이지만 모두 `contents: []`였다. 이 빈 결과를 252개 스킬 또는 28개 에이전트의 native 검증 통과로 세지 않았다. [검사 공백 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/claude-components-gap.json).

## Baseline-attribution — 측정 대상

- 트리: `/Users/goos/.codex/worktrees/b0aa/moai-cowork`
- 기준 HEAD: `2c3cef1d24e88b3bfe8db61c713ffae317b346d0`, detached 상태
- 이번 변경은 해당 HEAD 위의 미커밋 작업이며 소스 파일 606개가 변경·추가됐다. 대부분 공통 메타데이터·버전·생성 파일과 평가 정의다.
- 파일별 SHA-256은 [변경 기준 기록](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/changed-files-baseline.json)에 보존했다. 검사 명령·출력은 이번 트리에서 실행한 값이며 다른 패키지·기존 보고서의 통과 수를 재사용하지 않았다.
- 이전 전수조사 보고서는 이 수정 이전의 기준으로 별도 보존했다. 커밋·푸시·앱 설치·공개 배포는 수행하지 않았다.

## Gaps — 아직 관찰하지 않은 범위

후속 확인: 사용자가 제공한 ChatGPT 질문 화면에서 `1 of 4` 카드 표시, 선택지, 직접 답변 입력, 건너뛰기 버튼을 확인했다. **ChatGPT에서 질문 도구를 사용할 수 있다.** 질문 계약과 호스트 계약에 이를 명시했다. 이 화면은 호출당 최대 질문 수, 도구의 내부 이름, 답변 제출·수신 완료까지 입증하지 않으므로 그 부분은 현재 세션의 도구 스키마와 실제 응답으로 확인한다. 화면의 강의 일정 질문은 이 저장소를 수정하라는 지시로 사용하지 않았다. [첨부 근거](/Users/goos/.codex/worktrees/b0aa/moai-cowork/reports/20261005-work-cowork-update/chatgpt-question-ui.png)

1. 실제 ChatGPT Work의 계정 Projects·로컬/Synced Work 및 Claude Cowork에서 설치 → Project 적용 → 새 작업 읽기 → 전문 스킬·에이전트 호출 → 대표 업무 완료까지의 전체 실행.
2. 178개 eval 정의의 실제 Claude 모델 실행·비교군·judge 결과. 준비된 파일과 오프라인 구문 검사만 완료했다.
3. 실제 외부 서비스 계정의 식별·인증·조회·변경·중복 실행·OAuth 회전. SDK 도구 목록과 단위 테스트는 실제 계정 실행을 대신하지 않는다.
4. Windows·Linux의 새 CI 실행 결과. Windows `.cmd` 테스트는 이번 macOS에서 제외됐다.
5. 28개 에이전트의 각 호스트 발견·독립 호출·실제 권한 제한, 내부 호출용 메타데이터 10개의 앱 메뉴 표시 방식. 공통 메타데이터는 호스트의 권한·표시 제어가 아니다.
6. 큰 혼합 action 도구에 대한 현재 앱의 선택 지연·잘못된 선택·토큰 비용. Imweb 입력 스키마 합계 84,670 bytes, Cafe24 33,687 bytes를 측정했지만, 그 크기만으로 성능 결함을 판정하지 않았다.

## Residual-risk — 운영 시 확인할 점

호스트의 실제 적용·노출·권한과 계약 문서의 선언은 다르다. PM은 관찰하지 못한 상태를 미확인으로 기록해야 한다. 프로젝트 계정 파일을 분리해도 실제 키 환경변수가 우선하므로 대상 계정 식별을 실제 조회로 대조해야 한다. OAuth 회전 파일도 계정별로 선택해야 한다.

계약 검사기는 의존성·소유권·계획을 검사하며 에이전트를 실행하거나 MCP 권한을 강제하지 않는다. 조건부 롤백 함수도 실제 파일 시스템의 원자적 compare-and-swap을 제공하지 않는다. 실제 쓰기는 현재 호스트의 충돌 감지 기능과 직전 상태 확인을 함께 사용해야 한다.

평가 정의의 문자열 검사·LLM judge만으로 법적 정확성·재무 산술·의미 보존·실제 게시를 통과시키지 않는다. 공개 MCP 배포에 필요한 인증·심사·운영 서버는 로컬 플러그인 형식 검사와 별도다. 이 보고서의 완료 범위는 소스 개선과 관찰한 로컬 검증까지다.

## 공식 근거

- [Agent Skills 규격](https://agentskills.io/specification) — 공통 frontmatter·metadata·설명 길이
- [OpenAI 플러그인 패키징](https://developers.openai.com/plugins/build/plugins) — 공통 매니페스트·MCP transport·확장 우선순위
- [OpenAI 프로젝트 지침](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [하위 에이전트](https://learn.chatgpt.com/docs/agent-configuration/subagents) — 실제 지침 발견·byte 예산·호스트 기능 구분
- [Claude Code 지침](https://code.claude.com/docs/en/memory), [하위 에이전트](https://code.claude.com/docs/en/sub-agents) — 지원되는 import·에이전트·선택적 스킬 로드
- [Claude 플러그인 eval](https://code.claude.com/docs/en/plugin-evals), [OpenAI 스킬 테스트](https://developers.openai.com/plugins/build/skills) — 업무 평가와 구조 검사의 구분
