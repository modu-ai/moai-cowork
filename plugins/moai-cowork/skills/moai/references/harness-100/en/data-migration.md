# Data Migration Harness (34-data-migration)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

Data migration: a harness in which an agent team collaborates to perform source analysis, schema mapping, transformation script generation, validation queries, and rollback planning.

## Expert Roles

- **Rollback Planner — Rollback and Emergency Response Specialist**: Rollback and emergency response specialist. Develops backup strategies, rollback scripts, emergency procedures, decision trees, and communication plans.

- **Schema Mapper — Schema Mapping Specialist**: Schema mapping specialist. Systematically designs field mappings, type conversion rules, business transformation logic, and default value definitions between source and target systems.

- **Script Developer — Migration Script Developer**: Migration script developer. Generates executable scripts including ETL transformation code, incremental migration logic, batch processing, and performance optimization.

- **Source Analyst — Source System Analysis Specialist**: Source system analysis specialist. Performs schema reverse-engineering, data profiling, inter-table dependency mapping, and data quality diagnostics on the source database.

- **Validation Engineer — Migration Validation Engineer**: Migration validation engineer. Designs and executes data integrity validation queries, row count matching, business rule validation, and regression test suites.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Source system**: DBMS type, version, connection info, schema scope
    - **Target system**: DBMS type, version, existing schema availability
    - **Migration scope**: Full/partial, target tables, data time range
    - **Constraints**: Allowable downtime, performance requirements, schedule
2. Create the `_workspace/` directory and subdirectories
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Source analysis | source-analyst | None | `01_source_analysis.md` |
| 2 | Schema mapping | schema-mapper | Task 1 | `02_schema_mapping.md` |
| 3a | Transformation scripts | script-developer | Task 2 | `03_migration_scripts/` |
| 3b | Validation suite | validation-engineer | Tasks 1, 2 | `04_validation_suite.md` |
| 4 | Rollback plan | rollback-planner | Tasks 1, 2, 3a, 3b | `05_rollback_plan.md` |

Tasks 3a (scripts) and 3b (validation) run **in parallel**.

**Inter-agent communication flow:**
- source-analyst completes > passes source schema to schema-mapper, volume/order to script-developer, integrity rules to validation-engineer
- schema-mapper completes > passes mapping spec to script-developer, transformation rules to validation-engineer, reverse mapping feasibility to rollback-planner
- script-developer completes > passes transaction boundaries to rollback-planner
- validation-engineer completes > passes rollback trigger conditions to rollback-planner
- rollback-planner develops the overall plan and feeds back risk items to each agent

### Phase 3: Integration and Final Deliverables

1. Verify all deliverables in `_workspace/`
2. Validate cross-deliverable consistency (mapping vs. scripts, validation vs. mapping, rollback vs. scripts)
3. Present the final migration execution checklist to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Full migration plan" | **Full pipeline** | All 5 agents |
| "Analyze the source DB only" | **Analysis mode** | source-analyst only |
| "Just do schema mapping" | **Mapping mode** | source-analyst + schema-mapper |
| "Generate ETL scripts only" | **Script mode** | script-developer (assumes mapping exists) |
| "Create validation queries only" | **Validation mode** | validation-engineer (assumes mapping exists) |
| "Just create a rollback plan" | **Rollback mode** | rollback-planner (assumes full analysis exists) |

**Reusing existing files**: If the user provides existing DDL, ERD, or schema mapping documents, copy those files to the appropriate location in `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Deliverable documents |
| Script-based | `_workspace/03_migration_scripts/` | Executable code |
| Message-based | SendMessage | Key information transfer, feedback |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| DB connection unavailable | Fall back to DDL/ERD document-based analysis |
| Target schema undecided | Auto-generate recommended target schema based on source |
| Incompatible types | Propose two-stage conversion via intermediate type |
| Very large tables (>100M rows) | Partition-level migration strategy |
| Agent failure | Retry once; if still failing, proceed without that deliverable |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Source system**: DBMS type, version, connection info, schema scope
    - **Target system**: DBMS type, version, existing schema availability
    - **Migration scope**: Full/partial, target tables, data time range
    - **Constraints**: Allowable downtime, performance requirements, schedule
2. Create the `_workspace/` directory and subdirectories
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Source analysis | source-analyst | None | `01_source_analysis.md` |
| 2 | Schema mapping | schema-mapper | Task 1 | `02_schema_mapping.md` |
| 3a | Transformation scripts | script-developer | Task 2 | `03_migration_scripts/` |
| 3b | Validation suite | validation-engineer | Tasks 1, 2 | `04_validation_suite.md` |
| 4 | Rollback plan | rollback-planner | Tasks 1, 2, 3a, 3b | `05_rollback_plan.md` |

Tasks 3a (scripts) and 3b (validation) run **in parallel**.

**Inter-agent communication flow:**
- source-analyst completes > passes source schema to schema-mapper, volume/order to script-developer, integrity rules to validation-engineer
- schema-mapper completes > passes mapping spec to script-developer, transformation rules to validation-engineer, reverse mapping feasibility to rollback-planner
- script-developer completes > passes transaction boundaries to rollback-planner
- validation-engineer completes > passes rollback trigger conditions to rollback-planner
- rollback-planner develops the overall plan and feeds back risk items to each agent

### Phase 3: Integration and Final Deliverables

1. Verify all deliverables in `_workspace/`
2. Validate cross-deliverable consistency (mapping vs. scripts, validation vs. mapping, rollback vs. scripts)
3. Present the final migration execution checklist to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Full migration plan" | **Full pipeline** | All 5 agents |
| "Analyze the source DB only" | **Analysis mode** | source-analyst only |
| "Just do schema mapping" | **Mapping mode** | source-analyst + schema-mapper |
| "Generate ETL scripts only" | **Script mode** | script-developer (assumes mapping exists) |
| "Create validation queries only" | **Validation mode** | validation-engineer (assumes mapping exists) |
| "Just create a rollback plan" | **Rollback mode** | rollback-planner (assumes full analysis exists) |

**Reusing existing files**: If the user provides existing DDL, ERD, or schema mapping documents, copy those files to the appropriate location in `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Deliverable documents |
| Script-based | `_workspace/03_migration_scripts/` | Executable code |
| Message-based | SendMessage | Key information transfer, feedback |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| DB connection unavailable | Fall back to DDL/ERD document-based analysis |
| Target schema undecided | Auto-generate recommended target schema based on source |
| Incompatible types | Propose two-stage conversion via intermediate type |
| Very large tables (>100M rows) | Partition-level migration strategy |
| Agent failure | Retry once; if still failing, proceed without that deliverable |

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input and migration requirements
- `01_source_analysis.md` — Source system analysis report
- `02_schema_mapping.md` — Schema mapping specification
- `03_migration_scripts/` — Transformation scripts directory
- `04_validation_suite.md` — Validation queries and test suite
- `05_rollback_plan.md` — Rollback and emergency response plan

## Extension Skills

| Skill | Path | Enhanced Agent | Role |
|-------|------|---------------|------|
| type-mapping-encyclopedia | `.claude/skills/type-mapping-encyclopedia/skill.md` | schema-mapper | MySQL/Oracle/PostgreSQL type mapping, RDBMS-to-NoSQL, character set conversion |
| data-validation-patterns | `.claude/skills/data-validation-patterns/skill.md` | validation-engineer | 5-level validation (count > schema > value > referential > business), Go/No-Go checklist |
