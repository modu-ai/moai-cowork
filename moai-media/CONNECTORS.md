# moai-media 커넥터·API 가이드

## 개요

moai-media는 **API 키 3개 + MCP 서버 2개**로 전체 미디어 생성을 커버합니다.

## API 키 등록 (3종)

### 1. Gemini API (`GEMINI_API_KEY`)

**용도**: `nano-banana` 스킬 — Gemini 3 Image Preview 계열 이미지 생성 (영상은 `kling` 스킬 별도)

**발급**:
1. [ai.google.dev](https://ai.google.dev/) 접속 → Google 계정 로그인
2. "Get API key" → 새 프로젝트 생성 또는 기존 선택
3. **Pay-as-you-go 결제 등록 필수** (Nano Banana 계열 3종 모두 무료 티어 불가, 공식 문서 명시)
4. 생성된 키 복사

**등록**:
```bash
/moai apikey
```
또는 환경변수 직접 설정:
```bash
export GEMINI_API_KEY="AIzaSy..."
```

**레거시 호환**: 기존 `NANO_BANANA_API_KEY` 환경변수도 자동 인식됩니다 (v1.0.x 사용자 마이그레이션 무중단).

### 2. fal.ai (`FAL_KEY`)

**용도**: `ideogram`, `kling`, `fal-gateway` 스킬 — 1000+ 모델 통합 게이트웨이

**발급**:
1. [fal.ai](https://fal.ai/) 가입 (GitHub·Google OAuth 지원)
2. [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys)에서 키 생성
3. 가입 시 **$5 무료 크레딧 자동 지급** (이미지 125장 또는 영상 60초 분량)
4. 추가 충전: 해외카드 필요 (트래블월렛·우리카드 권장)

**등록**:
```bash
export FAL_KEY="fal-..."
```

### 3. ElevenLabs (`ELEVENLABS_API_KEY`)

**용도**: `elevenlabs` 스킬 — TTS, 음성복제, 다국어 더빙, 사운드 이펙트

**발급**:
1. [elevenlabs.io](https://elevenlabs.io) 가입
2. [elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)에서 키 생성
3. Free 티어: 월 10,000 char TTS 무료 (API 포함)
4. 유료: Starter $5/mo (30,000 char)부터

**등록**:
```bash
export ELEVENLABS_API_KEY="sk_..."
```

## MCP 서버 (2종, 자동 등록)

플러그인 설치 시 `moai-media/.mcp.json`이 자동 적용됩니다.

### fal-ai (hosted MCP)

```json
{
  "fal-ai": {
    "type": "http",
    "url": "https://mcp.fal.ai/mcp",
    "headers": {
      "Authorization": "Bearer ${FAL_KEY}"
    }
  }
}
```

- **설치 불필요** — 원격 호스팅 MCP
- fal.ai 모델 전체에 자연어로 접근
- `ideogram`, `kling`, `fal-gateway` 스킬이 내부적으로 호출

### elevenlabs (local MCP)

```json
{
  "elevenlabs": {
    "command": "/bin/bash",
    "args": ["-l", "-c", "exec uvx elevenlabs-mcp"],
    "env": { "ELEVENLABS_API_KEY": "${ELEVENLABS_API_KEY}" }
  }
}
```

- **uvx 자동 설치** — 최초 실행 시 `elevenlabs-mcp` 패키지 설치
- 사전 준비: `uv` 설치 필요 (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [공식 MCP GitHub](https://github.com/elevenlabs/elevenlabs-mcp)

## Cowork 공식 커넥터 (선택)

moai-media 자체는 Cowork 커넥터를 요구하지 않지만, 다음 커넥터를 함께 사용하면 유용합니다:

| 커넥터 | 활용 | 대상 스킬 |
|---|---|---|
| **Google Drive** | 생성된 미디어 파일 자동 저장·공유 | 전체 |
| **Canva** | AI 생성 이미지 → Canva 템플릿 합성 | `nano-banana`, `ideogram` |
| **Notion** | 포트폴리오·에셋 라이브러리 관리 | 전체 |
| **YouTube** (선택) | Kling 숏폼·영상 자동 업로드 | `kling` |

Cowork > Settings > Connectors에서 OAuth 연결.

## 비용 관리 팁

- **시안 단계**: Nano Banana 2 (`gemini-3.1-flash-image-preview`), Hailuo Standard ($0.045/sec)
- **최종 단계**: Nano Banana Pro (2K/4K), Kling Pro (립싱크·1080p)
- fal.ai 대시보드와 Google Cloud Billing에서 월 예산 한도 설정
- `num_images: 1` 기본 유지, A/B 테스트 시만 증가
- ElevenLabs는 크레딧 한도 설정 가능 (Starter 플랜 기준)

## 트러블슈팅

| 증상 | 원인 | 해결 |
|---|---|---|
| Nano Banana 401 Unauthorized | 무료 티어로 호출 시도 | Gemini API Pay-as-you-go 활성화 |
| `uvx elevenlabs-mcp` 실패 | `uv` 미설치 | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| fal.ai 402 Payment Required | 무료 크레딧 소진 | [fal.ai/billing](https://fal.ai/billing)에서 충전 |
| 레거시 `NANO_BANANA_API_KEY` 작동 안 함 | v4.0에서 Gemini 3 Image Preview로 이전. Pay-as-you-go 재활성 필요 | Gemini API 계정 확인 |
| 한글 프롬프트 서로게이트 오류 | 일부 이모지·특수문자 | `scripts/generate_image.py`의 `sanitize_text()` 자동 처리 |
