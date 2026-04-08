# Hiring Pipeline (90-hiring-pipeline)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
hiring process: JDwriting→sourcing→screening→interview→assessment→offerto A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **interview-designer**: interview designspecialist. structure interview, competency based question, interviewer guide, evaluation form design.
  - interview stage, time, interviewer composition design
  - STAR technique based action interview question design
  - jobby technical competency assessment method design
  - interviewer companybefore training material and progress guide writing
  - interview after writingto do structuredone evaluation form design
- **jd-writer**: JD writing expert. jobanalysis, competencydefinition, job description(Job Description), hiringposting writing.
  - degree core responsibility, expected performance, reporting total definition
  - required(Must-have) and preferred(Nice-to-have) competency minute
  - withindepartment official JD writing
  - external when capabilityqualityperson hiringposting writing
  - from assessment and interview assessment basis competency standard organization
- **offer-coordinator**: assessment·offer total. final afterreport assessment comprehensive, report package design, offer writing, onboarding annualtotal responsible.
  - before stage assessment result integration analysis
  - grade, person, benefits includedKorean package design
  - official hiring proposal writing
  - grade/condition negotiation strategy and Korean also setting
  - overall pipeline consistency and nature verify
- **screening-expert**: screening expert. from assessment standard, companybefore task design, before/ screening guide writing.
  - capabilityfrom/portfolio assessment design
  - job related task or test design
  - 15~30minute companybefore interview question and assessment standard design
  - candidate comparison for scorecard design
  - each stageby and time standard setting
- **sourcing-specialist**: sourcing expert. hiring channel strategy, Full building, value message, hiring responsible.
  - jobby quality sourcing channel(hiringcompany, LinkedIn, recommendation, etc.)
  - candidate search , Boolean search design
  - candidateto report message/email template writing
  - company/team capability deliver content design
  - channelby beforeexchange, cost, duration tracking indicator setting

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **degree**: hiringto do job, grade
 - ** information**: companypeople, team composition, document
 - **hiring condition**: , , grade scope
 - **grade**: hiring deadline, hiring personKRW
 - **existing material** (optional): existing JD, applicant current status
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. existing material `_workspace/` companyand applicable Phase 
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | JD writing | writer | None | `_workspace/01_job_description.md` |
| 2 | sourcing strategy | sourcing | task 1 | `_workspace/02_sourcing_strategy.md` |
| 3 | screening design | screening | task 1 | `_workspace/03_screening_framework.md` |
| 4 | interview design | interview | task 1, 3 | `_workspace/04_interview_design.md` |
| 5 | assessment·offer | offer | task 1, 2, 3, 4 | `_workspace/05_evaluation_offer.md` |

task 2(sourcing) and 3(screening) ** execution**. task 1(JD) only dependency.

**teamKRW between flow:**
- writer complete → sourcingto target ·EVP, screeningto competency·assessmentstandard deliver
- sourcing complete → offerto market report level deliver
- screening complete → interviewto confirm needed competency deliver
- interview complete → offerto evaluation form structure·hiring recommendation standard deliver
- offer overall pipeline cross-verification, dayvalue findings when revision request (versus 2)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. offer consistency verify result reflected
3. Report the final summary to the user

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_job_description.md` — job description and hiringposting
- `02_sourcing_strategy.md` — sourcing strategy
- `03_screening_framework.md` — screening framework
- `04_interview_design.md` — interview designfrom
- `05_evaluation_offer.md` — final assessment and offer guide

## Extension Skills
- **competency-model**: `.claude/skills/competency-model/skill.md`
- **interview-scorecard**: `.claude/skills/interview-scorecard/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| job information insufficient | writer tablelevel JD template + guide provide |
| grade information None | sourcing market value research, 3stage scope proposal |
| web search failure | day degree based JD/sourcing strategy, "[market data un-reflected]" specify |
| agent failure | Retry once -> proceed without that deliverable |
| consistency dayvalue | offer revision request → re-task (versus 2) |
