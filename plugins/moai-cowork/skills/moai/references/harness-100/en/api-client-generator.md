# API Client Generator Harness (35-api-client-generator)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

API client SDK generation: a harness in which an agent team collaborates to perform spec parsing, type generation, client code development, testing, and usage documentation.

## Expert Roles

- **Doc Writer — SDK Documentation Specialist**: SDK documentation specialist. Writes README, quick start guides, API references, usage examples, changelogs, and migration guides.

- **SDK Developer — SDK Client Developer**: SDK client developer. Develops production-grade SDKs including HTTP client wrappers, authentication handlers, pagination helpers, retry/circuit breaker logic, and error handling.

- **Spec Parser — API Spec Analysis Specialist**: API spec parser. Parses API specifications in OpenAPI (Swagger), GraphQL SDL, gRPC Proto, and other formats to systematically extract endpoints, models, authentication methods, and error codes.

- **Test Engineer — SDK Test Engineer**: SDK test engineer. Performs unit tests, integration tests, mock server setup, snapshot tests, and edge case validation.

- **Type Generator — Type Generation Specialist**: Type generation specialist. Transforms API schemas into the target language's type system. Generates request/response models, enums, union types, generics, and utility types.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **API spec**: File path/URL, spec format (OpenAPI/GraphQL/gRPC)
    - **Target language**: TypeScript, Python, Go, Java, etc.
    - **SDK name**: Package/module name
    - **Settings** (optional): Authentication priority, naming conventions, additional features
2. Create the `_workspace/` directory and subdirectories
3. Organize the input and save it to `_workspace/00_input.md`
4. Copy the API spec file to `_workspace/`
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Spec analysis | spec-parser | None | `01_spec_analysis.md` |
| 2 | Type generation | type-generator | Task 1 | `02_types/` |
| 3 | SDK development | sdk-developer | Tasks 1, 2 | `03_client/` |
| 4a | Test authoring | test-engineer | Tasks 2, 3 | `04_tests/` |
| 4b | Documentation | doc-writer | Tasks 1, 3 | `05_docs/` |

Tasks 4a (tests) and 4b (docs) run **in parallel**.

**Inter-agent communication flow:**
- spec-parser completes > passes model details to type-generator, endpoint groupings to sdk-developer
- type-generator completes > passes type import info to sdk-developer, factory data to test-engineer
- sdk-developer completes > passes public API list to test-engineer, usage examples to doc-writer
- test-engineer/doc-writer > requests fixes from sdk-developer if code/doc inconsistencies are found

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Final consistency check across code, types, tests, and documentation
3. Report the final summary along with build/test execution commands

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Generate full SDK", "full client" | **Full pipeline** | All 5 agents |
| "Just generate types" | **Type mode** | spec-parser + type-generator |
| "Client code only" | **Code mode** | spec-parser + type-generator + sdk-developer |
| "Write tests only" (existing SDK) | **Test mode** | test-engineer only |
| "Write docs only" (existing SDK) | **Doc mode** | doc-writer only |
| "Spec analysis only" | **Analysis mode** | spec-parser only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Code, types, tests, documentation |
| Message-based | SendMessage | Key information transfer, fix requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Spec parsing failure | Report syntax error location; proceed with parseable portions only |
| Incomplete spec | Supplement with type inference; mark as "inferred" |
| Circular references | Auto-apply lazy reference pattern |
| Non-standard authentication | Provide custom interceptor extension points |
| Agent failure | Retry once; if still failing, proceed without that deliverable |
| Code-doc inconsistency | doc-writer/test-engineer requests fix from sdk-developer (up to 2 rounds) |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **API spec**: File path/URL, spec format (OpenAPI/GraphQL/gRPC)
    - **Target language**: TypeScript, Python, Go, Java, etc.
    - **SDK name**: Package/module name
    - **Settings** (optional): Authentication priority, naming conventions, additional features
2. Create the `_workspace/` directory and subdirectories
3. Organize the input and save it to `_workspace/00_input.md`
4. Copy the API spec file to `_workspace/`
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Spec analysis | spec-parser | None | `01_spec_analysis.md` |
| 2 | Type generation | type-generator | Task 1 | `02_types/` |
| 3 | SDK development | sdk-developer | Tasks 1, 2 | `03_client/` |
| 4a | Test authoring | test-engineer | Tasks 2, 3 | `04_tests/` |
| 4b | Documentation | doc-writer | Tasks 1, 3 | `05_docs/` |

Tasks 4a (tests) and 4b (docs) run **in parallel**.

**Inter-agent communication flow:**
- spec-parser completes > passes model details to type-generator, endpoint groupings to sdk-developer
- type-generator completes > passes type import info to sdk-developer, factory data to test-engineer
- sdk-developer completes > passes public API list to test-engineer, usage examples to doc-writer
- test-engineer/doc-writer > requests fixes from sdk-developer if code/doc inconsistencies are found

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Final consistency check across code, types, tests, and documentation
3. Report the final summary along with build/test execution commands

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Generate full SDK", "full client" | **Full pipeline** | All 5 agents |
| "Just generate types" | **Type mode** | spec-parser + type-generator |
| "Client code only" | **Code mode** | spec-parser + type-generator + sdk-developer |
| "Write tests only" (existing SDK) | **Test mode** | test-engineer only |
| "Write docs only" (existing SDK) | **Doc mode** | doc-writer only |
| "Spec analysis only" | **Analysis mode** | spec-parser only |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Code, types, tests, documentation |
| Message-based | SendMessage | Key information transfer, fix requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Spec parsing failure | Report syntax error location; proceed with parseable portions only |
| Incomplete spec | Supplement with type inference; mark as "inferred" |
| Circular references | Auto-apply lazy reference pattern |
| Non-standard authentication | Provide custom interceptor extension points |
| Agent failure | Retry once; if still failing, proceed without that deliverable |
| Code-doc inconsistency | doc-writer/test-engineer requests fix from sdk-developer (up to 2 rounds) |

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input and API spec information
- `01_spec_analysis.md` — API spec analysis results
- `02_types/` — Generated type definition files
- `03_client/` — SDK client code
- `04_tests/` — Test code
- `05_docs/` — Usage documentation

## Extension Skills

| Skill | Path | Enhanced Agent | Role |
|-------|------|---------------|------|
| openapi-spec-patterns | `.claude/skills/openapi-spec-patterns/skill.md` | spec-parser | Endpoint grouping, auth mapping, pagination/error patterns, GraphQL/gRPC |
| sdk-design-patterns | `.claude/skills/sdk-design-patterns/skill.md` | sdk-developer | Builder pattern, interceptor chain, retry, type safety, pagination wrapper |
