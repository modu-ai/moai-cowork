---
version: alpha
name: Wise-design-analysis
description: A Wise-inspired green and neutral design reference. Use portable fonts and verify current regional fees, product content, assets, and rendered accessibility before reuse.

colors:
  primary: "#9fe870"
  on-primary: "#0e0f0c"
  primary-active: "#cdffad"
  primary-neutral: "#c5edab"
  primary-pale: "#e2f6d5"
  ink: "#0e0f0c"
  ink-deep: "#163300"
  body: "#454745"
  mute: "#62645e"
  canvas: "#ffffff"
  canvas-soft: "#e8ebe6"
  positive: "#187239"
  positive-deep: "#054d28"
  warning: "#ffd11a"
  warning-deep: "#b86700"
  warning-content: "#4a3b1c"
  negative: "#d03238"
  negative-deep: "#a72027"
  negative-darkest: "#a7000d"
  negative-bg: "#320707"
  accent-orange: "#ffc091"
  accent-cyan: "#38c8ff"
  control-border-light: "#767676"
  control-border-dark: "#b7b7b7"

typography:
  display-mega:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 126px
    fontWeight: 900
    lineHeight: 139px
  display-xxl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 96px
    fontWeight: 900
    lineHeight: 106px
  display-xl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 64px
    fontWeight: 900
    lineHeight: 72px
  display-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 47px
    fontWeight: 400
    lineHeight: 70.5px
    letterSpacing: -0.108px
  display-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 40px
    fontWeight: 900
    lineHeight: 48px
  display-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 600
    lineHeight: 38.4px
    letterSpacing: -0.96px
  display-xs:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 31.2px
    letterSpacing: -0.48px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 30px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 20px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px

rounded:
  none: 0px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
    padding: "{spacing.md} {spacing.xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm-strong}"
  button-primary:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.xl}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.xl}"
  button-icon-circular:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    outlineColor: "{colors.ink}"
    outlineStyle: solid
    outlineWidth: 2px
    outlineOffset: 2px
    typography: "{typography.body-md}"
  text-input-focus-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    outlineColor: "{colors.canvas}"
    outlineStyle: solid
    outlineWidth: 2px
    outlineOffset: 2px
    typography: "{typography.body-md}"
  card-content:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-feature-sage:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-feature-green:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  card-feature-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-mega}"
    padding: "{spacing.3xl} {spacing.xl}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.primary}"
    typography: "{typography.display-mega}"
    padding: "{spacing.3xl} {spacing.xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.3xl} {spacing.xl}"
  currency-converter-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  badge-positive:
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.positive-deep}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  badge-negative:
    backgroundColor: "{colors.negative-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm-strong}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Illustrative pricing tier; verify current regional product and fees."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-light}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode)."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Illustrative summary drawer, not a Wise fee quote."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    item-divider: "{colors.control-border-light}"
  ex-app-shell-row:
    description: "Illustrative app shell row, not a claim about Wise navigation."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.control-border-light}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.xl}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---

## Scope and official sources

This is a **Wise-inspired** reusable reference, not a current Wise product specification. [Wise Design](https://wise.design/) publishes public component and pattern guidance. Its [list item guidance](https://wise.design/components/list-item) explicitly covers focus states, clear content, and avoiding color-only meaning. Its [trust pattern](https://wise.design/patterns/highlight-trust) shows both light and forest-green themes and warns about translation length. These sources do not establish one universal page layout or converter-card placement.

Wise's [conversion help](https://wise.com/help/articles/2596980/how-can-i-convert-money) says fees vary by currency. Its [account help](https://wise.com/help/articles/2897226/what-is-a-wise-account) says the main account name can vary by location. Verify country, currency, fee, rate, eligibility, and legal copy in the live product before publishing a financial example. `ex-*` components are kit demonstrations, not live Wise pricing or transaction flows.

## Typography and assets

Wise Sans is a source reference; this work did not establish rights to redistribute it. The YAML deploys [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with `system-ui, sans-serif` fallback. Its large display sizes are examples and must scale with viewport and translated copy. Line heights were raised to avoid clipping under fallback and mixed-script rendering. Inspect the actual font load and wrapping on macOS, Windows, and Linux. Use original graphics or confirm rights for Wise's logo, flags, illustrations, screenshots, and typeface.

## Color and controls

- Bright green (`{colors.primary}`) with near-black text (`{colors.on-primary}`) calculates to 13.05:1. Bright green on white calculates to only 1.47:1, so do not use it as small text or the sole boundary of a control on white.
- `{colors.mute}` now uses `#62645e`, calculated at 5.99:1 on white and 4.98:1 on the sage canvas. The old `#868685` was 3.64:1 on white and 3.03:1 on sage.
- The positive color is an illustrative semantic token; pair every status color with text or an icon and verify the final background. Warning and error messages need text labels and measured contrast, not color alone.
- White cards, buttons, and inputs need a visible boundary on white or pale surfaces. The YAML gives light controls `{colors.control-border-light}` and provides separate input focus variants for light and dark surroundings. Links require an underline or other non-color cue. Verify the composed focus outline, not just its token.

## Layout and verification

The converter card, green hero, dark hero, and soft-surface cards are optional compositions. Avoid copying balances, exchange rates, fees, testimonials, or account screenshots into new work without current source and permission. For currency amounts, show clear units and distinguish an indicative estimate from a confirmed quote; verify the actual amount and legal wording for the market.

Render the resulting interface at target widths and zoom levels. Measure touch targets and spacing, keyboard order, focus, contrast, error states, and translation expansion in the final screen. Token padding alone does not establish an accessibility pass.
