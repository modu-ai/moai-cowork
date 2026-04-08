# Procurement Docs (95-procurement-docs)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
A procurement document set generation harness. An agent team collaborates to produce everything from requirements definition through vendor comparison, evaluation criteria, contract review, and acceptance criteria.

## Expert Roles
- **Acceptance Builder**: Acceptance criteria creation expert. Designs inspection items, test procedures, and pass/fail criteria for deliverables to enable objective acceptance testing.
  - Inspection Item Derivation: Convert each requirement from the requirements specification into inspectable items
  - Test Procedure Design: Design specific test methods and procedures for each inspection item
  - Pass Criteria Definition: Quantify pass/conditional pass/fail determination criteria
  - Acceptance Schedule: Plan schedules for each acceptance phase (document review → functional test → performance test → final approval)
  - Defect Handling Procedures: Define procedures for remediation requests, re-inspection, and returns upon failure
- **Contract Reviewer**: Contract terms review expert. Analyzes procurement contract clauses, risk provisions, SLAs, intellectual property, and termination conditions, and identifies negotiation points.
  - Standard Contract Structure: Present standard contract structure and essential clauses appropriate to the procurement type
  - Risk Clause Analysis: Analyze risk clauses including penalties, damages, force majeure, and termination
  - SLA/SLO Definition: Design service level agreement metrics, targets, and penalties for non-compliance
  - Intellectual Property Review: Review clauses related to deliverable IP, licenses, and data ownership
  - Negotiation Point Identification: Develop negotiation strategies to secure favorable terms from the buyer's perspective
- **Evaluation Designer**: Evaluation criteria design expert. Designs evaluation criteria, scoring scales, and weighting for vendor/product selection, and establishes qualitative/quantitative assessment methodologies and consensus decision processes.
  - Evaluation Category Design: Define evaluation categories such as technical fit, price competitiveness, vendor capability, and support infrastructure
  - Weight Allocation: Allocate weights to each category/item based on procurement objectives and priorities
  - Scoring Criteria: Define specific 1-5 point (or 100-point) scoring criteria for each item
  - Qualitative/Quantitative Separation: Separate measurable items (quantitative) from judgment-based items (qualitative)
  - Evaluation Process Design: Propose evaluation panel composition, evaluation schedule, and consensus methods
- **Requirements Definer**: Procurement requirements definition expert. Systematically defines technical specifications, quantities, delivery dates, budgets, and required/optional requirements to produce the foundational document for vendor selection.
  - Technical Specification Definition: Describe functional and non-functional requirements of the procurement target in detail
  - Priority Classification: Classify requirements as Must-Have/Should-Have/Nice-to-Have (MoSCoW method)
  - Quantity, Delivery, and Budget Setting: Specify procurement quantity, delivery schedule, and budget range
  - Eligibility Criteria: Define minimum thresholds that vendors/products must meet
  - Stakeholder Requirements Integration: Consolidate requirements from various stakeholders including user departments, IT, finance, and legal
- **Vendor Comparator**: Vendor comparison analysis expert. Researches vendor/product candidates matching procurement requirements and creates multi-dimensional comparison tables covering features, pricing, track record, and support.
  - Candidate Vendor Research: Use web search to identify 3-5 vendor/product candidates matching requirements
  - Feature Comparison Table: Compare must/should/nice-to-have requirement fulfillment by vendor
  - Price Comparison Analysis: Compare initial costs, annual operating costs, and TCO (Total Cost of Ownership)
  - Reference Research: Research each vendor's similar project track record, customer reviews, and market share
  - SWOT Analysis: Analyze each vendor's Strengths/Weaknesses/Opportunities/Threats

## Workflow
### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Procurement target**: Goods, software, services, construction, etc.
    - **Procurement context**: New introduction, replacement, expansion, etc.
    - **Budget**: Budget range or limit
    - **Timeline**: Desired delivery date, project schedule
    - **Vendor candidates** (optional): Vendors already under consideration
    - **Existing documents** (optional): Existing specifications, contract drafts
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Requirements definition | definer | None | `_workspace/01_requirements_spec.md` |
| 2 | Vendor comparison | comparator | Task 1 | `_workspace/02_vendor_comparison.md` |
| 3a | Evaluation criteria | evaluator | Tasks 1, 2 | `_workspace/03_evaluation_criteria.md` |
| 3b | Contract review | contract | Tasks 1, 2 | `_workspace/04_contract_review.md` |
| 4 | Acceptance criteria | acceptance | Tasks 1, 3b | `_workspace/05_acceptance_criteria.md` |

Tasks 3a (evaluation) and 3b (contract) run **in parallel**.

**Inter-team communication flow:**
- definer completes → sends requirements/budget to comparator, priorities/criteria to evaluator, delivery/support terms to contract, must-have requirements/criteria to acceptance
- comparator completes → sends vendor info/comparison items to evaluator, license/clause highlights to contract
- contract completes → sends acceptance conditions/warranty to acceptance
- Orchestrator performs final cross-document consistency validation

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Cross-validation:
    - [ ] All must-have requirements are reflected in acceptance criteria
    - [ ] Evaluation criteria weight totals equal 100%
    - [ ] Contract terms align with requirements/acceptance criteria
    - [ ] Vendor comparison items map to requirements
3. Generate procurement summary report at `_workspace/06_procurement_summary.md`
4. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Procurement request and background
- `01_requirements_spec.md` — Procurement requirements specification
- `02_vendor_comparison.md` — Vendor comparison analysis
- `03_evaluation_criteria.md` — Evaluation criteria
- `04_contract_review.md` — Contract terms review
- `05_acceptance_criteria.md` — Acceptance criteria
- `06_procurement_summary.md` — Procurement summary report

## Extension Skills
- **Contract Checklist**: Procurement contract review checklist. Referenced by contract-reviewer and acceptance-builder agents when reviewing contract terms and establishing acceptance criteria. Used for 'contract review', 'contract terms', 'acceptance criteria' requests. Note: legal counsel and contract notarization are out of scope.
- **Vendor Scoring**: Vendor evaluation scorecard framework. Referenced by vendor-comparator and evaluation-designer agents when systematically comparing and evaluating vendors. Used for 'vendor evaluation', 'supplier comparison', 'bid evaluation' requests. Note: posting bid announcements and executing contracts are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Unclear procurement target | definer presents clarifying question list, works from answers |
| Insufficient vendor info | comparator provides RFI template when web search fails, requests user direct input |
| Budget undetermined | Estimate budget range based on market prices, proceed after user confirmation |
| Legal review needed | contract tags with "[Legal review needed]", warns cannot replace legal counsel |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note in report |
