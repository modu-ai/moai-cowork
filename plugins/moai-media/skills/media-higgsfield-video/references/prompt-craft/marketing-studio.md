# marketing-studio.md — Marketing Studio 영상 크래프트 (Higgsfield)

> 대상 모델(라이브 카탈로그 기준): `marketing_studio_video`
> preset 슬러그·hook·setting·aspect·duration은 현재 연결의 목록·모델 상세 도구로 라이브 조회.

**Evidence tier:** 1차 (Higgsfield 공식 agent 문서 + 라이브 MCP)
출처: https://github.com/higgsfield-ai/skills

**프롬프트가 아니라 워크플로다.** 이 모델은 prompt가 선택이다.

---

## preset 모드는 라이브 조회한다 (26개는 예시일 뿐, 계약 아님)

`marketing_studio_video`의 `mode`는 preset 슬러그다. 2026-07-12 Claude MCP 조회에서는 26개였고, 이 세션의 ChatGPT 공식 플러그인 `marketing_list_video_presets`도 `formats` 26개와 `presets` 26개를 반환했다. 이 수와 `dop-motions.md`의 슬러그는 **관측 사례이지 현재 계약이 아니다**. Claude MCP에서는 `show_marketing_studio`, ChatGPT 공식 플러그인에서는 현재 노출된 `marketing_list_video_presets` 같은 대응 도구로 다시 조회하고 사용자가 고른 모드를 전달한다. 목록 도구가 없으면 모드를 추측해 유료 생성을 호출하지 않는다.

## 구성 규칙 (HARD — MCP 스키마 + Higgsfield agent 문서 일치)

- `hook_id`(the "what" — 어텐션 메커닉)와 `setting_id`(the "where" — 장소/바이브)는 서로 **독립**(둘 중 하나, 둘 다, 또는 없음).
- 둘 다 `ad_reference_id`와 **mutually exclusive(상호 배타)**다. hook/setting은 명시적 빌딩블록으로 구성하고, `ad_reference_id`는 기존 영상 시나리오를 재현한다. **한 접근만 고르고 둘을 함께 쓰지 않는다.** Higgsfield agent 문서 verbatim: *"When the user has selected an ad reference for the ad, do not also pass --hook_id or --setting_id."*
- hook/setting의 허용 모드와 슬러그는 호출 직전 현재 연결의 목록·모델 상세 도구에서 확인한다. ChatGPT 공식 플러그인에서는 노출된 `marketing_list_hooks`·`marketing_list_settings`를 사용할 수 있다. 2026-07-12 MCP 조회 때는 `ugc`, `ugc_how_to`, `ugc_unboxing`, `product_review`, `ugc_virtual_try_on`에 허용됐지만 이를 현재 계약으로 고정하지 않는다.
- hook을 쓰면 `product_ids`를 **반드시** 포함("they require product context").
- `ad_reference_id`는 연결된 아바타/제품을 자동으로 끌어오지 **않는다** — 명시적으로 전달한다.
- 기본 aspect는 landscape → TikTok/Reels는 `9:16`을 **명시적으로** 전달.

**Avatars**: `preset`(큐레이션, 업로드 비용 없음) vs `custom`(업로드, 비용 있음). UGC 모드는 아바타 선택 — *"the backend can synthesize a Soul Character automatically."*

벤더 자체 10단어 "Wild Card" 예시(verbatim): *"You scan the fridge, get a recipe, cook a meal."* 실제 param·슬러그·개수는 현재 연결의 모델 상세·목록 도구로 확인한다. 모드 선택 뒤에도 비용·잔액 조회와 코어의 유료 생성 승인 게이트를 거친다.
