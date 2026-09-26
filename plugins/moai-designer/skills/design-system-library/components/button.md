# Button — shadcn vanilla

shadcn `Button`(variant: default / secondary / ghost / destructive)를 React 없이 **vanilla HTML + Tailwind token class**로 재현합니다. 토큰 규칙은 [`../mapping/tailwind.md`](../mapping/tailwind.md) §1·§3 참조.

## 변형

### default (primary CTA)

```html
<button class="inline-flex h-10 items-center rounded-md bg-primary px-5 text-sm font-medium text-on-primary hover:bg-primary-active hover:text-on-primary-active focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-2 focus-visible:ring-offset-canvas">
  Action
</button>
```

### secondary

```html
<button class="inline-flex h-10 items-center rounded-md border border-hairline bg-canvas px-5 text-sm font-medium text-ink hover:bg-surface-card">
  Secondary
</button>
```

### ghost

```html
<button class="inline-flex h-10 items-center rounded-md px-5 text-sm font-medium text-ink hover:bg-surface-card">
  Ghost
</button>
```

### destructive

```html
<button class="inline-flex h-10 items-center rounded-md bg-error px-5 text-sm font-medium text-on-error hover:opacity-90 focus-visible:ring-2 focus-visible:ring-error">
  삭제
</button>
```

### pill (일부 브랜드 — starbucks · mastercard · lovable 등 full-radius)

```html
<button class="inline-flex h-10 items-center rounded-full bg-primary px-6 text-sm font-medium text-on-primary hover:bg-primary-active hover:text-on-primary-active focus-visible:ring-2 focus-visible:ring-primary">
  주문하기
</button>
```

## 토큰 메모

- `text-on-primary`·`hover:text-on-primary-active`·`text-on-error`는 각 배경과 실제 대비를 계산해 토큰으로 제공한다. Claude primary 위 흰색은 3.28:1, ClickHouse primary 위 흰색은 1.07:1이라 두 시스템 모두 `text-white` 고정이 안 된다. Claude hover coral 위 검정도 3.65:1이라 hover에는 흰색을 쓴다. 오류색도 별도 확인한다.
- `focus-visible:ring-*` — 키보드 접근성. ring 색은 `primary` 권장.
- pill 브랜드는 시스템 frontmatter `rounded.pill` / `rounded.full` 토큰이 있을 때만 `rounded-full` 사용(자동 매핑은 §1.3).
