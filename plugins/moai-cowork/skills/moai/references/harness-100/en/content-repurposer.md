# Content Repurposer (04-content-repurposer)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team transforms a single source piece of content into multiple formats: blog posts, social media, newsletters, presentations, and scripts.

## Expert Roles

- **Blog Writer**: Blog writer. Transforms source content into SEO-optimized blog posts. Maximizes both search traffic and reader value.
  - Title Optimization: Include search keywords + drive clicks — under 60 characters
  - Intro Design: Define the reader's problem/interest and promise a solution within the first 2 paragraphs
  - Body Structure: Scannable structure using H2/H3 heading hierarchy, bullet points, and numbered lists
  - SEO Optimization: Meta description, keyword placement, internal/external link suggestions
  - CTA Design: Related content recommendations, newsletter subscription, social sharing prompts

- **Presentation Builder**: Presentation builder. Transforms source content into slide presentations. Generates story arcs, slide layouts, and speaker notes.
  - Story Arc Design: Design a Problem → Solution → Evidence → Action narrative structure
  - Slide Composition: Title, body, visual guide, and speaker notes for each slide
  - Data Visualization: Propose converting the source's numbers/statistics into chart/graph formats
  - Speaker Notes: Write presenter talking points/guides for each slide
  - Handout Summary: Create a one-page summary document for post-presentation distribution

- **Quality Reviewer**: Content repurposing quality reviewer (QA). Cross-validates message consistency, factual accuracy, and format suitability between source and converted content.
  - Message Consistency: Is the source's core message conveyed without distortion across all formats?
  - Factual Accuracy: Were data, quotes, and facts altered during conversion?
  - Format Suitability: Does each converted piece follow the best practices for its format?
  - Tone Appropriateness: Is the tone conversion natural for each format (not forced uniformity)?
  - Cross-Reference: Are there no contradictions between converted pieces?

- **Sns Copywriter**: Social media copywriter. Transforms source content into platform-optimized posts for Twitter/X, Instagram, LinkedIn, Facebook, Threads, and more.
  - Twitter/X Thread: Break core messages into a tweet thread, with the first tweet as the viral hook
  - Instagram Carousel: Plan slide-based content (text + visual guide)
  - LinkedIn Post: Long-form post with a professional expertise + personal experience tone
  - Facebook Post: Community conversation-driving post
  - Short-Form Script: 30–60 second script for Reels/Shorts/TikTok

- **Source Analyst**: Source content analyst. Analyzes the source's structure, core messages, target audience, and tone, then develops optimal conversion strategies for each output format.
  - Structure Analysis: Map the source's logical structure, section organization, and information hierarchy
  - Core Message Extraction: Identify 1 overarching message and 3–5 supporting messages that thread through the source
  - Audience Analysis: Analyze the gap between the source's target reader and each output format's expected audience
  - Tone Mapping: Identify the source's tone and propose tone conversion directions for each format
  - Conversion Strategy: Design what to emphasize, reduce, or restructure for each format

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Source Content**: The original to convert (text, file, URL)
   - **Output Formats** (optional): Desired conversion formats (default: blog + social + presentation)
   - **Target Audience** (optional): Target audience for each format
   - **Brand Tone** (optional): Consistent brand voice
   - **Constraints** (optional): Specific platforms, length limits, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If the source is a URL, fetch its content via WebFetch
5. Determine the **execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Source analysis | source-analyst | None | `_workspace/01_source_analysis.md` |
| 2a | Blog conversion | blog-writer | Task 1 | `_workspace/02_blog_post.md` |
| 2b | Social media conversion | sns-copywriter | Task 1 | `_workspace/03_sns_package.md` |
| 2c | Presentation conversion | presentation-builder | Task 1 | `_workspace/04_presentation.md` |
| 3 | Quality review | quality-reviewer | Tasks 2a, 2b, 2c | `_workspace/05_review_report.md` |

Tasks 2a (blog), 2b (social), and 2c (presentation) run **in parallel**. All depend only on Task 1 (source analysis), so they can start simultaneously.

**Inter-agent communication flow:**
- source-analyst complete → deliver format-specific strategies to each conversion agent
- blog-writer complete → deliver blog quotes & links to sns-copywriter
- sns-copywriter complete → deliver visual consistency info to presentation-builder
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items have been addressed
3. Report the final summary to the user:
   - Source Analysis — `01_source_analysis.md`
   - Blog Post — `02_blog_post.md`
   - Social Media Package — `03_sns_package.md`
   - Presentation — `04_presentation.md`
   - Review Report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_source_analysis.md` — Source analysis report
- `02_blog_post.md` — Blog post
- `03_sns_package.md` — Social media post package
- `04_presentation.md` — Presentation slides
- `05_review_report.md` — Review report

## Extension Skills

- **content-atomization**: Content atomization skill used by the source analyst and presentation builder. Provides methodology for breaking a single piece of content into its smallest units and recombining them for maximum conversion efficiency. Use for 'content decomposition,' 'atomization,' 'key extraction,' 'recombination,' and similar requests.
- **platform-adaptation**: Platform adaptation skill used by the social media copywriter and blog writer. Provides content conversion methodologies tailored to each platform's algorithm, format constraints, and user behavior patterns. Use for 'platform optimization,' 'social media conversion,' 'format adaptation,' and similar requests.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Source URL inaccessible | Request text input from user, or work with cached content |
| Source too short (under 500 words) | Supplement with related material via web search, note "source augmented" |
| Agent failure | Retry once → if still failing, proceed without that format, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |
