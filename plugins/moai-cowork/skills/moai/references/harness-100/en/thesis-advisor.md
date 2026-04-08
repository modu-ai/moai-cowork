# Thesis Advisor (58-thesis-advisor)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for thesis writing: topic selection, literature review, methodology, writing, and proofreading.

## Expert Roles
- **literature-analyst**: Literature analyst. Systematically surveys prior research, critically reviews it, and constructs the theoretical framework for the study.
  - Search strategy
  - Prior research classification
  - Critical review
  - Theoretical framework construction
  - Research gap confirmation
- **methodology-expert**: Research methodology expert. Designs research approaches, data collection methods, and analysis techniques appropriate to the research questions, and ensures methodological rigor.
  - Research design
  - Sample design
  - Data collection instruments
  - Analysis method selection
  - Research ethics
- **proofreader**: Thesis proofreader. Performs grammar and spelling correction, academic format verification, consistency review, and plagiarism risk assessment.
  - Grammar and spelling correction
  - Academic style verification
  - Format verification
  - Logical consistency
  - Plagiarism risk assessment
- **topic-explorer**: Research topic explorer. Surveys trends in the research field, discovers research gaps, and formulates specific research questions and hypotheses.
  - Field trend analysis
  - Research gap identification
  - Research question formulation
  - Hypothesis development
  - Feasibility assessment
- **writing-coach**: Thesis writing coach. Designs the overall structure of the thesis, drafts each chapter, and strengthens the argumentation.
  - Thesis structure design
  - Introduction writing
  - Literature review chapter
  - Methods chapter
  - Argumentation strengthening

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Discipline**: Major and sub-field
    - **Thesis type**: Master's / Doctoral / Journal article / Undergraduate thesis
    - **Topic of interest** (optional): Specific topic or keywords
    - **Advisor's research area** (optional): Lab research direction
    - **Existing materials** (optional): Existing manuscripts, reference lists, data
    - **Deadline** (optional): Submission date
2. Create a `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing materials are provided, copy them to `_workspace/` and adjust the relevant phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Agent | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Topic exploration | topic-explorer | None | `_workspace/01_topic_proposal.md` |
| 2 | Literature review | literature-analyst | Task 1 | `_workspace/02_literature_review.md` |
| 3 | Methodology design | methodology-expert | Tasks 1, 2 | `_workspace/03_methodology_design.md` |
| 4 | Draft writing | writing-coach | Tasks 1, 2, 3 | `_workspace/04_draft_manuscript.md` |
| 5 | Proofreading | proofreader | Task 4 | `_workspace/05_proofread_report.md` |

**Inter-agent communication flow:**
- topic-explorer completes -> sends research questions and keywords to literature-analyst; sends hypotheses and variables to methodology-expert
- literature-analyst completes -> sends methodology trends from prior studies to methodology-expert; sends literature review content to writing-coach
- methodology-expert completes -> sends full methodology design to writing-coach
- writing-coach completes -> sends completed draft to proofreader
- proofreader completes -> on critical findings, requests corrections from the relevant agent (max 2 rounds)

### Phase 3: Integration and Final Report

1. Verify all files in `_workspace/`
2. Confirm that all critical proofreading items have been addressed
3. Report the final summary to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_topic_exploration.md` — Topic exploration report
- `02_literature_review.md` — Literature analysis report
- `03_methodology.md` — Methodology design document
- `04_writing_guide.md` — Writing guide
- `05_proofreading.md` — Proofreading report
- `06_review_report.md` — Review report

## Extension Skills
- **research-methodology**: Research design matrix, sample size calculation, validity/reliability, analysis method selection

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Academic DB search failure | Substitute with web search; note "search limited" in report |
| Cannot determine field | Ask user narrowing questions; infer from interests |
| Existing manuscript format unclear | Apply standard dissertation format |
| Agent failure | Retry once -> proceed without that deliverable if still failing |
| Critical finding in proofreading | Request correction from relevant agent -> re-verify (max 2 rounds) |
