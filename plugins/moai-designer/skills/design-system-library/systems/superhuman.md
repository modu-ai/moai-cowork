---
version: alpha
name: Superhuman-design-analysis
description: A historical Superhuman Mail marketing reference with indigo, white, and teal surfaces. Current Superhuman spans Mail, Grammarly, Docs, and Go; verify live pages, assets, and pricing before reuse. Portable tokens use OFL Inter Variable.

colors:
  primary: "#1b1938"
  primary-deep: "#0e0c1f"
  on-primary: "#ffffff"
  ink: "#292827"
  ink-mute: "#66615e"
  ink-faint: "#9a9794"
  canvas: "#ffffff"
  canvas-soft: "#fafaf8"
  surface-violet-soft: "#c9b4fa"
  surface-teal-deep: "#0e3030"
  surface-teal-mid: "#155555"
  hairline: "#e8e4dd"
  hairline-dark: "#3f3a52"
  control-border-light: "#767676"
  control-border-dark: "#a29db3"
  on-dark-mute: "#bcbac9"
  on-dark-faint: "#5a5772"

typography:
  display-xxl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 540
    lineHeight: 1.15
    letterSpacing: 0
  display-xl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 460
    lineHeight: 1.15
    letterSpacing: -1.32px
  display-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 540
    lineHeight: 1.14
    letterSpacing: -0.63px
  display-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 460
    lineHeight: 1.1
    letterSpacing: -0.315px
  heading-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 460
    lineHeight: 1.2
    letterSpacing: -0.4px
  body-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 540
    lineHeight: 1.5
    letterSpacing: -0.135px
  body-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 460
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18.72px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-cap:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  caption:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 460
    lineHeight: 1.4
    letterSpacing: 0
  micro:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 540
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  huge: 64px

components:
  button-primary-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-primary-dark-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  button-on-dark-pill:
    backgroundColor: "{colors.surface-violet-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
  button-secondary-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
    border: "1px solid {colors.control-border-light}"
  button-on-teal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.surface-teal-deep}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    border: "1px solid {colors.control-border-light}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    border: "2px solid {colors.primary}"
    outline: "2px solid {colors.primary}"
  card-feature-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-pricing-featured:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-dark}"
  card-teal-band:
    backgroundColor: "{colors.surface-teal-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: 64px
  card-feature-row:
    backgroundColor: "{colors.canvas-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
  pill-tab-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-cap}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.control-border-light}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
    textDecoration: underline
  footer-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-mute}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
---

## Overview

> **Scope:** This is an older Superhuman Mail marketing reference, not a current design contract for the [Superhuman suite](https://superhuman.com/plans), which now includes Mail, Grammarly, Docs, and Go. The company [describes Super Sans, Super Serif, and Super Mono](https://blog.superhuman.com/docs-new-visual-identity/) as its newer custom family. The deployable tokens below use [OFL Inter Variable](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with system fallbacks. Check current screens, pricing, image and logo rights, font loading, and mixed-script layout before publication.

The older Mail reference pairs an indigo `{colors.primary}` canvas with violet atmosphere and an optional portrait. Portable `{typography.display-xxl}` uses Inter at 64px / weight 540. Use only permitted imagery and check text contrast for every actual crop; choose the number of actions from the current task.

The reference body can shift to white. `{colors.canvas}` (`#ffffff`) takes over below the hero, with body type in `{colors.ink}` (`#292827` — a slightly warm dark grey, never pure black) and feature rows alternating between white and `{colors.canvas-soft}` (a barely-tinted off-white). Pricing tiers sit on this white surface; the featured tier inverts to the indigo navy, completing the brand's binary polarity.

Some older Mail pages use a **deep-teal CTA band** (`{colors.surface-teal-deep}` — `#0e3030`). When supported by the current page, it can hold a closing CTA in `{typography.display-lg}` with a white button.

The source uses a custom Super Sans family. Portable tokens use OFL Inter Variable at 460 / 540 / 600 where the loaded font supports those weights. Display tracking should be checked after loading; the largest line heights are 1.15 to avoid clipping.

**Key Characteristics:**
- Three-canvas system: indigo navy (`{colors.primary}`) for hero, white (`{colors.canvas}`) for body, deep teal (`{colors.surface-teal-deep}`) for closing CTA.
- Half-bleed portrait subject in the hero with violet-sky atmospheric backdrop — the brand uses a person looking off-frame as a recurring visual.
- Keep actions focused; confirm the current page flow before setting CTA count.
- Portable Inter Variable uses 460 / 540 / 600 weights where available.
- Portable large display line height is 1.15; check wrapping in the rendered page.
- Off-warm-grey body ink (`#292827`) — never pure black; the brand's quiet warmth.
- Pill-shaped on-hero CTA in pale violet (`{colors.surface-violet-soft}`); rounded-rectangle CTAs everywhere else.

## Colors

> **Historical reference paths:** home, product, sales, and plans. Confirm current suite routes and prices through the official site before reuse.

### Brand & Accent
- **Primary Indigo Navy** (`{colors.primary}` — `#1b1938`): The brand's primary surface and CTA color. Hero canvas, filled rounded-rectangle button, featured pricing tier.
- **Indigo Deep** (`{colors.primary-deep}` — `#0e0c1f`): Pressed-state lift / deeper navy used in hero gradient stops.
- **Surface Violet Soft** (`{colors.surface-violet-soft}` — `#c9b4fa`): The hero pill-button fill — pale violet over the indigo canvas. Also appears in atmospheric backdrops.
- **Surface Teal Deep** (`{colors.surface-teal-deep}` — `#0e3030`): The signature closing-CTA band color. Rich green-blue, almost black.
- **Surface Teal Mid** (`{colors.surface-teal-mid}` — `#155555`): Slightly lifted teal for nested chrome inside the band.

### Surface
- **Canvas** (`{colors.canvas}` — `#ffffff`): Default body background.
- **Canvas Soft** (`{colors.canvas-soft}` — `#fafaf8`): Barely-warm off-white for alternating feature-row bands.
- **Hairline** (`{colors.hairline}` — `#e8e4dd`): decorative divider only, not a required control boundary.
- **Hairline Dark** (`{colors.hairline-dark}` — `#3f3a52`): decorative dark divider only. Control borders use `{colors.control-border-light}` (`#767676`) on white and `{colors.control-border-dark}` (`#a29db3`) on dark surfaces.

### Text
- **Ink** (`{colors.ink}` — `#292827`): Default body text. Warm dark grey, never pure black.
- **Ink Mute** (`{colors.ink-mute}` — `#66615e`): Secondary text, captions.
- **Ink Faint** (`{colors.ink-faint}` — `#9a9794`): Decorative or disabled treatment only; do not use for required text.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): Text on dark navy / teal surfaces.
- **On Dark Mute** (`{colors.on-dark-mute}` — `#bcbac9`): Secondary text on dark.
- **On Dark Faint** (`{colors.on-dark-faint}` — `#5a5772`): Decorative or disabled treatment only; it measures 2.45:1 on indigo.

## Typography

### Font Family

The source custom family is a reference only. Deploy the declared Inter Variable stack with system fallbacks; verify loading and redistribution terms.

Inter Variable supports intermediate weights, but its metrics differ from the source face. Check each weight and line break on macOS, Windows, and Linux.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 64px | 540 | 1.15 | 0 | Hero headline |
| `{typography.display-xl}` | 48px | 460 | 1.15 | -1.32px | Section opener on light surfaces |
| `{typography.display-lg}` | 28px | 540 | 1.14 | -0.63px | Sub-section / feature title |
| `{typography.display-md}` | 22px | 460 | 1.1 | -0.315px | Card title |
| `{typography.heading-lg}` | 20px | 460 | 1.2 | -0.4px | Compact card title |
| `{typography.body-lg}` | 18px | 540 | 1.5 | -0.135px | Marketing body lead |
| `{typography.body-md}` | 16px | 460 | 1.5 | 0 | Default UI body |
| `{typography.body-strong}` | 18.72px | 700 | 1.5 | 0 | Emphasized body |
| `{typography.button-md}` | 16px | 700 | 1.3 | 0 | Rounded-rectangle button label |
| `{typography.button-cap}` | 14px | 600 | 1.3 | 0 | Compact button label |
| `{typography.caption}` | 14px | 460 | 1.4 | 0 | Helper, footnote |
| `{typography.micro}` | 12px | 540 | 1.4 | 0 | Pill label, fine print |

### Principles
- **Sub-default weights.** The brand picks 460 / 540 / 600 instead of 400 / 500 / 700 — a quiet warmth in the typography that distinguishes it from default SaaS systems.
- **Display leading.** Portable 48–64px tokens use 1.15; verify mixed-script line boxes and wrapping.
- **Negative tracking on display sizes.** -1.32px at 48px scaling proportionally — tightens the variable letterforms into editorial density.

### Note on Font Substitutes
Use the declared Inter Variable weights when loaded; browser `font-weight` normally selects the variable axis. Do not assume the source face's metrics or force `font-variation-settings` across the whole page.

## Layout

### Spacing System
- **Base unit**: 8px (with 2 / 4 / 12 sub-tokens for fine work).
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 64px.
- **Section padding**: 64–96px on most sections; closing teal band uses 96–128px for editorial weight.
- **Card internal padding**: 32px on pricing cards; 24px on alternating feature rows.

### Grid & Container
- Hero spans full viewport width with the violet-sky backdrop edge-to-edge; content centers in a ~960px column.
- Body content centers in ~960–1100px.
- Reflow the current plan cards to fit the actual content and viewport; the older Mail reference used 3-up → 2-up → 1-up.

### Whitespace Philosophy
The brand uses generous editorial whitespace on both polarities — dark hero and white body. Section gaps tend toward 96px; the teal closing band gets up to 128px of vertical air. The whitespace itself is part of the brand's "considered, slow-tempo" feel.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `box-shadow: 0 1px 3px rgba(0,0,0,0.08)` | Subtle card lift |
| 2 | `box-shadow: 0 8px 24px rgba(0,0,0,0.12)` | Floating panels, modals |
| 3 | Atmospheric backdrop (violet-sky over indigo) | The hero's depth medium |

### Decorative Depth
The hero's depth is the **violet-sky atmospheric backdrop** — a soft indigo-to-violet-to-sky-blue radial wash that sits behind the portrait subject. Implemented as a CSS radial gradient or large background image. Below the hero, depth is minimal — the white canvas is flat.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Hairline tags |
| `{rounded.sm}` | 6px | Form inputs |
| `{rounded.md}` | 8px | Rounded-rectangle buttons; a separate hero pill is available |
| `{rounded.lg}` | 12px | Pricing cards, feature cards |
| `{rounded.xl}` | 16px | Modal dialogs, large feature cards |
| `{rounded.full}` | 9999px | Pill tabs in feature row, hero CTA |

### Photography Geometry
The hero uses **half-bleed portrait subjects** — a person photographed at twilight, looking off-frame, occupying the right half of the hero. The portrait extends edge-to-edge vertically and stops mid-canvas horizontally; type sits on the left side. Other photography is rare; product UI mockups handle most other illustrative needs.

## Components

### Buttons

**`button-primary-dark`** — the dominant rounded-rectangle CTA on white surfaces.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `{spacing.md} {spacing.xl}` (12px 20px), rounded `{rounded.md}` 8px.
- Pressed state `button-primary-dark-pressed` shifts to `{colors.primary-deep}`.

**`button-on-dark-pill`** — the hero CTA in pale violet pill shape.
- Background `{colors.surface-violet-soft}`, text `{colors.primary}`, same typography, padding 12px 20px, rounded `{rounded.full}`. The pill shape only appears on the hero — body CTAs use the rounded rectangle.

**`button-secondary-outline`** — outline alternative on white.
- Background `{colors.canvas}`, text `{colors.ink}`, 1px solid `{colors.control-border-light}` border, same shape as `button-primary-dark`; provide a separate visible keyboard-focus ring.

**`button-on-teal`** — CTA inside the closing teal band.
- Background `{colors.canvas}`, text `{colors.surface-teal-deep}`, rounded-rectangle, same typography.

### Cards & Containers

**`card-feature-light`** — feature card on white.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`, 1px `{colors.control-border-light}` border.

**`card-pricing`** — standard pricing tier card.
- Background `{colors.canvas}`, padding `{spacing.xxl}`, rounded `{rounded.lg}`, 1px `{colors.control-border-light}` border.

**`card-pricing-featured`** — inverted indigo featured tier.
- Background `{colors.primary}`, text `{colors.on-primary}`, otherwise identical to `card-pricing`.

**`card-teal-band`** — an optional closing CTA treatment from the older Mail reference.
- Background `{colors.surface-teal-deep}`, text `{colors.on-primary}`, padding `{spacing.huge}` 64px, rounded `{rounded.lg}` 12px (often radius-less in practice when full-bleed). Holds a single closing headline in `{typography.display-lg}` and a `button-on-teal`.

**`card-feature-row`** — alternating feature-row card on the body.
- Background `{colors.canvas-soft}`, text `{colors.ink}`, padding `{spacing.xl}` 24px, rounded `{rounded.md}` 8px. Used in pairs/triplets to explain features below the hero.

### Inputs & Forms

**`text-input`** — standard form input.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding 10px 12px, rounded `{rounded.sm}` 6px, 1px `{colors.control-border-light}` border. `{components.text-input-focused}` adds a dark border and outline; verify the rendered focus state.

### Navigation

**`nav-bar-dark`** — top nav over the indigo hero.
- Background `{colors.primary}`, text `{colors.on-primary}`, padding `{spacing.lg} {spacing.xl}`. The historical layout puts a logo left and a CTA right; take the current wording, structure, and approved logo from the live product page.

**`nav-bar-light`** — top nav on body / pricing pages.
- Background `{colors.canvas}`, text `{colors.ink}`, otherwise same structure with `button-primary-dark` on the right.

### Pills, Tags, and Chips

**`pill-tab-light`** — feature-row tab selector.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button-cap}`, padding `{spacing.sm} {spacing.lg}`, rounded `{rounded.full}`. Used in the feature category picker (Mail / Channels / Code / AI / Calendar etc.) below the hero.

### Signature Components

**Half-Bleed Portrait Hero** — a historical Mail composition, with type left and a portrait right. Use it only when a current approved image and crop support readable text; it is not required for the present suite.

**Closing Teal Band** — use a `card-teal-band` only when the current page needs a closing CTA. Verify the live brand context first.

**`link-on-light`** — inline links on body.
- Text `{colors.ink}` rendered in `{typography.body-md}` with persistent underline.

**`footer-light`** — site-wide footer.
- Background `{colors.canvas}`, text `{colors.ink-mute}`, type `{typography.caption}`, padding `{spacing.huge} {spacing.xl}` (64px 24px). Holds 4 columns of link groups, social icons, and a small legal/copyright row.

## Do's and Don'ts

### Do
- Use an approved portrait only where the current page supports one; verify rights and text contrast for each crop.
- Render display tiers at sub-default weights (460 / 540) — the warmth is the typographic signature.
- Use rounded-rectangle CTAs for this historical body reference; the hero pill is an optional variant.
- Use the deep-teal CTA treatment only when supported by the current page design.
- Use warm dark grey `{colors.ink}` for body text — never pure black.
- Use the declared 1.15 line height for large portable display tokens; check the rendered result.

### Don't
- Don't use pill-shaped buttons in the body of the page; the pill is hero-only.
- Keep the two large display tokens at their declared 460/540 weights unless rendered evidence supports a change; body and button weights have separate roles.
- Don't render body text in pure black — the warm grey `#292827` is part of the brand.
- Check the current site before reusing the older Mail closing-band pattern.
- Don't introduce additional accent colors beyond indigo, violet-soft, teal, and the off-warm-greys.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Historical Mail composition; verify portrait and closing band against the current page |
| Desktop | 1024–1440px | Historical Mail layout; choose current suite pricing structure from the live page |
| Tablet | 768–1023px | Reflow actual plan cards and verify any permitted portrait crop |
| Mobile | < 768px | Stack actual plan cards; measure nav and display wrapping |

### Touch Targets
- Measure rendered button target sizes and spacing at each breakpoint; padding does not prove compliance.
- Measure rendered form targets and focus visibility in the running interface.

### Collapsing Strategy
- Display tiers stair-step 64 → 48 → 36 → 28 → 22px.
- Half-bleed portrait crops to head-and-shoulders on mobile; atmospheric backdrop simplifies.
- Reflow the actual current plan cards; do not infer the suite plan count from the older Mail layout.
- Top nav collapses to hamburger below 768px.
- Closing teal band reduces vertical padding from 128 → 64px on mobile.

### Image Behavior
If current permitted portrait imagery is available, provide responsive crops and verify alt text, focal point, text contrast, and rights at each breakpoint.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly.
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md`
    after edits.
4. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
5. Keep the three-canvas rhythm (indigo / white / teal) — adding a fourth canvas color breaks the system.
6. Use a closing teal band only when the current page and product flow support it.

## Known Gaps

- This historical Mail palette does not establish the current suite design, prices, product claims, or page routes. Verify them against official current pages.
- Portraits, logos, screenshots, and custom Super fonts require asset-specific rights checks before reuse.
- Inter loading, mixed-script wrapping, photo contrast, focus visibility, target size, and behavior in Claude Cowork or ChatGPT Work on macOS, Windows, and Linux have not been observed.
