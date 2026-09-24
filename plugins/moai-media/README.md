# 미디어 크리에이터 (moai-media)

미디어 생성 전담 AI 코워커입니다. 이미지·영상·오디오 스킬과 Higgsfield 이미지·영상·3D·설명영상·제품촬영·캐릭터 일관성, ElevenLabs TTS/보이스클로닝 MCP 연동, GPT Image 2.5·Gemini 3·Midjourney v8 프롬프트 빌더를 하나의 플러그인으로 제공합니다. ChatGPT Work에서는 기본 이미지 도구로 이미지를 직접 생성할 수 있습니다.

> **분리 안내**: 본 플러그인의 미디어 생성 스킬들은 `moai-marketer`에서 분리되었습니다(카피·캠페인·콘텐츠 스킬은 moai-marketer에 잔류). 신규 호출은 `moai-media:<스킬명>` 네임스페이스를 사용하세요.

**이런 분께 추천**: 콘텐츠 크리에이터 · 마케터 · 디자이너 · 1인 브랜드

## 설치

Claude Cowork와 ChatGPT Work는 마켓플레이스 등록 권한과 경로가 다릅니다.

- **Claude Cowork**: Settings(또는 Plugins) → Marketplace → +에서 `modu-ai/moai-cowork`를 추가한 뒤 Plugins에서 **moai-media**를 설치하세요.
- **ChatGPT Work**: 워크스페이스 관리자가 Workspace settings → Plugins → Add → Import marketplace에서 `https://github.com/modu-ai/moai-cowork`를 가져와야 합니다. 이용자는 권한이 부여된 뒤 Plugins에서 **moai-media**를 찾아 Install plugin을 누르세요. 외부 서비스 연결은 별도 인증이 필요합니다.

> 앱별 정확한 클릭 경로와 잘 안 될 때 대처법은 [플러그인 설치와 관리](https://cowork.mo.ai.kr/plugins/install/)에 정리해 두었습니다.

## 스킬

호출 형식: `/moai-media:<스킬명>` — 예: `/moai-media:media-higgsfield-image`. 자연어 요청("표지 이미지 만들어줘", "TTS 성우 더빙 생성")으로도 자동 매칭됩니다.

### Higgsfield 계열

| 스킬 | 역할 |
|------|------|
| `media-higgsfield-core` | (공유 코어) 호출 계약·라이브 카탈로그 조회·비용 프리플라이트 SSOT. 단독 호출용 아님 |
| `media-higgsfield-image` | Higgsfield 계정의 이미지 모델로 생성 (Claude MCP·ChatGPT 공식 플러그인) |
| `media-higgsfield-video` | Higgsfield 계정의 영상 모델로 생성 (Claude MCP·ChatGPT 공식 플러그인) |
| `media-higgsfield-identity` | 캐릭터·인물 일관성 참조 — Soul 학습 / Element 생성 판정 |
| `media-higgsfield-assets` | 3D 메시(GLB)·리깅·오디오·바이럴 예측·업스케일/리프레임/누끼 |
| `media-higgsfield-explainer` | 10초 블록 조립형 내레이션 설명 영상 (1~10분) |
| `media-higgsfield-product` | 브랜드·제품 비주얼 10모드 판정과 생성 |

### 그 밖의 생성·프롬프트

| 스킬 | 역할 |
|------|------|
| `media-production` | 이미지·영상·오디오 복합 요청의 생성 경로를 선택해 해당 스킬로 연결 |
| `media-brand-audit` | 생성 산출물·프롬프트의 브랜드·권리·비용 표시를 증거로 검수 |
| `media-audio-gen` | ElevenLabs MCP 기반 다국어 TTS·보이스 클로닝·더빙·효과음. 언어 지원은 선택한 모델에서 확인 |
| `media-gpt-image-prompt` | OpenAI GPT Image 2.5(Flare·Sunburst) 공식 가이드 기반 이미지 프롬프트 빌더 |
| `media-gemini-3-image-prompt` | Gemini 3 Pro Image(Nano Banana Pro) 전용 5-component 프롬프트 빌더 |
| `media-midjourney-v8-prompt` | Midjourney V8 프롬프트 빌더. 현재 기본 V8.2와 Edit Model 안내 |
| `media-codex-image` | ChatGPT Work 기본 도구(`gpt-image-2`)로 생성·편집하고, 정확한 GPT Image 2.5 생성은 별도 API 키를 쓰는 `moai-mcp-openai`로 실행 (기존 스킬 이름 유지) |
| `media-notebooklm-slide-prompt` | 강연 마크다운 → NotebookLM 슬라이드 데크 + 슬라이드별 이미지 프롬프트 |
| `media-asset-production` | 구명칭 호환 스텁. 신규 호출은 분리 스킬 사용 |

## MCP 연동

Claude에서 Higgsfield는 플러그인 루트 `.mcp.json`의 공식 원격 MCP 연결을 사용합니다. ChatGPT Work에서는 **공식 Higgsfield 플러그인을 연결**한 뒤 같은 Higgsfield 계정으로 로그인합니다. 두 경로의 도구 이름과 입력 스키마는 다를 수 있으므로 `media-higgsfield-core`가 현재 연결을 확인합니다. ElevenLabs는 플러그인의 MCP 런처와 계정 API 키를 사용합니다.

| 서버 | 역할 | 인증 방법 |
|------|------|-----------|
| `higgsfield` | AI 영상·이미지 생성 (media-higgsfield-* 사용) | Claude: 공식 MCP OAuth · ChatGPT: 공식 Higgsfield 플러그인 OAuth |
| `ElevenLabs` | TTS·보이스 클로닝·더빙·효과음 (media-audio-gen 전용) | `ELEVENLABS_API_KEY` 환경변수 (elevenlabs.io에서 발급) + `uv` 사전 설치 |

- Higgsfield MCP 생성은 크레딧이 소모되므로 **사전 크레딧 고지 + 사용자 확인** 후에만 실행합니다. ChatGPT 기본 이미지 도구의 이용 한도는 앱에 표시되는 계정 조건을 따릅니다.
- MCP 미연결 시 프롬프트 온리 모드(생성 프롬프트만 산출)로 자동 전환됩니다

## Claude 에이전트

Claude의 에이전트 실행 환경에서는 아래 역할을 사용할 수 있습니다. ChatGPT 플러그인에서는 같은 진입 목적의 `media-production`·`media-brand-audit` 스킬을 사용합니다.

| 에이전트 | 등급 | 역할 |
|----------|------|------|
| `media-producer` | worker | 이미지·영상·오디오 생성 산출물을 만드는 실무 에이전트. 목표 이해 → 계획 → media-* 스킬 선택 → 실행 → 검증의 에이전트 루프로 동작. 저작권/초상권 준수·크레딧 사전 고지·카피/전략은 marketer·토큰은 designer로 인계를 HARD 가드레일로 준수 |
| `media-brand-auditor` | read-only audit | 미디어 산출물·프롬프트를 회의적으로 검증하는 감사 에이전트 — 브랜드/스타일 정합, 저작권·라이선스 위험, 프롬프트 인젝션/불쾌 콘텐츠 위험, 프롬프트 엔지니어링 품질. 증거 기반 PASS/FAIL 판정만 반환하며 파일을 수정하지 않음 |

## 라이선스

Apache-2.0 · © 2026 modu-ai (email@mo.ai.kr) — 산출물은 이용자 소유([LICENSE-OUTPUT.md](../../LICENSE-OUTPUT.md))
