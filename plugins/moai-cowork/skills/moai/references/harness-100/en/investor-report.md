# Investor Report (51-investor-report)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
Investor report generation: an agent team collaborates to produce financial performance analysis, KPI dashboard, market trends, strategy updates, and risk disclosures.

## Expert Roles
- **financial-analyst**: Financial analysis expert. Analyzes P&L, cash flow, and key financial metrics, interprets period-over-period and budget-vs-actual variances, and writes the financial section from an investor perspective.
  - P&L Analysis
  - Cash Flow Analysis
  - Key Financial Metrics
  - Comparative Analysis
  - Financial Highlights
- **ir-reviewer**: IR report reviewer (QA). Cross-validates consistency across financial, KPI, market, and strategy sections, and evaluates the report's persuasiveness, transparency, and completeness from an investor perspective.
  - Financial ↔ KPI Consistency
  - Market ↔ Strategy Consistency
  - Numerical Consistency
  - Investor Perspective Evaluation
  - Compliance
- **kpi-designer**: KPI dashboard design expert. Selects key performance indicators from an investor perspective and systematizes trend visualization, benchmark comparisons, and goal achievement rates.
  - KPI Selection
  - Trend Visualization
  - Benchmark Comparison
  - Goal Achievement Tracking
  - Traffic Light System
- **market-analyst**: Market trends analysis expert. Analyzes industry trends, competitive landscape changes, regulatory developments, and macroeconomic impacts to write the market section of the investor report.
  - Industry Trend Analysis
  - Competitive Landscape Analysis
  - Regulatory Developments
  - Macroeconomic Impact
  - Market Outlook
- **strategy-updater**: Strategy update writer. Writes the progress of business strategy, future roadmap, and risk disclosures from an investor perspective. Also completes the final integrated report.
  - Strategy Progress
  - Future Roadmap
  - Risk Disclosure
  - Executive Message
  - Final Integrated Report

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Company Information**: Company name, industry, stage (startup/growth/public)
    - **Reporting Period**: Quarterly/semi-annual/annual, target period
    - **Financial Data**: P&L, cash flow, KPIs, etc. (file or text)
    - **Strategy Information** (optional): Existing strategy, initiative progress
    - **Target Investors**: VC/PE/public shareholders/creditors
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | Financial Analysis | financial-analyst | None | `_workspace/01_financial_analysis.md` |
| 1b | Market Trends | market-analyst | None | `_workspace/03_market_trends.md` |
| 2 | KPI Dashboard | kpi-designer | Task 1a | `_workspace/02_kpi_dashboard.md` |
| 3 | Strategy + Risk + Integration | strategy-updater | Tasks 1a, 1b, 2 | `_workspace/04_strategy_update.md`, `_workspace/06_investor_report_final.md` |
| 4 | IR Review | ir-reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_review_report.md` |

Tasks 1a (Financial) and 1b (Market) are **executed in parallel**.

**Inter-team Communication Flow:**
- financial-analyst completes → delivers financial KPI data to kpi-designer, requests revenue variance factor analysis from market-analyst
- market-analyst completes → delivers benchmark data to kpi-designer, delivers implications to strategy-updater
- kpi-designer completes → delivers KPI achievement status to strategy-updater
- strategy-updater completes → delivers all documents + final integrated report to ir-reviewer
- ir-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final integrated report (`06_investor_report_final.md`) to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_financial_analysis.md` — Financial performance analysis report
- `02_kpi_dashboard.md` — KPI dashboard
- `03_market_trends.md` — Market trends report
- `04_strategy_update.md` — Strategy update and risk disclosure
- `05_review_report.md` — Review report
- `06_investor_report_final.md` — Final integrated report

## Extension Skills
- **financial-ratio-analyzer**: DuPont analysis, SaaS metrics, 5 financial ratio categories
- **kpi-benchmark-engine**: Industry KPI benchmarks, SMART-R selection framework, pyramid structure

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Incomplete financial data | Perform analysis with available data, specify missing items |
| Web search failure | Work from general market knowledge, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
| Numerical discrepancy | Unify using financial analyst as the source of truth |
