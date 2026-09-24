---
name: media-higgsfield-video
description: |
  Higgsfield 계정의 영상 모델로 영상을 생성합니다. Claude의 MCP 연결과 ChatGPT의 공식
  Higgsfield 플러그인에서 현재 노출된 모델·견적·생성 도구를 확인해 호출합니다.
  다음과 같은 요청 시 사용하세요:
  - "Higgsfield 영상 만들어줘"
  - "Veo로 영상"
  - "Kling으로 영상"
  - "Seedance로 다이내믹 영상"
  - "Cinema Studio로 시네마틱 영상"
  - "Marketing Studio UGC 광고 영상"
  Veo·Kling·Seedance·Cinema Studio·Marketing Studio·Wan·Gemini Omni·Grok 등 계열의 프롬프트 크래프트는
  references/prompt-craft/*.md에 출처와 함께 큐레이션돼 있고(계열마다 규칙이 다름 — 범용 공식 없음),
  실제 파라미터(모델 id·해상도·비율·길이·비용)는 런타임에 라이브 조회합니다.
version: "1.3.3"
---

# Higgsfield 영상 생성 (media-higgsfield-video)

> `moai-media` | 라이브 카탈로그 기반 영상 생성 (코어: `media-higgsfield-core`)

## 개요

Claude에서는 Higgsfield MCP, ChatGPT에서는 공식 Higgsfield 플러그인의 영상 생성 도구를 호출합니다. 사용자 의도로 계열 후보를 좁힌 뒤 **파라미터는 현재 연결의 라이브 카탈로그에서 조회**해 생성합니다.

핵심 설계는 코어 스킬 `media-higgsfield-core`에 있습니다: 호출 계약(`call-schema.md`), 라이브 조회(`catalog-protocol.md`), 공통 규칙 R1–R5(`universal-rules.md`), 잡·비용·리드백(`job-lifecycle.md`).

## 계열 크래프트 (references/prompt-craft/) — 계열마다 규칙이 다르다

각 파일은 벤더 공식 문서 기반이며 출처·Evidence tier를 답니다.

| 파일 | 계열 |
|---|---|
| `references/prompt-craft/veo.md` | Veo (오디오 문법 SFX:/Ambient noise:) |
| `references/prompt-craft/kling.md` | Kling (유연 프레임워크, 1차-relayed) |
| `references/prompt-craft/seedance.md` | Seedance (2.0의 정밀 타이밍 주의·2.5의 샷별 구성 구분) |
| `references/prompt-craft/cinema-studio.md` | Cinema Studio (4계층 참조, enum 라이브 조회) |
| `references/prompt-craft/marketing-studio.md` | Marketing Studio (hook/setting↔ad_reference 상호배타) |
| `references/prompt-craft/wan.md` | Wan (Timestamp 멀티샷 — Seedance 세대별 지침과 구분) |
| `references/prompt-craft/gemini-omni.md` | Gemini Omni (편집은 단순 프롬프트) |
| `references/prompt-craft/grok.md` | Grok (xAI 오디오 문서 확인, Higgsfield 옵션은 별도 조회) |

카메라 디렉팅·Marketing Studio 슬러그 참고: `references/dop-motions.md`.

## 범용 비디오 공식은 없다 — per-family 라우팅

**단일 범용 비디오 프롬프트 공식을 쓰지 않는다.** 모델 세대마다 타이밍 지침도 다르다. 이전 Seedance 안내는 초 단위 강제를 경고했지만, Higgsfield의 Seedance 2.5 가이드는 샷별 구성과 시간대 예시를 보여준다. Wan의 타임스탬프 지침도 별개다. 따라서 대상 모델 세대의 `prompt-craft/` 파일과 현재 연결의 제약을 대조한다.

## 워크플로우 (REQ-010 흐름)

### 1단계 — 의도 파악 → 후보 좁히기

사용자 요청에서 subject·action·scene·camera·audio·references(+각 용도)·shot count·duration 등 슬롯을 수집(→ core `interview-schema.md`)하고 계열 후보를 좁힙니다. 후보를 좁힐 뿐 파라미터를 단정하지 않습니다. 슬롯이 부족하면 직접 실행에서만 현재 앱의 질문 채널로 필요한 항목을 확인합니다. 하위 에이전트는 질문 도구가 보여도 누락 슬롯·선택지·재개 방법을 blocker로 상위에 반환하고, 직접 실행에 채널이 없어도 같은 blocker를 반환합니다.

| 사용자 표현 | 후보 계열 |
|---|---|
| "사실적", "오디오 있는 영상" | Veo |
| "인물·표정·스토리보드" | Kling |
| "다이내믹 모션·멀티샷" | Seedance 또는 Wan |
| "영화 룩·모션 전이" | Cinema Studio |
| "UGC·DTC 광고 영상" | Marketing Studio |
| "이미지 편집·간단 참조" | Gemini Omni |
| "Grok 영상" | Grok |

### 2단계 — 현재 연결의 라이브 모델 조회

MCP는 `models_explore(action:'get')`, ChatGPT 공식 플러그인은 `models_get({model_id})`로 후보의 실제 제약(aspect_ratios·durations·media role·모델별 param)을 조회합니다. 범위 밖 모델이면 계열 크래프트가 없다는 것을 명시하고 라이브 제약과 R1–R5를 적용합니다. Marketing Studio 계열은 현재 연결의 preset/hook/setting 목록 도구를 사용합니다.

### 3단계 — 연결별 비용 견적

MCP는 `get_cost: true`, ChatGPT 공식 플러그인은 `estimate_video_cost({params})`로 청구 크레딧을 확인합니다. `adjustments`가 있으면 승인 전에 보여줍니다(예: 오디오를 요청했는데 `generate_audio: false`로 치환). HTTPS 참조의 외부 업로드가 필요하면 견적 전에 허용을 받습니다. 잔액 정지 규칙은 core `job-lifecycle.md`.

### 4단계 — 승인 게이트 (크레딧 소진 전)

견적은 생성 승인이 아닙니다. 크레딧이 실제로 나가기 전 코어 §유료 생성 승인 게이트를 따릅니다 — 프롬프트 전문·모델 id·입력 미디어·확정 옵션·길이·생성 개수·`adjustments`·견적 크레딧·잔액을 보여주고 승인을 받습니다.

- **[HARD] 3단계에서 확보한 `adjustments`를 여기서 보여줍니다.** 3단계의 예(오디오를 요청했는데 `generate_audio: false`로 치환)가 바로 이 게이트가 필요한 이유입니다 — 오디오 없는 영상에 영상 값 크레딧을 낸 뒤에 알게 되면 늦습니다.
- 위 §주의 블록에 해당하는 참조 영상 사용이나 정밀 카메라 명령이면 **현재 확인한 제약을 승인 화면에 함께 띄웁니다.** 사용자가 예상 결과와 비용을 알고 결정하게 합니다.
- 서브에이전트로 실행 중이면 승인서를 blocker로 반환합니다. 사용자와 직접 대화하는 세션이면 코어의 런타임 중립 승인 요청 계약을 따릅니다.

### 5단계 — 생성 (generate_video)

승인된 값으로만 실제 `generate_video`를 호출합니다. 도구 이름과 입력 스키마는 현재 연결에서 확인합니다. 참조 미디어 값도 연결 스키마를 따르며, HTTPS URL은 외부 전송 허용 뒤에만 사용합니다.

- **[HARD] 실패해도 새 잡을 만들지 않습니다.** 애매하게 실패하면 반환된 job ID를 현재 연결의 상태 도구로 확인하고, ID조차 없으면 실제 노출된 생성 이력 도구나 Higgsfield 대시보드에서 확인합니다. 기존 잡이 없거나 실패한 것이 확인된 뒤에만 다시 호출합니다. 영상은 이미지보다 단가가 높아 중복 비용이 큽니다.

### 6단계 — 폴링·리드백

MCP는 `job_status`, ChatGPT 공식 플러그인은 `jobs_wait`로 완료를 확인합니다. 생성 도구가 결과 위젯을 이미 보여줬으면 단순 표시를 위해 `job_display`를 다시 호출하지 않습니다. 결과 URL과 `adjustments`를 보고합니다.

## 주의 블록 (해당 요청에 적용)

해당 기능을 요청했을 때 현재 연결과 벤더 문서의 제약을 대조해 사용자에게 알린다:

- **`gemini_omni` 영상 참조** — 이 세션의 Higgsfield 모델 상세 조회는 `video_references`를 노출했다. 현재 [Google의 Omni 안내](https://ai.google.dev/gemini-api/docs/omni)는 짧은 영상 참조를 지원한다고 설명하지만 참조 영상의 오디오는 무시되고 여러 영상을 함께 참조하면 결과가 저하될 수 있다고 경고한다. Higgsfield 연결에서 실제 결과를 확인하지 않았으므로 성공을 보장하지 않는다(→ `prompt-craft/gemini-omni.md`).
- **`minimax_hailuo`는 카메라 명령을 조용히 덮어쓸 수 있다** — MiniMax 자체 API의 `prompt_optimizer`(기본 true)가 프롬프트를 자동 재작성해 정밀한 수동 카메라 명령을 뭉갤 수 있다. **Higgsfield는 이 스위치를 노출하지 않으므로** MCP로는 끌 수 없다. 정밀 카메라 디렉팅이 무시될 수 있음을 경고한다.
- **Grok 영상 오디오** — [xAI의 현재 문서](https://docs.x.ai/developers/model-capabilities/video/generation)는 자체 API 영상에 기본 오디오와 `generate_audio` 옵션을 설명한다. 이 세션의 Higgsfield `grok_video_v15` 모델 상세에는 해당 옵션이 없었다. xAI API의 오디오 제어 인자를 Higgsfield 호출에 그대로 넣거나 결과의 오디오를 보장하지 않는다(→ `prompt-craft/grok.md`).

## 범위 밖 모델 폴백 (live lookup)

계열 크래프트에 없는 모델을 요청하면, 계열 특화 크래프트가 없다는 사실을 명시하고 현재 연결의 모델 상세 도구로 제약을 조회한 뒤 공통 규칙 R1–R5를 적용합니다.

## 출력 형식

```
## Higgsfield 영상 생성 결과
- 모델: [라이브 모델 도구로 확인한 실제 id]
- 프롬프트: [계열 크래프트로 조립된 최종 프롬프트]
- 비율·길이: [라이브 aspect_ratios·durations 중 선택]
- 비용: [연결별 견적 도구가 반환한 credits]
- Job ID / 결과 URL: [연결별 상태 도구가 확인한 완료 결과]
- 서버 조정(adjustments): [있으면 그대로 보고]
```

## 주의사항

- 프롬프트는 대상 계열의 `prompt-craft/` 벤더 공식 컨벤션을 따릅니다 — 범용 공식을 쓰지 않습니다.
- image-to-video는 시작 이미지가 담은 정적 정보를 빼고 motion + camera로 시작합니다(R2). 시작 이미지는 `media-higgsfield-image`로 먼저 생성할 수 있습니다.
- 모델 id·파라미터를 추측하지 않습니다 — 현재 연결의 라이브 모델 조회 도구로 확인합니다.
- nsfw·초상권·저작권 침해 소지 콘텐츠는 생성하지 않습니다.

## 관련 스킬

| 스킬 | 시점 |
|---|---|
| `moai-media:media-higgsfield-core` | 코어: 호출 계약·라이브 조회·공통 규칙 |
| `moai-media:media-higgsfield-image` | 선행: 시작 이미지 생성 |
| `moai-media:media-audio-gen` | 보조: 영상용 음성·BGM |

## 출처

- [Higgsfield Skills (공식 agent 문서)](https://github.com/higgsfield-ai/skills)
- [Higgsfield MCP](https://higgsfield.ai/mcp)
- 계열별 프롬프트 크래프트 출처는 각 `references/prompt-craft/*.md`의 Evidence tier·출처 참조.
- 라이브 카탈로그: MCP의 `models_explore` 또는 ChatGPT 공식 플러그인의 모델 조회 도구. 스냅샷은 런타임 계약이 아닙니다.
