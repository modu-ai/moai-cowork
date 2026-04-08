# Product Manager (46)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to generate the full PM workflow: Roadmap, PRD, User Stories, Sprint Plan, and Retrospective.

## Expert Roles

- **PM Reviewer**: PM Reviewer (QA). Cross-validates consistency, feasibility, and gaps across the roadmap, PRD, user stories, and sprint plan.
  - Roadmap to PRD Consistency: Does the PRD reflect the roadmap's priority initiatives?
  - PRD to User Story Consistency: Have all PRD requirements been decomposed into user stories?
  - User Story to Sprint Consistency: Do story points fit within sprint capacity?
  - OKR to Success Metric Consistency: Are success metrics linked to OKR Key Results?
  - Feasibility Assessment: Is the overall plan realistically executable?

- **PRD Writer**: PRD Writer. Authors the product requirements document, defining exactly what the engineering and design teams need to build.
  - Problem Definition: Clearly articulate the user problem and business problem to be solved
  - Solution Definition: Describe the proposed solution, core features, and user flows
  - Scope Setting: Clearly distinguish In-scope vs. Out-of-scope items
  - Success Metrics: Define how the success of this feature will be measured
  - Technical Requirements: Specify non-functional requirements such as performance, security, accessibility, and compatibility

- **Sprint Planner**: Sprint Planner. Calculates team capacity, sets sprint goals, allocates stories, manages risks, and designs retrospective templates.
  - Team Capacity Calculation: Compute sprint capacity based on team size, available hours, and historical velocity
  - Sprint Goal Setting: Define clear sprint-level goals — "the one thing to achieve in this sprint"
  - Story Allocation: Assign stories to sprints based on dependencies, priorities, and capacity
  - Risk Management: Identify sprint risks, allocate buffers, and define escalation criteria
  - Retrospective Design: Create sprint retrospective frameworks and improvement action tracking templates

- **Story Writer**: Story Writer. Creates development-ready user stories from the PRD, including story maps, acceptance criteria (AC), and story points.
  - Story Map Design: Design the hierarchy of User Activities, Tasks, and Stories
  - User Story Writing: Use the format "As a [user], I want [feature], so that [value]"
  - Acceptance Criteria (AC): Define specific verification conditions using Given-When-Then format
  - Story Point Estimation: Estimate relative sizes based on complexity, uncertainty, and effort
  - Dependency Mapping: Identify sequential relationships and technical dependencies between stories

- **Strategist**: Product Strategist. Defines product vision, sets goals, builds roadmaps, operates prioritization frameworks, and establishes OKRs.
  - Product Vision Definition: Set the long-term (1-3 year) product direction and North Star Metric
  - OKR Setting: Define quarterly Objectives and Key Results
  - Roadmap Development: Design theme-based quarterly/semi-annual roadmaps
  - Prioritization Framework: Make systematic priority decisions using RICE/ICE/Kano and other frameworks
  - Stakeholder Alignment: Align expectations across executives, engineering, design, and marketing

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
    - **Product/Feature**: The product or feature to be planned
    - **Goals**: Business/user goals to achieve
    - **Team Info** (optional): Team size, role composition, velocity
    - **Constraints** (optional): Timeline, tech stack, resources
    - **Existing Assets** (optional): Existing PRDs, roadmaps, backlogs
2. Create the `_workspace/` directory at the project root
3. Organize input and save as `_workspace/00_input.md`
4. If existing files are present, skip the corresponding phase
5. **Determine the execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Roadmap development | strategist | None | `_workspace/01_product_roadmap.md` |
| 2 | PRD writing | prd-writer | Task 1 | `_workspace/02_prd.md` |
| 3 | User story decomposition | story-writer | Tasks 1, 2 | `_workspace/03_user_stories.md` |
| 4 | Sprint planning | sprint-planner | Task 3 | `_workspace/04_sprint_plan.md` |
| 5 | PM review | pm-reviewer | Tasks 1-4 | `_workspace/05_review_report.md` |

**Inter-agent communication flow:**
- strategist completes → sends initiatives, OKRs, and success metrics to prd-writer; sends personas and use cases to story-writer
- prd-writer completes → sends requirements, AC, and scope to story-writer; sends timeline and dependencies to sprint-planner
- story-writer completes → sends story list, dependencies, and total SP to sprint-planner
- pm-reviewer cross-verifies all deliverables. When RED Must Fix items are found, sends revision requests → rework (up to 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills

- **rice-prioritizer**: RICE score formula, Reach/Impact/Confidence/Effort scoring, supplementary frameworks
- **story-point-estimator**: Fibonacci scale reference, three-dimensional complexity assessment, velocity calculation, story decomposition criteria

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient product info | Strategist proposes 3 general product categories, then prompts user to choose |
| No team info | Plan based on a standard 4-6 person Scrum team |
| Agent failure | Retry once → if still failing, proceed without that deliverable and note the omission in the review report |
| RED found in review | Send revision request to the relevant agent → rework → re-verify (up to 2 iterations) |
