# Scenario Planner (52-scenario-planner)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness that defines key variables in uncertain environments, constructs a scenario matrix, and develops impact analysis and response strategies.

## Expert Roles
- **impact-assessor**: Per-scenario impact assessment expert. Analyzes the quantitative and qualitative impact of each scenario on the organization's strategy, finances, operations, and workforce, and systematically evaluates risks and opportunities.
  - Impact Dimension Definition
  - Quantitative Impact Analysis
  - Qualitative Impact Analysis
  - Risk-Opportunity Mapping
  - Cross-Scenario Comparison
- **integration-reviewer**: Scenario planning integration reviewer (QA). Cross-validates logical consistency across variable analysis, scenario matrix, impact analysis, and response strategy, and edits the final integrated decision document.
  - Logical Consistency Verification
  - MECE Verification
  - Assumption Consistency Verification
  - Feasibility Verification
  - Integrated Decision Document Editing
- **scenario-designer**: Scenario matrix designer. Constructs 2x2 or 3x3 scenario matrices based on key variable axes and writes the narrative and development path for each scenario.
  - Matrix Construction
  - Scenario Naming
  - Narrative Writing
  - Internal Consistency Verification
  - Scenario Probability Estimation
- **strategy-architect**: Response strategy development expert. Based on per-scenario impact analysis results, designs robust strategies, hedge strategies, and option strategies, and writes integrated decision documents.
  - Robust Strategy Design
  - Hedge Strategy Design
  - Option Strategy Design
  - Decision Trigger Setup
  - Integrated Decision Document
- **variable-analyst**: Key variable analyst for scenario planning. Identifies critical uncertainty variables affecting decision-making, analyzes correlations between variables, and determines scenario axes.
  - Environmental Scanning
  - Variable Identification
  - Uncertainty-Impact Assessment
  - Core Axis Selection
  - Inter-Variable Correlation Analysis

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Decision Topic**: The strategic question subject to scenario analysis
    - **Time Horizon**: Analysis target period (default 3-5 years if unspecified)
    - **Analysis Scope**: Industry, region, organizational scope
    - **Existing Materials** (optional): Analysis reports, data provided by user
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on request scope (see "Execution Modes by Request Scale" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies:

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1 | Key Variable Analysis | variable-analyst | None | `_workspace/01_variable_analysis.md` |
| 2 | Scenario Matrix | scenario-designer | Task 1 | `_workspace/02_scenario_matrix.md` |
| 3 | Impact Analysis | impact-assessor | Tasks 1, 2 | `_workspace/03_impact_assessment.md` |
| 4 | Response Strategy | strategy-architect | Tasks 2, 3 | `_workspace/04_response_strategy.md` |
| 5 | Integration Review + Decision Document | integration-reviewer | Tasks 1-4 | `_workspace/05_decision_document.md`, `_workspace/06_review_report.md` |

**Inter-team Communication Flow:**
- variable-analyst completes → delivers scenario axes, extreme values, predetermined trends to scenario-designer
- scenario-designer completes → delivers 4 scenario narratives, metrics, early warning signals to impact-assessor
- impact-assessor completes → delivers common impacts, key risks/opportunities, vulnerable areas to strategy-architect
- integration-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

Based on the reviewer's report, finalize all deliverables:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user:
    - Key Variable Analysis Report — `01_variable_analysis.md`
    - Scenario Matrix — `02_scenario_matrix.md`
    - Impact Analysis Report — `03_impact_assessment.md`
    - Response Strategy Document — `04_response_strategy.md`
    - Integrated Decision Document — `05_decision_document.md`
    - Review Report — `06_review_report.md`

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_variable_analysis.md` — Key variable analysis report
- `02_scenario_matrix.md` — Scenario matrix and narratives
- `03_impact_assessment.md` — Impact analysis report
- `04_response_strategy.md` — Response strategy document
- `05_decision_document.md` — Integrated decision document
- `06_review_report.md` — Review report

## Extension Skills
- **steep-framework**: STEEP 6-dimension scanning, uncertainty-impact matrix, trend classification
- **scenario-narrative-engine**: 2x2 matrix construction, timeline development, early warning signal design
- **decision-trigger-mapper**: Real options thinking, strategy portfolio, trigger card design, execution roadmap

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient topic information | Ask follow-up questions about industry, scope, time horizon |
| Web search failure | Work from general knowledge, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
| Logical contradiction between deliverables | Request reconciliation from all related agents, resolve root cause |
