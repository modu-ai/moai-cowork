# Meeting Strategist (84-meeting-strategist)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
meeting strategy document agenda itemstructuredesign→backgroundmaterialresearch→decision-makingframework→meetingrecordtemplate→ A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **agenda-architect**: meeting agenda item designspecialist. meeting purpose people definitionand, agenda item structure, time allocation, attendee role, progress method design.
  - meetingfrom mustwhen nature to do goal people (information /decision-making/person/problem)
  - agenda item order, total(versusagenda item/agenda item), decision
  - each agenda itemby to do time and overall meeting time optimization
  - each agenda itemby presentationspecialist, debate specialist, decision-makingspecialist degree
  - each agenda item progress method(presentation→debate→decision, , table etc.) decision
- **background-researcher**: meeting background researchKRW. each agenda item neededKorean data, case, stakeholder analysis, before meeting decisionmatters researchto attendee judgment degreeKRW writing.
  - each agenda item neededKorean figure, current status, trend collection
  - agenda item impact key stakeholder and organization
  - before meetingfrom decisiondone matters current status confirm
  - company case, competitor , total case collection
  - attendee meeting before to do core material package composition
- **followup-planner**: meeting and cross-verification expert(QA). meeting after execution plan establishand, agenda item-background-framework-template between consistency cross-verification.
  - meeting after execution task, person responsible, deadline, tracking method design
  - meeting result to, , deliverto dodegree plan
  - basis task duringbetween inspection timing and reporting total design
  - task degreeannual, issue occurrence when reporting/response definition
  - agenda item-background-framework-template between consistency final inspection
- **framework-designer**: decision-making framework designspecialist. meetingfrom decision-making agenda item regarding judgment standard, option comparison matrix, risk assessment, derive method design.
  - each agenda item decision-making type by (day optional/during optional/ decision/Go-NoGo/specialistKRW allocation)
  - decision-making appliedto do assessment standard and duringvalue setting
  - versusplan standardby comparison matrix writing
  - each option risk and expected and analysis
  - table, , report etc. derive method proposal
- **template-builder**: meeting document template . meetingrecord, decisionmatters basisrecorddegree, table , report etc. meeting operations neededKorean all document template creation.
  - agenda item structure meetingrecord creation
  - decision-making result and basis basisrecord
  - meetingfrom derivedone task tracking design
  - meeting effectnature assessment feedback writing
  - meeting result reportingbasis for provide

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **meeting type**: basisreporting/decision-making/person/problem//
 - **meeting purpose**: natureandspecialist specific goal
 - **attendee**: personKRW, role, grade
 - **time**: example time
 - **existing material** (optional): before meetingrecord, agenda item plan, related report
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | agenda item structure design | architect | None | `_workspace/01_agenda_design.md` |
| 2a | background material research | researcher | task 1 | `_workspace/02_background_brief.md` |
| 2b | decision-making framework | designer | task 1 | `_workspace/03_decision_framework.md` |
| 3 | document template creation | builder | task 1, 2b | `_workspace/04_meeting_templates.md` |
| 4 | and verify | planner | task 2a, 2b, 3 | `_workspace/05_followup_plan.md` |

task 2a(backgroundresearch) and 2b(framework) ** execution**. task 1(agenda item) only dependency.

**teamKRW between flow:**
- architect complete → researcherto needed background material list deliver, designerto decision-making agenda item+initial option deliver
- researcher complete → designerto data+constraintcondition deliver, builderto companybefore information deliver
- designer complete → builderto basisrecord +table deliver
- planner all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - agenda item designfrom — `01_agenda_design.md`
 - background material — `02_background_brief.md`
 - decision-making framework — `03_decision_framework.md`
 - meeting document template — `04_meeting_templates.md`
 - — `05_followup_plan.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_agenda_design.md` — agenda item structure designfrom
- `02_background_brief.md` — background material 
- `03_decision_framework.md` — decision-making framework
- `04_meeting_templates.md` — meetingrecord and reporting template
- `05_followup_plan.md` — and verify report

## Extension Skills
- **decision-frameworks**: `.claude/skills/decision-frameworks/skill.md`
- **facilitation-techniques**: `.claude/skills/facilitation-techniques/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| meeting purpose people | userto meeting type and goal confirm question |
| attendee information None | role(facilitator/frombasis/attendee) design |
| web search failure | user provide material and day degree based task, "external data un-secure" specify |
| agent failure | Retry once -> proceed without that deliverable |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
