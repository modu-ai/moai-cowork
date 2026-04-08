# Presentation Designer (13)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to produce presentations: planning, storyboards, slides, and speaker notes.

## Expert Roles
- **deck-reviewer**: Deck reviewer (QA). Cross-validates consistency across story, information design, visuals, and speaker notes, identifying gaps, contradictions, and quality issues to provide feedback.
- **info-architect**: Information architect. Selects charts/graphs/diagrams for effective data visualization and structures complex information into audience-friendly formats.
- **presentation-coach**: Presentation coach. Provides slide-by-slide speaker notes, timing allocation, audience engagement strategies, anticipated Q&A responses, and rehearsal guides.
- **storyteller**: Presentation storyteller. Defines the presentation's core message based on audience analysis and designs the logical flow and emotion curve.
- **visual-designer**: Visual designer. Designs presentation slide layouts, colors, typography, and images, and produces markdown-based slide decks.

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **Presentation **: within
 - **Audience Information** (Selection): Audienceof background, expectations, decision-making authority
 - **Presentation whenbetween** (Selection): goal whenbetween
 - **Presentation Format** (Selection): //Suggestion//
 - ** File** (Selection): , 
2. `_workspace/` to in generate
3. Organize input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1 | Story Structure Design | storyteller | None | `_workspace/01_story_structure.md` |
| 2 | Information Design | info-architect | 1 | `_workspace/02_info_design.md` |
| 3 | Slide Deck production | visual-designer | 1, 2 | `_workspace/03_slide_deck.md` |
| 4a | Speaker notes Writing | presentation-coach | 1, 3 | `_workspace/04_speaker_notes.md` |
| 4b | Deck Review | deck-reviewer | 2, 3, 4a | `_workspace/05_review_report.md` |

**Inter-team communication flow:**
- storyteller complete -> info-architectTo Visualization Slide before, visual-designerTo before, coachTo before before
- info-architect complete -> visual-designerTo Chart Style·Color before, coachTo description before
- visual-designer complete -> coachTo Slide before Timing before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - Story Structure — `01_story_structure.md`
 - Information Design — `02_info_design.md`
 - Slide Deck — `03_slide_deck.md`
 - Speaker notes — `04_speaker_notes.md`
 - Review — `05_review_report.md`

## Deliverables
- `00_input.md` — Organized user input
- `01_story_structure.md` — Story structure/message map
- `02_info_design.md` — Information design/data visualization guide
- `03_slide_deck.md` — Slide deck (markdown-based)
- `04_speaker_notes.md` — Speaker notes/timing/Q&A
- `05_review_report.md` — Review report

## Extension Skills
- **data-visualization-guide**:  Visualization Chart Selection Guide, Information Hierarchy Design , number-Chart matrix info-architect Extended Skill. 'Chart Selection', ' Visualization', ' ', 'Information Design', 'Chart ', ' Storytelling' etc. Visualto expression . , Chart BI of .
- **slide-layout-patterns**:  Slide Layout Pattern Library. ///comparison/line etc. 20 Slide typeper optimal Layout, margins/grid , Color/ system visual-designer Extended Skill. 'Slide Layout', 'Slide Pattern', 'design system', 'grid', 'Typography', 'Color ' etc. Slide Visual Design when . , PPT/Keynote File of .

## Error Handling

| in type | Strategy |
|----------|------|
| Audience Information | Audience , in the report "Audience " when |
| Presentation whenbetween | 15(15Slide) application |
| | to Chart Structure Design, when |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
