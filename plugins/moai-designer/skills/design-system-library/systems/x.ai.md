---
version: alpha
name: xAI-design-analysis
description: A dark x.ai-era design reference for the site now branded SpaceXAI. Use portable fonts and verify current products, marks, assets, and rendered accessibility before reuse.

colors:
  primary: "#ffffff"
  on-primary: "#0a0a0a"
  ink: "#ffffff"
  ink-hover: "#fafaf7"
  body: "#dadbdf"
  body-mid: "#7d8187"
  mute: "#7d8187"
  hairline: "#212327"
  canvas: "#0a0a0a"
  canvas-soft: "#1a1c20"
  canvas-card: "#191919"
  canvas-mid: "#363a3f"
  accent-sunset: "#ff7a17"
  accent-sunset-soft: "#ffc285"
  accent-dusk: "#7c3aed"
  accent-twilight: "#c4b5fd"
  accent-breeze: "#a0c3ec"
  accent-midnight: "#0d1726"
  control-border-dark: "#8c8c8c"

typography:
  display-xl:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 96px
    fontWeight: 400
    lineHeight: 110px
    letterSpacing: -2.4px
  display-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 72px
    fontWeight: 400
    lineHeight: 83px
    letterSpacing: -1.8px
  display-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 400
    lineHeight: 58px
    letterSpacing: -1.2px
  display-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 32px
    fontWeight: 400
    lineHeight: 36px
    letterSpacing: -0.6px
  display-xs:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 28px
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  caption-mono:
    fontFamily: JetBrains Mono, ui-monospace, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 1.4px
  caption-mono-sm:
    fontFamily: JetBrains Mono, ui-monospace, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 1.2px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px

rounded:
  none: 0px
  sm: 8px
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
    minHeight: 44px
    minWidth: 44px
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  button-outline-on-dark:
    backgroundColor: "{colors.canvas}"
    minHeight: 44px
    minWidth: 44px
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.sm} {spacing.lg}"
  button-outline-sm:
    backgroundColor: "{colors.canvas}"
    minHeight: 44px
    minWidth: 44px
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: "{spacing.xs} {spacing.md}"
  text-input:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input-focus:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    outlineColor: "{colors.ink}"
    outlineStyle: solid
    outlineWidth: 2px
    outlineOffset: 2px
    typography: "{typography.body-md}"
  card-content:
    backgroundColor: "{colors.canvas-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  card-feature-product:
    backgroundColor: "{colors.canvas-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  hero-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.4xl} {spacing.xl}"
  content-band:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.4xl} {spacing.xl}"
  eyebrow-mono:
    textColor: "{colors.ink}"
    typography: "{typography.caption-mono}"
  divider-hairline:
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.3xl} {spacing.xl}"

  # ─── Examples (illustrative) — auto-derived; resolve any TO_FILL markers below ───
  ex-pricing-tier:
    description: "Illustrative pricing tier; not a current SpaceXAI product or price claim."
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.control-border-dark}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-pricing-tier-featured:
    description: "Illustrative highlighted tier with a fixed light surface and dark text; not a live SpaceXAI plan."
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-product-selector:
    description: "What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery)."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-cart-drawer:
    description: "Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart)."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    item-divider: "{colors.hairline}"
  ex-app-shell-row:
    description: "Illustrative app shell row, not a claim about current SpaceXAI navigation."
    backgroundColor: "{colors.canvas}"
    activeIndicator: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  ex-data-table-cell:
    description: "Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm."
    headerBackground: "{colors.canvas-soft}"
    headerTypography: "{typography.caption-mono}"
    bodyTypography: "{typography.body-sm}"
    cellPadding: "{spacing.md} {spacing.lg}"
    rowBorder: "{colors.hairline}"
  ex-auth-form-card:
    description: "Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-modal-card:
    description: "Modal dialog surface — same chrome as feature-card with elevated shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  ex-empty-state-card:
    description: "Empty-state illustration frame."
    backgroundColor: "{colors.canvas-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.3xl}"
    captionTypography: "{typography.body-md}"
  ex-toast:
    description: "Toast notification surface — feature-card shape + medium shadow."
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    typography: "{typography.body-sm}"

---

## Scope and current official sources

This is a **dark x.ai-era reference**. The current [x.ai homepage](https://x.ai/) identifies the company as **SpaceXAI** and shows Grok, developer tools, and other current products. Do not treat the older page's exact navigation, product cards, model names, or CTA copy as current. The profile file name remains `x.ai.md` for catalog continuity; its dark palette is one possible design starting point, not a claim that every current SpaceXAI screen is dark.

The [SpaceXAI brand guidelines](https://x.ai/legal/brand-guidelines) govern use of its names and marks. They prohibit misleading endorsement or using the marks as part of another product name, and require downloaded logos to be used as provided. This kit does not grant a license to copy the mark or original media. Confirm permitted use before publishing a SpaceXAI-branded artifact. The `ex-*` components are generated design-kit examples and do not describe live SpaceXAI pricing, subscriptions, drawers, or application flows.

## Typography and portability

Universal Sans is an original-site reference, not a font distributed by this kit. The YAML uses [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) for display and body, and [OFL JetBrains Mono](https://github.com/google/fonts/blob/main/ofl/jetbrainsmono/METADATA.pb) for technical captions, each with operating-system fallbacks. Confirm actual font loading and line breaks on macOS, Windows, and Linux. The larger display line heights leave room for fallback glyphs and translated text; adapt size and tracking to content rather than forcing one English line break.

## Color and controls

- `{colors.canvas}` is a dark reference surface with white `{colors.ink}` text. `{colors.body-mid}` on it calculates to 5.06:1; verify any composited or translucent variant separately.
- `{colors.hairline}` is only a decorative divider: its `#212327` value calculates to 1.26:1 against the dark canvas. Interactive controls and cards use `{colors.control-border-dark}` (`#8c8c8c`), calculated at 5.89:1 against canvas and 5.23:1 against the dark card.
- The small button's original padding did not establish a touch target. The YAML now sets a 44px minimum height and width for button variants; verify spacing and the final rendered hit area as well. Inputs have a visible focus variant with explicit outline style and width. Links need a non-color cue such as an underline.
- Orange, violet, and blue accent tokens are illustrative. Do not use them as status or text colors without measuring contrast against the chosen background. Convey status with text or an icon alongside color.

## Layout, content, and verification

Use hero bands, product cards, and illustrations only after checking the current official site and asset rights. Present model availability, prices, performance figures, and company descriptions from current primary sources at publication time. No universal no-photography, pill-only, or dark-only rule is asserted here.

### Applying this reference

- Start a dark composition with `hero-band` or `content-band` on `{colors.canvas}`. Set the display token according to the available width; the 96px `display-xl` is a large-screen example, not a mobile minimum. At narrow widths, stack text and media and reduce the display size before text clips.
- `nav-bar` and `footer` share the dark canvas. Their text roles differ: use `{colors.ink}` for primary navigation and `{colors.body}` for supporting footer copy. Give navigation links an underline or another visible non-color cue for interactive states.
- `card-content` and `card-feature-product` place white text on `{colors.canvas-card}` with `{colors.control-border-dark}` as a boundary. Use `eyebrow-mono` only for short technical labels; its wide tracking and uppercase style are unsuitable for long or translated sentences.
- `button-primary` is a light-filled example, while `button-outline-on-dark` and `button-outline-sm` are dark examples with visible borders. Keep their minimum target dimensions and verify focus, label wrapping, and spacing in the final layout. `text-input` has a separate focus variant; labels and errors must be added by the consuming interface.
- `ex-*` surfaces demonstrate how to adapt these tokens to unrelated kit screens. Their pricing, selector, cart, and table names are not evidence that SpaceXAI offers those specific flows. The featured tier is a fixed light-on-dark-context example; define separate theme tokens before using it in a light theme.

Render at target widths and zoom levels. Inspect typography, keyboard order, focus, link identification, card and input boundaries, touch targets, and any text placed over media. Static token calculations cannot establish rendered accessibility or host-app behavior.
