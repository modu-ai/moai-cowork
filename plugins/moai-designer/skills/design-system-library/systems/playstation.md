---
version: alpha
name: PlayStation-design-analysis
description: |
  A reference marketing system with alternating black, white, and PlayStation Blue chapters, rounded CTAs, and product imagery. The source-reference display face is PlayStation SST; distribution defaults use OFL Roboto at weight 300 for display and OFL Inter for body and controls. Game art, console images, wordmarks, and pricing require current source and usage-right checks before publication.

colors:
  primary: "#0070d1"
  primary-pressed: "#0064b7"
  primary-active: "#004d8d"
  on-primary: "#ffffff"
  link-light: "#0064b7"
  link-dark: "#53b1ff"
  commerce: "#d53b00"
  commerce-pressed: "#aa2f00"
  commerce-link-base: "#d63d00"
  on-commerce: "#ffffff"
  ink: "#000000"
  ink-deep: "#121314"
  ink-elevated: "#181818"
  charcoal: "#1f2024"
  body-light: "rgba(0,0,0,0.6)"
  mute-light: "#6b6b6b"
  ash-light: "#cccccc"
  body-dark: "rgba(255,255,255,0.7)"
  mute-dark: "rgba(229,229,229,0.55)"
  ash-dark: "rgba(229,229,229,0.2)"
  canvas-light: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#f5f7fa"
  surface-filter: "rgba(245,247,250,0.3)"
  canvas-dark: "#000000"
  surface-dark-elevated: "#121314"
  surface-dark-card: "#181818"
  hairline-light: "#f3f3f3"
  card-border-light: "#898989"
  card-border-dark: "#6b6b6b"
  hairline-dark: "rgba(229,229,229,0.2)"
  on-dark: "#ffffff"
  on-dark-mute: "#cccccc"
  warning: "#c81b3a"
  ps-plus-gold-start: "#ffce21"
  ps-plus-gold-mid: "#f5a623"
  ps-plus-gold-end: "#ee8e00"
  marathon-yellow: "#deff20"

typography:
  display-xl:
    fontFamily: Roboto, Arial, sans-serif
    fontSize: 54px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.1px
  display-lg:
    fontFamily: Roboto, Arial, sans-serif
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  display-md:
    fontFamily: Roboto, Arial, sans-serif
    fontSize: 35px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  heading-xl:
    fontFamily: Roboto, Arial, sans-serif
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  heading-lg:
    fontFamily: Roboto, Arial, sans-serif
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.1px
  heading-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  body-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.1px
  body-strong:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.4px
  body-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  link-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-lg:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.45px
  button-md:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.324px

rounded:
  none: 0px
  sm: 4px
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
  section: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
  button-commerce:
    backgroundColor: "{colors.commerce}"
    textColor: "{colors.on-commerce}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-commerce-pressed:
    backgroundColor: "{colors.commerce-pressed}"
    textColor: "{colors.on-commerce}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
  button-secondary-light:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
    border: "1px solid {colors.mute-light}"
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
    border: "1px solid {colors.on-dark-mute}"
  button-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ash-light}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.mute-light}"
  text-input-focused:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  filter-pill:
    backgroundColor: "{colors.surface-filter}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.mute-light}"
  filter-pill-active:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "1px solid {colors.card-border-light}"
  product-card-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
    border: "1px solid {colors.card-border-dark}"
  game-tile:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  feature-card:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 32px
    border: "1px solid {colors.card-border-light}"
  hero-band-blue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    rounded: "{rounded.none}"
    padding: 96px 48px
  hero-band-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 96px 48px
  hero-band-light:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: 96px 48px
  ps-plus-banner:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    typography: "{typography.heading-xl}"
    rounded: "{rounded.md}"
    padding: 48px 32px
    accentGradient: "linear-gradient(90deg, {colors.ps-plus-gold-start}, {colors.ps-plus-gold-mid}, {colors.ps-plus-gold-end})"
    accentPlacement: top
  carousel-paddle:
    backgroundColor: "{colors.surface-dark-elevated}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    size: 48px
    border: "1px solid {colors.on-dark-mute}"
  pagination-dot:
    backgroundColor: "{colors.mute-light}"
    rounded: "{rounded.full}"
    size: 8px
  pagination-dot-active:
    backgroundColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    size: 8px
  badge-info:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  primary-nav:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-strong}"
    rounded: "{rounded.none}"
    height: 48px
  sub-nav:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
    height: 40px
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-md}"
    rounded: "{rounded.none}"
    padding: 48px 32px
  support-search-bar:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 56px
    border: "1px solid {colors.mute-light}"
  support-row:
    backgroundColor: "{colors.canvas-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 16px 0px
  link-inline:
    textColor: "{colors.link-light}"
    typography: "{typography.link-md}"
    textDecoration: underline
  link-inline-on-dark:
    textColor: "{colors.link-dark}"
    typography: "{typography.link-md}"
    textDecoration: underline
---

## Overview

The design reference alternates full-bleed bands of `{colors.canvas-dark}`, `{colors.canvas-light}`, and `{colors.primary}`. A section can carry console imagery, a game rail, a PlayStation Plus tier banner, or news. The background change separates chapters, with `{spacing.section}` (96px) as the documented spacing token. Recheck current campaigns and assets before using historical examples.

Dark and light modes share `{rounded.full}` buttons and `{rounded.md}` cards. The YAML uses Roboto and Inter as distribution fonts while retaining the source-reference type weights. `{colors.primary}` (`#0070d1`) is the third surface mode for high-priority bands such as a CTA strip or footer.

The display hierarchy keeps **weight 300** through 54, 44, 35, 28, and 22px roles; Roboto supplies that weight by default. Body copy uses Inter at 18px and 1.5 line height. Check wrapping and readability with the chosen language and loaded fonts.

**Key Characteristics:**
- Three-canvas chapter system: `{colors.canvas-dark}` (black), `{colors.canvas-light}` (white), `{colors.primary}` (PlayStation Blue) alternating down the page
- PlayStation Blue (`{colors.primary}` — `#0070d1`) is the universal primary CTA — fully-rounded pill at `{rounded.full}` (9999px)
- Commerce orange (`{colors.commerce}` — `#d53b00`) is the secondary CTA reserved for "Buy now" / "Pre-order" / store actions
- Roboto distribution display tier renders at **weight 300** with the token tracking; PlayStation SST is the source-reference face
- 8px-radius (`{rounded.md}`) for product cards and feature panels; 4px-radius (`{rounded.sm}`) for inputs; pills (`{rounded.full}`) for every CTA
- Game tiles, console renders, and tier illustrations carry the main visual content when current assets and rights are available
- Color-block page rhythm (one observed band sequence): dark hero → light console showcase → dark "Great PS4 & PS5 games" rail → light "Discover PlayStation Plus" tier band → light "30 years of PlayStation" callout → dark "ON PLAYSTATION" band → light news strip → blue footer

## Colors

> **Source-reference paths:** `/en-tr/`, `/en-tr/ps5/games/`, `/en-tr/games/marathon/`, `/tr-tr/support/account/`. These are not a current live-page verification.

### Brand & Accent
- **PlayStation Blue** (`{colors.primary}` — `#0070d1`): filled primary CTA, footer surface, and info badge. The active filter pill uses a white fill with `{colors.primary-active}` border; inline links on dark use `{colors.link-dark}`.
- **PlayStation Blue Pressed** (`{colors.primary-pressed}` — `#0064b7`): pressed state for the primary pill — also doubles as the inline link color on light surfaces.
- **PlayStation Blue Active** (`{colors.primary-active}` — `#004d8d`): darker blue used for the selected filter-pill border; the primary button's pressed state uses `{colors.primary-pressed}`.
- **Commerce Orange** (`{colors.commerce}` — `#d53b00`): the secondary CTA reserved for store/buy/pre-order actions. The only warm color in the system.
- **Commerce Orange Pressed** (`{colors.commerce-pressed}` — `#aa2f00`): pressed state for commerce buttons.
- **Marathon Yellow** (`{colors.marathon-yellow}` — `#deff20`): a single high-saturation game-page accent extracted from Marathon's product palette — used only inside the dedicated `/marathon/` game page chrome and not part of the system's general accent vocabulary.

### Surface
- **Canvas Dark** (`{colors.canvas-dark}` — `#000000`): pure black hero band, primary nav background, footer base. The dominant surface for editorial product moments.
- **Surface Dark Elevated** (`{colors.surface-dark-elevated}` — `#121314`): inset dark panels, PS Plus tier banner background, "ON PLAYSTATION" gradient end.
- **Surface Dark Card** (`{colors.surface-dark-card}` — `#181818`): game tile fill, dark product card background.
- **Canvas Light** (`{colors.canvas-light}` — `#ffffff`): true white console-showcase band, support page body, news strip background.
- **Soft Surface** (`{colors.surface-soft}` — `#f3f3f3`): hairline-soft band fill on light pages, divider rule on light surfaces.
- **Surface Card** (`{colors.surface-card}` — `#f5f7fa`): cool-blue-tinted product card and tier-card background on light canvas.
- **Surface Filter** (`{colors.surface-filter}` — `rgba(245,247,250,0.3)`): translucent fill for filter-pill default state on light canvas.
- **Hairline Light** (`{colors.hairline-light}` — `#f3f3f3`): 1px divider rule on light pages.
- **Hairline Dark** (`{colors.hairline-dark}` — `rgba(229,229,229,0.2)`): translucent 1px divider on dark canvas.

### Text
- **Ink** (`{colors.ink}` — `#000000`): primary text on `{colors.canvas-light}`. Headlines, button text, support body.
- **Ink Deep** (`{colors.ink-deep}` — `#121314`): dark panel and gradient tone; use `{colors.on-dark}` for readable titles on dark cards.
- **Ink Elevated** (`{colors.ink-elevated}` — `#181818`): the lightest of the dark-canvas inks, used for elevated card backgrounds.
- **Body Light** (`{colors.body-light}` — `rgba(0,0,0,0.6)`): translucent body text on light canvas — the system's default paragraph color.
- **Mute Light** (`{colors.mute-light}` — `#6b6b6b`): metadata text and footer link captions on light canvas.
- **Ash Light** (`{colors.ash-light}` — `#cccccc`): disabled-state text or decorative rule only; use `{colors.mute-light}` for essential utility text on white.
- **On Dark** (`{colors.on-dark}` — `#ffffff`): primary text on `{colors.canvas-dark}` — headlines, button text on dark hero bands.
- **Body Dark** (`{colors.body-dark}` — `rgba(255,255,255,0.7)`): translucent body text on dark canvas.
- **On Dark Mute** (`{colors.on-dark-mute}` — `#cccccc`): secondary text and disabled state on dark surfaces.
- **Mute Dark** (`{colors.mute-dark}` — `rgba(229,229,229,0.55)`): captions and metadata on dark canvas.
- **Card Borders** (`{colors.card-border-light}`, `{colors.card-border-dark}`): visible boundaries for cards against their matching light or dark canvases.

### Semantic
- **Warning** (`{colors.warning}` — `#c81b3a`): validation errors and destructive confirmation copy.
- **Link Light** (`{colors.link-light}` — `#0064b7`): inline body-prose anchor link on light canvas — same hex as `{colors.primary-pressed}`.
- **Link Dark** (`{colors.link-dark}` — `#53b1ff`): inline body-prose anchor link on dark canvas — a brightened blue for dark-mode legibility.

### Brand Gradient
- **PlayStation Plus Gold Gradient** — a horizontal three-stop gold gradient `{colors.ps-plus-gold-start}` (`#ffce21`) → `{colors.ps-plus-gold-mid}` (`#f5a623`) → `{colors.ps-plus-gold-end}` (`#ee8e00`) placed at the top of the PS Plus banner. Gold is reserved for this banner; the separate dark chapter gradient uses no gold.

## Typography

### Font Family
- **Roboto** is the distribution default for display and light headings at weight 300, with `Arial, sans-serif` fallback. [Google Fonts lists Roboto under OFL](https://github.com/google/fonts/blob/main/ofl/roboto/METADATA.pb).
- **Inter** is the distribution default for body, labels, links, and buttons at their token weights, with `system-ui, sans-serif` fallback. [Google Fonts lists Inter under OFL](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb).
- **PlayStation SST / SST** are source-reference faces. Use them only when the font files and intended usage rights are available.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 54px | 300 | 1.25 | -0.1px | Hero headline ("Discover all PS5 consoles and accessories") |
| `{typography.display-lg}` | 44px | 300 | 1.25 | 0.1px | Section headline ("Great PS4 & PS5 games out now or coming soon") |
| `{typography.display-md}` | 35px | 300 | 1.25 | 0 | Mid-section headline, game-page sub-hero |
| `{typography.heading-xl}` | 28px | 300 | 1.25 | 0.1px | "30 Years of PlayStation" callout, in-band sub-heading |
| `{typography.heading-lg}` | 22px | 300 | 1.25 | 0.1px | News card title, support category title |
| `{typography.heading-md}` | 18px | 600 | 1 | 0 | Card label, navigation menu heading, in-product strong title |
| `{typography.body-md}` | 18px | 400 | 1.5 | 0.1px | Body copy, paragraph text, support article body |
| `{typography.body-strong}` | 18px | 500 | 1.25 | 0.4px | Inline emphasis, primary nav link, button label (large) |
| `{typography.body-sm}` | 16px | 400 | 1.5 | 0 | Card description, secondary body |
| `{typography.caption-md}` | 14px | 400 | 1.5 | 0 | Footer link, metadata, sub-nav text |
| `{typography.caption-sm}` | 12px | 500 | 1.5 | 0 | Smallest utility text, badge label |
| `{typography.link-md}` | 18px | 400 | 1.5 | 0 | Inline body-prose anchor link |
| `{typography.button-lg}` | 18px | 700 | 1.25 | 0.45px | Primary CTA pill |
| `{typography.button-md}` | 14px | 700 | 1.25 | 0.324px | Compact pill, filter chip, secondary CTA |

### Principles
The hierarchy works on a 1.25-line-height ladder almost exclusively — even body sits at 1.5 instead of the typical 1.6 — which keeps long-form support pages tight and console showcases efficient. The weight contrast between display (300) and button (700) is dramatic: a single 18px chrome line might host a heavyweight CTA next to a feather-light 22px headline, giving the system its editorial gaming-magazine feel.

### Note on Font Substitutes
The YAML already specifies Roboto and Inter. Keep each token's weight and letter-spacing, then check wrapping and line breaks in the rendered layout. No metric-equivalence to the source-reference face is assumed.

## Layout

### Spacing System
- **Base unit:** 8px (with finer 4/12px steps for tight inline gaps).
- **Tokens (front matter):** `{spacing.xxs}` (4px) · `{spacing.xs}` (8px) · `{spacing.sm}` (12px) · `{spacing.md}` (16px) · `{spacing.lg}` (24px) · `{spacing.xl}` (32px) · `{spacing.xxl}` (48px) · `{spacing.section}` (96px).
- **Universal section rhythm:** every page in the set uses `{spacing.section}` (96px) as the vertical gap between major content blocks. Card grids use `{spacing.lg}` (24px) gutters; in-card padding sits at `{spacing.lg}` to `{spacing.xl}` depending on density.
- **Hero band padding:** 96px vertical / 48px horizontal — the largest spacing in the system, reserved for full-bleed surface chapters.

### Grid & Container
- **Max width:** ~1280px content area for body text on desktop with 24px gutters that expand to ~48px at ultrawide. Hero bands and game-tile rails go full-bleed with no max-width constraint on imagery.
- **Game tile carousel:** 4-up at desktop with horizontal scroll on the same row, collapsing to 3-up at 1024px and 2-up at 768px. Each tile uses 16:9 cover art at `{rounded.md}`.
- **Console showcase grid:** desktop 5-column thumbnail strip below the main hero render, collapsing to 3-up + horizontal scroll at tablet.
- **Support page:** desktop 2-column 30/70 split (sidebar nav + article body), collapsing to single-column with the sidebar promoted to a top accordion at mobile.
- **News strip:** 3-up card grid at desktop, 2-up at tablet, 1-up at mobile.

### Whitespace Philosophy
Whitespace is structural and band-defined. The 96px `{spacing.section}` between chapters reads as silence between trailer cuts — there's no decorative wash, no gradient transition, no mid-section divider. Inside a section, content is left-aligned in a tight column with the imagery breathing in the right 60-70% of the band. Paragraph text is comfortable at 1.5 line-height but column widths stay narrow (~520px at desktop) to keep long-form copy readable.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | No border, no shadow | Default for hero bands, footer, full-bleed sections — the dominant treatment |
| 1 — Divider or card border | `{colors.hairline-light}` / `{colors.hairline-dark}` for decorative rules; `{colors.card-border-light}` / `{colors.card-border-dark}` for card boundaries | Support rows, footer rules, cards |
| 2 — Soft active shadow | `0 4px 12px rgba(0,0,0,0.16)` | Active/pressed CTAs, lifted product card |
| 3 — Section gradient | Soft top-to-bottom darkening from `{colors.surface-dark-elevated}` to `{colors.canvas-dark}` | "ON PLAYSTATION" band — only place a gradient appears on chrome |

The system has effectively no resting shadow on cards; depth is built from surface-color contrast across band chapters. Cards lift only on press.

### Decorative Depth
Depth comes from the alternating-band rhythm and from the imagery itself:
- **Console product photography** — DualSense controller and PS5 console renders shot on neutral white with crisp edge lighting, full-bleed inside the light-canvas band.
- **Game key art** — full-bleed cinematic stills (Marathon, the latest blockbuster releases) inside dark-canvas bands with title lockup overlaid in the lower-left.
- **PS Plus tier banner** — a subtle horizontal gold gradient (`{colors.ps-plus-gold-start}` → `{colors.ps-plus-gold-end}`) sits as the only chrome gradient in the system, anchoring the "Discover PlayStation Plus" CTA.
- **"ON PLAYSTATION" gradient band** — top-to-bottom deepening from `{colors.surface-dark-elevated}` (`#121314`) to `{colors.canvas-dark}` (`#000000`) creates a cinematic dimming effect under the anniversary callout.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | Hero bands, primary nav, footer, sub-nav, support article body — every full-bleed structural surface |
| `{rounded.sm}` | 4px | Text inputs, support search field utilities |
| `{rounded.md}` | 8px | Game tiles, product cards, feature cards, PS Plus banner |
| `{rounded.lg}` | 16px | Rare large container with extra-soft corners (e.g., dialog cards) |
| `{rounded.full}` | 9999px | Every CTA pill (primary / commerce / secondary), filter chips, pagination dots, carousel paddles |

The radius vocabulary works on a 4 / 8 / pill rhythm for chrome with structural surfaces staying flat at 0px.

### Photography Geometry
- **Hero console render:** large centered console + DualSense composition on white, ~70% width of the band, with copy slot to the left.
- **Game tiles:** 16:9 key art at `{rounded.md}` (8px), 4-up rail at desktop with horizontal carousel.
- **Marathon game page hero:** full-bleed cinematic 16:9 still with the "MARATHON" wordmark in the lower-left at light weight, brand yellow `{colors.marathon-yellow}` accent on a few small UI tags.
- **News card thumbnails:** 16:9 imagery at `{rounded.md}` with a small text block below.
- **Avatar / brand icons:** 32–40px circles for sub-nav social row.

## Components

> **No hover states documented** per system policy. Each spec covers Default and Active/Pressed only.

### Buttons

**`button-primary`** — the universal PlayStation CTA
- Background `{colors.primary}` (PlayStation Blue), text `{colors.on-primary}`, type `{typography.button-lg}`, padding `12px 28px`, height ~48px, rounded `{rounded.full}`.
- Used for "Add to bag", "Sign up", "Learn more", "Subscribe" — every primary action across both light and dark canvases.
- Pressed state lives in `button-primary-pressed` — background drops to `{colors.primary-pressed}` (`#0064b7`).

**`button-commerce`** — orange store CTA
- Background `{colors.commerce}` (`#d53b00`), text `{colors.on-commerce}`, type `{typography.button-lg}`, padding `12px 28px`, height ~48px, rounded `{rounded.full}`.
- Reserved for "Buy now", "Pre-order", "Add to cart" — store actions only. The only warm color in the system.
- Pressed state lives in `button-commerce-pressed` — background drops to `{colors.commerce-pressed}`.

**`button-secondary-light`** — outline variant on light canvas
- Background transparent, text `{colors.ink}`, 1px solid `{colors.mute-light}` border, type `{typography.button-lg}`, padding `12px 28px`, height 48px, rounded `{rounded.full}`.
- Lower-emphasis CTA on white surfaces ("Learn more →", "Watch trailer").

**`button-secondary-dark`** — outline variant on dark canvas
- Background transparent, text `{colors.on-dark}`, 1px solid `{colors.on-dark-mute}` border, type `{typography.button-lg}`, padding `12px 28px`, height 48px, rounded `{rounded.full}`.
- Same role as the light variant but inverted for use on `{colors.canvas-dark}` hero bands.

**`button-disabled`**
- Background `{colors.surface-soft}`, text `{colors.ash-light}`, rounded `{rounded.full}` — flat soft gray.

### Filter & Tab Chips

**`filter-pill`** + **`filter-pill-active`**
- Default: background `{colors.surface-filter}` (translucent), text `{colors.ink}`, 1px `{colors.mute-light}` border, type `{typography.button-md}`, padding `8px 16px`, rounded `{rounded.full}`.
- Active: background flips to `{colors.canvas-light}` with a 2px `{colors.primary-active}` border. Check the selected state in the rendered filter strip.
- Used in the PS5 games filter strip ("All", "Coming Soon", "PlayStation VR2", "Recently Released").

### Inputs & Forms

**`text-input`** + **`text-input-focused`**
- Default: background `{colors.canvas-light}`, text `{colors.ink}`, 1px solid `{colors.mute-light}`, type `{typography.body-md}`, padding `12px 16px`, height 48px, rounded `{rounded.sm}` (4px).
- Focused: 2px solid `{colors.primary}` border. Verify its visibility beside adjacent controls in the rendered form.

**`support-search-bar`** — the support-page signature search field
- Background `{colors.canvas-light}`, text `{colors.ink}`, 1px `{colors.mute-light}` border, type `{typography.body-md}`, padding `12px 24px`, height 56px, rounded `{rounded.full}`.
- Sits at the top of the support page hero with a magnifier icon at the left edge and "Search the support center" placeholder.

### Cards & Containers

**`product-card`** — light-canvas product/feature card
- Container: background `{colors.surface-card}` (`#f5f7fa`), 1px solid `{colors.card-border-light}`, padding `{spacing.lg}` (24px), rounded `{rounded.md}` (8px).
- Used for the "PlayStation Store" sale callout, news cards, and PS Plus tier comparison cards on light canvas.

**`product-card-dark`** — dark-canvas product card
- Container: background `{colors.surface-dark-card}` (`#181818`), 1px solid `{colors.card-border-dark}`, padding `{spacing.lg}`, rounded `{rounded.md}`.
- Used for game-detail cards and dark-canvas feature panels.

**`game-tile`** — game/console thumbnail tile
- Container: background `{colors.surface-dark-elevated}`, padding 0, rounded `{rounded.md}`.
- Layout: 16:9 cover art at full bleed inside the radius, with title + platform tag overlaid at the bottom-left in `{typography.body-sm}`. Check text contrast against every final crop and add an opaque backing if needed.
- Used in the "Great PS4 & PS5 games" rail and the PS5 games listing grid.

**`feature-card`** — light-canvas marketing card
- Container: background `{colors.canvas-light}`, 1px solid `{colors.card-border-light}`, padding `{spacing.xl}` (32px), rounded `{rounded.md}`.
- Used for the "PlayStation Store" hero card and similar feature panels with a small product icon, title, body, and CTA.

**`hero-band-blue`** — the PlayStation Blue full-bleed band
- Background `{colors.primary}`, text `{colors.on-primary}` in `{typography.display-md}`, padding `96px 48px`, rounded `{rounded.none}`.
- The Marathon launch CTA strip and the footer surface use this band. The band's defining purpose is "this is the action moment of the page."

**`hero-band-dark`** — full-bleed dark hero
- Background `{colors.canvas-dark}` (with optional gradient end at `{colors.surface-dark-elevated}`), text `{colors.on-dark}` in `{typography.display-xl}`, padding `96px 48px`, rounded `{rounded.none}`.
- The home-page hero, the game-detail page hero, and the "ON PLAYSTATION" anniversary band.

**`hero-band-light`** — full-bleed white hero
- Background `{colors.canvas-light}`, text `{colors.ink}` in `{typography.display-xl}`, padding `96px 48px`, rounded `{rounded.none}`.
- The console showcase band ("Discover all PS5 consoles and accessories") and the support page top.

**`ps-plus-banner`** — PlayStation Plus tier callout
- Background `{colors.surface-dark-elevated}` with the YAML's three-stop gold accent gradient across the top, text `{colors.on-dark}` in `{typography.heading-xl}`, padding `48px 32px`, rounded `{rounded.md}`. Use it only with current PlayStation Plus art and rights.
- The "Discover PlayStation Plus" full-width banner on the home page.

**`carousel-paddle`** — circular carousel control
- Background `{colors.surface-dark-elevated}`, icon `{colors.on-dark}`, 1px `{colors.on-dark-mute}` border, rounded `{rounded.full}`, size 48px. Check its visibility against each game image.
- Anchored to the left/right edge of the game tile carousel.

**`pagination-dot`** + **`pagination-dot-active`**
- 8px circle at `{rounded.full}`. Default fill `{colors.mute-light}` on dark; active fill `{colors.on-dark}`. Verify the state contrast in the rendered carousel.
- Carousel position indicator below the game tile rail.

### Inline

**`badge-info`** — small info tag
- Background `{colors.primary}`, text `{colors.on-primary}` in `{typography.caption-sm}`, padding `4px 10px`, rounded `{rounded.full}`.
- "New", "Pre-order", and "Coming Soon" labels may overlay game tiles when current product data supports each status; check the full badge boundary against every image crop.

**`link-inline`** — body-prose anchor link
- `{components.link-inline}` uses underlined `{colors.link-light}` text on light canvas; `{components.link-inline-on-dark}` uses underlined `{colors.link-dark}` on dark canvas.

### Navigation

**`primary-nav`**
- Background `{colors.canvas-dark}`, text `{colors.on-dark}`, height ~48px, type `{typography.body-strong}`, rounded `{rounded.none}`.
- Layout reference (desktop): logo at left, centered nav, utility controls at right. Verify current labels, available features, and logo rights before publication.

**`sub-nav`** — secondary nav strip
- Background `{colors.canvas-dark}`, text `{colors.on-dark}` in `{typography.caption-md}`, height ~40px, rounded `{rounded.none}`.
- Sits directly below the primary nav on PS5 games / single game / PS Plus pages with section-specific anchor links.

**Top Nav (Mobile)**
- Hamburger menu icon at left, P-logo at center, search + cart icons at right. Primary nav collapses into a full-screen dark drawer that slides from the left.

### Footer

**`footer-section`**
- Background `{colors.primary}` (PlayStation Blue), text `{colors.on-primary}` in `{typography.caption-md}`, padding `{spacing.xxl}` (48px) vertical.
- Layout reference: authorized wordmark at top-left, multi-column link grid, terms and privacy text at the bottom. Verify current labels and destinations before publication.
- The footer's blue surface is the system's "we're done — return to the brand" anchor.

### Support-page-specific

**`support-row`** — support article-list row
- Background `{colors.canvas-light}`, text `{colors.ink}` in `{typography.body-md}`, padding `16px 0`, with a 1px `{colors.hairline-light}` bottom rule.
- Used for FAQ / category-listing rows on the support page with a small chevron-right icon at the right edge.

## Do's and Don'ts

### Do
- Reserve `{colors.primary}` (PlayStation Blue) for primary CTAs and the footer surface only. The blue band is precious — at most one full-bleed blue band per page.
- Reserve `{colors.commerce}` (orange) for store/buy/pre-order CTAs only. It is never used on marketing chrome or hero pills.
- Use the distribution default Roboto at weight 300 for display headings (54 / 44 / 35 / 28 / 22); use PlayStation SST only with the necessary font rights.
- Stack content sections at `{spacing.section}` (96px) rhythm with the next band's surface color taking over the page edge-to-edge — no decorative dividers between bands.
- Use `{rounded.full}` (9999px) on every CTA pill and `{rounded.md}` (8px) on every product card. The two-radius vocabulary is the entire shape system aside from inputs.
- Pair authorized game art and console renders with dark or light bands; check every image crop and any overlaid text for contrast.
- Use `{components.ps-plus-banner}` with the gold gradient exclusively for the PlayStation Plus tier callout — never decorate other components with the gold.

### Don't
- Don't introduce drop shadows on resting cards. The system is flat-on-canvas; cards lift only on press.
- Don't replace `{colors.primary}` with another shade of blue. The brand blue is precise — `#0070d1` for default and `#0064b7` for pressed.
- Don't use `{colors.commerce}` (orange) on marketing/hero CTAs. It's reserved exclusively for store actions.
- Keep Inter as the distribution body font. Use a source-reference PlayStation SST face only with the necessary rights and recheck line breaks.
- Don't soften pill geometry. CTAs are always `{rounded.full}` — no medium-radius buttons.
- Don't use the gold PS Plus gradient on anything that isn't the PS Plus banner. It is a tier-specific brand asset.
- Don't put a gradient on chrome. The only allowed gradient is the gold PS Plus accent and the soft top-to-bottom darkening of the "ON PLAYSTATION" band.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| ultrawide | 1920px+ | Hero band stays at content max-width 1280px; outer gutters grow to ~80px |
| desktop-large | 1440px | Default desktop — 4-up game tile carousel, full primary nav |
| desktop | 1280px | Same layout with narrower outer gutters |
| desktop-small | 1024px | Game tile rail collapses to 3-up; sub-nav remains horizontal |
| tablet | 768px | Game tiles → 2-up; primary nav becomes hamburger drawer |
| mobile | 480px | Single-column everything; hero `{typography.display-xl}` scales 54px → ~32px |
| mobile-narrow | 320px | Section padding tightens to 32px; hero further scales to ~28px |

### Touch Targets
The primary and commerce buttons specify 48px height, text input 48px, support search bar 56px, and carousel paddle 48px diameter. Filter pills have padding without an explicit minimum height. Measure rendered hit areas, including any additional padding, before claiming target-size conformance.

### Collapsing Strategy
- **Primary nav:** desktop horizontal cluster → tablet hamburger drawer at 768px. The right-cluster icons (search, cart, account) stay visible at every breakpoint.
- **Sub-nav:** desktop horizontal anchor row → tablet horizontal scroll → mobile select dropdown.
- **Game tile carousel:** 4-up → 3-up → 2-up at 1024 and 768px; carousel paddles stay visible at every desktop breakpoint, hide on mobile in favor of touch-swipe.
- **Hero bands:** stay full-bleed at every breakpoint; only the internal content column reflows from 2-column (text-left + image-right) to single-column (text above image).
- **Console showcase:** desktop 5-up thumbnail strip → tablet 3-up + horizontal scroll → mobile 1-up with paddle.
- **Support page:** desktop 30/70 split (sidebar + body) → tablet sidebar promoted to top accordion → mobile fully collapsed accordion.
- **Section padding:** `{spacing.section}` (96px) desktop → 64px tablet → 48px mobile.
- **Hero headline:** `{typography.display-xl}` (54px) at desktop, scaling 44px / 32px / 28px down the breakpoint stack.

### Image Behavior
- Hero imagery (console renders, game key art) uses art-direction crops on mobile so the central subject stays centered when the band collapses to single-column.
- Game tile cover art preserves 16:9 ratio at every breakpoint; only the column count changes.
- Console showcase thumbnails maintain their natural aspect (~1:1 product render) across breakpoints.
- All non-critical imagery is lazy-loaded as the user scrolls into the next chapter.

## Iteration Guide

1. Focus on ONE component at a time. Pull its YAML entry and verify every property resolves.
2. Reference component names and tokens directly (`{colors.primary}`, `{components.button-primary-pressed}`, `{rounded.full}`) — do not paraphrase.
3. Run `npx --yes -p "@google/design.md@0.4.0" designmd lint DESIGN.md` after edits — `broken-ref`, `contrast-ratio`, and `orphaned-tokens` warnings flag issues automatically.
4. Add new variants as separate component entries (`-pressed`, `-disabled`) — do not bury them inside prose.
5. Default body to `{typography.body-md}` (18px / 400 / 1.5); reach for `{typography.display-xl}` strictly for the page-top hero headline; use `{typography.body-strong}` for primary nav links.
6. Keep `{colors.primary}` scarce per viewport — at most one full-bleed PlayStation Blue band per page.
7. When introducing a new component, ask whether it can be expressed with the existing pill + 8px-radius card + full-bleed-band vocabulary before adding new tokens. The system's strength is that it almost never needs new ones.

## Known Gaps

- **Mobile screenshots not captured** — responsive behavior synthesizes PlayStation's known mobile pattern (hamburger drawer, single-column band reflow, hero downscale) from desktop evidence and the breakpoint stack.
- **Hover states not documented** by system policy.
- **Sign-in / authentication chrome** (login modal, account dashboard, profile pages) not in the captured pages.
- **PlayStation Store** in-store browsing surfaces (PDP / cart / checkout) are not in the captured set — those use a more dense data-table layout that this document does not describe.
- **Game-page-specific theming** — the `/marathon/` page uses `{colors.marathon-yellow}` as a chapter accent. Other game pages may pull in their own per-title brand colors that vary outside the documented system.
- **Form validation states** (success / error inline messages) not present in the captured surfaces beyond the `{colors.warning}` color token.
- **Current pages and asset rights not checked** — validate campaign dates, game art, console imagery, wordmarks, product availability, prices, and destinations before publication.
