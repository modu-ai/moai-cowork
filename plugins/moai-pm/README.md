# moai-pm (PM) — AI 코워커를 부르는 진입점

> **PM**은 프로젝트를 시작할 때 **어떤 AI 코워커가 필요한지 판단해 팀을 꾸려 주는** 허브 플러그인입니다. 진입점은 단 하나 — `/project` 스킬 하나로 통합되어 있습니다.

---

## `/project` — 단일 진입점

```
/project <자연어 지시>
```

Claude Cowork·ChatGPT Work 프로젝트 초기화 — 소크라테스 인터뷰 → 현재 호스트의 AI 코워커 인벤토리 확인 → **프로젝트 전용 커스텀 에이전트·스킬 체인 설계** → `AGENTS.md`(폴더 지침 정본, ≤500라인) + `CLAUDE.md`(`@AGENTS.md` 포인터) + `.claude/agents/`·`.codex/agents/` + `.moai/` 스캐폴드 생성 → **사용하면서 재귀적 자가 개선**

```
                        ┌───────────────────────┐
                        │  이번에 뭘 할 건가요?   │
                        └───────────┬───────────┘
                                    ▼
                          /project <지시>
                                    ▼
                     ┌──────────────────────────┐
                     │ 🪿 Cowork 셋업            │
                     │ 데스크톱 코워커 업무      │
                     │ 두 호스트의 지침 +        │
                     │ 커스텀 에이전트 +         │
                     │ 재귀적 자가 개선          │
                     └──────────────────────────┘
```

> **범위 주의**: 이 마켓플레이스는 비개발 AI 코워커 전용입니다. 개발-프로젝트 초기화(SPEC·DDD/TDD·품질 게이트)는 범위 밖입니다.

---

## AI 코워커 ('MoAI-Cowork, 모두의 코워크')

`modu-ai/moai-cowork` 마켓플레이스에서 필요한 AI 코워커를 설치합니다. 플러그인 목록과 역할의 정본은 `.claude-plugin/marketplace.json`이며, PM은 현재 앱에 실제로 설치·노출된 스킬을 확인해 프로젝트에 맞는 팀을 꾸립니다.

PM은 직접 일하지 않습니다. **누가 이 일에 맞는지 찾아 팀을 꾸리는 안내자** 역할만 합니다.

---

## 설치

Claude Cowork와 ChatGPT Work는 마켓플레이스 등록 권한과 경로가 다릅니다.

- **Claude Cowork**: Settings(또는 Plugins) → Marketplace → +에서 `modu-ai/moai-cowork`를 추가한 뒤 Plugins에서 **moai-pm**를 설치하세요.
- **ChatGPT Work**: 워크스페이스 관리자가 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져와야 합니다. 이용자는 권한이 부여된 뒤 Plugins에서 **moai-pm**를 찾아 Install plugin을 누르세요. 외부 서비스 연결은 별도 인증이 필요합니다.

> 처음엔 PM + 코워커만 설치해도 충분합니다. 나중에 다른 코워커가 필요해지면 셋업 중 **Gap Detection**이 감지해 설치를 안내한 뒤, 완료되면 "이어서 진행"이라고 말해 이어서 진행합니다.

> 앱별 정확한 클릭 경로와 잘 안 될 때 대처법은 [플러그인 설치와 관리](https://cowork.mo.ai.kr/plugins/install/)에 정리해 두었습니다.

## 사용법

```
/project
```

PM이 먼저 인사하고 무엇을 할지 묻습니다. "온라인 클래스 런칭 준비할 거야"처럼 답하면 프로젝트 전용 커스텀 에이전트와 스킬 체인을 설계해 `AGENTS.md`를 생성합니다.

### 서브커맨드

`/project`는 자연어 단일 진입 스킬입니다. 기본 동작은 `<자연어 지시>`로 진입하는 것이고, 아래 3가지 액션만 명시적 서브커맨드로 씁니다. 그 외(재개·카탈로그·상태·API 키)는 자연어로 요청하면 알아서 라우팅합니다.

| 커맨드 | 동작 |
|--------|------|
| `/project <지시>` | 진입 — 인터뷰 후 에이전트/체인 설계 + 생성. **기본 동작.** |
| `/project update` | 플러그인 업데이트 후 전수조사 → AGENTS.md·에이전트 재동기화 |
| `/project evolve` | 재귀적 자가 개선 수동 발동 |
| `/project doctor` | 환경 진단 |

### 재귀적 자가 개선

셋업이 끝난 뒤에도 PM의 역할은 끝나지 않습니다. 사용 중 아래 신호가 감지되면 에이전트와 `AGENTS.md`를 **자율적으로 개선**합니다:

- 같은 유형의 수정 요청이 2회 이상 반복될 때(톤·형식 불일치)
- 스킬 체인이 반복적으로 같은 단계에서 실패·우회할 때
- 플러그인 설치·제거로 인벤토리가 실제와 어긋날 때(inventory drift)
- 사용자가 직접 요청할 때(`/project evolve`)

개선은 최소 diff(최대 3개 파일) 단위로만 이루어지고, 변경 요지를 1-3줄로 보고한 뒤 적용하며, 이력은 `AGENTS.md` 말미 `<!-- evolution-log -->`에 기록됩니다. 자가 개선은 `AGENTS.md`와 `.claude/agents/`만 수정합니다.

---

## 산출물

| 파일 | 내용 |
|------|------|
| `./AGENTS.md` | 프로젝트 지침 정본(≤500라인) — 워크플로우 표 + 8개 HARD 규칙 + evolution-log |
| `./CLAUDE.md` | Claude용 포인터 — `@AGENTS.md` 임포트 한 줄(본문 복제 없음) |
| `./.claude/agents/*.md` · `./.codex/agents/*.toml` | 각 호스트용 프로젝트 전용 커스텀 에이전트(자가 개선 대상) |
| `./.moai/config.json` | 플러그인·커넥터·API 키 참조 |
| `./.moai/credentials.env` | API 키 안내(프로젝트 격리, GUIDANCE 전용 — 실제 값은 기록하지 않음) |

---

## 라이선스

Apache-2.0 · © 2026 modu-ai (email@mo.ai.kr) — 산출물은 이용자 소유([LICENSE-OUTPUT.md](../../LICENSE-OUTPUT.md))
