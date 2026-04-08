# Compliance Checker (67-compliance-checker)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
Regulatory compliance verification — an agent team collaborates to perform law mapping, status audit, gap analysis, and remediation planning.

## Expert Roles
- **gap-analyst**: Gap analyst. Analyzes the differences between legal requirements and current compliance status, calculates risk, and derives corrective action priorities.
  - Gap Identification and Classification: Specifically identify differences between legal requirements and current status, and classify by type
  - Risk Calculation: Calculate risk level for each gap using probability x impact
  - Root Cause Analysis: Analyze root causes of gaps (lack of awareness, insufficient resources, absent processes, etc.)
  - Priority Derivation: Determine action priorities by combining risk level, legal deadlines, and remediation difficulty
  - Benchmarking: Assess relative position by comparing against typical compliance levels in the same industry
- **law-mapper**: Compliance law analyst. Identifies laws, regulations, and standards applicable to the target business/service, and structures and maps obligations by clause.
  - Applicable Law Identification: Analyze business type, industry, data processing scope, and service targets to derive applicable laws
  - Obligation Extraction by Clause: Extract specific obligations the organization must fulfill from each law
  - Regulatory Hierarchy Structuring: Design a mapping structure reflecting the hierarchy of laws, enforcement decrees, enforcement rules, and notices
  - Penalty and Sanction Analysis: Organize the level of sanctions including administrative actions, fines, and penalties for violations
  - Regulatory Trend Monitoring: Use web search to check for recent amendments or legislative notices
- **remediation-planner**: Remediation planner. Based on gap analysis results, designs specific corrective action plans, schedules, responsibility assignments, and monitoring frameworks.
  - Corrective Action Design: Design specific corrective actions (policy/process/technology/training) for each gap
  - Execution Roadmap Development: Create short-term (30 days), mid-term (90 days), and long-term (180 days) roadmaps by priority
  - Resource Estimation: Estimate the personnel, budget, and technical resources needed for each corrective action
  - Monitoring Framework Design: Set KPIs and inspection cycles for continuously checking compliance status
  - Final Verification: Verify logical consistency across all reports and present a comprehensive opinion
- **status-auditor**: Status auditor. Investigates the organization's current regulatory compliance state, collects and classifies evidence, and assesses compliance status for each obligation.
  - Audit Design: Design inspection items and verification methods for each obligation
  - Evidence Collection and Classification: Systematically organize compliance evidence including policy documents, technical measures, and operational records
  - Compliance Level Assessment: Determine fully compliant / partially compliant / non-compliant / not applicable for each obligation
  - Status Report Writing: Objectively describe the organization's current compliance state
  - Risk Indicator Identification: Flag high-risk non-compliance items requiring immediate action

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Target Organization/Service**: Business type and scale of the audit target
    - **Industry/Sector**: Finance, IT, Healthcare, Manufacturing, Education, etc.
    - **Regulatory Domain** (optional): Personal data, finance, labor, environment, etc.
    - **Existing Materials** (optional): Policy documents, compliance reports, org charts, etc.
    - **Focus Areas** (optional): Specific law or specific domain
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing materials are available, copy to `_workspace/` and utilize for the relevant phase
5. Determine the **execution mode** based on the requested scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Law Mapping | law-mapper | None | `_workspace/01_law_mapping.md` |
| 2 | Status Audit | status-auditor | Task 1 | `_workspace/02_status_audit.md` |
| 3 | Gap Analysis | gap-analyst | Tasks 1, 2 | `_workspace/03_gap_analysis.md` |
| 4 | Remediation Plan | remediation-planner | Tasks 1, 2, 3 | `_workspace/04_remediation_plan.md` |

**Inter-agent Communication Flow:**
- law-mapper completes -> Delivers obligation checklist to status-auditor, mapping original to gap-analyst
- status-auditor completes -> Delivers compliance status to gap-analyst, existing infrastructure info to remediation-planner
- gap-analyst completes -> Delivers priority matrix and root cause analysis to remediation-planner
- remediation-planner cross-verifies logical consistency across all deliverables when writing the final report

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that the remediation plan's comprehensive opinion is consistent with law mapping, status audit, and gap analysis
3. Report the final summary to the user:
    - Law Mapping Report — `01_law_mapping.md`
    - Status Audit Report — `02_status_audit.md`
    - Gap Analysis Report — `03_gap_analysis.md`
    - Remediation Plan — `04_remediation_plan.md`

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_law_mapping.md` — Law mapping report
- `02_status_audit.md` — Status audit report
- `03_gap_analysis.md` — Gap analysis report
- `04_remediation_plan.md` — Remediation plan

## Extension Skills
- **audit-checklist-engine**: A systematic checklist generation engine for compliance audits. The 'status-auditor' and 'remediation-planner' agents must use this skill's audit framework and checklist templates when conducting status assessments and developing remediation plans. Used for 'audit checklist', 'compliance inspection form', 'compliance status assessment', etc. Note: Law mapping or full orchestration is outside the scope of this skill.
- **compliance-checker**: A full compliance verification pipeline. An agent team collaborates to perform law mapping, status audit, gap analysis, and remediation planning in a single pass. Use this skill for contexts such as 'check regulatory compliance', 'compliance check', 'legal compliance status', 'run gap analysis', 'regulatory response plan', 'legal risk analysis', 'compliance audit', 'regulatory inspection', 'compliance status assessment', and other compliance verification tasks. Note: Actual legal counsel (attorney opinions), litigation representation, administrative filings/submissions, and direct integration with legal databases (case law search systems) are outside the scope of this skill.
- **regulation-knowledge-base**: A structured knowledge base of key regulatory laws. The 'law-mapper' and 'gap-analyst' agents must use this skill's law database and mapping methodology when identifying applicable laws by industry and mapping obligations. Used for 'applicable law verification', 'regulatory mapping', 'obligation extraction', etc. Note: Full compliance orchestration or remediation planning is outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Web search failure | Law analyst works based on general knowledge, notes "latest amendments unverified" |
| Insufficient target organization info | Assume-based audit using general organization standards, note "assumption-based" |
| Agent failure | Retry once -> if failed, proceed without that deliverable, note omission in final report |
| Uncertain law applicability | Conservatively include, note "professional legal consultation recommended" |
| Gap analysis and status audit inconsistency | remediation-planner identifies inconsistency, applies conservative judgment |
