---
name: elevenlabs
description: >
  ElevenLabs 공식 MCP 서버로 AI 음성을 생성합니다. TTS(텍스트 → 음성), 음성 복제,
  32개 언어 더빙, 사운드 이펙트, 대화형 에이전트(ConvAI) 지원. 카드뉴스 보이스오버·
  숏폼 내레이션·팟캐스트·오디오북에 최적.
  '음성 생성', '내레이션 만들어줘', '보이스오버', 'AI 더빙',
  '/moai-media elevenlabs'로 호출하세요.
user-invocable: true
metadata:
  version: "1.2.0"
  status: "stable"
  updated: "2026-04-14"
  tags: "voice,tts,elevenlabs,narration,dubbing,podcast,voice-cloning"
---

# ElevenLabs — AI 음성/TTS 생성

> moai-media v1.2.0 | 공식 MCP 서버 (`uvx elevenlabs-mcp`)

## 개요

[ElevenLabs](https://elevenlabs.io)는 AI 음성 생성 업계 표준입니다. **공식 MCP 서버를 제공**하여
Claude에서 별도 코드 없이 즉시 호출 가능합니다.

- **32개 언어** 자연스러운 TTS (한국어 포함)
- **음성 복제**: 1분 샘플로 나만의 목소리 복제
- **다국어 더빙**: 한국어 영상 → 영어·일어 등 자동 더빙 (입모양 싱크)
- **사운드 이펙트** 생성
- **ConvAI**: 실시간 대화형 음성 에이전트

## 언제 이 스킬을 쓰나?

| 용도 | 활용 |
|---|---|
| **카드뉴스 보이스오버** | 인스타 릴스·쇼츠용 내레이션 |
| **숏폼 영상 내레이션** | Kling 영상에 음성 합성 |
| **팟캐스트·오디오북** | 장문 TTS |
| **다국어 더빙** | 한국 콘텐츠의 글로벌 확장 |
| **브랜드 보이스** | 일관된 브랜드 음성 에셋 |
| **사운드 이펙트** | BGM·효과음 생성 |

## MCP 설치 (최초 1회)

`moai-media/.mcp.json`에 이미 등록되어 있습니다:

```json
{
  "elevenlabs": {
    "command": "/bin/bash",
    "args": ["-l", "-c", "exec uvx elevenlabs-mcp"],
    "env": { "ELEVENLABS_API_KEY": "${ELEVENLABS_API_KEY}" }
  }
}
```

`uvx`가 처음 실행되면 자동으로 `elevenlabs-mcp` 패키지를 설치합니다.

## 호출 방식

Claude에게 자연어로 요청:
- "'안녕하세요, 오늘의 인사이트입니다'를 여성 한국어 음성으로 생성해줘"
- "이 스크립트를 남성 ASMR 톤으로 TTS 해줘"
- "한국어 영상을 영어로 더빙해줘 (입모양 싱크 유지)"
- "카페 배경 소음 효과음 30초"

MCP 서버가 내부적으로 ElevenLabs API를 호출하여 오디오 파일을 반환합니다.

## 모델 선택 가이드

| 모델 ID | 용도 | 한국어 품질 | 속도 |
|---|---|---|---|
| `eleven_multilingual_v2` (기본) | 다국어 TTS | 우수 | 보통 |
| `eleven_flash_v2_5` | 저지연 실시간 | 양호 | 초고속 |
| `eleven_turbo_v2_5` | 저비용 장문 | 양호 | 빠름 |

## 음성 프리셋 (한국어 기본)

MCP 호출 시 지정 가능:
- **여성 차분**: Adam (Korean adapted) / Rachel
- **남성 친근**: Antoni / Josh
- **여성 발랄**: Bella / Domi
- **내레이터**: Callum (다큐멘터리 톤)

자신만의 음성 복제: 1분 녹음 파일을 ElevenLabs에 업로드 → Voice ID 획득 → MCP에서 사용.

## 비용 가이드

| 플랜 | 월 | 크레딧 | 용도 |
|---|---|---|---|
| Free | $0 | 10,000 char | 테스트 |
| Starter | $5 | 30,000 char | 카드뉴스 30편 보이스오버 |
| Creator | $22 | 100,000 char | 숏폼 일 1~2편 제작자 |
| Pro | $99 | 500,000 char | 팟캐스트·에이전시 |

30,000 char ≒ 한국어 음성 약 30분 분량.

## API 키 설정

- 환경변수: `ELEVENLABS_API_KEY`
- 발급처: [elevenlabs.io/app/settings/api-keys](https://elevenlabs.io/app/settings/api-keys)
- Free 티어도 API 사용 가능 (월 10,000 char)

## 연계 스킬

- `kling` (moai-media) — 영상 생성 → ElevenLabs 내레이션 합성
- `card-news` (moai-content) — 카드뉴스 10장 + 각 슬라이드 보이스오버
- `nano-banana` (moai-media) — 이미지 + 음성 조합 인스타 릴스 생성

## 참고

- [ElevenLabs 공식 MCP GitHub](https://github.com/elevenlabs/elevenlabs-mcp)
- [ElevenLabs API 문서](https://elevenlabs.io/docs/api-reference/introduction)
- [MCP 런칭 블로그](https://elevenlabs.io/blog/introducing-elevenlabs-mcp)
