# SOP Writer (83-sop-writer)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
standard operating procedure(SOP) processanalysis→procedure document→checklist→training materials→versionmanagement A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **checklist-designer**: SOP checklist designspecialist. procedure document core stage execution inspectiontable exchangeand, quality , dayday/weekbetween/monthbetween inspection checklist design.
  - procedure document each stage possibleKorean itemas exchange
  - next stage basis before mustwhen confirm to do quality document definition
  - dayday/weekbetween/monthbetween/minutebasisby basis inspection checklist design
  - example situation occurrence when i.e.when reference checklist writing
  - withindepartment/external company when preparation to do checklist writing
- **procedure-writer**: SOP procedure document writingspecialist. process analysis result basedas according toto do number peopleKorean stageby procedure document writing. ISO/ requirement department document applied.
  - versusclassification→duringclassification→taxdepartment stage totalquality procedure design
  - each stage perform method, judgment standard, weekmatters people technical
  - "approx. ~" conditionby minutebasis and each procedure specify
  - situation occurrence when response procedure and technical
  - ISO 9001/ basis requirements department document structure applied
- **process-analyst**: SOP process analysis. current work flow systematicas analysisand, input/capability/relatedspecialist/examplesituation identificationto procedure document writing based .
  - current process whenwork→to overall flow
  - Supplier-Input-Process-Output-Customer identification
  - process within degreepoint, between, dependencynature risk identify
  - each stageby responsibilityspecialist(R), approver(A), specialist(C), reportspecialist(I) definition
  - flow example/minutebasis situation and response procedure identification
- **training-developer**: SOP training materials workspecialist. procedure document and checklist basedas personcapability to do number training guide, scenario annual, assessment document work.
  - procedure document training purpose re-compositionKorean learning document writing
  - actual situation companyKorean and annual problem design
  - also /from/actualbasis assessment document development
  - currentfrom referenceto do number 1degree summary
  - training targetby and time design
- **version-controller**: SOP version management and cross-verification expert(QA). procedure document-checklist-training materials between consistency cross-verificationand, document version management total establish.
  - procedure document all core stage checklist reflecteddegree confirm
  - training materials procedure document content reflecteddegree confirm
  - overall document taxfrom , total, daydegree confirm
  - document change capability, person process, deployment total design
  - document to deployment degree definition

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **target process**: work/procedure regarding SOPperson
 - **applied scope**: target departmentfrom/team/
 - ** requirement** (optional): related , authentication(ISO, HACCP etc.)
 - **existing document** (optional): current , work technicalfrom, 
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | process analysis | analyst | None | `_workspace/01_process_analysis.md` |
| 2 | procedure document writing | writer | task 1 | `_workspace/02_procedure_document.md` |
| 3a | checklist design | designer | task 2 | `_workspace/03_checklists.md` |
| 3b | training materials work | developer | task 2 | `_workspace/04_training_materials.md` |
| 4 | version management and verify | controller | task 3a, 3b | `_workspace/05_version_control.md` |

task 3a(checklist) and 3b(training materials) ** execution**. task 2(procedure document) only dependency.

**teamKRW between flow:**
- analyst complete → writerto process flow+RACI+example deliver, designerto quality degreepoint deliver
- writer complete → designerto verify standard deliver, developerto difficulty stage+actualnumber case deliver
- designer complete → developerto checklist usage deliver
- controller all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - process analysis — `01_process_analysis.md`
 - tablelevel procedure document — `02_procedure_document.md`
 - checklist tax — `03_checklists.md`
 - training materials — `04_training_materials.md`
 - version management and verify — `05_version_control.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_process_analysis.md` — process analysis result
- `02_procedure_document.md` — tablelevel procedure document
- `03_checklists.md` — checklist tax
- `04_training_materials.md` — training materials
- `05_version_control.md` — version management and verify report

## Extension Skills
- **process-mapping**: `.claude/skills/process-mapping/skill.md`
- **checklist-design**: `.claude/skills/checklist-design/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| existing document None | user person based process re-composition, tablelevel reference |
| requirement people | applicable day framework web searchas research |
| agent failure | Retry once -> proceed without that deliverable, verify report specify |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| process | process minuteto eacheach SOP creation |
