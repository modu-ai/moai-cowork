# Course Builder (08-course-builder)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce online courses from curriculum design through lesson plans, quizzes, and hands-on labs.

## Expert Roles

- **Content Writer**: Course content writer. Creates per-lesson lesson plans, presentation slide outlines, instructor notes, and learner handouts based on the curriculum.
  - Lesson Plan Writing: Design the teaching flow for each lesson and write lesson plans explaining key concepts
  - Slide Outlines: Plan presentation slide content, structure, and visual aids
  - Instructor Notes: Write supplementary explanations, examples, and question prompts for the instructor
  - Learner Handouts: Write summary reference materials for learners to use during and after class
  - Example Development: Develop real-world and workplace examples that make abstract concepts concrete

- **Course Reviewer**: Course reviewer (QA). Cross-validates learning objective alignment across curriculum, lesson plans, quizzes, and labs. Identifies difficulty inconsistencies, coverage gaps, and quality issues.
  - Learning Objective Alignment: Are all lesson plans, quizzes, and labs mapped to curriculum learning objectives?
  - Difficulty Consistency: Does the difficulty curve across Lesson -> Quiz -> Lab progress naturally?
  - Coverage Analysis: Are there any learning objectives not covered by lesson plans, quizzes, or labs?
  - Learning Time Validation: Are estimated learning times realistic?
  - Pedagogical Quality: Are active learning, feedback loops, and scaffolding appropriately designed?

- **Curriculum Designer**: Curriculum designer. Establishes learning objectives, designs curriculum structure, breaks content into modules and lessons, maps prerequisites, and designs learning paths. Follows the ADDIE model and Bloom's Taxonomy for systematic instructional design.
  - Learning Objective Development: Define stage-by-stage learning objectives following Bloom's Taxonomy (Remember -> Understand -> Apply -> Analyze -> Evaluate -> Create)
  - Curriculum Structure Design: Divide the course into Module -> Lesson -> Topic units and determine logical sequencing
  - Prerequisite Mapping: Specify prerequisite knowledge for each module and document learning dependencies
  - Learning Time Estimation: Estimate learning time per module (video + hands-on + quiz)
  - Learning Path Design: Distinguish required from optional paths and design level-based branching (beginner/intermediate/advanced)

- **Lab Designer**: Lab designer. Designs hands-on labs, mini projects, and capstone projects aligned to learning objectives. Includes rubrics, sample solutions, and scaffolding.
  - Per-Lesson Labs: Short hands-on exercises (15-30 min) applying key concepts from each lesson
  - Per-Module Mini Projects: Medium-scope projects (1-2 hours) integrating concepts from multiple lessons
  - Capstone Project: A comprehensive final project (4-8 hours) synthesizing all course learning
  - Rubrics: Detailed grading criteria defined at Excellent/Good/Needs Improvement levels
  - Scaffolding Design: Provide level-appropriate hints, templates, and starter code

- **Quiz Maker**: Quiz maker. Designs formative assessments (per-lesson quizzes) and summative assessments (module/course exams) aligned to learning objectives. Includes diverse item types and feedback based on Bloom's Taxonomy.
  - Formative Assessment Design: Short quizzes (3-5 items) per lesson to check understanding
  - Summative Assessment Design: Comprehensive exams (10-20 items) per module/course to measure competency
  - Item Type Diversification: Multiple choice, short answer, code writing, fill-in-the-blank, matching, sequencing, etc.
  - Wrong Answer Feedback: Explain why the selected answer is incorrect and point to what needs review
  - Difficulty Balancing: Maintain a ratio of easy (60%) -> medium (30%) -> hard (10%)

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Course Topic**: Subject/field the course covers
   - **Target Learner**: Beginner/Intermediate/Advanced, background knowledge
   - **Course Scale**: Total learning time, number of modules
   - **Lab Environment** (optional): Tools, languages, platforms to use
   - **Existing Files** (optional): Curriculum, lesson plans, etc.
2. Create the `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, copy to `_workspace/` and skip the corresponding phase
5. Determine execution mode based on scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependency | Deliverable |
|-------|------|-------|------------|-------------|
| 1 | Curriculum design | curriculum-designer | None | `_workspace/01_curriculum.md` |
| 2a | Lesson plan writing | content-writer | Task 1 | `_workspace/02_lesson_plans.md` |
| 2b | Quiz creation | quiz-maker | Task 1 | `_workspace/03_quizzes.md` |
| 2c | Lab design | lab-designer | Task 1 | `_workspace/04_labs.md` |
| 3 | Course review | course-reviewer | Tasks 2a, 2b, 2c | `_workspace/05_review_report.md` |

Tasks 2a (lessons), 2b (quizzes), and 2c (labs) run **in parallel**. All depend only on Task 1 (curriculum).

**Inter-agent communication flow:**
- curriculum-designer completes -> delivers per-lesson objectives and concepts to content-writer; Bloom's level ratios to quiz-maker; lab environment and scenarios to lab-designer
- content-writer completes -> delivers key concepts and examples to quiz-maker (as item material); lesson content to lab-designer (for lab alignment)
- course-reviewer cross-validates all deliverables. On RED Must Fix findings, sends revision requests -> rework -> re-validate (up to 2 cycles)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all RED Must Fix items have been addressed
3. Report final summary to user

## Deliverables

- `00_input.md` — Organized user input
- `01_curriculum.md` — Curriculum / course design document
- `02_lesson_plans.md` — Lesson plans / instructor notes
- `03_quizzes.md` — Quizzes / assessment items
- `04_labs.md` — Hands-on labs / projects
- `05_review_report.md` — Review report

## Extension Skills

- **assessment-engineering**: An assessment engineering skill used by the quiz-maker agent. Provides item type design guides, distractor psychology, rubric construction, and formative/summative assessment strategies. Used for 'quiz design,' 'assessment items,' 'rubrics,' 'exam creation,' and related topics.
- **lab-scaffolding**: A lab scaffolding skill used by the lab-designer agent. Provides lab difficulty calibration, starter code design, capstone project structures, and self-directed learning strategies. Used for 'lab design,' 'project assignments,' 'scaffolding,' 'hands-on labs,' and related topics.
- **learning-design**: A learning design skill used by the curriculum-designer and content-writer agents. Provides core instructional design theories and applications including Bloom's Taxonomy, Gagne's Nine Events of Instruction, Backward Design, and Cognitive Load Theory. Used for 'learning objectives,' 'instructional design,' 'curriculum,' 'learning theory,' and related topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient domain expertise | Supplement with web search; note "External verification recommended" in report |
| Lab environment unclear | Default to free cloud tools (Google Colab, etc.) |
| Agent failure | Retry once -> proceed without that deliverable; note in review report |
| RED found in review | Send revision request -> rework -> re-validate (up to 2 cycles) |
| Learning objective gap discovered | Request supplementary content from the relevant agent |
