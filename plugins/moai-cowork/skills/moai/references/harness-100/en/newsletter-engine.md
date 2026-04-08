# Newsletter Engine (03-newsletter-engine)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce newsletter content through the pipeline of curation, writing, A/B testing, and send optimization.

## Expert Roles

- **Analyst**: Newsletter analyst. Designs A/B tests, optimizes send timing, develops segment strategies, and builds performance forecasting models.
  - A/B Test Design: Design tests for key variables including subject line, preheader, CTA, and send time
  - Send Optimization: Recommend optimal send times by day and time slot
  - Segment Strategy: Develop tailored content distribution strategies based on subscriber characteristics
  - Performance Forecasting: Provide KPI projections based on industry benchmarks
  - Improvement Suggestions: Derive improvements from previous newsletter data (when available)

- **Copywriter**: Newsletter copywriter. Creates newsletter body copy based on the curation brief that gets subscribers to read to the end and take action.
  - Subject Line/Preheader Writing: Craft the subject line and preview text that determine open rates
  - Intro Writing: Design an opening that captures the reader within the first 2 sentences
  - Body Copy: Reshape curated content into a reader-friendly tone
  - CTA Design: Place clear CTAs that drive clicks, replies, shares, and other reader actions
  - Layout Design: Create a scannable layout using headings, bullets, and bold text

- **Curator**: Newsletter curator. Collects content from diverse sources, analyzes trends, and selects and prioritizes content for inclusion in the newsletter.
  - Source Collection: Gather the latest articles, blogs, reports, and social media trends related to the topic via web search
  - Trend Analysis: Identify patterns and trends from the collected content
  - Content Selection: Prioritize content that matches subscriber interests and the newsletter's tone
  - Angle Setting: Define the perspective from which each piece of content should be covered in the newsletter
  - Category Organization: Distribute content across newsletter sections

- **Editor In Chief**: Newsletter Editor-in-Chief. Performs final review of brand tone consistency, content flow, and layout structure, and finalizes the publish-ready version.
  - Tone Consistency Review: Ensure the entire newsletter is consistent with the brand voice
  - Content Flow Optimization: Review section order, weighting, and transition smoothness
  - Spelling & Grammar Correction: Fix typos, awkward phrasing, and grammatical errors
  - Legal Review: Verify legal requirements including copyright, attribution, advertising disclosure, and unsubscribe links
  - Final Editing: Finalize the version incorporating the analyst's A/B test recommendations

- **Quality Reviewer**: Newsletter quality reviewer (QA). Cross-validates consistency across curation, copy, analysis, and editing. Identifies gaps, contradictions, and quality issues and provides actionable feedback.
  - Curation–Copy Alignment: Is the curation brief's angle faithfully reflected in the copy?
  - Copy–Analysis Alignment: Are A/B test variants properly reflected in the draft?
  - Editorial–Legal Alignment: Are all legal requirements (unsubscribe, sender info, etc.) met?
  - Link Validation: Are all URLs in the body valid and pointing to the correct destinations?
  - Quality Checklist: Spelling, consistency, mobile optimization, etc.

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Topic/Theme**: The subject the newsletter will cover
   - **Newsletter Info** (optional): Brand tone, subscriber count, publication frequency
   - **Target Reader** (optional): Subscriber characteristics, interests
   - **Constraints** (optional): Length, specific section requirements
   - **Existing Files** (optional): Content, previous issues, etc. provided by the user
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Content curation | curator | None | `_workspace/01_curation_brief.md` |
| 2 | Newsletter writing | copywriter | Task 1 | `_workspace/02_newsletter_draft.md` |
| 3 | A/B test design | analyst | Tasks 1, 2 | `_workspace/03_ab_test_plan.md` |
| 4 | Final editing | editor-in-chief | Tasks 2, 3 | `_workspace/04_editorial_final.md` |
| 5 | Quality review | quality-reviewer | Tasks 2, 3, 4 | `_workspace/05_review_report.md` |

**Inter-agent communication flow:**
- curator complete → deliver angles & content to copywriter, trending keywords to analyst
- copywriter complete → deliver A/B variant materials to analyst, draft to editor-in-chief
- analyst complete → deliver send optimization & A/B recommendations to editor-in-chief
- editor-in-chief complete → deliver final version to quality-reviewer
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items have been addressed
3. Report the final summary to the user:
   - Curation Brief — `01_curation_brief.md`
   - Newsletter Draft — `02_newsletter_draft.md`
   - A/B Test Plan — `03_ab_test_plan.md`
   - Editor-in-Chief Final — `04_editorial_final.md`
   - Review Report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_curation_brief.md` — Curation brief
- `02_newsletter_draft.md` — Newsletter draft
- `03_ab_test_plan.md` — A/B test plan
- `04_editorial_final.md` — Editor-in-Chief final version
- `05_review_report.md` — Review report

## Extension Skills

- **audience-segmentation**: Audience segmentation skill used by the analyst and curator agents. Provides subscriber behavior analysis, persona-based content personalization, and segment-specific strategy methodologies. Use for 'audience analysis,' 'segmentation,' 'persona,' 'send optimization,' and similar requests.
- **deliverability-optimization**: Email deliverability optimization skill used by the Editor-in-Chief and analyst agents. Provides spam filter avoidance, technical authentication, content filtering rules, and list hygiene management methodologies. Use for 'deliverability,' 'spam filters,' 'email authentication,' 'send optimization,' and similar requests.
- **email-copywriting**: Email copywriting skill used by the copywriter agent. Provides subject line psychology, preheader optimization, CTA design, and scannable body structure methodologies specific to the email medium. Use for 'email copy,' 'newsletter writing,' 'subject lines,' 'CTA design,' and similar requests.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Curator works from user-provided materials, notes "real-time data not reflected" |
| Brand tone unclear | Apply default tone (professional + friendly), editor-in-chief recommends tone refinement after first issue |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |
