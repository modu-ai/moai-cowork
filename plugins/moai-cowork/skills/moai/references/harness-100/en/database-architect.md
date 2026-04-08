# Database Architect (19)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to perform DB design from modeling through migration, indexing, and query optimization.

## Expert Roles
- **data-modeler**: Data Modeler. Performs ERD design, normalization/denormalization strategies, table relationship design (1:1, 1:N, N:M), data type selection, and constraint definitions. Proficient in both RDBMS (PostgreSQL, MySQL) and NoSQL (MongoDB, DynamoDB).
- **integration-reviewer**: Integration Reviewer (QA). Cross-validates alignment across data model, migration, performance, and security artifacts, and evaluates operational readiness.
- **migration-manager**: Migration Manager. Generates DDL scripts, manages migration versioning, designs rollback strategies, creates seed data, and designs zero-downtime migration procedures.
- **performance-analyst**: DB Performance Analyst. Designs index strategies, query optimization, execution plan (EXPLAIN) analysis, partitioning, connection pooling, and caching strategies.
- **security-auditor**: DB Security Auditor. Verifies and designs access control (RBAC), data encryption (TDE, column-level encryption), SQL injection defense, audit logging, and backup/recovery strategies.

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Domain**: What service is the DB for
   - **DBMS**: PostgreSQL / MySQL / MongoDB / DynamoDB
   - **Core Entities**: Primary data subjects
   - **Expected Scale** (optional): Row counts, TPS
   - **Existing Files** (optional): Existing schemas, ERDs, SQL, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1 | Data Modeling | data-modeler | None | `_workspace/01_data_model.md` |
| 2 | Migration Generation | migration-manager | Task 1 | `_workspace/02_migration.sql`, `02_migration_plan.md` |
| 3a | Performance Optimization | performance-analyst | Tasks 1, 2 | `_workspace/03_performance.md` |
| 3b | Security Verification | security-auditor | Tasks 1, 2 | `_workspace/04_security.md` |
| 4 | Integration Review | integration-reviewer | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (performance) and 3b (security) are **executed in parallel**.

**Inter-team communication flow:**
- data-modeler completes -> Delivers DDL basis to migration-manager, access patterns to performance-analyst, sensitive data to security-auditor
- migration-manager completes -> Delivers index DDL to performance-analyst, permission DDL to security-auditor
- performance-analyst <-> security-auditor: Mutually verify that performance optimizations do not compromise security
- integration-reviewer cross-validates all artifacts. When 🔴 must-fix issues are found, requests revisions from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Artifacts

Organize the final artifacts based on the review report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 must-fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills
- **normalization-patterns**: Database normalization/denormalization pattern library. An extension skill for data-modeler that provides 1NF-BCNF criteria, functional dependency analysis, step-by-step normalization procedures, strategic denormalization patterns, and common domain ERD templates. Use when data modeling involves 'normalization', 'denormalization', 'ERD patterns', 'functional dependencies', 'table splitting', 'relationship design', etc. Note: DDL generation and query optimization are outside the scope of this skill.
- **query-optimization-catalog**: SQL query optimization catalog. An extension skill for performance-analyst that provides index strategies (B-Tree/Hash/GIN/GiST), execution plan analysis, N+1 problem resolution, partitioning strategies, and per-pattern optimization techniques for slow queries. Use when performing DB performance analysis involving 'query optimization', 'index design', 'execution plans', 'N+1 problems', 'partitioning', 'slow queries', etc. Note: data modeling and security configuration are outside the scope of this skill.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| DBMS not specified | Default to PostgreSQL; add compatibility notes for other DBMSs |
| Insufficient domain information | Data modeler starts with common patterns; document assumptions |
| Agent failure | Retry once -> If still fails, proceed without that artifact; note the omission in the review report |
| 🔴 found during review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| Existing schema parsing failure | Manually analyze and reconstruct the data model |
