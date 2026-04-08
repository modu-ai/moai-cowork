# Legacy Modernizer (22)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for transforming legacy codebases into modern architectures. Automates the analysis -> refactoring strategy -> migration -> verification pipeline.

## Expert Roles
- **Legacy Analyzer**: Legacy code analysis expert. Identifies technical debt in the codebase, maps dependency graphs, measures complexity, and determines modernization priorities.
  - **Technology Stack Audit**: Identify the versions and EOL status of languages, frameworks, and libraries in use
  - **Technical Debt Identification**: Quantitatively measure hardcoding, circular dependencies, code duplication, and anti-patterns
  - **Dependency Mapping**: Visualize inter-module dependency relationships as a directed graph and calculate coupling
  - **Complexity Measurement**: Calculate Cyclomatic Complexity, Cognitive Complexity, and Class Cohesion (LCOM)
  - **Hotspot Identification**: Find "hotspots" with high change frequency but low test coverage
- **Migration Engineer**: Migration execution engineer. Performs actual code transformation, API modernization, framework migration, and configuration externalization according to the refactoring strategy, and generates migration scripts.
  - **Code Transformation**: Convert legacy patterns to modern patterns (callbacks -> Promise/async-await, class -> functional, etc.)
  - **API Modernization**: REST API design improvements, GraphQL migration, OpenAPI spec generation
  - **Framework Migration**: Implement compatibility layers for framework upgrades or replacements
  - **Configuration Externalization**: Separate hardcoded configurations into environment variables, config files, or Secret Manager
  - **Migration Scripts**: Write data schema transformations, automation scripts, and codemods
- **Modernization Reviewer**: Modernization project reviewer (QA). Cross-validates consistency across analysis, strategy, migration, and testing, identifying gaps, contradictions, and risks to provide feedback.
  - **Analysis-Strategy Consistency**: Has all technical debt found in the analysis been reflected in the strategy?
  - **Strategy-Migration Consistency**: Are the strategy's phases and priorities accurately reflected in the migration plan?
  - **Migration-Test Consistency**: Do verification tests exist for all transformation items?
  - **Business Logic Preservation**: Have core business rules been preserved without loss during modernization?
  - **Rollback Safety**: Has a safe rollback strategy been established for each phase?
- **Refactoring Strategist**: Refactoring strategy expert. Selects optimal refactoring patterns based on legacy analysis results, determines priorities using a risk-impact matrix, and designs a phased migration roadmap.
  - **Refactoring Pattern Selection**: Choose the appropriate pattern from Strangler Fig, Branch by Abstraction, Parallel Run, etc. based on the situation
  - **Priority Determination**: Calculate a priority matrix using Risk x Business Value x Effort
  - **Dependency Resolution Strategy**: Design strategies for dependency cleanup such as circular dependency removal, interface segregation, and inversion
  - **Migration Roadmap**: Establish a phased execution plan in sprint increments (no Big Bang principle)
  - **Rollback Strategy**: Formulate safe rollback strategies for when issues arise at each phase
- **Regression Tester**: Regression testing expert. Verifies behavior preservation before and after migration, performs performance comparison benchmarks, and checks backward compatibility.
  - **Behavior Preservation Verification**: Write test cases to verify that core business logic input/output is identical before and after migration
  - **Performance Comparison**: Perform Before/After performance benchmarks to confirm no performance degradation
  - **Compatibility Testing**: Verify API backward compatibility and data format compatibility
  - **Edge Case Discovery**: Detect and test undocumented behavior implicit in legacy code
  - **Coverage Analysis**: Measure and improve test coverage for migration target code

## Workflow
### Phase 1: Preparation (Performed directly by Orchestrator)

1. Extract from user input:
    - **Target Code/System**: Codebase or system information to modernize
    - **Target Architecture** (optional): Desired technology stack/patterns to migrate to
    - **Constraints** (optional): Downtime tolerance, budget, timeline
    - **Existing Documentation** (optional): Architecture documents, analysis reports, etc.
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on the scope of the request (see "Modes by Task Scale" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Assignee | Dependencies | Deliverable |
|-------|------|----------|-------------|-------------|
| 1 | Legacy Analysis | analyzer | None | `_workspace/01_legacy_analysis.md` |
| 2 | Refactoring Strategy | strategist | Task 1 | `_workspace/02_refactoring_strategy.md` |
| 3 | Migration Execution Plan | engineer | Tasks 1, 2 | `_workspace/03_migration_plan.md` |
| 4 | Regression Testing | tester | Tasks 1, 3 | `_workspace/04_test_report.md` |
| 5 | Final Review | reviewer | Tasks 1-4 | `_workspace/05_review_report.md` |

**Inter-team Communication Flow:**
- analyzer completes -> delivers tech debt, hotspots, and dependencies to strategist; delivers tech stack and business logic to engineer; delivers current coverage to tester
- strategist completes -> delivers roadmap and migration mapping to engineer; delivers Phase completion criteria to tester
- engineer completes -> delivers Before/After and verification points to tester
- tester completes -> requests fixes from engineer if regressions are found
- reviewer cross-validates all deliverables. When RED Must Fix items are found, requests fixes from the relevant agent -> rework -> re-verification (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Check all files in `_workspace/`
2. Verify that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_legacy_analysis.md` — Legacy analysis report
- `02_refactoring_strategy.md` — Refactoring strategy document
- `03_migration_plan.md` — Migration execution plan and code
- `04_test_report.md` — Regression test report
- `05_review_report.md` — Final review report

## Extension Skills
- **dependency-analysis**: Tools and methodologies for analyzing codebase dependency graphs and quantitatively measuring coupling/cohesion. Use this skill for 
- **strangler-fig-patterns**: Detailed implementation guide for the Strangler Fig pattern and related migration patterns for incrementally replacing legacy systems. Use this skill for 

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Code inaccessible | Inference-based analysis from user-provided information, note "Limited Access" in report |
| No test environment | Substitute with static analysis and code review-based verification |
| Agent failure | Retry once -> if fails, proceed without that deliverable, note omission in review |
| RED found in review | Request fix from relevant agent -> rework -> re-verify (up to 2 times) |
| Circular dependency unresolvable | Insert Anti-Corruption Layer to isolate, then resolve incrementally |
