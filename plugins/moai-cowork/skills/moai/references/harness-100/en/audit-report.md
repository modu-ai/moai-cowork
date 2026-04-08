# Audit Report (94-audit-report)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
An internal audit report generation harness. An agent team collaborates to handle everything from audit scope design through checklist creation, findings analysis, improvement recommendations, and tracking ledger management.

## Expert Roles
- **Checklist Builder**: Audit checklist creation expert. Breaks down audit criteria into specific control items, test procedures, and evidence requirements to create field-ready checklists.
  - Control Item Decomposition: Break down each clause of audit criteria into testable control items
  - Test Procedure Design: Design specific verification methods for each control item (document review, interview, observation, reperformance)
  - Evidence Requirements: Specify the type and collection method for required evidence for each item
  - Sampling Plan: Set statistical sampling criteria for items where full population testing is impractical
  - Judgment Criteria: Objectively define criteria for conforming/nonconforming/observation determinations
- **Findings Analyst**: Audit findings analysis expert. Structures findings based on checklist results, assigns risk ratings, and performs root cause analysis and impact assessment.
  - Findings Structuring: Describe each finding using the 4C framework — Condition, Criteria, Cause, and Effect
  - Risk Rating: Classify finding severity as Critical/Major/Minor/Observation
  - Root Cause Analysis: Use 5 Whys or fishbone diagrams to identify root causes beyond surface-level symptoms
  - Impact Assessment: Evaluate financial impact, regulatory violation risk, operational impact, and reputational risk
  - Pattern Identification: Identify common patterns or systemic issues across individual findings
- **Recommendation Writer**: Improvement recommendation writing expert. Designs corrective actions for each finding and produces actionable improvement recommendations including implementation plans, expected benefits, and priorities.
  - Corrective Action Design: Design specific corrective actions that address each finding's root cause
  - Implementation Planning: Plan phased implementation schedules, owners, and required resources
  - Expected Benefits: Calculate quantitative/qualitative expected benefits of implementing recommendations
  - Prioritization: Prioritize considering risk level, urgency, and feasibility
  - Alternative Proposals: Present alternatives alongside primary recommendations to support decision-making
- **Scope Designer**: Audit scope design expert. Defines audit objectives, applicable standards (laws/regulations/policies), audit targets, audit period, and resource allocation, and produces the audit plan.
  - Audit Objective Definition: Clearly establish the audit purpose (adequacy/effectiveness/efficiency/compliance)
  - Audit Criteria Setup: Identify applicable laws, regulations, internal policies, and industry standards (ISO, COSO, etc.)
  - Audit Scope: Specifically define the audit scope including departments, processes, systems, and time periods
  - Risk-based Approach: Determine audit focus areas and priorities through risk assessment
  - Audit Schedule: Plan the schedule and resources for fieldwork, document review, interviews, etc.
- **Tracking Manager**: Implementation tracking ledger management expert. Tracks corrective action implementation status for audit findings and manages follow-up actions, closure criteria, and escalation procedures.
  - Tracking Ledger Design: Design a tracking ledger that integrates findings, recommendations, implementation schedules, owners, and status
  - Status Management: Define and track statuses: Not started/In progress/Completed/Delayed/Closed
  - Closure Criteria Definition: Objectively define closure conditions for each finding (evidence-based)
  - Escalation Procedures: Establish escalation procedures for issues such as deadline overruns and implementation refusals
  - Follow-up Audit Planning: Propose follow-up audit schedules for high-risk findings

## Workflow
### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Audit target**: Department, process, system, project
    - **Audit type**: Regular/Special/Follow-up
    - **Audit context**: Regulation changes, incidents, scheduled review
    - **Applicable criteria** (optional): Related laws, policies, industry standards
    - **Existing materials** (optional): Previous audit results, existing checklists
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing materials are provided, copy to `_workspace/` and determine whether to skip the relevant phase
5. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Audit scope design | scope | None | `_workspace/01_audit_scope.md` |
| 2 | Checklist creation | checklist | Task 1 | `_workspace/02_audit_checklist.md` |
| 3 | Findings analysis | findings | Tasks 1, 2 | `_workspace/03_audit_findings.md` |
| 4 | Recommendations | recommendation | Task 3 | `_workspace/04_recommendations.md` |
| 5 | Tracking ledger | tracking | Tasks 3, 4 | `_workspace/05_tracking_ledger.md` |

This workflow is **sequential by default**. Audit processes have strong step-by-step dependencies, limiting parallelization opportunities.

**Inter-team communication flow:**
- scope completes → sends audit criteria/risk assessment to checklist, criteria/rating framework to findings
- checklist completes → sends checklist result framework to findings
- findings completes → sends findings/root causes to recommendation, finding IDs/ratings to tracking
- recommendation completes → sends recommendations/implementation plans/deadlines to tracking
- tracking integrates all information to generate the tracking ledger

### Phase 3: Comprehensive Report Generation

The orchestrator generates the final comprehensive audit report:

1. Verify all files in `_workspace/`
2. Generate comprehensive report at `_workspace/06_final_report.md`:
    - Executive summary (1 page)
    - Audit scope and methodology
    - Findings summary and detail
    - Recommendation summary
    - Implementation tracking plan
3. Cross-validation:
    - [ ] Every finding has a corresponding recommendation
    - [ ] Every recommendation has an implementation deadline and owner
    - [ ] The tracking ledger includes all findings
    - [ ] Risk ratings are consistently applied
4. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Audit request and background
- `01_audit_scope.md` — Audit scope and plan
- `02_audit_checklist.md` — Audit checklist
- `03_audit_findings.md` — Findings report
- `04_recommendations.md` — Improvement recommendations
- `05_tracking_ledger.md` — Implementation tracking ledger
- `06_final_report.md` — Comprehensive audit report

## Extension Skills
- **Finding Classification**: Audit finding classification and reporting framework. Referenced by findings-analyst and recommendation-writer agents when systematically classifying findings and writing improvement recommendations. Used for 'finding classification', 'audit reporting', 'improvement recommendations' requests. Note: legal sanction decisions and disciplinary procedures are out of scope.
- **Internal Control Framework**: Internal control framework guide. Referenced by scope-designer and checklist-builder agents when designing audit scope and control items. Used for 'COSO', 'internal controls', 'control testing' requests. Note: external audit representation and legal opinion preparation are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Unclear audit criteria | Apply COSO framework as default, request criteria confirmation from user |
| Insufficient audit target info | Present interview question list to user, work from answers |
| No findings | Write report with "conforming" conclusion, include preventive improvement suggestions |
| Insufficient evidence | Record as provisional findings, establish additional evidence collection plan |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note in report |
