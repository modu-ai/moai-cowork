---
version: alpha
name: Zapier-design-analysis
description: A Zapier-inspired orange, cream, and dark design reference. Use portable fonts and verify current products, pricing, brand assets, and rendered accessibility before reuse.

colors:
  primary: "#ff4f00"
  on-primary: "#201515"
  on-dark: "#fffefb"
  ink: "#201515"
  ink-soft: "#2f2a26"
  ink-mid: "#36342e"
  body: "#605d52"
  body-mid: "#6b665c"
  mute: "#c5c0b1"
  canvas: "#fffefb"
  canvas-soft: "#f8f4f0"
  control-border-light: "#767676"

typography:
  display-xl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 56px
    fontWeight: 500
    lineHeight: 64px
  display-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 500
    lineHeight: 56px
  display-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 500
    lineHeight: 36px
    letterSpacing: 1px
  display-sub-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 500
    lineHeight: 56px
  display-sub-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 400
    lineHeight: 40px
  display-sub-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 30px
    letterSpacing: -0.6px
  display-xs:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 700
    lineHeight: 25px
    letterSpacing: -0.5px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 30px
    letterSpacing: -0.2px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 27px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 27px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-sm-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 24px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 21px
  eyebrow-uppercase:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 1px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 27px
  button-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 20px
    letterSpacing: 0.144px

rounded:
  none: 0px
  sm: 6px
  md: 12px
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
  4xl: 64px

components:
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.xl}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.xl}"
  button-tertiary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderStyle: solid
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.xl}"
  button-text:
    textDecoration: underline
    borderColor: "{colors.control-border-light}"
    borderStyle: solid
    borderWidth: 1px
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderStyle: solid
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderStyle: solid
    borderWidth: 1px
    outlineColor: "{colors.ink}"
    outlineStyle: solid
    outlineWidth: 2px
    outlineOffset: 2px
    typography: "{typography.body-md}"
  card-content:
    borderColor: "{colors.control-border-light}"
    borderStyle: solid
    borderWidth: 1px
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  card-feature-cream:
    borderColor: "{colors.control-border-light}"
    borderStyle: solid
    borderWidth: 1px
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  card-feature-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderStyle: solid
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  pricing-card-featured:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.xl}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.xl}"
  content-band-cream:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.4xl} {spacing.xl}"
  content-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.4xl} {spacing.xl}"
  eyebrow-uppercase:
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow-uppercase}"
  badge-pill:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Illustrative pricing tier; verify current Zapier plans and prices."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-light}"
    borderStyle: solid
    borderWidth: 1px
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Illustrative highlighted tier with a fixed dark surface and light text; not a live Zapier plan."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Illustrative summary drawer, not a live Zapier billing flow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    item-divider: "{colors.control-border-light}"
  ex-app-shell-row:
    description: "Illustrative app shell row, not a claim about current Zapier navigation."
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
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---

## Scope and official sources

This is a **Zapier-inspired** reusable reference, not a current Zapier product or pricing specification. Zapier's [brand announcement](https://zapier.com/blog/zapiers-new-look/) describes the orange update and identifies Degular as the brand typeface. The [official newsroom](https://zapier.com/press) links to downloadable marks, product screenshots, and [brand guidelines](https://brand.zapier.com/). Use those official resources to check any real Zapier asset. The site now presents multiple automation products; confirm product names, features, and prices on its current pages before publishing.

The YAML's cream, orange, and coffee tones and reusable components are interpretation tokens, not a scrape of every Zapier screen. `ex-*` components demonstrate kit surfaces; their pricing tiers, subscription drawer, app shell, and table are not assertions about live Zapier flows.

## Typography and assets

Degular is the original brand reference. No redistribution license for Degular was established here, so the deployable YAML uses [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with `system-ui, sans-serif` fallback. The display hierarchy is illustrative; adjust sizes and line wraps for the actual language, operating system, and viewport. Inspect the loaded font on macOS, Windows, and Linux. Downloading an official logo or screenshot does not by itself establish permission for every use; follow Zapier's current brand guidelines and asset terms.

## Color and controls

- Orange `{colors.primary}` with warm-white text calculates to 3.27:1. The paired `{colors.on-primary}` token is therefore dark `#201515`, calculated at 5.40:1 against orange. Dark cards and buttons use the separate light `{colors.on-dark}` token.
- `{colors.body-mid}` now uses `#6b665c`, calculated at 5.66:1 on warm white and 5.21:1 on soft cream. The previous `#939084` was 3.17:1 on warm white. `{colors.mute}` is decorative or disabled on light surfaces; do not use it for required captions.
- Pale cards and white text buttons can vanish on a warm-white canvas. The YAML gives light cards and the text button a `{colors.control-border-light}` edge and underlines the text button. Links elsewhere also need a non-color cue. The input focus variant specifies color, style, width, and offset; test it in the final rendered context.
- Status, validation, and errors need explicit words or icons. Orange cannot be the only error indicator just because it is the brand accent.

## Applying the components

Use `hero-band`, `hero-band-dark`, and cream or light content bands as optional compositions. The display tokens suit short headings; stack columns and reduce display size at narrow widths. `card-content` and `card-feature-cream` need their edge on a pale canvas. `pricing-card` and `pricing-card-featured` are layout examples only: fetch current price, plan eligibility, trial terms, and region-specific copy before reuse. The button tokens encode an action hierarchy, but do not require one shape for all screens.

Render the interface at target widths and zoom levels. Measure keyboard focus, contrast, touch area and spacing, input errors, and translated text expansion. No padding token or flat-color calculation proves a rendered accessibility pass.
