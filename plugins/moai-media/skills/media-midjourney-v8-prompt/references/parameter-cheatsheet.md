# Midjourney V8 — 파라미터 요약

[공식 Version 표](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)의 현재 기본 버전은 V8.2입니다. 사용자가 V8.1을 지정하면 `--v 8.1`을 포함해 그 버전으로 작성합니다. 앱 설정에서 다른 기본 버전을 고른 경우에는 현재 설정을 확인합니다.

| 목적 | V8.1·V8.2에서 쓰는 방법 | 확인 사항 |
|---|---|---|
| 화면비 | `--ar W:H` | SD 최대 14:1, HD 최대 4:1. 21:9 가능 |
| 자동 스타일 줄이기 | `--raw` | 사용자 요청이 있을 때 추가 |
| 고해상도 | `--hd` | 2K 출력. GPU 시간 확인 |
| 스타일 강도 | `--s 0~1000` | 기본값 100 |
| 다양한 시안 | `--c 0~100` | 필요한 경우만 |
| 제외 요소 | `--no <요소>` | 원하는 장면을 먼저 긍정형으로 설명 |
| 스타일 참조 | `--sref <코드 또는 URL>` | 강도 조절은 `--sw 0~1000`, 기본값 100 |
| 개인 스타일 | `--p [프로필 ID]` | 계정의 프로필 잠금 해제 확인 |
| 이미지 참조·편집 | 웹의 Attach to prompt 또는 Discord `--edit IMAGE_URL` | Edit Model은 이미지 최대 4개 |

`--q` Quality 파라미터는 V8.1·V8.2에서 지원하지 않습니다. V8의 캐릭터·객체 참조에 `--oref`·`--cw`·`--cref`를 쓰지 않습니다. 사용자가 예전 옵션을 적었다면 현재 Edit Model 경로를 설명하고, 의도한 피사체 특징을 확인합니다.

## Style Reference

`--sref`는 색·매체·질감·조명 같은 스타일에 영향을 줍니다. 피사체 자체를 복제하려는 요청에는 Edit Model을 씁니다. `--sw`는 0~1000, 기본값 100입니다. `--sref random`을 쓰면 생성 뒤 확정된 코드를 저장합니다. `--sv`는 과거 스타일 참조 결과를 재현할 때만 공식 버전별 문서를 확인하고 지정합니다. V8의 기본값을 `--sv 7`로 단정하지 않습니다.

## GPU 시간

일반적인 공식 예시는 SD 0.8분, HD 1.3분, Edit Model SD 1분, Edit Model HD 2.3분입니다. 옵션별 고정 배수나 곱연산으로 견적을 만들지 않습니다. 자세한 내용은 `cost-traps.md`와 현재 계정의 사용량을 확인합니다.

## 출처

- [Midjourney — Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)
- [Midjourney — Parameter List](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List)
- [Midjourney — Aspect Ratio](https://docs.midjourney.com/hc/en-us/articles/31894244298125-Aspect-Ratio)
- [Midjourney — Raw](https://docs.midjourney.com/hc/en-us/articles/32634113811853-Raw)
- [Midjourney — Style Reference](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference)
- [Midjourney — Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)
