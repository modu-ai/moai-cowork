# Midjourney V8 — 비용·호환성 확인

현재 기본 버전은 V8.2입니다. 사용자가 V8.1을 지목하면 그 버전을 유지합니다. 프롬프트를 출력하기 전에 버전별 지원 옵션을 확인합니다.

## 지원하지 않는 옵션

- V8.1·V8.2에서는 Quality 파라미터 `--q`가 지원되지 않습니다. `--q 4`를 고해상도 옵션으로 쓰지 않습니다.
- V8에서는 Omni Reference `--oref`·`--cw`와 Character Reference `--cref` 대신 Edit Model을 사용합니다. 웹에서는 이미지를 **Attach to prompt**에 넣고, Discord에서는 `--edit IMAGE_URL`을 씁니다.
- 기존 옵션이 입력에 들어오면 조용히 다른 의미로 바꾸지 말고, 대체 경로와 결과 차이를 설명합니다. 참조 이미지에서 유지할 특징은 문장으로 명시합니다.

## GPU 시간

[Midjourney 공식 GPU 시간 표](https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo)의 일반적인 예시는 다음과 같습니다.

| 작업 | 대략적인 GPU 시간 |
|---|---:|
| SD 이미지 프롬프트 | 0.8분 |
| HD 이미지 프롬프트 | 1.3분 |
| Edit Model SD 프롬프트 | 1분 |
| Edit Model HD 프롬프트 | 2.3분 |

이 값은 실제 청구를 보장하지 않습니다. 화면비·버전·업스케일 등 작업 조건에 따라 달라집니다. `--sref`·`--hd` 같은 옵션마다 임의의 배수를 정해 곱하지 않습니다. 생성 전 현재 계정의 남은 Fast 시간과 속도 설정을 확인합니다.

## 다른 확인 항목

- `--sref random`의 결과가 마음에 들면 생성 후 확정된 스타일 코드를 저장합니다.
- `--p`는 현재 계정에서 Global Profile이 잠금 해제됐을 때 사용합니다.
- Relax 사용 가능 여부는 현재 요금제와 설정에서 확인합니다.

## 출처

- [Midjourney — Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)
- [Midjourney — Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)
- [Midjourney — GPU Speed](https://docs.midjourney.com/hc/en-us/articles/32016412137741-GPU-Speed-Fast-Relax-Turbo)
