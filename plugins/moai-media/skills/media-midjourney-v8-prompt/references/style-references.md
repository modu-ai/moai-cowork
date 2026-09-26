# Midjourney V8 — 스타일·피사체 참조

참조 이미지의 역할을 먼저 구분합니다. **스타일**을 빌릴 때는 Style Reference를, **피사체나 캐릭터**를 유지하거나 이미지를 편집할 때는 Edit Model을 씁니다.

## Style Reference (`--sref`)

`--sref <숫자 코드 또는 이미지 URL>`은 색감·매체·질감·조명 같은 시각적 분위기를 반영합니다. 피사체의 동일성 보장은 아닙니다. `--sw 0~1000`으로 영향력을 조절하며 기본값은 100입니다. 결과가 약하면 강도를 올리고, 본문 내용이 묻히면 낮춥니다.

```text
a quiet lakeside cabin at dusk, soft reflected light --ar 16:9 --sref 1234567890 --sw 200
```

`--sref random`을 썼다면 생성 후 확정된 코드를 저장합니다. 오래된 스타일 코드를 재현할 때만 해당 버전의 `--sv` 지원 범위를 공식 문서에서 확인합니다. V8 기본값을 `--sv 7`로 가정하지 않습니다.

## Edit Model (피사체·캐릭터 참조)

V8.1·V8.2에서는 Edit Model이 Omni Reference와 Character Reference를 대체합니다. 웹에서는 이미지를 Imagine Bar의 **Attach to prompt**에 넣고, Discord에서는 `--edit IMAGE_URL`을 사용합니다. 최대 4개의 참조 이미지를 넣을 수 있습니다. 유지할 특징과 바꿀 특징을 텍스트로 구분합니다.

```text
The same original illustrated fox from the reference image, preserve its cream muzzle and green scarf, walking through a snowy forest --ar 4:5 --edit https://example.com/fox.jpg
```

웹의 Attach to prompt는 이미지 첨부 동작이므로 위 Discord 파라미터를 웹 입력란에 복사할 필요는 없습니다. 사용자가 `--oref`·`--cw`·`--cref`를 가져오면 V8에서는 그대로 넣지 않고 Edit Model 경로를 설명합니다. 예전 숫자 가중치를 새 기능에 1:1로 옮길 수 있다고 주장하지 않습니다.

## Personalization (`--p`)

현재 계정의 Global Profile이 잠금 해제되었으면 `--p`나 특정 프로필 ID를 사용할 수 있습니다. 공식 안내는 이미지 격자에서 좋아하는 이미지를 선택해 잠금을 푸는 절차를 설명합니다. 정해진 ratings 수치를 모든 계정의 승인 기준으로 쓰지 않습니다.

## 출처

- [Midjourney — Style Reference](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference)
- [Midjourney — Edit Model](https://docs.midjourney.com/hc/en-us/articles/48495453462797-Edit-Model)
- [Midjourney — Personalization](https://docs.midjourney.com/hc/en-us/articles/32433330574221-Personalization)
- [Midjourney — Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version)
