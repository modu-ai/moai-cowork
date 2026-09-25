---
version: alpha
name: TheVerge-design-analysis
description: 'Historical 2022 Verge editorial design reference with a dark canvas, mint and violet accents, and color-block story tiles. Current site supports Light, System, and Dark; verify theme, assets, and portable fonts before reuse.'
colors:
  primary: "#3cffd0"
  primary-active: "#21c9a0"
  ink: "#ffffff"
  body: "#ababab"
  muted: "#e9e9e9"
  hairline: "#8c8c8c"
  canvas: "#131313"
  surface-soft: "#2d2d2d"
  surface-card: "#2d2d2d"
  on-primary: "#131313"
---

# Design System Inspired by The Verge

> **Source and portability boundary:** [Vox Media announced the site redesign in 2022](https://www.voxmedia.com/2022/9/13/23350983/the-verge-launches-an-ambitious-new-site). The [current homepage](https://www.theverge.com/) exposes Light, System, and Dark themes; this file's dark palette is one inspired mode, not a sitewide mandate. Manuka and Poly Sans are source-font references, not fonts distributed by this profile. Use licensed or OFL alternatives in deployable work, and verify current article content, photos, logos, subscriptions, and layout before publication.

## 1. Visual Theme & Atmosphere

This is an interpretation of the [2022 Verge redesign](https://www.voxmedia.com/2022/9/13/23350983/the-verge-launches-an-ambitious-new-site), which introduced a Storystream news feed. It uses a near-black canvas, mint and violet accents, large condensed headlines, and colorful story tiles. These are historical design references; the current site has Light, System, and Dark theme choices.

Use current, licensed editorial imagery and article data. A logo or wordmark is a protected asset, so obtain an approved file and do not recreate it with a substitute font. Check each tile's text contrast, focus state, and responsive crop in the rendered page.

**Reference characteristics:**
- Near-black `#131313` for the dark variant; define a separate verified light palette when a light theme is required.
- Mint `#3cffd0` and ultraviolet `#5200ff` as accents, with text colors chosen per actual surface.
- Storystream-style vertical feed and saturated story tiles as optional historical patterns.
- Large condensed display type as an interpretation, with readable line heights and licensed fonts.

## 2. Color Palette & Roles

### Primary (Brand Hazards)
- **Jelly Mint** (`#3cffd0`): The Verge's signature acid-mint accent. Used as CTA button fill, link underlines, active tab borders, and high-attention story-tile backgrounds. Treat it as the visual equivalent of neon safety paint — applied sparingly to the most important element on screen.
- **Verge Ultraviolet** (`#5200ff`): A historical accent for color-block tiles. Use solid fill with white text only after checking the actual rendered contrast; its outline alone is too faint on the dark canvas.

### Secondary & Accent
- **Console Mint Border** (`#309875`): A historical darker mint; use the visible `#8c8c8c` boundary for required controls on the dark canvas.
- **Historical Link Blue** (`#3860be`): Source reference only; it measures 3.17:1 on the dark canvas. Use `#a9c4ff` for portable dark-surface link hover and choose a separate dark hover for light tiles.
- **Focus Cyan** (`#1eaedb`): Visible focus treatment on dark surfaces; pair cyan fill with dark text and a distinct outline.
- **Purple Rule** (`#3d00bf`): Decorative historical timeline rail only; reading order and state must not depend on it.

### Surface & Background
- **Canvas Black** (`#131313`): The base of this inspired dark variant; the current site also offers light and system themes.
- **Surface Slate** (`#2d2d2d`): Secondary card background, used when a story tile doesn't need to be a saturated color block.
- **Image Frame** (`#313131`): Decorative dark image edge; use a stronger boundary if the image frame must be perceivable.
- **Hazard White** (`#ffffff`): Used as story-tile fill, button border, and primary text. When white appears as a large block, it's an editorial decision — a "spotlight" on that tile.
- **Absolute Black** (`#000000`): Text option on light accent tiles after a contrast check.

### Neutrals & Text
- **Primary Text** (`#ffffff`): Headlines and display text on the canvas.
- **Secondary Text** (`#ababab`): Required bylines, timestamps, and photo credits on dark surfaces; verify contrast on each tile.
- **Muted Text** (`#e9e9e9`): Button text on dark slate buttons. Slightly off-white to reduce screen glare.
- **Inverted Text** (`#131313`): Used only on accent tiles (mint, yellow, white) to keep contrast legible.

### Semantic & Accent
- **Focus Ring** (`#1eaedb`): Keyboard focus on dark surfaces; verify its actual outline and offset.
- **Overlay Black** (`rgba(0, 0, 0, 0.33)`): Subtle 1px ring used as the quiet shadow alternative on stacked cards.
- **Dim Gray** (`#8c8c8c`): Visible dark-surface control boundary in this portable variant; primary pressed buttons keep their own solid fill.

### Gradient System
The historical reference favors solid color blocks. This profile makes no claim that every current page or theme excludes gradients.

## 3. Typography Rules

### Source and portable fonts

A [Vox Media design-team account of the redesign](https://medium.com/vox-media-product-team/if-were-going-to-relaunch-the-verge-we-might-as-well-reinvent-the-whole-media-stack-d523ace2c3b1) names Manuka for special feature headlines, Poly Sans for article headlines and subheadings, and FK Roman for article body copy. Their distribution rights are not established by this profile. For deployable work, use [OFL Barlow Condensed](https://github.com/google/fonts/blob/main/ofl/barlowcondensed/METADATA.pb) for large display text, [OFL Inter](https://github.com/google/fonts/blob/main/ofl/inter/METADATA.pb) for UI and headlines, [OFL JetBrains Mono](https://github.com/google/fonts/blob/main/ofl/jetbrainsmono/METADATA.pb) for short labels, and [OFL Lora](https://github.com/google/fonts/blob/main/ofl/lora/METADATA.pb) for article prose and editorial serif. Include `system-ui, sans-serif`, `ui-monospace, monospace`, and `Georgia, serif` fallbacks as appropriate. These are explicit approximations, not the official brand faces.

| Role | Portable stack | Size | Weight | Line height | Use |
|---|---|---:|---:|---:|---|
| Display | Barlow Condensed, system-ui, sans-serif | up to 107px | 700 | 1.1 | Large headline only; use an approved logo file for the wordmark |
| Section headline | Inter, system-ui, sans-serif | 24–34px | 700 | 1.2 | Story titles |
| Article body | Lora, Georgia, serif | 16px | 400 | 1.6 | Long-form reading |
| Small body | Inter, system-ui, sans-serif | 14px | 400 | 1.5 | Captions and metadata where contrast allows |
| Label | JetBrains Mono, ui-monospace, monospace | 12–14px | 600 | 1.4 | Short category and time labels |
| Editorial serif | Lora, Georgia, serif | 16–20px | 400 | 1.5 | Optional pull quotes |

Avoid the original 0.80 display line height with substitute fonts. Check actual ascenders, mixed-script wrapping, zoom, and font loading on each target OS. Give all required metadata readable size and contrast rather than preserving the historical 10–11px samples verbatim.

## 4. Component Stylings

These are **inspired dark-theme patterns**, not a copy of the current site. Use approved article data, images, logos, and subscription wording. Check actual contrast and keyboard behavior after rendering.

### Buttons and links

- **Mint primary:** `#3cffd0` background with `#131313` text, a pill radius, and a measured target. A solid `#21c9a0` hover retains dark-text contrast; do not make the whole control translucent on press.
- **Slate secondary:** `#2d2d2d` background with `#e9e9e9` text. Keep a visible boundary if it sits on another slate surface.
- **Outlined mint:** dark background, `#3cffd0` text and border. A violet accent `#5200ff` is suitable as a fill with white text; its border alone measures only 2.48:1 on `#131313`, so use a lighter visible boundary there.
- **Focus:** use a distinct 2px solid outline with spacing from the control edge. A cyan `#1eaedb` fill needs dark text; verify focus separately from hover in the rendered UI.
- **Links:** keep an underline at rest. `#a9c4ff` may be used for hover on `#131313` (10.64:1); choose another tested color on light, mint, or violet tiles.

### Story tiles and controls

- **Storystream tile:** a historical feed pattern with a rounded dark or saturated card, category, headline, and timestamp. Use current approved story data. Choose text color per tile: dark on mint or white, white on violet or near-black. The tile border must remain visible without relying on a shadow.
- **Timeline rail:** a decorative vertical rule can connect items, but timestamp and reading order remain understandable without color or the rail.
- **Input:** dark `#131313` background, white label and value, visible `#8c8c8c` border, and a distinct mint focus ring. Use a text error message plus a visible error border; do not use violet alone to mean error.
- **Navigation:** use current approved logo artwork and live navigation names. The wordmark must not be rebuilt from a substitute headline font. Keep keyboard focus and active location visible in each theme.
- **Images:** use permitted editorial media with alt text and responsive crops. Check article-image rights, focal points, and contrast of any overlaid text. Lazy-load below-the-fold images only when it does not hide essential content.

## 5. Layout and Responsive Behavior

The historical feed mixes a dark canvas, colored tiles, and a timeline. Start with a flexible reading column and allow cards to reflow with content. The original document's long breakpoint list was an extraction snapshot, not a portable implementation contract. Test narrow and wide desktop windows, mobile widths, zoom, and long mixed-script headings.

Measure rendered control targets and spacing; padding values alone do not prove conformance. Keep required timestamps and bylines readable. Respect the current site's Light, System, and Dark choice: the colors in this profile define only the dark variant. A light variant needs its own background, text, border, link, hover, and focus pairs checked in the rendered interface.

## 6. Agent Prompt Guide

1. For a dark editorial story tile, use `#131313` or a verified accent fill, an approved headline and image, a readable timestamp, and text colors chosen for that tile. Preserve keyboard access and reading order.
2. For a large inspired headline, use Barlow Condensed 700 with at least 1.1 line height and check font loading, zoom, and mixed-script wrapping. Use an approved logo file for any Verge wordmark.
3. For a mint CTA, use `#3cffd0` with dark text, a visible focus outline, and a measured target. Confirm current subscription wording from the live site before publication.
4. For links, retain a persistent underline. Verify default, hover, and focus contrast on every light or dark tile; use `#a9c4ff` hover only on the near-black canvas.
5. Before delivery, confirm the current theme, story data, image and logo rights, layout, and all rendered states in the target app and OS.

## Known Gaps

- The 2022 redesign announcement establishes historical inspiration, not current CSS values, every breakpoint, or licensed reuse of artwork and fonts.
- The current site exposes theme choices, but this file supplies only an inspired dark palette. No light-mode token set has been measured here.
- Font loading, mixed-script wrapping, image and tile contrast, keyboard focus, target size, and Claude Cowork or ChatGPT Work behavior on macOS, Windows, and Linux have not been observed.
