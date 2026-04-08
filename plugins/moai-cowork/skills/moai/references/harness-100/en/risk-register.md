# Risk Register (88-risk-register)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
project risk managementversus: riskidentification→probability·impactassessment→responsestrategyestablish→monitoringplan→statusreportto A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **assessment-analyst**: risk assessment analysis. probability·impact matrix, expectedtransfervalue(EMV), risk score , priority decision perform.
  - each risk occurrence probability 5stage(Very High/High/Medium/Low/Very Low) assessment
  - schedule/cost/quality/scope 4items from 5stage impact assessment
  - probability×impact matrix writingand risk arrangement
  - analysis possibleKorean risk expectedtransfervalue(EMV = probability × impactamount)
  - risk score based Critical/High/Medium/Low priority decision
- **monitoring-planner**: risk monitoring designspecialist. KRI(coreriskindicator), condition, monitoring cycle, review process design.
  - each risk coreriskindicator(Key Risk Indicator) definition
  - response plan standard people setting
  - risk priorityby inspection cycle decision
  - basis risk review meeting agenda item and process design
  - risk management process specialist effectnature verify company standard establish
- **report-writer**: risk status report writingspecialist. management dashboard, trend analysis, risk includedKorean comprehensive risk report writing.
  - current risk current status Korean reportweek dashboard writing
  - probability×impact matrix wheneachquality tablecurrent creation
  - risk score and pattern analysis
  - core decision-making matters 1degree summary
  - all deliverable between consistency confirm
- **response-strategist**: risk response strategy. riskby quality response strategy(avoidance/transfer/mitigation/acceptance) establishand, response plan and residual risk management.
  - (avoidance/transfer/mitigation/acceptance), opportunity(utilization///acceptance) strategy decision
  - specific action(Action), person responsible, schedule, budget includedKorean execution plan writing
  - response after residual risk(Residual Risk) assessment
  - response action specialistfrom occurrence 2gap risk identification
  - response cost versus risk decrease and comparison
- **risk-identifier**: risk identification expert. project nature systematic risk identification, RBS(Risk Breakdown Structure) writing, risk categoryby derive perform.
  - technical/schedule/cost/specialistKRW/external/ etc. categoryby Risk Breakdown Structure writing
  - person, checklist, SWOT, analysis techniqueas risk derive
  - cause-companycase-result structure peopleKorean risk technicaldocument(Risk Statement) writing
  - (Threat) and opportunity(Opportunity) minute
  - each risk 1gap responsibilityspecialist proposal

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **project overview**: people, goal, scale, duration
 - **project type**: IT/case/R&D//service etc.
 - **stakeholder**: core stakeholder and expectedmatters
 - **constraint condition** (optional): budget, schedule, technical, 
 - **existing material** (optional): existing risk list, 
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. existing material `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | risk identification | identifier | None | `_workspace/01_risk_identification.md` |
| 2 | probability·impact assessment | analyst | task 1 | `_workspace/02_risk_assessment.md` |
| 3 | response strategy establish | strategist | task 1, 2 | `_workspace/03_response_strategy.md` |
| 4 | monitoring plan | planner | task 2, 3 | `_workspace/04_monitoring_plan.md` |
| 5 | status report | writer | task 1, 2, 3, 4 | `_workspace/05_status_report.md` |

**teamKRW between flow:**
- identifier complete → analystto risk list·RBS, strategistto ·dependencynature deliver
- analyst complete → strategistto priority·EMV, plannerto score standard deliver
- strategist complete → plannerto ·natureindicator, writerto response summary deliver
- planner complete → writerto monitoring schedule·KRI deliver
- writer all deliverable cross-verification, dayvalue findings when applicable agent revision request (versus 2)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. writer consistency verify result reflected
3. Report the final summary to the user

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_risk_identification.md` — risk identification report
- `02_risk_assessment.md` — probability·impact assessment matrix
- `03_response_strategy.md` — response strategy planfrom
- `04_monitoring_plan.md` — monitoring plan
- `05_status_report.md` — risk status report

## Extension Skills
- **risk-scoring-matrix**: `.claude/skills/risk-scoring-matrix/skill.md`
- **risk-response-patterns**: `.claude/skills/risk-response-patterns/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| project information insufficient | identifier by day risk template provide, "[ needed]" specify |
| data None | analyst nature assessment versus, "[data secure after re-assessment]" tablebasis |
| web search failure | day degree based risk derive, report "reference limitation" specify |
| agent failure | Retry once -> proceed without that deliverable, report specify |
| consistency dayvalue | writer revision request → re-task (versus 2) |
