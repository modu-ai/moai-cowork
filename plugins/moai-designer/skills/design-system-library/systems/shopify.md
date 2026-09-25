---
version: alpha
name: Shopify-design-analysis
description: An inspired interpretation of Shopify's design language with dark cinematic and light commerce surfaces. The source display uses Neue Haas Grotesk; portable tokens use OFL Inter with a system sans-serif fallback. Merchant photography, pricing, and brand assets require current source and rights checks before reuse.

colors:
  primary: "#000000"
  ink: "#000000"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  canvas-night: "#000000"
  canvas-night-elevated: "#0a0a0a"
  canvas-light: "#ffffff"
  canvas-cream: "#fbfbf5"
  surface-elevated-dark: "#1e2c31"
  shade-30: "#d4d4d8"
  shade-40: "#a1a1aa"
  shade-50: "#71717a"
  shade-60: "#52525b"
  shade-70: "#3f3f46"
  hairline-light: "#e4e4e7"
  hairline-dark: "#1e2c31"
  control-border-light: "#666666"
  control-border-dark: "#8c8c8c"
  aloe-10: "#c1fbd4"
  pistachio-10: "#d4f9e0"
  link-cool-1: "#9dabad"
  link-cool-2: "#9797a2"
  link-cool-3: "#bdbdca"
  link-mint: "#99b3ad"

typography:
  display-xxl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 96px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 2.4px
  display-xl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 70px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0
  display-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 55px
    fontWeight: 300
    lineHeight: 1.16
    letterSpacing: 0
  display-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.14
    letterSpacing: 0
  heading-xl:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0.42px
  heading-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.36px
  heading-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
  heading-sm:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.72px
  body-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-strong:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.49
    letterSpacing: 0.28px
  micro:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: -0.13px
  eyebrow-cap:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.72px
  code:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 5px
  md: 8px
  lg: 12px
  xl: 20px
  pill: 9999px

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
  button-primary-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-pill-pressed:
    backgroundColor: "{colors.shade-70}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-outline-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
  button-outline-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-aloe-pill:
    backgroundColor: "{colors.aloe-10}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 12px
    border: "1px solid {colors.control-border-light}"
  text-input-focused:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 10px 12px
    border: "2px solid {colors.ink}"
    outline: "2px solid {colors.ink}"
  card-pricing:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-pricing-featured:
    backgroundColor: "{colors.aloe-10}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-feature-cinematic:
    backgroundColor: "{colors.canvas-night-elevated}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-dark}"
  card-pistachio-band:
    backgroundColor: "{colors.pistachio-10}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
    border: "1px solid {colors.control-border-light}"
  card-photo-frame:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xl}"
    padding: 0px
  pill-tag-mint:
    backgroundColor: "{colors.aloe-10}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  pill-tag-shade:
    backgroundColor: "{colors.shade-30}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow-cap}"
    rounded: "{rounded.pill}"
    padding: 4px 12px
  nav-bar-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  nav-bar-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 16px 24px
  link-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
    textDecoration: underline
  footer-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
  footer-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 64px 24px
---

## Overview

This Shopify reference has two tracks that share pill controls but diverge in canvas polarity. The marketing track uses `{colors.canvas-night}` with merchant photography and large `{typography.display-xxl}` headlines. Its source display face is Neue Haas Grotesk Display; portable tokens use Inter 300 with a 1.15 line height. The outlined dark-canvas CTA is `{components.button-outline-on-dark}`. Check each actual photograph and layout before reuse.

The commerce track uses `{colors.canvas-light}` and `{colors.canvas-cream}` with the same pill controls. Aloe and pistachio accents stay on light surfaces. Source current plan labels, offers, and featured states from [Shopify's pricing page](https://www.shopify.com/pricing) before publishing.

The source display uses Neue Haas Grotesk Display. Portable display and UI tokens use OFL Inter with system sans-serif fallback; code uses the system monospace stack. The source `ss03` styling is not applied globally because fallback fonts do not share the same glyph features. Verify loaded fonts and mixed-script line breaks in a rendered page.

**Key Characteristics:**
- Two-canvas system: `{colors.canvas-night}` for cinematic marketing, `{colors.canvas-light}` / `{colors.canvas-cream}` for transactional surfaces — never blended.
- Pill-shape (`{rounded.pill}`) is the only button shape across both tracks; rounded rectangles do not exist for buttons.
- Thin display typography remains a reference; `{typography.display-xxl}` is 96px / weight 300 in the portable tokens.
- Aloe and pistachio greens (`{colors.aloe-10}`, `{colors.pistachio-10}`) are reserved for the light track — they signal commerce, growth, transactional success.
- Photography is full-bleed, edge-to-edge, never inset in cards on the cinematic track; merchants and storefront imagery do the heavy visual lifting that gradients and illustrations would do elsewhere.
- Treat source `ss03` styling as font-specific; do not enable it globally in the portable stack without checking glyphs.
- Tight letter-spacing on display sizes (2.4px positive tracking on 96px display) gives the thin weight extra optical air.

## Colors

> **Source reference:** marketing, website, and pricing surfaces. Verify current URLs, content, and assets before reuse.

### Brand & Accent
- **Aloe** (`{colors.aloe-10}` — `#c1fbd4`): a light-surface accent used for pill buttons and feature cards in this reference. Connect it to a featured tier only when the current official offer does so.
- **Pistachio** (`{colors.pistachio-10}` — `#d4f9e0`): Softer than aloe; used as a wide section band fill on the light track to signal a different category of feature without leaving the green family.
- **Cool Link Tones** (`{colors.link-cool-1}` `#9dabad`, `{colors.link-cool-2}` `#9797a2`, `{colors.link-cool-3}` `#bdbdca`, `{colors.link-mint}` `#99b3ad`): Muted footer / tertiary link colors used on dark surfaces to create a quiet hierarchy below the primary white type.

### Surface
- **Canvas Night** (`{colors.canvas-night}` — `#000000`): Pure black hero, cinematic feature pages, footer.
- **Canvas Night Elevated** (`{colors.canvas-night-elevated}` — `#0a0a0a`): Cards on cinematic surfaces, video frames.
- **Surface Elevated Dark** (`{colors.surface-elevated-dark}` — `#1e2c31`): Dark teal-shifted surface used on a small subset of dark cards to introduce subtle depth without breaking the black.
- **Canvas Light** (`{colors.canvas-light}` — `#ffffff`): Pricing, signup, comparison tables.
- **Canvas Cream** (`{colors.canvas-cream}` — `#fbfbf5`): Slightly warm off-white used on the pricing-page background canvas — invisibly different from `#ffffff` but adds editorial warmth.
- **Hairline Light** (`{colors.hairline-light}` — `#e4e4e7`): decorative light-surface divider only.
- **Hairline Dark** (`{colors.hairline-dark}` — `#1e2c31`): decorative dark-surface divider only.
- **Control Borders** (`{colors.control-border-light}` / `{colors.control-border-dark}`): visible boundaries on light and dark surfaces.

### Shade Ladder
- **Shade-30** (`{colors.shade-30}` — `#d4d4d8`): Tag / chip background on light, footer hairline on dark.
- **Shade-40** (`{colors.shade-40}` — `#a1a1aa`): secondary text on dark only; its white-surface contrast is too low for essential small text.
- **Shade-50** (`{colors.shade-50}` — `#71717a`): Secondary text on light.
- **Shade-60** (`{colors.shade-60}` — `#52525b`): Tertiary text on light, deep on dark.
- **Shade-70** (`{colors.shade-70}` — `#3f3f46`): Pressed-state of the primary pill button; deep dark surface accent.

### Text
- **Ink** (`{colors.ink}` — `#000000`): All text on light canvas.
- **On Primary** (`{colors.on-primary}` — `#ffffff`): All text on dark canvas + filled-pill labels.

## Typography

### Font Family

The source display tier uses Neue Haas Grotesk Display and requires separate use-rights confirmation. The portable tokens use [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) at weight 300 for large display sizes, with `system-ui, sans-serif` fallback on macOS, Windows, and Linux.

The UI tier also uses Inter, at 400 for regular body, 600 for strong text and leads, and 500 for captions. Check fallback weight rendering and glyph coverage in the actual host.

The code tier is **ui-monospace**, the system mono — preferred over a webfont mono to avoid unnecessary downloads.

The source's `ss03` setting is font-specific. The portable YAML does not set it; enable such a feature only for a verified font and specimen.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 96px | 300 | 1.15 | 2.4px | Cinematic hero headline |
| `{typography.display-xl}` | 70px | 300 | 1.15 | 0 | Section opener on cinematic pages |
| `{typography.display-lg}` | 55px | 300 | 1.16 | 0 | Pricing-page page title |
| `{typography.display-md}` | 48px | 300 | 1.14 | 0 | Sub-section headline on light track |
| `{typography.heading-xl}` | 28px | 500 | 1.28 | 0.42px | Card title / pricing tier name |
| `{typography.heading-lg}` | 24px | 400 | 1.14 | 0.36px | Compact card title |
| `{typography.heading-md}` | 20px | 500 | 1.4 | 0.3px | Section sub-heading |
| `{typography.heading-sm}` | 18px | 500 | 1.25 | 0.72px | Eyebrow / mini-section label |
| `{typography.body-lg}` | 18px | 600 | 1.56 | 0 | Marketing body lead, large body |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default UI body, pill-button labels |
| `{typography.body-strong}` | 16px | 600 | 1.5 | 0 | Emphasized body run |
| `{typography.caption}` | 14px | 500 | 1.49 | 0.28px | Helper copy, footnotes |
| `{typography.micro}` | 13px | 500 | 1.5 | -0.13px | Pricing fine print |
| `{typography.eyebrow-cap}` | 12px | 400 | 1.2 | 0.72px | All-caps eyebrow above large headlines |
| `{typography.code}` | 16px | 400 | 1.5 | 0 | Code blocks |

### Principles
- **Display thinness is the source cue.** The portable display tokens use Inter 300; check loaded font and wrapping before changing their weight.
- **Use Inter for portable display and body.** Keep Neue Haas Grotesk as a reference until rights are confirmed.
- **Tracking lifts on display.** The 96px hero gets +2.4px positive tracking — the thin glyphs need air. At 70px and below, tracking returns to 0.

### Note on Font Substitutes
Use the line heights and weights declared in YAML with Inter and its system fallback. Verify actual line breaks and contrast on both canvases rather than assuming source font metrics transfer.

## Layout

### Spacing System
- **Base unit**: 8px (with denser sub-units 1, 2, 3, 4 for fine work).
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 64px.
- **Section padding**: `{spacing.huge}` 64–128px on cinematic marketing pages (extreme negative space is the point); collapses to ~48px on transactional pages where density takes priority.
- **Card internal padding**: `{spacing.xxl}` 32px on pricing cards; `{spacing.xl}` 24px on compact tag rows.

### Grid & Container
- Cinematic hero pages use a wide max-width container (~1440–1600px) with edge-bleeding photography that escapes the container.
- Pricing collapses through 4-up → 2-up → 1-up tiers based on viewport.
- Body content centers in a ~720–840px reading column on long-form pages.

### Whitespace Philosophy
The cinematic track treats whitespace as the brand's most valuable asset — sections often have 128–192px of vertical air between content blocks, with photography filling the rest. The transactional track tightens to ~48–64px between bands because users are scanning, comparing, and acting. The contrast between the two whitespace philosophies is part of the brand voice.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat, no shadow | Default surface |
| 1 | `0 1px 2px rgba(255,255,255,0.05), inset 0 1px 0 rgba(255,255,255,0.04)` | Subtle inset highlight on dark cards (a top-edge sheen) |
| 2 | `0 0 0 1px rgba(255,255,255,0.08), 0 1px 3px rgba(0,0,0,0.3), 0 5px 10px rgba(0,0,0,0.2)` | Dark elevated cards with hairline + drop shadow stack |
| 3 | `0 8px 8px rgba(0,0,0,0.1), 0 4px 4px rgba(0,0,0,0.1), 0 2px 2px rgba(0,0,0,0.1), 0 0 0 1px rgba(0,0,0,0.1)` | Stacked-shadow card on light surfaces; layered tiny shadows produce a soft halo |
| 4 | `0 25px 50px -12px rgba(0,0,0,0.25)` | Modal / floating panel on light |

### Decorative Depth
On the cinematic track, depth comes from photography — full-bleed merchant imagery layered behind cards, with subtle inset top-edge highlights creating the illusion of light hitting a glass surface. On the light track, the layered tiny-shadow stack (Level 3) produces a soft, paper-like halo around pricing cards — depth without harshness.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Inputs, hairline tags |
| `{rounded.sm}` | 5px | Image containers (small) |
| `{rounded.md}` | 8px | Form inputs, video frames, smaller cards |
| `{rounded.lg}` | 12px | Pricing cards, feature cards |
| `{rounded.xl}` | 20px (top-only on some asymmetric cards) | Hero photo frames, cinematic card chrome |
| `{rounded.pill}` | 9999px | All buttons, pill tags, mint chips |

### Photography Geometry
Photography is full-bleed with no border. On cinematic pages it escapes the container entirely; on transactional pages it sits inside `{rounded.lg}` containers with no shadow. Avatar treatments in customer-logo strips are simple greyscale wordmarks at uniform height (~24–32px), aligned in a single horizontal strip.

## Components

### Buttons

**`button-primary-pill`** — the dominant CTA across the system.
- Background `{colors.primary}` (black), text `{colors.on-primary}`, type `{typography.body-md}`, padding `{spacing.md} {spacing.xl}` (12px 24px), rounded `{rounded.pill}` 9999px.
- Pressed state `button-primary-pill-pressed`: background lifts to `{colors.shade-70}`.

**`button-outline-on-dark`** — the cinematic hero CTA.
- Background `{colors.canvas-night}` (transparent on the canvas), 2px solid `{colors.on-primary}` border, text `{colors.on-primary}`, same pill geometry.

**`button-outline-on-light`** — the light-track equivalent.
- Background `{colors.canvas-light}`, 1px solid `{colors.ink}` border, text `{colors.ink}`, same pill geometry.

**`button-aloe-pill`** — an accent CTA on light pricing surfaces.
- Background `{colors.aloe-10}`, text `{colors.ink}`, same pill geometry. Use its wording and prominence only after checking the current offer.

### Cards & Containers

**`card-pricing`** — the standard tier card on the pricing page.
- Background `{colors.canvas-light}`, padding `{spacing.xxl}`, rounded `{rounded.lg}` 12px, 1px `{colors.control-border-light}` border. Title in `{typography.heading-xl}`, current price in `{typography.display-md}`, body in `{typography.body-md}`.

**`card-pricing-featured`** — the highlighted pricing tier.
- Background `{colors.aloe-10}` with `{colors.control-border-light}` border. Use only when the current official offer identifies a featured tier, with a text label as well as the fill.

**`card-feature-cinematic`** — feature card on the cinematic track.
- Background `{colors.canvas-night-elevated}`, text `{colors.on-primary}`, `{colors.control-border-dark}` boundary and `{rounded.lg}` corners. Holds full-bleed photography or a single large statement.

**`card-pistachio-band`** — wide horizontal band card used to highlight a category of features on the light track.
- Background `{colors.pistachio-10}`, text `{colors.ink}`, rounded `{rounded.lg}` 12px, padding `{spacing.xxl}`.

**`card-photo-frame`** — full-bleed photography container on cinematic pages.
- Background `{colors.canvas-night}`, padding 0, rounded `{rounded.xl}` 20px (often top-only). The photo IS the content; no inner padding, no overlay text inside the card.

### Inputs & Forms

**`text-input`** — standard text input on light surfaces.
- Background `{colors.canvas-light}`, text `{colors.ink}`, type `{typography.body-md}`, padding 10px 12px, rounded `{rounded.md}` 8px, 1px `{colors.control-border-light}` border. `{components.text-input-focused}` adds a dark border and outline; check actual keyboard focus rendering.

### Navigation

**`nav-bar-light`** — top nav on light pages.
- Background `{colors.canvas-light}`, text `{colors.ink}`, padding `{spacing.lg} {spacing.xl}`. The reference puts a wordmark left, navigation in the centre, and two pill actions right. Source current CTA wording from the official page before publication.

**`nav-bar-dark`** — top nav on cinematic pages.
- Background `{colors.canvas-night}`, text `{colors.on-primary}`, otherwise identical structure. Two pill buttons on the right (`button-outline-on-dark` for both, with the rightmost subtly more prominent via type weight).

### Pills, Tags, and Chips

**`pill-tag-mint`** — small tag on light surfaces, signaling a feature category.
- Background `{colors.aloe-10}`, text `{colors.ink}`, type `{typography.eyebrow-cap}`, padding `{spacing.xs} {spacing.md}`, rounded `{rounded.pill}`.

**`pill-tag-shade`** — neutral tag on light surfaces.
- Background `{colors.shade-30}`, text `{colors.ink}`, otherwise same shape as `pill-tag-mint`.

### Signature Components

**Cinematic Photography Layer** — full-bleed merchant photos on the hero. No overlay scrim, no text-on-image; instead, the type sits in clean negative space above or below the photo. The brand treats photography as an editorial spread, not as decoration.

**Stacked Tiny Shadows (Level 3 Elevation)** — pricing cards on the light track use 4 stacked tiny drop shadows (each 1–8px Y offset, 10% black) to produce a soft, layered paper halo. This is the brand's distinctive depth on light.

**`link-on-dark`** — inline link on cinematic pages.
- Color `{colors.on-primary}` with a persistent underline. Tertiary footer links may use the cool muted tones if each rendered pair keeps enough contrast.

**`footer-dark`** — full-page-width footer on the cinematic track.
- Background `{colors.canvas-night}`, text `{colors.on-primary}`, type `{typography.caption}`, padding `{spacing.huge} {spacing.xl}`. Contains 4–5 columns of muted-tone link groups, social icons, and a small legal row.

**`footer-light`** — equivalent on the transactional track.
- Background `{colors.canvas-light}`, text `{colors.ink}`, otherwise same structure.

## Do's and Don'ts

### Do
- Reserve `{colors.aloe-10}` and `{colors.pistachio-10}` for the light track only — they don't appear on cinematic black pages.
- Always use `{rounded.pill}` for buttons; never `{rounded.md}` or `{rounded.lg}`.
- Render the portable display tiers at Inter 300 and verify fallback line breaks.
- Use full-bleed photography on cinematic pages — let it escape the container.
- Keep the source's `ss03` treatment optional until glyph support is confirmed for the chosen loaded font.
- Pair black canvas with white type and white-stroked outline pills; pair light canvas with black type and filled-black pills.

### Don't
- Don't introduce a third canvas color — stick to black or light/cream. Greys, beiges, and blues are not in the system.
- Don't add drop shadows on cinematic dark cards beyond the subtle inset top-highlight; the cinematic track wants flat blackness.
- Don't shrink display tiers below `{typography.display-md}` (48px) on hero surfaces; below that they read as section heads, not display.
- Keep `{colors.ink}` text on aloe and pistachio fills; do not use the greens as text colors on white.
- Don't replace the pill shape with a rounded-rectangle button anywhere.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1440px | Full cinematic hero with edge-bleeding photography; pricing 4-up |
| Desktop | 1024–1440px | Default content max-width; pricing 4-up tightens |
| Tablet | 768–1023px | Pricing 2-up; cinematic hero photography crops |
| Mobile | < 768px | Pricing 1-up; hamburger nav; display-xxl drops to ~56–64px |

### Touch Targets
- Measure the rendered size and spacing of buttons and form fields at each breakpoint; padding alone does not establish target-size compliance.
- Check focus visibility and keyboard operation in the running interface.

### Collapsing Strategy
- Display sizes scale down through the breakpoint stair: 96 → 70 → 55 → 48 → 36px on mobile.
- Cinematic photography crops aggressively at smaller widths, prioritizing focal subject over edge-bleed.
- The reference pricing cards stair-step 4-up → 2-up → 1-up. If the current official offer marks a tier as featured, preserve both its text label and visual treatment at every breakpoint.
- Top nav collapses to hamburger below 768px; menu inherits canvas polarity.

### Image Behavior
Use responsive crops when approved merchant photos are available. Verify rights, alt text, focal subject, and any text contrast at each rendered breakpoint.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly (`{colors.aloe-10}`, `{components.button-primary-pill-pressed}`, `{rounded.pill}`).
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md`
    after edits.
4. Add new variants as separate entries.
5. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
6. Keep the two canvas tracks separated — when designing a new page, choose cinematic OR transactional, not both.
7. The pill shape is non-negotiable; new button variants vary in fill / border / canvas, never in shape.

## Known Gaps

- Current Shopify prices, plan promotions, featured labels, merchant images, logos, and reuse rights require confirmation from current official sources before publication.
- Inter loading and mixed-script wrapping, control and focus rendering, target sizes, and desktop behavior on macOS, Windows, and Linux have not been observed.
