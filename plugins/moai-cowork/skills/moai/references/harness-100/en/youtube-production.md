# Youtube Production (01-youtube-production)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce YouTube video content through the pipeline of strategy, script, thumbnail, and SEO.

## Expert Roles

- **Content Strategist**: YouTube content strategist. Performs topic analysis, target audience definition, competitive channel benchmarking, content positioning, and video concept design.
  - Topic Analysis: Derive viable video angles from the topic/keywords provided by the user
  - Target Audience Definition: Analyze the core viewer segment's interests, pain points, and search intent
  - Competitive Benchmarking: Research existing YouTube videos on the same topic via web search and identify differentiation opportunities
  - Content Concept Design: Determine the video's tone, structure (listicle/story/tutorial/interview/comparison, etc.), and core hook
  - Keyword Research: Identify primary and related keywords based on search traffic potential

- **Production Reviewer**: YouTube production reviewer (QA). Cross-validates consistency across strategy, script, thumbnail, and SEO. Identifies gaps, contradictions, and quality issues and provides actionable feedback.
  - Strategy–Script Alignment: Is the brief's core angle faithfully reflected in the script?
  - Script–Thumbnail Alignment: Does the script deliver on the curiosity the thumbnail promises?
  - Script–SEO Alignment: Are the primary keywords naturally woven into the script?
  - Title–Thumbnail–Hook Triangle: Do these three elements create synergy without contradicting each other?
  - Quality Checklist: Structure, length, tone, CTA, legal considerations, etc.

- **Scriptwriter**: YouTube scriptwriter. Creates video scripts optimized for audience retention based on the strategy brief. Generates timecode-based scripts including hook, development, transitions, and closing.
  - Hook Writing: Design an opening that captures the viewer within the first 5–10 seconds
  - Body Structure: Logical progression across segments with well-placed transitions
  - Dialogue Styling: Conversational tone, natural rhythm, direct address to the viewer
  - Visual Cue Insertion: Editing directives such as `[B-roll: ...]`, `[Graphic: ...]`, `[Text Overlay: ...]`
  - CTA Design: Likes, subscriptions, and comments — woven naturally into the content

- **Seo Optimizer**: YouTube SEO specialist. Handles search optimization, metadata creation, tag strategy, description optimization, and subtitle/chapter generation. Maximizes discoverability through the YouTube algorithm.
  - Title Optimization: Include search keywords + drive clicks — under 60 characters, with the primary keyword placed near the front
  - Description Writing: Place the core value proposition + keywords in the first 2 lines (visible when collapsed)
  - Tag Strategy: Structure tags from primary keyword → related keywords → channel name → series name
  - Chapter Markers: Generate YouTube chapters based on the script's timecodes
  - Subtitle File Generation: Convert the script to SRT format
  - Hashtags: Select 3 hashtags to appear above the video title

- **Thumbnail Designer**: YouTube thumbnail designer. Designs thumbnail concepts that maximize click-through rate (CTR) and produces actual thumbnails using Gemini image generation.
  - Thumbnail Concept Design: Determine how to visually express the strategy brief's core angle
  - Text Overlay Design: A punchy 3–5 word text overlay — complementing the title without repeating it
  - Color Strategy: Choose a color scheme that stands out from competing thumbnails
  - Image Generation: Produce actual thumbnail images using Gemini image generation
  - A/B Variants: Create a primary thumbnail + 1–2 alternatives to provide options

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Topic/Keywords**: The subject the video will cover
   - **Channel Info** (optional): Channel tone, subscriber count, existing content direction
   - **Constraints** (optional): Video length, specific requirements
   - **Existing Files** (optional): Scripts, briefs, or other materials provided by the user
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on request scope (see "Scope-Based Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Content strategy | strategist | None | `_workspace/01_strategist_brief.md` |
| 2a | Script writing | writer | Task 1 | `_workspace/02_scriptwriter_script.md` |
| 2b | Thumbnail design & generation | designer | Task 1 | `_workspace/03_thumbnail_concept.md` |
| 3 | SEO package | seo | Tasks 1, 2a | `_workspace/04_seo_package.md`, `_workspace/subtitle.srt` |
| 4 | Production review | reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (script) and 2b (thumbnail) run **in parallel**. Both depend only on Task 1 (strategy), so they can start simultaneously.

**Inter-agent communication flow:**
- strategist complete → deliver core angle & tone to writer, title candidates & emotional triggers to designer, keyword map to seo
- writer complete → deliver hook core message to designer (thumbnail-hook consistency), deliver script to seo
- seo complete → deliver title-thumbnail combination feedback to designer
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision from the responsible agent → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Compile the final deliverables based on the reviewer's report:

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Strategy Brief — `01_strategist_brief.md`
   - Video Script — `02_scriptwriter_script.md`
   - Thumbnail Concept + Images — `03_thumbnail_concept.md`
   - SEO Package — `04_seo_package.md`
   - Review Report — `05_review_report.md`
   - Subtitle File — `subtitle.srt`

## Deliverables

- `00_input.md` — Organized user input
- `01_strategist_brief.md` — Strategy brief
- `02_scriptwriter_script.md` — Video script
- `03_thumbnail_concept.md` — Thumbnail concept
- `04_seo_package.md` — SEO package
- `05_review_report.md` — Review report
- `subtitle.srt` — Subtitle file

## Extension Skills

- **hook-writing**: YouTube video hook (opening) writing skill. Provides 15 hook patterns, viewer retention psychology, and click-to-watch conversion formulas. Referenced by the scriptwriter agent when designing video openings to minimize viewer drop-off. Also used standalone for requests like 'show me hook patterns' or 'how to write great openings.' Full script writing and SEO optimization fall under the youtube-production skill.
- **thumbnail-psychology**: YouTube thumbnail visual psychology skill. Provides color theory, composition principles, CTR optimization patterns, and mobile readability checklists. Referenced by the thumbnail-designer agent when designing visually effective thumbnails. Also used standalone for requests like 'how to make great thumbnails' or 'thumbnails that boost click-through rate.' Actual image generation falls under the gemini-3-pro-imagegen skill.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Strategist works from general knowledge, report notes "data limitation" |
| Thumbnail image generation failure | Proceed with text concept only, include Gemini prompt for user retry |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |
