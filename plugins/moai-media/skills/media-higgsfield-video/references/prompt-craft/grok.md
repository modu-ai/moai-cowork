# grok.md — Grok 계열 크래프트 (xAI)

> 대상 모델(라이브 카탈로그 기준): `grok_video`, `grok_video_v15`, `grok_image`
> 파라미터·aspect·duration·media role은 `models_explore(action:'get')`로 라이브 조회.

**Evidence tier:** 1차 ([xAI 영상 생성 문서](https://docs.x.ai/developers/model-capabilities/video/generation), 2026-09-24 재확인). Higgsfield 노출 범위는 별도 라이브 조회 필요.

---

## 공식 영상 API와 Higgsfield 연결의 경계

xAI의 현재 영상 생성 문서는 `grok-imagine-video-1.5`에서 영상에 오디오 트랙이 기본 포함되며 `generate_audio=false`로 끌 수 있다고 명시한다. 참조 영상은 `reference_audios`의 프리셋 `voice_id`와 `<AUDIO_0>` 같은 인덱스 표기도 지원한다. 따라서 과거의 "공식 오디오 문서 없음" 주장은 폐기한다.

이 기능이 Higgsfield의 `grok_video_v15`에 그대로 노출되는지는 별개다. `models_explore`의 실제 입력 스키마에 없는 `generate_audio`·`reference_audios`·`voice_id`를 Higgsfield 호출에 넣지 않는다. 오디오 연출은 현재 연결에서 확인된 프롬프트·옵션 범위에서만 안내한다.

## 공식 예시 (verbatim, docs.x.ai — 라벨 없는 평이한 단문)

- *"A glowing crystal-powered rocket launching from the red dunes of Mars, ancient alien ruins lighting up in the background as it soars into a sky full of unfamiliar constellations."*
- *"Timelapse of a flower blooming in a sunlit garden."*
- image-to-video: *"Make the water crash down and slowly pan out the camera."*

## 참조 문법 주의

xAI의 자체 API에는 `reference_images`와 `reference_audios`가 있다. Higgsfield가 제공하는 참조 role은 별도 스키마이므로 번호 플레이스홀더가 그대로 매핑된다고 가정하지 않는다. 실제 role·param은 `models_explore`로 확인한다.
