# project 스킬 references — 전체 인덱스

`plugins/moai-pm/skills/project/references/`의 레퍼런스 파일 인덱스. project 스킬은 Claude Cowork와 ChatGPT Work 데스크톱의 비개발 작업을 설정한다.

## 진입점

- 진입점은 `/project <자연어 지시>`. 소크라테스 인터뷰 → 플러그인 인벤토리 스캔 → 커스텀 에이전트/스킬 체인 설계 → `AGENTS.md`(폴더 지침 정본, ≤500라인) + `CLAUDE.md`(`@AGENTS.md` 포인터) + `.claude/agents/` + `.moai/` 스캐폴드 생성.
- 자연어 의도를 판별할 수 없으면 현재 런타임에 노출된 질문 도구로 확인한다(`router.md`). 도구가 없으면 필요한 입력을 명시한다.

## 파일 인덱스

| 파일 | 역할 |
|------|------|
| `router.md` | 산출물과 현재 노출된 스킬을 대조하는 라우팅·모호성 해소·복합 요청·검증 깊이 연동 |
| `cowork-setup.md` | 코워커·작가 8-Phase 정본(역할 자동 감지·체인 프리셋·커스텀 에이전트 생성·인용 가드) |
| `designer-setup.md` | 디자인 자산 5-Phase 서브 프로토콜 |
| `init-protocol.md` | 인터뷰 질문 스키마·인벤토리 스캔·Gap Detection·재개(Re-entry) 상세 |
| `context-collector.md` | 맥락 등급(A/B/C)·커버리지 기반 라운드 설문 플로우·모호성 감지·맥락 적용 규칙 |
| `agentsmd-generator.md` | AGENTS.md 변수 치환·500라인 예산·HARD 블록 보존·CLAUDE.md 포인터 규칙·레거시 마이그레이션 |
| `execution-protocol.md` | 스킬 체인 순차 실행·검증 깊이 사다리·검색 스케일링 |
| `evaluation-protocol.md` | 5차원 산출물 평가(정확성·완전성·실용성·톤·도메인) |
| `quality-evaluator.md` | 결정론적 품질 게이트(파일 유효성·마크다운 렌더링·AI 작문 패턴·근거 검증) |
| `diagnostic-protocol.md` | 환경 진단(`/project doctor`) · 상태 조회(자연어) |
| `update-protocol.md` | 플러그인 업데이트 동기화(`/project update` — 전수조사·세션 신호 분석·동기화·검증·롤백) |
| `templates/AGENTS.md.tmpl` | 생성 AGENTS.md 정본 템플릿(Desktop 변형, 8개 HARD 블록 고정) |
| `templates/CLAUDE.md.tmpl` | 생성 CLAUDE.md 포인터 템플릿(`@AGENTS.md` 임포트, 변수 없음) |

## 패밀리 로스터

플러그인/스킬 카운트는 이 인덱스에 하드코딩하지 않는다. `.claude-plugin/marketplace.json`에서 배포 로스터를 읽고, 현재 런타임에 실제 노출된 스킬과 대조한다. 설치 경로 하나만으로 사용 가능하다고 판정하지 않는다.

## 아키텍처

```
계층 1: 플러그인(Read-Only) — AI 코워커 플러그인(moai-pm 허브 포함)
         ↑ Gap Detection: 현재 호스트의 설치·노출 상태와 배포 로스터 대조
         ↑ 누락 플러그인 감지 → 설치 안내 → "이어서 진행" 재개
계층 2: ./AGENTS.md(정본) — 프로젝트별 맞춤형 페르소나 + 스킬 체인 정의
         + ./CLAUDE.md — @AGENTS.md 임포트 포인터(Claude가 정본을 자동 로딩)
         + ./.claude/agents/ · ./.codex/agents/ — 지원 형식별 프로젝트 에이전트
         + ./.moai/ — 설정, 컨텍스트, API 키 가이던스, evolution/
         + 호스트별 메모리 — 실제 제공되는 경우에만 사용
```

단일 자가 개선 모델(재귀적 자가 개선, project 스킬 SKILL.md §Recursive Self-Improvement)만 사용한다 — 강제 점수화·별도 지표 파일을 요구하는 무거운 다단계 모델은 채택하지 않는다.
