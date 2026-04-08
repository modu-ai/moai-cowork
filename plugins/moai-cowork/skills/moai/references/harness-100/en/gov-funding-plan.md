# Government Funding Plan (45)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

Government funding proposal: a harness where an agent team collaborates to perform announcement analysis → business plan writing → technical writing → budget planning → submission review.

## Expert Roles

- **Announcement Analyst**: Announcement analyst. Systematically analyzes government funding program announcements including eligibility requirements, evaluation criteria, scoring weights, preferential considerations, and required documents.
  - Eligibility Analysis: Analyze applicant qualifications, company size/type restrictions, technology readiness level requirements
  - Evaluation Criteria Breakdown: Decompose scoring criteria, identify weight distribution, find high-leverage items
  - Preferential Considerations: Identify bonus points (regional, demographic, prior performance, etc.)
  - Document Requirements: List all required submission documents with specifications
  - Timeline Management: Key dates, submission deadlines, evaluation schedule

- **Biz Writer**: Business feasibility writer. Writes market analysis, commercialization strategy, marketing plan, expected outcomes, and utilization plan according to government business plan formats.
  - Market Analysis: Present target market size, growth trends, and opportunities
  - Commercialization Strategy: Outline go-to-market approach, sales channels, partnerships
  - Marketing Plan: Define marketing strategy, customer acquisition approach, branding
  - Expected Outcomes: Quantify expected economic, social, and technological impacts
  - Utilization Plan: Describe how results will be used, including technology transfer and IP strategy

- **Budget Planner**: Budget planner. Performs government R&D budget allocation by cost category, personnel cost calculation, indirect cost estimation, private co-funding allocation, and documentation guidance.
  - Cost Category Allocation: Allocate budget across personnel, equipment, materials, outsourcing, travel, and overhead
  - Personnel Cost Calculation: Calculate researcher costs based on government salary standards and effort rates
  - Indirect Cost Estimation: Apply proper indirect cost rates per regulations
  - Co-Funding Allocation: Distribute government funding vs. private matching requirements
  - Documentation Guidance: Specify required evidence documents for each cost item

- **Submission Reviewer**: Submission reviewer (QA). Cross-validates consistency between announcement requirements, technical section, business section, and budget. Identifies missing items, deduction factors, and assesses submission readiness.
  - Requirements Compliance: Verify all announcement requirements are met across all sections
  - Cross-Section Consistency: Ensure technical plan, business plan, and budget align with each other
  - Scoring Optimization: Verify that high-weight evaluation criteria are thoroughly addressed
  - Deduction Factor Check: Identify potential deduction items before submission
  - Document Completeness: Verify all required documents are prepared with correct formats

- **Tech Writer**: Technical section writer. Writes the technology development objectives, development content, technical differentiation, research methodology, and implementation framework according to government business plan formats.
  - Technology Development Objectives: Define clear, measurable technical goals aligned with the program
  - Development Content: Detail the technical approach, methodology, and development process
  - Technical Differentiation: Articulate what makes this technology unique vs. existing solutions
  - Research Methodology: Describe the R&D approach, tools, and validation methods
  - Implementation Framework: Present the team structure, timeline, and milestone-based execution plan

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Announcement/Program**: Program name, announcement document
    - **Applicant Info**: Company type, size, technology area
    - **Project Overview**: Technology description, development goals
    - **Existing Materials** (optional): Technical plans, business plans, prior proposals
2. Create `_workspace/` directory and save input to `_workspace/00_input.md`
3. Determine execution mode based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Announcement analysis | announcement-analyst | None | `_workspace/01_announcement_analysis.md` |
| 2a | Technical section | tech-writer | Task 1 | `_workspace/02_tech_section.md` |
| 2b | Business section | biz-writer | Task 1 | `_workspace/03_biz_section.md` |
| 3 | Budget planning | budget-planner | Tasks 1, 2a, 2b | `_workspace/04_budget_plan.md` |
| 4 | Submission review | submission-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a and 2b run **in parallel**.

**Inter-agent communication flow:**
- announcement-analyst completes > passes criteria to tech-writer and biz-writer, passes budget guidelines to budget-planner
- tech-writer completes > passes technical needs to budget-planner
- biz-writer completes > passes commercialization costs to budget-planner
- budget-planner completes > passes budget plan to submission-reviewer
- submission-reviewer cross-validates all deliverables. On CRITICAL findings, requests corrections > rework > re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all CRITICAL findings addressed
3. Report final summary to user

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and funding program information
- `01_announcement_analysis.md` — Funding announcement analysis
- `02_business_plan.md` — Business plan document
- `03_technical_plan.md` — Technical plan document
- `04_budget_plan.md` — Budget plan and justification
- `05_submission_review.md` — Final review and submission checklist

## Extension Skills

- **scoring-optimizer**: Evaluation scoring strategy, high-score tactics
- **budget-standard-checker**: Budget compliance verification, cost category standards

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No announcement document | Request user to provide the announcement or specify the program |
| Technical details insufficient | Request additional technical information from user |
| Budget standards unclear | Apply conservative estimates, flag for user review |
| Agent failure | Retry once > proceed without that deliverable |
