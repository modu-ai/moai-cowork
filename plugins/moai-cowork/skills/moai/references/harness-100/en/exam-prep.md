# Exam Prep (57-exam-prep)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for exam preparation: exam trend analysis, weakness diagnosis, customized study plans, mock exams, and error analysis.

## Expert Roles
- **diagnostician**: Diagnostic assessment expert. Measures the learner's current proficiency level by subject area, identifies weaknesses, and provides the foundation for a customized study strategy.
  - Per-area proficiency measurement
  - Weakness identification
  - Strength-weakness mapping
  - Learning style analysis
  - Goal gap analysis
- **error-analyst**: Error analysis expert. Analyzes mock exam results to identify error patterns, diagnose concept deficits, and formulate targeted remediation strategies.
  - Error pattern classification
  - Concept deficit tracking
  - Error notebook generation
  - Weakness update
  - Remediation suggestions
- **examiner**: Mock exam creator. Designs mock exams that match the real exam in format, difficulty, and timing, and writes detailed answer explanations.
  - Question creation
  - Difficulty design
  - Scoring design
  - Trap item design
  - Answer explanations
- **learning-designer**: Customized study plan designer. Creates a personalized learning curriculum, schedule, and materials based on diagnostic results.
  - Study priority determination
  - Schedule creation
  - Learning method matching
  - Study material assembly
  - Milestone setting
- **trend-analyst**: Exam trend analysis expert. Analyzes past exam question patterns, identifies frequently tested areas, tracks difficulty trends, and predicts likely topics for upcoming exams.
  - Past exam pattern analysis
  - Frequently tested areas
  - Difficulty trend tracking
  - Predicted topics
  - Trap classification

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Exam name**: Which exam is being prepared for (college entrance, civil service, certification, TOEIC, etc.)
    - **Subject/area**: All subjects or a specific subject
    - **Current level** (optional): Existing scores, mock exam results, self-assessment
    - **Goal** (optional): Target score, pass threshold
    - **Remaining time** (optional): Time until the exam
    - **Existing data** (optional): Score reports, error notebooks, study history
2. Create a `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing data is provided, copy it to `_workspace/` and adjust the relevant phase accordingly
5. Determine the **execution mode** based on the scope of the request (see "Task-Scale Modes" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Agent | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Trend analysis | trend-analyst | None | `_workspace/01_trend_analysis.md` |
| 2 | Weakness diagnosis | diagnostician | Task 1 | `_workspace/02_diagnosis_report.md` |
| 3 | Study plan design | learning-designer | Tasks 1, 2 | `_workspace/03_learning_plan.md` |
| 4 | Mock exam creation | examiner | Tasks 1, 2, 3 | `_workspace/04_mock_exam.md`, `04_mock_exam_answer.md` |
| 5 | Error analysis | error-analyst | Task 4 | `_workspace/05_error_analysis.md` |

**Inter-agent communication flow:**
- trend-analyst completes -> sends frequently tested areas and trap types to diagnostician; sends predicted topics to learning-designer; sends frequency and difficulty data to examiner
- diagnostician completes -> sends weak areas, weakness types, and goal gap to learning-designer; sends weakness-focused item requests to examiner
- learning-designer completes -> sends study scope and difficulty guide to examiner
- examiner completes -> sends question sheet, answer key, and item design intents to error-analyst
- error-analyst completes -> feeds remediation items back to learning-designer; sends next-exam reflection items to examiner

### Phase 3: Integration and Final Report

1. Verify all files in `_workspace/`
2. Confirm that the error analysis remediation suggestions are reflected in the study plan
3. Report the final summary to the user:
    - Trend analysis — `01_trend_analysis.md`
    - Weakness diagnosis — `02_diagnosis_report.md`
    - Customized study plan — `03_learning_plan.md`
    - Mock exam question sheet — `04_mock_exam.md`
    - Mock exam answer key — `04_mock_exam_answer.md`
    - Error analysis — `05_error_analysis.md`

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_trend_analysis.md` — Exam trend analysis
- `02_diagnosis.md` — Diagnostic results
- `03_study_plan.md` — Study plan
- `04_mock_exam.md` — Mock exam
- `05_error_analysis.md` — Error analysis report
- `06_review_report.md` — Review report

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Exam info search failure | Ask user to confirm exam format directly; work from general knowledge |
| Insufficient past exam data | Analyze within available range; note "data limited" in report |
| User non-response (diagnostic items) | Substitute with self-assessment checklist; perform subjective diagnosis |
| Excessive subject scope | Process core subjects first; guide remaining subjects to follow-up requests |
| Agent failure | Retry once -> proceed without that deliverable if still failing |
