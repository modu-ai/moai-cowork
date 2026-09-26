---
name: media-higgsfield-image
description: |
  Higgsfield 계정의 이미지 모델로 이미지를 생성합니다. Claude의 MCP 연결과 ChatGPT의 공식
  Higgsfield 플러그인에서 현재 노출된 모델·견적·생성 도구를 확인해 호출합니다.
  다음과 같은 요청 시 사용하세요:
  - "Higgsfield로 이미지 만들어 줘"
  - "Soul로 인물 이미지"
  - "Nano Banana Pro로 카드뉴스 이미지"
  - "시네마틱 키 비주얼 만들어줘"
  - "캐릭터 일관성 있는 시리즈 이미지"
  - "DTC 광고 이미지(Marketing Studio)"
  Soul·Nano Banana·GPT Image·Seedream·FLUX·Recraft·Marketing Studio 등 계열의 프롬프트 크래프트는
  references/prompt-craft/*.md에 출처와 함께 큐레이션돼 있고, 실제 파라미터(모델 id·해상도·비율·비용)는
  런타임에 라이브 조회합니다. 프롬프트만 필요하면 media-gpt-image-prompt 등 해당 모델의
  프롬프트 스킬을 사용하세요.
version: "1.3.7"
---

# Higgsfield 이미지 생성 (media-higgsfield-image)

> `moai-media` | 라이브 카탈로그 기반 이미지 생성 (코어: `media-higgsfield-core`)

## 개요

Claude에서는 Higgsfield MCP, ChatGPT에서는 공식 Higgsfield 플러그인의 이미지 생성 도구를 호출합니다. 사용자 요청에서 의도를 추출하고 계열 크래프트로 후보를 좁힌 뒤, **파라미터는 현재 연결의 라이브 카탈로그에서 조회**해 생성합니다.

핵심 설계는 코어 스킬 `media-higgsfield-core`에 있습니다:
- 호출 계약: `../media-higgsfield-core/references/call-schema.md`
- 라이브 조회 프로토콜: `../media-higgsfield-core/references/catalog-protocol.md`
- 공통 규칙 R1–R5: `../media-higgsfield-core/references/universal-rules.md`
- 잡·비용·리드백: `../media-higgsfield-core/references/job-lifecycle.md`

## 트리거 키워드

Higgsfield 이미지, Higgsfield Soul, Higgsfield Nano Banana, Higgsfield GPT Image, Higgsfield Seedream, Higgsfield FLUX, Higgsfield Recraft, Higgsfield Marketing Studio, Higgsfield DTC 광고 이미지

## 계열 크래프트 (references/prompt-craft/)

각 파일은 벤더 공식 문서 기반이며 출처·Evidence tier를 답니다. 파라미터가 아니라 **프롬프트 크래프트**만 다룹니다.

| 파일 | 계열 |
|---|---|
| `references/prompt-craft/soul.md` | Soul (공식 프롬프트 공식 부재 → R1–R5 폴백) |
| `references/prompt-craft/nano-banana.md` | Nano Banana (Google 5-part 공식) |
| `references/prompt-craft/openai.md` | GPT Image (openai_hazel 매핑은 unverified) |
| `references/prompt-craft/seedream.md` | Seedream (ByteDance 5원칙) |
| `references/prompt-craft/flux.md` | FLUX (어순 load-bearing, 부정 프롬프트 없음) |
| `references/prompt-craft/recraft.md` | Recraft (global-to-local, 벡터/로고) |
| `references/prompt-craft/marketing-studio.md` | Marketing Studio / DTC Ads (style 선택 워크플로) |

## 워크플로우 (REQ-010 흐름)

### 1단계 — 의도 파악 → 후보 좁히기

사용자 요청에서 subject·용도·톤·리터럴 텍스트 등 슬롯을 수집(→ core `interview-schema.md`)하고, 계열 크래프트로 **후보 모델을 좁힙니다**. 이 단계는 후보를 좁힐 뿐 파라미터를 단정하지 않습니다. 슬롯이 부족하면 직접 실행에서만 현재 앱의 질문 채널로 필요한 항목을 확인합니다. 하위 에이전트는 질문 도구가 보여도 누락 슬롯·선택지·재개 방법을 blocker로 상위에 반환하고, 직접 실행에 채널이 없어도 같은 blocker를 반환합니다.

후보 좁히기 힌트(파라미터가 아니라 계열 선택 힌트):

| 사용자 표현 | 후보 계열 |
|---|---|
| "글자 정확하게", "포스터", "카드뉴스" | GPT Image 또는 Nano Banana Pro |
| "시네마틱", "인물 디테일", "캐릭터 일관성" | Soul |
| "사진처럼", "사실적", "제품 샷" | FLUX |
| "예술적", "독특한 톤" | Seedream |
| "로고", "아이콘", "벡터" | Recraft |
| "DTC 광고", "제품 광고 포맷" | Marketing Studio (ms_image) |

### 2단계 — 현재 연결의 라이브 모델 조회

MCP 연결은 `models_explore(action:'get')`, ChatGPT 공식 플러그인은 `models_get({model_id})`로 후보 모델의 **실제 제약**(aspect_ratios·모델별 파라미터·media role)을 조회합니다. 범위 밖 모델이면 계열 크래프트가 없다는 것을 명시하고 라이브 제약과 R1–R5를 적용합니다. Marketing Studio 계열은 현재 연결의 스타일 목록 도구를 사용합니다.

### 3단계 — 연결별 비용 견적

MCP는 `get_cost: true`, ChatGPT 공식 플러그인은 `estimate_image_cost({params})`로 청구 크레딧을 확인합니다. `adjustments`가 있으면 승인 전에 보여줍니다. 공식 플러그인의 HTTPS 참조 이미지는 견적 중 계정에 업로드될 수 있으므로, 외부 전송 허용을 먼저 확인합니다. 잔액 정지 규칙은 core `job-lifecycle.md`.

### 4단계 — 승인 게이트 (크레딧 소진 전)

견적은 생성 승인이 아닙니다. 크레딧이 실제로 나가기 전 코어 §유료 생성 승인 게이트를 따릅니다 — 프롬프트 전문·모델 id·입력 미디어·확정 옵션·생성 개수·`adjustments`·견적 크레딧·잔액을 보여주고 승인을 받습니다.

- **[HARD] 3단계에서 확보한 `adjustments`를 여기서 보여줍니다.** 6단계 리드백은 이미 돈이 나간 뒤입니다 — 서버가 요청을 바꿨다는 사실은 취소할 수 있을 때 알아야 합니다.
- 서브에이전트로 실행 중이면 승인서를 blocker로 반환합니다. 사용자와 직접 대화하는 세션이면 코어의 런타임 중립 승인 요청 계약을 따릅니다.

### 5단계 — 생성 (generate_image)

승인된 값으로만 실제 `generate_image`를 호출합니다. 도구 이름과 입력 스키마는 현재 연결에서 확인합니다(→ core `call-schema.md`). MCP는 `media_id`/`job_id`를, ChatGPT 공식 플러그인은 승인된 HTTPS 참조도 지원합니다. 외부 전송 허용 없이 URL을 보내지 않습니다.

- **[HARD] 실패해도 새 잡을 만들지 않습니다.** 애매하게 실패하면 반환된 job ID를 현재 연결의 상태 도구로 확인하고, ID조차 없으면 실제 노출된 생성 이력 도구나 Higgsfield 대시보드에서 확인합니다. 기존 잡이 없거나 실패한 것이 확인된 뒤에만 다시 호출합니다.

### 6단계 — 폴링·리드백

MCP는 `job_status`, ChatGPT 공식 플러그인은 `jobs_wait`로 완료를 확인합니다. 공식 플러그인의 생성 도구가 결과 위젯을 이미 보여줬으면 다시 `job_display`를 호출하지 않습니다. 결과 URL과 `adjustments`를 보고합니다.

## Marketing Studio (ms_image) 하드 규칙

`ms_image`는 `style_id`에 기본값이 없어 스타일 없이는 오류입니다. 현재 연결에서 제공하는 Marketing Studio 이미지 스타일 목록 도구로 선택지를 보여주고 사용자가 이름으로 고르게 한 뒤 생성합니다. 스타일을 자동 기본값으로 채우지 않습니다(→ `references/prompt-craft/marketing-studio.md`).

## 범위 밖 모델 폴백 (live lookup)

크래프트 계열에 없는 모델을 요청하면, 계열 특화 크래프트가 없다는 사실을 명시하고 현재 연결의 모델 상세 도구로 제약을 조회한 뒤 공통 규칙 R1–R5를 적용합니다.

## 출력 형식

```
## Higgsfield 이미지 생성 결과
- 모델: [라이브 모델 도구로 확인한 실제 id]
- 프롬프트: [계열 크래프트로 조립된 최종 프롬프트]
- 비율: [라이브 aspect_ratios 중 선택]
- 비용: [연결별 견적 도구가 반환한 credits]
- Job ID / 결과 URL: [연결별 상태 도구가 확인한 완료 결과]
- 서버 조정(adjustments): [있으면 그대로 보고]
```

## 주의사항

- 프롬프트는 계열 크래프트(references/prompt-craft/)의 벤더 공식 컨벤션을 따릅니다.
- 제외 표현은 긍정 장면 묘사로(R1). 리터럴 텍스트는 따옴표+폰트로(R3).
- 모델 id·파라미터를 추측하지 않습니다 — 현재 연결의 라이브 모델 조회 도구로 확인합니다.
- nsfw·초상권·저작권 침해 소지 콘텐츠는 생성하지 않습니다.

## 관련 스킬

| 스킬 | 시점 |
|---|---|
| `moai-media:media-higgsfield-core` | 코어: 호출 계약·라이브 조회·공통 규칙 |
| `moai-media:media-higgsfield-video` | 후속: 이미지를 영상으로 |
| `moai-media:media-gemini-3-image-prompt` | 대안: 프롬프트만 산출 (외부 도구) |
| `moai-media:media-gpt-image-prompt` | GPT Image 2.5 프롬프트 설계 (Higgsfield `gpt_image_2_5` 지원 여부를 현재 연결에서 확인). ChatGPT Work의 Images 2.5 배포와 별도 경로 |
| `moai-marketer:content-card-news` | 후속: 이미지를 카드뉴스에 배치 |

## 출처

- [Higgsfield Skills (공식 agent 문서)](https://github.com/higgsfield-ai/skills)
- [Higgsfield MCP](https://higgsfield.ai/mcp)
- 계열별 프롬프트 크래프트 출처는 각 `references/prompt-craft/*.md`의 Evidence tier·출처 참조.
- 라이브 카탈로그: MCP의 `models_explore` 또는 ChatGPT 공식 플러그인의 모델 조회 도구. 스냅샷은 런타임 계약이 아닙니다.
