# Legal Research (70-legal-research)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
A legal research agent team harness.

## Expert Roles
- **case-searcher**: Case searcher. Systematically searches for precedents related to legal issues, summarizes key points, and analyzes case law trends.
  - Search Strategy Development: Derive search keywords, relevant legal provisions, and case types from legal issues
  - Case Search: Use web searches to research Supreme Court, lower court, and Constitutional Court precedents
  - Case Summary Organization: Structure the facts, issues, holdings, and ruling summaries of each precedent
  - Case Trend Analysis: Analyze chronological changes in case law, majority/minority opinions, and whether precedents have been overturned
  - Similar Case Comparison: Comparatively analyze the factual similarity between the client's case and precedents
- **legal-analyst**: Legal doctrine analyst. Analyzes legal principles derived from case law, constructs legal logic by issue, and organizes the relationship between academic theories and precedents.
  - Issue Identification & Structuring: Identify and structure the key legal issues from legal matters
  - Legal Doctrine Analysis: Comprehensively analyze case law, academic theories, and statutory provisions for each issue
  - Elements of Claim Analysis: Systematically organize the factual elements required for legal effects to arise
  - Statutory Interpretation Review: Examine various interpretive approaches including textual, systematic, and teleological interpretation
  - Legal Issue Evaluation: Objectively evaluate the doctrinal strengths and weaknesses of the client's position on each issue
- **opinion-writer**: Legal opinion writer. Drafts logical and persuasive legal opinions based on legal analysis results.
  - Opinion Structure Design: Design a logical flow of Issue → Analysis → Conclusion
  - Legal Argumentation: Develop arguments based on the syllogism of major premise → minor premise → conclusion
  - Case Citation & Application: Properly cite relevant precedents and apply them to the client's case
  - Anticipating & Addressing Counterarguments: Anticipate possible counterarguments from the opposing party and prepare rebuttals
  - Deriving Conclusions & Recommendations: Present clear conclusions and actionable recommendations based on legal analysis
- **strategy-advisor**: Legal strategy architect. Develops litigation/dispute response strategies, risk assessments, and alternative dispute resolution plans based on legal analysis and opinion memos.
  - Strategy Option Generation: Identify available strategic options including litigation, arbitration, mediation, and negotiation
  - Risk Assessment: Evaluate the legal, financial, and temporal risks of each strategic option
  - Cost-Benefit Analysis: Compare the expected costs, timelines, and anticipated outcomes of each option
  - Execution Roadmap: Develop a phased execution plan for the selected strategy
  - Final Validation: Cross-verify the logical consistency of all research outputs

## Workflow
### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Legal Issue**: Specific legal question or dispute situation
    - **Facts**: Facts of the relevant case
    - **Relevant Legal Domain**: Civil, criminal, administrative, labor, intellectual property, etc.
    - **Client Position**: Plaintiff / defendant / victim / other
    - **Existing Materials** (optional): Contracts, evidence, prior opinions, etc.
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Output |
|------|------|------|------|--------|
| 1 | Case search | case-searcher | None | `_workspace/01_case_search.md` |
| 2 | Legal doctrine analysis | legal-analyst | Task 1 | `_workspace/02_legal_analysis.md` |
| 3 | Opinion drafting | opinion-writer | Tasks 1, 2 | `_workspace/03_legal_opinion.md` |
| 4 | Strategy formulation | strategy-advisor | Tasks 2, 3 | `_workspace/04_legal_strategy.md` |

**Inter-team Communication Flow:**
- case-searcher completes → delivers key cases and issue-by-issue classification to legal-analyst
- legal-analyst completes → delivers issue structure map and legal doctrine analysis to opinion-writer; delivers win probability assessment to strategy-advisor
- opinion-writer completes → delivers opinion conclusions and certainty level to strategy-advisor
- strategy-advisor cross-validates logical consistency across all outputs when drafting the final report

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify logical consistency across case search → legal doctrine → opinion → strategy
3. Report final summary to the user:
    - Case Search Report — `01_case_search.md`
    - Legal Doctrine Analysis Report — `02_legal_analysis.md`
    - Legal Opinion — `03_legal_opinion.md`
    - Strategy Formulation Report — `04_legal_strategy.md`

## Deliverables


## Extension Skills
- **case-analysis-framework**: A systematic framework for case analysis and issue structuring methodology. The 'case-searcher' and 'legal-analyst' agents must use this skill's IRAC framework, case analysis matrix, and issue structuring techniques when searching, analyzing cases, and deriving legal principles. Used for 'case analysis', 'issue organization', 'legal principle derivation', etc. However, drafting opinions or developing strategy is outside the scope of this skill.
- **legal-research**: Full legal research pipeline. An agent team collaborates to perform case search → legal doctrine analysis → opinion drafting → strategy formulation in one pass. Use this skill for all legal research tasks including 'legal research', 'case search', 'legal doctrine analysis', 'legal opinion', 'litigation strategy', 'legal issue analysis', 'legal review', 'dispute response strategy', 'legal risk analysis', 'legal advisory materials', etc. However, actual legal advice (attorney opinion letters), litigation/arbitration representation, direct integration with legal databases (comprehensive legal information systems), and notarization of legal documents are outside the scope of this skill.
- **legal-writing-methodology**: Professional methodology for drafting legal opinions and strategy reports. The 'opinion-writer' and 'strategy-advisor' agents must utilize the document structure, argumentation techniques, and citation formats in this skill when drafting legal opinions or formulating strategies. Used for 'legal opinion drafting', 'legal document structure', 'argumentation methods', etc. Note: case law research and legal doctrine analysis are outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|----------|------|
| Web search failure | Case searcher proceeds with general legal knowledge, notes "case DB not queried" |
| Insufficient facts | Ask follow-up questions before proceeding; perform general analysis with minimal information |
| Agent failure | Retry once → if still failing, proceed without that deliverable; note omission in final report |
| Legal judgment uncertainty | Present multiple interpretations, note "professional legal counsel recommended" |
| Logical inconsistency between outputs | strategy-advisor identifies inconsistency and requests re-review |
