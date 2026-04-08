# Debate Simulator (60-debate-simulator)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for debate simulation.

## Expert Roles
- **con-debater**: Con-side debater. Systematically constructs arguments against the resolution and prepares rebuttals of the pro side's claims.
  - Core claim formulation
  - Argument construction
  - Pro-side rebuttal
  - Alternative proposal
  - Cross-examination question design
- **judge**: Debate judge. Fairly evaluates both sides' arguments, renders a verdict according to evaluation criteria, and provides educational feedback.
  - Argument quality evaluation
  - Rebuttal effectiveness evaluation
  - Cross-examination evaluation
  - Verdict rendering
  - Educational feedback
- **pro-debater**: Pro-side debater. Systematically constructs arguments for the affirmative position and prepares rebuttals against anticipated counterarguments.
  - Core claim formulation
  - Argument construction
  - Evidence and data usage
  - Anticipated rebuttal preparation
  - Cross-examination question design
- **rapporteur**: Rapporteur. Summarizes the entire debate, presents both sides' arguments in a balanced manner, and produces a comprehensive report with key insights.
  - Debate summary
  - Argument comparison
  - Common ground identification
  - Key insights
  - Usage guide
- **topic-analyst**: Debate topic analyst. Structures the issues within a topic, identifies core points of contention, and designs the debate framework.
  - Issue structuring
  - Contention identification
  - Background research
  - Debate format design
  - Term definition

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Resolution**: A clear resolution that can be debated pro/con
    - **Debate purpose** (optional): Educational / decision-making / competition prep / analysis
    - **User's position** (optional): Pro / Con / Neutral
    - **Debate format** (optional): Parliamentary / Lincoln-Douglas / Open debate
    - **Existing materials** (optional): Related reports, papers, articles
2. Create a `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Agent | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Topic analysis | topic-analyst | None | `_workspace/01_topic_analysis.md` |
| 2a | Pro argument construction | pro-debater | Task 1 | `_workspace/02_pro_arguments.md` |
| 2b | Con argument construction | con-debater | Task 1 | `_workspace/03_con_arguments.md` |
| 3 | Cross-examination | pro + con | Tasks 2a, 2b | `_workspace/04_cross_examination.md` |
| 4 | Judge evaluation | judge | Tasks 2a, 2b, 3 | `_workspace/05_judge_verdict.md` |
| 5 | Comprehensive report | rapporteur | All | `_workspace/06_final_report.md` |

Tasks 2a (pro) and 2b (con) run **in parallel**. However, since the con side may reference pro arguments, initial arguments are constructed independently and cross-referenced during the rebuttal phase.

**Inter-agent communication flow:**
- topic-analyst completes -> sends pro-favorable materials to pro-debater; con-favorable materials to con-debater; evaluation criteria to judge
- pro-debater + con-debater complete -> cross-examination simulation: exchange questions and answers
- cross-examination completes -> judge evaluates all arguments + cross-examination
- judge completes -> rapporteur synthesizes everything into a comprehensive report

### Phase 3: Cross-Examination Simulation

The orchestrator mediates cross-examination:
1. Deliver pro-debater's cross-examination questions to con-debater
2. Record con-debater's answers
3. Deliver con-debater's cross-examination questions to pro-debater
4. Record pro-debater's answers
5. Save the results to `_workspace/04_cross_examination.md`

### Phase 4: Integration and Final Report

1. Verify all files in `_workspace/`
2. Verify the comprehensive report's balance and completeness
3. Report the final summary to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_topic_analysis.md` — Topic analysis
- `02_pro_arguments.md` — Pro-side arguments
- `03_con_arguments.md` — Con-side arguments
- `04_verdict.md` — Verdict
- `05_debate_record.md` — Debate record
- `06_review_report.md` — Review report

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Resolution unclear | Ask user to clarify, or have topic-analyst reframe |
| Pro/con balance impossible | Adjust premises to reframe the resolution |
| Background materials insufficient | Apply analogous cases; note "limited data" |
| Web search failure | Work from general knowledge; note in report |
| Agent failure | Retry once -> proceed without that deliverable |
