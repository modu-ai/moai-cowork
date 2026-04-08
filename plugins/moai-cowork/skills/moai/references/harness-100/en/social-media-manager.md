# Social Media Manager (10-social-media-manager)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce SNS content calendars, post copy, hashtags, and performance analysis.

## Expert Roles

- **Copywriter**: SNS copywriter. Writes post copy, captions, and CTAs tailored to each platform. Optimizes for each platform's grammar — Instagram captions, Twitter threads, TikTok scripts, LinkedIn posts.
  - Instagram Copy: Captions (first-line hooks), carousel text, story text, Reels captions
  - Twitter/X Copy: Standalone tweets (280 chars), threads (5-10 tweets), quote tweets
  - TikTok Scripts: Hook (1-3 sec), body, short-form scripts with CTA
  - LinkedIn Posts: Professional-toned long-form posts, case studies, insights
  - CTA Design: Action-prompting phrases matched to each post's purpose (engagement/click/save/share)

- **Hashtag Analyst**: Hashtag analyst. Designs optimal hashtag sets per post, analyzes trend hashtags, researches competitor hashtags, and develops brand hashtag strategy.
  - Hashtag Research: Research and categorize optimal hashtags by topic/industry
  - Hashtag Set Design: Design optimized hashtag combinations per post
  - Trend Hashtag Analysis: Select usable trending hashtags from current trends
  - Brand Hashtag Development: Develop brand-specific and campaign hashtags
  - Performance Prediction: Analyze expected reach and competition intensity per hashtag

- **Performance Reviewer**: SNS performance reviewer (QA). Cross-validates consistency across strategy, posts, visuals, and hashtags. Verifies KPI alignment, platform suitability, and brand consistency, providing feedback.
  - Strategy-Execution Alignment: Does the content calendar and actual posts align with the strategy?
  - Platform Suitability: Does each post match the grammar, specs, and culture of its platform?
  - Brand Consistency: Do tone, visuals, and messaging match the brand guide?
  - Copy-Visual Alignment: Do text and images convey the same message?
  - Hashtag Appropriateness: Are hashtags relevant to post content and aligned with strategy?

- **Sns Strategist**: SNS strategist. Performs channel-specific analysis, target audience definition, content calendar design, and campaign structure planning. Establishes optimized strategies for each platform (Instagram, Twitter/X, TikTok, Facebook, LinkedIn).
  - Channel Analysis: Analyze platform-specific characteristics (algorithms, optimal content types, active time slots)
  - Target Audience Definition: Define personas, interests, consumption patterns, and active hours
  - Content Calendar Design: Design weekly/monthly content calendars (posting frequency, content mix, seasonal events)
  - Content Pillar Composition: Determine the ratio of educational/entertainment/inspirational/promotional/community content
  - Campaign Design: Plan campaigns aligned with specific goals (brand awareness, conversion, community growth)

- **Visual Planner**: SNS visual planner. Designs image concepts per post, card news layouts, Reels/short-form storyboards, and visual guidelines.
  - Image Concept Design: Determine composition, color palette, and style for each post's imagery
  - Card News Layout: Design slide-by-slide layouts for swipeable carousels
  - Reels/Short-Form Storyboard: Plan cut-by-cut composition, text overlays, and transition effects for short videos
  - Visual Guidelines: Organize color, font, and layout guides for brand consistency
  - Image Generation Prompts: Write prompts for Gemini image generation

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Brand/Account Info**: Industry, tone & voice, target customers
   - **Platforms**: Instagram, Twitter/X, TikTok, Facebook, LinkedIn
   - **Period**: Weekly/monthly content plan
   - **Goals** (optional): Brand awareness, conversion, community growth
   - **Existing Files** (optional): Brand guide, existing content
2. Create the `_workspace/` directory in the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding Phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|------------|--------------|-------------|
| 1 | SNS strategy | sns-strategist | None | `_workspace/01_strategy.md` |
| 2a | Post copy | copywriter | Task 1 | `_workspace/02_posts.md` |
| 2b | Hashtag strategy | hashtag-analyst | Task 1 | `_workspace/04_hashtags.md` |
| 3 | Visual planning | visual-planner | Tasks 1, 2a | `_workspace/03_visuals.md` |
| 4 | Performance review | performance-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (copy) and 2b (hashtags) are **executed in parallel**. Visual planning (3) starts after copy is complete.

**Inter-team communication flow:**
- sns-strategist complete -> Deliver tone and calendar to copywriter, keywords and competitor accounts to hashtag-analyst, brand guide to visual-planner
- copywriter complete -> Deliver text overlays and image keywords to visual-planner, post topics to hashtag-analyst
- hashtag-analyst complete -> Deliver trend hashtags to visual-planner
- performance-reviewer cross-validates all deliverables. When RED Must Fix is found, request revisions from the relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Strategy/Calendar — `01_strategy.md`
   - Post Copy — `02_posts.md`
   - Visual Plan — `03_visuals.md`
   - Hashtag Strategy — `04_hashtags.md`
   - Review Report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_strategy.md` — SNS strategy/content calendar
- `02_posts.md` — Post copy collection
- `03_visuals.md` — Visual plan
- `04_hashtags.md` — Hashtag strategy
- `05_review_report.md` — Review report

## Extension Skills

- **hashtag-science**: A specialized skill for the hashtag-analyst agent covering hashtag science. Provides hashtag pyramid strategy, competition analysis, trend prediction, and platform-specific optimal hashtag strategies. Use for 'hashtags,' 'keyword strategy,' 'trend analysis,' 'hashtag research,' and similar topics.
- **platform-algorithms**: A specialized skill for the sns-strategist and visual-planner agents covering platform algorithms. Provides how recommendation algorithms work and reach optimization strategies for Instagram, TikTok, LinkedIn, and X. Use for 'algorithm,' 'reach rate,' 'exposure optimization,' 'feed algorithm,' and similar topics.
- **viral-copywriting**: A specialized skill for the copywriter agent covering viral copywriting. Provides scroll-stopping hook patterns, platform-specific copy structures, emotion triggers, and CTA psychology. Use for 'viral copy,' 'hook writing,' 'caption writing,' 'SNS copy,' and similar topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Brand info insufficient | Apply industry-standard guide, note "customization needed" |
| Web search failure | Work with general SNS knowledge, note "trend data limited" |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Image generation failure | Proceed with text concepts and prompts only, available for user retry |
