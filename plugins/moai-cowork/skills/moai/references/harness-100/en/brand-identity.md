# Brand Identity (06-brand-identity)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to design brand identity from naming through slogans, tone and manner, and visual guidelines.

## Expert Roles

- **Brand Strategist**: Brand strategist. Conducts market analysis, competitive positioning, target persona development, brand archetype selection, and differentiation strategy.
  - Market Analysis: Analyze the brand landscape within the relevant industry or category
  - Competitive Positioning: Benchmark competitor brands' positioning, naming, and visual identity
  - Target Persona: Define the core customer's demographics, psychographics, and behavioral traits
  - Brand Archetype: Select the optimal archetype from the 12 brand archetypes
  - Differentiation Strategy: Deliver a clear answer to "Why should customers choose this brand?"

- **Copywriter**: Brand copywriter. Creates slogans, taglines, brand stories, and tone-and-manner guides.
  - Slogan Development: Write memorable slogans that distill the brand essence
  - Tagline Creation: Write sub-copy to accompany the brand name
  - Brand Story: Write the narrative of the brand's origin, mission, and values
  - Tone and Manner Guide: Define the brand's voice, expression principles, and Do/Don't rules
  - Core Message Framework: Design a hierarchical message structure for each customer touchpoint

- **Identity Reviewer**: Brand identity reviewer (QA). Cross-validates consistency across strategy, naming, verbal identity, and visual identity, and identifies brand coherence issues.
  - Strategy-Naming Alignment: Does the name reflect the brand essence and archetype?
  - Naming-Copy Alignment: Do the slogan and name harmonize rhythmically and semantically?
  - Verbal-Visual Alignment: Do the tone and manner and visual mood convey the same impression?
  - Overall Brand Experience: Does a consistent brand impression form across all touchpoints?
  - Practicality Review: Are the proposed elements usable in real business contexts?

- **Naming Specialist**: Brand naming specialist. Develops naming candidates based on brand strategy and reviews domain availability, trademark conflicts, and pronunciation ease.
  - Name Candidate Development: Generate diverse name candidates across multiple naming types based on brand strategy
  - Naming Type Diversification: Explore coined words, compound words, metaphors, acronyms, onomatopoeia, and more
  - Domain Availability Check: Verify key domains like .com, .io, etc. (using web search)
  - Trademark Conflict Review: Pre-screen for similarity with existing registered trademarks
  - Linguistic Validation: Evaluate pronunciation ease, negative meanings (multilingual), and memorability

- **Visual Director**: Visual director. Designs the brand color system, typography, logo concepts, and visual guidelines.
  - Color System: Primary/secondary/neutral color palette + HEX/RGB codes
  - Typography: Select headline/body/caption typefaces + define usage rules
  - Logo Concept: Design symbol mark/wordmark/combination mark concepts + attempt image generation
  - Image Style: Style guide for photos/illustrations/icons
  - Layout Principles: Grid system, spacing, and visual hierarchy guide

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Business Domain**: What product/service?
   - **Target Customer** (optional): Core customer segment
   - **Competitors** (optional): Brands to benchmark
   - **Brand Direction** (optional): Desired image, keywords
   - **Existing Elements** (optional): Already-finalized brand name, colors, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Brand strategy | brand-strategist | None | `_workspace/01_brand_strategy.md` |
| 2 | Naming development | naming-specialist | Task 1 | `_workspace/02_naming_candidates.md` |
| 3a | Verbal identity | copywriter | Tasks 1, 2 | `_workspace/03_verbal_identity.md` |
| 3b | Visual identity | visual-director | Tasks 1, 2 | `_workspace/04_visual_identity.md` |
| 4 | Identity review | identity-reviewer | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (verbal) and 3b (visual) run **in parallel**. Both depend on Task 2 (naming), so they can start simultaneously once naming is complete.

**Inter-agent communication flow:**
- brand-strategist completes -> delivers essence, archetype, and competitive analysis to naming-specialist; mission/vision/target to copywriter; archetype and positioning to visual-director
- naming-specialist completes -> delivers TOP 5 names + meanings to copywriter; visual characteristics of names to visual-director
- copywriter <-> visual-director: coordinate tone and manner with visual mood for consistency
- reviewer cross-validates all deliverables. On RED Must Fix findings, sends revision requests to the relevant agent -> rework -> re-validate (up to 2 cycles)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Brand strategy — `01_brand_strategy.md`
   - Naming candidates — `02_naming_candidates.md`
   - Verbal identity — `03_verbal_identity.md`
   - Visual identity — `04_visual_identity.md`
   - Review report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_brand_strategy.md` — Brand strategy report
- `02_naming_candidates.md` — Naming candidates
- `03_verbal_identity.md` — Verbal identity (slogans, tone and manner)
- `04_visual_identity.md` — Visual identity (color, typography, logo)
- `05_review_report.md` — Review report

## Extension Skills

- **brand-archetype**: A brand archetype skill used by the brand-strategist and copywriter agents. Provides Jungian 12-archetype-based brand personality design, tone-and-voice mapping, and storytelling frameworks. Used for 'brand personality,' 'archetypes,' 'tone and voice,' 'brand story,' and related topics.
- **color-psychology**: A color psychology skill used by the visual-director agent. Provides color-emotion mapping, industry-specific color strategies, accessibility-based palette design, and color system construction methodologies. Used for 'color palette,' 'color strategy,' 'color psychology,' 'brand colors,' and related topics.
- **naming-methodology**: A brand naming methodology skill used by the naming-specialist agent. Provides linguistic analysis, 12 naming techniques, domain/trademark pre-verification, and global suitability evaluation. Used for 'brand naming,' 'name creation,' 'trademark review,' 'domains,' and related topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Strategist works from general knowledge; note "Real-time market data not reflected" |
| Domain/trademark verification unavailable | Mark as "[Verification Needed]"; recommend user verify directly |
| Image generation failure | Proceed with text concepts + prompts only; user can retry |
| Agent failure | Retry once -> if still failing, proceed without that deliverable; note the gap in the review report |
| RED found in review | Send revision request to relevant agent -> rework -> re-validate (up to 2 cycles) |
