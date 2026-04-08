# Advertising Campaign (12)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to design advertising campaigns: target analysis, copy, creative, and media plans.

## Expert Roles
- **campaign-reviewer**: Campaign reviewer (QA). Cross-validates consistency across market analysis, copy, creative, and media plans, identifying gaps, contradictions, and quality issues to provide feedback.
- **copywriter**: Advertising copywriter. Writes ad copy across all campaign channels including headlines, body copy, CTAs, and slogans based on target analysis.
- **creative-director**: Creative director. Designs visual concepts for advertising campaigns, writes storyboards, and creates ad visual drafts using Gemini image generation.
- **market-analyst**: Advertising campaign market/target analyst. Segments the target audience for products/services, analyzes competitive advertising, and derives insights that form the foundation of campaign strategy.
- **media-planner**: Media planner. Designs optimal media mixes according to campaign goals and budget, establishing per-channel budget allocation, scheduling, and KPIs.

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
 - **/**: ad subject
 - **Campaign goal**: //before/
 - **Budget** (Selection): Budget Budget
 - **between** (Selection): Campaign between
 - **channel** (Selection): channel
 - ** File** (Selection): Copy, Brand Guide etc.
2. `_workspace/` to in generate
3. Organize input and save to `_workspace/00_input.md`in save
4. If existing files are present `_workspace/`, copy to _workspace/ and skip the corresponding Phase
5. Based on the scope of the request **determine the execution mode** ( " per mode" )

### Phase 2: Team Assembly and Execution

 compositionand . between of relationship and :

| sequence | | | of | |
|------|------|------|------|--------|
| 1 | market·Target Analysis | analyst | None | `_workspace/01_market_analysis.md` |
| 2 | ad Copy Writing | copywriter | 1 | `_workspace/02_ad_copy.md` |
| 3a | Creative Design | creative | 1, 2 | `_workspace/03_creative_concept.md` |
| 3b | | planner | 1, 2 | `_workspace/04_media_plan.md` |
| 4 | Campaign Review | reviewer | 2, 3a, 3b | `_workspace/05_review_report.md` |

 3a(Creative)and 3b() **executed in parallel**. 1(Analysis)and 2(Copy)in ofto Copy after whenin when .

**Inter-team communication flow:**
- analyst complete -> copywriterTo Target Insight·USP before, creativeTo Visual before, plannerTo consumption Pattern before
- copywriter complete -> creativeTo line·to before (Copy-Visual Integration), plannerTo Per-channel Copy before
- creative complete -> plannerTo · Information before
- reviewer cross-validate. 🔴 Must Fix when AgentTo → → Verification (vs 2)

### Phase 3: Integration and Final Deliverables

Reviewof based on :

1. `_workspace/` within File verify
2. from the review report 🔴 Must Fix reflected verify
3. summary To :
 - market·Target Analysis — `01_market_analysis.md`
 - ad Copy — `02_ad_copy.md`
 - Creative Concept — `03_creative_concept.md`
 - — `04_media_plan.md`
 - Review — `05_review_report.md`

## Deliverables
- `00_input.md` — Organized user input
- `01_market_analysis.md` — Market/target analysis report
- `02_ad_copy.md` — Ad copy set
- `03_creative_concept.md` — Creative concept/storyboards
- `04_media_plan.md` — Media plan
- `05_review_report.md` — Review report

## Extension Skills
- **ad-copywriting-formulas**: ad Copy Writing when Verification Formula(AIDA, PAS, BAB, 4Ps, SLAP, FAB)and Per-channel Character limit , Psychology Trigger Pattern Copy Extended Skill. 'Copy Formula', 'line Formula', ' Framework', 'AIDA application', 'PAS Copy', 'CTA Pattern' etc. Copy Writingof Structure . , Copy Writing Campaign total Planning of .
- **media-mix-calculator**: Media mix Design when GRP/CPM/CPC/CPA/ROAS etc. core Metrics Calculation Formula, Budget allocation Model, Per-channel Benchmark Extended Skill. ' Metrics Calculation', 'CPM Calculation', 'ROAS Analysis', 'Budget allocation', ' comparison', 'Per-channel Benchmark' etc. of Analysis . , ad Platform whenbetween Optimization of .

## Error Handling

| in type | Strategy |
|----------|------|
| web search | Analysis based on , in the report " " when |
| Image | Text Conceptto , Gemini Prompt when |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Budget | 3 when(500/1,000/3,000)to Writing |
