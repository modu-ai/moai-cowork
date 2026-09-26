# training-photo-guide.md — Soul 학습 사진 기준

> `media-higgsfield-identity` | Soul Character 학습에 넣을 사진의 품질 기준과 실패 원인.
> Element 경로에는 적용되지 않는다(Element는 1장이면 충분하다).

**Evidence tier:** 1차 (Higgsfield 공식 CLI 스킬 `higgsfield-soul-id` v0.12.0 및 웹 도움말). 사진 품질 기준은 CLI 스킬의 `references/photo-guide.md` · `references/troubleshooting.md` 기반.

---

## 1. 수량

- **공식 CLI 스킬:** 5~20장. 해당 스킬은 8~12장을 권장한다.
- **Higgsfield 웹 도움말:** 20~80장. 웹 학습 화면의 기준이다.
- **MCP·ChatGPT 연결:** 현재 노출된 학습 도구의 스키마나 연결별 공식 안내에서 제한을 먼저 확인한다. 확인하지 못하면 5~19장만으로 학습을 제출하지 않는다.
- 수량을 맞추려고 비슷한 사진을 늘리지 않는다. 다양한 각도와 조명을 확보한다.

---

## 2. 내용

- 얼굴이 선명하고 **눈이 보일 것**.
- **한 장에 한 사람만.**
- 강한 필터·선글라스 없이.

---

## 3. 다양성 (품질을 가르는 축)

다양성이 높을수록 identity 포착이 좋아진다. 아래 네 축을 골고루 섞는다.

| 축 | 섞을 것 |
|---|---|
| 각도 | 정면, 3/4 좌, 3/4 우, 약간 위/아래 |
| 조명 | 실내, 실외, 부드러운 빛, 강한 빛 |
| 표정 | 무표정, 미소, 말하는 중 |
| 거리 | 얼굴 클로즈업, 상반신, 전신 |

---

## 4. 화질

- 초점이 맞고 선명할 것.
- 해상도 1024×1024 이상 권장.
- JPEG 또는 PNG.

---

## 5. 피할 것

- 단체 사진 — identity를 혼동시킨다.
- 평소 하지 않는 진한 메이크업.
- 코스튬·코스프레.
- 얼굴을 가리는 모자.
- 같은 포즈의 반복.

---

## 6. 실패 진단

| 증상 | 원인 | 조치 |
|---|---|---|
| `Minimum Basic plan required` | 무료 플랜 | 유료 플랜 필요를 사용자에게 알린다. 제출 전에 알리는 것이 낫다 |
| `Training failed` | 선택한 연결의 최소 수량 미달 / 지나치게 단조로움 / 선글라스·모자 가림 / 단체 사진 / 이미지가 아닌 업로드 타입 | 연결별 제한과 사진 품질을 확인하고 재학습 |
| 학습이 오래 걸림 | 정상 (약 10분, 큐 상황에 따라 더 걸릴 수 있음) | 조용히 대기. 진행 상황을 반복 보고하지 않는다 |
| 인증 만료 | 세션 만료 | MCP 커넥터 재인증 |

> 제출 **전** 연결별 수량 제한과 사진 품질을 확인한다. 제한 미확인 또는 같은 각도 사진뿐이라면 학습을 걸기 전에 사용자에게 알린다.

출처: [공식 CLI 스킬](https://github.com/higgsfield-ai/skills/blob/main/higgsfield-soul-id/SKILL.md) · [공식 웹 도움말](https://higgsfield.ai/creator-hub/help-center/ai-models/how-do-i-create-and-use-a-soul-id-character)
