---
version: alpha
name: Runwayml-design-analysis
description: >-
  An inspired interpretation of Runway's design language — an editorial, gallery-grade marketing system for an AI creative-tools company. Cinematic photographic heroes give way to crisp white reading surfaces, a tight monochrome neutral ladder, and a portable OFL Inter stack carrying every level of the hierarchy. The source abcNormal face remains a reference until rights are confirmed. Pure black solid pills serve primary actions, with no accent colour competing for attention.

colors:
  primary: "#000000"
  on-primary: "#ffffff"
  ink: "#030303"
  ink-soft: "#1a1a1a"
  graphite: "#404040"
  slate: "#676f7b"
  slate-soft: "#727a85"
  mute: "#6b7280"
  stone: "#939393"
  ash: "#999999"
  hairline: "#e7eaf0"
  hairline-soft: "#c9ccd1"
  control-border: "#767676"
  surface-cool: "#d0d4d4"
  canvas: "#ffffff"
  canvas-warm: "#fefefe"
  scrim: "#1a1a1a"
  footer: "#030303"

typography:
  display:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -1.2px
  display-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -1px
  heading-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.9px
  heading-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
  subtitle:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  body-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
  body-tight:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.16px
  link-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
  meta:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.26px
  eyebrow:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.35px
  micro-caps:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 11px
    fontWeight: 450
    lineHeight: 1.3
    letterSpacing: 0.2px
  button:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 16px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 12px
    height: 48px
  button-primary-on-dark:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 12px
    height: 48px
  button-ghost:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.full}"
    padding: 12px
    height: 48px
  button-text-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.link-sm}"
    rounded: "{rounded.xs}"
    padding: 4px
    textDecoration: underline
    minHeight: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.link-sm}"
    height: 64px
    padding: 24px
  nav-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.link-sm}"
    padding: 8px
    minHeight: 44px
  pricing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 24px
    width: 224px
    border: "1px solid {colors.control-border}"
  pricing-card-featured:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 24px
    width: 224px
    border: "1px solid {colors.control-border}"
  pricing-tier-name:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-md}"
  pricing-amount:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
  research-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.control-border}"
  media-thumbnail:
    backgroundColor: "{colors.surface-cool}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  hero-photo:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: 48px
  studios-tile:
    backgroundColor: "{colors.canvas-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-tight}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.control-border}"
  studios-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.slate}"
    border: "1px solid {colors.control-border}"
    typography: "{typography.micro-caps}"
    rounded: "{rounded.full}"
    padding: 6px
  form-field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px
    borderBottom: "1px solid {colors.control-border}"
  form-field-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px
    borderBottom: "2px solid {colors.ink}"
    outline: "2px solid {colors.ink}"
  alert-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-tight}"
    rounded: "{rounded.lg}"
    padding: 16px
    border: "1px solid {colors.control-border}"
  footer:
    backgroundColor: "{colors.footer}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    padding: 64px
  footer-link:
    backgroundColor: "{colors.footer}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    textDecoration: underline
  footer-eyebrow:
    backgroundColor: "{colors.footer}"
    textColor: "{colors.stone}"
    typography: "{typography.eyebrow}"
---

## Overview

This reference interprets Runway's marketing site as a curatorial space. Cinematic stills anchor hero modules in `{colors.scrim}`, while the remaining sections use `{colors.canvas}` for reading. The restrained neutral palette carries captions and dividers; use `{colors.slate}` for essential secondary text on white and reserve `{colors.slate-soft}` for decoration.

Typography does almost all of the heavy lifting. The source uses `abcNormal`; the portable tokens use Inter with a system sans-serif fallback from 11px micro-caps to 48px editorial display. Negative letter-spacing tightens the heading silhouette, but the rendered line breaks need checking with the substitute font. Primary actions use black solid pills (`{colors.primary}` background, `{colors.on-primary}` text, `{rounded.full}` corners).

The layout discipline is editorial: hairline dividers (`{colors.hairline}`), uppercase eyebrows (`{typography.eyebrow}`), and an 8-px spacing grid that resolves to large 64–96px section gutters. Sections cycle through a tight rhythm — dark photographic hero → white reading band → research grid on canvas → photographic full-width interlude → dark CTA strip → black footer — letting black ink and black-and-white photography do the dramatic work that other sites delegate to colour.

**Key Characteristics:**
- Cinematic dark photographic heroes (`{colors.scrim}` over editorial stills) bookending crisp `{colors.canvas}` reading bands
- A portable Inter stack covering every typographic role, with `abcNormal` retained only as a source reference
- Black-only primary action language: every CTA is `{components.button-primary}` (`{colors.primary}` pill with `{rounded.full}` corners and 14px/600 button text)
- Five-tier neutral ladder (`{colors.ink}` → `{colors.graphite}` → `{colors.slate}` → `{colors.stone}` → `{colors.hairline}`) carries the entire UI without accent colour
- A reference 5-column pricing grid with a pale featured infill; verify the live tiers before reuse
- Hairline dividers and uppercase `{typography.eyebrow}` lock-ups give marketing sections an editorial, exhibition-catalogue cadence
- Photography is treated as content, not decoration — full-bleed, cinematic, and tonal rather than vivid

## Colors

### Brand & Accent
- **Black** (`{colors.primary}`): The single brand action colour. Every primary CTA, every pricing-tier subscription button, every form submit pill resolves to this exact black. Used as the footer canvas as well, which extends the brand voice through the bottom of every page.
- **Paper White** (`{colors.on-primary}`): Type colour on `{colors.primary}` surfaces; canvas of every reading section.

### Surface
- **Canvas** (`{colors.canvas}`): Primary reading-page background.
- **Canvas Warm** (`{colors.canvas-warm}`): Near-imperceptible off-white used to lift studios-page tiles a half-tone above pure white without losing the paper feel.
- **Featured Surface** (`{colors.hairline}`): The infill behind the featured pricing tier ("Pro") and behind certain table-style banners — chosen for its near-zero saturation so it reads as a tonal step rather than a fill.
- **Hairline Soft** (`{colors.hairline-soft}`): decorative 1-pixel dividers only; important column boundaries use `{colors.control-border}`.
- **Cool Surface** (`{colors.surface-cool}`): Default placeholder fill for media thumbnails and image-loading frames before the asset paints.
- **Scrim** (`{colors.scrim}`): The atmospheric dark layer that cinematic hero photography is laid into; behaves as the "stage" colour for full-bleed image modules.
- **Footer** (`{colors.footer}`): Near-pure black footer canvas, one notch warmer than `{colors.primary}` so it sits visually distinct when the two stack.

### Text
- **Ink** (`{colors.ink}`): Primary heading and body text on `{colors.canvas}`; closest the system gets to absolute black for type.
- **Ink Soft** (`{colors.ink-soft}`): Nav links, secondary headings, body emphasis — one click softer than ink.
- **Graphite** (`{colors.graphite}`): Standard body copy across marketing sections, balancing readability with calm.
- **Slate** (`{colors.slate}`): tertiary metadata on white. **Slate Soft** (`{colors.slate-soft}`): decorative tint only on white; its small-text contrast is insufficient there.
- **Mute** (`{colors.mute}`): Lighter neutral for inline disabled or fine-print copy.
- **Stone** (`{colors.stone}`): footer eyebrow caps on dark; not essential text on white.
- **Ash** (`{colors.ash}`): decorative light neutral only, not captions or fine print on white.

### Semantic
The system does not introduce signal colours (red, green, yellow). Validation states in forms rely on borders and copy rather than colour shifts. Where the contact form indicates a required field, the only visual cue is an asterisk in `{colors.ink}` paired with helper text in `{colors.graphite}`.

## Typography

### Font Family
The source references proprietary **abcNormal**. The portable tokens use [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) with `system-ui, sans-serif` fallback on macOS, Windows, and Linux. Load Inter where available; use abcNormal only after confirming its rights. Check glyph coverage and wrapping in the rendered interface.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display}` | 48px | 400 | 1.15 | -1.2px | Page-level editorial display |
| `{typography.display-sm}` | 40px | 400 | 1.15 | -1px | Pricing tier amount, hero secondary headlines |
| `{typography.heading-md}` | 36px | 400 | 1.2 | -0.9px | Section headlines, tier names |
| `{typography.heading-sm}` | 24px | 400 | 1.25 | 0 | Card titles, sub-section heads, link text in featured cards |
| `{typography.subtitle}` | 20px | 400 | 1.3 | 0 | Hero sub-copy and lead paragraphs |
| `{typography.body}` | 16px | 400 | 1.5 | 0 | Default body copy, form fields, footer link list |
| `{typography.body-strong}` | 16px | 600 | 1.5 | 0 | Inline emphasis, "Get Started"-class label text |
| `{typography.body-tight}` | 16px | 400 | 1.3 | -0.16px | Tight-leading body for marketing cards and CTA cards |
| `{typography.link-sm}` | 14px | 600 | 1.43 | 0 | Nav links, button labels, "Learn More" text links |
| `{typography.eyebrow}` | 14px | 500 | 1.43 | 0.35px | Uppercase eyebrows above section headings |
| `{typography.meta}` | 13px | 400 | 1.3 | -0.26px | Tertiary metadata (dates, fine print, table footnotes) |
| `{typography.micro-caps}` | 11px | 450 | 1.3 | 0.2px | Footer column headings, small-caps tags ("PRESS", "RESOURCES") |
| `{typography.button}` | 14px | 600 | 1.43 | 0 | Every button label across the system |

### Principles
- **One face, every level.** Hierarchy is articulated through size, weight, and tracking — never through a contrasting display family. The result is a uniform editorial cadence that reads as confident rather than expressive.
- **Negative tracking on display, neutral tracking on body.** Headings 24–48px sit at -0.9 to -1.2px to tighten silhouettes; body copy stays at 0 for legibility.
- **Tight leading on display, generous leading on body.** The portable display tokens use line heights of 1.15–1.3; body uses 1.5. Check each breakpoint for clipping.
- **Uppercase reserved for two roles.** `{typography.eyebrow}` for section labels, `{typography.micro-caps}` for footer columns and small tags. Body copy is never set in uppercase.

### Note on Font Substitutes
The YAML already uses Inter with its specified tracking. Recheck actual font loading and line breaks before adjusting font size or tracking.

## Layout

### Spacing System
- **Base unit**: 8px (with 4px and 6px micro-steps for inline element gaps).
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 64px · `{spacing.section-lg}` 96px.
- Card internal padding sits at `{spacing.lg}` (24px). Section vertical rhythm alternates between `{spacing.section}` (64px) for tight reading bands and `{spacing.section-lg}` (96px) for editorial breaks between major modules. Inline button padding is `{spacing.sm}` vertical / `{spacing.lg}` horizontal.

### Grid & Container
- Marketing pages render inside a centred container that caps near 1280px on widescreen breakpoints; the document maintains generous left/right gutters (~`{spacing.xxl}`) at every breakpoint above 1024px.
- The reference pricing surface uses five equal-width columns on widescreen. Fetch current plan names and prices before rendering; [Runway's plan transition notice](https://help.runwayml.com/hc/en-us/articles/52068047744019-Unlimited-plan-is-switching-to-Max) makes fixed tier labels unsafe. Use visible `{colors.control-border}` column rules.
- Research/products listings use a 12-column underlying grid where each row presents a 5/7 split: media thumbnail on the left (5 columns), aligned text block on the right (7 columns).
- Studios pages break the discipline deliberately: a dense, irregular masonry of editorial poster tiles, captioned in `{typography.body-tight}`, with no consistent column count — the page is meant to read as a programme grid.

### Whitespace Philosophy
Whitespace at Runway is structural, not decorative. Sections are separated by 64–96px verticals; cards inside a section are separated by 16–24px gaps. There are no card shadows or coloured surfaces standing in for layout — `{colors.canvas}` carries through, and rhythm comes from line-height and section spacing alone. The studios pages are the exception; their dense poster grids feel almost cluttered by contrast, which is the point — they read like a printed catalogue.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, optional 1px `{colors.hairline}` divider | Default state for cards, pricing columns, research rows, footer surfaces |
| Photographic | Full-bleed image laid into `{colors.scrim}`, no border, `{rounded.lg}` corners on contained variants | Hero modules, "We are building foundational simulation World Models" interlude, mid-page CTA panels |
| Subtle Surface Lift | `{colors.hairline}` infill behind a card on a `{colors.canvas}` page, with `{colors.control-border}` boundary | Reference featured pricing tier; confirm the current offer |

The system avoids drop shadows entirely. Depth is created by photographic layering and tonal surface shifts, never by blurred shadows. This is a deliberate aesthetic choice — Runway communicates polish through editorial restraint, not material affordance.

### Decorative Depth
- **Cinematic photography as backdrop.** Reference hero and interlude imagery uses a dark stage. Confirm rights for each selected image and measure text contrast over each crop; add a scrim or relocate text when necessary.
- **Tonal surface stepping.** The featured-tier infill (`{colors.hairline}` against `{colors.canvas}`) is subtle; use the control border and a text label so the state does not rely on the infill alone.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Pricing-grid cells, table rows, form fields, footer link blocks |
| `{rounded.xs}` | 4px | Small inline accents, focus rings, secondary link chips |
| `{rounded.sm}` | 6px | Tag chips, secondary link buttons |
| `{rounded.md}` | 8px | Research-card thumbnails, studios poster tiles, media containers |
| `{rounded.lg}` | 16px | Alert banners, hero-photograph containers, full-bleed CTA panels |
| `{rounded.full}` | 9999px | Every primary button (CTA pills), studios tag pills |

### Photography Geometry
- **Hero stills** are full-bleed, no rounding — they extend to the page edges to feel cinematic rather than card-like.
- **Contained hero panels** (mid-page interludes) take `{rounded.lg}` corners, signalling "module" rather than "page".
- **Research thumbnails** are 16:9 with `{rounded.md}` corners and a `{colors.surface-cool}` placeholder fill.
- **Studios poster tiles** vary in aspect ratio (square, 4:5, landscape) and use `{rounded.md}` corners; the deliberate aspect-ratio inconsistency is what gives the studios grid its programme-catalogue feel.
- **Avatar/logo lockups** in the partner row are rendered without rounding, in flat black wordmarks on `{colors.canvas}`, evenly spaced.

## Components

### Buttons

**`button-primary`** — primary CTA in this reference system
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}`, rounded `{rounded.full}`, height 48px.
- The system uses the same pill at every scale; no large/small distinction.

**`button-primary-on-dark`** — the inverse used when the surface itself is `{colors.scrim}` (dark hero CTAs)
- Background `{colors.on-primary}`, text `{colors.primary}`, otherwise identical token set to `{components.button-primary}`.

**`button-ghost`** — secondary actions on light surfaces ("Schedule a Demo", "Sign Up" on the Free tier)
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.button}`, rounded `{rounded.full}`, with a 1px `{colors.ink}` border.

**`button-text-link`** — inline secondary actions and table-row links
- Background `{colors.canvas}`, text `{colors.ink}`, persistent underline, type `{typography.link-sm}`, minimum height 44px.

### Navigation

**`nav-bar`** — the persistent top bar
- Background `{colors.canvas}`, height ~64px, padding `{spacing.lg}` horizontal, `{typography.link-sm}` for menu items.
- Reference layout: brand wordmark left, navigation in the centre, actions on the right. Confirm current navigation labels and logo asset before publication.
- The bar sits flush against the document top and is divided from the page only by spacing, not by a hairline.

**`nav-link`** — top-bar menu items
- Background `{colors.canvas}`, text `{colors.ink-soft}`, type `{typography.link-sm}`, 8px padding and a 44px minimum height.

### Cards & Containers

**`pricing-card`** — standard tier in the reference layout
- Background `{colors.canvas}`, text `{colors.ink}`, padding `{spacing.lg}`, no rounding, separated by 1px `{colors.control-border}` rules.
- Internal stack: tier name (`{typography.heading-md}`) → description (`{typography.body}` in `{colors.graphite}`) → current amount (`{typography.display-sm}`) → unit caption (`{typography.meta}` in `{colors.slate}`) → action button → feature list. Confirm live plan data before use.

**`pricing-card-featured`** — a featured tier, if one is offered
- Identical structure to `{components.pricing-card}` but the column infill is `{colors.hairline}` instead of `{colors.canvas}`. Preserve its clear boundary and use any badge shown in current official plan data.

**`pricing-tier-name`** — header line of each pricing column
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.heading-md}`. Source current tier names from the live offer.

**`pricing-amount`** — large monetary display in each pricing card
- Background `{colors.canvas}`, text `{colors.ink}`, type `{typography.display}` paired with a `{typography.meta}` "per user/month" caption beside it.

**`research-card`** — each row of "Our latest Research and Products"
- Layout: `{components.media-thumbnail}` left (16:9) + text block right.
- Right block: title (`{typography.heading-sm}`) → description (`{typography.body}` in `{colors.graphite}`) → footer link (`{typography.link-sm}`, underlined on active).

**`studios-tile`** — poster cards on the studios index
- Background `{colors.canvas-warm}`, image fills the tile, optional caption strip below in `{typography.body-tight}` (`{colors.graphite}`).
- Tiles are deliberately heterogeneous in aspect ratio.

**`studios-tag`** — small-caps category pills on studios cards
- Background `{colors.canvas}`, text `{colors.slate}`, type `{typography.micro-caps}`, padding `{spacing.xxs}` × `{spacing.sm}`, rounded `{rounded.full}`.

**`hero-photo`** — full-bleed cinematic hero blocks
- `{colors.scrim}` background carrying a photographic still, padding `{spacing.xxl}`, rounded `{rounded.lg}` on contained variants and `{rounded.none}` on edge-to-edge variants.
- Internal stack: optional eyebrow, headline, sub-copy, and `{components.button-primary-on-dark}` CTA. Keep text opaque until each image crop's contrast has been measured.

**`media-thumbnail`** — image placeholder
- Background `{colors.surface-cool}`, rounded `{rounded.md}`, ratio 16:9 by default, image lazy-loads on top.

### Inputs & Forms

**`form-field`** — every contact-form input (select, text, textarea)
- Background `{colors.canvas}`, text `{colors.ink}`, label above field in `{typography.body}` `{colors.ink}`, helper text in `{typography.meta}` `{colors.slate}`.
- The field uses a 1px bottom rule in `{colors.control-border}`; use `{colors.slate}` for essential placeholder or helper text.
- Padding `{spacing.sm}` vertical, no rounding.

**`form-field-focused`** — focused state
- Bottom rule deepens to `{colors.ink}` and a 2px outline marks keyboard focus.

**`alert-banner`** — privacy/cookie disclosure copy
- Background `{colors.canvas}`, text `{colors.ink}`, `{typography.body-tight}`, padding `{spacing.md}`, rounded `{rounded.lg}`, 1px `{colors.control-border}` border.

### Footer

**`footer`** — the system's terminal surface
- Background `{colors.footer}`, text `{colors.on-primary}`, padding `{spacing.section}` vertical, `{spacing.lg}` horizontal.
- Reference layout: link grid followed by a brand and legal strip. Use the current approved logo asset.

**`footer-eyebrow`** — small-caps column headings ("Product", "Initiatives", "Company")
- Background `{colors.footer}`, text `{colors.stone}`, type `{typography.eyebrow}`.

**`footer-link`** — link-list items
- Background `{colors.footer}`, text `{colors.on-primary}`, type `{typography.body}`.

### Signature Components

**Pricing 5-Column Slab** — The reference module is a flat five-column slab. The featured tier has a pale infill plus a clear border and text label. Plan names, prices, and availability must come from current official data before publication.

**Editorial Eyebrow + Display Lockup** — Across the site, headline modules follow a fixed three-part rhythm: uppercase `{typography.eyebrow}` label → 36–48px `{typography.display}` headline → `{typography.body}` lead paragraph. Section spacing locks to `{spacing.section}` between modules. The lockup is what gives marketing pages their festival-programme cadence.

**Cinematic Atmospheric Interlude** — Mid-document interludes (the "We are building foundational simulation World Models" forest scene, the "We are building AI to simulate the world…" closing strip) use a contained `{components.hero-photo}` panel with `{rounded.lg}` corners. They function as pacing breaks between research grids and CTA bands rather than promotional units.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for primary actions and the footer; use `{components.button-primary}` for every primary CTA without varying corner radius or fill.
- Stack uppercase `{typography.eyebrow}` over `{typography.display}` for every major section opener — it is the system's signature lockup.
- In the reference pricing layout, pair `{colors.hairline}` infill with a visible border and text label. Follow current official badges when representing a live plan.
- Set body copy in `{colors.graphite}` against `{colors.canvas}` for paragraphs, and reserve `{colors.ink}` for headings and emphasis only.
- Treat photography as content: full-bleed, cinematic, aligned to the page edge in heroes; `{rounded.lg}` only when the photo is contained inside a section.
- Lock display headings to negative letter-spacing (`-0.9px` to `-1.2px`) — the tight tracking is core to the brand voice.
- Use `{rounded.full}` pills for buttons and `{rounded.none}` for table/grid cells. Never mix.

### Don't
- Don't introduce accent colours (blue, green, red) into marketing surfaces — Runway's voice is monochrome plus photography.
- Don't apply drop shadows or glows to cards. Depth is photographic and tonal, not material.
- Don't invent badges or tier labels; [current Runway pricing](https://runway.com/pricing) uses named plan badges that must be sourced as displayed.
- Don't break headings into bold + light contrast; every heading is regular weight (`400`) with tight tracking.
- Don't centre body paragraphs longer than one sentence — the system uses left-aligned reading bands almost exclusively.
- Don't use uppercase for body or button copy. Uppercase is reserved for `{typography.eyebrow}` (14px) and `{typography.micro-caps}` (11px).
- Use the approved wordmark asset and check its contrast on each surface.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| 2xl | 1600px | Reference editorial container; old pricing example was 5-up; current tier count comes from the live offer |
| xl | 1536px | Same layout, marginally tighter gutters |
| lg | 1280px | Default desktop reading view |
| md | 1200px | Fit current pricing tiers to available width; verify text wrapping |
| sm | 1024px | Pricing columns collapse as needed; research rows stack at certain breakpoints |
| xs | 768px | Top nav collapses to a hamburger; section padding drops to `{spacing.section}` |
| xxs | 640px | Single-column reading; hero display drops to `{typography.display-sm}`; pricing tiers stack 1-up |

### Touch Targets
- The YAML sets primary buttons to 48px and inline links to a 44px minimum height. Measure rendered size, spacing, focus, and keyboard operation in each layout.
- `{components.nav-link}` specifies a 44px minimum height; measure the rendered mobile menu targets.
- Pricing-tier `{components.button-primary}` extends full-column-width on mobile.

### Collapsing Strategy
- **Nav.** Centred desktop menu collapses into a single hamburger that opens an overlay sheet; the right-side `{components.button-primary}` "Try Runway" stays visible above the hamburger as the persistent action.
- **Pricing.** The reference slab collapses to single-column cards at xxs; preserve the featured text label and border alongside its pale infill.
- **Research grid.** 5/7 split collapses to image-on-top, text-below at sm; thumbnail rounding (`{rounded.md}`) is preserved.
- **Footer.** The reference link grid collapses to fewer columns; check the approved wordmark and legal links in the rendered mobile layout.

### Image Behavior
- Hero photographs swap to a tighter crop on mobile (vertical-leaning) so the focal subject stays centred at xxs widths.
- `{components.media-thumbnail}` containers preserve their 16:9 ratio at every breakpoint; the `{colors.surface-cool}` placeholder fill paints during lazy-load.
- Studios poster tiles preserve their original aspect ratios at every breakpoint — the masonry simply re-flows into fewer columns.

## Iteration Guide

1. Focus on ONE component at a time. Start with `{components.button-primary}` and `{components.nav-bar}` — they appear on every page and anchor the system.
2. Reference component names and tokens directly (`{colors.ink}`, `{components.button-primary-on-dark}`, `{rounded.full}`) — do not paraphrase or substitute hex values.
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag drift automatically.
4. Add new variants as separate `components:` entries (`-pressed`, `-disabled`, `-focused`) — never bury them inside prose.
5. Default body copy to `{typography.body}` and emphasis to `{typography.body-strong}`. Reserve `{typography.eyebrow}` and `{typography.micro-caps}` for their two specific roles (section openers and footer columns).
6. Keep `{colors.primary}` scarce — if more than one black-pill action appears in a single viewport, neutralise the secondary one to `{components.button-ghost}`.
7. When introducing photography, lay it into `{colors.scrim}` and let the next white band break against it. Avoid mid-section photographic accents that don't span the full content width — they read as off-system.

## Known Gaps

- Current Runway plans, prices, navigation, wordmark, photographs, and reuse rights require confirmation from current official sources before publication.
- Inter loading and glyph fallback, photograph overlay contrast, focus states and target sizes, and desktop behavior on macOS, Windows, and Linux have not been observed.
