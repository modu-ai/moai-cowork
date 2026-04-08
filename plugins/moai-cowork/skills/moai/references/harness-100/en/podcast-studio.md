# Podcast Studio (02-podcast-studio)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce podcast content through the pipeline of planning, research, scripting, show notes, and distribution strategy.

## Expert Roles

- **Distribution Manager**: Podcast distribution manager. Generates platform-specific metadata, episode descriptions, promotional copy, social media posts, and newsletter introductions.
  - Platform-Specific Metadata: Optimization for major platforms including Apple Podcasts, Spotify, YouTube Podcasts
  - Episode Description: Keyword-rich descriptions optimized for platform search and discovery
  - Social Media Promotional Copy: Generate promotional posts for Twitter/X, Instagram, LinkedIn, Facebook
  - Newsletter Introduction: Write an episode introduction for email subscribers
  - Promotional Calendar: Propose a pre/post-release promotional schedule

- **Production Reviewer**: Podcast production reviewer (QA). Cross-validates consistency across research, script, show notes, and distribution. Identifies gaps, contradictions, and quality issues and provides actionable feedback.
  - Research–Script Alignment: Are the research brief's key facts and talking points accurately reflected in the script?
  - Script–Show Notes Alignment: Do the show note timestamps and summary match the script structure?
  - Script–Distribution Alignment: Does the promotional copy accurately reflect the actual episode content?
  - Fact Accuracy: Do statistics/facts cited in the script match the research brief's sources?
  - Quality Checklist: Tone consistency, length, CTA, legal considerations, etc.

- **Researcher**: Podcast researcher. Performs deep topic investigation, fact-checking, guest background research, reference compilation, and talking point extraction.
  - Deep Topic Investigation: Gather the latest trends, statistics, and case studies on the user's topic
  - Fact-Checking: Verify the accuracy of cited figures, research findings, and expert opinions via web search
  - Guest Background Research: When a guest is involved, research their career, publications, recent statements, and social media activity
  - Competitive Podcast Analysis: Investigate existing episodes on the same topic and identify differentiation opportunities
  - Talking Point Extraction: Generate structured talking points the scriptwriter can immediately use

- **Scriptwriter**: Podcast scriptwriter. Creates episode scripts optimized for listener retention based on the research brief. Generates timecode-based scripts including opening, segments, transitions, and closing.
  - Opening Hook: Design an opening that captures the listener within the first 30 seconds (shocking stat/question/story)
  - Segment Structure: Arrange talking points in a logical flow with natural transitions
  - Dialogue Cue Insertion: Directives such as `[Host Question]`, `[Guest Response Prompt]`, `[Listener Engagement Prompt]`
  - Tone & Pace Management: Design conversational rhythm suited to the episode type (solo/interview/panel)
  - CTA Design: Subscription, reviews, shares, community engagement — woven naturally into the conversation

- **Shownote Editor**: Podcast show note editor. Organizes episode summaries, timestamps, reference links, guest bios, and key quotes into structured show notes.
  - Episode Summary: A 3–5 sentence summary + 1-line elevator pitch to help listeners decide whether to tune in
  - Timestamp Generation: Create accurate timestamps based on the script's segment structure
  - Reference Compilation: Organize books, papers, websites, and tools mentioned in the episode as clickable links
  - Key Quote Extraction: Select 1–3 key quotes suitable for social media sharing
  - Guest Bio: Write a guest biography with links to their website and social profiles

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Topic/Keywords**: The subject the episode will cover
   - **Podcast Info** (optional): Show tone, listener base, existing episode direction
   - **Episode Type** (optional): Solo/Interview/Panel/Storytelling/Q&A
   - **Guest Info** (optional): Guest name, area of expertise
   - **Constraints** (optional): Episode length, specific requirements
   - **Existing Files** (optional): Scripts, research materials, etc. provided by the user
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on request scope (see "Scope-Based Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Topic research | researcher | None | `_workspace/01_research_brief.md` |
| 2 | Script writing | scriptwriter | Task 1 | `_workspace/02_script.md` |
| 3a | Show notes | shownote-editor | Tasks 1, 2 | `_workspace/03_shownotes.md` |
| 3b | Distribution package | distribution-manager | Tasks 1, 2 | `_workspace/04_distribution_package.md` |
| 4 | Production review | production-reviewer | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (show notes) and 3b (distribution) run **in parallel**. Both depend on Task 2 (script), so they can start simultaneously once the script is complete.

**Inter-agent communication flow:**
- researcher complete → deliver talking points & facts to scriptwriter, references to shownote-editor, trending keywords to distribution-manager
- scriptwriter complete → deliver segment timecodes to shownote-editor, key quotes to distribution-manager
- shownote-editor complete → deliver episode summary & quotes to distribution-manager
- reviewer cross-validates all deliverables. On 🔴 Must Fix: request revision from the responsible agent → rework → re-validate (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Compile the final deliverables based on the reviewer's report:

1. Verify all files in `_workspace/`
2. Confirm all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Research Brief — `01_research_brief.md`
   - Episode Script — `02_script.md`
   - Show Notes — `03_shownotes.md`
   - Distribution Package — `04_distribution_package.md`
   - Review Report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_research_brief.md` — Research brief
- `02_script.md` — Podcast script
- `03_shownotes.md` — Show notes
- `04_distribution_package.md` — Distribution package
- `05_review_report.md` — Review report

## Extension Skills

- **audio-storytelling**: Audio storytelling skill used by the podcast scriptwriter and show note editor. Provides narrative structure, pacing, and sound design methodologies that maximize listener immersion in an audio-only medium. Use this skill's knowledge for 'audio narrative,' 'listener retention,' 'story arc,' 'sound design,' and similar requests.
- **interview-techniques**: Interview technique skill used by the podcast scriptwriter. Provides question design, conversation flow management, and emotional arc design methodologies for drawing out deep conversations in guest interviews. Use this skill's knowledge for 'interview question design,' 'conversation structure,' 'guest questions,' 'dialogue flow,' and similar requests.
- **podcast-growth**: Podcast growth strategy skill used by the distribution manager. Provides platform-specific optimization, cross-promotion, listener acquisition strategies, and community building methodologies. Use this skill's knowledge for 'podcast growth,' 'distribution optimization,' 'listener acquisition,' 'platform strategy,' and similar requests.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Researcher works from general knowledge, report notes "data limitation" |
| Guest info unavailable | Provide generic interview framework, request guest info from user |
| Agent failure | Retry once → if still failing, proceed without that deliverable, note omission in review report |
| 🔴 found in review | Request revision from responsible agent → rework → re-validate (up to 2 rounds) |
