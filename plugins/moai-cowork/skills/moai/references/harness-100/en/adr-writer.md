# ADR Writer (62-adr-writer)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
An agent team harness for creating Architecture Decision Records (ADRs).

## Expert Roles
- **adr-author**: ADR Document Author. Synthesizes context analysis, alternative research, and tradeoff evaluation results to produce a formal Architecture Decision Record in standard ADR format.
  - ADR Numbering Management: Manage sequential numbering with existing ADRs and track status (Proposed/Accepted/Superseded/Deprecated)
  - Standard Format Writing: Apply Michael Nygard-style ADR or MADR (Markdown ADR) format
  - Decision Rationale Documentation: Focus on "why was this decision made" rather than "what was decided"
  - Consequence Documentation: Record both positive and negative consequences of the chosen option
  - Related ADR Linking: Specify relationships with prior and subsequent decisions
- **alternative-researcher**: Alternative Researcher. Explores technology options for architecture decisions and investigates each alternative's characteristics, maturity, community, and adoption cases, organizing them for comparison.
  - Alternative Identification: Identify at least 3 technical alternatives for solving the problem
  - Deep Technical Research: Analyze each alternative's architecture, operating principles, and key characteristics
  - Maturity Assessment: Investigate community size, release stability, and enterprise adoption cases
  - PoC Design: Propose prototype-level validation approaches for each alternative
  - Include "Do Nothing" Option: Always include the consequences of maintaining the status quo as an alternative
- **context-analyst**: Technical Context Analyst. Assesses the current system architecture, defines the problem requiring a decision, and identifies technical, organizational, and business constraints.
  - Current Architecture Assessment: Analyze the existing system's structure, technology stack, and dependencies
  - Problem Definition: Clarify why an architecture decision is needed and what core problem must be resolved
  - Constraint Identification: Enumerate technical (compatibility, performance), organizational (team capabilities, timeline), and business (budget, regulatory) constraints
  - Stakeholder Mapping: Identify teams and systems affected by this decision
  - Quality Attribute Prioritization: Define priorities among quality attributes such as performance, scalability, security, and maintainability
- **impact-tracker**: Impact Tracker. Analyzes the impact of architecture decisions on systems, teams, and processes, and establishes execution plans, migration roadmaps, and monitoring criteria.
  - System Impact Analysis: Identify services, modules, and interfaces affected by the decision
  - Team Impact Analysis: Determine required technical training, role changes, and workflow modifications
  - Migration Roadmap: Establish phased execution plans with rollback strategies for each phase
  - Monitoring Criteria: Define metrics and thresholds for judging the decision's success or failure
  - Inter-ADR Dependency Tracking: Map the impact of this decision on existing and future ADRs
- **tradeoff-evaluator**: Tradeoff Evaluator. Performs quantitative and qualitative comparison analysis between alternatives, generates weighted evaluation matrices by quality attribute, and recommends the optimal alternative.
  - Weighted Evaluation Matrix Generation: Assign weights by quality attribute and score each alternative
  - Quantitative Analysis: Compare measurable items such as performance, cost, and migration time
  - Qualitative Analysis: Compare hard-to-quantify items such as team capability, vendor reliability, and ecosystem maturity
  - Risk-Reward Analysis: Evaluate each alternative's expected reward relative to its risk
  - Recommendation Derivation: Synthesize analysis results to recommend the optimal alternative

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Decision Topic**: What architecture decision is being made
    - **Project Context** (optional): Technology stack, team size, project phase
    - **Constraints** (optional): Budget, timeline, technical constraints
    - **Existing ADRs** (optional): Previously written ADR list or codebase
2. Create the `_workspace/` directory in the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If a codebase is available, instruct the context analyst to explore it
5. Determine the **execution mode** based on the scope of the request (see "Execution Modes by Request Scope" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Technical Context Analysis | context-analyst | None | `_workspace/01_context_analysis.md` |
| 2 | Alternatives Research | alternative-researcher | Task 1 | `_workspace/02_alternatives_report.md` |
| 3 | Tradeoff Evaluation | tradeoff-evaluator | Tasks 1, 2 | `_workspace/03_tradeoff_matrix.md` |
| 4a | ADR Document Writing | adr-author | Tasks 1, 2, 3 | `_workspace/04_adr_document.md` |
| 4b | Impact Assessment | impact-tracker | Tasks 1, 2, 3 | `_workspace/05_impact_assessment.md` |

Tasks 4a (ADR document) and 4b (impact assessment) are executed **in parallel**. Both depend only on Tasks 1-3, so they can start simultaneously.

**Inter-agent Communication Flow:**
- context-analyst completes -> Delivers constraints and technology stack to alternative-researcher; delivers quality attribute priorities to tradeoff-evaluator
- alternative-researcher completes -> Delivers alternatives list and data to tradeoff-evaluator
- tradeoff-evaluator completes -> Delivers recommendation to adr-author; delivers risk list to impact-tracker
- adr-author <-> impact-tracker: Cross-verify consistency between ADR document and impact assessment

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Validate consistency between the ADR document and impact assessment
3. Present the final summary to the user:
    - Technical Context — `01_context_analysis.md`
    - Alternatives Research — `02_alternatives_report.md`
    - Tradeoff Evaluation — `03_tradeoff_matrix.md`
    - ADR Document — `04_adr_document.md`
    - Impact Assessment — `05_impact_assessment.md`

## Deliverables


## Extension Skills
- **adr-writer**: A pipeline where an agent team systematically creates Architecture Decision Records (ADRs). Use this skill for requests such as 'write an ADR,' 'architecture decision record,' 'document a technical decision,' 'architecture decision record,' 'organize architecture selection rationale,' 'technology stack decision,' 'alternative comparison analysis,' 'tradeoff analysis,' or 'architecture decision history.' Note: actual code migration execution, infrastructure provisioning, and performance test execution are outside the scope of this skill.
- **madr-template-engine**: A specialized skill for structuring ADRs in MADR (Markdown Any Decision Record) standard format and systematizing status management. Used by the adr-author and impact-tracker agents when writing standard-format ADR documents and tracking decision history. Automatically applied in contexts involving 'MADR format,' 'ADR template,' 'decision status,' 'ADR numbering system,' or 'decision history.' Note: Git commit hook setup and CI/CD pipeline construction are outside the scope of this skill.
- **quality-attribute-analyzer**: A specialized skill for systematically analyzing quality attributes in architecture decisions and quantifying tradeoffs. Used by the tradeoff-evaluator agent when evaluating tradeoffs between quality attributes such as performance, scalability, and security. Automatically applied in contexts involving 'quality attributes,' 'QA analysis,' '-ility,' 'performance requirements,' 'scalability,' 'security,' or 'CAP theorem.' Note: actual performance test execution and security audits are outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| No codebase available | Analyze context based on user description; mark as "inference-based" |
| Web search failure | Research alternatives based on general technical knowledge; mark as "latest data unverified" |
| Insufficient quantitative data | Substitute with qualitative evaluation; mark as "estimates" in the tradeoff matrix |
| Agent failure | Retry once; if still failing, proceed without that deliverable; note omission in final report |
| Decision deferred | Set ADR status to "Proposed"; specify additional information needed |
