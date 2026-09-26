# 디자인 시스템 → getdesign.md 링크 매핑표

현재 설치된 [`moai-designer:design-system-library`](../../../moai-designer/skills/design-system-library/SKILL.md)의 브랜드 시스템에 대한 [`getdesign.md`](https://getdesign.md) 참고 링크입니다. 이 사이트는 브랜드 공식 규격이 아닌 독립 분석이며, 아래 링크는 먼저 해당 브랜드의 목록 페이지를 엽니다. 상세 디자인은 목록에서 다시 선택합니다. 링크와 토큰 값은 사용 전에 확인합니다.

## URL 패턴

```
https://getdesign.md/<slug>
```

`/<slug>`는 목록 페이지입니다. 확인한 `claude`와 `clickhouse`의 상세 분석은 각각 `/<slug>/design-md`에 있었습니다. 나머지 슬러그도 열어서 확인합니다.

## 매핑 규칙

저장소 시스템 파일명(`systems/<name>.md`) → getdesign.md slug:
- 대부분 1:1 (`clickhouse` → `clickhouse`, `notion` → `notion`)
- `.ai`/`.com` TLD 접미사 제거 + 하이픈 정규화
- 특이케이스: `anthropic-claude`→`claude`, `mistral.ai`→`mistral-ai`, `together.ai`→`together-ai`, `x.ai`→`xai`, `opencode.ai`→`opencode`, `theverge`→`the-verge`, `runwayml`→`runway`

## 기본 3 테마

| design_system | 분류 | 캔버스 | Primary | 폰트 | getdesign.md 미리보기 |
|---------------|------|--------|---------|------|----------------------|
| `claude` (기본) | light | `#faf9f5` | `#cc785c` | Copernicus | https://getdesign.md/claude |
| `clickhouse` | dark | `#0a0a0a` | `#faff69` | Inter | https://getdesign.md/clickhouse |
| `clay` | light | `#fffaf0` | `#0a0a0a` | Plain Black | https://getdesign.md/clay |

## LIGHT

| design_system | Primary | getdesign.md |
|---------------|---------|--------------|
| `cohere` | `#17171c` | https://getdesign.md/cohere |
| `coinbase` | `#0052ff` | https://getdesign.md/coinbase |
| `cursor` | `#f54e00` | https://getdesign.md/cursor |
| `elevenlabs` | `#292524` | https://getdesign.md/elevenlabs |
| `expo` | `#000000` | https://getdesign.md/expo |
| `figma` | `#000000` | https://getdesign.md/figma |
| `ibm` | `#0f62fe` | https://getdesign.md/ibm |
| `intercom` | `#111111` | https://getdesign.md/intercom |
| `meta` | `#0064e0` | https://getdesign.md/meta |
| `minimax` | `#0a0a0a` | https://getdesign.md/minimax |
| `mintlify` | `#0a0a0a` | https://getdesign.md/mintlify |
| `miro` | `#1c1c1e` | https://getdesign.md/miro |
| `mistral.ai` | `#fa520f` | https://getdesign.md/mistral-ai |
| `mongodb` | `#00ed64` | https://getdesign.md/mongodb |
| `nike` | `#111111` | https://getdesign.md/nike |
| `notion` | `#0075de` | https://getdesign.md/notion |
| `nvidia` | `#76b900` | https://getdesign.md/nvidia |
| `ollama` | `#000000` | https://getdesign.md/ollama |
| `opencode.ai` | `#201d1d` | https://getdesign.md/opencode |
| `pinterest` | `#e60023` | https://getdesign.md/pinterest |
| `posthog` | `#f7a501` | https://getdesign.md/posthog |
| `renault` | `#ffed00` | https://getdesign.md/renault |
| `replicate` | `#ea2804` | https://getdesign.md/replicate |
| `runwayml` | `#000000` | https://getdesign.md/runway |
| `slack` | `#4a154b` | https://getdesign.md/slack |
| `superhuman` | `#1b1938` | https://getdesign.md/superhuman |
| `together.ai` | `#000000` | https://getdesign.md/together-ai |
| `uber` | `#000000` | https://getdesign.md/uber |
| `vodafone` | `#e60000` | https://getdesign.md/vodafone |
| `wise` | `#9fe870` | https://getdesign.md/wise |
| `zapier` | `#ff4f00` | https://getdesign.md/zapier |
| `kraken` | `#7132f5` | https://getdesign.md/kraken |
| `lovable` | `#1c1c1c` | https://getdesign.md/lovable |
| `mastercard` | `#cf4500` | https://getdesign.md/mastercard |
| `starbucks` | `#00754a` | https://getdesign.md/starbucks |
| `tesla` | `#3e6ae1` | https://getdesign.md/tesla |
| `airbnb` | `#ff5a5f` | https://getdesign.md/airbnb |
| `airtable` | `#2d7ff9` | https://getdesign.md/airtable |
| `apple` | `#0071e3` | https://getdesign.md/apple |
| `cal` | `#111827` | https://getdesign.md/cal |
| `dell-1996` | `#007db8` | https://getdesign.md/dell-1996 |
| `hp` | `#0096d6` | https://getdesign.md/hp |
| `nintendo-2001` | `#e60012` | https://getdesign.md/nintendo-2001 |
| `stripe` | `#635bff` | https://getdesign.md/stripe |
| `webflow` | `#146ef5` | https://getdesign.md/webflow |
| `wired` | `#0000ee` | https://getdesign.md/wired |

## WARM

| design_system | Primary | getdesign.md |
|---------------|---------|--------------|
| `playstation` | `#0070d1` | https://getdesign.md/playstation |
| `revolut` | `#494fdf` | https://getdesign.md/revolut |

## DARK

| design_system | Primary | getdesign.md |
|---------------|---------|--------------|
| `composio` | `#0007cd` | https://getdesign.md/composio |
| `discord` | `#5865f2` | https://getdesign.md/discord |
| `ferrari` | `#da291c` | https://getdesign.md/ferrari |
| `framer` | `#ffffff` | https://getdesign.md/framer |
| `hashicorp` | `#000000` | https://getdesign.md/hashicorp |
| `raycast` | `#ffffff` | https://getdesign.md/raycast |
| `resend` | `#fcfdff` | https://getdesign.md/resend |
| `sanity` | `#0b0b0b` | https://getdesign.md/sanity |
| `sentry` | `#150f23` | https://getdesign.md/sentry |
| `shopify` | `#000000` | https://getdesign.md/shopify |
| `spacex` | `#000000` | https://getdesign.md/spacex |
| `x.ai` | `#ffffff` | https://getdesign.md/xai |
| `lamborghini` | `#ffc000` | https://getdesign.md/lamborghini |
| `spotify` | `#1ed760` | https://getdesign.md/spotify |
| `theverge` | `#3cffd0` | https://getdesign.md/the-verge |
| `binance` | `#f0b90b` | https://getdesign.md/binance |
| `bmw` | `#1c69d4` | https://getdesign.md/bmw |
| `bmw-m` | `#1c69d4` | https://getdesign.md/bmw-m |
| `bugatti` | `#1f4fa0` | https://getdesign.md/bugatti |
| `linear.app` | `#7c84ec` | https://getdesign.md/linear |
| `supabase` | `#3ecf8e` | https://getdesign.md/supabase |
| `vercel` | `#ffffff` | https://getdesign.md/vercel |
| `voltagent` | `#00d992` | https://getdesign.md/voltagent |
| `warp` | `#01a2ff` | https://getdesign.md/warp |

## 안내 패턴 (SKILL.md 1단계에서 사용)

design_system 선택 안내 시 각 옵션에 getdesign.md 링크를 함께 표시:

```text
테마 후보 (getdesign.md 미리보기로 확인 후 선택):
1. claude (warm editorial, 기본) → https://getdesign.md/claude
2. clickhouse (dark tech)        → https://getdesign.md/clickhouse
3. notion (light minimalism)     → https://getdesign.md/notion
4. spotify (dark bold)           → https://getdesign.md/spotify
다른 테마: design-system-links.md 매핑표 참조
```

> 테마 목록과 외부 사이트는 바뀔 수 있습니다. 일부 슬러그는 브랜드 표기 정규화(`.ai`→`-ai`, `xAI`→`xai`, `linear.app`→`linear` 등)가 필요합니다. 링크가 깨지면 getdesign.md 홈(https://getdesign.md)에서 검색하고 현재 설치된 토큰을 확인하세요.
