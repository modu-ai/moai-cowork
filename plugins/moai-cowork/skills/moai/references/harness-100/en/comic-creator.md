# Comic Creator (07-comic-creator)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce comics — from storyboarding through dialogue, image generation, and editing — for formats ranging from 4-panel strips to long-form series.

## Expert Roles

- **Comic Editor**: Comic editor. Handles speech bubble placement, sound effect layering, final page layout, and reading flow optimization. Creates detailed editing specifications that can be directly applied in design/editing tools.
  - Speech Bubble Placement: Position bubbles to match reading order while maintaining visual balance within panels
  - Sound Effect Layering: Specify the size, angle, font style, and position of sound effects
  - Page Layout Finalization: Finalize panel borders, gutters (inter-panel spacing), and page margins
  - Reading Flow Optimization: Verify that gaze direction flows naturally left-to-right, top-to-bottom
  - Final Editing Specification: Write detailed specifications that can be directly applied in design/editing tools

- **Dialogue Writer**: Comic dialogue writer. Writes dialogue in each character's unique voice, and produces dialogue scripts including sound effects (onomatopoeia), narration, and speech bubble instructions.
  - Character Dialogue: Write dialogue in a unique voice matching each character's personality and background
  - Sound Effects Design: Place onomatopoeia and mimetic words appropriate to each scene
  - Narration: Write narration for time lapses, scene transitions, and inner monologues
  - Speech Bubble Type Assignment: Distinguish between normal, thought, shout, whisper, and other bubble types
  - Dialogue Length Control: Maintain appropriate dialogue length relative to panel size

- **Image Generator**: Comic image generator. Uses AI image generation (Gemini) to produce panel images based on the storyboard. Maintains character consistency and art style uniformity.
  - Character Visual Establishment: Design prompts that maintain consistent appearance based on character sheets
  - Panel Image Generation: Generate images via Gemini matching each panel's composition, angle, background, and emotion
  - Art Style Uniformity: Keep the art style consistent throughout (manga, American comics, webtoon, etc.)
  - Background Management: Maintain visual consistency for recurring backgrounds (school, home, office, etc.)
  - Emotion Visualization: Incorporate comic-specific emotion cues (sweat drops, anger marks, sparkles, etc.) into prompts

- **Quality Reviewer**: Comic quality reviewer (QA). Cross-validates consistency across story, dialogue, images, and editing. Identifies narrative continuity issues, character inconsistencies, and reading flow problems.
  - Narrative Continuity: Does the story flow logically from panel to panel?
  - Character Consistency: Are appearance, speech patterns, and personality consistent throughout?
  - Dialogue-Image Alignment: Does the dialogue match the visual situation and emotion?
  - Reading Flow Verification: Are gaze direction, bubble order, and panel transitions natural?
  - Genre Appropriateness: Does the work faithfully follow the conventions of its genre?

- **Storyboarder**: Comic storyboarder. Develops synopses, breaks scenes into panels, designs panel layouts, and creates storyboards. Designs visual narrative structures specific to comics, from 4-panel strips to long-form series.
  - Synopsis Development: Build a narrative structure (setup-development-twist-punchline, 3-act structure) from the user's idea
  - Scene Breakdown: Split the story into scenes and determine each scene's key visual moment
  - Panel Layout Design: Decide panels per page, panel size ratios, and gaze flow direction
  - Storyboard Creation: Detail each panel's composition (angle, shot size), character positioning, background, and emotional tone
  - Pacing Control: Design tension-release rhythms, page-turn hooks, and cliffhanger placement

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Topic/Story Idea**: The story to turn into a comic
   - **Format**: 4-panel / Short-form (8-16 pages) / Long-form (chapter-based) / Webtoon
   - **Genre**: Comedy, drama, fantasy, slice-of-life, action, etc.
   - **Art Style** (optional): Manga, American comics, webtoon style, etc.
   - **Existing Files** (optional): Scenario, character settings, etc.
2. Create `_workspace/` directory and `_workspace/panels/` subdirectory
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, copy to `_workspace/` and skip corresponding phase
5. Determine execution mode based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Storyboard | storyboarder | None | `_workspace/01_storyboard.md` |
| 2a | Dialogue writing | dialogue-writer | Task 1 | `_workspace/02_dialogue.md` |
| 2b | Panel image generation | image-generator | Task 1 | `_workspace/03_image_prompts.md`, `_workspace/panels/` |
| 3 | Page editing spec | comic-editor | Tasks 1, 2a, 2b | `_workspace/04_layout.md` |
| 4 | Quality review | quality-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (dialogue) and 2b (images) run **in parallel**. Both depend only on Task 1 (storyboard).

**Inter-agent communication flow:**
- storyboarder completes -> delivers per-panel situations and emotions to dialogue-writer; character sheets and compositions to image-generator
- dialogue-writer completes -> delivers SFX style to image-generator; bubble types and reading order to comic-editor
- image-generator completes -> delivers image files and blank area info to comic-editor
- comic-editor completes -> delivers editing spec to quality-reviewer
- quality-reviewer cross-validates all deliverables. On RED Must Fix findings, sends revision requests -> rework -> re-validate (up to 2 cycles)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all RED Must Fix items have been addressed
3. Report final summary to user

## Deliverables

- `00_input.md` — Organized user input
- `01_storyboard.md` — Storyboard
- `02_dialogue.md` — Dialogue script
- `03_image_prompts.md` — Image generation prompts and results
- `04_layout.md` — Page layout / editing specification
- `05_review_report.md` — Review report
- `panels/` — Generated panel images

## Extension Skills

- **character-design-system**: A character design system skill used by the storyboarder and image-generator agents. Provides character sheet design, silhouette testing, expression charts, and AI image generation consistency methodologies. Used for 'character design,' 'character sheet,' 'visual consistency,' 'character setup,' and related topics.
- **panel-composition**: A panel composition skill used by the storyboarder and image-generator agents. Provides comic panel layout patterns, camera angles, gaze flow design, and page rhythm methodologies. Used for 'panel layout,' 'composition,' 'storyboard design,' 'gaze flow,' and related topics.
- **visual-narrative**: A visual narrative skill used by the dialogue-writer and comic-editor agents. Provides speech bubble systems, sound effect typography, Show-Don't-Tell principles, and visual metaphor techniques. Used for 'speech bubbles,' 'sound effects,' 'visual storytelling,' 'comic direction,' and related topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Image generation failure | Proceed with text prompts only; user can retry with the prompts |
| Character consistency breaks | Strengthen character descriptions in prompts and regenerate (up to 2 times) |
| Agent failure | Retry once -> if still failing, proceed without that deliverable; note in review report |
| RED found in review | Send revision request -> rework -> re-validate (up to 2 cycles) |
| Content rejected as inappropriate | Modify prompt and retry; note in report |
