---
name: meta-skill-builder
description: |
  6-Phase 스킬 생성 워크플로우. revfactory/harness 방법론을 기반으로 체계적으로 새 스킬을 생성합니다.
  요구사항 분석부터 최종 검증까지 전체 생명주기를 관리합니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "새 스킬 만들어줘", "스킬 생성", "meta-skill-builder"
  - "이 기능 스킬로 만들고 싶어", "스킬 제작"
  - "Vibe 스킬 추가", "새 플러그인 스킬"
  - meta-skill-template으로 시작한 스킬의 체계적 생성이 필요할 때
user-invocable: false
version: "1.1.3"
---

# Skill Builder — 6-Phase 스킬 생성 워크플로우

> moai-coworker | revfactory/harness 방법론 기반 스킬 생성

## 개요

harness 오픈소스의 6-Phase 스킬 생성 워크플로우를 모두의 코워크 컨텍스트에 맞게 변환한 스킬입니다. 수작업 스킬 작성의 품질 편차를 줄이고, 체계적인 생성 프로세스를 통해 일관된 품질의 스킬을 생산합니다.

> **이름 이력**: v1.3.x까지 `skill-forge`로 제공되던 스킬이 v1.5.x에서 `meta-skill-builder`로 이름 변경되었습니다. 별칭은 유지되지 않으며 모든 참조는 `meta-skill-builder`로 갱신해야 합니다.

## 트리거 키워드

스킬 생성 스킬 제작 meta-skill-builder 새 스킬 만들기 스킬 추가 신규 스킬 harness 워크플로우

## 워크플로우

```
Phase 1: Requirements   → 사용자 의도 분석, 트리거 키워드 정의
Phase 1.5: Research     → 공식 자료·베스트 프랙티스 외부 조사 (현재 앱의 검색 기능, 관련 공식 문서 우선)
Phase 2: Architecture   → 에이전트 패턴 선택 (6종 중 매핑)
Phase 3: Skill Draft    → meta-skill-template 기반 SKILL.md 초안 + ## 출처 섹션
Phase 4: Test Gen       → 테스트 프롬프트 2-3개 + 기대 출력 정의
Phase 5: Validation     → 4차원 루브릭 스코어링 (meta-skill-tester 본문 §스코어링 루브릭)
Phase 6: Review         → 품질 게이트 통과 확인, 파일 배치
```

## 실행 규칙

### Phase 1: Requirements (요구사항 분석)

사용자의 자연어 요청에서 스킬 요구사항을 추출합니다.

**필수 수집 항목:**

| 항목 | 질문 | 예시 |
|------|------|------|
| 목적 | "이 스킬이 해결할 문제는?" | "영업 제안서를 자동 생성하고 싶다" |
| 타겟 플러그인 | "어느 플러그인에 배치할까?" | moai-coworker |
| 입력 | "사용자가 무엇을 입력하나?" | 회사명, 타겟 산업, 제품 정보 |
| 출력 | "어떤 산출물을 기대하나?" | 제안서 DOCX 파일 |
| 복잡도 | "스킬이 얼마나 복잡한가?" | Standard (50-150줄) |

**출력물:** 요구사항 요약. 확인이 필요한 항목은 현재 앱의 질문 기능 또는 대화로 묻고, 질문 기능이 없는 하위 실행은 누락 항목을 상위에 반환합니다.

### Phase 1.5: Research (외부 자료 조사) ★ v1.6.0 신설

스킬 도메인의 공식 자료·표준 양식·베스트 프랙티스를 조사하여 SKILL.md의 정확성과 권위를 확보합니다.

**조사 트리거 (다음 중 하나라도 해당하면 Phase 1.5 의무):**

- 한국 법규·표준 양식 관련 (세무·노무·계약·채용·의료 등)
- 외부 라이브러리·SDK·API·CLI 활용
- 글로벌 베스트 프랙티스 인용이 필요한 도메인 (B2B SaaS·HR·BI·DevOps 등)
- 정량 수치·통계 데이터·시장 규모 인용

**조사 절차:**

1. **현재 앱에서 사용 가능한 검색·문서 열람 기능으로 조사**
   - 한국어 쿼리 1-2회: `"<도메인> <핵심 키워드> <연도>"` 형식 (예: "한국 채용절차법 NCS 2026")
   - 영어 쿼리 1-2회 (글로벌 베스트 프랙티스 인용 시): `"<topic> best practice <year>"` 형식
   - 검색 결과의 최신성 확인 (2년 이내 자료 우선)

2. **라이브러리·SDK·CLI 관련 스킬일 때**
   - 공식 문서와 릴리스 노트에서 현재 API·CLI와 폐기된 기능을 확인
   - Context7 MCP가 연결된 경우에는 보조 자료로 활용하고 원저작자 문서와 대조

3. **도메인별 공식 출처 화이트리스트 (우선 인용):**

   | 도메인 | 1차 권장 출처 |
   |---|---|
   | 한국 세무·재무 | 국세청 nts.go.kr, 홈택스 hometax.go.kr, DART dart.fss.or.kr |
   | 한국 노무·채용 | 고용노동부 moel.go.kr, NCS ncs.go.kr, 한국노동연구원 kli.re.kr |
   | 한국 의료·건강 | 식약처 mfds.go.kr, 보건복지부 mohw.go.kr, 건강보험공단 nhis.or.kr |
   | 한국 정부지원 | K-Startup k-startup.go.kr, BIZINFO bizinfo.go.kr |
   | 한국 통계·시장 | KOSIS kosis.kr, 한국은행 ECOS ecos.bok.or.kr |
   | 한국 법률 | 국가법령정보센터 law.go.kr, 대법원 종합법률정보 glaw.scourt.go.kr |
   | 글로벌 회계 표준 | K-IFRS, IFRS Foundation ifrs.org |
   | 글로벌 채용 규제 | EEOC eeoc.gov, NYC Local Law 144, ISO 42001:2023 |
   | 글로벌 SaaS BP | 제품 공식 문서(HubSpot·Salesforce·Greenhouse 등) + 업계 리딩 블로그 |

4. **출처 보존:**
   - 조사 결과의 URL·발행일·핵심 인용 문장을 인메모리에 보존
   - Phase 3에서 SKILL.md `## 출처` 섹션에 markdown hyperlink 형식으로 인용
   - 정량 수치는 출처 인라인 표기 또는 `[추정]` 태그 강제

**산출물:** research notes (인메모리, Phase 3 입력으로 전달)

**금지:**
- 출처 없는 정량 수치 인용 (반드시 출처 명시 또는 `[추정]` 태그)
- 한국 도메인 스킬에 한국 공식 출처 누락
- 라이브러리·SDK 관련 스킬에서 공식 문서 확인 없이 도구 가용성만으로 API를 단정
- 구버전 자료 인용 (3년 초과 시 최신 자료 재검색)

**스킵 조건 (Phase 1.5 생략 가능):**
- 단순 포맷 변환·텍스트 처리 스킬 (도메인 지식 불필요)
- 사용자가 명시적으로 `--skip-research` 플래그 지정
- 기존 cowork 스킬의 minor 개선·트리거 키워드 조정만

### Phase 2: Architecture (아키텍처 선택)

6개 에이전트 패턴 중 최적 패턴을 선택합니다.

| 패턴 | 적용 시나리오 | 스킬 예시 |
|------|-------------|-----------|
| Pipeline | 순차 처리, 각 단계 출력이 다음 입력 | doc-docx, content-blog |
| Fan-out/Fan-in | 병렬 분석 후 결과 통합 | collab-ux-design, market-analysis |
| Expert Pool | 다 도메인 전문 지식 결합 | consult-brief, consult-startup |
| Producer-Reviewer | 생성 + 품질 검토 순환 | collab-sales-playbook, content-copywriting |
| Supervisor | 다수 전문 스킬 오케스트레이션 | moai-coworker:ai-diagnostic, project |
| Hierarchical Delegation | 복잡 작업 계층적 분해 | consult-startup |

**선택 기준:** 스킬의 워크플로우 단계 수, 병렬성 여부, 품질 검증 필요성을 기준으로 판단합니다.

**출력물:** 선택된 패턴 + 근거 (1-2문장)

### Phase 3: Skill Draft (스킬 초안 생성)

`meta-skill-template` 템플릿을 기반으로 SKILL.md 초안을 생성합니다.

**필수 적용:**

1. meta-skill-template의 필수 섹션 구조 사용
2. Frontmatter에는 `name`, `description`, `version`을 포함하고 현재 앱·플러그인 포맷의 지원 필드를 확인
3. 트리거 키워드는 대상 플러그인의 실제 스킬 목록과 대조해 중복을 검사
4. 사용 예시 최소 2개 포함
5. 관련 스킬 섹션에 before/after/alternative 관계 명시
6. **`## 출처` 섹션 의무**: Phase 1.5에서 수집한 URL·인용을 markdown hyperlink로 명시 (Phase 1.5 적용 스킬)
7. **정량 수치 인용 규칙**: 모든 수치는 출처 인라인 표기 또는 `[추정]` 태그

**참조:** `moai-coworker:meta-skill-tester (plugins/moai-coworker/skills/meta-skill-tester/SKILL.md` §스코어링 루브릭 (품질 기준 single source)
**참조:** `moai-coworker:meta-skill-template (plugins/moai-coworker/skills/meta-skill-template/SKILL.md` (템플릿)

**출력물:** `<target-plugin>/skills/<skill-name>/SKILL.md` 초안

### Phase 4: Test Generation (테스트 생성)

스킬 검증용 테스트 케이스를 생성합니다.

**테스트 구성:**

```yaml
skill: <skill-name>
version: 0.1.0
test_cases:
  - id: TC-001
    name: "happy-path"
    prompt: "<대표적인 사용 프롬프트>"
    assertions:
      - type: format
        value: "<markdown|json|text|html>"
      - type: contains
        value: "<필수 포함 내용>"
      - type: not_contains
        value: "<금지 내용>"

  - id: TC-002
    name: "edge-case"
    prompt: "<경계 조건 프롬프트>"
    assertions:
      - type: handles_gracefully
        value: true

  - id: TC-003
    name: "complex-input"
    prompt: "<복잡한 입력 프롬프트>"
    assertions:
      - type: contains
        value: "<복잡한 입력에서 반드시 반영할 항목>"
```

**출력물:** `<skill-dir>/tests/test-cases.yaml`

### Phase 5: Validation (품질 검증)

4차원 루브릭으로 스킬을 평가합니다.

| 차원 | 가중치 | 평가 |
|------|--------|------|
| Correctness | 30% | 목적 달성 여부 |
| Completeness | 25% | 에지 케이스 커버 |
| Clarity | 25% | 사용자 이해 가능성 |
| Efficiency | 20% | 토큰 대비 품질 |

**통과 기준:** 실행 결과가 관측됐을 때 기존 스킬은 가중 평균 >= 0.70, 신규 스킬은 >= 0.75이며 모든 차원은 >= 0.50입니다. 실행하지 못한 검사는 `NOT-RUN`으로 표시합니다.

**미달 시:** Phase 3으로 돌아가서 부족한 차원을 보완합니다. 최대 3회 반복.

**참조:** `moai-coworker:meta-skill-tester (plugins/moai-coworker/skills/meta-skill-tester/SKILL.md` §스코어링 루브릭 (anchor 점수표 + 평가 절차)

### Phase 6: Review (최종 검토)

배포 전 최종 체크리스트를 실행합니다.

**체크리스트:**

- [ ] Frontmatter 형식 준수 (`name`, `description`, `version`과 현재 런타임이 지원하는 필드)
- [ ] 필수 섹션 모두 존재 (개요, 트리거, 워크플로우, 예시, 출력, 주의사항, 관련 스킬)
- [ ] 트리거 키워드가 기존 스킬과 중복되지 않음
- [ ] 수정한 스킬의 `version`, 양쪽 `plugin.json`, 마켓플레이스 버전을 같은 변경에서 갱신
- [ ] 스킬 체인 관계가 프로젝트의 스킬 체인 정의와 일치 (해당 시)
- [ ] 테스트 케이스가 생성됨
- [ ] 실제 실행 결과를 바탕으로 기존 스킬 0.70 이상, 신규 스킬 0.75 이상 통과. 미실행 검사는 `NOT-RUN`
- [ ] **`## 출처` 섹션 존재** (Phase 1.5 적용 스킬, `--skip-research` 미지정 시)
- [ ] **정량 수치 모두 출처 또는 `[추정]` 태그** (Phase 1.5 적용 스킬)

**배치:** `<target-plugin>/skills/<skill-name>/SKILL.md` 에 최종 파일을 배치합니다.

## 사용 예시

**예시 1: 신규 스킬 생성**
> "moai-coworker에 영업 제안서 자동 생성 스킬을 만들어줘. 회사명과 타겟 기업 입력하면 제안서 DOCX가 나오게"

**예시 2: Vibe 갭 스킬 생성**
> "meta-skill-builder로 moai-coworker에 UX 디자인 분석 스킬을 만들어줘. Vibe Designing 기능 참고해서"

## 출력 형식

| 산출물 | 위치 | 설명 |
|--------|------|------|
| SKILL.md | `<plugin>/skills/<name>/SKILL.md` | 완성된 스킬 정의 |
| test-cases.yaml | `<plugin>/skills/<name>/tests/` | 테스트 케이스 |
| score-report | 인메모리 | 루브릭 스코어 보고서 |

## 주의사항

- 기존 스킬 수정이 아닌 **신규 스킬 생성**에만 사용합니다
- 플러그인 디렉토리(`moai-*`)가 존재하는지 사전 확인이 필요합니다
- 스킬을 생성·수정하면 해당 플러그인의 Claude·Codex 매니페스트와 마켓플레이스 버전을 함께 갱신합니다.
- 트리거 키워드 중복 시 기존 스킬의 description을 확인하여 명확히 구분해야 합니다

## 한국어 예시 카피 작성 규칙 (슬롭 방지)

신규 스킬에 한국어 예시 카피를 넣을 때 AI 슬롭 패턴이 예시로 전염되지 않도록 아래 3종을 금지합니다. 이 규칙은 `ai-slop-reviewer`·`korean-humanize` 게이트가 슬롭으로 분류하는 패턴이 "좋은 예"로 등록되는 것을 원천 차단합니다.

| # | 금지 패턴 | 설명 | [나쁜 예] (슬롭) | 권장 예시 |
|---|----------|------|-----------------|-----------|
| 1 | **대시 대비 헤드라인** | 대시(`—`)로 문장을 분할하는 "X — Y" 구조 (대시 대비 헤드라인) | [나쁜 예] "복붙에서 위임으로 — 목표만 주면" | 완결된 문장으로 작성 |
| 2 | **조사·체언 종결 조각문** | 조사(~은/에/로)나 체언으로 끝나는 파편문 (조사·체언 종결) | [나쁜 예] "성공의 열쇠 — 자동화" | 서술어를 갖춘 완전문 |
| 3 | **"A에서 B로" 전환 공식** | "X에서 Y로" 전환 공식 도입 (슬롭 상투문) | [나쁜 예] "엑셀에서 노션으로" | 구체적 사례로 시작 |

예시 카피에는 이 슬롭 패턴을 넣지 마세요 — 새 스킬이 슬롭을 가르치는 원천이 되지 않도록 합니다.

## 관련 스킬

| 스킬 | 관계 | 설명 |
|------|------|------|
| meta-skill-template | before | 템플릿 구조를 제공하는 기반 스킬 |
| meta-skill-tester | after | 생성된 스킬의 테스트 실행 + 루브릭 스코어링 |
| ai-slop-reviewer | after | 스킬 본문의 AI 패턴 검수 (선택) |

## 실행 진입점

현재 앱에 이 스킬이 노출돼 있으면 자연어로 스킬 제작을 요청합니다. `meta-skill-tester`의 검증과 `ai-slop-reviewer`의 문체 검수는 각 스킬이 노출된 경우에만 연결합니다. 이 플러그인은 별도 `/harness` 명령을 제공하지 않습니다.

---

Source: revfactory/harness 6-Phase workflow (Apache 2.0) + MoAI adaptation

## Changelog

- **재정립 전 1.6.0** (2026-05-01): Phase 1.5 Research 신설 — 외부 자료 조사(WebSearch·Context7) 의무화, 도메인별 공식 출처 화이트리스트 추가, `## 출처` 섹션 의무화 + 정량 수치 출처/`[추정]` 태그 강제
- **재정립 전 1.5.x**: skill-forge → meta-skill-builder 이름 변경
- **이전**: harness 6-Phase 워크플로우 흡수
