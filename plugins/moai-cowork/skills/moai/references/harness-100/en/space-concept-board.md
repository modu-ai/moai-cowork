# Space Concept Board (77-space-concept-board)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to generate style analysis, moodboard, color palette, furniture/accessory list, budget sheet, and shopping guide for an interior space concept board.

## Expert Roles
- **Budget Manager**: Budget Manager
  - Calculate the budget based on the item curator's list (`_workspace/03_item_list.md`)
  - Allocate realistically relative to the user's total budget; specify reduction priorities when budget is exceeded
  - Reflect local market pricing structures (shipping fees, installation fees)
  - Include seasonal discount information: off-season periods, furniture expos, Black Friday, etc.
  - Research the latest prices and promotions via web search
  - **From Style Analyst**: Receive budget range, rental/owned status, and renovation scope
  - **From Moodboard Designer**: Receive recommended material and brand information
  - **From Item Curator**: Receive the full item list and price ranges
  - **To Concept Reviewer**: Deliver the full budget sheet + shopping guide
  - User budget not specified: Present average budgets by space type (studio: $2,000, living room: $5,000, full home: $15,000)
  - Price information unavailable for an item: Apply category average pricing, mark as "estimated price"
  - Budget exceeded by 150% or more: Present 2 reduction plans (Plan A: essentials only, Plan B: phased approach)

- **Concept Reviewer**: Concept Reviewer
  - **Cross-compare all deliverables**. Identify issues in inter-file relationships, not individual files
  - **Evaluate from the resident's perspective**. "Would daily life in this space be satisfying?"
  - Provide **specific revision suggestions** when issues are found
  - Classify severity into 3 levels: Critical (must fix) / Recommended / Informational
  - [ ] Are the recommended style's key visual elements reflected in the color palette?
  - [ ] Does the material board align with the style characteristics?
  - [ ] Has color correction been applied for the lighting conditions?
  - [ ] Are selected furniture colors within the color palette range?
  - [ ] Do materials (fabric/wood/metal) match the material board?
  - [ ] Does the lighting color temperature match the moodboard atmosphere?
  - [ ] Are furniture dimensions appropriate for the space area (no oversizing or undersizing)?
  - [ ] Is the main traffic path (60cm+ minimum) maintained?
  - [ ] Are storage needs met?
  - [ ] Does the total stay within the budget?
  - [ ] Are prices realistic?
  - [ ] Are shipping and installation fees accounted for?
  - [ ] Is the priority strategy reasonable?
  - **From all team members**: Receive all deliverables
  - **To individual team members**: Send specific revision requests for their deliverables via SendMessage
  - When critical issues are found: Immediately request revisions from the responsible team member, then re-verify the corrected results
  - When all verification is complete: Generate the final integrated report

- **Item Curator**: Item Curator
  - Select products based on the color palette and materials from the moodboard (`_workspace/02_moodboard.md`)
  - Always verify sizes are appropriate for the space area; avoid oversized or undersized furniture placement
  - Prioritize products that are actually available for purchase (domestic brands, international brands with local shipping)
  - Balance functionality and aesthetics: evaluate storage capacity, durability, and ease of maintenance
  - Use web search (WebSearch/WebFetch) to research actual prices and purchase channels
  - **From Style Analyst**: Receive spatial conditions, constraints, and style direction
  - **From Moodboard Designer**: Receive color palette, material board, and room-by-room atmosphere
  - **To Budget Manager**: Deliver the full item list and price ranges
  - **To Concept Reviewer**: Deliver the full furniture/accessory list
  - Price cannot be confirmed via web search: Use category average price estimates, mark as "price unconfirmed"
  - Recommended product is out of stock or discontinued: Prioritize presenting similar alternatives
  - No space dimensions provided: Use a standard apartment living room (approx. 4.5m x 3.5m) as the default layout basis

- **Moodboard Designer**: Moodboard Designer
  - Always read the style analyst's report (`_workspace/01_style_analysis.md`) before starting work
  - Specify all colors with HEX codes; do not rely solely on vague color names like "beige tones"
  - Reflect the characteristics of typical residential environments: standard flooring, white walls, built-in HVAC, etc.
  - Adjust the color palette for natural light conditions: reinforce warm tones for north-facing rooms, allow cooler tones for south-facing rooms
  - **From Style Analyst**: Receive recommended styles, key descriptors, and references
  - **To Item Curator**: Deliver color palette, material board, and room-by-room atmosphere guide
  - **To Budget Manager**: Deliver recommended materials and brand information
  - **To Concept Reviewer**: Deliver the full moodboard
  - No existing finish information: Assume standard apartment finishes (white walls, laminate flooring)
  - No lighting information: Design a neutral-tone color palette, note "adjust when lighting conditions are confirmed"

- **Style Analyst**: Style Analyst
  - Actively use web search (WebSearch/WebFetch) to gather the latest interior trends and real renovation case studies
  - Define styles through concrete visual elements (materials, colors, shapes, textures), not abstract style names
  - Include design strategies to overcome spatial drawbacks (small area, poor lighting, columns)
  - Recommend realistic styles considering the user's budget range
  - **To Moodboard Designer**: Deliver recommended styles, key descriptors, and reference examples
  - **To Item Curator**: Deliver spatial conditions, constraint strategies, and style direction
  - **To Budget Manager**: Deliver the user's budget range and renovation scope (rental/owned)
  - **To Concept Reviewer**: Deliver the full style analysis report
  - Insufficient space information: Apply defaults based on a standard apartment (approx. 84 sq m / 900 sq ft), note "estimated" in the report
  - Web search failure: Analyze using general interior knowledge and trends, note "search limitations" in the references section
  - Vague style preferences: Present 3 contrasting styles to guide the user's choice

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Space information**: Type (living room/bedroom/study/studio), area, structure
    - **Style preference** (optional): Preferred styles, reference images
    - **Budget** (optional): Total budget range
    - **Constraints** (optional): Rental/owned, renovation scope, pets/children
    - **Existing files** (optional): User-provided moodboard, furniture list, etc.
2. Create a `_workspace/` directory at the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request (see "Modes by Request Scale" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Style analysis | analyst | None | `_workspace/01_style_analysis.md` |
| 2 | Moodboard design | designer | Task 1 | `_workspace/02_moodboard.md` |
| 3 | Item curation | curator | Tasks 1, 2 | `_workspace/03_item_list.md` |
| 4 | Budget/shopping guide | budget | Tasks 1, 2, 3 | `_workspace/04_budget_shopping.md` |
| 5 | Concept review | reviewer | Tasks 1-4 | `_workspace/05_review_report.md` |

**Inter-team communication flow:**
- analyst complete -> Deliver recommended styles and references to designer, spatial conditions and constraints to curator, budget range and rental status to budget
- designer complete -> Deliver color palette and material board to curator, recommended materials and brands to budget
- curator complete -> Deliver full item list and price ranges to budget
- reviewer cross-verifies all deliverables. If critical issues are found, request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all critical issues from the review report have been addressed
3. Report the final summary to the user:
    - Style analysis — `01_style_analysis.md`
    - Moodboard + color palette — `02_moodboard.md`
    - Furniture/accessory list — `03_item_list.md`
    - Budget sheet + shopping guide — `04_budget_shopping.md`
    - Review report — `05_review_report.md`

## Deliverables
- `00_input.md` — Organized user input
- `01_style_analysis.md` — Style analysis report
- `02_moodboard.md` — Moodboard + color palette
- `03_item_list.md` — Furniture/accessory list + layout suggestions
- `04_budget_shopping.md` — Budget sheet + shopping guide
- `05_review_report.md` — Review report

## Extension Skills
- **Color Harmony Engine**: Color Harmony Engine — Interior Color Harmony Engine
- **Spatial Layout Guide**: Spatial Layout Guide

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient space information | Apply standard apartment (84 sq m) defaults, note "estimated" in the report |
| Web search failure | Work from general interior knowledge, note "data limitations" |
| Budget not specified | Suggest average budgets by space type, then proceed |
| Agent failure | Retry once -> If still failing, proceed without that deliverable, note the gap in the review report |
| Critical issue found in review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
