# Competency Modeler (61-competency-modeler)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to perform the full competency modeling pipeline: job analysis → competency dictionary → assessment rubric design → development plan → competency matrix.

## Expert Roles
- **competency-architect**: Competency Architect. Defines competencies based on job analysis results, creates behavioral indicators, and designs proficiency level frameworks.
  - Competency Derivation: Cluster KSAs to derive higher-level competencies — typically 8–15
  - Competency Definition: Clearly describe each competency's name, definition, and sub-elements
  - Behavioral Indicator Development: Write observable behavioral indicators for each competency by proficiency level
  - Proficiency Level Design: Design a 5-level proficiency framework and define criteria for each level
  - Competency Classification: Classify competencies into core, leadership, and functional categories
- **development-planner**: Competency Development Planner. Creates individual and organizational competency development plans based on gap analysis, and produces competency matrices.
  - Competency Gap Analysis: Analyze the gap between current and target levels for each competency
  - Development Plan Creation: Design competency development activities following the 70:20:10 principle (experience:relationships:education)
  - Learning Path Design: Provide step-by-step learning paths for each competency
  - Competency Matrix Creation: Build a 3-dimensional matrix of job × competency × level
  - ROI Estimation: Quantitatively estimate the expected returns on competency development investment
- **job-analyst**: Job Analyst. Performs job description writing, core task analysis, and KSA (Knowledge, Skill, Attitude) extraction.
  - Job Description Writing: Systematically describe the job's purpose, responsibilities, authority, and reporting lines
  - Task Analysis: Identify core tasks that comprise the job and assign weights based on frequency, importance, and difficulty
  - KSA Extraction: Identify the Knowledge, Skill, and Attitude required for each task
  - Job Context Analysis: Analyze organizational structure, industry characteristics, work environment, and stakeholders
  - Job Classification: Map to standard job classification systems such as NCS (National Competency Standards) and O*NET
- **rubric-designer**: Assessment Rubric Designer. Designs assessment criteria, scoring guides, and assessment tools for each competency.
  - Assessment Rubric Design: Create specific assessment criteria for each competency by proficiency level
  - Scoring Guide Creation: Provide detailed scoring guides for consistent evaluator ratings
  - Assessment Tool Design: Design appropriate assessment methods including self-assessment, supervisor assessment, peer assessment, and 360-degree feedback
  - Assessment Item Development: Develop assessment items such as Behavioral Event Interviews (BEI) and Situational Judgment Tests (SJT)
  - Reliability & Validity Assurance: Provide guidelines to ensure assessment consistency and accuracy

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Target Job**: The job title for which to build the competency model
    - **Organization Info** (optional): Industry, size, organizational culture
    - **Purpose** (optional): Hiring/evaluation/development/promotion/organizational design
    - **Grade Range** (optional): Specific grade or all grades
    - **Existing Materials** (optional): Existing job descriptions, competency frameworks
2. Create the `_workspace/` directory in the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If existing materials are provided, copy them to `_workspace/` and adjust the relevant phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Job Analysis | job-analyst | None | `_workspace/01_job_analysis.md` |
| 2 | Competency Dictionary | competency-architect | Task 1 | `_workspace/02_competency_dictionary.md` |
| 3 | Assessment Rubric Design | rubric-designer | Tasks 1, 2 | `_workspace/03_assessment_rubric.md` |
| 4a | Development Plan | development-planner | Tasks 1, 2, 3 | `_workspace/04_development_plan.md` |
| 4b | Competency Matrix | development-planner | Tasks 1, 2, 3 | `_workspace/05_competency_matrix.md` |

**Inter-agent Communication Flow:**
- job-analyst completes -> Delivers KSA mapping and task weights to competency-architect; delivers per-task performance standards to rubric-designer
- competency-architect completes -> Delivers competency definitions, behavioral indicators, and proficiency framework to rubric-designer; delivers competency list and proficiency framework to development-planner
- rubric-designer completes -> Delivers assessment result interpretation guide and gap analysis framework to development-planner
- development-planner synthesizes all information to produce the development plan and matrix

### Phase 3: Integration and Final Report

1. Review all files in `_workspace/`
2. Validate consistency across job analysis, competency dictionary, rubric, and development plan
3. Present the final summary to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_job_analysis.md` — Job analysis report
- `02_competency_dictionary.md` — Competency dictionary
- `03_assessment_rubric.md` — Assessment rubric
- `04_development_plan.md` — Competency development plan
- `05_competency_matrix.md` — Competency matrix

## Extension Skills
- **bars-assessment**: Specialized skill for designing BARS (Behaviorally Anchored Rating Scale) assessment tools. Used by the rubric-designer agent when defining behavioral anchors per competency and designing BEI questions and SJT items. Automatically applied in contexts involving 'BARS,' 'behavioral rating scale,' 'BEI interview,' 'SJT,' 'assessment center,' or 'behavioral anchors.' Actual assessment execution or psychometric validation (factor analysis) is outside the scope of this skill.
- **competency-modeler**: Comprehensive competency modeling pipeline. An agent team collaborates to execute the full workflow: job analysis, competency dictionary creation, assessment rubric design, development plan formulation, and competency matrix construction. Use this skill for requests such as 'build a competency model,' 'job analysis,' 'competency dictionary,' 'assessment rubric,' 'competency development plan,' 'competency matrix,' 'KSA analysis,' 'job description,' 'behavioral indicators,' or 'competency assessment.' If existing job descriptions or competency data are provided, the corresponding phase is augmented. Note: integration with actual HR systems (SAP HR, Workday), compensation structure design, and legal HR advisory are outside the scope of this skill.
- **ksa-taxonomy**: A specialized skill for building KSA (Knowledge, Skill, Ability) taxonomies in job analysis and mapping them to NCS/O*NET standards. Used by the job-analyst and competency-architect agents when writing job descriptions and systematically classifying competencies. Automatically applied in contexts involving 'KSA analysis,' 'job description,' 'NCS,' 'O*NET,' 'task analysis,' or 'competency classification system.' Note: actual NCS system access or HR system data integration is outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Insufficient job information | Collect similar job postings via web search; request additional information from the user |
| High industry specificity | Reference NCS/O*NET standards; leverage industry-specific terminology dictionaries |
| Organization info not provided | Work based on a typical mid-sized company; provide customization guide |
| Multiple job requests | Prioritize one core job; provide framework for the rest in the matrix |
| Agent failure | Retry once; if still failing, proceed without the affected deliverable |
