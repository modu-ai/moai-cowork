# Contributing to moai-cowork-plugins

## 새 플러그인 추가

1. 플러그인 디렉토리를 `moai-{name}/` 형식으로 생성합니다.
2. `.claude-plugin/plugin.json`을 작성합니다 (name, version, description, author, keywords, license 필수).
3. `skills/` 디렉토리에 스킬을 추가합니다.
4. `README.md`를 작성합니다 (스킬 테이블, 사용 예시 포함).

```
moai-{name}/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── {skill-name}/
│       └── SKILL.md
├── agents/          (선택)
├── .mcp.json        (선택)
└── README.md
```

## SKILL.md 작성 규칙

모든 SKILL.md는 YAML frontmatter로 시작해야 합니다:

```yaml
---
name: skill-name
description: >
  스킬 설명 — 핵심 기능과 주요 용어를 포함합니다.
user-invocable: true
metadata:
  version: "1.0.0"
  status: "draft"   # draft | active | stable
  updated: "YYYY-MM-DD"
---
```

- `name`: 스킬 디렉토리명과 일치해야 합니다.
- `description`: 한국어로 작성. 트리거 키워드를 포함하면 자동 라우팅에 유리합니다.
- `status`: `draft` (작성 중), `active` (사용 가능), `stable` (검증 완료)

## 에이전트 정의 규칙

`agents/` 디렉토리의 `.md` 파일은 frontmatter를 포함해야 합니다:

```yaml
---
name: agent-name
description: 에이전트 역할 설명. 공유 호출 가능 여부를 명시합니다.
model: haiku | sonnet | opus
---
```

- 가벼운 분류·판정 작업: `haiku`
- 문서 생성·분석 작업: `sonnet`
- 복잡한 전략 수립: `opus`

## PR 프로세스

1. `feature/{plugin-name}` 브랜치를 생성합니다.
2. 스킬과 README를 작성한 뒤 커밋합니다.
3. PR을 열고 다음 항목을 체크리스트로 확인합니다:
   - [ ] SKILL.md frontmatter 완성
   - [ ] `status` 값이 정확히 설정됨
   - [ ] README.md에 스킬 테이블과 사용 예시 포함
   - [ ] plugin.json 작성 완료
4. 리뷰어 1명 이상의 승인 후 merge합니다.

## 코드 스타일

- 파일명: `kebab-case`
- 스킬 ID: `kebab-case` (디렉토리명과 동일)
- 설명: 한국어 (description 필드)
- 주석: 한국어 또는 영어 모두 허용
