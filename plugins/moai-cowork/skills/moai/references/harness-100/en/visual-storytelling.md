# Visual Storytelling (15)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to produce visual storytelling: story design, text writing, AI image generation, HTML layout, and integrated editing.

## Expert Roles
- **editorial-reviewer**: Editorial reviewer (QA). Cross-validates consistency across story, text, images, and layout, verifying the quality of narrative flow, emotional consistency, and visual unity.
- **essay-writer**: Essay writer. Writes the text portion of visual storytelling. Composes body text, captions, quotes, and dialogue in an emotional style that breathes in sync with images scene by scene.
- **image-prompter**: Image . Gemini Image utilization Visual Storyof Scenein Image generate. Scene between Visual Consistency Prompt design.
- **layout-builder**: Layout . Textand Image Integration HTML/CSS Visual Story page produce. Responsive , Typography, design.
- **story-architect**: Story Design. Visual Storytellingof Narrative Structure, Scene composition, visual-Text Balance design. Scene Imageand Textof combinationto of narrative photography .

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **Story **: Visual Storyof /
 - **type** (Selection): in/in/BrandStory/
 - **** (Selection): ///intense
 - **Scene ** (Selection): 
 - ** File** (Selection): Text, Image, 
2. `_workspace/` and `_workspace/images/` generate
3. Organize input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1 | Story Design | architect | None | `_workspace/01_story_blueprint.md` |
| 2a | Text writing | writer | 1 | `_workspace/02_essay_text.md` |
| 2b | Image Prompt· | prompter | 1 | `_workspace/03_image_prompts.md`, `images/` |
| 3 | HTML Layout | builder | 2a, 2b | `_workspace/04_layout.html` |
| 4 | Editing Review | reviewer | 2a, 2b, 3 | `_workspace/05_review_report.md` |

 2a(Text)and 2b(Image) **executed in parallel**. 1(Story Design)in ofto whenin when .

**Inter-team communication flow:**
- architect complete -> writerTo Sceneper Text Role·Emotion before, prompterTo Visual ·Image concept before, builderTo Scene Structure·ratio before
- writer complete -> prompterTo Text Emotionand Image before, builderTo Text placement Guide before
- prompter complete -> builderTo Image File··placement Information before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - Story lean — `01_story_blueprint.md`
 - in Text — `02_essay_text.md`
 - Image Prompt — `03_image_prompts.md`
 - HTML Layout — `04_layout.html`
 - Review — `05_review_report.md`
 - Image — `images/` 

## Deliverables
- `00_input.md` — Organized user input
- `01_story_blueprint.md` — Story blueprint
- `02_essay_text.md` — Essay body text
- `03_image_prompts.md` — Image prompt sheet
- `04_layout.html` — HTML layout
- `05_review_report.md` — Editorial review report
- `images/` — Generated images directory

## Extension Skills
- **image-prompt-engineering**: AI Image (Gemini/DALL-E/Midjourney) Prompt Writing Guide. compositionper Prompt , Style before, Consistency technique, Prompt Pattern image-prompter Extended Skill. 'Image Prompt', 'AI Image Style', 'Prompt Writing', 'composition ', 'Style Consistency', ' Prompt' etc. AI Image Prompt Optimization when . , Image candidates of .
- **narrative-structure-patterns**: Visual Storytellingof Narrative Structure Pattern Library. 3/5/hero's journey Structure, Emotion Curve Design, Scene before technique, Text-Image Balance Formula story-architect Extended Skill. 'Narrative Structure', 'Story arc', 'Emotion Curve', 'Scene before', ' Structure', 'Visual rhythm' etc. Story Design when . , Text writing Image of .

## Error Handling

| in type | Strategy |
|----------|------|
| Image | vs Prompt 1 when → when + Prompt Text |
| | StoryDesign 3 Suggestion after |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Image-Text Emotion conflict | Image Prompt Text |
