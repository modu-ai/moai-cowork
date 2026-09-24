# seedance.md — Seedance 계열 크래프트 (ByteDance)

> 대상 모델(라이브 카탈로그 기준): `seedance_2_5`, `seedance_2_0`, `seedance_2_0_mini`, `seedance1_5`
> 파라미터·aspect·duration·media role은 현재 연결의 모델 상세 도구로 라이브 조회.

**Evidence tier:** 1차 (이전 세대: BytePlus ModelArk EN + Volcengine ZH, 2.5: Higgsfield 공식 프롬프트 가이드)
출처: https://docs.byteplus.com/en/docs/ModelArk/2222480 · https://higgsfield.ai/blog/seedance-2-5-prompting-guide

모델 세대별 안내를 구분한다. 아래 BytePlus·Volcengine 문구의 정밀 타이밍 경고를 Seedance 2.5 전체에 그대로 적용하지 않는다.

---

## 이전 세대 공식 안내 (1차)

`Precise subject + action details + scene/environment + lighting & color tone + camera movement + visual style + image quality + constraints`
가이드는 프롬프트를 **"engineering-style instructions"**로 규정한다(창작 글쓰기가 아님).
Seedance 1.5 Pro: `Subject + motion + environment + camera movement/cuts + aesthetic description + sound`(뒤 4개 선택).

## 이전 Seedance 안내의 정밀 타이밍 경고

> *"The model's support for precise timing (such as 0–3 seconds) is unstable, and forcibly limiting duration may lead to abnormal generation results."*
> *"Do not impose strict limits on the duration of each segment; prioritize allowing the model to naturally generate the pacing."*

이전 가이드는 초 단위 결과를 강제하기보다 `Shot 1 / Shot 2 / Shot 3`처럼 샷을 구분하고 자연스러운 속도를 허용하라고 설명한다. 이 경고는 프레임 단위 정확도를 보장하지 않는다는 뜻이며, 모든 Seedance 모델에서 시간 범위를 금지한다는 뜻은 아니다. 다음 절의 2.5 지침과 구분해 적용한다.

## Seedance 2.5 — 현재 Higgsfield 안내

[Higgsfield의 Seedance 2.5 프롬프트 가이드](https://higgsfield.ai/blog/seedance-2-5-prompting-guide)는 GLOBAL STYLE·SCENE·CHARACTERS·LOCATION·FIRST FRAME AND BLOCKING·샷별 동작·CAMERA·LIGHTING·AUDIO를 필요한 만큼 구분한다. 여러 샷이면 `Shot 1`·`Shot 2`로 구분하고 컷 위치와 각 샷의 동작을 적는다. 가이드의 실전 예시에는 시간대와 사건 시점도 나오지만, 이를 프레임 단위로 정확히 지키는 보장으로 읽지 않는다. 참조는 일관성이 필요한 인물·제품·장소별로 용도를 명시하고 무조건 최대 개수를 채우지 않는다.

이 세션의 Higgsfield `models_get(model_id="seedance_2_5")`는 `mode`에 `t2v`·`omni_reference`·`video_edit`·`video_extension`, 길이 4~30초, 해상도 `480p`·`720p`·`1080p`, `generate_audio` 기본값 `true`를 반환했다. 이는 이 연결의 조회 결과이며 다른 앱·계정에서도 같다고 가정하지 않는다. 실제 입력 역할과 옵션은 생성 직전 연결 스키마로 확인한다.

## @-mention 참조 시스템 (1차, verbatim)

- `Reference <Subject_N> in <Image_N> to generate...` / `Reference <Action/Camera_movement/Style/Sound_effect> in <Video_N>`
- 실무(공식 사례)에서 `@Image 1` / `@Video 1` / `@Audio 1`로 산문에 인라인, **각자 용도를 명시** — "use the girl in @Image 1 **as the main character**", "use @Image 2 **as the dormitory scene style reference**".
- 이는 API 필드가 아니라 프롬프트 TEXT다 — Higgsfield `prompt` 문자열로 직접 전이된다. `medias[]` role은 *어느 파일*이 Image 1/Video 1인지 바인딩하고, *용도 진술*은 산문에 남는다.

## 브래킷 컨벤션 (1차, "Special Formatting Standards")

| 채널 | 구분자 |
|---|---|
| Music | `（parentheses）` |
| Sound effects | `<angle brackets>` |
| Dialogue | `{curly braces}` |
| Subtitles | `【square brackets】` |

공식 예시: `{How did the exam go? Did you pass?}`.

## 캐릭터 드리프트 회피 (1차)

- *"Use 2–3 clear and stable static features … to describe the subject."*
- *"Too Many Reference Characters: Limit to 4; generate in groups if needed."*
- 권장 asset 예산: 캐릭터 1–2 + 씬 1 + 카메라 참조 영상 1 + 오디오 1. 슬롯을 다 채우면 *"feature prioritization confusion."*

**Gap(이전 세대 자료 범위)**: 위 ByteDance 자료에서는 흔한 오디오 품질 키워드(reverb/muffled/echo)의 공식 효과를 확인하지 못했다. 이를 모든 Seedance 세대의 기능 부재로 단정하지 않는다. 실제 param·role은 현재 연결의 모델 상세·생성 도구에서 확인한다.
