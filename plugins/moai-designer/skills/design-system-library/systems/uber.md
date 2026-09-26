---
version: alpha
name: Uber-design-analysis
description: An Uber-inspired black, white, and gray reference. Use portable fonts and verify current Base guidance, product content, assets, and rendered accessibility before reuse.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  body: "#5e5e5e"
  mute: "#afafaf"
  hairline-mid: "#4b4b4b"
  canvas: "#ffffff"
  canvas-soft: "#efefef"
  canvas-softer: "#f3f3f3"
  surface-pressed: "#e2e2e2"
  link: "#0000ee"
  on-dark: "#ffffff"
  black-elevated: "#282828"
  control-border-light: "#767676"
  control-border-dark: "#8c8c8c"

typography:
  display-xxl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 52px
    fontWeight: 700
    lineHeight: 64px
  display-xl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 36px
    fontWeight: 700
    lineHeight: 44px
  display-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
  display-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
  display-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 700
    lineHeight: 28px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 24px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 20px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 20px
  button-large:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 24px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 20px

rounded:
  none: 0px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 999px
  pill-tab: 36px
  full: 9999px

spacing:
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.md}"
  button-secondary:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.md}"
  button-subtle:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.lg}"
  button-floating:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md}"
  button-large-rounded:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-large}"
    rounded: "{rounded.xl}"
    padding: "{spacing.lg} {spacing.xl}"
  button-tab-translucent:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.pill-tab}"
  text-input:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  text-input-on-soft:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-softer}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  text-input-focus:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    outlineColor: "{colors.ink}"
    outlineOffset: 2px
    typography: "{typography.body-md}"
  text-input-focus-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    outlineColor: "{colors.on-dark}"
    outlineOffset: 2px
    typography: "{typography.body-md}"
  card-content:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  card-elevated:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  card-soft-tinted:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  promo-card-illustrated:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  promo-card-on-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  request-form-card:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.lg}"
  request-form-input-row:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  category-button:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.lg}"
  faq-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md-strong}"
    padding: "{spacing.lg} 0"
  app-download-pill:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.md} {spacing.xl}"
  hero-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  showcase-image-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    rounded: "{rounded.xl}"
    padding: "{spacing.3xl}"
  link-blue:
    textDecoration: underline
    textColor: "{colors.link}"
    typography: "{typography.body-md}"
  link-on-dark:
    textDecoration: underline
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
  link-mute:
    textDecoration: underline
    textColor: "{colors.hairline-mid}"
    typography: "{typography.body-md}"
  link-mute-soft:
    textDecoration: underline
    textColor: "{colors.mute}"
    typography: "{typography.body-md}"
  icon-button-circular:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Illustrative pricing tier; not a claim about Uber prices or plans."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-light}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to ink with white text."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-product-selector:
    description: "Illustrative product selector; use current, region-specific product labels only after verification."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.2xl}"
  ex-cart-drawer:
    description: "Illustrative summary drawer; not a claim about an Uber subscription flow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
    item-divider: "{colors.surface-pressed}"
  ex-app-shell-row:
    description: "Illustrative app shell row; not a claim about Uber navigation."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Illustrative data table using the portable type scale."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.body-sm-strong}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.surface-pressed}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors card-content chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as card-content with Level 2 drop shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.2xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame. Generous padding on canvas-soft surface."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — flat-cornered card-content chrome with Level 2 drop shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---

## Scope and sources

This is a reusable **Uber-inspired** interpretation, not a current Uber brand kit or a copy of a live product screen. [Uber Base](https://base.uber.com/) is the official design-system source. Its [typography guidance](https://base.uber.com/6d2425e9f/p/976582-typography/b/667160) identifies Uber Move family roles. The public [ride page](https://www.uber.com/us/en/ride/) shows a request flow, but its copy, services, prices, and layout can vary by region and date. Check the current official page before using product-specific material.

The YAML preserves a black/white/gray reference palette, a type scale, and reusable components. Its values are **design starting points**, not measured CSS from every Uber screen. The `ex-*` components are generated examples for kit previews; they do not assert that Uber has those pricing tiers, drawers, tables, or app shell patterns.

## Typography and portability

Uber Move and Uber Move Text are source references. No redistribution right was established here. Deploy the YAML's [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with `system-ui, sans-serif` fallback on macOS, Windows, and Linux. Check font loading and mixed-script line wraps in the rendered app. The size and weight tokens express hierarchy; adapt them to the language and viewport. Do not package Uber fonts or logo assets without verifying the applicable rights.

## Color and components

- Black (`{colors.primary}`) and white (`{colors.canvas}`) form the main reference surfaces. `{colors.body}` is secondary text on light surfaces. `{colors.mute}` is for dark-surface secondary text or nonessential decoration; on white it is too faint for ordinary body copy.
- Keep light-surface links distinct with an underline. `link-mute` uses `{colors.hairline-mid}` on light surfaces only. `link-mute-soft` uses `{colors.mute}` on black surfaces only. The `#0000ee` link token is an illustrative conventional link color, not a claim that Uber uses browser-default blue everywhere.
- White buttons, cards, and inputs can disappear against a white canvas. Their YAML components use `{colors.control-border-light}` as a visible edge. On dark surfaces, use `{colors.control-border-dark}` and check the actual composited result. Decorative dividers may be lighter, but cannot be the only boundary of an interactive control.
- Pill, square, and rounded controls coexist in these reusable tokens. Choose the shape for the task; do not force every interactive element into a pill. `button-large-rounded` and the text inputs are deliberate non-pill variants.
- Links must remain identifiable without color alone. Inputs need visible labels, errors in text, and a visible keyboard focus treatment. Add a focus outline that contrasts with both the control and its surrounding surface; test the composed state, not only the color token.

## Layout and content

Use the ride-request card only as an illustrative composition. A live flow may have different fields, availability, regulatory text, and prices. Check the current region-specific Uber page before publishing names, offers, or service claims. Images, illustrations, screenshots, and maps require source and rights checks; no universal 4:3 ratio or recurring annual campaign is asserted here. Crop, overlay text, and responsive layout need inspection at target widths.

The spacing and card tokens can start a responsive layout. Confirm actual touch-target dimensions and spacing in the rendered app. Padding alone does not prove a WCAG target-size level; test keyboard order, focus visibility, zoom, and mobile touch interaction. For photography or maps behind text, measure contrast after the final image, crop, and overlay are chosen.

## Reuse checklist

1. Verify current product names, regional availability, prices, and copy on the official Uber page.
2. Confirm rights for Uber marks, fonts, screenshots, photography, maps, and illustrations, or use original assets.
3. Load the portable font stack on each target operating system and inspect wrapping.
4. Render buttons, inputs, links, cards, focus states, errors, and dark-surface variants; measure contrast and touch targets in context.
5. Treat every `ex-*` component as a kit demonstration until it is adapted and tested for the actual product.
