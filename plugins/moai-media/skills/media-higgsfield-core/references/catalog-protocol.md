# catalog-protocol.md — 라이브 카탈로그 조회 프로토콜

> `media-higgsfield-core` | 파라미터·모델·프리셋을 **런타임에 조회**하는 도구와 순서.
> 이 파일은 "무엇을 물어보는가"를 정의한다. "무엇을 하드코딩하는가"의 답은 언제나 **아무것도**다.

**Evidence tier:** 1차 (라이브 MCP와 ChatGPT 공식 Higgsfield 플러그인 도구 스키마 관측 + Higgsfield 공식 agent 문서)

Higgsfield 자신의 agent 문서가 이 설계를 직접 확인한다. `references/`는 에이전트에게 이렇게 지시한다: **"When unsure, run `higgsfield model get <model>` and inspect the schema."** — 벤더 스스로 정적 파라미터 계약 발행을 거부한다.
출처: https://github.com/higgsfield-ai/skills

---

## 1. 연결별 카탈로그·생성 도구

같은 Higgsfield 계정이라도 Claude의 MCP 연결과 ChatGPT 공식 플러그인은 도구 이름과 일부 입력 계약이 다르다. 실행 전 실제 노출된 도구의 스키마로 연결 프로필을 확인한다.

| 작업 | Higgsfield MCP 연결 | ChatGPT 공식 Higgsfield 플러그인 |
|---|---|---|
| 모델 목록·검색·추천·상세 | `models_explore(action: ...)` | `models_list`·`models_search`·`models_recommend`·`models_get` |
| 이미지·영상 견적 | `generate_image`·`generate_video`의 `params.get_cost:true` | `estimate_image_cost({params})`·`estimate_video_cost({params})` |
| 이미지·영상 생성 | `generate_image({params})`·`generate_video({params})` | `generate_image({params})`·`generate_video({params})` |
| 잔액 | `balance` | `balance` |
| 생성 상태 | `job_status` | `jobs_wait` (반환된 job ID 사용) |

아래 표는 **MCP 연결 프로필**의 상세 계약이다. ChatGPT 공식 플러그인에서는 오른쪽 열의 대응 도구를 사용하고, 현재 스키마에 없는 인자를 전달하지 않는다.

| 도구 | 런타임 역할 |
|---|---|
| `models_explore(action:'list'\|'search'\|'get'\|'recommend')` | 카탈로그 진실원. `get`은 한 모델의 정확한 제약(aspect·duration·media role·모델별 param)을 반환. `recommend`는 목표 + 입력 컨텍스트로 후보를 제안. `list`는 유형별 전체 목록. `search`는 키워드 검색. |
| `show_marketing_studio(type:'image_style'\|'brand_kit'\|'product'\|'hook'\|'setting'\|'ad_reference')` | MCP 연결에서 `ms_image` / `marketing_studio_video`의 사전 목록 호출. ChatGPT 공식 플러그인에서는 현재 노출된 대응 목록 도구를 확인한다. 이 세션의 DTC Ads 이미지 포맷 목록은 `marketing_list_ad_formats`가 반환했다. |
| `presets_show` | `higgsfield_preset`용 프리셋 카탈로그. |
| `get_workflow_instructions()` | 브리핑형 워크플로 카탈로그. 인자 없이 목록, `{workflow}`로 상세. |
| `get_cost`(생성 도구의 `params.get_cost:true`) | 비용 프리플라이트. `job-lifecycle.md` 참조. |
| `balance` | 크레딧 잔액. |
| `media_upload` / `media_import_url` | 로컬 파일·웹 URL → `media_id`. `medias[].value`에 사용. |
| `job_status` / `job_display` | 비동기 JOB 폴링. |

---

## 2. 표준 런타임 순서 (REQ-010)

생성은 아래 순서를 따른다. ChatGPT 공식 플러그인의 일반 이미지 생성은 기본 모델로 바로 실행할 수도 있지만, 이 스킬은 유료 생성 전 비용·잔액 고지와 승인을 위해 견적 단계를 유지한다.

1. **후보 좁히기** — 사용자 의도에서 계열 후보를 추린다(→ 각 `prompt-craft` 크래프트 노트). 이 단계는 후보를 *좁힐 뿐*, 파라미터를 단정하지 않는다.
2. **라이브 조회** — MCP는 `models_explore(action:'get', ...)`, ChatGPT 공식 플러그인은 `models_get({model_id})`로 제약을 가져온다. 사용자가 모델을 지정하지 않은 평범한 이미지 생성에서는 공식 플러그인이 안내하는 기본 모델을 사용할 수 있다. Marketing Studio의 필수 스타일 목록은 현재 연결의 대응 목록 도구로 조회한다.
3. **비용 프리플라이트** — MCP는 `get_cost: true`, ChatGPT 공식 플러그인은 작업 유형에 맞는 `estimate_image_cost`·`estimate_video_cost`로 견적을 받는다. `adjustments`를 승인 전에 확인한다. 공식 플러그인에 HTTPS 참조 이미지를 전달하면 이 단계에서 미디어 라이브러리 업로드가 일어날 수 있으므로, 업로드 허용을 먼저 받는다.
4. **유료 생성 승인** — 코어 스킬의 승인서를 사용자에게 보여주고 명시적 응답을 받는다. 하위 실행에서 직접 물을 수 없으면 승인서 전체를 상위에 반환한다. 견적 조회만으로 생성 승인을 받은 것으로 보지 않는다.
5. **생성** — 승인된 값으로만 실제 `generate_image` / `generate_video`를 호출한다.
6. **폴링·리드백** — MCP는 `job_status`, ChatGPT 공식 플러그인은 반환된 job ID를 `jobs_wait`에 전달한다. ChatGPT 생성 도구가 결과 위젯을 자동으로 표시한 경우 같은 결과를 다시 `job_display`로 열지 않는다. 반환된 `adjustments`를 보고한다(→ `job-lifecycle.md`).

---

## 3. 범위 밖 모델 폴백 (live lookup)

15개 크래프트 계열에 없는 모델(예: `z_image`, `kling_omni_image`, `grok_image`)을 사용자가 요청하면:

- 계열 크래프트 파일이 없다는 사실을 **명시적으로 말한다.**
- `models_explore(action:'get')`로 제약을 **live lookup(라이브 조회)**한다.
- 공통 규칙 R1–R5(→ `universal-rules.md`)를 적용한다.

계열 특화 크래프트가 없다고 해서 모델을 못 쓰는 게 아니다 — 카탈로그를 라이브로 조회하면 제약을 알 수 있다. 다만 그 사실을 숨기지 않고 사용자에게 알린다.

---

## 4. 왜 스냅샷을 계약으로 쓰지 않는가

개발 중 기록한 모델 스냅샷은 배포 패키지에 포함되지 않으며 런타임 계약이 아니다. 현재 연결의 라이브 카탈로그가 이전 관측과 다르면 라이브 값을 사용한다. 모델 목록을 스킬 본문에 고정하지 않는다.
