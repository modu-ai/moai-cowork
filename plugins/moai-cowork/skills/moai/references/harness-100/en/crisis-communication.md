# Crisis Communication (87-crisis-communication)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
crisis situation occurrence when situationidentify→messagestrategy→press release→Q&A→monitoringto agent team to integration crisis package creation .

## Expert Roles
- **media-monitor**: media monitoring and afterwithin response expert. ·SNS tracking, risk degree, afterwithin response strategy, crisis judgment standard establish.
  - , SNS, , search trend etc. channelby monitoring plan establish
  - /department/during ratio, core tracking standard design
  - , report, etc. 2gap crisis basis report standard setting
  - stageby afterwithin response scenario establish
  - crisis standard and proposal
- **message-strategist**: crisis message strategy. stakeholderby core message, communication tone, channel strategy, presentation design.
  - 3degree core message(companyactualperson·empathy·responseaction) design
  - each stakeholder message design
  - company/description/ etc. situationby qualityKorean decision
  - press release, SNS, withindepartmentdegree, clientreport etc. channelby message differentiation
  - ( 1time), 24time, 72time message roadmap establish
- **press-release-writer**: press release and official document writingspecialist. crisis situation press release, CEO fromKorean, official naturepeople writing.
  - un- structure crisis press release writing
  - CEO or versusperson people official document writing
  - detailed information confirm before i.e.when presentationto do initial document writing
  - KRW target withindepartment communication document writing
  - situation before afterwithin press release writing
- **qa-preparer**: crisis Q&A preparationspecialist. basisspecialist, person, withindepartment versusKorean expected question and answer guide, versusperson when writing.
  - stakeholderby question example
  - core message Korean answer template writing
  - Korean questionfrom core message beforeexchange degree document preparation
  - 1 core summary writing
  - also question, question, comparison question response strategy establish
- **situation-analyst**: crisis situation analysis. companyactualtotal identify, stakeholder mapping, crisis etc.grade , legal·quality risk identification perform.
  - confirmdone companyactual, un-confirm matters, estimation matters people minute
  - directly impact(moat, client, KRW) and between impact(weekweek, basis, media, versusduring) classification
  - 5stage crisis etc.grade(Critical/High/Medium/Low/Watch)
  - legal responsibility, possiblenature, ·reporting identification
  - companycase occurrencedepartment currentto and timeas organization

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **crisis situation**: day occurrence
 - ** information**: people, scale, 
 - **current status**: press coverage department, withindepartment persondegree timing, initial response department
 - **constraint condition** (optional): legal issue, matters, time constraint
 - **existing document** (optional): existing press release, withindepartment report etc.
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. existing document `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request ( "task scaleby mode" reference)

### Phase 2: team composition and execution

team compositionand task to do. task between dependency total next and :

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | situation analysis | analyst | None | `_workspace/01_situation_analysis.md` |
| 2 | message strategy | strategist | task 1 | `_workspace/02_message_strategy.md` |
| 3a | press release writing | writer | task 1, 2 | `_workspace/03_press_release.md` |
| 3b | Q&A preparation | preparer | task 1, 2 | `_workspace/04_qa_briefing.md` |
| 4 | monitoring plan | monitor | task 1, 2, 3a, 3b | `_workspace/05_monitoring_plan.md` |

task 3a(press release) and 3b(Q&A) ** execution**. task 2(messagestrategy) only dependency when whenworkto do number .

**teamKRW between flow:**
- analyst complete → strategistto crisisetc.grade·stakeholder· deliver
- strategist complete → writerto coremessage·tone·No-Go Phrases deliver, preparerto stakeholderby message deliver
- writer complete → preparerto official documentplan deliver (Q&A consistency secure)
- preparer complete → monitorto expected question pattern deliver
- monitor all deliverable cross-verificationto message consistency, scenario, inspection

### Phase 3: integration and final deliverable

 verify result basedas final deliverable organization:

1. `_workspace/` Verify all files in the directory
2. message consistency issue findings applicable agent revision request (versus 2)
3. Report the final summary to the user:
 - situation analysis report — `01_situation_analysis.md`
 - message strategyfrom — `02_message_strategy.md`
 - press release/document — `03_press_release.md`
 - Q&A when — `04_qa_briefing.md`
 - monitoring plan — `05_monitoring_plan.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_situation_analysis.md` — situation analysis report
- `02_message_strategy.md` — message strategyfrom
- `03_press_release.md` — press release/official document
- `04_qa_briefing.md` — Q&A when
- `05_monitoring_plan.md` — monitoring plan and afterwithin response guide

## Extension Skills
- **stakeholder-mapping**: `.claude/skills/stakeholder-mapping/skill.md`
- **media-response-templates**: `.claude/skills/media-response-templates/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| crisis information insufficient | analyst scenario basedas task, "[information limitation]" specify |
| web search failure | company crisis type day patternas versus, report " un-confirm" specify |
| legal judgment needed | ⚖️ tablebasis after ratereview needed matters by also organization, reportnumberquality version |
| agent failure | Retry once -> proceed without that deliverable, final reporting specify |
| message day findings | applicable agent revision request → re-task (versus 2) |
