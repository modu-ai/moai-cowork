---
version: alpha
name: Vodafone-design-analysis
description: A Vodafone-inspired red, dark, and light design reference. Use portable fonts and verify current local product content, campaign assets, and rendered accessibility before reuse.

colors:
  primary: "#e60000"
  on-primary: "#ffffff"
  ink: "#25282b"
  body: "#5f5f5f"
  mute: "#bebebe"
  canvas: "#ffffff"
  canvas-soft: "#f2f2f2"
  on-dark: "#ffffff"
  control-border-light: "#767676"
  control-border-dark: "#bebebe"

typography:
  display-hero:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 144px
    fontWeight: 800
    lineHeight: 160px
    letterSpacing: -1px
  display-xxl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 126px
    fontWeight: 800
    lineHeight: 140px
    letterSpacing: -1px
  display-xl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 90px
    fontWeight: 800
    lineHeight: 100px
  display-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 300
    lineHeight: 52px
  display-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 40px
    fontWeight: 300
    lineHeight: 44px
  display-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
  display-xs:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 700
    lineHeight: 30px
  eyebrow-uppercase:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 800
    lineHeight: 24px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 22px
    fontWeight: 400
    lineHeight: 30px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 28px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 700
    lineHeight: 22px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  caption-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 700
    lineHeight: 21px
  caption-uppercase:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 600
    lineHeight: 16px
    letterSpacing: 0.5691px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px

rounded:
  none: 0px
  xs: 1px
  sm: 6px
  card: 6px
  pill-md: 32px
  pill-lg: 60px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px

components:
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill-lg}"
    padding: "{spacing.md} {spacing.2xl}"
  button-outline-red:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill-lg}"
    padding: "{spacing.md} {spacing.2xl}"
  button-outline-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill-lg}"
    padding: "{spacing.md} {spacing.2xl}"
  button-icon-circular:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-light}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    outlineColor: "{colors.ink}"
    outlineOffset: 2px
    typography: "{typography.body-sm}"
  text-input-focus-on-dark:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    outlineColor: "{colors.on-dark}"
    outlineOffset: 2px
    typography: "{typography.body-sm}"
  badge-chip:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.pill-md}"
    padding: "{spacing.xs} {spacing.md}"
  card-content:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  card-hero:
    borderColor: "{colors.control-border-light}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  hero-band-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-hero}"
    padding: "{spacing.3xl} {spacing.3xl}"
  hero-band-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.3xl} {spacing.3xl}"
  content-band-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.3xl} {spacing.3xl}"
  speechmark-logo-orb:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  divider-on-dark:
    borderColor: "{colors.on-dark}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.3xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Illustrative pricing tier; verify current plans and prices before use."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-light}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to ink with white text and white pill CTA inside."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-product-selector:
    description: "Illustrative plan selector; check current tariffs in the target market."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-cart-drawer:
    description: "Illustrative subscription summary, not a claim about a live Vodafone plan."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
    item-divider: "{colors.control-border-light}"
  ex-app-shell-row:
    description: "Illustrative app shell row, not a claim about Vodafone navigation."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table cell chrome. Header uses caption-uppercase mono-style eyebrow; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption-uppercase}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.control-border-light}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors card-content chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as card-content; brand uses scrim, not card shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.card}"
    padding: "{spacing.lg}"
  ex-empty-state-card:
    description: "Empty-state illustration frame on canvas-soft with generous interior padding."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.card}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — card-content shape with caption-strong body."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---

## Scope and official sources

This file is a **Vodafone-inspired** reusable reference. Vodafone's [brand announcement](https://www.vodafone.com/news/newsroom/technology/vodafone-announces-new-brand-positioning-strategy) documents the speech mark and its 2017 visual identity change; it does not establish one permanent hero layout or button shape for every country and product. Vodafone's [accessibility statement](https://www.vodafone.com/site-services/accessibility) describes keyboard access and visible focus on its own site. Check the current local Vodafone site before using offers, service names, photographs, or campaign copy.

The YAML's red, dark, and light palette and component geometry are starting points, not measured CSS from all Vodafone properties. The `ex-*` entries are kit demonstrations; pricing tiers, subscription drawers, tables, and app shells are not claims about live Vodafone flows.

## Typography and assets

The Vodafone typeface is an original brand reference. No public font redistribution right was established here. The deployable YAML uses [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with `system-ui, sans-serif` fallback. Large display sizes are optional examples: scale them with available width and inspect line wraps in every supported language and operating system. The revised line heights leave more room for ascenders, descenders, and mixed scripts. Avoid all-caps text when the target language, readability, or content calls for sentence case.

Vodafone's speech mark is a protected brand asset. Its [code of conduct](https://www.vodafone.com/sites/default/files/2023-06/vodafone-code-of-conduct.pdf) tells third parties to discuss brand or logo use with Vodafone's legal team; the [site terms](https://www.vodafone.com/site-services/terms-and-condition) do not grant a brand license. Use the mark or original campaign photography only with the relevant permission. A generic red card in the kit must not masquerade as an authorized logo.

## Color and controls

- `{colors.primary}` red with white text calculates to 4.81:1; `{colors.body}` on white calculates to 6.39:1. The old body gray `#7e7e7e` calculated to 4.06:1 on white, so it is no longer the body token.
- `{colors.mute}` is too faint for ordinary text on white (1.86:1). It is suitable as secondary text on `{colors.ink}` only after checking the actual rendering (7.97:1 by flat-color calculation).
- Use `{colors.control-border-light}` for controls that need a visible edge on white and pale surfaces. Use `{colors.control-border-dark}` on dark surfaces. A white icon button on white must keep its border; a flat white card also needs an edge or other verified separation.
- Inputs need visible labels and text errors. Keep keyboard focus visible on both light and dark surfaces; the YAML includes separate focus variants. Links need an underline or equivalent non-color cue. Recheck contrast when opacity, photography, or overlays enter the composition.

## Layout and verification

The `hero-band-dark`, `hero-band-red`, and `content-band-light` components can be arranged for a specific page, but no fixed dark-hero-to-light-content sequence is required. Photography, crop, and text overlay are optional. Verify rights and text contrast on the final image at each responsive width. Do not infer a WCAG touch-target result from token padding; measure the rendered target and spacing with keyboard, zoom, and touch interaction.

Before publishing, verify the target market's tariff names, prices, eligibility, legal copy, and campaign status on the current official Vodafone property. Render the portable font stack on macOS, Windows, and Linux, then inspect large-type wrapping, focus, control boundaries, color contrast, and responsive behavior.
