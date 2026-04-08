# BI Dashboard (42)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

BI dashboard construction: a harness where an agent team collaborates to perform KPI design → data engineering → dashboard building → report automation → review.

## Expert Roles

- **BI Reviewer**: BI reviewer (QA). Cross-validates consistency between data model, KPI calculations, visualizations, and reports. Identifies data errors, metric contradictions, and UX issues to provide feedback.
  - Data Model <> KPI Consistency: Can KPI formulas actually be implemented with the existing tables/columns?
  - KPI <> Dashboard Consistency: Are all defined KPIs reflected in visualizations? Are chart types appropriate?
  - Dashboard <> Report Consistency: Do report figures use the same calculation logic as the dashboard?
  - End-to-End Data Flow: Is there no break in the entire path from source > warehouse > KPI > visualization > report?
  - User Experience Verification: Is it at a level that decision-makers can actually use?

- **Dashboard Builder**: Dashboard builder. Designs dashboard layouts, chart types, interactions, and color schemes that effectively visualize KPIs.
  - Dashboard Architecture: Overall dashboard structure (tab/page layout), views by user role
  - Chart Type Selection: Determine optimal visualization types for each KPI (Bar, Line, KPI Card, Heatmap, etc.)
  - Layout Design: Information hierarchy, visual flow (Z-pattern/F-pattern), grid placement
  - Interaction Design: Define filters, drill-downs, cross-filtering, and tooltip behavior
  - Color and Style Guide: Optimize data-ink ratio, accessibility-aware palettes (color blindness)

- **Data Engineer**: BI data engineer. Performs source data analysis, data warehouse schema design, ETL pipeline definition, and data quality rule establishment.
  - Source Data Analysis: Identify data sources (DB, API, files) the user has, diagnose schema and quality
  - Data Warehouse Design: Design Fact/Dimension tables based on Star/Snowflake schema
  - ETL Pipeline Definition: Define the extract-transform-load flow, scheduling frequency, incremental/full load strategies
  - Data Quality Rules: Specify null checks, range validation, referential integrity, and deduplication rules
  - Performance Optimization: Propose partitioning, indexing, and aggregation table strategies

- **KPI Designer**: KPI designer. Derives key performance indicators from business objectives and defines calculation logic, targets, benchmarks, and drill-down paths.
  - KPI Tree Design: Decompose from top-level business objectives to operational metrics (MECE principle)
  - Metric Definition: Specify exact calculation formula, numerator/denominator, filter conditions, and time range for each KPI
  - Target Setting: Establish realistic targets based on industry benchmarks, historical trends, and business goals
  - Drill-Down Paths: Design hierarchical metric connections to trace causes from top-level indicators
  - Alert Thresholds: Define warning/critical thresholds for when metrics fall outside normal ranges

- **Report Automator**: Report automation specialist. Builds scheduled report generation, alert rule configuration, distribution channel management, and data storytelling templates.
  - Report Template Design: Design custom report structures and content by recipient type (executives/team leads/practitioners)
  - Automated Generation Pipeline: Design the automation flow for data extraction > processing > rendering > distribution
  - Alert Rule Configuration: Define real-time/batch alert conditions and escalation paths based on KPI thresholds
  - Distribution Channel Management: Optimize formats for each channel (email, Slack, Teams, PDF, web links)
  - Data Storytelling: Design commentary templates that transform numbers into context and narrative

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Business domain**: E-commerce/SaaS/Manufacturing/Finance/Education, etc.
    - **Data sources**: Available DB, API, file information
    - **Key questions**: Business questions the dashboard should answer
    - **User tiers**: Executives/team leads/practitioners — dashboard users
    - **Existing assets** (optional): Existing KPIs, data models, reports, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request (see "Execution Modes by Request Scope" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Data warehouse design | data-engineer | None | `_workspace/01_data_warehouse_design.md` |
| 2 | KPI definition | kpi-designer | Task 1 | `_workspace/02_kpi_definition.md` |
| 3a | Dashboard visualization | dashboard-builder | Tasks 1, 2 | `_workspace/03_dashboard_spec.md` |
| 3b | Report automation | report-automator | Task 2 | `_workspace/04_report_automation.md` |
| 4 | BI review | bi-reviewer | Tasks 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (dashboard) and 3b (report) run **in parallel**.

**Inter-agent communication flow:**
- data-engineer completes > passes Measure/Dimension list to kpi-designer
- kpi-designer completes > passes KPI priorities/drill-down to dashboard-builder, passes reporting schedule/thresholds to report-automator
- dashboard-builder completes > passes snapshot capture method to report-automator
- bi-reviewer cross-validates all deliverables. On CRITICAL findings, requests corrections from the relevant agent > rework > re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Finalize deliverables based on the reviewer's report:

1. Verify all files in `_workspace/`
2. Confirm that all CRITICAL findings have been addressed
3. Report the final summary to the user

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and business requirements
- `01_kpi_design.md` — KPI tree and metric definitions
- `02_data_model.md` — Data model and ETL pipeline design
- `03_dashboard_specs/` — Dashboard specifications and layout
- `04_automation_config.md` — Report automation and alert settings
- `05_review_report.md` — Quality review and optimization report

## Extension Skills

- **kpi-tree-builder**: KPI tree decomposition methodology, domain templates, threshold setting, drill-down design
- **chart-selector**: Chart type decision tree, per-chart rules, color palettes, layout principles

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No data source information | Design with domain-standard schema, specify customization points |
| Business objectives unclear | Propose domain-standard KPI frameworks, guide selection |
| Agent failure | Retry once > if still failing, proceed without that deliverable, note in review report |
| CRITICAL finding in review | Request correction from relevant agent > rework > re-verify (up to 2 rounds) |
