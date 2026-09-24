# Tabs — shadcn vanilla

shadcn `Tabs` / `TabsList` / `TabsTrigger` / `TabsContent`를 React 없이 재현합니다. 두 패턴 — (A) 의존성 0 `<details>` 폴백, (B) vanilla JS ARIA 탭. 토큰 규칙은 [`../mapping/tailwind.md`](../mapping/tailwind.md) §1·§3 참조.

## (A) `<details>` 폴백 — JS 불필요

아코디언형 공개/접기 패턴이다. 탭과 동작이 다르므로 여러 패널 중 하나만 표시해야 하는 요구에는 쓰지 않는다.

```html
<details class="rounded-lg border border-hairline bg-surface-card" open>
  <summary class="cursor-pointer list-none px-5 py-4 font-medium text-ink marker:hidden">
    개요 <span class="float-right text-muted">▾</span>
  </summary>
  <div class="border-t border-hairline px-5 py-4 text-body">
    첫 번째 패널 내용.
  </div>
</details>
<details class="mt-2 rounded-lg border border-hairline bg-surface-card">
  <summary class="cursor-pointer list-none px-5 py-4 font-medium text-ink marker:hidden">
    상세 <span class="float-right text-muted">▾</span>
  </summary>
  <div class="border-t border-hairline px-5 py-4 text-body">
    두 번째 패널 내용.
  </div>
</details>
```

## (B) ARIA 탭 (vanilla JS) — 동시 노출 불가, 한 패널만

```html
<div class="rounded-lg border border-hairline bg-surface-card">
  <div role="tablist" class="flex gap-1 border-b border-hairline p-1" aria-label="보고서 섹션">
    <button role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1"
            class="rounded-md bg-primary px-4 py-2 text-sm font-medium text-on-primary">요약</button>
    <button role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1"
            class="rounded-md px-4 py-2 text-sm font-medium text-muted hover:text-ink">지표</button>
  </div>
  <div role="tabpanel" id="panel-1" aria-labelledby="tab-1" class="p-5 text-body">
    요약 패널.
  </div>
  <div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden class="p-5 text-body">
    지표 패널.
  </div>
</div>

<script>
  document.querySelectorAll('[role="tablist"]').forEach((list) => {
    const tabs = [...list.querySelectorAll('[role="tab"]')];
    const select = (tab, moveFocus = false) => {
      tabs.forEach((item) => {
        const active = item === tab;
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
        item.classList.toggle('bg-primary', active);
        item.classList.toggle('text-on-primary', active);
        item.classList.toggle('text-muted', !active);
        item.classList.toggle('hover:text-ink', !active);
        document.getElementById(item.getAttribute('aria-controls')).hidden = !active;
      });
      if (moveFocus) tab.focus();
    };
    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => select(tab));
      tab.addEventListener('keydown', (event) => {
        const next = {
          ArrowRight: tabs[(index + 1) % tabs.length],
          ArrowLeft: tabs[(index - 1 + tabs.length) % tabs.length],
          Home: tabs[0],
          End: tabs[tabs.length - 1],
        }[event.key];
        if (!next) return;
        event.preventDefault();
        select(next, true);
      });
    });
  });
</script>
```

## 토큰 메모

- 선택 탭은 `bg-primary text-on-primary`, 비선택은 `text-muted` → `text-ink` hover. 실제 대비를 확인한다.
- `<details>` 패턴은 JavaScript가 없는 단일 파일과 호환된다. ARIA 탭은 위 JavaScript와 필요한 스타일을 결과 HTML에 포함하면 오프라인에서도 사용할 수 있다. 실제 키보드 동작을 브라우저에서 확인한다.
- 키보드 접근성: 좌우 화살표·Home·End로 이동하고 선택한다([WAI-ARIA Tabs Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)). 여러 탭 묶음을 쓴다면 `id`와 `aria-controls`를 묶음마다 고유하게 만든다.
