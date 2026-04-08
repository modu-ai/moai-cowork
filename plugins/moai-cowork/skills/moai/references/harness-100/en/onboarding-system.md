# Onboarding System (91-onboarding-system)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
New hire onboarding: A harness where an agent team collaborates to generate everything from checklists to training, mentor assignments, and 30-60-90 day plans.

## Expert Roles
- **Experience Reviewer**: Onboarding experience reviewer. Cross-validates the overall program for consistency, identifies improvements, and produces the final report.
  - Consistency Validation: Verify alignment across checklist, training, mentoring, and 30-60-90 day plan
  - Experience Flow Validation: Verify the flow feels natural from the new hire's perspective
  - Overload Validation: Ensure activities are not excessively concentrated in any specific period
  - Gap Validation: Ensure no essential items are missing (legal requirements, security training, etc.)
  - Final Report: Produce the comprehensive onboarding program report
- **Mentor Matcher**: Mentor/buddy matching expert. Defines mentor/buddy roles, establishes matching criteria, creates mentor guides, and designs relationship management processes.
  - Role Definition: Distinguish and define the roles of mentors (work guidance) and buddies (cultural adaptation)
  - Matching Criteria: Design selection criteria and matching algorithms for mentors/buddies
  - Mentor Guide: Provide activity guides and conversation topics for mentors
  - Meeting Framework: Design the structure, frequency, and agenda for regular 1:1 meetings
  - Relationship Management: Establish a system to evaluate and adjust mentor-mentee relationship effectiveness
- **Milestone Tracker**: 30-60-90 day milestone designer. Designs stage-by-stage goals, performance criteria, feedback systems, and progress tracking.
  - 30-Day Goals: Learning stage — Set goals for understanding the organization/role and building relationships
  - 60-Day Goals: Contributing stage — Set goals for independent work and small-scale achievements
  - 90-Day Goals: Performing stage — Set goals for full role ownership and visible results
  - Feedback System: Design the structure for regular manager-new hire feedback meetings
  - Progress Tracking: Design goal tracking documents and processes
- **Onboarding Architect**: Onboarding architect. Designs the onboarding checklist, schedule, milestones, and stakeholder roles from pre-boarding through the first 90 days.
  - Onboarding Checklist: Create checklists covering pre-boarding, Day 1, the first week, the first month, and up to 90 days
  - Schedule Design: Design a week-by-week onboarding schedule
  - Milestone Definition: Set completion criteria and success metrics for each stage
  - Stakeholder Roles: Define onboarding responsibilities for HR, managers, mentors, and team members
  - Environment Setup: Create checklists for IT equipment, accounts, and physical workspace preparation
- **Training Builder**: Training content builder. Designs onboarding training curriculum, learning materials, quizzes, and self-assessments.
  - Curriculum Design: Distinguish required vs. optional training and optimize sequencing
  - Learning Material Structure: Design the structure and format of training materials
  - Quizzes/Assessments: Design quizzes and self-assessments for comprehension checks
  - Learning Paths: Design customized learning paths by job role and level
  - Learning Guide: Provide guides and recommended resources for self-directed learning

## Workflow
### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **New hire info**: Role, level, employment type
    - **Organization info**: Team size, work arrangement (office/remote/hybrid)
    - **Start date**: First day
    - **Special requirements** (optional): Remote start, international hire, experienced/entry-level
    - **Existing materials** (optional): Existing onboarding docs, training materials
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing materials are provided, copy to `_workspace/` and adjust the relevant Phase
5. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Onboarding checklist | architect | None | `_workspace/01_onboarding_checklist.md` |
| 2a | Training program | builder | Task 1 | `_workspace/02_training_program.md` |
| 2b | Mentor guide | matcher | Task 1 | `_workspace/03_mentor_guide.md` |
| 3 | 30-60-90 plan | tracker | Tasks 1, 2a, 2b | `_workspace/04_30_60_90_plan.md` |
| 4 | Experience review | reviewer | Tasks 1, 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (training) and 2b (mentor) run **in parallel**. Both depend only on Task 1 (checklist).

**Inter-team communication flow:**
- architect completes → sends learning goals/system list to builder, role definitions to matcher
- builder + matcher share mutually → agree on mentor training responsibility areas
- builder + matcher complete → send training completion criteria and mentoring milestones to tracker
- tracker completes → sends 30-60-90 goals and feedback framework to reviewer
- reviewer cross-validates all deliverables; requests corrections for inconsistencies/overload (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Incorporate reviewer's consistency validation and overload analysis results
3. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_onboarding_checklist.md` — Onboarding checklist and schedule
- `02_training_program.md` — Training program
- `03_mentor_guide.md` — Mentor/buddy assignment guide
- `04_30_60_90_plan.md` — 30-60-90 day plan
- `05_review_report.md` — Onboarding experience review report

## Extension Skills
- **Buddy Program Guide**: Buddy/mentor program design guide. Referenced by the mentor-matcher agent when matching new hire mentors/buddies and structuring programs. Used for 'buddy program', 'mentor matching', 'onboarding buddy' requests. Note: HR system integration and actual personnel assignments are out of scope.
- **Learning Path Design**: Learning path design framework. Referenced by training-builder and onboarding-architect agents when designing new hire learning curricula. Used for 'learning path', 'curriculum design', 'training program' requests. Note: LMS system development and e-learning content production are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Insufficient role information | architect provides standard templates by job category |
| Unknown organization size | 3 versions: small (~20), medium (~100), large (100+) |
| Remote new hire | Include remote alternative activities for all items |
| Agent failure | 1 retry → proceed without that deliverable if still failing |
| Overload detected | reviewer requests activity redistribution → readjust (up to 2 rounds) |
