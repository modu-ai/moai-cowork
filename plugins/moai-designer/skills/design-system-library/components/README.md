# components/ — shadcn vanilla 컴포넌트 참조 마크업

shadcn UI 컴포넌트를 React 없이 **vanilla HTML + Tailwind utility class**로 재현한 참조 마크업입니다. 단일 파일 HTML 산출물(doc-html-report 등)에서 `design_system` 토큰과 함께 카드·버튼·테이블 등을 칠할 때 참조합니다. 토큰 규칙은 [`../mapping/tailwind.md`](../mapping/tailwind.md) §1·§3 기준.

## 컴포넌트 (6종)

| 파일 | shadcn 원본 | 용도 |
|------|-------------|------|
| [`card.md`](card.md) | `Card` / `CardHeader` / `CardContent` | 콘텐츠 카드 · 강조(CTA) 카드 · 다크 패널 |
| [`button.md`](button.md) | `Button` (default / secondary / ghost / destructive / pill) | CTA · 보조 · 파괴적 액션 |
| [`badge.md`](badge.md) | `Badge` (neutral / primary / semantic / outline) | 상태 · 라벨 칩 |
| [`table.md`](table.md) | `Table` / `TableHeader` / `TableRow` | 데이터 표(스트라이프 · 다크 지원) |
| [`tabs.md`](tabs.md) | `Tabs` / `TabsList` | `<details>` 폴백(0-JS) + ARIA vanilla JS 탭 |
| [`alert.md`](alert.md) | `Alert` (info / success / warning / error) | 안내 · 주의 · 경고 콜아웃 |

## 원칙

- React · Vue · 빌드 단계 없이 **단일 파일 HTML** 안에서 동작하는 마크업만 둡니다
- utility class + **token class** 조합(`bg-canvas` · `text-ink` · `border-hairline` · `font-display` 등)을 개발 미리보기에서 참조한다. 최종 HTML은 해당 클래스를 제공하는 정적 CSS 또는 빌드 결과를 포함해야 한다.
- 외부 의존이 없는 단일 파일 출력(이메일 첨부·오프라인·인쇄)이 필요하고 별도 `moai-officer:doc-html-report`가 현재 앱에 설치·노출돼 있으면 해당 기본 템플릿을 사용한다. 없으면 현재 사용 가능한 HTML 생성 도구를 확인하고, 만들 수 없으면 토큰과 적용 지침만 제공한다.
- 토큰 정의는 각 [`../systems/`](../systems/) frontmatter(`colors` · `typography` · `rounded` · `spacing`)에서, 매핑은 [`../mapping/tailwind.md`](../mapping/tailwind.md)에서
- `primary`·`error` 같은 배경의 글자색은 토큰별 대비를 계산해 `on-primary`·`on-error`로 제공한다. HTML 예시의 대비는 브랜드 토큰을 주입한 뒤 확인해야 한다.
