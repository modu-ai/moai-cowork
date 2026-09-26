---
version: alpha
name: Spacex-design-analysis
description: >-
  An inspired interpretation of SpaceX's black-and-white marketing design. D-DIN remains a source-font reference; portable display and body tokens use OFL Barlow Condensed and Inter with system fallbacks. Photographs, video, logo, launch details, and their usage rights require current verification before reuse.

colors:
  primary: "#000000"
  ink: "#000000"
  on-primary: "#ffffff"
  on-primary-mute: "#f0f0fa"
  canvas-night: "#000000"
  canvas-night-soft: "#0a0a0a"
  canvas-light: "#ffffff"
  canvas-cool: "#f0f0fa"
  hairline-on-dark: "#3a3a3f"
  hairline-on-light: "#e0e0e8"
  control-border-light: "#767676"
  control-border-dark: "#8c8c8c"
  link-on-dark: "#ffffff"
  link-blue-fallback: "#0000ee"
  ink-mute: "#5a5a5f"

typography:
  display-xxl:
    fontFamily: "Barlow Condensed, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 1.6px
  display-xl:
    fontFamily: "Barlow Condensed, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
  display-lg:
    fontFamily: "Barlow Condensed, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.96px
  body-lg:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0.32px
  body-md:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.32px
  button-cap:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 13.008px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.17px
  micro-cap:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 2.0
    letterSpacing: 0.96px
  caption:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 13.008px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 8px
  md: 16px
  pill: 32px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 18px
  xl: 24px
  xxl: 32px
  huge: 48px

components:
  button-ghost-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-cap}"
    rounded: "{rounded.pill}"
    padding: 18px 24px
    border: "1px solid {colors.on-primary}"
  button-ghost-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-cap}"
    rounded: "{rounded.pill}"
    padding: 18px 24px
    border: "1px solid {colors.ink}"
  button-filled-cool:
    backgroundColor: "{colors.canvas-cool}"
    textColor: "{colors.ink}"
    typography: "{typography.button-cap}"
    rounded: "{rounded.pill}"
    padding: 18px 24px
    border: "1px solid {colors.control-border-light}"
  text-input:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.control-border-light}"
  text-input-focused:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "2px solid {colors.ink}"
    outline: "2px solid {colors.ink}"
  card-photo-band:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
  card-shop-product:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.control-border-light}"
  nav-bar-overlay:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-cap}"
    rounded: "{rounded.xs}"
    padding: 24px 32px
  link-on-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.link-on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
    textDecoration: underline
  link-on-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 0px
    textDecoration: underline
  footer-dark:
    backgroundColor: "{colors.canvas-night}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 32px 24px
---

## Overview

This SpaceX reference uses a black canvas, uppercase white display type, and full-bleed rocket imagery. The source display face is D-DIN; portable tokens use Barlow Condensed 700 at 80px with a 1.15 line height. Use current, permitted imagery and verify each band in the rendered layout rather than assuming every band is a full-viewport photo or video.

Depth comes from photography in this reference. Text over an image needs a contrast check for every crop; use a dark scrim, a solid text panel, or a different placement if the image alone cannot keep the text legible. `{colors.canvas-night-soft}` is available for a solid panel, with `{colors.control-border-dark}` for any boundary users need to see.

Source typography uses D-DIN display and regular cuts. Portable tokens use Barlow Condensed for display and Inter for body and controls. The largest display token uses 1.15 leading and 1.6px positive tracking; check mixed-script wrapping after font loading.

**Key Characteristics:**
- Single canvas: pure `{colors.canvas-night}` (`#000000`) for marketing; `{colors.canvas-light}` only on the shop site.
- Portable display tier in uppercase Barlow Condensed with positive horizontal tracking (1.6px at 80px); D-DIN remains a source reference.
- Full-bleed photography or video as a reference treatment, with text contrast verified for each asset and crop.
- Single ghost-outlined pill CTA per band, at `{rounded.pill}` 32px radius — never filled, never accent-colored.
- All-caps eyebrow microtext (`{typography.micro-cap}` and `{typography.button-cap}`) with positive 0.96–1.17px tracking — every chrome element shouts in caps.
- The YAML uses an opaque black top nav for reliable white-text contrast.
- The portable 80px display uses 1.15 line height; check actual line breaks before tightening it.

## Colors

> **Source reference:** marketing, vehicle, human spaceflight, and shop surfaces. Verify current URLs, missions, products, and assets before reuse.

### Brand & Accent
The brand has no accent colors. Black and white do all the chromatic work; photography supplies every other hue.

### Surface
- **Canvas Night** (`{colors.canvas-night}` — `#000000`): Default marketing canvas. Pure black, no tint.
- **Canvas Night Soft** (`{colors.canvas-night-soft}` — `#0a0a0a`): Barely-lifted near-black for content sections that need a subtle separation from the pure-black hero.
- **Canvas Light** (`{colors.canvas-light}` — `#ffffff`): The shop site's product surface.
- **Canvas Cool** (`{colors.canvas-cool}` — `#f0f0fa`): A pale cool-blue-white used as the secondary surface on the shop site and as the hover-canvas of certain ghost buttons.
- **Hairline on Dark** (`{colors.hairline-on-dark}` — `#3a3a3f`): decorative dark-surface divider only.
- **Hairline on Light** (`{colors.hairline-on-light}` — `#e0e0e8`): decorative light-surface divider only.
- **Control Borders** (`{colors.control-border-light}` / `{colors.control-border-dark}`): visible boundaries for light and dark components.

### Text
- **On Primary** (`{colors.on-primary}` — `#ffffff`): Default text on dark canvas; the dominant text color across the marketing site.
- **On Primary Mute** (`{colors.on-primary-mute}` — `#f0f0fa`): Slightly cooled-white used for secondary text on dark surfaces — barely distinguishable from `{colors.on-primary}` but enough to suggest a hierarchy.
- **Ink** (`{colors.ink}` — `#000000`): Default text on light surfaces (shop site).
- **Ink Mute** (`{colors.ink-mute}` — `#5a5a5f`): Secondary text on light surfaces.

### Link
- **Link on Dark** (`{colors.link-on-dark}` — `#ffffff`): Underlined inline link on dark canvas.
- **Link Blue Fallback** (`{colors.link-blue-fallback}` — `#0000ee`): The browser default that appears in unstyled fallback contexts — documented for completeness, not used as a brand color.

## Typography

### Font Family

The source display tier uses D-DIN-Bold. The portable tokens use [OFL Barlow Condensed](https://github.com/google/fonts/blob/main/ofl/barlowcondensed/METADATA.pb) with `system-ui, sans-serif` fallback. Use the source face only after confirming its rights.

The portable body, button, and caption tokens use [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with a system sans-serif fallback.

D-DIN distribution and use rights are not established by this profile. Verify the loaded Barlow Condensed and Inter faces, glyph coverage, and line breaks across desktop systems.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 80px | 700 | 1.15 | 1.6px | Hero headline (uppercase) |
| `{typography.display-xl}` | 60px | 700 | 1.2 | 1.2px | Section opener (uppercase) |
| `{typography.display-lg}` | 48px | 700 | 1.25 | 0.96px | Sub-section heading (uppercase) |
| `{typography.body-lg}` | 16px | 400 | 1.7 | 0.32px | Marketing body lead |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0.32px | Default UI body |
| `{typography.button-cap}` | 13.008px | 700 | 1.3 | 1.17px | All-caps button label |
| `{typography.micro-cap}` | 12px | 400 | 2.0 | 0.96px | All-caps eyebrow / nav item |
| `{typography.caption}` | 13.008px | 400 | 1.5 | 0 | Helper / footer text |

### Principles
- **Uppercase across display.** Every display tier renders in uppercase. The brand never uses sentence-case display headlines.
- **Display leading.** The portable 80px token uses 1.15 and the 60px token 1.2; check rendered wrapping at each breakpoint.
- **Wide horizontal tracking.** Positive 0.96–1.6px tracking on display sizes; positive 0.96–1.17px on caps eyebrows. The wide tracking is the brand's signature optical air.
- **No mono.** Code blocks are not part of the brand's typographic system.

### Note on Font Substitutes
The YAML already uses Barlow Condensed for display and Inter for body. Keep its declared weights, tracking, and line heights until rendered evidence supports adjustment.

## Layout

### Spacing System
- **Base unit**: 8px (with denser sub-units 4 / 12 / 16 / 18 / 24).
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 18px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.huge}` 48px.
- **Section padding**: For a full-bleed marketing band, set enough space for its actual text and CTA; shop sections can use 48–64px vertical padding as a starting point.

### Grid & Container
- A full-bleed marketing band can span the viewport width. Set its height and crop from the actual content and available screen space.
- Shop product grid: 4-up at desktop, 2-up at tablet, 1-up at mobile.
- Overlaid type can sit in an inner reading column up to about 1200px wide; adjust placement and contrast for each image.

### Whitespace Philosophy
This reference often uses open space within photography. Preserve room around the actual text and controls instead of relying on an image crop to supply it. Shop layouts can start with 32px grid gutters.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | Flat | Default — and the only level on marketing surfaces |
| 1 | Photographic — full-bleed image or video | The primary depth medium; photographs do all the lifting |

This reference relies on photography for depth. Use an overlay or solid panel when an actual image crop needs one to keep text legible; verify contrast rather than relying on its color grade.

### Decorative Depth
Photography and video provide decorative depth in the reference. If video autoplays, provide a pause control and respect reduced-motion preferences in the running interface.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Form inputs (shop site) |
| `{rounded.sm}` | 8px | Shop product card chrome, video frames |
| `{rounded.md}` | 16px | Larger surface chrome |
| `{rounded.pill}` | 32px | Ghost outlined pill CTAs (the brand's signature button shape) |
| `{rounded.full}` | 9999px | Circular play-button overlays on video frames |

### Photography Geometry
Marketing photography may be full-bleed where the asset and content support it; choose height and crop for each breakpoint. Shop product photography can sit inside `{rounded.sm}` 8px containers without a shadow. No single aspect ratio is required for marketing images.

## Components

### Buttons

**`button-ghost-on-dark`** — the universal CTA on marketing surfaces.
- Opaque `{colors.canvas-night}` background for reliable contrast, 1px `{colors.on-primary}` border, white text, `{typography.button-cap}` type, 18px 24px padding, `{rounded.pill}` corners.

**`button-ghost-on-light`** — the same button on shop / light pages.
- Background `{colors.canvas-light}`, 1px `{colors.ink}` border, dark text, otherwise identical.

**`button-filled-cool`** — fill variant on shop product cards.
- Background `{colors.canvas-cool}`, text `{colors.ink}`, same pill geometry. Used as "Add to cart" or similar product CTAs.

### Cards & Containers

**`card-photo-band`** — full-bleed photographic band on marketing pages.
- Background `{colors.canvas-night}`, padding 0, rounded `{rounded.xs}`. The photograph fills the entire band; type and CTA sit overlaid.

**`card-shop-product`** — product card on the shop site.
- Background `{colors.canvas-light}`, padding `{spacing.md}` 16px, rounded `{rounded.sm}` 8px, 1px `{colors.control-border-light}` border. Populate product photo, name, price, and CTA from current authorized data.

### Inputs & Forms

**`text-input`** — form input on the shop site.
- Background `{colors.canvas-light}`, text `{colors.ink}`, type `{typography.body-md}`, padding 12px 16px, rounded `{rounded.xs}` 4px, 1px `{colors.control-border-light}` border. `{components.text-input-focused}` adds a dark border and outline; verify keyboard focus in the rendered page.

### Navigation

**`nav-bar-overlay`** — top nav across the marketing site.
- Opaque `{colors.canvas-night}` background and white text preserve contrast independently of the hero image. Confirm current logo, navigation labels, and fixed or sticky behavior in the running page.

### Signature Components

**Full-Bleed Photo / Video Hero** — a reference treatment. Use only current permitted media, check each crop's text contrast, and add a scrim or solid panel when needed. Autoplaying video requires a pause control and reduced-motion handling.

**Uppercase Display Headline** — the source D-DIN reference is represented by the portable 80px Barlow Condensed 700 token with 1.6px positive tracking. Check glyphs and wrapping after font load.

**`link-on-dark`** — inline links on dark canvas.
- Text `{colors.link-on-dark}` (white) with persistent underline.

**`link-on-light`** — inline links on light canvas.
- Text `{colors.ink}` with persistent underline.

**`footer-dark`** — site-wide footer.
- Background `{colors.canvas-night}`, text `{colors.on-primary}`, type `{typography.caption}`, padding `{spacing.xxl} {spacing.xl}` (32px 24px). Holds nav columns in `{typography.micro-cap}` (uppercase), and a small legal/copyright row at the bottom.

## Do's and Don'ts

### Do
- Use approved full-bleed media where appropriate and verify every text-overlay crop.
- Render portable display tiers in uppercase Barlow Condensed with the declared positive tracking; check mixed-script rendering.
- Use `{components.button-ghost-on-dark}` for the reference marketing CTA treatment.
- Use a scrim or solid panel when the actual photograph cannot keep text legible.
- Keep the opaque black nav in the portable tokens so white links remain legible over changing imagery.

### Don't
- Don't introduce brand accent colors — black, white, and photography are the entire palette.
- Avoid decorative shadows; add a contrast overlay when actual imagery needs it for legibility.
- Don't render display tiers in sentence-case or title-case — uppercase is the brand.
- Don't put filled buttons on marketing surfaces — the ghost outlined pill is the only marketing CTA.
- Keep the Barlow Condensed and Inter portable stacks unless a source face is licensed and the rendered result is verified.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Wide | ≥ 1500px | Full hero photograph; max-content type column at 1200px |
| Desktop | 1280–1499px | Default desktop layout |
| Laptop | 961–1279px | Type column tightens; photo crops adjust |
| Tablet | 768–960px | Display drops 80 → 60px; nav compresses |
| Mobile | 600–767px | Display drops to 48px; ghost button retains pill shape |
| Small Mobile | < 600px | Display drops to 40px; nav becomes hamburger |

### Touch Targets
- Measure rendered button and input targets at each breakpoint; padding alone does not establish target-size compliance.
- Verify focus visibility and keyboard operation in the running interface.

### Collapsing Strategy
- Display sizes stair-step 80 → 60 → 48 → 40px through the breakpoints.
- Photography re-crops to focal subject on smaller widths (rocket centered, Mars landscape centered).
- Top nav collapses to hamburger below 768px; menu retains the dark overlay treatment.
- Shop product grid stair-steps 4-up → 2-up → 1-up.

### Image Behavior
Use responsive crops when current permitted marketing imagery is available. Verify rights, alt text, focal point, and text contrast at every breakpoint.

## Iteration Guide

1. Focus on ONE component at a time.
2. Reference component names and tokens directly (`{colors.canvas-night}`, `{components.button-ghost-on-dark}`, `{rounded.pill}`).
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md`
    after edits.
4. Add new variants as separate entries.
5. Default body to `{typography.body-md}`; reserve `{typography.body-lg}` for marketing leads.
6. The black-and-white-only rule is load-bearing — adding a brand accent color breaks the system.
7. Ghost pill is the only marketing CTA; filled buttons live exclusively on the shop site.

## Known Gaps

- Current mission details, products, imagery, video, logo, and reuse rights require confirmation from current official sources before publication.
- Barlow Condensed and Inter loading, mixed-script wrapping, photo and video text contrast, video controls, focus and target sizes, and desktop behavior on macOS, Windows, and Linux have not been observed.
