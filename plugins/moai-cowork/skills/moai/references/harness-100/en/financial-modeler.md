# Financial Modeler (53-financial-modeler)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to produce the full financial modeling lifecycle: revenue model, cost structure, scenario analysis, and valuation.

## Expert Roles
- **cost-analyst**: Cost structure analysis expert. Classifies fixed and variable costs, designs cost structures to calculate break-even points, and derives cost optimization strategies.
  - Cost Classification
  - Cost Structure Design
  - Break-Even Analysis
  - Cost Scaling Model
  - Margin Analysis
- **model-reviewer**: Financial model reviewer (QA). Cross-validates formula accuracy, assumption consistency, and logical validity across revenue model, cost structure, scenarios, and valuation.
  - Formula Accuracy Verification
  - Assumption Consistency Verification
  - Logical Validity Verification
  - Inter-Scenario Consistency
  - Integrated Financial Summary Editing
- **revenue-modeler**: Revenue model design expert. Defines business revenue streams and builds revenue forecast models through pricing strategy, sales volume estimation, and growth rate scenarios.
  - Revenue Stream Definition
  - Pricing Strategy Analysis
  - Sales Volume Estimation
  - Growth Rate Modeling
  - Unit Economics
- **scenario-planner**: Financial scenario analysis expert. Constructs Base/Bull/Bear scenarios and performs sensitivity analysis on key variables to calculate the range of financial performance variation.
  - 3-Scenario Construction
  - Sensitivity Analysis
  - Tornado Chart Data
  - Per-Scenario Financial Statements
  - Probability-Weighted Forecast
- **valuation-expert**: Valuation expert. Applies various valuation methodologies including DCF, multiples, and comparable company analysis to calculate enterprise value and provide the basis for investment decisions.
  - DCF Analysis
  - Multiples Valuation
  - Comparable Company Analysis
  - Valuation Integration
  - Investment Return Analysis

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Business Information**: Industry, business model, product/service, current stage (idea/MVP/PMF/scale-up)
    - **Financial Data** (optional): Current revenue, costs, investment amounts, etc.
    - **Analysis Purpose**: Fundraising, internal planning, M&A, business feasibility validation, etc.
    - **Existing Files** (optional): Existing financial models, business plans, etc.
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | Revenue Model | revenue-modeler | None | `_workspace/01_revenue_model.md` |
| 1b | Cost Structure | cost-analyst | Task 1a | `_workspace/02_cost_structure.md` |
| 2 | Scenario Analysis | scenario-planner | Tasks 1a, 1b | `_workspace/03_scenario_analysis.md` |
| 3 | Valuation | valuation-expert | Task 2 | `_workspace/04_valuation_report.md` |
| 4 | Integration Review | model-reviewer | Tasks 1-3 | `_workspace/05_financial_summary.md`, `_workspace/06_review_report.md` |

**Inter-team Communication Flow:**
- revenue-modeler completes → delivers revenue stream structure and revenue scale to cost-analyst, delivers key assumptions to scenario-planner
- cost-analyst completes → delivers fixed/variable cost structure to scenario-planner
- scenario-planner completes → delivers per-scenario financial statements and probability-weighted forecasts to valuation-expert
- model-reviewer cross-validates all deliverables. If 🔴 Must Fix, sends revision request (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items have been addressed
3. Report the final summary to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_revenue_model.md` — Revenue model
- `02_cost_structure.md` — Cost structure
- `03_scenario_analysis.md` — Scenario analysis results
- `04_valuation.md` — Valuation report
- `05_review_report.md` — Review report

## Extension Skills
- **dcf-valuation**: WACC calculation, FCFF estimation, terminal value, multiples cross-validation
- **sensitivity-analysis**: Tornado chart, 2-way table, Bear/Base/Bull scenarios, break-even
- **unit-economics**: LTV/CAC, 3-layer contribution margin, cohort analysis, bottom-up revenue estimation

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient market data | Apply similar industry benchmarks, tag as "estimates" |
| Unclear business model | Propose 3 revenue model types, request user selection |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note omission in review |
| Numerical discrepancy found | Trace to original, correct figures, document revision history |
| 🔴 found in review | Send revision request → rework → re-validate (up to 2 times) |
