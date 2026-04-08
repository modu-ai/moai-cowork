# Grant Writer (54-grant-writer)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates on grant and funding applications: announcement analysis, business plan writing, budget design, and submission verification.

## Expert Roles
- **announcement-analyst**: Grant/funding announcement analysis expert. Analyzes eligibility requirements, evaluation criteria, scoring systems, and key keywords from announcements to provide the foundation for application strategy.
  - Eligibility Requirements Analysis
  - Evaluation Criteria Analysis
  - Key Keyword Extraction
  - Competition Analysis
  - Application Strategy Development
- **budget-designer**: Budget design expert. Calculates per-category budgets compliant with announcement regulations, and creates matching fund plans, execution plans, and settlement guides.
  - Per-Category Budget Calculation
  - Unit Price Calculation Basis
  - Matching Fund Plan
  - Execution Plan
  - Settlement Guide
- **compliance-checker**: Compliance verification expert. Verifies that the business plan and budget fully comply with announcement requirements, and derives improvements for score optimization.
  - Final Eligibility Verification
  - Per-Evaluation-Item Compliance Assessment
  - Budget Regulation Compliance
  - Score Optimization Recommendations
  - Format Requirements Check
- **plan-writer**: Business plan writing expert. Writes business plans optimized for evaluation criteria based on announcement analysis results. Systematically describes technical merit, business viability, and execution capability.
  - Business Overview Writing
  - Technical Merit Description
  - Business Viability Description
  - Execution Capability Description
  - Implementation Plan Development
- **submission-verifier**: Submission verification expert (QA). Performs final verification of the application package completeness and creates submission checklists and submission guides.
  - Document Completeness Check
  - Format Requirements Check
  - Content Consistency Check
  - Submission Checklist Generation
  - Submission Guide Creation

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Announcement Information**: Announcement document, program name, administering agency (file or URL)
    - **Applicant Information**: Company/institution name, industry, size, core technology/product
    - **Business Idea**: Overview of the proposed project
    - **Existing Materials** (optional): Existing business plans, financial statements, resumes, etc.
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1 | Announcement Analysis | announcement-analyst | None | `_workspace/01_announcement_analysis.md` |
| 2a | Business Plan Writing | plan-writer | Task 1 | `_workspace/02_business_plan.md` |
| 2b | Budget Preparation | budget-designer | Tasks 1, 2a | `_workspace/03_budget_plan.md` |
| 3 | Compliance Verification | compliance-checker | Tasks 1, 2a, 2b | `_workspace/04_compliance_report.md` |
| 4 | Submission Verification | submission-verifier | Tasks 1-3 | `_workspace/05_submission_checklist.md` |

**Inter-team Communication Flow:**
- announcement-analyst completes → delivers evaluation criteria, keywords, strategy to plan-writer; delivers budget regulations to budget-designer
- plan-writer completes → delivers implementation plan and resource needs to budget-designer
- compliance-checker cross-validates business plan + budget. If 🔴 Disqualification Risk found, sends revision request (up to 2 times)
- submission-verifier performs final completeness verification of all documents

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 items from compliance report are resolved
3. Report the final summary to the user

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_announcement_analysis.md` — Announcement analysis
- `02_business_plan.md` — Business plan
- `03_budget.md` — Budget plan
- `04_compliance_review.md` — Compliance review
- `05_submission_checklist.md` — Submission checklist
- `06_review_report.md` — Review report

## Extension Skills
- **budget-rule-engine**: Per-category ceiling rules, labor cost rate tables, calculation basis templates, settlement preparation

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Announcement not provided | Search for announcement by program name via web; if unsuccessful, request from user |
| Insufficient business info | Write general framework based on industry/technology, mark as [Confirmation Required] |
| Eligibility non-compliance found | Analyze alternatives (consortium, joint application, requirement supplementation) |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note omission |
| Regulation violation found | Send revision request → rework → re-validate (up to 2 times) |
