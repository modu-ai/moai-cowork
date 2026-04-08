# Sustainability Audit (99-sustainability-audit)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
A sustainability audit harness. An agent team collaborates to produce environmental analysis, social assessment, governance review, ESG reporting, and improvement planning.

## Expert Roles
- **Environmental Analyst**: ESG environmental analyst. Assesses carbon emissions calculation, energy efficiency, waste management, water resource usage, and biodiversity impact.
  - Carbon Emissions Calculation: Calculate Scope 1 (direct), Scope 2 (indirect - electricity), and Scope 3 (value chain) emissions
  - Energy Efficiency Analysis: Evaluate energy consumption status, renewable energy share, and energy intensity
  - Waste Management Assessment: Assess waste generation volumes, recycling rates, and hazardous waste handling adequacy
  - Water Resource Management: Analyze water usage, water quality impact, and water stress area considerations
  - Environmental Regulatory Compliance: Review environmental impact assessments, emission standards, and compliance with environmental regulations
- **Esg Reporter**: ESG report writer. Compiles environmental, social, and governance assessment results into an integrated ESG report aligned with international frameworks such as GRI, SASB, and TCFD.
  - Framework Application: Apply GRI Standards, SASB, TCFD, ISSB (IFRS S1/S2), etc.
  - Materiality Assessment: Conduct Double Materiality analysis — financial materiality + impact materiality
  - Integrated Report Writing: Compile E/S/G assessments into a consistent, unified report structure
  - Data Visualization: Design ESG scorecards, trend charts, and benchmark comparisons
  - Stakeholder Communication: Design report executive summaries and key indicator dashboards
- **Governance Reviewer**: ESG governance reviewer. Reviews board structure, corporate ethics, compliance, risk management, information disclosure, and anti-corruption frameworks.
  - Board Structure Assessment: Evaluate independence, diversity, expertise, and existence of ESG committees
  - Corporate Ethics Framework: Assess code of ethics, whistleblowing systems, and conflict of interest prevention policies
  - Compliance: Review regulatory compliance systems, internal controls, and audit mechanisms
  - Risk Management: Evaluate enterprise risk management (ERM) and integrated ESG risk management
  - Disclosure Transparency: Assess ESG disclosure quality and stakeholder communications
- **Improvement Planner**: ESG improvement planner. Analyzes weaknesses across E/S/G pillars and develops prioritized improvement roadmaps, KPIs, and investment plans.
  - Gap Analysis: Analyze gaps between current levels and target levels (industry leadership, regulatory requirements, internal goals)
  - Prioritization: Determine task priority using an Impact x Feasibility matrix
  - Roadmap Design: Create short-term (1 year), medium-term (3 year), and long-term (5 year) improvement roadmaps
  - KPI Setting: Define measurable key performance indicators for each improvement initiative
  - Investment Planning: Estimate budget, personnel, and system investment required for improvements
- **Social Assessor**: ESG social impact assessor. Evaluates labor practices, human rights, diversity and inclusion, community contribution, and supply chain social responsibility.
  - Labor Practices Assessment: Diagnose working conditions, occupational safety, employee benefits, and labor relations
  - Human Rights Due Diligence: Identify human rights risks based on the UN Guiding Principles on Business and Human Rights (UNGPs)
  - Diversity, Equity & Inclusion (DEI): Evaluate gender, disability, and age diversity metrics and inclusive culture
  - Community Contribution: Assess social contribution activities, local economic impact, and stakeholder engagement
  - Supply Chain Social Responsibility: Evaluate supplier human rights/labor due diligence, conflict minerals, and child labor risks

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Company Information**: Company name, industry, size (revenue/headcount), listing status
    - **Audit Scope** (optional): Full E/S/G or specific pillars
    - **Existing Materials** (optional): Annual reports, existing ESG reports, emissions data
    - **Objectives** (optional): ESG rating target, regulatory compliance, investor requirements
    - **Constraints** (optional): Timeline, budget, specified reporting framework
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and use as reference materials
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Environmental Assessment | environmental | None | `_workspace/01_environmental_assessment.md` |
| 1b | Social Assessment | social | None | `_workspace/02_social_assessment.md` |
| 1c | Governance Assessment | governance | None | `_workspace/03_governance_assessment.md` |
| 2 | Integrated Report | reporter | Tasks 1a, 1b, 1c | `_workspace/04_esg_report.md` |
| 3 | Improvement Plan | planner | Tasks 1a, 1b, 1c, 2 | `_workspace/05_improvement_plan.md` |
| 4 | Cross-Validation | orchestrator | All | `_workspace/06_review_report.md` |

Tasks 1a, 1b, and 1c (E/S/G assessments) run **in parallel**. The three pillars can be assessed independently.

**Inter-Agent Communication Flow:**
- E/S/G analysts mutually: Cross-share inter-pillar issues (environmental -> social impact, governance -> environmental policies)
- E/S/G complete -> deliver pillar data and ratings to reporter
- E/S/G complete -> deliver weaknesses, risks, and improvement opportunities to planner
- reporter completes -> deliver report targets/commitments to planner
- orchestrator cross-validates overall consistency

### Phase 3: Integration and Final Deliverables

1. Verify consistency across all files in `_workspace/`
2. Detect discrepancies across E/S/G assessments, report, and improvement plan
3. Generate the cross-validation report
4. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Organization information and audit scope
- `01_environmental_analysis.md` — Environmental analysis report
- `02_social_assessment.md` — Social assessment report
- `03_governance_review.md` — Governance review report
- `04_esg_report.md` — ESG report
- `05_improvement_plan.md` — Improvement plan

## Extension Skills
- **Ghg Protocol**: GHG Protocol detailed guide. Referenced by the environmental-analyst agent when calculating and reporting greenhouse gas emissions. Use for 'GHG Protocol', 'carbon emissions', 'Scope 1/2/3', or 'carbon footprint' requests. Carbon credit trading and CDM project execution are out of scope.
- **Materiality Assessment**: ESG materiality assessment matrix. Referenced by the esg-reporter and improvement-planner agents when evaluating ESG issue materiality and setting priorities. Use for 'materiality assessment', 'importance analysis', or 'Materiality Matrix' requests. Stakeholder surveys and external certification are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Company data unavailable | Estimate using industry averages, attach "Estimate" label |
| Web search failure | Work with general ESG standards, note "Data limitations" |
| Industry-specific standards unknown | Search based on SASB industry classification, apply general standards if unavailable |
| Agent failure | Retry once -> if still fails, proceed with that pillar omitted |
| E/S/G inconsistency | Detected in cross-validation -> request corrections from relevant agent (up to 2 rounds) |
