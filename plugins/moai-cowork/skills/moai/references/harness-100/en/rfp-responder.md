# RFP Responder (55-rfp-responder)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to create RFI/RFP responses: requirements analysis, capability matching, technical proposal, pricing proposal, and differentiation strategy.

## Expert Roles
- **capability-matcher**: Capability matching expert. Maps company performance records, personnel, and technical capabilities to RFP requirements based on requirements analysis, and derives gaps and remediation strategies.
  - Performance Record Matching
  - Team Composition
  - Technical Capability Mapping
  - Partner/Subcontractor Strategy
  - Differentiation Point Development
- **pricing-strategist**: Pricing strategy expert. Creates optimal price proposals considering cost estimation, pricing strategy, and competitive positioning.
  - Cost Estimation
  - Price Structure Design
  - Competitive Price Analysis
  - Pricing Strategy Development
  - Price Sensitivity Analysis
- **proposal-reviewer**: Proposal reviewer (QA). Cross-validates consistency across requirements analysis, capability matching, technical proposal, and pricing proposal, and checks differentiation strategy consistency and final completeness.
  - Requirements Fulfillment Verification
  - Consistency Cross-Validation
  - Differentiation Consistency Check
  - Evaluator Perspective Assessment
  - Differentiation Strategy Document
- **requirement-analyst**: RFP requirements analysis expert. Precisely dissects RFP/RFI documents to classify mandatory/optional requirements, and identifies per-criterion scoring and hidden needs.
  - RFP Structure Analysis
  - Requirements Classification
  - Evaluation Criteria Analysis
  - Hidden Needs Identification
  - Competitive Landscape Analysis
- **technical-proposer**: Technical proposal writing expert. Based on requirements analysis and capability matching, writes technical proposals including methodology, architecture, implementation schedule, and quality management plans.
  - Business Understanding
  - Technical Methodology
  - System Architecture Design
  - Implementation Schedule
  - Quality and Risk Management

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)
1. Extract from user input: RFP document, company info, track record, team info
2. Create `_workspace/` and save input to `00_input.md`

### Phase 2: Team Assembly and Execution
| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1 | Requirements Analysis | requirement-analyst | None | `01_requirement_analysis.md` |
| 2 | Capability Matching | capability-matcher | Task 1 | `02_capability_matrix.md` |
| 3 | Technical Proposal | technical-proposer | Tasks 1, 2 | `03_technical_proposal.md` |
| 4 | Pricing Proposal | pricing-strategist | Tasks 1, 2, 3 | `04_pricing_proposal.md` |
| 5 | Review + Differentiation | proposal-reviewer | Tasks 1-4 | `05_differentiation_strategy.md`, `06_review_report.md` |

### Phase 3: Integration and Final Deliverables

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_requirement_analysis.md` — Requirements analysis
- `02_capability_matching.md` — Capability matching table
- `03_technical_proposal.md` — Technical proposal
- `04_pricing_proposal.md` — Pricing proposal
- `05_review_report.md` — Review report

## Extension Skills
- **pricing-calculator**: Labor cost calculation, overhead/profit calculation, bidding strategy simulation

