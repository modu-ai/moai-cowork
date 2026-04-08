# Code Reviewer (21)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to perform automated code review across style, security, performance, and architecture.

## Expert Roles
- **Architecture Reviewer**: Architecture Reviewer. Analyzes design patterns, SOLID principles, dependency direction, coupling/cohesion, module structure, testability, and extensibility.
  - **SOLID Principle Verification**: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
  - **Design Pattern Analysis**: Appropriateness of applied patterns, missed pattern opportunities, anti-pattern identification
  - **Dependency Analysis**: Dependency direction (inward to outward), circular dependencies, coupling, cohesion
  - **Module Structure**: Layer separation, separation of concerns, domain boundaries
  - **Testability**: DI implementation, mocking ease, side effect isolation, test coverage
- **Performance Analyst**: Code Performance Analyst. Analyzes time/space complexity, memory leaks, concurrency issues, DB query optimization, unnecessary computations, and caching opportunities.
  - **Complexity Analysis**: Time complexity (Big-O), space complexity, hot path identification
  - **Memory Analysis**: Memory leaks, unnecessary object creation, large data handling
  - **Concurrency Analysis**: Deadlocks, race conditions, thread safety, async patterns
  - **DB/Network Optimization**: N+1 queries, unnecessary API calls, batch processing opportunities
  - **Caching Opportunities**: Repeated computations, redundant API calls, memoization candidates
- **Review Synthesizer**: Code Review Synthesizer (QA). Synthesizes style, security, performance, and architecture review results; determines priorities and verifies cross-domain alignment.
  - **Priority Adjustment**: Re-rank findings from all 4 domains into unified priorities
  - **Cross-Domain Conflict Resolution**: Arbitrate conflicts such as security vs performance, readability vs optimization
  - **Deduplication**: Merge findings where multiple domains flagged the same issue
  - **Action Item Generation**: Create a specific, actionable list of fixes
  - **Overall Quality Verdict**: Render final verdict of Approve / Request Changes / Reject
- **Security Analyst**: Code Security Analyst. Analyzes OWASP Top 10, injection vulnerabilities, authentication/authorization flaws, sensitive data exposure, insecure deserialization, and dependency vulnerabilities.
  - **Injection Analysis**: Detect SQL Injection, XSS, Command Injection, LDAP Injection
  - **Authentication/Authorization Inspection**: Hardcoded credentials, weak hashing, missing permission checks, IDOR
  - **Data Protection**: Sensitive data logging, plaintext storage, insecure transmission
  - **Dependency Vulnerabilities**: Packages with known CVEs, outdated dependencies, license conflicts
  - **Cryptography Inspection**: Weak crypto algorithms, hardcoded keys, insecure random number generation
- **Style Inspector**: Code Style Inspector. Inspects coding conventions, formatting, naming rules, comment quality, readability, and consistency. Proficient in language-specific style guides (PEP 8, Airbnb JS, Google Java, etc.).
  - **Naming Inspection**: Naming conventions and semantic clarity of variables, functions, classes, and filenames
  - **Formatting Inspection**: Indentation, spacing, line length, brace style, import ordering
  - **Readability Assessment**: Function length, nesting depth, complex expressions, magic numbers
  - **Comments/Documentation**: Missing JSDoc/docstrings, comment quality, TODO management
  - **Consistency Verification**: Style uniformity within the project, pattern consistency

## Workflow
### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Target Code**: File paths, PR number, diff, directory
   - **Language/Framework**: Auto-detect or user-specified
   - **Review Scope** (optional): If only specific domains were requested
   - **Context** (optional): PR description, related issues, change rationale
   - **Style Guide** (optional): Team-specific conventions
2. Create the `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. Identify the target code and determine the review scope
5. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
6. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1a | Style Review | style-inspector | None | `_workspace/01_style_review.md` |
| 1b | Security Review | security-analyst | None | `_workspace/02_security_review.md` |
| 1c | Performance Review | performance-analyst | None | `_workspace/03_performance_review.md` |
| 1d | Architecture Review | architecture-reviewer | None | `_workspace/04_architecture_review.md` |
| 2 | Comprehensive Review | review-synthesizer | Tasks 1a-1d | `_workspace/05_review_summary.md` |

Tasks 1a-1d (all 4 domain reviews) are **all executed in parallel**.

**Inter-team communication flow:**
- style-inspector -> Delivers sensitive info in comments to security-analyst, complex function lists to performance-analyst
- security-analyst -> Delivers security measure performance impact to performance-analyst, authentication architecture to architecture-reviewer
- performance-analyst -> Delivers structural bottlenecks to architecture-reviewer
- review-synthesizer integrates all reviews. Requests additional analysis from relevant analysts when cross-domain conflicts are found

### Phase 3: Integration and Final Artifacts

Organize the final artifacts based on the comprehensive report:

1. Verify all reviews in `_workspace/`
2. Determine the final verdict (Approve/Request Changes/Reject)
3. Report the final summary to the user

## Deliverables
All artifacts are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_style_review.md` — Code style review
- `02_security_review.md` — Security review
- `03_performance_review.md` — Performance review
- `04_architecture_review.md` — Architecture review
- `05_review_summary.md` — Comprehensive review report

## Extension Skills
- **refactoring-catalog**: Code refactoring catalog. An extension skill for architecture-reviewer/performance-analyst that provides Martin Fowler-based refactoring patterns, code smell detection-to-refactoring mapping, SOLID principle violation identification, and complexity measurement criteria. Use when reviewing code structure improvement involving 
- **vulnerability-patterns**: Code vulnerability pattern database. An extension skill for security-analyst that provides language-specific (Python/JS/Java/Go) vulnerable code patterns, CWE classification, safe alternative code, and severity assessment criteria. Use when performing security reviews involving 

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Language not identified | Auto-detect from file extensions + code patterns |
| Large codebase | Focus on changed or core files; note the scope in the review report |
| Agent failure | Retry once -> If still fails, proceed without that domain; note the omission in the comprehensive report |
| Cross-domain conflict | review-synthesizer performs trade-off analysis and renders verdict |
| Insufficient context | Review based on code alone if no PR description or issue number; note limitations |
