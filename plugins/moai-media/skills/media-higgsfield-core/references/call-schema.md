# call-schema.md — 호출 스키마 계약 (SSOT)

> `media-higgsfield-core` | `generate_image` / `generate_video`의 **형태(shape)** 계약.
> 개별 모델의 파라미터 **값**(enum·aspect·duration·media role)은 여기 하드코딩하지 않는다 — 현재 연결이 노출하는 모델 조회 도구로 확인한다(→ `catalog-protocol.md`).

**Evidence tier:** 1차 (Higgsfield MCP `models_explore`와 ChatGPT 공식 Higgsfield 플러그인의 `models_get` 도구 스키마 관측. 두 표면의 차이는 런타임에 재확인)

---

## 1. 중첩 `params` 객체

확인한 두 연결 모두 생성 인자를 중첩된 `params` 객체로 받는다. 안의 개별 값은 모델별로 라이브 조회한다. 아래 `get_cost` 예시는 **Higgsfield MCP 도구**에만 적용한다.

```
generate_image({
  params: {
    model:        "<catalog id>"        // models_explore로 확인한 실제 id
    prompt:       "<text>"
    aspect_ratio: "<model의 aspect_ratios 중 하나>"
    count:        <1-4>                  // 병렬 JOB 수
    medias:       [{ role: "<model이 선언한 role>", value: "<media_id | job_id>" }]
    get_cost:     <bool>                 // Higgsfield MCP 전용: true = JOB 제출 없이 견적
  }
})
```

```
generate_video({
  params: {
    model:        "<catalog id>"
    prompt:       "<text>"               // Marketing Studio 워크플로는 선택
    aspect_ratio: "<model의 aspect_ratios 중 하나>"
    duration:     <int>                  // model의 durations / duration_range 준수
    count:        <1-4>
    medias:       [{ role: "<role>", value: "<media_id | job_id>" }]
    get_cost:     <bool>                 // Higgsfield MCP 전용
  }
})
```

ChatGPT 공식 Higgsfield 플러그인은 `get_cost` 필드 대신 별도 `estimate_image_cost({params})`를 제공한다. 생성은 `generate_image({params})`, 모델 제약은 `models_get({model_id})`로 조회한다. 모델별 추가 인자의 허용 값은 **현재 연결의 라이브 조회 도구**로 확인한다.

---

## 2. HARD 제약 (tool schema 관측)

| 제약 | 내용 |
|---|---|
| `medias[].value` | Higgsfield MCP 표면은 `media_id` 또는 이전 생성 `job_id`를 받는다. ChatGPT 공식 플러그인은 이 값 외에 **승인된 HTTPS 이미지 URL**도 받아 자동으로 계정 미디어 라이브러리에 가져온다. URL을 보낼 때는 외부 업로드라는 사실을 먼저 알리고 사용자의 허용을 확인한다. |
| `medias[].role` | 연결과 모델별로 다르다. MCP는 `models_explore`에서 허용 role을 확인한다. ChatGPT 공식 플러그인은 `generate_image`·`generate_video` 도구의 입력 스키마가 받는 **공통 role**을 보내고, `models_get`의 모델 내부 media role과 대응되는지 확인한다. 예를 들어 이 세션의 `gpt_image_2_5` 상세 응답은 `image_references`를 보였지만 생성 도구 입력은 `image`를 받는다. 모델 내부 이름을 생성 인자로 그대로 복사하지 않는다. |
| `aspect_ratio` | 모델이 선언한 목록 안에 있어야 한다. 일부 모델은 빈 목록을 선언(aspect 미적용). |
| `duration` | 모델이 `durations`(enum) 또는 `duration_range`(범위) 중 하나를 선언한다. 허용 밖 값은 가장 가까운 값으로 스냅/클램프된다. |
| 비용 조회 | MCP는 `get_cost: true`, ChatGPT 공식 플러그인은 `estimate_image_cost({params})`를 사용한다. 둘 다 생성 JOB은 제출하지 않는다. 다만 공식 플러그인은 HTTPS 참조를 미디어 라이브러리에 가져올 수 있어, URL이 있으면 이 호출을 무부작용 조회로 취급하지 않는다. |
| `count` vs `batch_size` | `count`(1-4) = 병렬 **JOB** 수. `batch_size`는 `ms_image`에만 있고(1-20) JOB당 이미지 수를 뜻한다. 둘은 다르다. (`batch_size`는 `ms_image` 전용이므로 그 밖의 어떤 호출에도 등장하지 않는다.) |

---

## 3. 런타임 namespace 해석 (하드코딩 금지)

Higgsfield MCP 도구의 **namespace(네임스페이스) 접두사는 등록 방식에 따라 달라진다.** 스킬은 이를 **런타임에 해석**하고, 어느 한쪽을 유일한 형태로 하드코딩하지 않는다.

| 등록 경로 | 도구 namespace 접두사 |
|---|---|
| 플러그인 `.mcp.json` (서버명 `higgsfield`) | `mcp__higgsfield__` |
| Claude Desktop / connector 등록 | `mcp__claude_ai_higgsfield__` |
| ChatGPT 공식 Higgsfield 플러그인 | `mcp__codex_apps__higgsfield_` 형태의 도구가 노출될 수 있음 |

런타임 해석 규칙: 현재 앱에서 사용할 수 있는 도구 목록이나 검색 수단으로 실제 이름과 입력 스키마를 확인한다. `ToolSearch`라는 도구가 없어도 앱이 노출한 도구 목록을 볼 수 있다면 그 목록을 사용한다. 이름 접두사와 비용·조회·폴링 도구를 묶어 **하나의 연결 프로필**로 선택하고, 다른 프로필의 인자를 섞지 않는다.

---

## 4. `get_cost` 프리플라이트 · `adjustments` 리드백

- 실제 생성 **직전**에는 현재 연결의 비용 조회 도구로 `credits`를 확인한다. MCP에서는 `get_cost: true`, ChatGPT 공식 플러그인에서는 `estimate_image_cost({params})`다. 자세한 비용·참조 업로드 규칙은 `job-lifecycle.md`.
- 응답에 `adjustments` 필드가 있으면 서버가 채운 기본값을 뜻한다. 스킬은 이 필드를 **리드백(read-back)하여 사용자에게 보고**한다 — 오디오를 요청했는데 서버가 `generate_audio: false`로 치환했다면, 그 치환 사실을 사용자에게 알려야 한다. `adjustments`를 무시하면 사용자는 자기가 요청한 것과 다른 결과를 조용히 받게 된다.

---

## 5. 안티패턴 — 존재하지 않는 파라미터 (parameters that **do not exist**)

아래 이름들은 **이전(pre-SPEC) 스킬 본문에 있었지만 라이브 스키마에 do not exist** — 즉 존재하지 않는다. 전달하면 잘해야 무시되고 최악은 오류다. 이 목록은 오직 **산문(prose)으로만** 존재하며, 이 파일을 포함해 어떤 호출 예시(코드 블록)에도 넣지 않는다. (이 절이 곧 계약의 반례 목록이자, 발명된 옛 모델 id 표를 부활시키지 못하게 하는 트립와이어다.)

- `width_and_height` — 존재하지 않음. aspect는 `aspect_ratio`로, 실제 해상도는 모델별 `resolution`/`quality`(라이브 조회)로.
- `duration_seconds` — 존재하지 않음. 영상 길이는 `duration`(정수 초).
- `image_url` — 독립 파라미터로는 존재하지 않음. 참조 이미지는 `medias[].value`에 넣고, 허용 값은 §2의 연결 프로필을 따른다.
- `enhance_prompt` — 존재하지 않음.
- `style_strength` — 존재하지 않음.
- `custom_reference_id` — 존재하지 않음. 캐릭터 일관성은 모델별 media role 또는 `soul_id`로.
- `image_reference_url` — 독립 파라미터로는 존재하지 않음. ChatGPT 공식 플러그인의 승인된 HTTPS 참조도 `medias[].value`에 넣는다.

또한 다음도 **최상위 flat 인자로는 존재하지 않는다**: 평평한 `quality`(모델별 `params` 내부 값), `seed`(일부 3D 모델 예외), `preset`(필드명은 `preset_id`이며 `higgsfield_preset` 전용). 이전 스킬 본문이 열거하던 옛 모델 id들은 실제 카탈로그에 아예 없다 — 모델 id는 언제나 `models_explore`로 확인한다.

> 규칙: 이 절은 반례를 **이름으로 지목**하기 위해 그 이름들을 산문에 담는 유일한 장소다. 다른 어떤 파일에서도, 그리고 이 파일의 코드 블록 안에서도, 위 이름들은 등장하지 않는다.
