# moai-core

MoAI 코어 플러그인 — 도메인 AI 라우터, 초기화, 자가학습 엔진.

84개 도메인 하네스를 자연어로 트리거하는 중앙 허브입니다. `/moai init`으로 프로젝트 맞춤형 `CLAUDE.md`를 생성하고, `/moai catalog`로 전체 스킬 목록을 조회합니다.

## 스킬

| 스킬 | 설명 | 상태 |
|------|------|:----:|
| [moai](./skills/moai/) | 도메인 AI 라우터 — `/moai init`, `/moai catalog`, `/moai status` 커맨드 처리 및 84개 도메인 자동 감지 | ✅ 완성 |

## 에이전트

| 에이전트 | 모델 | 설명 |
|---------|:----:|------|
| quality-evaluator | Haiku | 전 플러그인에서 공유 호출 가능한 범용 품질 평가자. 5개 차원으로 PASS/FAIL 판정 |

## MCP 커넥터

| 커넥터 | 설명 |
|--------|------|
| sequential-thinking | 복잡한 다단계 추론을 위한 구조적 사고 엔진 |

## 사용 예시

```
/moai init
```
대화형 설문을 통해 프로젝트에 맞춤화된 `.claude/CLAUDE.md`를 자동 생성합니다.

```
유튜브 채널 기획서 만들어줘
```
자연어를 감지하여 `moai-content` 플러그인의 `media-production` 스킬을 자동 트리거합니다.
