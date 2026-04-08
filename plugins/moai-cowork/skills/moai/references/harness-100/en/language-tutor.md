# Language Tutor (56-language-tutor)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for foreign language learning: level testing, curriculum design, lessons, quizzes, and review management.

## Expert Roles
- **curriculum-designer**: Foreign language curriculum design expert. Designs customized curricula including learning objectives, phased study plans, textbook selection, and milestones based on level assessment results.
  - Goal Setting
  - Curriculum Structure
  - Content Selection
  - Skill Integration
  - Adaptive Planning
- **lesson-tutor**: Foreign language lesson tutor. Generates specific lesson materials including grammar explanations, vocabulary learning, conversation practice, and reading/writing tasks according to the curriculum.
  - Grammar Instruction
  - Vocabulary Building
  - Conversation Practice
  - Reading/Writing Tasks
  - Interactive Exercises
- **level-assessor**: Foreign language level assessment expert. Designs and administers CEFR-based diagnostic tests to precisely evaluate the learner's current level and analyze strengths and weaknesses by skill area.
  - Diagnostic Test Design
  - Level Determination
  - Skill Gap Analysis
  - Learning Readiness Assessment
  - Baseline Documentation
- **quiz-master**: Foreign language quiz expert. Creates various types of quizzes based on learned content, adjusts difficulty levels, and provides accurate scoring criteria and feedback.
  - Quiz Design
  - Difficulty Calibration
  - Scoring Rubrics
  - Detailed Feedback
  - Progress Measurement
- **review-coach**: Review coach. Designs spaced repetition learning based on the Ebbinghaus forgetting curve, develops weakness reinforcement plans, and manages overall learning progress.
  - Spaced Repetition Design
  - Weakness Reinforcement
  - Progress Tracking
  - Review Material Curation
  - Learning Plan Adjustment

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Target language**: Which foreign language the learner wants to study
    - **Native language**: The learner's native language (default: English)
    - **Learning experience**: Prior study experience and self-assessed current level
    - **Learning goal**: Travel / work / exam / immigration / hobby, etc.
    - **Available time**: Weekly hours available for study
    - **Existing materials** (optional): Prior study materials, exam scores, etc.
2. Create a `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`

### Phase 2: Team Assembly and Execution

| Order | Task | Agent | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Level assessment | level-assessor | None | `_workspace/01_level_assessment.md` |
| 2 | Curriculum design | curriculum-designer | Task 1 | `_workspace/02_curriculum.md` |
| 3 | First lesson | lesson-tutor | Task 2 | `_workspace/03_lesson_01.md` |
| 4 | First quiz | quiz-master | Task 3 | `_workspace/04_quiz_01.md` |
| 5 | Review plan | review-coach | Tasks 2, 3, 4 | `_workspace/05_review_plan.md` |

**Inter-agent communication flow:**
- level-assessor completes -> sends skill-area levels, strengths/weaknesses, learning goals, and available time to curriculum-designer
- curriculum-designer completes -> sends Week 1 topics, grammar, and vocabulary to lesson-tutor; sends milestone criteria to quiz-master
- lesson-tutor completes -> sends key learning items to quiz-master; sends learning items to review-coach
- quiz-master -> sends results to review-coach -> weakness reinforcement + review schedule generated

**Continuous learning cycle:**
Lessons, quizzes, and reviews run iteratively. When the user requests more lessons:
1. lesson-tutor generates the next lesson (`03_lesson_02.md`, `03_lesson_03.md`, ...)
2. quiz-master creates a quiz for that lesson (`04_quiz_02.md`, ...)
3. review-coach updates the review plan + generates a progress report

### Phase 3: Progress Reporting

review-coach periodically generates progress reports:
- `_workspace/06_progress_report.md` — Overall progress, skill-area growth, quiz trends, study patterns

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_level_assessment.md` — Level test results
- `02_curriculum.md` — Learning curriculum
- `03_lessons.md` — Lesson materials
- `04_quizzes.md` — Quizzes
- `05_review_plan.md` — Review plan
- `06_review_report.md` — Review report

## Extension Skills
- **spaced-repetition**: SM-2 algorithm, Ebbinghaus forgetting curve, review session design
- **cefr-assessment**: CEFR 6-level descriptors, adaptive diagnostic tests, CEFR-to-exam mapping

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Target language not specified | Default to English, but ask for confirmation |
| Level diagnosis refused | Set provisional level via self-assessment; adjust in first lesson |
| Agent failure | Retry once -> proceed without that deliverable if still failing |
| Difficulty mismatch | Adjust immediately based on learner feedback; update curriculum |
| Limited support for rare languages | Inform the user of supported range; focus on major languages (English, Japanese, Chinese, Spanish, French, German) |
