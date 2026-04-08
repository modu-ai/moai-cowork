# Contract Analyzer (66-contract-analyzer)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
A contract analysis agent team harness.

## Expert Roles
- **clause-analyst**: Clause analyst. Identifies the structure of contracts, analyzes the legal meaning, effect, and scope of each clause, and identifies missing essential clauses.
  - Contract Structure Mapping: Map the overall structure including preamble, definitions, body, and appendices
  - Clause-by-Clause Interpretation: Analyze the legal meaning, scope, and effect of each clause
  - Essential Clause Verification: Verify the inclusion of essential terms required for the contract type
  - Definition Clause Validation: Verify the clarity, consistency, and appropriate scope of term definitions
  - Ambiguity Identification: Identify ambiguous expressions that could lead to legal disputes
- **clause-drafter**: Clause drafting and revision expert. Writes standard contract clauses, proposes improvements to existing clauses, and designs clauses that protect the parties' interests.
  - Standard Clause Writing: Write standard clauses adapted to the specific transaction for each contract type
  - Amendment Proposals: Propose specific revised wording for problematic clauses
  - Protective Clause Design: Add clauses that protect the user's interests (Party A or Party B perspective)
  - Missing Clause Supplementation: Draft additional clauses when essential clauses are missing
  - Terminology Unification: Unify terminology consistently throughout the contract
- **comparison-reviewer**: Comparison reviewer. Compares contracts against industry standards, previous versions, or counterparty drafts to analyze differences and derive negotiation points.
  - Standard Comparison: Analyze differences between the current contract and industry-standard contract templates
  - Version Comparison: Track changes from previous versions (redline)
  - Negotiation Point Derivation: Classify items to request modification and items open to concession
  - Market Practice Research: Research common contract practices in the industry via web search
  - Similar Contract Benchmarking: Evaluate appropriateness by referencing contract terms from similar transactions
- **contract-coordinator**: Contract coordinator (QA). Synthesizes clause analysis, amendments, risk assessment, and comparison review to produce a final legal opinion and verify consistency across deliverables.
  - Comprehensive Opinion Writing: Present an overall opinion on whether the contract should be signed
  - Deliverable Consistency Verification: Verify consistency across clause analysis, amendments, risk assessment, and comparison review
  - Priority Organization: Determine the final priority of items requiring modification/negotiation
  - Action Recommendations: Organize pre-signature verification items, need for ancillary documents, etc.
  - Checklist Generation: Create a final pre-signing verification checklist
- **risk-assessor**: Risk assessor. Identifies legal and business risks in contracts, discovers disadvantageous clauses, and presents risk mitigation strategies.
  - Legal Risk Identification: Identify legal risks such as contract invalidity, cancellation, and unfair clauses
  - Business Risk Identification: Assess business risks including financial loss, operational constraints, and opportunity costs
  - Disadvantageous Clause Discovery: Identify clauses that are excessively unfavorable to one party
  - Risk Matrix: Assess the probability and impact of each risk
  - Mitigation Strategy Presentation: Recommend specific mitigation measures for each risk

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Contract Text**: The contract to analyze (file or text)
    - **Contract Type**: Sale/Service/Lease/NDA/Employment/License, etc.
    - **Party Position**: User's position as Party A or Party B
    - **Special Concerns** (optional): Specific clauses, risks, comparison targets
    - **Comparison Target** (optional): Standard template, previous version
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If contract text is available, copy to `_workspace/original_contract.md`
5. Determine the **execution mode** based on the requested scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Clause Analysis | clause-analyst | None | `_workspace/01_clause_analysis.md` |
| 2a | Risk Assessment | risk-assessor | Task 1 | `_workspace/03_risk_assessment.md` |
| 2b | Comparison Review | comparison-reviewer | Task 1 | `_workspace/04_comparison_report.md` |
| 3 | Clause Drafting/Revision | clause-drafter | Tasks 1, 2a, 2b | `_workspace/02_draft_clauses.md` |
| 4 | Comprehensive Opinion | contract-coordinator | Tasks 1, 2a, 2b, 3 | `_workspace/05_final_opinion.md` |

Tasks 2a (Risk) and 2b (Comparison) are executed **in parallel**.

**Inter-agent Communication Flow:**
- clause-analyst completes -> Delivers risk clauses to risk-assessor, structural info to comparison-reviewer
- risk-assessor + comparison-reviewer complete -> Deliver modification requirements to clause-drafter
- clause-drafter completes -> contract-coordinator comprehensively verifies all deliverables
- contract-coordinator: If Red inconsistencies found, requests revision from relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that all Red required actions in the comprehensive opinion are reflected in the amendments
3. Report the final summary to the user:
    - Clause Analysis Report — `01_clause_analysis.md`
    - Amendments — `02_draft_clauses.md`
    - Risk Assessment — `03_risk_assessment.md`
    - Comparison Review — `04_comparison_report.md`
    - Comprehensive Opinion — `05_final_opinion.md`

## Deliverables


## Extension Skills
- **clause-risk-database**: A risk clause database that systematically identifies and grades risk patterns in contract clauses. The 'risk-assessor' and 'clause-analyst' agents must use this skill's pattern DB and scoring methodology when evaluating clause-level risk in contracts. Used for clause-level risk assessment tasks such as 'risk clause analysis', 'disadvantageous clause identification', 'risk scoring', etc. Note: Overall contract orchestration or contract drafting itself is outside the scope of this skill.
- **contract-analyzer**: A pipeline where an agent team performs contract analysis, drafting, review, and risk assessment. Use this skill for contexts such as 'review the contract', 'contract analysis', 'draft a contract', 'contract risk assessment', 'contract review', 'clause modification', 'contract comparison', 'NDA review', 'service agreement', 'lease agreement', 'employment contract', 'license agreement', and other contract management tasks. Note: Providing legal counsel, conducting litigation, notarization, and court document preparation are outside the scope of this skill.
- **negotiation-playbook**: A contract negotiation strategy and amendment proposal playbook. The 'clause-drafter' and 'comparison-reviewer' agents must use this skill's strategy framework and wording templates when drafting amendments or deriving negotiation points. Used for contract negotiation-related tasks such as 'negotiation strategy', 'amendment proposal', 'contract terms coordination', etc. Note: Overall contract orchestration or risk score calculation is outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| No contract text | Switch to drafting mode based on standard template for the contract type |
| Party position unclear | Analyze from both Party A and Party B perspectives, request position confirmation from user |
| Governing law unclear | Default analysis based on domestic law, note possibility of other applicable laws |
| Web search failure | Work based on general legal knowledge, note "latest case law unverified" |
| Agent failure | Retry once -> if failed, proceed without that deliverable, note omission in report |
