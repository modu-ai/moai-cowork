# Patent Drafter (68-patent-drafter)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
A patent application drafting agent team harness.

## Expert Roles
- **claim-drafter**: Claim drafter. Designs optimal claim scope based on prior art search results and systematically drafts independent and dependent claims.
  - Claim Strategy Development: Determine the invention category (article/method/apparatus/system) and claim types
  - Independent Claim Drafting: Draft independent claims that cover the core inventive concept with minimal elements
  - Dependent Claim Design: Arrange dependent claims that progressively narrow the independent claim (fallback strategy)
  - Multi-Category Claims: Extend protection scope by claiming the same invention across multiple categories (article/method/system)
  - Terminology Unification: Ensure term consistency throughout claims and identify terms requiring definition
- **drawing-designer**: Drawing designer. Designs the drawing composition for patent specifications, defines detailed descriptions and reference numeral placement for each drawing. Creates text-based drawing specifications.
  - Drawing Composition Design: Determine the types and number of drawings needed to explain the invention
  - Reference Numeral System Design: Consistently assign reference numerals for each component
  - Drawing Detail Specifications: Describe in detail the components, layout, arrows, and annotations to be included in each drawing
  - Flowchart Design: Design step-by-step flowcharts for method inventions
  - ASCII/Mermaid Drawing Generation: Represent drawings in text-based format for inventor comprehension
- **patent-reviewer**: Patent reviewer. Cross-verifies consistency between claims, specification, and drawings, and pre-checks for grounds of rejection from description deficiency, novelty, and inventive step perspectives.
  - Claim-Specification Support Verification: Confirm that all claim elements are sufficiently described in the specification
  - Claim-Drawing Consistency Verification: Confirm that claim elements are reflected in drawings and reference numerals match
  - Description Deficiency Check: Pre-identify description deficiency grounds such as unclear terms, insufficient support, and enablement issues
  - Novelty and Inventive Step Re-verification: Reconfirm that claims have novelty and inventive step compared to prior art
  - Formal Requirements Check: Check formal requirements such as claim format, specification structure, and reference numeral consistency
- **prior-art-researcher**: Prior art researcher. Investigates existing patents, papers, and technical literature related to the invention, and analyzes differentiation points from novelty and inventive step perspectives.
  - Keyword and Classification Code Derivation: Derive search keywords and IPC/CPC classification codes from the invention's technical field and core components
  - Prior Art Search: Use web search to investigate related patents, papers, and technical literature
  - Similarity Analysis: Compare and analyze element-by-element similarity between discovered prior art and the target invention
  - Novelty and Inventive Step Assessment: Derive differentiating points that secure novelty and inventive step compared to prior art
  - Design-Around Suggestions: Propose claim scope design directions to avoid conflicts with prior art
- **specification-writer**: Specification writer. Writes a detailed description of the invention that fully supports the claims. Includes technical field, background art, problems to be solved, means for solving problems, effects of the invention, and embodiments.
  - Technical Field Description: Describe the technical field to which the invention belongs in accordance with IPC classification
  - Background Art Description: Objectively describe the problems and limitations of prior art
  - Problem, Means, and Effects: Logically connect the problem to be solved, the means of solution, and the expected effects
  - Detailed Description for Implementation: Describe embodiments at a level reproducible by a person skilled in the art
  - Claim Support: Verify that all claim elements and terms are described in the specification

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Title of Invention**: Technical title
    - **Technical Field**: The field to which the invention belongs
    - **Invention Overview**: Core technical concept, components, operating principles
    - **Problem to be Solved**: Problems with existing technology and the problem to be solved
    - **Existing Materials** (optional): Invention report, technical documents, prototype information
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. Determine the **execution mode** based on the requested scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Prior Art Search | prior-art-researcher | None | `_workspace/01_prior_art_report.md` |
| 2 | Claim Drafting | claim-drafter | Task 1 | `_workspace/02_claims.md` |
| 3a | Specification Writing | specification-writer | Tasks 1, 2 | `_workspace/03_specification.md` |
| 3b | Drawing Design | drawing-designer | Task 2 | `_workspace/04_drawings.md` |
| 4 | Patent Review | patent-reviewer | Tasks 1, 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (Specification) and 3b (Drawing) are executed **in parallel**. Both depend on claims, so they can start simultaneously after Task 2 is complete. However, both sides communicate for reference numeral coordination.

**Inter-agent Communication Flow:**
- prior-art-researcher completes -> Delivers differentiation points and design-around direction to claim-drafter
- claim-drafter completes -> Delivers elements and terms to specification-writer, structure to drawing-designer
- specification-writer <-> drawing-designer: Mutual coordination of reference numeral system
- patent-reviewer cross-verifies all deliverables. If Red must-fix items found, requests revision from relevant agent (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that all Red must-fix items from the review report have been addressed
3. Report the final summary to the user:
    - Prior Art Search Report — `01_prior_art_report.md`
    - Claim Set — `02_claims.md`
    - Detailed Description of Invention — `03_specification.md`
    - Drawing Description — `04_drawings.md`
    - Review Report — `05_review_report.md`

## Deliverables


## Extension Skills
- **claim-drafting-patterns**: Strategic drafting patterns and claim scope design guide for patent claims. The 'claim-drafter' and 'patent-reviewer' agents must use this skill's drafting patterns, terminology rules, and dependent claim strategies when writing or verifying claims. Used for 'claim drafting', 'claim scope design', 'dependent claim strategy', etc. Note: Overall patent orchestration or prior art search is outside the scope of this skill.
- **patent-drafter**: A full patent specification drafting pipeline. An agent team collaborates to generate prior art search, claims, specification, and drawing descriptions in a single pass. Use this skill for contexts such as 'write a patent specification', 'patent application', 'invention patent', 'draft claims', 'prior art search', 'patent draft', 'patent specification draft', 'convert invention report to patent', 'turn an idea into a patent', and other patent specification drafting tasks. Note: Actual patent office filing, patent examination responses (opinion statements/amendments), patent litigation, and international filing (PCT/Paris Convention) practice are outside the scope of this skill.
- **prior-art-search-strategy**: A strategic search methodology for patent prior art investigation. The 'prior-art-researcher' agent must use this skill's search strategies, classification code system, and analysis frameworks when searching prior art and determining novelty and inventive step. Used for 'prior art search', 'novelty determination', 'inventive step analysis', etc. Note: Claim drafting or specification writing is outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Web search failure | Prior art researcher works based on general knowledge, notes "DB search not performed" |
| Insufficient invention info | Request additional info from user, draft with minimum information |
| Agent failure | Retry once -> if failed, proceed without that deliverable, note omission in review report |
| Red items found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Reference numeral mismatch | drawing-designer and specification-writer mutually coordinate |
