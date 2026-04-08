# Coding Bootcamp (59-coding-bootcamp)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to deliver coding education: curriculum design, hands-on exercises, code review, projects, and portfolio building.

## Expert Roles
- **code-reviewer**: Code reviewer. Reviews learner code from quality, readability, performance, and pattern perspectives, providing specific improvement guidance.
  - Code quality assessment
  - Pattern analysis
  - Performance review
  - Security review
  - Learning feedback
- **curriculum-designer**: Curriculum designer. Creates step-by-step learning paths, selects tech stacks, and designs weekly schedules tailored to the learner's level and goals.
  - Level assessment
  - Goal setting
  - Tech stack selection
  - Step-by-step roadmap
  - Weekly schedule
- **exercise-creator**: Exercise creator. Designs coding problems by difficulty level, with test cases and solution guides, aligned to the curriculum.
  - Phase-by-phase exercise creation
  - Difficulty calibration
  - Test case writing
  - Hint system
  - Model solution writing
- **mentor**: Developer mentor. Provides real-world project design, portfolio building, technical interview preparation, and career guidance.
  - Project design
  - Portfolio strategy
  - Technical interview prep
  - Career guidance
  - Motivation management

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Current level**: Programming experience, languages used
    - **Goal**: Desired role, employment / career switch / side project
    - **Study time** (optional): Weekly available hours
    - **Duration** (optional): Target timeline
    - **Existing code** (optional): Code for review, existing projects
2. Create a `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Agent | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Curriculum design | curriculum-designer | None | `_workspace/01_curriculum.md` |
| 2 | Exercise creation | exercise-creator | Task 1 | `_workspace/02_exercises/` |
| 3a | Code review | code-reviewer | Task 1 | `_workspace/03_code_review.md` |
| 3b | Project design | mentor | Task 1 | `_workspace/04_project_spec.md` |
| 4 | Portfolio guide | mentor | Tasks 3a, 3b | `_workspace/05_portfolio_guide.md` |

Tasks 3a (code review) and 3b (project design) run **in parallel**.

**Inter-agent communication flow:**
- curriculum-designer completes -> sends weekly learning objectives to exercise-creator; sends per-phase quality expectations to code-reviewer; sends overall roadmap to mentor
- exercise-creator completes -> sends model solution verification request to code-reviewer; shares exercise-project connection points with mentor
- code-reviewer completes -> sends learner coding patterns and strengths/weaknesses to mentor
- mentor synthesizes all information to write the project spec and portfolio guide

### Phase 3: Integration and Final Report

1. Verify all files in `_workspace/`
2. Verify consistency across curriculum -> exercises -> project -> portfolio
3. Report the final summary to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_curriculum.md` — Curriculum
- `02_exercises.md` — Practice exercises
- `03_code_review.md` — Code review results
- `04_project_guide.md` — Project guide
- `05_review_report.md` — Review report

## Extension Skills
- **code-kata-generator**: 5-Tier difficulty system, exercise templates, test case design, scaffolding
- **tech-interview-prep**: UMPIRE problem-solving method, 4-step system design, STAR behavioral interviews, portfolio integration

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Learner level unclear | Assess with simple diagnostic coding problems |
| Goal undefined | Provide a general full-stack curriculum by default |
| Web search failure | Work from general technology trend knowledge |
| Specialized language/framework | Design around core principles; refer to language-specific resources |
| Agent failure | Retry once -> proceed without that deliverable if still failing |
