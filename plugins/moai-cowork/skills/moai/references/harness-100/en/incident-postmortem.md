# Incident Postmortem (25)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness that collaborates to generate incident postmortem reports. Automates the pipeline of timeline reconstruction -> root cause analysis -> impact assessment -> remediation planning -> report generation.

## Expert Roles
- **Impact Assessor**: Impact assessment expert. Quantitatively assesses user impact, revenue impact, SLA impact, and reputation impact of incidents, providing a comprehensive business impact evaluation.
  - **User Impact**: Assess the number, percentage, region, and segment of affected users
  - **Revenue Impact**: Estimate direct revenue loss, opportunity cost, and compensation costs
  - **SLA Impact**: Assess SLA/SLO violation status, error budget consumption, and credit obligations
  - **Reputation Impact**: Evaluate social media reactions, press coverage, and customer churn risk
  - **Operational Cost**: Assess personnel, time, and additional infrastructure costs invested in incident response
- **Postmortem Reviewer**: Postmortem reviewer (QA). Cross-validates consistency across timeline, root cause, impact, and remediation, and ensures blameless culture is maintained.
  - **Timeline-Cause Consistency**: Do timeline events logically align with the root cause analysis?
  - **Cause-Remediation Consistency**: Do countermeasures exist for all root causes and contributing factors?
  - **Impact-Remediation Proportionality**: Is the scale of countermeasures proportional to the severity of impact?
  - **Blameless Culture**: Are there no expressions blaming specific individuals? Is the focus on systems/processes?
  - **Executability**: Do all action items satisfy the SMART principle?
- **Remediation Planner**: Remediation planning expert. Establishes short/mid/long-term countermeasures for root causes and contributing factors, generating actionable action items with ownership and deadlines.
  - **Short-term Actions (Immediate~1 week)**: Establish immediate risk mitigation measures
  - **Mid-term Actions (1~4 weeks)**: Design systematic improvements such as process changes and monitoring enhancements
  - **Long-term Actions (1~3 months)**: Plan fundamental improvements such as architecture changes and cultural shifts
  - **Action Item Management**: Specify owner, deadline, and tracking method for each countermeasure
  - **Effectiveness Verification Criteria**: Set KPIs to measure the effectiveness of each countermeasure
- **Root Cause Investigator**: Root cause investigation expert. Traces from surface symptoms to root causes using 5 Whys, Fishbone diagrams, and Fault Tree Analysis.
  - **5 Whys Analysis**: Starting from the surface symptom, repeat "Why?" five or more times to derive the root cause
  - **Fishbone (Ishikawa) Diagram**: Classify causes across People, Process, Technology, and Environment dimensions
  - **Fault Tree Analysis**: Decompose the incident into a tree structure to identify necessary/sufficient conditions
  - **Contributing Factor Identification**: Find contributing factors that exacerbated the incident beyond the direct cause
  - **Evidence-based Verification**: Collect evidence/counter-evidence for each hypothesis to validate conclusions
- **Timeline Reconstructor**: Incident timeline reconstruction expert. Collects incident-related events, orders them chronologically, and identifies gaps to reconstruct an accurate incident progression.
  - **Event Collection**: Collect related events from logs, alerts, chat records, deployment history, metric changes, etc.
  - **Chronological Ordering**: Sort all events by UTC timestamp
  - **Gap Identification**: Identify intervals with missing information and flag items needing further investigation
  - **Key Transition Marking**: Highlight critical transition points such as incident start, detection, escalation, mitigation, and recovery
  - **Multi-source Correlation**: Correlate events from different sources to infer causal relationships

## Workflow
### Phase 1: Preparation (Performed directly by Orchestrator)

1. Extract from user input:
    - **Incident Description**: What happened and when
    - **Evidence** (optional): Logs, metric screenshots, chat records, alert records
    - **Impact Information** (optional): Number of affected users, services, duration
    - **Actions Taken** (optional): Emergency measures already performed
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on the scope of the request (see "Modes by Task Scale" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Assignee | Dependencies | Deliverable |
|-------|------|----------|-------------|-------------|
| 1 | Timeline Reconstruction | reconstructor | None | `_workspace/01_timeline.md` |
| 2a | Root Cause Analysis | investigator | Task 1 | `_workspace/02_root_cause.md` |
| 2b | Impact Assessment | assessor | Task 1 | `_workspace/03_impact_assessment.md` |
| 3 | Remediation Planning | planner | Tasks 2a, 2b | `_workspace/04_remediation_plan.md` |
| 4 | Final Review | reviewer | Tasks 1-3 | `_workspace/05_review_report.md` |

Tasks 2a (root cause) and 2b (impact) can be **executed in parallel**.

**Inter-team Communication Flow:**
- reconstructor completes -> delivers timeline and trigger candidates to investigator; delivers incident duration and metrics to assessor
- investigator completes -> delivers root cause and contributing factors to planner
- assessor completes -> delivers impact magnitude and SLA violation status to planner
- planner completes -> delivers full countermeasures to reviewer
- reviewer cross-validates all deliverables. Requests fixes for RED Must Fix items (up to 2 times)

### Phase 3: Integrated Report Generation

1. Generate `_workspace/postmortem_report.md` integrating all deliverables
2. Report structure: Summary -> Timeline -> Root Cause -> Impact -> Remediation -> What Went Well -> Lessons Learned
3. Deliver the final report to the user

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_timeline.md` — Incident timeline
- `02_root_cause.md` — Root cause analysis
- `03_impact_assessment.md` — Impact assessment
- `04_remediation_plan.md` — Remediation plan
- `05_review_report.md` — Review report
- `postmortem_report.md` — Final integrated postmortem report

## Extension Skills
- **rca-methodology**: Detailed guide for Root Cause Analysis (RCA) methodologies. Structured RCA techniques including 5 Whys, Fishbone diagrams, Fault Tree Analysis, change analysis, and a cognitive bias prevention checklist. Use this skill for 
- **sla-impact-calculator**: Calculation models and business impact matrices for quantitatively assessing incident impact based on SLA/SLO. Use this skill for 

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Insufficient incident information | Ask user additional questions, tag uncertain parts with "[Unconfirmed]" |
| Logs/metrics inaccessible | Reconstruct from verbal accounts, tag with "[Verbal account-based]" |
| Agent failure | Retry once -> if fails, proceed without that deliverable, note omission in review |
| RED found in review | Request fix from relevant agent -> rework -> re-verify (up to 2 times) |
| Blaming language found | Reviewer immediately requests fix — blameless culture is an absolute principle |
