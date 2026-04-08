# Public Speaking (85-public-speaking)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
comprehensive speechdocument→presentationversus→debatepreparationfrom→Q&Aexpectedanswer→rehearsalguide A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **audience-analyst**:  audience analysis. presentation/speech/debate target audience analysisand, context, expected, emotion status, companybefore degree level identifyto content strategy based .
  - personstatistics, , company, degree level identify
  - event type, venue, timeversus, minutecrisis, presentation analysis
  - audience presentationfrom basis KRW and identification
  - presentation before→during→after audience emotion design
  - audience value and message proposal
- **debate-preparer**: debate preparation expert. presentationspecialist argument and, expected counterargument regarding buildingand, quality gapdocument strategy establish.
  - presentation core argument qualityas report (argument-basis-case-re-)
  - audience/versus basisto do number counterargument exampleand classification
  - each expected counterargument regarding systematic preparation
  - versus weakness question strategy design
  - emotionquality , point regarding response method preparation
- **qa-strategist**: Q&A strategy. presentation after versusto expected question classificationand, each question regarding quality answer strategy and writing.
  - presentation content and audience nature basedKorean expected question systematicas derive
  - difficulty, type(information//before/), frequencyby question classification
  - each question regarding quality answer structure(STAR/Bridge/ABC) design
  - actual to do number specialistannual answer writing
  - question optional order, time management, question processing method design
- **rehearsal-coach**: rehearsal value and cross-verification expert(QA). presentation delivercapability rehearsal guide writingand, speechdocument-debatepreparation-Q&A between consistency cross-verification.
  - presentationdayto annual schedule and stageby goal design
  - within, , , , when etc. quality element guide provide
  - exampleannual scenario and assessment standard writing
  - presentation plan management quality·quality technique proposal
  - speechdocument-debatepreparation-Q&A between quality consistency and consistency inspection
- **speech-writer**:  speech/presentation work. audience analysis basedas persuasioncapability basis00M speechdocument and presentation versus writing. numbercompanyquality technique and story utilization.
  - 30 plan audience company department writing
  - quality beforeitems, story, numbercompanyquality technique utilizationKorean body text writing
  - section between specialistannual annualresult flow
  - core message summary and action (Call to Action) writing
  - , when, beforeexchange, etc. quality element

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **presentation type**: basisspeech/presentation/value/debate/interviewpresentation
 - **week**: presentation week and core message
 - **audience**: target audience nature
 - **time**: to do time
 - **context**: eventpeople, situation, by requirements
 - **existing material** (optional): before presentation material, , KRW
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | audience analysis | analyst | None | `_workspace/01_audience_analysis.md` |
| 2 | speechdocument writing | writer | task 1 | `_workspace/02_speech_script.md` |
| 3a | debate preparation | preparer | task 1, 2 | `_workspace/03_debate_prep.md` |
| 3b | Q&A strategy | strategist | task 1, 2 | `_workspace/04_qa_playbook.md` |
| 4 | rehearsal guide and verify | coach | task 3a, 3b | `_workspace/05_rehearsal_guide.md` |

task 3a(debate) and 3b(Q&A) ** execution**. task 1, 2 dependency.

**teamKRW between flow:**
- analyst complete → writerto audience file+emotion + deliver, preparerto audience also deliver, strategistto question direction deliver
- writer complete → preparerto core point+approx. point deliver, strategistto question point deliver
- preparer complete → strategistto counterargument list 
- coach all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - audience analysis — `01_audience_analysis.md`
 - speechdocument/presentation versus — `02_speech_script.md`
 - debate preparationfrom — `03_debate_prep.md`
 - Q&A — `04_qa_playbook.md`
 - rehearsal guide — `05_rehearsal_guide.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_audience_analysis.md` — audience analysis report
- `02_speech_script.md` — speechdocument/presentation versus
- `03_debate_prep.md` — debate preparationfrom
- `04_qa_playbook.md` — Q&A expected answer
- `05_rehearsal_guide.md` — rehearsal guide and verify report

## Extension Skills
- **rhetoric-patterns**: `.claude/skills/rhetoric-patterns/skill.md`
- **audience-engagement**: `.claude/skills/audience-engagement/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| audience information None | event typefrom general audience file , "estimation based" specify |
| presentation type people | presentation basicas applied |
| web search failure | user provide information and day degree based task |
| agent failure | Retry once -> proceed without that deliverable |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| debate needed | debate preparation , Q&A during |
