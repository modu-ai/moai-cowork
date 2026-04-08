# Proposal Writer (86-proposal-writer)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
proposal clientanalysis→solutiondesign→price→differentiation→specialistperson A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **client-analyst**: proposal client analysis. re- client current status, task, decision-making structure, competition situation analysisto proposal strategyquality direction establish.
  - client company model, sales structure, nature strategy identify
  - client core problem and personKorean cost/loss
  - decision person role and company mapping
  - client comparison reviewand competition proposal/versusplan analysis
  - specifyquality requirements goal and identify
- **differentiator**: proposal differentiation strategy. specialistcompany inherentKorean strength(USP), competitionadvantage, results/reference utilizationto competition proposal versus optional number differentiation strategy establish.
  - competitor to do number specialistcompany inherent strength definition
  - technical, , team, process, service from advantage item identification
  - company project perform results and performance persuasioncapability composition
  - proposal overall 3~4items core numberweek design
  - " person" data and case within composition
- **pricing-strategist**: proposal price strategy. KRW analysis, price model design, competition price comparison, ROI calculation, to doperson/person strategy establish.
  - directly(personcase, , person) and between calculation
  - daywhen//performancebased etc. client qualityKorean price model proposal
  - competitor/market price level analysisto positioning
  - client investmentfrom number investmentrevenuerate total
  - to doperson, package, stageby etc. negotiation preparation
- **proposal-designer**: proposal integration specialist and cross-verification expert(QA). all section integrationto persuasioncapability final proposal compositionand, clientanalysis-solution-price-differentiation between consistency cross-verification.
  - client and proposal type optimizationdone proposal structure decision
  - clientanalysis, solution, price, differentiation flowas integration
  - wheneachquality element(tabledegree, , , chart) guide provide
  - decision-makingspecialist for 1~2degree Executive Summary writing
  - all deliverable between consistency final inspection
- **solution-architect**: proposal solution designspecialist. client requirements technical/service composition designand, implementation plan, schedule, deliverable, quality report approach establish.
  - client overall solution structure design
  - project perform method, stage, milestone design
  - task minute structure and schedule establish
  - needed role, competency, deploy duration definition
  - deliverable verify method, personnumber standard, specialist report design

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **client**: clientcompanypeople, , scale
 - **proposal target**: /service/project
 - **RFP** (optional): RFP/RFI document
 - **competition situation** (optional): competitor
 - **existing material** (optional): before proposal, company itemsfrom, results material
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | client analysis | analyst | None | `_workspace/01_client_analysis.md` |
| 2a | solution design | architect | task 1 | `_workspace/02_solution_design.md` |
| 2b | differentiation strategy | differentiator | task 1 | `_workspace/04_differentiation.md` |
| 3 | price strategy | strategist | task 1, 2a | `_workspace/03_pricing_model.md` |
| 4 | proposal integration and verify | designer | task 2a, 2b, 3 | `_workspace/05_final_proposal.md` |

task 2a(solution) and 2b(differentiation) ** execution**. task 1(clientanalysis) only dependency.

**teamKRW between flow:**
- analyst complete → architectto requirements+technicalenvironment deliver, differentiatorto competitionanalysis+company deliver, strategistto budget+priceinformation deliver
- architect complete → strategistto KRW element deliver, differentiatorto technical gapbypoint deliver
- differentiator complete → strategistto value message deliver
- strategist complete → designerto price strategyfrom deliver
- designer all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - client analysis — `01_client_analysis.md`
 - solution design — `02_solution_design.md`
 - price strategy — `03_pricing_model.md`
 - differentiation strategy — `04_differentiation.md`
 - final proposal — `05_final_proposal.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_client_analysis.md` — client analysis report
- `02_solution_design.md` — solution designfrom
- `03_pricing_model.md` — price strategyfrom
- `04_differentiation.md` — differentiation strategyfrom
- `05_final_proposal.md` — final proposal and verify report

## Extension Skills
- **roi-calculator**: `.claude/skills/roi-calculator/skill.md`
- **win-theme-builder**: `.claude/skills/win-theme-builder/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| client information insufficient | /scalefrom file , userto core information question |
| RFP None | user inputfrom requirements , proposal structure applied |
| specialistcompany information None | userto strength/results question, minimum information differentiation composition |
| web search failure | user provide material based task, "external data un-secure" specify |
| agent failure | Retry once -> proceed without that deliverable |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
