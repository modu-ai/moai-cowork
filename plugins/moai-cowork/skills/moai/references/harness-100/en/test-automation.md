# Test Automation (24)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness that collaborates on test automation strategy development, test writing, CI integration, and coverage analysis.

## Expert Roles
- **Coverage Analyst**: Coverage analysis expert. Measures test coverage, identifies coverage gaps, and determines additional test priorities based on risk.
  - **Coverage Measurement**: Measure line, branch, function, and statement coverage per module
  - **Gap Analysis**: Identify modules with low coverage and prioritize them in conjunction with risk
  - **Blind Spot Discovery**: Find testing blind spots that coverage numbers alone might miss
  - **Mutation Testing Analysis**: Evaluate the actual effectiveness of tests through mutation testing
  - **Improvement Roadmap**: Establish a phased plan for achieving coverage targets
- **Integration Tester**: Integration testing expert. Verifies interactions between APIs, databases, and external services, and designs test environment setup and data seeding strategies.
  - **API Testing**: Verify per-endpoint request/response, status codes, and error handling
  - **DB Integration Testing**: Verify CRUD operations, transactions, and migrations with actual databases
  - **External Service Testing**: Simulate third-party API integrations with WireMock/MSW
  - **Test Environment Setup**: Configure isolated test environments using Docker Compose and Testcontainers
  - **Data Seeding**: Design test data creation, cleanup, and isolation strategies
- **Qa Reviewer**: Test automation reviewer (QA). Cross-validates consistency between strategy, tests, and coverage, and evaluates test quality and maintainability.
  - **Strategy-Test Consistency**: Has the scope defined in the strategy been implemented as actual tests?
  - **Test Quality Evaluation**: AAA pattern compliance, assertion meaning, clarity of test names
  - **Maintainability Evaluation**: DRY principle, helper/factory usage, identifying fragile tests
  - **Coverage-Risk Consistency**: Are coverage gaps correctly prioritized on a risk basis?
  - **CI Integration Verification**: Is the pipeline configuration executable and optimized?
- **Test Strategist**: Test strategy expert. Determines scope based on the test pyramid, selects frameworks/tools, and designs CI integration strategy and quality gates.
  - **Test Pyramid Design**: Determine unit/integration/E2E ratios based on project characteristics
  - **Test Scope Definition**: Determine test priorities and scope through risk-based analysis
  - **Tool/Framework Selection**: Select the test tool stack appropriate for the language/framework
  - **CI Integration Design**: Design test pipelines, parallel execution, and caching strategies
  - **Quality Gate Definition**: Set coverage thresholds, performance criteria, and merge conditions
- **Unit Tester**: Unit testing expert. Writes unit tests for business logic, designs mocking strategies, and derives effective test cases using boundary value analysis and equivalence partitioning.
  - **Test Case Derivation**: Systematically derive cases using boundary value analysis, equivalence partitioning, and decision tables
  - **Mocking/Stubbing Design**: Isolate external dependencies to test pure logic only
  - **AAA Pattern Application**: Write readable tests using the Arrange-Act-Assert pattern
  - **Edge Case Testing**: Verify boundary conditions including null, undefined, empty arrays, min/max values, concurrency
  - **Test Double Management**: Use Mock, Stub, Spy, and Fake appropriately

## Workflow
### Phase 1: Preparation (Performed directly by Orchestrator)

1. Extract from user input:
    - **Target Code**: Codebase or module to test
    - **Tech Stack** (optional): Language, framework, existing test tools
    - **Constraints** (optional): Coverage targets, CI platform, time constraints
    - **Existing Tests** (optional): Already written test code
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on the scope of the request (see "Modes by Task Scale" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Assignee | Dependencies | Deliverable |
|-------|------|----------|-------------|-------------|
| 1 | Test Strategy | strategist | None | `_workspace/01_test_strategy.md` |
| 2a | Unit Test Writing | unit-tester | Task 1 | `_workspace/02_unit_tests.md` |
| 2b | Integration Test Writing | integration-tester | Task 1 | `_workspace/03_integration_tests.md` |
| 3 | Coverage Analysis | coverage-analyst | Tasks 1, 2a, 2b | `_workspace/04_coverage_report.md` |
| 4 | Final Review | qa-reviewer | Tasks 1-3 | `_workspace/05_review_report.md` |

Tasks 2a (unit) and 2b (integration) can be **executed in parallel**.

**Inter-team Communication Flow:**
- strategist completes -> delivers test scope and mocking strategy to unit-tester; delivers integration test scope and environment strategy to integration-tester
- unit-tester completes -> shares mocked interface list with integration-tester; delivers test list to coverage-analyst
- integration-tester completes -> delivers integration test list to coverage-analyst
- coverage-analyst completes -> requests additional tests from unit-tester/integration-tester when gaps are found
- qa-reviewer cross-validates all deliverables. Requests fixes for RED Must Fix items (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Check all files in `_workspace/`
2. Verify all RED Must Fix items have been addressed
3. Report the final summary to the user

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_test_strategy.md` — Test strategy document
- `02_unit_tests.md` — Unit test code and guide
- `03_integration_tests.md` — Integration test code and guide
- `04_coverage_report.md` — Coverage analysis report
- `05_review_report.md` — Final review report

## Extension Skills
- **mocking-strategy**: Test double (Mock, Stub, Spy, Fake) selection and effective mocking strategy guide. Use this skill for 
- **test-design-patterns**: Patterns for effective test design, including boundary value analysis, equivalence partitioning, state transition testing, and other systematic test case derivation methodologies. Use this skill for 

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Code inaccessible | Write general tests based on user description, note "estimation-based" in report |
| Test framework not installed | Provide test code with installation guide |
| Agent failure | Retry once -> if fails, proceed without that deliverable, note omission in review |
| RED found in review | Request fix from relevant agent -> rework -> re-verify (up to 2 times) |
| Coverage tool cannot run | Substitute with static analysis-based estimated coverage |
