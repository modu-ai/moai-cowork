# Technical Writer (81-technical-writer)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
technical document writing structuredesign→→diagram→review→versionmanagement A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **diagram-maker**: diagram writingspecialist. Mermaid grammaras diagram, when diagram, flowchart etc. technical document wheneach material creation.
  - whensystem composition element and annual total visualization
  - between communication flow, API order
  - decision-making flow, process stage
  - data model, total
  - status before, company
- **doc-writer**: technical document specialist. information design according to body text writingand, code example and includedKorean nature also technical document creation.
  - structure designfrom sectionby body text writing
  - execution possibleKorean code example writing, stageby description included
  - orderversus according toto do number stageby guide
  - endpoint, un-, , error code organization
  - day, tone consistency, style guide levelnumber
- **info-architect**: information designspecialist. technical document reader analysisand, quality document structure and table of contents designand, document typeby template provide.
  - target reader technical level, purpose, definition
  - API reference//guide/document/operations during quality type
  - information quality flow reflectedKorean totalquality table of contents composition
  - gap reference, condition, related document annual structure design
  - each section purpose, , expected minute guide
- **tech-reviewer**: technical reviewer(QA). document technicalquality accuracy, completeness, consistency, reader qualitynature verifyand specific revision feedback provide.
  - code example, API , description technicalqualityas matching
  - section, un-description items, done error without
  - , peoplepeople rule, code style document overallfrom dayqualityperson
  - target reader level description person
  - table of contents and body text dayvalue, diagram qualityKorean position existing
- **version-controller**: version managementspecialist. document data, change capability, version managementand, deployment preparation status confirm.
  - Semantic Versioning(Major.Minor.Patch) applied
  - each version change matters, change reason, impact scope basisrecord
  - writingspecialist, reviewer, status, category, management
  - final format, verify, data nature also confirm
  - document cycle, person responsible, basis standard definition

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **document week**: regarding documentperson
 - **document type** (optional): API//guide//operations
 - **target reader** (optional): role, technical level
 - **reference material** (optional): code, existing document, 
 - **existing file** (optional): existing document plan, structureplan
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | structure design | architect | None | `_workspace/01_doc_structure.md` |
| 2a | body text | writer | task 1 | `_workspace/02_doc_draft.md` |
| 2b | diagram writing | diagram | task 1 | `_workspace/03_diagrams.md` |
| 3 | technical review | reviewer | task 2a, 2b | `_workspace/04_review_report.md` |
| 4 | version management | version | task 1~3 | `_workspace/05_version_meta.md` |

task 2a(body text) and 2b(diagram) ** execution**. task 1(structure) only dependency when whenworkto do number .

**teamKRW between flow:**
- architect complete → writerto table of contents·content strategy, diagramto diagram requirement, versionto data deliver
- writer ↔ diagram: position, caption 
- reviewer body text+diagram cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)
- version review result reflectedto final data 

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. review reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - document structure — `01_doc_structure.md`
 - document body text — `02_doc_draft.md`
 - diagram — `03_diagrams.md`
 - review report — `04_review_report.md`
 - version — `05_version_meta.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_doc_structure.md` — document structure designfrom
- `02_doc_draft.md` — document body text plan
- `03_diagrams.md` — diagram 
- `04_review_report.md` — technical review report
- `05_version_meta.md` — version management data

## Extension Skills
- **diagram-patterns**: `.claude/skills/diagram-patterns/skill.md`
- **api-doc-standards**: `.claude/skills/api-doc-standards/skill.md`
- **code-example-patterns**: `.claude/skills/code-example-patterns/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| document week/scope people | reader·purpose afterreport present, optional also |
| technical taxdepartmentmatters insufficient | [confirm needed] , review when verify |
| code example verify impossible | "verify needed" tablewhen, readerto test |
| agent failure | Retry once -> proceed without that deliverable, note the gap in the review report |
| reviewfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
