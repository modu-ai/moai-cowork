---
version: alpha
name: Together AI-design-analysis
description: An inspired Together AI cloud design reference with dark and light bands, a multicolor accent, and technical labels. Use portable OFL fonts and verify current products, prices, assets, and rendered contrast before reuse.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#000000"
  body: "#666666"
  hairline: "#767676"
  canvas: "#ffffff"
  canvas-dark: "#010120"
  surface-dark-soft: "#313641"
  control-border-dark: "#8c8c8c"
  on-dark: "#ffffff"
  accent-orange: "#fc4c02"
  accent-magenta: "#ef2cc1"
  accent-periwinkle: "#bdbbff"
  accent-mint: "#c8f6f9"

typography:
  display-xxl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 64px
    fontWeight: 500
    lineHeight: 70.4px
    letterSpacing: -1.92px
  display-xl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 40px
    fontWeight: 500
    lineHeight: 48px
    letterSpacing: -0.8px
  display-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 28px
    fontWeight: 500
    lineHeight: 32.2px
    letterSpacing: -0.42px
  display-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 22px
    fontWeight: 500
    lineHeight: 25.3px
    letterSpacing: -0.22px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 23.4px
    letterSpacing: -0.18px
  body-lg-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 23.4px
    letterSpacing: -0.18px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: -0.16px
  body-md-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: -0.16px
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 19.6px
  caption-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 19.6px
  mono-caps-button:
    fontFamily: JetBrains Mono, ui-monospace, monospace
    fontSize: 16px
    fontWeight: 500
    lineHeight: 21px
    letterSpacing: 0.08px
  mono-caps-eyebrow:
    fontFamily: JetBrains Mono, ui-monospace, monospace
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.55px
  mono-caps-label:
    fontFamily: JetBrains Mono, ui-monospace, monospace
    fontSize: 12px
    fontWeight: 500
    lineHeight: 18px
    letterSpacing: 0.055px
  mono-caption:
    fontFamily: JetBrains Mono, ui-monospace, monospace
    fontSize: 12px
    fontWeight: 400
    lineHeight: 18px
    letterSpacing: 0.05px

rounded:
  none: 0px
  xs: 3.25px
  sm: 4px
  md: 8px
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
  4xl: 44px
  5xl: 48px
  6xl: 55.2px
  section: 80px

components:
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.3xl}"
  nav-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  button-secondary-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  button-secondary-white:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  button-ghost-on-dark:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.xs}"
  button-icon-circular:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary}"
    outline: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  badge-neutral:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  badge-subtle-on-dark:
    backgroundColor: "{colors.surface-dark-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xxl}"
    padding: "{spacing.section} {spacing.3xl}"
  research-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.3xl}"
  feature-tab-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.2xl}"
  feature-tab-pill-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.body-md-strong}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.2xl}"
  pricing-sub-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  pricing-sub-tab-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
  stats-card-tinted:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  research-card:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  testimonial-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  article-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.display-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  code-editor-mockup:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  data-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    padding: "{spacing.md} {spacing.lg}"
  data-table-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.mono-caps-eyebrow}"
    padding: "{spacing.md} {spacing.lg}"
  toggle-pill-group:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs}"
  toggle-pill-selected:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.mono-caps-button}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.2xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.3xl}"
  footer-wordmark-banner:
    assetRequirement: "Use approved Together AI wordmark artwork; do not recreate it with a substitute font."
    backgroundColor: "{colors.canvas}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Default Pricing tier card. Mirrors article-card chrome on canvas-soft surface with a hairline border."
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-pricing-tier-featured:
    description: "Featured tier — polarity-flipped to canvas-dark with white text."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.control-border-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-product-selector:
    description: "What's Included summary card — repurposed for the brand's GPU / inference packaging tiers."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
  ex-cart-drawer:
    description: "Subscription summary — line items per add-on (NOT a literal e-commerce cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.2xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Sidebar nav row. Active state uses brand primary as a left-edge indicator bar."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Mirrors the brand's pricing-page table. Header uses mono-caps-eyebrow uppercase; body uses body-md."
    headerBackground: "{colors.canvas}"
    headerTypography: "{typography.mono-caps-eyebrow}"
    bodyTypography: "{typography.body-md}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Mirrors article-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as article-card; relies on tinted scrim instead of card shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame. Generous padding on canvas-soft surface."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.5xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — flat-cornered article-card chrome with a soft brand-tinted drop shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-md}"

---


## Overview

This is an inspired Together AI cloud design reference. The [current official products page](https://www.together.ai/products) covers inference, compute, model shaping, and other platform services; the [pricing page](https://www.together.ai/pricing) contains changing models, rates, and product categories. Build any live pricing or product UI from those current sources instead of copying labels, model names, or amounts from a design example.

The palette pairs dark navy and white bands with orange, magenta, and periwinkle accents. The gradient is an optional historical visual treatment, not a requirement for every current surface. Use approved logos, customer stories, photographs, and illustrations; a public page does not by itself grant reuse rights.

## Colors and Contrast

- `canvas` is white with black `ink`. Required secondary text uses `body` `#666666`, which measures 5.74:1 on white.
- `canvas-dark` is `#010120` with white `on-dark` text. `surface-dark-soft` can separate a nested panel, but required boundaries use `control-border-dark` `#8c8c8c`.
- `hairline` `#767676` is the required visible boundary on white for inputs, buttons, cards, and table rows. A pale decorative divider may be added separately; do not replace the control boundary with an 8%-opacity black line.
- Orange `#fc4c02`, magenta `#ef2cc1`, and periwinkle `#bdbbff` are accent references. Check text, icons, and borders against the actual gradient or tinted surface. Do not put small required text directly on an unmeasured gradient.
- Mint `#c8f6f9` can fill a secondary button or stat card with dark text. Give mint-on-white controls the visible `hairline` border from the YAML.

## Typography and Portability

The original source reference mentions `The Future` and `PP Neue Montreal Mono`; their distribution rights and present-day use are not established here. The deployable YAML uses [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) for display and body text, and [OFL JetBrains Mono](https://github.com/google/fonts/blob/main/ofl/jetbrainsmono/METADATA.pb) for short technical labels, each with system fallbacks. Verify actual font loading, weights, glyph coverage, and mixed-script line breaks on each target OS.

`display-xxl` is 64px/500 with a 70.4px line box. `body-md` is 16px/400 with a 24px line box. `mono-caps-button` is 16px/500 with a 21px line box. Required labels and code captions are at least 12px in the portable tokens; check legibility at zoom rather than treating a former 10–11px extraction as a target.

Keep long paragraphs in Inter. Uppercase JetBrains Mono can label short categories, tabs, and model columns when the current product calls for them. The font families are substitutes; do not claim they exactly reproduce source metrics or force a global OpenType feature without testing.

## Components

- `button-primary` uses black fill and white text. `button-secondary-mint` and `button-secondary-white` use dark text and a visible border. `button-ghost-on-dark` has a visible dark-surface border. Provide distinct hover, pressed, disabled, and keyboard-focus states in the running interface.
- `button-outline` and `text-input` use `hairline` borders on white. `text-input-focused` adds a dark outline. Keep labels, errors, and help text visible without depending on color alone.
- `research-card`, `testimonial-card`, `article-card`, `data-table-row`, and `ex-pricing-tier` have explicit boundaries in YAML. `research-card` uses `control-border-dark`; light cards use `hairline`. Verify borders against every actual nested surface.
- `data-table-header` uses white background and dark secondary text. Preserve table headers and associations when model names or price cells reflow; derive every current model and rate from official pricing data.
- `feature-tab-pill`, `pricing-sub-tab`, and `toggle-pill-group` use a visible `hairline` boundary on white. Their selected variants use black fill with white text. Expose the selected state in text or accessible state attributes, keep a 2px visible keyboard-focus outline distinct from selection, and verify all three states in the rendered UI.
- `hero-band-dark`, `research-band-dark`, `stats-card-tinted`, and `footer-wordmark-banner` are optional inspired treatments. Check current branding and do not recreate a company wordmark using a substitute font.
- `button-icon-circular` and the `ex-*` entries are illustrative component examples. They do not prove that the current site has a chat launcher, subscription cart, GPU tier selector, toast, or auth card. Keep their labels and behavior conditional on the actual product flow.

## Layout and Interaction

Use the declared spacing and radius tokens as starting points, then size sections from actual content. The old fixed grid counts and breakpoint list are reference observations, not a cross-platform contract. Test narrow and wide windows, zoom, long labels, and mixed-script content. A pricing table may need horizontal scrolling or stacked rows while preserving column meaning and keyboard access.

Measure rendered targets and spacing. The YAML's 4px vertical button padding alone does not establish an accessible target. Preserve visible focus and error states, and check the contrast of image and gradient overlays on every crop. Use responsive images and alt text for permitted media.

## Iteration Guide

1. Choose the current product and page from the official Together AI site, then confirm its content and pricing.
2. Start with the YAML's portable fonts and dark/light color pairs; check actual rendering before tightening type or spacing.
3. Use `ex-*` examples as layout demonstrations only, and replace all business data with verified current data.
4. Check borders, text, links, focus, errors, target sizes, and responsive tables in the rendered page.
5. Use approved logos, customer stories, screenshots, and images only after confirming their rights and freshness.

## Known Gaps

- This profile does not establish the current brand's exact CSS, every product category, model, price, claim, or logo usage right.
- Current asset rights and the real rendered contrast of gradients, photos, nested cards, and focus rings have not been verified.
- Inter and JetBrains Mono loading, mixed-script layout, and behavior in Claude Cowork or ChatGPT Work on macOS, Windows, and Linux have not been observed.
