# Academic Paper (98-academic-paper)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
An academic paper writing harness. An agent team collaborates to produce research design, experiment management, statistical analysis, paper writing, and submission preparation.

## Expert Roles
- **Experiment Manager**: Academic experiment manager. Develops experiment protocols, data collection procedures, instrument/survey design, and pilot test plans based on the research design.
  - Experiment Protocol Writing: Document step-by-step procedures at a reproducible level of detail
  - Measurement Instrument Design: Design questionnaires, interview guides, experimental stimuli, etc.
  - Data Collection Planning: Establish collection methods, schedules, and quality control procedures
  - Pilot Testing: Develop preliminary study plans prior to the main experiment
  - Data Management Planning: Define data coding, storage, security, and sharing policies
- **Paper Writer**: Academic paper writer. Writes scholarly papers following the IMRaD structure, adhering to academic writing conventions and managing citations.
  - Paper Structure Design: Design the paper skeleton following the IMRaD (Introduction-Methods-Results-and-Discussion) structure
  - Introduction Writing: Develop the research background, prior literature, research purpose, and hypotheses in a logical progression
  - Methods Writing: Describe the research methods at a reproducible level of detail
  - Results Writing: Report analysis results objectively following the hypothesis sequence
  - Discussion Writing: Discuss result interpretation, theoretical and practical implications, limitations, and future research
- **Research Designer**: Academic research designer. Formulates research questions, develops hypotheses, selects research methodology, defines variables, and analyzes prior literature.
  - Research Question Formulation: Identify research gaps in prior literature and develop specific, answerable research questions
  - Hypothesis Development: Specify testable hypotheses (H1, H2, ...) grounded in theoretical reasoning
  - Methodology Selection: Determine the optimal methodology — quantitative/qualitative/mixed methods, experimental/survey/case study, etc.
  - Variable Definition: Operationally define independent, dependent, control, and mediating/moderating variables
  - Literature Analysis: Systematically organize relevant theories and prior studies to establish the scholarly positioning of the research
- **Statistical Analyst**: Academic statistical analyst. Develops statistical analysis strategies suited to the research design, generates analysis code, interprets results, and creates visualizations.
  - Analysis Strategy Development: Select statistical techniques suited to the research design and data characteristics
  - Preprocessing Plan: Design missing data handling, outlier detection, normality testing, and transformation strategies
  - Analysis Code Generation: Write analysis code in R or Python (statsmodels/scipy)
  - Results Interpretation: Distinguish between statistical significance and practical significance (effect size) in interpretation
  - Visualization: Design publication-quality tables and figures for academic papers
- **Submission Preparer**: Academic paper submission preparer. Manages target journal selection, journal-specific formatting, cover letters, reviewer suggestions, and submission checklists.
  - Target Journal Selection: Recommend journals considering research field, impact factor (IF), scope, and review turnaround time
  - Formatting: Adjust formatting to meet journal-specific submission guidelines (word count, reference style, figure format)
  - Cover Letter Writing: Write a cover letter to the editor-in-chief emphasizing the research's novelty, relevance, and contribution
  - Reviewer Suggestions/Exclusions: Prepare a list of 3-5 recommended reviewers and any exclusion requests
  - Submission Checklist: Verify all required documents per journal specifications

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Research Topic**: Research field, core keywords
    - **Research Level** (optional): Undergraduate/Master's/Doctoral/Faculty level
    - **Target Journal** (optional): Journal name, IF range
    - **Existing Materials** (optional): Data, drafts, literature lists
    - **Constraints** (optional): Deadline, length, special considerations
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Research Design | designer | None | `_workspace/01_research_design.md` |
| 2 | Experiment Protocol | experiment | Task 1 | `_workspace/02_experiment_protocol.md` |
| 3 | Statistical Analysis | analyst | Tasks 1, 2 | `_workspace/03_analysis_report.md` |
| 4 | Manuscript Writing | writer | Tasks 1, 2, 3 | `_workspace/04_manuscript.md` |
| 5 | Submission Preparation | preparer | Tasks 1, 4 | `_workspace/05_submission_package.md` |
| 6 | Integrated Review | orchestrator | All | `_workspace/06_review_report.md` |

**Inter-Agent Communication Flow:**
- designer completes -> delivers variables and sampling plan to experiment, hypotheses and analysis direction to analyst, theoretical background to writer, research field to preparer
- experiment completes -> delivers data structure to analyst, Methods materials to writer
- analyst completes -> delivers Results materials (APA format + Tables/Figures) to writer, analysis code to preparer
- writer completes -> delivers completed manuscript to preparer
- orchestrator cross-validates overall consistency (hypotheses <-> analysis <-> results <-> discussion)

### Phase 3: Integration and Final Deliverables

1. Verify consistency across all files in `_workspace/`
2. Validate logical consistency of hypotheses-analysis-results-discussion chain
3. Generate the integrated review report
4. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Research topic and conditions
- `01_research_design.md` — Research design document
- `02_experiment_protocol.md` — Experiment protocol
- `03_statistical_analysis.md` — Statistical analysis results
- `04_paper_draft.md` — Paper draft
- `05_submission_package.md` — Submission preparation package

## Extension Skills
- **Citation Standards**: Academic citation and reference standards guide. Referenced by the paper-writer and submission-preparer agents when composing citations and references. Use for 'citation format', 'APA', or 'references' requests. Original paper retrieval and professional database access are out of scope.
- **Research Methodology**: Research methodology guide. Referenced by the research-designer and statistical-analyst agents when selecting research designs and analysis methods. Use for 'research methodology', 'experiment design', or 'statistical analysis' requests. Actual data collection and IRB review processing are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Prior literature search failure | Work from user-provided references, note "Limited literature review" |
| Vague research topic | Propose 3 specific sub-topics and request user selection |
| No data available | Provide analysis strategy and code only, instruct "Run after data collection" |
| Agent failure | Retry once -> if still fails, proceed without that deliverable, note omission in review |
| Hypothesis-results mismatch | Paper writer addresses in Discussion, suggests post-hoc analyses |
