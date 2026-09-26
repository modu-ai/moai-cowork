# marketing-studio.md — Marketing Studio 이미지 크래프트 (Higgsfield)

> 대상 모델(라이브 카탈로그 기준): `ms_image` (DTC Ads), `marketing_studio_image`
> 파라미터·style·aspect는 `models_explore` / `show_marketing_studio`로 라이브 조회.

**Evidence tier:** 1차 (Higgsfield 공식 agent 문서 + 라이브 MCP)
출처: https://github.com/higgsfield-ai/skills

---

## 이 계열은 프롬프트가 아니라 워크플로다

프롬프트는 부차적이고, **스타일/포맷 선택이 지배적인 창작 드라이버**다.

## 필수 사전 호출 순서 (연결별 라이브 확인)

1. Claude의 Higgsfield MCP 연결에서는 `show_marketing_studio(action='list', type='image_style')`, ChatGPT 공식 플러그인에서는 현재 노출된 DTC Ads 포맷 목록 도구를 호출한다. 이 세션의 ChatGPT 연결은 `marketing_list_ad_formats`에서 이름과 ID를 반환했다. 어느 도구도 없으면 목록 선택을 건너뛰고 생성하지 않는다.
2. **사용자가 목록에서 이름으로 스타일·포맷을 고른다.** MCP 스키마: *"Style is the dominant creative driver for ms_image output, so silently defaulting would produce a result the user didn't ask for."*
3. 선택한 ID를 현재 생성 도구 스키마의 필드에 연결하고 모델 상세·비용·잔액을 확인한다. 코어의 승인서에 프롬프트와 모든 옵션·견적을 보여주고 명시적 응답을 받는다.
4. 승인된 값으로만 `generate_image`를 호출한다.

`style_id`에는 **no default(기본값 없음)** — 없이 호출하면 오류다. Higgsfield 자체 agent 문서도 의도를 반복한다: *"always display the ad format list and let users pick by name rather than auto-selecting."* 스킬은 스타일을 **절대 자동 기본값으로 채우지 않는다** — 현재 연결의 목록을 보여주고 사용자가 고르게 한다.

> `style_id`(MCP 표면) vs `format_id`(CLI 표면)의 명칭 충돌은 라이브 목록과 생성 도구 스키마로 해소한다. 이 세션의 ChatGPT 공식 플러그인은 `marketing_list_ad_formats`에서 이름과 ID가 있는 DTC Ads 포맷 목록을 반환했다. 현재 연결에서 사용자가 고른 항목의 ID와 생성 도구가 받는 필드명을 다시 확인한다. 어느 것도 하드코딩하지 않는다.

## 선택 파라미터 (엄격히 opt-in, 절대 추론 금지)

- `brand_kit_id`: `status: completed`여야 함. 실제 웹사이트 URL을 가져와 생성(이름·로고·히어로 이미지·색·폰트·톤·제품 캡처, 30–90초; 실패 kit는 terminal).
- `product_ids`와 `medias`: 허용 개수는 호출 시점의 모델 상세·도구 스키마에서 확인.

이 값들은 사용자가 명시적으로 줄 때만 넣는다. 실제 허용 값·개수는 현재 연결의 모델 상세 도구로 확인한다.
