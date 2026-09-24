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

**[HARD] 질문은 불필요하게 나눠 내지 않는다.** 과거의 1-1/1-2/1-3 3연발 순차 호출은 폐기됐다. 한 라운드에는 현재 런타임의 질문 채널이 허용하는 수만큼 묶어 묻고, 남은 축은 다음 라운드에 확인한다.

### S1 — 일괄 진단 라운드 (구조화 질문 1회)

> **런타임별 상한**: Claude `AskUserQuestion` 최대 4질문 × 각 4옵션 · ChatGPT Work `request_user_input` **1질문 권장·3 초과 금지 × 각 2~3옵션**. 두 곳에서 같은 인터뷰를 돌린다면 **1질문 × 3옵션**을 공통 단위로 잡는다 — 잘려 나간 질문은 한쪽에서만 물어지고, 같은 프로젝트가 런타임에 따라 다른 깊이로 세워진다.

질문은 **고정 세트가 아니다.** 아래 풀에서 이번 프로젝트에 정보 이득이 큰 순으로 고르고, 현재 런타임의 한 호출 상한 안에서 배치한다.

| # | 축 | 형태 예시(현재 도구 상한에 맞게 조정) | 기본 선택지 예시 |
|---|---|---|---|
| ① | 업무 유형 | multiSelect 4옵션 | 사업 기획·전략 / 콘텐츠 제작 / 문서·행정 / 제품·연구 |
| ② | 주요 산출물 | 4옵션(+Other 자유입력) | 보고서·기획서 / 마케팅 콘텐츠 / 계약·공문 / 데이터·분석물 |
| ③ | 대상 독자·수신자 | 4옵션 | 경영진·투자자 / 고객·소비자 / 내부 팀·부서 / 공공기관·심사역 |
| ④ | 톤·형식 제약 | 4옵션 | 공식·격식체 / 캐주얼·대화체 / 산업 전문용어 / 제약 없음 |
| ⑤ | 산출물 포맷 | multiSelect 4옵션 | 한글(HWP) / PPTX·Word / 웹·노션·마크다운 / 이미지·영상 |
| ⑥ | 작업 주기·마감 | 4옵션 | 일회성 / 주간 반복 / 월간 반복 / 상시·수시 |
| ⑦ | 기존 자료 유무 | 4옵션 | 기존 산출물 있음 / 레퍼런스만 있음 / 브랜드 가이드 있음 / 백지에서 시작 |
| ⑧ | 반드시 피할 것 | 4옵션(+Other) | 과장·단정 표현 / 특정 경쟁사 언급 / 개인정보 노출 / 없음 |
| ⑨ | 배경·동기 (소크라테스 축) | 4옵션(+Other) | 신규 사업 착수 / 기존 업무 자동화 / 품질 편차 해소 / 인력 부족 보완 |

**슬롯 채우기 규칙 (HARD)**: 진입 발화·기존 `./AGENTS.md`·`.moai/context.md`에서 **이미 확보된 축은 질문 목록에서 제거**한다. 나머지는 현재 도구의 질문·옵션 상한에 맞춰 묻고, 초과한 축은 다음 라운드로 넘긴다. 두 런타임 공통 설계는 1질문 × 3옵션을 쓴다.

**작성 규칙**: 도구가 옵션별 `description`을 지원할 때만 설명을 붙인다. 문자열 옵션만 받으면 선택 결과가 분명한 짧은 문구를 쓴다. 첫 옵션에만 `(권장)` 라벨. 자유 서술은 도구가 제공하는 입력란을 쓴다.

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

라운드 수를 미리 정하지 않는다. **A등급 + 필수 B등급이 채워지면 종료**한다. 수집 결과는 메모리에 임시 저장되며, Phase 6에서 `AGENTS.md`에 직접 기록된다. 별도 `moai-profile.md`를 생성하지 않는다.

---

## Phase 2: Inventory — 활성 스킬 인벤토리 구성

### 2-1. 인벤토리 소스

**[HARD] 스캔 필터링 — moai-cowork 출처만 인정 (동적 도출)**: 설치 위치에는 다른 마켓플레이스 플러그인도 섞일 수 있다. 현재 호스트의 플러그인 목록과 접근 가능한 설치 파일을 대조해 **moai-cowork(modu-ai/moai-cowork) 출처 플러그인만** 인벤토리에 포함한다. 다른 호스트의 설치 파일이 보인다는 이유로 현재 호스트에서 사용할 수 있다고 표시하지 않는다.

**[HARD] 플러그인 집합은 하드코딩 화이트리스트가 아니라 동적으로 도출한다.** `moai-*` 접두어이면서 moai-cowork 마켓플레이스 출처인 플러그인을 `plugin.json` 스캔으로 식별한다. 마켓플레이스에 신규 플러그인이 추가되면 자동으로 포함된다. **카운트(플러그인 수·스킬 수)는 하드코딩하지 않는다** — `.claude-plugin/marketplace.json`이 로스터 정본이다.

**소스 A — 현재 호스트의 플러그인·스킬 목록**: 앱이 보여 주는 설치 플러그인과 이 세션에 노출된 스킬을 먼저 확인한다. 앱 목록에 없어도 파일이 있다는 이유만으로 설치되었다고 기록하지 않는다. 세션 스킬 목록이 제공되지 않으면 그 상태를 `미확인`으로 남긴다.

**소스 B — 접근 가능한 설치 파일**: 호스트가 제공한 설치 경로에서 `.claude-plugin/plugin.json` 또는 `.codex-plugin/plugin.json`을 찾아 이름·버전·출처를 읽는다. 폴더 깊이를 고정하지 않고 중복 매니페스트는 플러그인 루트로 합친다. 각 `skills/*/SKILL.md`의 frontmatter를 읽어 스킬과 소속 플러그인을 연결한다. 파일 도구가 없고 명령 실행만 가능하면 현재 OS의 파일 탐색 기능으로 같은 순서를 수행한다. 특정 셸·`$HOME`·Unix 경로를 전제로 하지 않는다.

**[HARD] 0개 또는 불일치는 조사 대상이다.** 사용자가 설치했다고 말하거나 세션에 MoAI 스킬이 보이는데 파일 검사 결과가 0개라면 빈 인벤토리로 진행하지 않는다. 호스트 목록과 경로를 다시 확인하고, 접근할 수 없는 출처는 `미확인`으로 기록한다. 설치 파일 존재, 세션 노출, 실제 호출 가능은 각각 별도 상태로 보관한다.

### 2-2. `.moai/config.json` 인벤토리 스냅샷 스키마

**[HARD] 아래 네 필드는 없으면 후속 기능이 통째로 죽는다.** `plugins_installed`의 **버전**과 `skills_available`의 **digest**가 없으면 `update`가 "변경된 스킬"을 영영 검출하지 못하고, `template_version`·`hard_block_digests`가 없으면 HARD 블록 재동기화가 사용자 편집과 구 템플릿을 구분하지 못한다(`update-protocol.md` §4-1). `sensitivity`가 없으면 맞춤법 단계가 fail-open 된다. `coverage`가 없으면 재개(resume) 시 이미 답한 축을 **다시 묻게 된다** — 커버리지 표(SKILL.md §Socratic Interview)의 24축 상태를 그대로 저장한다.

```json
{
  "scanned_at": "2026-07-11T00:00:00+09:00",
  "plugins_installed": { "moai-pm": "1.5.0", "moai-coworker": "1.2.0" },
  "skills_available": {
    "content-blog": { "plugin": "moai-coworker", "digest": "sha256:..." },
    "ai-slop-reviewer": { "plugin": "moai-coworker", "digest": "sha256:..." }
  },
  "template_version": "1.5.0",
  "hard_block_digests": { "6. 한국어 품질 체인 (HARD)": "sha256:...", "...": "..." },
  "sensitivity": "public | sensitive | unknown",
  "coverage": {
    "A": { "1": "충족", "2": "충족", "3": "유예" },
    "H": { "22": "충족", "23": "미확인", "24": "유예" }
  },
  "confidence": { "moai-pm": "HIGH" }
}
```

### 2-3. Phase 1 답변 기반 매칭

| 업무 유형 | 우선 코워커(플러그인) |
|----------|------------|
| 사업 기획·전략 | 코워커(business-* 스킬군) |
| 콘텐츠 제작 | 마케터(content-*, marketing-* 스킬군) |
| 문서·행정 | 사무관(office-*), 법무(legal-*) |
| 제품·연구 | 코워커(spec/ux 스킬군), 튜터(education-* 스킬군) |
| 이커머스 | 셀러(commerce-* 스킬군) |
| 출판·원고·웹툰·IP | 작가(book-*), 스토리(story-*) |
| 디자인 핸드오프·브랜드 | 디자이너(cd-*, moai-domain-design 스킬군) |

라우터 허브는 project 스킬(`/project` 진입). 실무/콘텐츠/사무 도메인은 코워커로 수렴하며, 스토리는 `moai-story`, 출판은 `moai-writer`, 디자인은 `moai-designer`로 분기된다. `ai-slop-reviewer`는 `moai-coworker`, `korean-humanize`는 `moai-writer` 소속이다. 각각 설치·노출 상태를 확인한 뒤 텍스트 후처리 체인에 넣는다.

---

## Phase 3: 스킬 체인 설계 (핵심)

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

스킬군 → 소속 플러그인 매핑은 **`.claude-plugin/marketplace.json` 로스터를 정본으로 삼는다** — 하드코딩 매핑 테이블을 유지하지 않는다(신규 플러그인 추가 시 자동 반영). 참고 패턴: `business-*`/`content-*`/`marketing-*`/`office-*`/`legal-*`/`finance-*`/`education-*`/`media-*`/`general-*` → `moai-coworker`; `commerce-*` → `moai-seller`; `book-*` → `moai-writer`; `story-*` → `moai-story`; `cd-*`/디자인 도메인 → `moai-designer`; 개발 도메인 스킬 → `moai`; `project`(PM 허브) → `moai-pm`.

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

현재 런타임의 질문 채널로 1질문, 3옵션을 제시한다: 승인(권장) / 수정 / 취소. 질문할 수 없으면 설계를 확정하지 않고 결정을 기다린다.

---

## Phase 6: 지침 생성 (AGENTS.md 정본 + CLAUDE.md 포인터)

`references/templates/AGENTS.md.tmpl`을 로드하여 변수를 치환하고 `./AGENTS.md`에 쓴다. 이어서 `references/templates/CLAUDE.md.tmpl`을 **치환 없이 그대로** `./CLAUDE.md`에 복사해 `@AGENTS.md` 포인터를 만든다(본문 복제 금지). 상세 변수 치환 테이블·생성 절차·포인터 규칙은 `agentsmd-generator.md` 참조. 생성 원칙: AGENTS.md ≤500라인, 스킬 체인 최대 10개, 8개 HARD 규칙 블록 항상 포함, UTF-8/LF/한국어.

---

## Phase 7: 커스텀 에이전트 생성

Phase 3-6 결과를 바탕으로 커스텀 에이전트를 **Claude용 `.claude/agents/*.md`(markdown+YAML frontmatter)와 Codex용 `.codex/agents/*.toml`(TOML: `name`·`description`·`developer_instructions`, `model`·`sandbox_mode` 선택) 양쪽**으로 생성한다. 절차·frontmatter·7-step 루프는 project 스킬 SKILL.md §Custom Agent & Skill-Chain Design 참조.

---

## Phase 8: API 키 / 커넥터 + 첫 실행 안내

Phase 2에서 선택된 플러그인이 API 키를 요구하면 해당 서비스의 현재 인증 방식을 확인해 등록을 안내한다. 공식 MCP가 계정 연결을 제공하면 앱 안에서 연결·인증한다.

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

1. `.moai/cache/init-progress.json` 존재 확인(없으면 "저장된 진행 상태가 없습니다. `/project`로 새로 시작하세요.")
2. `init-progress.json` 로드(Phase 1-3 결과 복원)
3. Phase 2 Inventory 재실행(설치 확인)
4. Phase 4 Gap Detection 재검증(여전히 누락 시 §4-3의 런타임별 선택지 제시, 0건이면 Phase 5로 진행)
5. Phase 5 이후는 정상 흐름과 동일

---

## API 키 관리 — "API 키 설정할래" (자연어)

사용자가 "API 키 설정할래"·"키 등록할래"라고 하면 Phase 8 안내 흐름이 6개 API 키를 조회·변경·추가·삭제한다.

---

## 구조화 질문 제약 준수 요약 (런타임별)

**[HARD] 호출 수가 아니라 라운드 수를 센다.** 한 라운드는 질문 여러 개를 묶은 **1회 호출**이다. 질문 1개당 1회 호출하는 분할 방식은 금지한다.

| Phase | 호출 | Claude — 질문 / 옵션 | ChatGPT Work — 질문 / 옵션 |
|-------|------|----------------------|---------------------------|
| Phase 1 · S1 일괄 진단 | 1 | 최대 4 / 각 ≤4 | **1 (최대 3) / 각 2~3** |
| Phase 1 · 후속 라운드(커버리지 미충족 시) | 0-N (상한 없음) | 최대 4 / 각 ≤4 | **1 (최대 3) / 각 2~3** |
| Phase 4 Gap Detection(조건부) | 0-1 | 1 / 4 | 1 / **3** |
| Phase 5 설계 확인 | 1 | 1 / 3 | 1 / 3 |
| Phase 8 API 키(조건부) | 0-1 | 1-2 / 최대 4 (multiSelect) | 1-2 / **3** (multiSelect 없음 — 필요하면 라운드를 나눈다) |

모든 Phase에 `Other`가 자동으로 붙는다(양쪽 런타임 공통). 직접 넣지 않는다.

- 정상 경로(맥락 충분): **총 2회 호출** — S1 + Phase 5 확인.
- 최대 경로: S1 + S2 반복 + Gap + 확인 + API 키. S2 반복이 2회를 넘으면 종료 선택지를 함께 제시한다.
- **[HARD] ChatGPT Work에서는 라운드가 늘어난다.** 한 화면에 4질문을 담을 수 없으므로 같은 커버리지를 채우려면 호출 수가 더 필요하다. **이것을 이유로 질문을 줄이지 않는다** — 커버리지가 종료 조건이지 호출 수가 아니다.
- **[HARD] 현재 세션의 질문 도구를 먼저 확인한다.** `request_user_input_async`가 노출된 세션은 Default 모드에서도 질문할 수 있다. 응답은 후속 사용자 메시지로 오며, 도구 호출 직후의 반환값을 답으로 해석하지 않는다. 질문 도구가 전혀 없으면 필요한 입력을 명시한 blocker를 반환한다. 절차는 `../SKILL.md` §ChatGPT Work 참조.
- 모든 질문은 **현재 세션에 노출된 구조화 질문 도구**로 묻는다. 도구의 실제 스키마와 질문 수·선택지 수 상한을 따른다. 자유 서술 질문·텍스트 대화형 심화 인터뷰는 사용하지 않는다(`Other` 옵션이 자유입력을 흡수한다).
