---
name: design-system-library
description: |
  글로벌 브랜드 디자인 시스템 참고 자료(Claude · ClickHouse · Clay 포함)의 색·타이포·간격·컴포넌트 구조를 읽고, 사용자 브랜드에 맞는 HTML 디자인 토큰을 설계합니다. Tailwind Play CDN 예시는 개발용이며 최종 산출물은 대상 환경에서 렌더·대비를 검증합니다.
  별도로 설치된 moai-officer:doc-html-report에서 design_system을 지정하면 토큰 참고 자료로 쓸 수 있습니다. Claude Design 핸드오프 시에는 DESIGN.md 지침 소스로 제공됩니다.
  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "Claude 스타일로 HTML 보고서 만들어줘"
  - "ClickHouse 다크 테마로 랜딩 만들어줘"
  - "Clay 디자인 시스템 적용해서 문서 생성"
  - "브랜드 디자인 시스템 골라서 HTML로"
  - "Notion / Linear / Stripe 스타일로 리포트"
  - "어두운 테마 / 따뜻한 화이트 테마로"
  - "Claude Design에 올릴 디자인 시스템 자료 정리"
version: "1.1.6"
---

# design-system-library — 75개 브랜드 디자인 시스템 SSOT

## 목적과 범위

글로벌 브랜드 75종(56개 풍부 분석 + 19개 경량 토큰)의 디자인 시스템(token 기반 분석 결과)을 단일 진실 원천(single source of truth)으로 보관하고, HTML 산출물에 적용 가능한 형태로 제공합니다.

**두 가지 소비 경로**:
1. **doc-html-report / HTML 문서 렌더** — 별도 `moai-officer`가 설치되고 해당 스킬을 사용할 수 있을 때 `design_system` 파라미터로 시스템 선택 → 토큰을 산출물 형식에 맞는 CSS와 HTML로 렌더
2. **Claude Design 핸드오프** — `design-system-prep`가 본 라이브러리 시스템을 DESIGN.md 합성 소스로 사용 → `design-handoff`의 references/context에 지침 포함

**핵심 원칙**:
- 라이브러리는 데이터(token + 분석) SSOT — 렌더 로직은 소비자(doc-html-report)가 소유
- 아래 `tailwind.config` 예시는 [Tailwind v3 Play CDN 공식 문서](https://v3.tailwindcss.com/docs/installation/play-cdn)의 JavaScript 설정 방식이다. 현재 v4 Play CDN의 CSS `@theme` 방식과 섞지 않는다. 개발 미리보기용이며 최종 배포물에는 필요한 스타일을 정적 CSS로 포함하거나 프로젝트의 빌드 경로를 사용한다.
- shadcn 컴포넌트는 React가 아닌 **vanilla HTML/CSS로 재현** (단일 파일·React 불필요)
- 기존 doc-html-report 0의존 템플릿은 유지 — design_system 미지정 시 하위 호환

---

## 3개 기본 테마 (Default)

모든 HTML 산출물의 기본 선택지. 사용자가 명시하지 않아도 결과물 성격에 따라 자동 추천합니다.

| 테마 | 무드 | 캔버스 | 강조 | 폰트 | 적합 산출물 |
|------|------|--------|------|------|-------------|
| **`claude`** | warm editorial (default) | cream `#faf9f5` | coral `#cc785c` | Copernicus serif + StyreneB sans | 보고서·사업계획서·편집성 문서 |
| **`clickhouse`** | high-contrast engineering | near-black `#0a0a0a` | electric yellow `#faff69` | Inter 700 | 기술 리포트·데이터 대시보드·개발자 문서 |
| **`clay`** | playful B2B | cream `#fffaf0` | 6-color saturated cards (pink/teal/lavender/peach/ochre) | Plain Black/Inter | 랜딩·마케팅·제품 소개 |

상세 토큰: [`systems/anthropic-claude.md`](systems/anthropic-claude.md) · [`systems/clickhouse.md`](systems/clickhouse.md) · [`systems/clay.md`](systems/clay.md)

### 자동 추천 휴리스틱

| 산출물 | 추천 테마 |
|--------|-----------|
| 주간 현황·경영 요약·사업계획서 | `claude` (warm editorial) |
| 인시던트 리포트·데이터 리포트·API 문서 | `clickhouse` (다크 엔지니어링) |
| 랜딩·제품 소개·마케팅 원고 | `clay` (playful saturated) |
| 재무제표·법률 문서 | `claude` (편집성·신뢰) |

---

## 전체 75개 카탈로그

[`systems/registry.md`](systems/registry.md) 참조 — 분류(light/warm/dark) · 캔버스 · primary 색 · 폰트 · 무드 메타 포함.

전체 시스템의 파일 목록과 출처 수준은 `registry.md`와 `BRAND-NOTICE.md`에서 확인한다. 기본 3테마의 예시 config가 있으나, 현재 산출물의 렌더·대비 통과를 뜻하지 않는다. 경량 토큰의 출처·재사용 조건이 확인되지 않은 항목은 내부 참고로만 다룬다.

브랜드 분석 문서 상당수에는 원 브랜드의 공식 출처 URL이 기록돼 있지 않다. 이 토큰을 현재 공식 디자인 시스템과 동일하다고 주장하지 않고, 사용자 브랜드를 설계하는 참고값으로만 쓴다. 특정 브랜드를 그대로 재현해야 한다면 해당 브랜드의 현재 공식 자료와 사용권을 별도로 확인한다.

---

## Tailwind v3 Play CDN 미리보기

[`mapping/tailwind.md`](mapping/tailwind.md) 참조 — YAML design token → Tailwind CDN inline config 매핑 규칙 + shadcn vanilla 컴포넌트 변환표.

**개발 미리보기 패턴** (네트워크 연결 필요, 최종 배포용 아님):

```html
<!-- 1. Tailwind v3 Play CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- 2. 브랜드 토큰 → tailwind.config 주입 -->
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: { primary: '#cc785c', canvas: '#faf9f5', /* ... */ },
        fontFamily: { display: ['Copernicus', 'serif'], sans: ['StyreneB', 'Inter', 'sans-serif'] },
        borderRadius: { md: '8px', lg: '12px', xl: '16px' },
        spacing: { section: '96px', /* ... */ }
      }
    }
  }
</script>
<!-- 3. shadcn vanilla 컴포넌트 (utility class로 직접 마크업) -->
<div class="bg-canvas rounded-lg border border-hairline p-8">
  <h2 class="font-display text-3xl tracking-tight text-ink">...</h2>
</div>
```

---

## shadcn vanilla 컴포넌트

[`components/`](components/) — shadcn UI 컴포넌트를 React 없이 vanilla HTML + Tailwind utility로 재현한 참조 마크업.

| 컴포넌트 | shadcn 원본 | vanilla 매핑 |
|----------|-------------|--------------|
| Card | `Card` / `CardHeader` / `CardContent` | `div.rounded-lg.border.p-8` + token classes |
| Button | `Button` (variant: default/secondary/ghost) | `button.inline-flex.rounded-md.px-5.py-3` + variant class |
| Badge | `Badge` | `span.inline-flex.rounded-full.px-3.py-1.text-xs` |
| Table | `Table` / `TableHeader` / `TableRow` | semantic `table.thead.tbody.tr` + token borders |
| Tabs | `Tabs` / `TabsList` | `<details>` 또는 vanilla JS tab + token classes |
| Alert | `Alert` | `div.rounded-lg.border.p-4` + semantic color |

각 컴포넌트의 풀 마크업(변형·접근성 메모 포함)은 개별 파일 — [`card.md`](components/card.md) · [`button.md`](components/button.md) · [`badge.md`](components/badge.md) · [`table.md`](components/table.md) · [`tabs.md`](components/tabs.md) · [`alert.md`](components/alert.md). 토큰 매핑 규칙은 [`mapping/tailwind.md`](mapping/tailwind.md) §1·§3.

---

## 소비자 연동

### doc-html-report (별도 moai-officer 플러그인)

`moai-officer:doc-html-report`가 현재 앱에 설치·노출된 경우, `design_system` 입력은 다음 의도로 쓰인다. 설치되지 않았다면 디자인 토큰과 적용 지침을 제공하고 HTML 생성은 사용 가능한 도구 범위에서 별도로 수행한다. 실제 렌더 결과는 소비자 스킬에서 확인한다:
- 미지정 → 기존 0의존 템플릿 (Anthropic 영감 ivory/slate/clay, 하위 호환)
- `design_system: claude|clickhouse|clay|<카탈로그 항목>` → 이 라이브러리에서 토큰을 읽고 결과물 형식에 맞는 CSS와 HTML을 생성한다. 개발 미리보기에만 Play CDN을 쓴다.

체인 예시:
```
[텍스트 스킬] → ai-slop-reviewer → doc-html-report (design_system: clickhouse)
```

### Claude Design 핸드오프 (moai-designer)

`design-system-prep`가 사용자가 지정한 시스템(또는 브랜드 무드 매칭)을 본 라이브러리에서 로드 → DESIGN.md 합성. `design-handoff`의 references.md / context.md에 design-system 지침으로 포함되어 claude.com Design 세션에 paste.

---

## 워크플로우

1. **시스템 선택** — 사용자 명시 또는 산출물 성격 기반 자동 추천(위 휴리스틱)
2. **토큰 로드** — `systems/<name>.md`의 YAML frontmatter(colors/typography/rounded/spacing/components) 파싱
3. **토큰 매핑** — `mapping/tailwind.md` 규칙을 참고하고, CTA·배지의 배경과 글자색 대비를 실제 계산
4. **shadcn vanilla 매핑** — 산출물 구조 카드/버튼/테이블을 `components/` 참조 마크업으로 치환
5. **단일 파일 렌더** — 대상 환경에 필요한 CSS와 마크업을 포함해 출력하고 브라우저에서 확인. Play CDN은 개발 미리보기일 때만 사용

디자인 시스템 파일을 수정해 `DESIGN.md` 형식을 점검할 때는 Node.js와 npm이 실제로 있는 환경에서 `npx -p "@google/design.md" designmd lint DESIGN.md`를 쓴다. [원저작자 안내](https://github.com/google-labs-code/design.md)는 Windows에서 점이 들어간 실행 이름이 마크다운 연결 프로그램으로 열릴 수 있어 `designmd` 별칭을 권한다. 이 명령은 macOS·Windows·Linux에서 같은 별칭을 사용한다. 앱에 실행 환경이 없으면 lint를 실행했다고 보고하지 않는다.

---

## 사용 예시

**예시 1: ClickHouse 다크 테마 기술 리포트**
```
결제 게이트웨이 502 장애를 ClickHouse 스타일 다크 테마로 인시던트 리포트 HTML로 만들어줘.
```

**예시 2: Claude warm 테마 사업계획서**
```
사업계획서를 Claude 디자인(warm cream + coral) HTML로 렌더해줘.
```

**예시 3: Clay playful 테마 랜딩**
```
신제품 랜딩 페이지를 Clay 스타일(컬러 카드)로 HTML로 만들어줘.
```

**예시 4: Claude Design 핸드오프용 시스템 정리**
```
Claude Design에 올릴 디자인 시스템 자료를 Linear 스타일 기반으로 정리해줘.
```

---

## 하지 않는 것

- 본 라이브러리는 렌더 로직을 소유하지 않습니다. 별도 설치된 `moai-officer:doc-html-report`·`doc-html-slide`가 현재 앱에 노출돼 있으면 해당 스킬에서 렌더합니다.
- React / Vue / 빌드 단계를 도입하지 않습니다 — 단일 파일·CDN·vanilla 고수
- 외부 의존이 없는 단일 파일 출력(이메일 첨부·오프라인·인쇄)이 필요하고 `moai-officer:doc-html-report`가 설치돼 있으면 해당 기본 템플릿을 사용합니다. 설치되지 않았다면 토큰과 적용 지침을 제공하고, 현재 앱에서 HTML을 만들 수 있는지 별도로 확인합니다.
- 브랜드 저작권 — 각 시스템은 **분석·참고용 token**이며, 저장소 Apache-2.0 라이선스의 **적용 범위 밖**입니다.
  각 브랜드의 디자인·상표·서체 권리는 해당 소유자에게 있습니다. 상업적 산출물에 적용하기 전
  반드시 [`BRAND-NOTICE.md`](BRAND-NOTICE.md)의 사용 경계와 오픈 라이선스 대체 서체표를 확인하세요

---

## 참고 문서

- [`systems/registry.md`](systems/registry.md) — 75개 전체 카탈로그 인덱스
- [`systems/anthropic-claude.md`](systems/anthropic-claude.md) · [`systems/clickhouse.md`](systems/clickhouse.md) · [`systems/clay.md`](systems/clay.md) — 기본 3테마 상세 토큰 (claude.md는 `CLAUDE.md` 자동 로드 회피를 위해 `anthropic-claude.md`로 명명)
- [`systems/keynote-editorial-dark.md`](systems/keynote-editorial-dark.md) — 프리미엄 에디토리얼 키노트 레시피(다크, no_box·거대숫자 3단·4모서리·단일 accent). 일반 다크 팔레트가 아닌 슬라이드 구성 계약
- [`references/korean-design-systems.md`](references/korean-design-systems.md) — 한국 기업 공개 디자인시스템 + 무료 한글 폰트 서베이 (당근 SEED·채널톡 Bezier·KRDS·Pretendard + 토스/브랜드 라이선스 함정 경고)
- [`mapping/tailwind.md`](mapping/tailwind.md) — YAML 토큰 → Tailwind CDN config 매핑 규칙
- [`components/`](components/) — shadcn vanilla 컴포넌트 참조 마크업
