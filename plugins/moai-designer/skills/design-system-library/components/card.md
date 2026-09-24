# Card — shadcn vanilla

shadcn `Card` / `CardHeader` / `CardContent`를 React 없이 **vanilla HTML + Tailwind token class**로 재현합니다. 모든 색은 `design_system` 토큰(`canvas` / `ink` / `hairline` / `surface-card`)으로, 지정한 브랜드가 주입됩니다. 토큰 매핑 규칙은 [`../mapping/tailwind.md`](../mapping/tailwind.md) §1·§3 참조.

## 기본 (default)

```html
<div class="rounded-lg border border-hairline bg-surface-card p-8">
  <div class="mb-2 text-sm font-medium uppercase tracking-wide text-muted">Label</div>
  <h3 class="font-display text-2xl tracking-tight text-ink">Card Title</h3>
  <p class="mt-2 text-body">Body content…</p>
</div>
```

## 변형

### 강조 카드(CTA 포함)

```html
<div class="rounded-lg border border-hairline bg-canvas p-8 ring-1 ring-primary/20">
  <h3 class="font-display text-2xl tracking-tight text-ink">Upgrade plan</h3>
  <p class="mt-2 text-body">요금제별 한도를 확인하세요.</p>
  <button class="mt-5 inline-flex h-10 items-center rounded-md bg-primary px-5 text-sm font-medium text-on-primary hover:bg-primary-active hover:text-on-primary-active focus-visible:ring-2 focus-visible:ring-primary">요금제 보기</button>
</div>
```

### 다크 패널 (다크 테마 시스템 — clickhouse · spotify · lamborghini 등)

```html
<div class="rounded-lg border border-hairline bg-surface-dark p-8 text-on-dark">
  <h3 class="font-display text-2xl tracking-tight">Incident #482</h3>
  <p class="mt-2 opacity-80">결제 게이트웨이 502 — 14:02 KST 복구.</p>
</div>
```

## 토큰 메모

- `bg-surface-card` — 카드 기본 배경(브랜드 `surface-card`).
- `border-hairline` — 1px 테두리(브랜드 `hairline`).
- 다크 테마 시스템은 `bg-surface-dark` + `text-on-dark`(또는 `text-ink`가 white로 정의된 시스템은 `text-ink`).
- `ring-primary/20` — CTA 카드에 쓰는 얕은 강조 링. `/20`은 alpha utility로 토큰 무관 동작.
