# soul.md — Soul 계열 크래프트 (Higgsfield)

> 대상 모델(라이브 카탈로그 기준): `soul_2` / `soul_v2`, `soul_cinematic`, `soul_cast`, `soul_location`
> 파라미터·aspect·media role은 `models_explore(action:'get')`로 라이브 조회. 이 파일은 크래프트만 다룬다.

**Evidence tier:** 메커니즘은 1차 (Higgsfield 공식 Soul ID / Soul Cast 문서). 프롬프트 공식·예시는 **none-found**(부재 확인).
출처: https://higgsfield.ai · https://github.com/higgsfield-ai/skills

---

## 공식 프롬프트 공식 부재 (No Official Prompt Formula)

Soul 계열에는 **no official prompt formula** — 공식 프롬프트 공식이 존재하지 않는다. 이것은 리서치 갭이 아니라 **증거로 확인된 부재**다. `soul-intro`·`soul-cinema`·Soul how-to 페이지는 프롬프트 크래프트 지침이 0인 기능 개요/마케팅 페이지다. Higgsfield의 명시적 설계 철학은 **anti-formula**다 — Soul은 사용자가 *"name a look instead of describing it technically"* 하도록, 프리셋과 무드보드에 기대도록 만들어졌다.

**Soul 공식을 지어내지 않는다.** 프롬프트 크래프트는 공통 규칙 R1–R5(`../../../media-higgsfield-core/references/universal-rules.md`)와 Higgsfield 일반 `prompt-engineering.md`로 폴백한다.

---

## 문서화된 것 — 정체성/일관성 메커니즘 (1차)

- **Soul ID**: 한 인물의 여러 사진으로 학습한다. 공식 웹 도움말은 20~80장, 공식 CLI 스킬은 5~20장을 안내한다. MCP·ChatGPT 연결은 학습 도구의 현재 수량 제한을 따르며, 확인 전에는 한쪽 값을 적용하지 않는다. 얼굴 구조·피부톤·머릿결·비율을 학습해 일관성을 높인다. 사진 요건: 밝은 조명, 선글라스·짙은 그림자·크롭된 얼굴 없음, 각도·표정 다양, 전신 1장 포함, 최근 사진. 극단적인 스타일 변화에서는 얼굴이 조금 달라질 수 있다. [웹 도움말](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character) · [CLI 스킬](https://github.com/higgsfield-ai/skills/blob/main/higgsfield-soul-id/SKILL.md)
- **참조는 프롬프트 문법이 아니라 선택으로 바인딩된다.** 인라인 `soul_id:` 프롬프트 토큰은 없다. `soul_id` MCP 파라미터가 바인딩 메커니즘이다(값은 라이브 조회).
- **Soul Cast는 프롬프트 기반이 아니다** — *"Build, don't describe."* 8개 카테고리로 파라미터화: Genre(14) · Budget(슬라이더 — 높을수록 *"refined, blockbuster-grade"*, 낮을수록 *"grittier, more indie"*; 이것이 `soul_cast`의 `budget` 파라미터가 구동하는 값) · Era · Archetype(12 융 원형) · Identity · Physical Appearance · Details · Outfit. 카탈로그도 `soul_cast`가 미디어 참조 없는 text-only임을 확인한다.

---

## 이 계열에서 실제로 하는 것

1. 사용자 의도에서 subject·lighting·style 슬롯을 수집(→ core `interview-schema.md`).
2. `models_explore(action:'get')`로 대상 Soul 모델의 실제 aspect_ratios·params(`soul_id`, 품질 티어 등)를 조회.
3. 프롬프트는 R1–R5 + Higgsfield 일반 가이드로 구성한다. 예: 제외는 긍정 묘사(R1), 리터럴 텍스트는 따옴표+폰트(R3).
4. 인물 시리즈 일관성은 `soul_id` 바인딩으로 한다. 이전 스킬이 쓰던 별도 참조-id 파라미터들은 라이브 스키마에 존재하지 않는다(반례 목록은 core `call-schema.md`의 안티패턴 절 참조).
5. Soul Cast는 프롬프트 대신 8개 카테고리 슬롯으로 안내한다.
