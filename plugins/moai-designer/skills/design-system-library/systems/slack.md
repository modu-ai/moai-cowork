---
version: alpha
name: Slack-design-analysis
description: An inspired interpretation of Slack's design language, with aubergine surfaces, light hero gradients, blue links, and pill controls. Source display and UI faces remain references; portable tokens use OFL Inter and system fallbacks. Product mockups and brand assets require current source and rights checks before reuse.

colors:
  primary: "#4a154b"
  primary-deep: "#481a54"
  primary-press: "#611f69"
  primary-tint: "#592466"
  on-primary: "#ffffff"
  ink: "#1d1d1d"
  ink-mute: "#696969"
  link-blue: "#1264a3"
  link-hover: "#3860be"
  canvas: "#ffffff"
  canvas-cream: "#f4ede4"
  canvas-lavender: "#f9f0ff"
  surface-elev: "#ffffff"
  surface-aubergine: "#4a154b"
  hairline: "#e6e6e6"
  hairline-strong: "#000000"
  control-border-light: "#696969"
  control-border-dark: "#d9bdde"
  ring-focus: "#767676"
  semantic-error: "#cc4117"
  semantic-success: "#007a5a"
  on-aubergine-mute: "#d9bdde"

typography:
  display-xxl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.768px
  display-xl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 58px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.464px
  display-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.6px
  display-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.256px
  heading-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.096px
  heading-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  heading-sm:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: -0.0216px
  body-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: -0.0216px
  body-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-strong:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.16px
  button-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0
  button-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.2px
  button-cap:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.144px
  caption:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.1px
  micro-cap:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.96px

rounded:
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  xxl: 48px
  pill: 90px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  xxl: 24px
  huge: 28px

components:
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-primary-pill-focused:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    outline: "2px solid {colors.ring-focus}"
    outlineOffset: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-primary-pill-pressed:
    backgroundColor: "{colors.primary-press}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-secondary-pill:
    backgroundColor: "{colors.canvas-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 10px 30px
    border: "1px solid {colors.control-border-light}"
  button-outline-aubergine:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
    border: "2px solid {colors.primary}"
  button-outline-on-aubergine:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
    border: "2px solid {colors.on-primary}"
  button-outline-on-aubergine-focused:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    outline: "2px solid {colors.ring-focus}"
    outlineOffset: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
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
  pill-cap-shade:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  card-pricing:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-pricing-featured:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
    border: "1px solid {colors.control-border-dark}"
  card-feature-cream:
    backgroundColor: "{colors.canvas-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-aubergine-band:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.xl}"
    padding: 48px
  card-stat:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.xl}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.link-blue}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
    textDecoration: underline
  link-on-aubergine:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
    textDecoration: underline
  footer-aubergine:
    backgroundColor: "{colors.surface-aubergine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 32px 24px
---

## Overview

This Slack reference centers on a deep aubergine primary (`{colors.primary}`) for buttons, footer bands, and some pricing surfaces. Cream-lavender hero canvases and product UI mockups provide a lighter counterpoint. Confirm current mockups, logo treatment, and usage rights before publishing.

The source display and UI tiers use proprietary Salesforce families. Portable tokens use Inter for both tiers, with a system sans-serif fallback. Check loaded font coverage and line wrapping in the rendered interface.

Buttons are pill-shaped at 90px radius with an unusual amount of horizontal padding (28–30px), giving them a distinctly comfortable, almost over-padded feel. The primary aubergine pill is the only filled button in most contexts; secondary actions use a soft lavender pill (`{colors.canvas-lavender}`) which reads as a gentler echo of the primary surface. Inline links shift to a saturated blue (`{colors.link-blue}`) — the brand's only chromatic departure from the aubergine-and-cream world.

**Key Characteristics:**
- Aubergine primary (`{colors.primary}`) reused across CTAs and footer bands; use featured pricing treatment only when the current offer marks a tier.
- Cream-lavender hero canvas (`{colors.canvas-cream}` / `{colors.canvas-lavender}`) with diffused pastel-mesh atmospheric gradients and floating UI mockups composited above.
- Pill buttons at `{rounded.pill}` (90px radius) with generous 28–30px horizontal padding — over-padded by SaaS-default standards, deliberately so.
- Tight negative letter-spacing on display sizes (-0.768px on 64px hero) for editorial-density headlines.
- Blue inline links (`{colors.link-blue}`) — the only non-aubergine chromatic accent in body type.
- Pastel-mesh gradients and approved product UI assets may be paired in hero bands when current brand guidance supports them.
- Statistics cards use large aubergine display type on white; replace example numbers with verified current data before publication.

## Colors

> **Source reference:** home, features, pricing, and contact surfaces. Verify current URLs, content, and assets before reuse.

### Brand & Accent
- **Aubergine** (`{colors.primary}` — `#4a154b`): The primary surface and CTA color in this reference. Confirm current featured status and approved wordmark treatment separately.
- **Aubergine Deep** (`{colors.primary-deep}` — `#481a54`): A near-identical sibling of `{colors.primary}` extracted from a different surface; treat as functionally equivalent.
- **Aubergine Press** (`{colors.primary-press}` — `#611f69`): Pressed-state lift of the primary, slightly lighter and warmer.
- **Aubergine Tint** (`{colors.primary-tint}` — `#592466`): Border accent on aubergine-on-aubergine surfaces.
- **Link Blue** (`{colors.link-blue}` — `#1264a3`): Inline link color — saturated, slightly warm blue. The only chromatic alternative to aubergine in body type.
- **Link Hover** (`{colors.link-hover}` — `#3860be`): A more saturated blue used on link hover state.

### Surface
- **Canvas White** (`{colors.canvas}` — `#ffffff`): Default content surface.
- **Canvas Cream** (`{colors.canvas-cream}` — `#f4ede4`): Warm off-white used on hero gradients and feature bands. Adds editorial warmth.
- **Canvas Lavender** (`{colors.canvas-lavender}` — `#f9f0ff`): Pale lavender tint used as the secondary-button surface and as a soft section band.
- **Surface Aubergine** (`{colors.surface-aubergine}` — `#4a154b`): The primary aubergine reused for footer and dark feature bands, and for a featured pricing tier only when current official data supports one.
- **Hairline** (`{colors.hairline}` — `#e6e6e6`): decorative table divider only; important light-surface boundaries use `{colors.control-border-light}`.
- **Control Borders** (`{colors.control-border-light}` / `{colors.control-border-dark}`): visible boundaries on light and aubergine surfaces.

### Text
- **Ink** (`{colors.ink}` — `#1d1d1d`): Primary body text on light surfaces. Just shy of pure black.
- **Ink Mute** (`{colors.ink-mute}` — `#696969`): Secondary text, captions, helper copy.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): Text on aubergine surfaces and filled CTAs.
- **On Aubergine Mute** (`{colors.on-aubergine-mute}` — `#d9bdde`): Secondary text on aubergine surfaces — a desaturated mauve that reads as muted-light.

### Semantic
- **Error** (`{colors.semantic-error}` — `#cc4117`): Form error and destructive-action color.
- **Success** (`{colors.semantic-success}` — `#007a5a`): Inline success indicators.

## Typography

### Font Family

The source display tier uses proprietary Salesforce Avant Garde. Portable tokens use [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with `system-ui, sans-serif` fallback on macOS, Windows, and Linux.

The source UI tier uses proprietary Salesforce Sans. Portable body, caption, and button tokens use the same Inter stack.

Use either source face only after confirming the appropriate rights. Check mixed-script wrapping and fallback glyphs in each host.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 64px | 700 | 1.12 | -0.768px | Marketing hero headline |
| `{typography.display-xl}` | 58px | 600 | 1.25 | -0.464px | Section openers |
| `{typography.display-lg}` | 50px | 700 | 1.12 | -0.6px | Statistics callouts |
| `{typography.display-md}` | 32px | 700 | 1.25 | -0.256px | Card / feature titles |
| `{typography.heading-lg}` | 24px | 700 | 1.33 | -0.096px | Pricing tier names |
| `{typography.heading-md}` | 22px | 600 | 1.4 | 0 | Sub-section heading |
| `{typography.heading-sm}` | 18px | 600 | 1.56 | -0.0216px | Compact card title |
| `{typography.body-lg}` | 18px | 400 | 1.55 | -0.0216px | Marketing body lead |
| `{typography.body-md}` | 16px | 400 | 1.55 | 0 | Default UI body |
| `{typography.body-strong}` | 16px | 700 | 1.5 | 0.16px | Emphasized body |
| `{typography.button-lg}` | 18px | 700 | 1.0 | 0 | Hero pill button label |
| `{typography.button-md}` | 16px | 700 | 1.38 | 0.2px | Standard pill button label |
| `{typography.button-cap}` | 14.4px | 700 | 1.0 | 0.144px | Compact pill label |
| `{typography.caption}` | 14px | 400 | 1.43 | 0.1px | Helper, footnote |
| `{typography.micro-cap}` | 12px | 700 | 1.0 | 0.96px | All-caps eyebrow |

### Principles
- **Tight tracking on display.** The portable tokens retain negative tracking across 32–64px sizes; check for clipping at each breakpoint.
- **Body at 1.55 leading.** Slightly relaxed for marketing readability without crossing into airy / 1.7+ territory.
- **Caps for eyebrows.** All eyebrows render uppercase with positive 0.96–0.144px tracking depending on size.

### Note on Font Substitutes
The YAML uses Inter with a system fallback throughout. Keep its declared line height and tracking until rendered evidence supports adjustment; confirm font loading and glyph coverage rather than relying on an assumed visual match.

## Layout

### Spacing System
- **Base unit**: 8px (with 4 / 12 / 16 / 20 / 24 / 28 sub-tokens for fine vertical rhythm).
- **Tokens**: `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 20px · `{spacing.xxl}` 24px · `{spacing.huge}` 28px.
- **Section padding**: 64–96px on marketing surfaces; tightens to 48px on transactional pages.
- **Card internal padding**: 32px on pricing cards; 48px on aubergine band cards.

### Grid & Container
- Marketing pages center in a ~1240px container with edge-bleeding pastel-mesh gradients escaping the container.
- The reference pricing layout collapses from four to fewer columns at narrower widths. Source current plan names, prices, and any recommendation from [Slack's official pricing page](https://join.slack.com/pricing) before publication.
- Statistics row: 3-column grid with massive 50px aubergine display numerals.

### Whitespace Philosophy
The pastel-mesh gradients fill most of the negative space on marketing pages — sections feel expansive without being literally empty. On transactional pages the gradients drop, and whitespace reverts to traditional 48px-section breathing room.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default surface |
| 1 | `box-shadow: rgba(0,0,0,0.1) 0 5px 20px 0` | Floating buttons on hero |
| 2 | `box-shadow: rgba(0,0,0,0.1) 0 0 32px 0` | Product UI mockup composites |
| 3 | `box-shadow: rgba(0,0,0,0.2) 0 1px 10px 0` | Toast / notification chrome |
| 4 | `box-shadow: rgb(97,31,105) 0 0 0 1px inset` | Aubergine inset border (button focus, special chrome) |

### Decorative Depth
The brand's depth language is the **pastel-mesh gradient** — peach, lavender, dusty green stops blurred together at large radii to create soft atmospheric backdrops behind product UI screenshots. The gradient is the brand's flavor of "depth without shadows": the eye perceives the product mockup as floating above a luminous backdrop without any literal lift.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 2px | Hairline tags, status pills (rare) |
| `{rounded.sm}` | 4px | Form inputs |
| `{rounded.md}` | 8px | Compact card chrome, video frames |
| `{rounded.lg}` | 12px | Mid-size cards, secondary surface |
| `{rounded.xl}` | 16px | Pricing cards, feature cards |
| `{rounded.xxl}` | 48px | Stat badge backdrops |
| `{rounded.pill}` | 90px | All buttons |

### Photography Geometry
The brand uses **product UI screenshots** more than photography. UI mockups sit on top of pastel-mesh gradients at roughly 4:3 aspect, with no shadow but with the gradient providing the "lift" the eye expects. Real photography appears in customer-logo strips and the occasional case-study card, treated as full-bleed inside `{rounded.xl}` containers.

## Components

### Buttons

**`button-primary-pill`** — the dominant CTA system-wide.
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button-md}`, padding `14px 28px`, rounded `{rounded.pill}` 90px.
- Pressed state `button-primary-pill-pressed` shifts background to `{colors.primary-press}`.
- `{components.button-primary-pill-focused}` adds an offset `{colors.ring-focus}` outline; the dark-canvas outline button has its own focused variant.

**`button-secondary-pill`** — the soft lavender alternative.
- Background `{colors.canvas-lavender}`, text `{colors.ink}`, `{colors.control-border-light}` boundary, padding `10px 30px`, same pill geometry.

**`button-outline-aubergine`** — outline variant on white surfaces.
- Background `{colors.canvas}`, text `{colors.primary}`, 2px solid `{colors.primary}` border, same pill shape.

**`button-outline-on-aubergine`** — outline on aubergine canvas.
- Background `{colors.surface-aubergine}` (transparent over the surface), text `{colors.on-primary}`, 2px solid `{colors.on-primary}` border, same pill shape.

### Cards & Containers

**`card-pricing`** — standard pricing tier card.
- Background `{colors.canvas}`, padding 32px, rounded `{rounded.xl}` 16px, 1px `{colors.control-border-light}` border. Title in `{typography.heading-lg}`, current price in `{typography.display-md}`, body in `{typography.body-md}`.

**`card-pricing-featured`** — the inverted aubergine featured tier.
- Background `{colors.surface-aubergine}`, text `{colors.on-primary}`, with `{colors.control-border-dark}` boundary. Use only if the current official offer identifies a featured tier, and pair the fill with a text label.

**`card-feature-cream`** — feature explanation card on the cream track.
- Background `{colors.canvas-cream}`, text `{colors.ink}`, rounded `{rounded.xl}`, padding 32px.

**`card-aubergine-band`** — large horizontal band card with aubergine fill, often containing the closing CTA of a marketing page.
- Background `{colors.surface-aubergine}`, text `{colors.on-primary}`, padding 48px, rounded `{rounded.xl}` 16px.

**`card-stat`** — statistics callout card.
- Background `{colors.canvas}` with `{colors.control-border-light}` boundary; text `{colors.primary}` rendered in `{typography.display-lg}` (50px aubergine numeral). Use only verified current figures and captions.

### Inputs & Forms

**`text-input`** — standard form field.
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.body-md}`, padding `10px 12px`, rounded `{rounded.sm}` 4px, 1px `{colors.control-border-light}` border. `{components.text-input-focused}` adds a dark border and outline; verify keyboard focus in the rendered layout.

### Navigation

**`nav-bar-light`** — top nav across all marketing pages.
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.xxl}`. The reference layout has a wordmark left, navigation in the centre, and two pill actions right. Verify current labels and approved logo assets.

### Pills, Tags, and Chips

**`pill-cap-shade`** — small all-caps pill used as eyebrow above pricing-tier titles.
- Background `{colors.canvas-cream}`, text `{colors.ink}`, type `{typography.micro-cap}`, padding `4px 12px`, rounded `{rounded.pill}`.

### Signature Components

**Pastel-Mesh Gradient Backdrop** — peach (`#fff0e6`-ish) + lavender (`#e9d8ff`) + dusty green stops blurred together behind hero bands. Implemented as a CSS radial-gradient stack, not a single image. Provides the brand's depth/luminosity without literal shadows.

**Floating Product UI Mockup** — product screenshots framed in `{rounded.lg}` (12px) containers, positioned above the pastel-mesh gradient with no border or shadow. The gradient does the lifting.

**Aubergine Footer Band** — every marketing page closes with a full-bleed `card-aubergine-band` containing a closing CTA in white type. The band height is generous (~480–600px on desktop) and reads as the page's signature.

**`link-on-light`** — inline links in body copy on light surfaces.
- Text `{colors.link-blue}` rendered in `{typography.body-md}` with a persistent underline.

**`link-on-aubergine`** — links inside aubergine surfaces.
- Text `{colors.on-primary}` with persistent underline.

**`footer-aubergine`** — site-wide footer.
- Background `{colors.surface-aubergine}`, text `{colors.on-primary}` rendered in `{typography.caption}`, padding `{spacing.huge}+ {spacing.xxl}` (32px 24px). Holds 4–5 columns of `{colors.on-aubergine-mute}` link groups, social icons, and a small legal/copyright row at the bottom.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` aubergine for filled CTAs and closing bands; use it for a featured tier only when current official data marks that tier.
- Use `{rounded.pill}` (90px) for every button across the system — never a rounded-rectangle button.
- Pair display tiers with their declared negative letter-spacing (`-0.768px` at 64px); check Inter's rendered wrapping before adjusting it.
- Use the pastel-mesh gradient with product UI mockups only when current, approved assets are available under [Slack's media-kit guidance](https://join.slack.com/media-kit).
- Use `{colors.link-blue}` for inline links — it's the only chromatic departure from aubergine and is part of the brand voice.

### Don't
- Don't add a third accent color to the system — the aubergine + blue link combination is exhaustive.
- Don't shrink button padding below `14px 28px` — the over-padded pill is part of the brand feel.
- Don't render display tiers at default tracking (0) — without negative letter-spacing the headlines read loose and unedited.
- Don't put product UI screenshots inside cards — they sit ABOVE the pastel-mesh gradient, never inside chrome.
- Don't use aubergine for body text — it's a surface and CTA color, not a type color at body sizes.
- Don't replace the pill shape with a square button anywhere.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Full-bleed pastel-mesh hero; pricing 4-up |
| Desktop | 1024–1440px | Default content max-width; pricing 4-up |
| Tablet | 768–1023px | Pricing 2-up; product UI mockups crop to focal panel |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display-xxl drops 64 → 40px |

### Touch Targets
- Measure rendered button and input target sizes at each breakpoint; padding alone does not establish target-size compliance.
- Check focus visibility and keyboard operation in the running interface.

### Collapsing Strategy
- Display tiers stair-step 64 → 50 → 32 → 28 → 24 across breakpoints.
- Pastel-mesh gradients re-tile on mobile to prevent the wash from disappearing entirely.
- If approved product UI mockups are used, crop to the most legible relevant panel on mobile and verify the rendered result.
- The reference pricing tiers stair-step 4 → 2 → 1. If a current tier is marked featured, preserve its text label and visual treatment.
- Top nav collapses to hamburger below 768px; menu inherits canvas color.

### Image Behavior
Use responsive product mockups when current, approved assets exist. Verify the focal panel, legibility, alt text, and rights in each crop.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly (`{colors.primary}`, `{components.button-primary-pill-pressed}`, `{rounded.pill}`).
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md`
    after edits.
4. Add new variants as separate entries.
5. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
6. Keep aubergine scarce — one filled aubergine button per viewport.
7. Use the pastel-mesh hero treatment only when the current brand guidance and approved assets support it; verify the rendered crop and text contrast.

## Known Gaps

- Current Slack pricing, offers, recommendation labels, product screenshots, wordmark, and reuse rights require confirmation before publication.
- Inter loading and mixed-script wrapping, control and focus rendering, target sizes, and desktop behavior on macOS, Windows, and Linux have not been observed.
