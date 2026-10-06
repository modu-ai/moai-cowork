# init-protocol.md — `/project` 초기화 전체 플로우

## 개요

`/project`는 모두의 코워크 프로젝트를 초기화하고, 사용자의 업무 워크플로우를 인터뷰한 뒤, **스킬 체이닝 + 프로젝트 전용 커스텀 에이전트 기반 AGENTS.md**(폴더 지침 정본)와 이를 불러오는 `CLAUDE.md` 포인터를 생성한다.

**현재 상태**:
- Phase 2 인벤토리는 설치된 플러그인을 **동적으로 도출**(plugin.json 스캔)하여 신규 플러그인을 자동 포함한다.
- Phase 4 Gap Detection: 체인 스킬 ↔ 인벤토리 대조 → 누락 감지 → 설치 안내 → Re-entry.
- 설치 완료 후 사용자가 "이어서 진행"·"설치 완료"라고 하면 저장된 진행 상태에서 재개한다(자연어 단일 경로).
- 글로벌 프로필 시스템은 사용하지 않는다(이름·회사·역할 재질문 없음).
- 생성 `AGENTS.md`에 8개 HARD 규칙 블록이 고정 포함된다.

---

## 전체 플로우

```
/project
    ↓
Phase 1: 워크플로우 인터뷰 (맥락 충분까지 수집)
    ↓
Phase 2: Inventory — 설치된 플러그인·스킬 인벤토리 구성
    ↓
Phase 3: 스킬 체인 설계 (산출물별 파이프라인)
    ↓
Phase 4: Gap Detection — 누락 플러그인/스킬 감지 + 설치 안내
    ↓ (누락 0건이거나 체인 조정 선택을 처리한 뒤)
Phase 5: 설계 확인 (현재 런타임의 질문 채널)
    ↓
Phase 6: 지침 생성 (AGENTS.md.tmpl 기반 AGENTS.md ≤500라인 + CLAUDE.md 포인터)
    ↓
Phase 7: 커스텀 에이전트 생성 (.claude/agents/*.md + .codex/agents/*.toml)
    ↓
Phase 8: API 키 / 커넥터 + 첫 실행 안내
```

---

## Phase 1: 워크플로우 인터뷰 (커버리지 기반 · 라운드 무제한)

사용자의 **이 프로젝트 맥락**만 수집한다. 이름·회사·역할 같은 **글로벌 프로필 정보는 묻지 않는다**.

질문 채널·상한·자유 입력·응답 대기는 `question-protocol.md`를 따른다. 현재 호스트·Project 종류는 `host-capabilities.md`로 먼저 확인한다.

### S1 — 필요한 맥락 확인

기존 자료와 사용자 발화에서 목적·산출물·독자·문체·업무 방식·품질·자산·제약을 읽는다. 이번 업무에 필요한 누락만 질문한다. 선택형으로 충분하면 현재 스키마에 맞는 옵션을 제공하고, 원문·구체적인 사실·자유 서술이 필요하면 지원 채널로 받는다. 이미 받은 답을 질문에서 제외한다. 호출당 질문 수나 옵션 수를 두 호스트의 공통 상수로 정하지 않는다.

### S2 — 보강 라운드 (조건부, 구조화 질문 추가 호출)

**발동 조건** — 하나라도 해당할 때만 실행한다:

| 조건 | 판정 신호 |
|---|---|
| (a) 필수 축 공백 | A등급 + 필수 B등급 중 미확보 항목 존재 |
| (b) 저신뢰 응답 | `Other` 선택, 모호한 자유입력 |
| (c) 답변 상충 | 예: 산출물=공문인데 톤=캐주얼 |
| (d) 슬롯 초과 | S1의 현재 도구 상한에 못 담은 필수 축이 남음 |

해당 없으면 **S2를 건너뛰고 즉시 Phase 2로 진행**한다. 실행할 때도 현재 도구의 상한 안에서 부족분을 묶어 배치한다. S2가 2회를 넘어가면 그 라운드에 「지금 아는 것으로 진행」 옵션을 함께 넣어 사용자가 종료할 수 있게 한다.

### 종료 판정

라운드 수를 미리 정하지 않는다. **A등급 + 필수 B등급이 채워지면 종료**한다. 실제 답·출처·유예 사항은 `context.answers`·`context.questions`와 `.moai/context.md`에 보존하고, Phase 6에서 공통 지침과 연결한다. 별도 `moai-profile.md`를 생성하지 않는다.

---

## Phase 2: Inventory — 활성 스킬 인벤토리 구성

### 2-1. 인벤토리 소스

**[HARD] 스캔 필터링 — moai-cowork 출처만 인정 (동적 도출)**: 설치 위치에는 다른 마켓플레이스 플러그인도 섞일 수 있다. 현재 호스트의 플러그인 목록과 접근 가능한 설치 파일을 대조해 **moai-cowork(modu-ai/moai-cowork) 출처 플러그인만** 인벤토리에 포함한다. 다른 호스트의 설치 파일이 보인다는 이유로 현재 호스트에서 사용할 수 있다고 표시하지 않는다.

**[HARD] 플러그인 집합은 하드코딩 화이트리스트가 아니라 동적으로 도출한다.** `moai-*` 접두어이면서 moai-cowork 마켓플레이스 출처인 플러그인을 `plugin.json` 스캔으로 식별한다. 마켓플레이스에 신규 플러그인이 추가되면 자동으로 포함된다. **카운트(플러그인 수·스킬 수)는 하드코딩하지 않는다** — 현재 호스트 노출 목록이 실제 사용 가능 상태의 근거다. 접근 가능한 marketplace 또는 내부 `skill-catalog.json`은 추천 목록이다.

**소스 A — 현재 호스트의 플러그인·스킬 목록**: 앱이 보여 주는 설치 플러그인과 이 세션에 노출된 스킬을 먼저 확인한다. 앱 목록에 없어도 파일이 있다는 이유만으로 설치되었다고 기록하지 않는다. 세션 스킬 목록이 제공되지 않으면 그 상태를 `미확인`으로 남긴다.

**소스 B — 접근 가능한 설치 파일**: 호스트가 제공한 설치 경로에서 루트 `plugin.json` 또는 호환 `.claude-plugin/plugin.json`·`.codex-plugin/plugin.json`을 찾아 이름·버전·출처를 읽는다. 폴더 깊이를 고정하지 않고 중복 매니페스트는 플러그인 루트로 합친다. 각 `skills/*/SKILL.md`의 frontmatter를 읽어 스킬과 소속 플러그인을 연결한다. 파일 도구가 없고 명령 실행만 가능하면 현재 OS의 파일 탐색 기능으로 같은 순서를 수행한다. 특정 셸·`$HOME`·Unix 경로를 전제로 하지 않는다.

**[HARD] 0개 또는 불일치는 조사 대상이다.** 사용자가 설치했다고 말하거나 세션에 MoAI 스킬이 보이는데 파일 검사 결과가 0개라면 빈 인벤토리로 진행하지 않는다. 호스트 목록과 경로를 다시 확인하고, 접근할 수 없는 출처는 `미확인`으로 기록한다. 설치 파일 존재, 세션 노출, 실제 호출 가능은 각각 별도 상태로 보관한다.

### 2-2. `.moai/config.json` 인벤토리 스냅샷 스키마

버전 2 계약은 `references/templates/config.schema.json`을 따른다. 기존 프로젝트의 사용자 값·`plugins_installed`·`template_version`·`hard_block_digests`·민감도·커버리지는 이관 시 보존한다. `skills_available` 키는 실제 `plugin:skill`이며, 버전은 `metadata.version`에서 읽고 digest는 실제 본문에서 계산한다. 설치·노출·호출은 `installed/exposed/callable`, 추천 목록은 `catalog`, 미확인은 `unknown`으로 구분한다.

`context.answers`에 실제 값·출처·검증 여부, `context.questions`에 프로젝트에서 도출한 질문 ID·영향 단계·상태를 저장한다. 고정 24축이나 선택되지 않은 값을 만들지 않는다. `workflows`에는 선행 단계·소유 스킬·쓰기 경로·계정 참조·완료 기준·실행 상태·증거를 둔다. `host`에는 현재 관찰한 Project 종류·실행 위치·분업 기능과 권한·실제 한도를 기록한다.

파일을 만든 뒤 `scripts/project_contract.py validate --config <설정 경로> --root <작업 폴더>`로 계약·참조·의존성을 검사한다. 이 검사는 실제 호스트 적용·업무 실행을 대신하지 않는다.

### 2-3. Phase 1 답변 기반 매칭

| 업무 유형 | 우선 코워커(플러그인) |
|----------|------------|
| 프로젝트 업무 | 후보 찾기 |
|---|---|
| 사업·문서·디자인·법무·재무·교육·커머스·창작 | 현재 노출된 스킬의 실제 목적·입력·출력·필요 MCP를 읽고 선택 |

접두어만으로 소속을 추정하지 않는다. 내부 카탈로그의 qualified ID와 현재 인벤토리를 대조하고, `expert-contract.md`로 프로젝트 전문가를 배치한다. 한국어 검수는 실제 노출 상태와 문서 민감도를 따른다.

### 3-1. 체인 구성 규칙

```
[기획/분석 스킬] → [생성 스킬] → [포맷 변환/미디어 스킬] → ⟨한국어 감사⟩
```

한국어 텍스트 산출물은 **최종 검수로 종료**한다. 인벤토리에 있고 실제 호출 가능한 경우 `moai-coworker:ai-slop-reviewer` → `moai-writer:korean-spell-check`(공개 문서만) → `moai-writer:korean-humanize` 순서로 쓴다. 없으면 해당 단계를 건너뛰고 원문·최종본의 의미, 수치, 인용을 직접 대조한다. 사용하지 못한 단계를 기록하고, 필요한 전문 스킬은 Gap Detection으로 넘긴다. 비텍스트는 한국어 감사 단계를 생략한다. 정본은 `cowork-setup.md` §3이다.

### 3-2. 체인 프리셋 테이블

상세 체인 프리셋(주요 산출물별 권장 체인)은 `cowork-setup.md` §3을 참조한다(단일 소스 — 중복 유지 안 함).

### 3-3. 체인 요약 포맷

Phase 5(확인 단계)에서 사용자에게 보여줄 요약:

```
이 프로젝트의 실행 체인 설계

[주 산출물 1] 사업계획서(PPT)
  체인: consult-strategy → doc-pptx → ⟨한국어 감사⟩
  트리거 예시: "사업계획서 만들어줘"
```

---

## Phase 4: Gap Detection — 누락 플러그인/스킬 감지

### 4-1. 누락 감지 알고리즘

```
for each skill in chain_skills:
    if skill not in inventory.skills_available:
        missing_skills.append(skill)
        missing_plugin = SKILL_PLUGIN_MAP[skill]
        missing_plugins.add(missing_plugin)
```

### 4-2. 스킬 → 플러그인 매핑

소속은 현재 인벤토리의 `plugin:skill`에서 읽는다. 내부 `skill-catalog.json`의 후보와 대조하되 추천 목록을 설치 증거로 쓰지 않는다. 이름 패턴으로 다른 플러그인에 배정하지 않는다.

### 4-3. 누락 발견 시 질문 채널로 선택지 제시

```
"체인에 필요한 스킬이 설치되지 않은 플러그인에 포함돼 있습니다."

누락 스킬: [skill-A] → [moai-X] 플러그인 필요

옵션:
  1. (권장) 설치 안내 받기 + 설치 후 재개
     → 앱 화면의 설치 절차를 안내하고, 완료 후 "이어서 진행"으로 재개합니다.
     → 현재 진행 상태(.moai/cache/init-progress.json)는 보존됩니다.
  2. 누락 스킬 제외하고 진행
  3. 대체 스킬로 변경
  4. 중단
```

질문 도구가 3개 선택지만 허용하면 먼저 **설치 안내 / 체인 조정 / 중단**을 묻는다. 첫 답변이 체인 조정일 때에만 **누락 스킬 제외 / 대체 스킬 선택**을 다시 묻는다. 첫 답변의 `중단`은 즉시 중단이며, 후속 질문의 `대체 스킬 선택`과 혼동하지 않는다. 사용자의 선택 없이 어느 경로도 실행하지 않는다.

### 4-4. 옵션 1 선택 시: 설치 안내 흐름

```
1. 누락 플러그인별 데스크톱 앱 설치 안내:
   - Claude Cowork: Settings(또는 Plugins) → Marketplace → +에서 `modu-ai/moai-cowork`를 추가한 뒤 Plugins 화면에서 해당 플러그인을 설치한다.
   - ChatGPT Work: 워크스페이스 관리자에게 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져오고 해당 플러그인의 설치 정책을 확인하도록 안내한다. 사용자는 워크스페이스에서 이용 가능해진 플러그인을 설치한다.

2. .moai/cache/init-progress.json 저장

3. 안내: "'이어서 진행' 또는 '설치 완료' 발화"
```

`.moai/cache/` 디렉터리가 없으면 현재 호스트에서 사용 가능한 파일 도구로 생성한다.

### 4-5. `init-progress.json` 스키마

```json
{
  "started_at": "2026-07-11T14:30:00+09:00",
  "phase_completed": 3,
  "interview_answers": { "work_type": ["사업 기획·전략"] },
  "chain_design": [
    { "deliverable": "사업계획서(PPT)", "chain": ["consult-strategy", "doc-pptx"], "review": "⟨한국어 감사⟩: 호출 가능한 스킬과 원문·전달본 대조" }
  ],
  "missing_skills": [],
  "missing_plugins": []
}
```

### 4-6. 체인 조정 선택 시

4개 선택지를 지원하는 도구에서는 원래 옵션 2(제외)와 옵션 3(대체)를 각각 처리한다. 3개 이하를 지원하는 도구에서는 첫 질문의 `체인 조정`만으로 처리하지 않고, 후속 질문에서 `누락 스킬 제외` 또는 `대체 스킬 선택`을 받은 뒤 처리한다.

- **제외**: `missing_skills`에 해당하는 체인 단계를 제거하고 Phase 5로 진행하며, `AGENTS.md`의 해당 체인에 미설치 주석을 삽입한다.
- **대체**: `inventory.skills_available`에서 유사 기능 스킬을 검색해 재설계 후 Phase 5로 진행한다.
- **중단**: 현재 진행을 멈추고 어떤 체인도 수정하지 않는다.

### 4-7. 누락 0건이면

즉시 Phase 5 Confirm으로 진행한다.

---

## Phase 5: 설계 확인

설계를 짧게 보여준다. 기존 요청이 설정 생성을 승인하고 필수 입력이 충분하면 진행한다. 빠진 결정이나 충돌이 있을 때만 `question-protocol.md`에 따라 해당 부분을 확인한다.

---

## Phase 6: 지침 생성 (AGENTS.md 정본 + CLAUDE.md 포인터)

`references/templates/AGENTS.md.tmpl`을 로드하여 변수를 치환하고 `./AGENTS.md`에 쓴다. 이어서 `references/templates/CLAUDE.md.tmpl`을 **치환 없이 그대로** `./CLAUDE.md`에 복사해 `@AGENTS.md` 포인터를 만든다(본문 복제 금지). 상세 변수 치환·byte 예산·포인터 규칙은 `agentsmd-generator.md` 참조. 파일 생성 다음에는 `host-capabilities.md`의 Project 적용·새 대화 읽기 확인을 수행한다. 생성 원칙: AGENTS.md ≤500라인과 실제 호스트 byte 한도, 본문에는 주요 스킬 체인 최대 10개(전체 정의는 config.json에 보존), 8개 HARD 규칙 블록 항상 포함, UTF-8/LF/한국어.

---

## Phase 7: 커스텀 에이전트 생성

Phase 3-6 결과를 바탕으로 커스텀 에이전트를 **Claude용 `.claude/agents/*.md`(markdown+YAML frontmatter)와 Codex용 `.codex/agents/*.toml`(TOML: `name`·`description`·`developer_instructions`, `model`·`sandbox_mode` 선택) 중 현재 지원되는 형식**으로 생성한다. 호출 불가 환경은 부모가 같은 전문가 계약을 실행한다. 절차·frontmatter·7-step 루프는 project 스킬 SKILL.md §Custom Agent & Skill-Chain Design 참조.

---

## Phase 8: API 키 / 커넥터 + 첫 실행 안내

Phase 2에서 선택된 플러그인이 API 키를 요구하면 해당 서비스의 현재 인증 방식을 확인해 등록을 안내한다. 공식 MCP가 계정 연결을 제공하면 앱 안에서 연결·인증한다.

아래는 연결 예시다. 실제 필요한 연결은 선택한 워크플로우·매니페스트·서버 README에서 확인하고, 계정 파일과 회전 토큰은 `account-bindings.md`에 따라 프로젝트별로 배선한다.

| # | 서비스 | 환경변수 | 용도 | 발급처 |
|---|--------|---------|------|--------|
| 1 | 공공데이터포털 | `DATA_GO_KR_API_KEY` | 공공데이터/KOSIS/KCI | data.go.kr |
| 2 | KIPRIS Plus | `KIPRIS_API_KEY` | 특허 검색 | plus.kipris.or.kr |
| 3 | 국가법령정보 | `KOREAN_LAW_OC` | 법령/판례 | law.go.kr |
| 4 | Google Gemini | `GEMINI_API_KEY` | 이미지 프롬프트 | ai.google.dev |
| 5 | Higgsfield | API 키 없음 | Claude는 공식 MCP 커넥터 `https://mcp.higgsfield.ai/mcp`, ChatGPT는 공식 Higgsfield 플러그인에서 계정 연결 | [공식 연결 안내](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent) |
| 6 | ElevenLabs | `ELEVENLABS_API_KEY` | media-audio-gen(TTS) | elevenlabs.io |

API 키가 필요한 서비스의 안내 위치: `./.moai/credentials.env`(프로젝트 격리, GUIDANCE 전용 — 실제 값은 절대 기록하지 않음). Higgsfield의 계정 인증을 API 키 입력으로 안내하지 않는다.

첫 실행 안내는 Phase 3에서 설계된 체인 중 상위 3개를 예시로 제시한다. 전체 코워커 목록이 궁금하면 "어떤 코워커 있어?", 현재 상태는 "지금 상태 어때?"로 물으면 안내한다.

---

## Re-entry: 설치 완료 후 진행 재개

| 트리거 | 처리 |
|--------|------|
| "이어서 진행" / "설치 완료" / "다시 진행" | 자연어 → resume 흐름 자동 트리거(유일한 재개 경로) |

### 복원 흐름

1. `.moai/cache/init-progress.json` 또는 `.moai/config.json`·`.moai/context.md`를 확인한다. 캐시가 없어도 저장된 실제 맥락이 있으면 그것을 복원하고 미확인 단계만 진행한다.
2. 존재하는 상태 파일에서 실제 답·질문 상태·체인·호스트 관측을 복원한다. 없는 항목은 미확인으로 남긴다.
3. Phase 2 Inventory 재실행(설치 확인)
4. Phase 4 Gap Detection 재검증(여전히 누락 시 §4-3의 런타임별 선택지 제시, 0건이면 Phase 5로 진행)
5. Phase 5 이후는 정상 흐름과 동일

---

## API 키 관리 — "API 키 설정할래" (자연어)

사용자가 "API 키 설정할래"·"키 등록할래"라고 하면 현재 작업에 필요한 연결만 확인하고 대상 계정 참조와 인증 경로를 안내한다. 키 값은 대화·지침·설정·로그에 기록하지 않는다. 이미 연결된 계정과 변경 권한은 재사용한다.

---

## 구조화 질문 제약 준수 요약 (런타임별)

**[HARD] 질문은 필요와 현재 도구 스키마로 구성한다.** 여러 질문을 묶을 수 있으면 관련 질문을 묶고, 자유 입력·파일 자료가 필요하면 지원 채널을 사용한다. 호출 횟수나 빈 슬롯을 목표로 삼지 않는다. 정본은 `question-protocol.md`다.

- 현재 노출된 도구의 질문·선택지 개수, 자유 입력, 파일 첨부 지원을 먼저 확인한다.
- 관련 질문을 묶되 빈 슬롯을 채우려고 질문을 만들지 않는다. 주관식 자료가 필요하면 지원하는 입력 경로를 사용한다.
- 비동기 도구 반환·기본 선택·시간 경과는 답변이 아니다. 답이 필요한 작업은 대기 상태로 보존하고 독립 작업을 진행한다.
- 기존 요청이 설계·변경을 이미 승인하면 확인 질문을 반복하지 않는다.
- 질문 채널이 없을 때는 상위 호스트의 대체 규칙을 따르며, 필수 입력이 없으면 해당 단계의 blocker를 반환한다.
