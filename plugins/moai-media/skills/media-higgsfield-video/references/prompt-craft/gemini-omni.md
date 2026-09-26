# gemini-omni.md — Gemini Omni Flash 크래프트 (Google)

> 대상 모델(라이브 카탈로그 기준): `gemini_omni`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 (ai.google.dev)
출처: https://ai.google.dev

---

## Veo와 정반대 철학 (1차, verbatim)

편집: *"Simple prompts work best for video editing. Overly descriptive prompts can lead to unintended changes."* 생성(편집 아님)에서는 camera movement·lighting·mood를 서술한다. (Veo는 상세할수록 좋고, Omni는 편집에서 단순할수록 좋다 — 정반대. core R4의 역방향 경고.)

## 참조 문법 — 정확한 인라인 토큰 (1차)

`<FIRST_FRAME>`가 시작 프레임을 지정, `<IMAGE_REF_N>`(0-indexed)가 스타일/주제 참조를 산문에 인라인 표기:
> *"in the style of `<IMAGE_REF_0>` a woman `<IMAGE_REF_1>` is walking"*

## 영상 참조의 현재 제약

[Google의 현재 Omni 문서](https://ai.google.dev/gemini-api/docs/omni)는 영상 참조를 지원하되 인물의 외형 참조에 적합하고, 참조 영상 속 오디오는 무시하며, 여러 영상을 함께 참조하면 품질이 떨어질 수 있다고 설명한다. 이전의 “영상 참조가 제대로 처리되지 않는다”는 일괄 경고를 현재 사실로 반복하지 않는다. 이 세션의 Higgsfield `models_get(model_id="gemini_omni")`는 `video_references`를 반환했지만 실제 생성 결과는 확인하지 않았다. 참조 영상이 필요한 요청에는 현재 연결의 허용 역할·개수를 확인하고 이 제약을 승인 전에 알린다.

## 오디오·타임코드

오디오는 Veo의 태그 문법이 아니라 **평이한 서술 언어** — *"Include calm background music"*, *"The audio is a low tinny radio broadcast in the background."*
타임코드 구조 지원: `[0-3s] A person is walking / [3-6s] They stop and turn around / [6-10s] They start running`
길이 상한은 Google 기준 10s. 실제 duration·role은 `models_explore`로 확인한다.
