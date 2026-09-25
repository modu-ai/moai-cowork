---
version: alpha
name: Replicate-design-analysis
description: |
  Replicate's marketing surfaces pair the warm-cream developer-tools aesthetic
  of an indie ML playground with a confident hot-orange brand accent and a
  signature display typeface (rb-freigeist-neue) sized aggressively large at
  72px+. The system reads as "AI lab notebook crossed with print magazine":
  cream and bone surfaces, dark ink type, monospace code wells, irregular
  hand-drawn-feeling diagrams, and a rich orange used scarcely on the most
  consequential CTA. Photography of contributors and example outputs is
  square-ish with mid-radius corners; everything else is borderless or hairline.

colors:
  primary: "#dc2503"
  primary-deep: "#c01f00"
  on-primary: "#ffffff"
  ink: "#202020"
  body: "#3a3a3a"
  charcoal: "#575757"
  mute: "#646464"
  ash: "#8d8d8d"
  stone: "#bbbbbb"
  on-dark: "#fcfcfc"
  on-dark-mute: "rgba(252,252,252,0.72)"
  canvas: "#f9f7f3"
  surface-bone: "#f3f0e8"
  surface-card: "#ffffff"
  surface-dark: "#202020"
  surface-deep: "#000000"
  hairline: "rgba(32,32,32,0.12)"
  hairline-strong: "#202020"
  control-border: "#8a8a8a"
  divider-dark: "rgba(255,255,255,0.2)"
  hero-warm: "#dc2503"
  hero-glow: "#ff6a3d"
  hero-pink: "#f4a8a0"
  badge-success: "#20774d"
  link: "#d02000"
  ring-focus: "#202020"
  ring-focus-dark: "#fcfcfc"
  github-dark: "#24292e"

typography:
  display-xxl:
    fontFamily: Bricolage Grotesque, system-ui, sans-serif
    fontSize: 128px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -3px
  display-xl:
    fontFamily: Bricolage Grotesque, system-ui, sans-serif
    fontSize: 72px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1.8px
  display-lg:
    fontFamily: Bricolage Grotesque, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1px
  display-md:
    fontFamily: Bricolage Grotesque, system-ui, sans-serif
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  heading-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 38.4px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  heading-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.35px
  heading-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.3px
  subtitle:
    fontFamily: Bricolage Grotesque, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0
  body-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0
  button-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0
  caption:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-tight:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: -0.35px
  code-md:
    fontFamily: JetBrains Mono, ui-monospace, Consolas, monospace
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  code-sm:
    fontFamily: JetBrains Mono, ui-monospace, Consolas, monospace
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 10px
  lg: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  xxxl: 48px
  section: 96px
  band: 160px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-primary-pressed:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-outline:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  button-icon:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.control-border}"
    rounded: "{rounded.full}"
    size: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.control-border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  text-input-focused:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.hairline-strong}"
    outline: "2px solid {colors.ring-focus}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  hero-band:
    backgroundColor: "{colors.hero-warm}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 96px 32px
  model-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.control-border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 16px
  collection-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.control-border}"
    typography: "{typography.heading-md}"
    rounded: "{rounded.md}"
    padding: 24px
  pricing-tier:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.control-border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  pricing-tier-featured:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  code-block:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.code-md}"
    rounded: "{rounded.md}"
    padding: 24px
  code-tab:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark-mute}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  code-tab-active:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    borderBottom: "2px solid {colors.primary}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  code-tab-focused:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    outline: "2px solid {colors.ring-focus-dark}"
    typography: "{typography.code-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  badge-status:
    backgroundColor: "{colors.badge-success}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.control-border}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 60px
  sub-nav-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  contributor-avatar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 40px
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 64px 32px
  link-inline:
    textColor: "{colors.link}"
    textDecoration: underline
    typography: "{typography.body-md}"
  link-inline-dark:
    textColor: "{colors.on-dark}"
    textDecoration: underline
    typography: "{typography.body-md}"
---

## Overview

Replicate is a developer-tools platform with the soul of an art zine. The
public marketing surfaces sit on a warm cream canvas (`{colors.canvas}` —
`#f9f7f3`) rather than the white-or-near-black default of typical AI
infrastructure sites, and that single decision colours everything else:
photography reads as editorial, code wells read as printed pull-quotes, and
the brand orange (`{colors.primary}` — `#dc2503`) feels like a stamp rather
than a notification.

The source design uses **rb-freigeist-neue** for display and **basier-square** for interface text. The portable tokens use **Bricolage Grotesque** for display, **Inter** for interface text, and **JetBrains Mono** for code, each with operating-system fallbacks. Display line height is 1.15 to protect mixed-script headlines; check actual wrapping in the rendered interface.

Page rhythm cycles between a default cream canvas, a bold full-bleed orange
hero band, and a `{colors.surface-dark}` (`#202020`) section that hosts the
code stories — the "how it works" walkthrough. Curves are intentional and
soft: every interactive surface (buttons, inputs, tags, avatars) uses
`{rounded.full}`, while content cards and code wells step up to `{rounded.md}`
or `{rounded.lg}`. There are no sharp corners on Replicate; the system reads
as friendly precision.

**Key Characteristics:**
- A warm cream canvas (`{colors.canvas}` — `#f9f7f3`) replaces the typical white background, paired with `{colors.surface-bone}` for inset cards.
- Hot orange (`{colors.primary}` — `#dc2503`) is reserved for the primary CTA, the hero band, and inline link colour. Never decorative.
- Display headlines run massive — `{typography.display-xxl}` at 128px in hero bands and `{typography.display-xl}` at 72px on section openers — with tight `lineHeight: 1.15` and negative letter-spacing.
- Portable three-family typography stack: Bricolage Grotesque for display, Inter for UI/body, JetBrains Mono for code.
- Every interactive element is fully rounded (`{rounded.full}` 9999px) — buttons, inputs, badges, avatars — while content cards step to `{rounded.md}` 10px.
- Dark code wells (`{colors.surface-dark}` background) sit inside the cream canvas as full-bleed reading surfaces, mimicking print pull-quotes.
- Section rhythm: cream → orange hero → cream → dark code-story band → cream → black footer.

## Colors

### Brand & Accent
- **Replicate Orange** (`{colors.primary}` — `#dc2503`): the brand accent. Reserved for the primary CTA, hero band background, and inline link colour. Treat as a stamp — one orange element per viewport at most.
- **Orange Pressed** (`{colors.primary-deep}` — `#c01f00`): the active/pressed state of `{colors.primary}` — used on `{components.button-primary-pressed}`.
- **Hero Glow** (`{colors.hero-glow}` — `#ff6a3d`): the lighter orange that appears in the radial atmospheric mesh behind the hero copy.
- **Hero Pink** (`{colors.hero-pink}` — `#f4a8a0`): a warm pink wash that softens the bottom edge of the hero band before it transitions to cream.
- **On-Primary** (`{colors.on-primary}` — `#ffffff`): label colour on top of `{colors.primary}` surfaces.

### Surface
- **Canvas** (`{colors.canvas}` — `#f9f7f3`): the default page background. Warm cream, never pure white.
- **Surface Bone** (`{colors.surface-bone}` — `#f3f0e8`): a half-step deeper cream used for inset card groups and feature bands.
- **Surface Card** (`{colors.surface-card}` — `#ffffff`): pure white for individual model cards, search inputs, and pricing tiers — the only place white appears.
- **Surface Dark** (`{colors.surface-dark}` — `#202020`): code wells, featured pricing tier, and the "how it works" walkthrough band.
- **Surface Deep** (`{colors.surface-deep}` — `#000000`): footer canvas and the inset code-tab strip inside `{components.code-block}`.
- **Hairline** (`{colors.hairline}` — `rgba(32,32,32,0.12)`): decorative dividers on cream surfaces only.
- **Hairline Strong** (`{colors.hairline-strong}` — `#202020`): button outlines, focused inputs, and structural separators.
- **Control Border** (`{colors.control-border}` — `#8a8a8a`): visible boundaries for inputs, cards, tags, and icon buttons.

### Text
- **Ink** (`{colors.ink}` — `#202020`): primary text colour. Notably warmer than `#000000`, matching the cream canvas.
- **Body** (`{colors.body}` — `#3a3a3a`): long-form body copy where ink would feel too heavy at 18px+ line lengths.
- **Charcoal** (`{colors.charcoal}` — `#575757`): captions, metadata, secondary nav.
- **Mute** (`{colors.mute}` — `#646464`): supporting text and inactive labels.
- **Ash** (`{colors.ash}` — `#8d8d8d`): disabled text only, never essential placeholder copy.
- **Stone** (`{colors.stone}` — `#bbbbbb`): decorative disabled foreground and neutral icon outlines only.
- **On-Dark** (`{colors.on-dark}` — `#fcfcfc`): primary text on `{colors.surface-dark}` and `{colors.surface-deep}`.
- **On-Dark Mute** (`{colors.on-dark-mute}` — `rgba(252,252,252,0.72)`): secondary text in dark regions; preserves the off-white feel without pure white pop.

### Semantic
- **Success** (`{colors.badge-success}` — `#20774d`): inline success badges and "running" status pills on model cards.
- **Link** (`{colors.link}` — `#d02000`): underlined inline link colour on canvas, bone, and white surfaces.
- **Focus Ring** (`{colors.ring-focus}` — `#202020`): visible input focus outline on light surfaces.
- **Dark Focus Ring** (`{colors.ring-focus-dark}` — `#fcfcfc`): visible focus outline on dark code surfaces.
- **GitHub Dark** (`{colors.github-dark}` — `#24292e`): the GitHub-branded button surface (kept off-brand-on-purpose to match GitHub's own tokens).

## Typography

### Font Family

The source design uses proprietary rb-freigeist-neue and basier-square. The portable tokens use [OFL Bricolage Grotesque](https://github.com/google/fonts/blob/main/ofl/bricolagegrotesque/METADATA.pb) for display, [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) for body and controls, and [OFL JetBrains Mono](https://github.com/google/fonts/blob/main/ofl/jetbrainsmono/METADATA.pb) for code. Load these fonts explicitly when available; their stacks fall back to system fonts across macOS, Windows, and Linux. Use the proprietary source faces only after rights are confirmed.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xxl}` | 128px | 700 | 1.15 | -3px | The single hero "Run AI" / "Imagine what you can build" headline. One per page. |
| `{typography.display-xl}` | 72px | 700 | 1.15 | -1.8px | Section openers ("How it works", "Scale on Replicate"). |
| `{typography.display-lg}` | 48px | 700 | 1.15 | -1px | Sub-section titles, pricing tier names. |
| `{typography.display-md}` | 30px | 600 | 1.2 | -0.5px | Feature card titles. |
| `{typography.heading-lg}` | 38.4px | 600 | 1.15 | -0.5px | Display headlines, used in pricing and enterprise hero. |
| `{typography.heading-md}` | 24px | 600 | 1.33 | -0.35px | Card titles, model detail headers. |
| `{typography.heading-sm}` | 20px | 600 | 1.4 | -0.3px | List section headers. |
| `{typography.subtitle}` | 18px | 600 | 1.56 | 0 | Lead paragraphs in display sections. |
| `{typography.body-lg}` | 18px | 400 | 1.56 | 0 | Marketing prose. |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body. |
| `{typography.body-sm}` | 14px | 400 | 1.43 | 0 | Captions, metadata. |
| `{typography.button-md}` | 16px | 600 | 1.15 | 0 | Default button label. |
| `{typography.button-sm}` | 14px | 600 | 1.15 | 0 | Compact button label, sub-nav pills. |
| `{typography.caption}` | 12px | 400 | 1.33 | 0 | Footer disclosure, copyright. |
| `{typography.caption-tight}` | 14px | 600 | 1.43 | -0.35px | Emphatic small caption used in pricing tier rows. |
| `{typography.code-md}` | 14px | 400 | 1.43 | 0 | Code blocks and inline code. |
| `{typography.code-sm}` | 11px | 400 | 1.5 | 0 | Code-tab labels and small inline tokens. |

### Principles
- Display and large heading tokens use `lineHeight: 1.15`; test multi-line and mixed-script text for clipping.
- Negative letter-spacing scales with size — bigger types tighten more (-3px at 128px down to -0.3px at 20px). Body type stays at 0.
- Body weight sits at 400 across `{typography.body-lg}` and `{typography.body-md}`; larger display type uses the Bricolage stack.
- Code uses the JetBrains Mono stack for literal commands, model slugs, and API calls.

### Note on Font Substitutes

Check loaded font coverage and line breaks before adjusting display tracking. The YAML uses an explicit 1.15 line height and platform fallbacks rather than forcing the source font's tight metrics.

## Layout

### Spacing System
- **Base unit**: 4px, with the working scale on multiples of 4 / 8 / 16.
- **Tokens**: `{spacing.xxs}` 2px · `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 12px · `{spacing.lg}` 16px · `{spacing.xl}` 24px · `{spacing.xxl}` 32px · `{spacing.xxxl}` 48px · `{spacing.section}` 96px · `{spacing.band}` 160px.
- Section padding: `{spacing.section}` (96px) vertical between full-width bands; `{spacing.band}` (160px) when a band needs extra editorial breathing room (the hero, the closing "Imagine what you can build" stripe).
- Card internal padding: `{spacing.lg}` (16px) on `{components.model-card}`, `{spacing.xxl}` (32px) on `{components.pricing-tier}`.

### Grid & Container
- **Max content width** ≈ 1280px on body sections, 1440px on hero bands which run full-bleed.
- **Model grid** on collections: 4 columns at desktop, 3 at tablet large, 2 at tablet, 1 at mobile.
- **Pricing**: 3-tier grid centred at desktop, stacking vertically below 1024px; the centre tier flips to `{components.pricing-tier-featured}` (dark inversion) as the recommended option.
- **Code-story sections**: a 2-up split — narrative copy left, code well right — collapsing to stacked at < 1024px.

### Whitespace Philosophy
- Whitespace on cream is generous and editorial — sections breathe at 96px and key bands open at 160px so the typography can scale up without feeling cramped.
- Inside cards, the system tightens to 16–32px so model thumbnails, statuses, and metadata sit in a compact list-of-cards rhythm.
- Hairline `{colors.hairline}` dividers replace shadow on cream surfaces; on dark surfaces, `{colors.divider-dark}` carries the equivalent role.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — flat | No shadow, no border | Default cream canvas, full-bleed bands. |
| 1 — outline | 1px solid `{colors.control-border}` | Model cards, pricing tiers, collection tiles. |
| 2 — bone inset | Surface colour shift to `{colors.surface-bone}` inside a `{colors.canvas}` band | Feature group containers, "How it works" walkthrough. |
| 3 — dark inversion | Card swaps to `{colors.surface-dark}` against cream | Code wells, featured pricing tier, "Scale on Replicate" hero card. |
| 4 — soft drop | `0 8px 24px rgba(32,32,32,0.08)` | Hover-anchored model thumbnails (visual only — not interaction-state-documented). |

Drop shadows exist in the extracted tokens but are restrained — used sparingly to lift photography thumbnails one step off the cream canvas. The dominant elevation language is colour-blocking.

### Decorative Depth
- **Hero atmospheric mesh** — the orange-to-pink gradient backing the home hero is a layered radial mesh: `{colors.primary}` core → `{colors.hero-glow}` mid-stop → `{colors.hero-pink}` outer wash. Reserved for the home hero band only.
- **Code-story dark band** — the "How it works" section uses `{colors.surface-dark}` full-bleed with a single hairline `{colors.divider-dark}` separating narrative copy and code well.
- **Contributor mosaic** — the home page features a horizontally-scrolling band of circular avatars (`{components.contributor-avatar}`) over a textured cream canvas; this is the only place avatars appear at the brand level.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero bands, full-bleed sections, footer. |
| `{rounded.xs}` | 4px | Code tabs, inline tags inside code wells. |
| `{rounded.sm}` | 6px | Mid-radius callouts, small inset chips. |
| `{rounded.md}` | 10px | Model cards, collection tiles, code wells. |
| `{rounded.lg}` | 16px | Pricing tiers, larger feature cards. |
| `{rounded.full}` | 9999px | Buttons, inputs, badges, avatars, pills. |

### Photography Geometry
- Model thumbnails: square (1:1) with `{rounded.md}` corners, full-bleed image to the card edge.
- Hero example outputs: 4:3 or 16:9 with `{rounded.md}` corners.
- Contributor avatars: circular (`{rounded.full}`), 40px on home, 32px in card metadata.
- The hero band uses a stylised black-ink illustration (the "tinkerer at the workbench") as its photography stand-in — kept inside the orange band rather than overlaid on cream.

## Components

### Buttons

**`button-primary`** — orange CTA
- Background `{colors.primary}`, label `{colors.on-primary}`, type `{typography.button-md}`, padding `12px 24px`, `rounded: {rounded.full}`, height 44px.
- The single most important action on a page (e.g. "Sign in with GitHub", "Try a model").
- Pressed state lives in `button-primary-pressed` (background `{colors.primary-deep}`).

**`button-dark`** — dark CTA
- Background `{colors.surface-dark}`, label `{colors.on-dark}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- Equal-weight secondary action paired with `{components.button-primary}`, or the primary action on cream when orange would be too loud.

**`button-outline`** — outlined CTA
- Background `{colors.surface-card}`, label `{colors.ink}`, 1px solid `{colors.hairline-strong}`, type `{typography.button-md}`, `rounded: {rounded.full}`.
- Tertiary action; appears alongside primary/dark for "View docs", "Read more".

**`button-ghost`** — inline button
- Background `{colors.canvas}`, label `{colors.ink}`, no border, type `{typography.button-md}`, `rounded: {rounded.full}`, padding `8px 16px`.
- Sub-actions inside cards and inline with body copy.

**`button-icon`** — icon button
- Background `{colors.surface-card}`, label `{colors.ink}`, 1px solid `{colors.control-border}`, `rounded: {rounded.full}`, 36×36px circular.
- Carousel arrows, copy-to-clipboard, GitHub link icon.

### Cards & Containers

**`model-card`** — model listing card
- Background `{colors.surface-card}`, text `{colors.ink}`, 1px `{colors.control-border}` border, type `{typography.body-md}`, `rounded: {rounded.md}`, padding `{spacing.lg}` (16px).
- Square thumbnail on top, model owner + name beneath in `{typography.body-sm}`, single-line description in `{colors.charcoal}`, status pill `{components.badge-status}` bottom-left.

**`collection-tile`** — collection-of-models tile
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.heading-md}`, `rounded: {rounded.md}`, padding `{spacing.xl}` (24px).
- Cream-on-cream tile inside a `{colors.surface-bone}` band, used for browsing model categories.

**`pricing-tier`** — pricing tier card
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}` (32px).
- 3-up grid; tier name in `{typography.display-lg}` ("Free", "Pro", "Enterprise"), price in `{typography.display-md}`.

**`pricing-tier-featured`** — featured pricing tier
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.body-md}`, `rounded: {rounded.lg}`, padding `{spacing.xxl}`.
- Centre tier flipped to dark inversion to mark "recommended".

**`code-block`** — code well
- Background `{colors.surface-dark}`, text `{colors.on-dark}`, type `{typography.code-md}`, `rounded: {rounded.md}`, padding `{spacing.xl}` (24px).
- Tab strip on top using `{components.code-tab}` for switching between languages (Python, Node.js, cURL, HTTP).

**`code-tab`** — code tab chip
- Background `{colors.surface-deep}`, text `{colors.on-dark-mute}`, type `{typography.code-sm}`, `rounded: {rounded.xs}`, padding `6px 12px`.
- `{components.code-tab-active}` swaps text colour to `{colors.on-dark}` and adds a 2px bottom underline in `{colors.primary}`; `{components.code-tab-focused}` adds a light outline for keyboard focus. Selection also needs a programmatic state.

**`hero-band`** — full-bleed hero
- Background `{colors.hero-warm}` with the atmospheric mesh detailed in Elevation, text `{colors.on-dark}`, type `{typography.display-xxl}` for the title.
- Used only on the home page; secondary pages open with cream + `{typography.display-xl}`.

### Inputs & Forms

**`text-input`** — default input
- Background `{colors.surface-card}`, text `{colors.ink}`, type `{typography.body-md}`, 1px solid `{colors.control-border}`, `rounded: {rounded.full}`, padding `12px 20px`, height 44px.
- Pill-shaped search and email fields. `{components.text-input-focused}` adds a 2px `{colors.ring-focus}` outline and stronger border; verify keyboard focus in the rendered interface.

### Navigation

**`nav-bar`** — top nav (desktop)
- Background `{colors.canvas}`, type `{typography.button-sm}`, height 60px, single hairline `{colors.hairline}` bottom border.
- Left: wordmark logo. Centre: top-level nav ("Explore", "Pricing", "Docs", "Blog"). Right: GitHub icon + "Sign in" link + `{components.button-primary}`.

**`nav-bar`** (mobile)
- Same height 60px, collapses centre nav into a hamburger icon. Logo stays left, sign-in CTA stays right.

**`sub-nav-pill`** — sub-nav chip
- Pill chips set in a horizontal row above content (e.g. "All", "Featured", "Image generation", "Audio"), `{components.sub-nav-pill}` styling.

### Signature Components

**`badge-status`** — model status badge
- Background `{colors.badge-success}`, label `{colors.on-dark}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 10px`.
- Anchored on the bottom-left of model cards to indicate "running" or "deployed".

**`badge-tag`** — neutral tag
- Background `{colors.canvas}`, label `{colors.ink}`, 1px solid `{colors.control-border}`, type `{typography.caption}`, `rounded: {rounded.full}`, padding `4px 10px`.
- Capability tags ("text-to-image", "video", "audio") on model cards.

**`contributor-avatar`** — community contributor
- Background `{colors.surface-card}` placeholder behind 1:1 photography, `rounded: {rounded.full}`, 40×40px (32px in metadata contexts).
- Used in the home-page contributor mosaic.

**`footer`** — global footer
- Background `{colors.surface-deep}`, text `{colors.on-dark}`, type `{typography.body-sm}`, `rounded: {rounded.none}`, padding `64px 32px`.
- Multi-column quick-links grid above a copyright row separated by `{colors.divider-dark}`.

## Do's and Don'ts

### Do
- Use `{colors.canvas}` (cream) as the default page background. White (`{colors.surface-card}`) appears only on individual cards, inputs, and the hero illustration backdrop.
- Reserve `{colors.primary}` for the primary CTA, the home hero band, and inline links — three roles, nothing else.
- Set every interactive element to `{rounded.full}` — buttons, inputs, badges, avatars, pills.
- Step content cards up to `{rounded.md}` (10px) or `{rounded.lg}` (16px) — never sharp corners.
- Open hero bands with `{typography.display-xxl}` (128px) and `{typography.display-xl}` (72px) at `lineHeight: 1.15` with negative letter-spacing.
- Use Bricolage Grotesque for display, Inter for UI/body, and JetBrains Mono for code; retain the system fallback in each token.
- Render code in `{components.code-block}` with a `{colors.surface-dark}` background — code is print, not an inline grey box.
- Pair photography with `{rounded.md}` corners and full-bleed crop inside cards.

### Don't
- Don't replace cream with pure white at the page level. The brand temperature comes from `{colors.canvas}`.
- Don't introduce a secondary brand colour. Orange is the only accent; semantic green and the dark focus outline are functional, not decorative.
- Check display wrapping before changing the 1.15 line height, especially with script fallback.
- Don't use the source proprietary families as a shipping default without confirmed rights.
- Don't apply `{rounded.full}` to content cards. Pill-shaped cards break the rhythm.
- Don't put code in a light grey box. Code wells are always `{colors.surface-dark}` or `{colors.surface-deep}`.
- Don't use orange for plain body text; keep it for underlined inline links, the primary CTA, and the hero band.
- Don't add drop shadows on cream surfaces. Elevation is colour-blocking; shadows are reserved for floating thumbnails.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop XL | ≥ 1440px | Full max-width 1280 body, hero band runs full-bleed, 4-up model grid. |
| Desktop | 1280–1439px | Container shrinks; padding `{spacing.xl}` (24px) sides. |
| Tablet Large | 1024–1279px | Model grid 3-up, code-story splits remain 2-up. |
| Tablet | 768–1023px | Model grid 2-up, code-story stacks (narrative on top, code below), pricing stacks vertically. |
| Mobile Large | 426–767px | Model grid 1-up at 480px+, nav collapses to hamburger, hero `{typography.display-xxl}` clamps to 64px. |
| Mobile | ≤ 425px | All grids 1-up, hero clamps to 48px, section padding `{spacing.section}` collapses to 64px. |

### Touch Targets
- The YAML lists 44px primary buttons and a 36px icon button; the sub-nav pill has no fixed height. Measure actual rendered target size and spacing on each layout, then enlarge smaller targets as needed for WCAG 2.2 criteria. Check keyboard focus and operation in the running interface.

### Collapsing Strategy
- Top-level nav collapses to hamburger at < 1024px; the wordmark and `{components.button-primary}` stay anchored.
- Hero `{typography.display-xxl}` clamps: 128px → 96px → 64px → 48px across the breakpoint ladder.
- Pricing 3-up grid stacks vertically at < 1024px with the featured tier remaining centre-stacked.
- Code-story splits switch from side-by-side to stacked at < 1024px, code well always second.
- Sub-nav pills convert from a wrap row to a horizontal scroll-rail at < 768px.

### Image Behavior
- Model thumbnails serve at 1.5× and 2× DPR; below 768px the system swaps to a 600×600 export instead of 1200×1200.
- Hero atmospheric mesh is rendered as a CSS gradient — no asset cost, no breakpoint variation.
- Code-block contents wrap softly at < 1024px (no horizontal scroll); long lines break with a continuation marker.

## Iteration Guide

1. Focus on ONE component at a time. Most interactive elements share `{rounded.full}` and the `{colors.canvas}` / `{colors.surface-card}` pair — only the role-specific tokens (`{colors.primary}`, `{components.code-block}`) shift between variants.
2. Reference component names and tokens directly (`{colors.primary}`, `{components.button-primary-pressed}`, `{rounded.lg}`) — do not paraphrase.
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md` after edits; orphaned-tokens warnings will catch unused entries.
4. Add new variants as separate entries (`-pressed`, `-disabled`, `-featured`) — do not bury them in prose.
5. Default body type to `{typography.body-md}`; reach for `{typography.subtitle}` only on hero subtitles.
6. Keep `{colors.primary}` scarce — if more than one orange element appears per viewport, ask whether one should drop to `{colors.surface-dark}` instead.

## Known Gaps

- Current Replicate model availability, pricing, source code examples, contributor photos, illustrations, logo, and reuse rights have not been checked. Verify current sources and permission before publication.
- Font loading and glyph fallback, photo-overlay contrast, actual focus and target sizes, and desktop behavior on macOS/Windows/Linux have not been observed.
- Active/pressed visual states are documented for `button-primary-pressed` and `code-tab-active`; most other controls still need explicit interactive-state testing. Use `{colors.ring-focus}` on light and `{colors.ring-focus-dark}` on dark surfaces.
- The model playground / try-this-model interactive surfaces (logged-in feature) are out of scope; only the public marketing canvas is documented.
- Dashboard / billing / API key management surfaces are not extracted — those live behind authentication.
- The home hero illustration ("the tinkerer at the workbench") is treated as decorative artwork, not a system component; replicating it requires bespoke illustration rather than tokens.
