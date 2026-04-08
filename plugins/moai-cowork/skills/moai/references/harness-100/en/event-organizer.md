# Event Organizer (89-event-organizer)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
event basis·operations: concept→venue→program→promotion→execution→companyafterassessmentto A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **concept-planner**: event concept basisspecialist. event goal, , target attendee, budget framework, core nature indicator design.
  - SMART goal(quality attendee number, , beforeexchange etc.) establish
  - event tone, , core message decision
  - attendee , expected value, basis analysis
  - overall budget categoryby allocation framework design
  - event nature to do core indicator definition
- **evaluation-analyst**: companyafter assessment analysis. KPI , attendee document, ROI analysis, derive, companyafter report writing.
  - concept basis KPI actual method design
  - attendee also research documentdegree design
  - investment versus and qualityas analysis
  - done point, improvementpoint, expected outside issue organization
  - management/stakeholder final report writing
- **logistics-manager**: logistics . venue , between arrangement, flow of movement design, equipment/technical, catering, planbefore management responsible.
  - scale, nature, when, cost Korean venue checklist writing
  - person, departmentversuswhen, etc.recordversus, etc. arrangement plan design
  - attendee flow of movement, VIP flow of movement, flow of movement minute design
  - sound system, , people, , actualtime etc. technical requirements definition
  - , basis, people, planwithin etc. departmentversus matters management
  - versus , grade response, insurance, response etc. establish
- **program-designer**: program specialist. event , tax composition, speaker management, content design.
  - taxby time allocation, , time optimization
  - , , , etc. decision
  - speaker standard, template, companybefore planwithin preparation
  - actualtime table, Q&A, , un- design
  - event overall progress versus and when writing
- **promotion-lead**: promotion responsible. channelby promotion strategy, content work, etc.record management, attendee communication responsible.
  - SNS, email, , etc. channelby promotion strategy establish
  - versus, degree , SNS post, email when writing
  - etc.record degree composition, , type design
  - etc.record confirm, person, companybefore planwithin etc. email when design
  - D-60department D-dayto stageby promotion schedule establish

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **event purpose**: for eventperson
 - **event type**: /taxun-///beforewhen/ etc.
 - **scale**: expected attendee number
 - **budget** (optional): total budget or 1person budget
 - **daywhen/venue** (optional): or condition
 - **constraint condition** (optional): number requirements
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. existing material `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | concept basis | planner | None | `_workspace/01_concept_plan.md` |
| 2a | logistics | logistics | task 1 | `_workspace/02_logistics_plan.md` |
| 2b | program design | designer | task 1 | `_workspace/03_program_design.md` |
| 3 | promotion plan | promotion | task 1, 2a, 2b | `_workspace/04_promotion_plan.md` |
| 4 | assessment framework | analyst | task 1, 2a, 2b, 3 | `_workspace/05_evaluation_framework.md` |

task 2a(logistics) and 2b(program) ** execution**. task 1(concept) only dependency.

**teamKRW between flow:**
- planner complete → logisticsto scale·budget·, designerto ·target·message deliver
- logistics + designer → between↔program consistency confirm
- logistics + designer complete → promotionto venue·program information deliver
- promotion complete → analystto promotion KPI deliver
- analyst all deliverable cross-verification, dayvalue findings when revision request (versus 2)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. analyst consistency verify result reflected
3. Report the final summary to the user

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_concept_plan.md` — concept basisfrom
- `02_logistics_plan.md` — logistics planfrom
- `03_program_design.md` — program designfrom
- `04_promotion_plan.md` — promotion planfrom
- `05_evaluation_framework.md` — assessment framework

## Extension Skills
- **budget-planning**: `.claude/skills/budget-planning/skill.md`
- **venue-evaluation**: `.claude/skills/venue-evaluation/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| event information insufficient | planner typeby basic template provide, "[detailed needed]" specify |
| budget un- | 3degree scale(/during/versus)by scenario provide |
| venue un- | logistics requirements checklist and recommendation standard provide |
| agent failure | Retry once -> proceed without that deliverable |
| consistency dayvalue | analyst revision request → re-task (versus 2) |
