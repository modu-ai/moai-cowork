# Operations Manual (92-operations-manual)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
An automated operations manual generation harness. An agent team collaborates to analyze existing documents/code and generate process flowcharts, step-by-step manuals, FAQs, and training materials.

## Expert Roles
- **Document Analyst**: Existing document, code, and wiki analysis expert. Extracts current business processes from organizational assets, converts tacit knowledge into explicit knowledge, and creates glossaries and process inventories.
  - Source Inventory: List all documents/code/systems to analyze and assess each source's reliability
  - Process Extraction: Identify work procedures, decision points, and exception handling from documents and code
  - Tacit Knowledge Discovery: Extract undocumented know-how from code comments, commit logs, and configuration files
  - Glossary Creation: Define domain terms, abbreviations, and internal jargon to ensure manual consistency
  - Gap Analysis: Identify discrepancies between documented procedures and actual code/configurations
- **Faq Builder**: FAQ and troubleshooting guide expert. Anticipates questions and problems that arise during work execution and creates FAQs, troubleshooting decision trees, and escalation guides.
  - FAQ Creation: Organize frequently asked questions by category and write clear answers
  - Troubleshooting Guide: Create problem-solving guides with a symptom → cause → resolution structure
  - Decision Trees: Provide Yes/No branching guides in Mermaid for situations requiring complex judgment
  - Escalation Matrix: Organize contacts and procedures for cases that cannot be self-resolved
  - Terminology Explanations: Re-explain technical terms used in the manual from a non-expert perspective
- **Flowchart Designer**: Process flowchart design expert. Visualizes business processes as Mermaid diagrams and creates complete process maps including branching logic, parallel processing, and exception flows.
  - Process Map Design: Visualize the overall workflow as a high-level map
  - Detailed Flowcharts: Represent individual process steps, branches, and loops as Mermaid flowcharts
  - RACI Matrix: Define the Responsible (R), Accountable (A), Consulted (C), and Informed (I) parties for each step
  - Exception Flow Design: Represent error, rollback, and escalation paths separately from the normal flow
  - Sequence Diagrams: Supplement with sequence diagrams for processes involving inter-system or inter-team interactions
- **Manual Writer**: Step-by-step operations manual writing expert. Creates procedures, checklists, and screenshot guides that anyone can follow based on process analysis results.
  - Step-by-Step Procedures: Break down each process into actionable steps and describe them in sequence
  - Prerequisites: Clearly state required permissions, tools, and prior knowledge before each procedure
  - Checklist Generation: Provide completion verification checklists for each procedure
  - Screenshot Guide Placeholders: Mark screenshot insertion points and descriptions for steps involving UI interaction
  - Version Control Metadata: Manage manual version, creation date, and review cycle
- **Training Producer**: Training material production expert. Transforms manual content into learning-objective-based training materials, generating quizzes, hands-on exercises, summary cards, and onboarding checklists.
  - Learning Objective Design: Define learning objectives at knowledge/comprehension/application/analysis levels based on Bloom's Taxonomy
  - Summary Card Production: Compress key processes into one-page summary cards (cheat sheets)
  - Quiz Creation: Create multiple-choice and scenario-based quizzes for comprehension checks
  - Hands-on Exercise Design: Design practical scenarios that simulate the real work environment
  - Onboarding Checklist: Create a roadmap for new team members to progressively learn the manual

## Workflow
### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Target processes**: Scope of work/systems to document
    - **Source materials**: Existing document paths, code repositories, wiki URLs
    - **Target audience**: New hires/experienced staff/managers — manual users
    - **Constraints** (optional): Specific format requirements, existing manual templates
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If an existing manual is provided, copy to `_workspace/` and switch to update mode
5. Determine the **execution mode** based on the request scope (see "Execution Modes by Scope" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies:

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Document/code analysis | analyst | None | `_workspace/01_document_analysis.md` |
| 2 | Process flowcharts | designer | Task 1 | `_workspace/02_process_flowcharts.md` |
| 3a | Step-by-step manual | writer | Tasks 1, 2 | `_workspace/03_step_by_step_manual.md` |
| 3b | FAQ/troubleshooting | faq | Tasks 1, 2 | `_workspace/04_faq_troubleshooting.md` |
| 4 | Training materials | producer | Tasks 3a, 3b | `_workspace/05_training_materials.md` |

Tasks 3a (manual) and 3b (FAQ) run **in parallel**. Both depend only on Tasks 1 and 2, so they can start simultaneously.

**Inter-team communication flow:**
- analyst completes → sends process inventory/branching conditions to designer, raw procedure data/glossary to writer, gap analysis/tacit knowledge to faq
- designer completes → sends flowcharts/RACI to writer, exception flows to faq, Level 0 map to producer
- writer/faq complete → sends manual structure and key FAQ items to producer
- producer generates training materials from all deliverables and performs final consistency validation between manual and training materials

### Phase 3: Integration and Final Deliverables

The orchestrator performs final integration validation:

1. Verify all files in `_workspace/`
2. Cross-validation checklist:
    - [ ] All flowchart processes are described as procedures in the manual
    - [ ] All manual exception situations are reflected in the FAQ
    - [ ] All glossary terms are used consistently in the manual
    - [ ] Quiz content in training materials matches the manual
3. Request corrections from the relevant agent if discrepancies are found (up to 2 rounds)
4. Save validation results to `_workspace/06_review_report.md`
5. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — User input and analysis targets
- `01_document_analysis.md` — Existing document/code analysis results
- `02_process_flowcharts.md` — Process flowcharts (Mermaid)
- `03_step_by_step_manual.md` — Step-by-step operations manual
- `04_faq_troubleshooting.md` — FAQ and troubleshooting guide
- `05_training_materials.md` — Training materials package
- `06_review_report.md` — Integrated review report

## Extension Skills
- **Flowchart Standards**: Process flowchart standards guide. Notation and patterns referenced by the flowchart-designer agent when visualizing business processes in Mermaid. Used for 'flowchart standards', 'process diagram' requests. Note: BPM engine implementation is out of scope.
- **Knowledge Base Design**: Knowledge base design guide. Referenced by faq-builder and manual-writer agents when systematically organizing FAQs and troubleshooting guides. Used for 'FAQ design', 'knowledge management', 'troubleshooting guide' requests. Note: wiki system implementation is out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Source file inaccessible | analyst works with accessible sources only, lists "unanalyzed sources" in report |
| Process extraction impossible | Present interview questions for key processes to user, work from answers |
| Document contradictions | Prioritize code-based behavior, record contradictions in gap analysis |
| Mermaid rendering limitations | Split complex diagrams into sub-processes, supplement with text descriptions |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note omission in review report |
