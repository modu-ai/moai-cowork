---
name: commerce-detail-page-image
description: >
  한국 이커머스 상세페이지 13섹션 이미지를 생성하고, 실행 환경에 이미지 합성 도구가 있으면 1080×12720 단일 PNG로 합성하는 스킬입니다.
  "상세페이지 이미지 만들어줘", "13섹션 합성 이미지", "상폐 이미지", "1080 12720 합성"처럼 말하면 됩니다.
  commerce-detail-page-copy의 13섹션 카피와 사용자 상품 사진을 받아 섹션별 이미지 프롬프트를 작성하고,
  ChatGPT에서는 사용 가능한 기본 이미지 도구를 우선 확인하고, Images 2.5 요청은 세션의 모델을 확인합니다. Flare·Sunburst API 모델 ID 지정 요청은 별도 API 경로를 확인합니다. 사용자가 Higgsfield를 지정하면 호스트에 맞는 공식 연결로 이미지를 생성한 뒤
  Python과 Pillow가 실행 가능한 환경에서는 1080×12720 세로 합성 PNG를 직접 조립합니다(합성 로직은 이 문서에 인라인 코드로 포함).
version: "1.1.4"
---

# 상세페이지 이미지 합성 (Detail Page Image Composer)

## 개요

13섹션 감정여정 상세페이지 이미지를 생성하고, 합성 도구가 있는 환경에서는 세로 PNG로 만드는 스킬입니다.
호스트에서 실제 사용 가능한 이미지 생성 도구로 섹션 이미지를 만듭니다. Python과 Pillow가 실행 가능할 때만 1080×12720 단일 합성 이미지를 산출하며, 실행하지 못한 합성은 미완료로 보고합니다.

## 트리거 키워드

상세페이지 이미지, 상폐 이미지, 13섹션 이미지, 1080 12720, 상세페이지 합성, 상품 상세 이미지,
combined.png, 상폐 합성본, 이커머스 이미지 합성

## 사전 조건

1. **합성 실행 환경 확인**: 현재 앱의 실행 환경에서 Python과 Pillow를 실제 호출할 수 있는지 확인합니다. 버전 문자열만으로 가능 여부를 판정하지 않습니다. 호출할 수 없으면 사용자에게 패키지 설치를 요구하지 않고, 섹션 이미지와 합성 명세를 제공하며 단일 PNG 합성은 미완료로 기록합니다.

2. **이미지 생성 도구 확인**: ChatGPT Work에서는 현재 앱의 기본 이미지 도구를 확인한다. Images 2.5를 명시했으면 노출된 모델을 확인하고, 모델이 보이지 않으면 정확한 버전을 미확인으로 남긴다. Flare·Sunburst API 모델 ID 지정 요청은 별도 API 경로가 실제 연결된 경우에만 따른다. Higgsfield 지정 시 Claude는 공식 MCP, ChatGPT는 별도로 설치·인증한 Higgsfield 공식 플러그인의 실제 도구를 확인한다.
   - 또는 사용자가 별도로 13장의 섹션 이미지를 준비해서 폴더 경로 제공

3. **상품 사진 1-14장**: 실제 상품 레퍼런스 (옵션이지만 권장)

## 워크플로우

### 1단계: 입력 수집

다음을 확보합니다:
- 13섹션 카피 JSON (`commerce-detail-page-copy` 스킬 출력)
- 상품 사진 1-14장 경로
- 카테고리 (electronics/fashion/food/beauty/home/supplement/pet/kids/handmade/general)
- ProductDNA (선택, `commerce-product-photo-brief` 스킬 출력)
- 출력 디렉토리 (기본: `./commerce-output/{job_id}/`)

### 2단계: 13섹션 이미지 프롬프트 생성

각 섹션의 카피와 카테고리 비주얼 브리프를 합쳐 선택한 이미지 도구용 프롬프트를 작성합니다.
`references/image-prompts.md` 참조 (섹션별 비주얼 언어, 합성 가이드).

각 섹션은 고유한 비주얼 언어를 가집니다:
- **Hero**: cinematic_product_portrait — 풀블리드 + 드라마틱 림라이트
- **Pain**: emotional_photography_no_product — 어두운 톤, 상품 미노출
- **Problem**: clinical_infographic — 깔끔한 인포그래픽
- **Story**: editorial_split_before_after — Before/After 좌우 분할
- **Solution**: product_beauty_shot — 스튜디오 뷰티샷
- **How**: illustrated_step_sequence — 3단계 일러스트
- **Proof**: magazine_spread — 매거진 스프레드
- **Authority**: portrait_with_quote — 인물 포트레이트 + 인용
- **Benefits**: icon_grid_with_lifestyle — 아이콘 그리드 + 라이프스타일
- **Risk**: document_with_seal — 문서·인증 스타일
- **Compare**: split_screen_vs — 50/50 분할 비교
- **Filter**: checklist_visual — 체크리스트 시각화
- **CTA**: product_reveal — 상품과 구매 행동 안내. 할인·마감은 실제 근거가 있을 때만 추가

### 3단계: 이미지 생성

ChatGPT Work에서 기본 이미지 생성 도구가 노출되면 그 도구로 진행합니다. Images 2.5 요청의 정확한 모델은 도구가 표시할 때만 확정하고, Flare·Sunburst API 모델 ID 지정 요청은 별도 API 경로가 확인될 때만 해당 모델로 진행합니다. Higgsfield 지정 시 호스트에 맞는 공식 연결의 모델·도구·비용을 확인하고 유료 호출 전에 사용자 승인을 받습니다. Higgsfield는 채팅 첨부 파일을 생성 도구가 직접 읽지 못하므로 상품 참조 사진은 별도 업로드 완료 또는 기존 자산 확인 후에만 생성 호출에 넘깁니다. 어느 경로도 사용할 수 없으면 생성 불가 섹션을 보고하고 사용자가 준비한 이미지를 받습니다.

생성 전략:
- 각 섹션 너비: **1080px**
- 섹션별 높이: `references/sections-spec.md` 표 참조 (Hero 1600-Filter 700)
- 카테고리 비주얼 브리프(electronics/fashion/...) 모든 프롬프트에 주입
- 상품 레퍼런스 사진은 선택한 도구가 해당 입력을 지원할 때만 전달

생성 결과를 `output_dir/{job_id}/sections/01_hero.png` 부터 `13_cta.png` 까지 저장.

생성 실패 시 해당 섹션을 실패로 기록합니다. 임시 합성본에 빈 영역을 넣을 수 있지만 완성본으로 보고하지 않습니다.

### 4단계: 1080×12720 합성 (Pillow 인라인 조립)

별도 스크립트 없이, 아래 Pillow 코드를 그대로 실행해 13장을 세로로 이어붙입니다.
동작: (1) 01_hero~13_cta 순서 로드 → (2) 너비 1080으로 리사이즈(비율 유지 + 중앙 크롭) →
(3) 섹션별 표준 높이로 조정 → (4) 세로 스택 → (5) 누락 섹션은 `(40,40,40)` 다크 플레이스홀더로 대체하고 `combined-draft.png`로 저장.

```python
from PIL import Image
from pathlib import Path

WIDTH = 1080
# (파일명 슬러그, 표준 높이) — sections-spec.md 표와 동일
SECTIONS = [
    ("01_hero", 1600), ("02_pain", 800), ("03_problem", 800), ("04_story", 1200),
    ("05_solution", 800), ("06_how", 900), ("07_proof", 1420), ("08_authority", 800),
    ("09_benefits", 1200), ("10_risk", 800), ("11_compare", 800), ("12_filter", 700),
    ("13_cta", 900),
]
PLACEHOLDER = (40, 40, 40)

def fit(img, w, h):
    # 비율 유지 리사이즈 후 중앙 크롭으로 정확히 w×h 맞춤
    scale = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
    left, top = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((left, top, left + w, top + h))

sections_dir = Path("./commerce-output/JOB_ID/sections")   # 실제 job_id로 치환
sections_dir.mkdir(parents=True, exist_ok=True)
total_h = sum(h for _, h in SECTIONS)
canvas = Image.new("RGB", (WIDTH, total_h), PLACEHOLDER)
failed, y = [], 0
for slug, h in SECTIONS:
    p = sections_dir / f"{slug}.png"
    if p.exists():
        with Image.open(p) as source:
            canvas.paste(fit(source.convert("RGB"), WIDTH, h), (0, y))
    else:
        failed.append(slug)   # 누락 → 다크 플레이스홀더 그대로 유지
    y += h
output = sections_dir.parent / ("combined-draft.png" if failed else "combined.png")
canvas.save(output)
print({"size": f"{WIDTH}x{total_h}", "output": str(output), "failed_sections": failed})
```

높이 표준값은 `references/sections-spec.md`를, 섹션별 비주얼 언어는 `references/image-prompts.md`를 참조합니다.

### 5단계: 출력 보고

```json
{
  "job_id": "a1b2c3d4",
  "output_dir": "/abs/.../commerce-output/a1b2c3d4",
  "combined": "/abs/.../combined.png",
  "sections": [
    "/abs/.../sections/01_hero.png",
    "...",
    "/abs/.../sections/13_cta.png"
  ],
  "failed_sections": [],
  "elapsed_sec": 0,
  "size": "1080x12720"
}
```

`failed_sections`가 비어있지 않으면 `combined-draft.png`는 검토용이라고 밝히고 사용자에게 다음을 안내:
- 어떤 섹션이 실패했는지
- 같은 `--output --job-id`로 재실행 시 자동 재개되는지 (재개는 사용자가 수동으로 해당 섹션만 재생성)

## 출력 파일 구조

```
./commerce-output/{job_id}/
├── analysis.json              # 13섹션 카피 + 프롬프트 + ProductDNA
├── sections/                   # 13장 섹션 (1080×가변)
│   ├── 01_hero.png            (1080×1600)
│   ├── 02_pain.png            (1080×800)
│   ├── ...
│   └── 13_cta.png             (1080×900)
└── combined.png                # 1080×12720 세로 합성본
```

## 합성 코드 조정 포인트

4단계 인라인 Pillow 코드에서 다음 값만 바꾸면 됩니다:

- `WIDTH`: 출력 너비 (기본 1080)
- `PLACEHOLDER`: 누락 섹션 색 (기본 `(40, 40, 40)`)
- `SECTIONS`: 섹션 순서·표준 높이 (기본 13섹션, `references/sections-spec.md`와 동일)
- `sections_dir`: 실제 job_id 경로로 치환

> 이 스킬은 부재 스크립트(compose.py) 참조를 원칙 A(프롬프트/인라인 코드 경로)로 대체했습니다 — 합성은 위 Pillow 코드를 직접 실행합니다.

## 사용 예시

- "이 카피 결과로 13섹션 이미지 합성해줘"
- "상품사진 5장으로 상세페이지 1080 12720 만들어줘"
- "electronics 카테고리, 무선 이어폰 상세페이지 이미지 풀세트"

## 관련 스킬

- `moai-seller:commerce-detail-page-copy` — 13섹션 카피 생성 (이 스킬 입력)
- `moai-seller:commerce-product-photo-brief` — 상품 사진 사전 분석
- 13섹션 이미지 생성 — 현재 앱 이미지 도구 또는 호스트에 맞게 인증된 Higgsfield 공식 연결
- `moai-seller:commerce-marketplace-coupang` — 채널별 이미지 규격 가이드

## 이 스킬을 사용하지 말아야 할 때

- 카피만 필요할 때: `commerce-detail-page-copy` 단독 사용
- 단일 상품 컷만 필요할 때: 사용 가능한 이미지 도구 직접 호출
- 영상 생성: 호스트에 맞게 인증된 Higgsfield 공식 연결에서 해당 도구가 노출될 때만 호출
- shadcn/ui 기반 웹 상세페이지: `moai-seller:commerce-product-detail`

## 라이선스

MIT.
