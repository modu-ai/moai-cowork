# Changelog

모든 주목할 만한 변경사항은 이 파일에 기록됩니다.

형식: [Keep a Changelog 1.1.0](https://keepachangelog.com/ko/1.1.0/) · 버저닝: [Semantic Versioning 2.0.0](https://semver.org/lang/ko/)

## 버전 통일 원칙 (HARD)

아래 82개 지점의 버전 표기는 **항상 완전히 동일**합니다:
- `.claude-plugin/marketplace.json` (`metadata.version`) × 1
- `<plugin>/.claude-plugin/plugin.json` (`version`) × 16
- `<plugin>/skills/<skill>/SKILL.md` (`metadata.version`) × 65

상세 정책: `CLAUDE.local.md` § 1 참조.

## 엔트리 템플릿

```markdown
## [X.Y.Z] - YYYY-MM-DD

### Added
- 신규 기능/스킬/플러그인 추가 사항 (파일 경로 포함)

### Changed
- 기존 기능 동작/인터페이스 변경 사항 (이유 명시)

### Deprecated
- 다음 메이저 릴리스에서 제거 예정인 기능

### Removed
- 이번 릴리스에서 삭제된 기능/파일

### Fixed
- 버그 수정 내역 (증상 → 원인 → 해결)

### Security
- 보안 취약점 수정 (CVE 번호 있으면 명시)

### Breaking
- 사용자 조치 필요 사항 (마이그레이션 가이드 포함)

### Migration
- 업그레이드 절차 (필수 명령어, 설정 변경)
```

작성 규칙:
- 모든 항목은 **사용자가 체감할 변화** 기준으로 서술 (내부 리팩터는 생략 가능)
- 파일 경로는 백틱으로 감싸기: `moai-core/skills/moai/SKILL.md`
- 증상/원인/해결을 명확히 분리하여 기술
- 관련 커밋·이슈·PR 번호가 있으면 `(#123, abc1234)` 형식으로 부기

---

## [1.2.0] - 2026-04-14

공식 MINOR 릴리스. v1.1.0~v1.1.3의 점진적 변경을 안정 버전으로 집약하여 배포.

### Highlights

- **신규 플러그인 `moai-media`** — AI 미디어 스튜디오 (이미지·영상·음성 통합)
- **Google Nano Banana 공식 전환** — Imagen 4 → Gemini 3 Image Preview (Pro + 2 체제)
- **영상은 Kling 단일화** — fal.ai 기반 숏폼·립싱크 커버
- **음성은 ElevenLabs 공식 MCP** — TTS, 32개 언어 더빙, ConvAI
- **fal.ai 게이트웨이** — Flux·Recraft·Hailuo·Luma·Pika·MiniMax Music 1000+ 모델 단일 접점
- **전 저장소 버전 통일 88 지점** → **1.2.0**

### Added

- 플러그인 `moai-media` (5 스킬)
  - [`nano-banana`](moai-media/skills/nano-banana/SKILL.md): Google Gemini 3 Image Preview 공식 2종 (`gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview`)
  - [`ideogram`](moai-media/skills/ideogram/SKILL.md): Ideogram 3.0 한국어 타이포 (fal.ai)
  - [`kling`](moai-media/skills/kling/SKILL.md): Kling 3.0 숏폼 영상 (fal.ai, 립싱크·다국어)
  - [`elevenlabs`](moai-media/skills/elevenlabs/SKILL.md): ElevenLabs 공식 MCP (TTS·음성복제·더빙·ConvAI)
  - [`fal-gateway`](moai-media/skills/fal-gateway/SKILL.md): fal.ai 1000+ 모델 통합 게이트웨이
- 번들 MCP 서버 2종 (`moai-media/.mcp.json`)
  - `fal-ai` (hosted HTTP MCP at `https://mcp.fal.ai/mcp`)
  - `elevenlabs` (local stdio via `uvx elevenlabs-mcp`)
- API 키 3종 통합 지원
  - `GEMINI_API_KEY` (nano-banana 전용 + 레거시 `NANO_BANANA_API_KEY` 호환)
  - `FAL_KEY` (ideogram / kling / fal-gateway 공유)
  - `ELEVENLABS_API_KEY` (elevenlabs)
- `moai-media/scripts/generate_image.py` v4.3 — Python 3.13+ 타입힌트, REST camelCase 준수, 서로게이트 sanitize
- 문서: `CLAUDE.local.md` § 4 MCP 번들 정책, § 5 외부 API 모델 ID 업데이트 정책
- 루트 `README.md` 전면 갱신 (17 플러그인 / 70 스킬 / moai-media 상세 섹션)

### Changed

- **공식 Nano Banana 2종 체제 확정**
  - `nano-banana-pro` → `gemini-3-pro-image-preview` (2K 기본, 텍스트 SOTA)
  - `nano-banana-2` → `gemini-3.1-flash-image-preview` (1K 기본, 비용 효율)
  - Ultra·cheap·2.5-flash 등 부가 별칭은 제거 → Pro/2로 자동 승격 (코드 무수정 호환)
- **API 호출 스펙** (공식 문서 `ai.google.dev/gemini-api/docs/image-generation` 100% 정합)
  - 엔드포인트 `:predict` → `:generateContent`
  - 페이로드 `numberOfImages` + top-level `aspectRatio` → `imageConfig.aspectRatio` + `imageSize`
  - REST 응답 `predictions[].bytesBase64Encoded` → `candidates[].content.parts[].inlineData.data`
  - 화면비 공식 14종 (`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1`)
  - 해상도 `"512"` / `"1K"` / `"2K"` / `"4K"`
- `generate_image.py` 이관: `moai-content/scripts/card-news/` → `moai-media/scripts/`
  (v3.0 Imagen 4 → v4.3 Gemini 3 Image Preview)
- `moai-content/skills/card-news/SKILL.md`: 이미지 생성을 `moai-media/nano-banana` 위임 구조로 전환
- `moai-core/skills/moai/references/core/init-protocol.md`: API 키 테이블 4개 → 6개 확장
- `.claude-plugin/marketplace.json`: `moai-media` 엔트리 추가

### Removed

- Veo 3.1 관련 참조 (영상은 Kling 단일화)
- `gemini-2.5-flash-image` 모델 매핑
- `nano-banana-ultra` 별칭 및 `ULTRA_ALIASES` 상수
- `moai-content/scripts/card-news/` 디렉토리 (moai-media로 이관)
- v1.0.x 잔존 로컬 태그 (v1.1.0~v1.3.0) — marketplace 버전 체계와 불일치하여 정리

### Migration

v1.0.x 사용자 조치 3단계:

1. **마켓플레이스 새로고침**
   ```
   /plugin marketplace update cowork-plugins
   /plugin install moai-media@cowork-plugins
   ```

2. **Gemini API 업그레이드**
   - Pay-as-you-go 결제 활성화 필수 (Nano Banana Pro/2 Free Tier 불가)
   - `NANO_BANANA_API_KEY` 그대로 사용 가능 (자동 인식), 혹은 `GEMINI_API_KEY`로 재명명 권장

3. **신규 API 키 (선택, moai-media 전체 사용 시)**
   - `FAL_KEY` — [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys) ($5 무료 크레딧)
   - `ELEVENLABS_API_KEY` — [elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys) (무료 10K char)
   - `uv` 설치 (ElevenLabs MCP용): `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Breaking

- **이미지 모델 ID 변경**: 기존 `imagen-4.0-*` 하드코딩은 Pro/2로 자동 승격되나, 장기적으로 `gemini-3-pro-image-preview` / `gemini-3.1-flash-image-preview` 직접 사용 권장
- **엔드포인트 변경**: 자체 스크립트를 복사·수정하여 사용하던 사용자는 `:predict` → `:generateContent` 및 페이로드 스키마 업데이트 필요 (참고: `moai-media/scripts/generate_image.py` v4.3)
- **무료 티어 불가**: Gemini 무료 키로 Nano Banana 호출하던 워크플로우는 Pay-as-you-go 전환 필요
- **`google-media` 스킬 경로 없음**: v1.1.0 잠깐 존재했던 `moai-media/skills/google-media/` 경로는 `nano-banana`로 개명됨 (v1.1.0 직후 설치한 극소수 사용자만 해당)

### 변경 이력 (v1.1.x 누적)

v1.2.0에 집약된 중간 릴리스:
- v1.1.0: moai-media 초기 릴리스 (6 스킬, google-media 포함)
- v1.1.1: google-media → nano-banana 개명, Veo 제거, 화면비 공식 14종 정정
- v1.1.2: Pro + 2 체제로 축약 (gemini-2.5-flash-image 제거)
- v1.1.3: nano-banana-ultra 제거, Ultra 별칭 자동 승격

---

## [1.1.3] - 2026-04-14

### Removed

- **`nano-banana-ultra` 별칭 제거** — 공식 라인업을 Pro + 2 **단 두 가지**로 최종 확정
- `ULTRA_ALIASES` 상수 및 `is_ultra` 분기 로직 삭제 (`scripts/generate_image.py`)
- 4K 해상도 자동 선택 로직 제거 — 필요 시 스크립트에서 `imageSize` 직접 지정
- `moai-content/skills/card-news/SKILL.md`의 Ultra 옵션 제거

### Changed

- **자동 승격 테이블 확장** (무수정 호환)
  - `"nano-banana-ultra"`, `"ultra"` → `gemini-3-pro-image-preview` (Pro로 승격)
  - `"nano-banana"`, `"cheap"` → Pro / 2로 승격 (v1.1.2 동일)
- 경고 메시지 개선: 제거된 별칭 사용 시 자동 전환 사실을 stderr로 명시
- `generate_image.py` v4.2 → v4.3 — MODEL_MAP·해상도 선택 로직 단순화
- `nano-banana` SKILL.md 비용 표 Pro/2 기준으로 재작성

### Migration

기존 `nano-banana-ultra` 호출 코드는 **무수정 작동** — 자동으로 Pro 2K로 처리되며 경고 출력. 4K가 필요하면 스크립트에서 `imageSize` 필드를 직접 `"4K"`로 수정.

---

## [1.1.2] - 2026-04-14

### Changed

- **`nano-banana` 스킬 공식 모델 2종 체제로 단순화**
  - 공식 라인업: `nano-banana-pro` (`gemini-3-pro-image-preview`) + `nano-banana-2` (`gemini-3.1-flash-image-preview`) **두 가지만**
  - `nano-banana-ultra`는 Pro의 4K 프리셋 (별도 모델 아님)
  - v1.1.1에서 도입한 `gemini-2.5-flash-image` (원조 Nano Banana) 제거 — 사용자 혼선 방지
- **레거시 별칭 자동 승격**
  - `"nano-banana"` 별칭 → `gemini-3-pro-image-preview` (v1.1.1에서는 `gemini-2.5-flash-image`)
  - `"cheap"` 별칭 → `gemini-3.1-flash-image-preview` (v1.1.1에서는 `gemini-2.5-flash-image`)
  - 사용자 코드 무수정 작동 보장
- **`image_size` 필수 적용** — 모든 요청에 `imageConfig.imageSize` 포함 (2.5-flash 미지원 케이스 삭제)
- **`generate_image.py` v4.1 → v4.2** — MODEL_MAP 정리, is_ultra 로직 단순화

### Fixed

- README 스킬 설명 "Pro/2/원조" → "Pro + 2, 2종만"으로 정확화
- SKILL.md 모델 카탈로그 표를 Pro/2/Ultra 3행으로 축소

### Migration

기존 사용자 조치 없음. `nano-banana` / `cheap` 별칭을 쓰던 코드는 그대로 작동 (자동 승격).

---

## [1.1.1] - 2026-04-14

### Changed

- **`moai-media` 스킬 구조 개편** (Google 공식 문서 재확인 반영)
  - `google-media` 스킬 → **`nano-banana`**로 개명 및 **이미지 전용**으로 스코프 축소
  - 영상 생성은 **`kling` 스킬로 단일화** — Veo 3.1 참조 모두 제거
  - 결과: 이미지는 `nano-banana` (Gemini) / `ideogram` (fal.ai), 영상은 `kling` 단독
- **Gemini 이미지 모델 카탈로그 공식화** (공식 문서 `ai.google.dev/gemini-api/docs/image-generation` 기준)
  - `gemini-2.5-flash-image` 모델 신규 추가 — 원조 Nano Banana, 최저가 **$0.039/img**
  - `nano-banana` 별칭 매핑: → `gemini-2.5-flash-image`
  - 모델 별 기본 해상도 자동 선택: Pro=2K, 2=1K, 원조=디폴트, Ultra=4K
- **공식 화면비 14종 리스트 재정의**
  - 구 리스트 (잘못됨): `9:21`, `3:5`, `2:1`, `1:2` 포함
  - 신 리스트 (공식): `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1`
- **REST API 페이로드 정합화**
  - camelCase로 통일 (`responseModalities`, `imageConfig`, `aspectRatio`, `imageSize`) — 공식 REST 스펙 준수
  - 응답 파싱은 `inlineData` 우선, `inline_data` 폴백
  - `imageSize` 지원 값 공식화: `"512"`, `"1K"`, `"2K"`, `"4K"` (이전에 `"512"` 누락)
- **`generate_image.py` v4.0 → v4.1**
  - 위 변경사항 반영, MODEL_MAP에 `"nano-banana"` / `"cheap"` 별칭 추가
  - `gemini-2.5-flash-image`는 `image_size` 미지원 → 페이로드에서 생략 처리 로직 추가

### Fixed

- **공식 문서 불일치 수정** — 기존 v1.1.0에서 파생 지식 기반으로 작성한 화면비 리스트가 공식 스펙과 달랐음. WebFetch로 공식 문서 재확인 후 전면 정정.
- `moai-core/init-protocol.md`의 "moai-media/google-media 스킬" 참조를 `nano-banana`로 수정

### Removed

- `moai-media/skills/google-media/` 스킬 디렉토리 전체 (→ `nano-banana`로 개명)
- Veo 3.1 관련 모든 참조:
  - README.md 스킬 카탈로그·영상 선택 가이드
  - CONNECTORS.md API 설명
  - plugin.json keywords (`"veo"` 제거)
  - marketplace.json 플러그인 description
  - 기타 SKILL.md 크로스 레퍼런스
- `plugin.json` keywords에서 `"veo"` 제외

### Migration

v1.1.0에서 방금 설치한 사용자도 즉시 업데이트 필요:

```
/plugin marketplace update cowork-plugins
```

기존 `google-media` 호출 코드가 있다면 **`nano-banana`**로 경로 변경:
- 스킬 호출: `/moai-media google-media` → `/moai-media nano-banana`
- SKILL.md 참조: `moai-media/skills/google-media/` → `moai-media/skills/nano-banana/`

영상 생성이 필요하면 **`kling` 스킬** 사용:
- 숏폼·릴스·쇼츠: `fal-ai/kling-video/v3/text-to-video`
- 립싱크 프리미엄: Kling Pro 모드

### Breaking

- **스킬 경로 변경**: `moai-media/skills/google-media/` → `moai-media/skills/nano-banana/`
- **Veo 사용 불가**: v1.1.0에서 `veo-3.1-generate-preview` 호출하던 워크플로우는 `kling` 또는 외부 Veo 직접 호출로 마이그레이션 필요

---

## [1.1.0] - 2026-04-14

### Added

- **신규 플러그인 `moai-media`** — AI 미디어 스튜디오 (이미지·영상·음성 통합)
  - [`moai-media/skills/google-media/`](moai-media/skills/google-media/SKILL.md): Google Gemini 3 Image Preview + Veo 3.1 통합 스킬
    - Nano Banana Pro (`gemini-3-pro-image-preview`, 2K), Nano Banana 2 (`gemini-3.1-flash-image-preview`, 1K), Nano Banana Ultra (Pro + 4K)
    - Veo 3.1 Standard/Fast 영상 (최대 8초, 1080p, 오디오 자동 생성)
    - 단일 `GEMINI_API_KEY`로 이미지 + 영상 + 텍스트 모두 호출
  - [`moai-media/skills/ideogram/`](moai-media/skills/ideogram/SKILL.md): Ideogram 3.0 (한국어 타이포그래피 렌더링 업계 최고)
  - [`moai-media/skills/kling/`](moai-media/skills/kling/SKILL.md): Kling 3.0 (숏폼 영상, 다국어 립싱크, Veo 대비 1/5 가격)
  - [`moai-media/skills/elevenlabs/`](moai-media/skills/elevenlabs/SKILL.md): ElevenLabs 공식 MCP (TTS, 음성복제, 32개 언어 더빙, ConvAI)
  - [`moai-media/skills/fal-gateway/`](moai-media/skills/fal-gateway/SKILL.md): fal.ai 통합 MCP 게이트웨이 (Flux, Recraft, Hailuo, Luma, Pika, MiniMax Music 등 1000+ 모델)
- **MCP 서버 자동 등록** — `moai-media/.mcp.json`에 2종 사전 구성
  - `fal-ai` (hosted HTTP MCP at `https://mcp.fal.ai/mcp`, `FAL_KEY` 인증)
  - `elevenlabs` (local stdio MCP via `uvx elevenlabs-mcp`, `ELEVENLABS_API_KEY` 주입)
- **API 키 2종 신규 지원**: `FAL_KEY`, `ELEVENLABS_API_KEY` (기존 `NANO_BANANA_API_KEY` 유지)
- **4K 이미지 해상도** 지원 (`image_size="4K"`, Nano Banana Ultra 전용)
- **14종 화면비 지원** (1:1 ~ 21:9, Gemini 3 Image Preview 기본 스펙)
- [`moai-media/CONNECTORS.md`](moai-media/CONNECTORS.md): API 키·MCP·커넥터 통합 가이드

### Changed

- **Google "Nano Banana" 브랜드 재정의 반영** (2026 Q1 공식 공지 반영)
  - 모델 ID 매핑: `imagen-4.0-generate-001` → **`gemini-3-pro-image-preview`**
  - 모델 ID 매핑: `imagen-4.0-fast-generate-001` → **`gemini-3.1-flash-image-preview`**
  - 엔드포인트 변경: `:predict` → **`:generateContent`**
  - 파라미터 스키마: `numberOfImages` + top-level `aspectRatio` → **`imageConfig.aspect_ratio` + `imageSize`**
  - 응답 파싱: `predictions[].bytesBase64Encoded` → `candidates[].content.parts[].inline_data.data`
  - ⚠️ **유료 플랜 필수**: Nano Banana Pro/2 및 Veo 3.1은 무료 티어 호출 불가
- **`generate_image.py` 이관 및 v3.0.0 → v4.0.0 마이그레이션**
  - 경로: `moai-content/scripts/card-news/generate_image.py` → **`moai-media/scripts/generate_image.py`**
  - Gemini 3 Image Preview API 스키마로 전면 재작성
  - Python 3.13+ 스타일 (`from __future__ import annotations`, `TypedDict`, PEP 604 union types)
  - 환경변수 우선순위: `GEMINI_API_KEY` > `NANO_BANANA_API_KEY` (레거시 호환 유지)
  - 키 파일 탐색 확장: `~/.gemini-api-key` 추가, `moai-credentials.env`에서 두 키 모두 인식
  - 서로게이트 sanitize 로직 v3.0 수준 유지 (한국어·이모지 안전)
- `moai-content/skills/card-news/SKILL.md`: 이미지 생성 섹션을 **moai-media 플러그인 위임 구조**로 전환
  - API 키 안내를 `NANO_BANANA_API_KEY` → `GEMINI_API_KEY`로 업데이트 (레거시 변수명도 인식됨 명시)
  - 모델 옵션 문구에 실제 Gemini 3 Image Preview 모델 ID 부기
  - 스크립트 경로 참조: `scripts/card-news/generate_image.py` → `moai-media/scripts/generate_image.py`
- **전체 버전 bump 1.0.3 → 1.1.0** (87 지점)
  - marketplace.json × 1
  - plugin.json × 17 (기존 16 + 신규 moai-media)
  - SKILL.md × 70 (기존 65 + 신규 5)
- `.claude-plugin/marketplace.json`: `moai-media` 플러그인 엔트리 추가

### Migration

**v1.0.x 사용자 조치 사항**:

1. **Google API 키 업그레이드**
   - 환경변수를 `NANO_BANANA_API_KEY` → `GEMINI_API_KEY`로 변경 권장 (구 변수명도 인식됨)
   - Gemini API 콘솔에서 **Pay-as-you-go 결제 활성화** 필수 (Nano Banana Pro/2 무료 티어 불가)

2. **신규 API 키 발급 (moai-media 사용 시)**
   - [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys) → `FAL_KEY`
   - [elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys) → `ELEVENLABS_API_KEY`

3. **`uv` 설치 (ElevenLabs MCP용)**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

4. **플러그인 마켓플레이스 새로고침**
   ```
   /plugin marketplace update cowork-plugins
   /plugin install moai-media@cowork-plugins
   ```

### Breaking

- **`scripts/card-news/generate_image.py` 경로 이동** — `moai-content/scripts/` 경로를 직접 참조하던 외부 스크립트는 `moai-media/scripts/`로 경로 변경 필요
- **엔드포인트 변경** — 구 스크립트를 복사하여 자체 수정해 사용하던 사용자는 `:predict` → `:generateContent` 전환 및 페이로드 스키마 업데이트 필요 (v4.0.0 `generate_image.py` 참고)
- **무료 티어 불가** — 기존 Gemini API 무료 키로 Nano Banana 호출하던 워크플로우는 Pay-as-you-go 활성화 필요

### Removed

- `moai-content/scripts/card-news/generate_image.py` (moai-media로 이관)
- `moai-content/scripts/` 빈 디렉토리 제거

---

## [1.0.3] - 2026-04-14

### Added
- `CHANGELOG.md`: Keep a Changelog 형식 공식 도입 및 엔트리 템플릿 정의
- `CLAUDE.local.md`: 저장소 로컬 지침 신규 작성
  - 버저닝 정책 (HARD): 82개 지점 동기화 절차 및 검증 명령
  - 플러그인 컴포넌트 규격: SKILL.md `user-invocable` 필수 명시
  - 릴리스 후 사용자 안내 템플릿 (`/plugin marketplace update`)
  - 태그 히스토리 관리 규정

### Changed
- **전체 버전 통일 (82 지점)**: 모든 버전 표기를 `1.0.3`으로 강제 일치
  - `.claude-plugin/marketplace.json`: `metadata.version`
  - `moai-*/.claude-plugin/plugin.json` × 16: `version` 필드
  - `moai-*/skills/*/SKILL.md` × 65: `metadata.version` 필드
  - 이전 상태: 대부분 `1.0.0` 잔존, 일부 파일만 개별 bump되어 불일치 상태였음
- `moai-core/skills/moai/SKILL.md` 본문 뱃지: `v1.0.0` → `v1.0.3`

### Fixed
- **`/moai` 슬래시 자동완성 미작동 문제** (#user-report)
  - 증상: Claude Code에서 `/moai` 입력 후 Tab 눌러도 자동완성 목록에 노출되지 않음
  - 원인: `moai-core/skills/moai/SKILL.md` frontmatter에 `user-invocable: true` 플래그 누락.
    Claude Code는 이 플래그가 `true`인 스킬만 슬래시 메뉴에 사용자 호출 가능 항목으로 등록함
  - 추가 원인: 비표준 `keywords` 필드 사용 (Claude Code 스펙 미지원)
  - 해결:
    1. `user-invocable: true` 추가
    2. `keywords` → 표준 `metadata.tags`로 이전
    3. `metadata.version`/`status`/`updated` 메타데이터 완성
- `moai-core/skills/feedback/SKILL.md` 버전 필드가 `1.0.0`에 고정되어 다른 파일과 불일치하던 문제 수정

### Removed
- 불필요한 로컬 Git 태그 정리: `v1.1.0`, `v1.2.0`, `v1.3.0`
  - 사유: `marketplace.json` 버전(`1.0.x` 트랙)과 태그 체계(`v1.x.0`)가 어긋나 혼란 유발
  - 원격 태그 `v1.1.0`도 함께 삭제 (푸시 전 단일 상태로 정리)

### Migration
사용자 측에서 신버전 반영 필요:
```
/plugin marketplace update cowork-plugins
```
이후 플러그인 상세 화면 재진입 시 `1.0.3`으로 표시되며 `/moai<Tab>` 자동완성 활성화됨.

### Breaking
없음. Frontmatter 필드 추가·정규화만 수행하여 기존 동작은 완전 호환.

---

## [1.0.2] - 2026-04-12

### Added
- `moai-core/skills/feedback/`: 버그/기능 요청 GitHub Issues 자동 등록 스킬
- `moai-office/skills/pptx-designer/`: NotebookLM 스타일 프롬프트 + 인포그래픽 선택 옵션

### Changed
- `README.md`: 퍼블릭 공개용 개편 (뱃지, 목차, 기여/문의 섹션 추가)
- 전 플러그인 스킬 테이블에 한글명 컬럼 추가 (65개 스킬)

### Fixed
- API 키와 Cowork 커넥터 혼동 방지 규칙 강화 (init 플로우 전반)
- API 키 가이드를 4개로 정리: DART/KOSIS/KCI 통합, 네이버·구글 API 제거
- `init` 안내 목록 외 서비스(네이버 API 등) 언급 금지 규칙 추가

---

## [1.0.1] - 2026-04-11

### Changed
- `init` 플로우의 모든 사용자 질문을 `AskUserQuestion` 도구로 통일

---

## [1.0.0] - 2026-04-08

### Added
- 초기 마켓플레이스 공개: 16개 플러그인, 64개 스킬
- `moai-core`: 도메인 AI 라우터 + 자가학습 엔진 (`/moai init`, `/moai catalog`)
- 도메인 플러그인 15종:
  business, marketing, legal, finance, hr, content, operations,
  education, lifestyle, product, support, office, career, data, research
