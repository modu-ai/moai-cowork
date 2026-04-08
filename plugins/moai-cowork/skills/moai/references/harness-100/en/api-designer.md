# API Designer (18)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to design, document, mock, and test REST/GraphQL APIs.

## Expert Roles
- **api-architect**: API Architect. Designs resource modeling, endpoints, URL naming, HTTP method mapping, versioning strategies, pagination, and filtering. Proficient in both REST and GraphQL paradigms.
- **doc-writer**: API Documentation Writer. Creates developer-friendly API documentation including quick start guides, authentication instructions, per-endpoint request/response examples, error code references, and SDK usage guides.
- **mock-tester**: API Mock and Test Specialist. Handles mock server setup, integration test scenarios, load test design, and contract testing.
- **review-auditor**: API Review Auditor (QA). Cross-validates security, consistency, performance, and RESTful best practice compliance. Verifies alignment across design, schema, documentation, and tests.
- **schema-validator**: API Schema Validator. Generates OpenAPI 3.1/GraphQL SDL schemas and validates type safety, required/optional fields, data formats (dates, emails, etc.), enumerations, and reference relationships.

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Domain**: What service is the API for
   - **Paradigm**: REST / GraphQL / Hybrid
   - **Key Resources**: List of core entities
   - **Authentication Method** (optional): OAuth, JWT, API Key
   - **Existing Files** (optional): Existing schemas, documentation, code, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1 | API Design | api-architect | None | `_workspace/01_api_design.md` |
| 2 | Schema Generation & Validation | schema-validator | Task 1 | `_workspace/02_schema.yaml`, `02_schema_validation.md` |
| 3a | API Documentation | doc-writer | Tasks 1, 2 | `_workspace/03_api_docs.md` |
| 3b | Mock Server & Tests | mock-tester | Tasks 1, 2 | `_workspace/04_mock_tests.md` |
| 4 | API Review | review-auditor | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (documentation) and 3b (tests) are **executed in parallel**.

**Inter-team communication flow:**
- api-architect completes -> Delivers resource model to schema-validator, endpoints to doc-writer, request/response examples to mock-tester
- schema-validator completes -> Delivers schema to doc-writer, schema-based examples to mock-tester
- doc-writer <-> mock-tester: Mutually verify that documentation examples and mock responses match
- review-auditor cross-validates all artifacts. When 🔴 must-fix issues are found, requests revisions from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Artifacts

Organize the final artifacts based on the review report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 must-fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills
- **api-error-design**: API error design patterns. An extension skill for doc-writer/mock-tester that provides error code systems, error response structures, client-friendly error messages, error catalog construction, and retry/fallback strategies. Use when designing API error handling systems involving 'API error design', 'error codes', 'error responses', 'error catalogs', 'error messages', 'retry strategies', etc. Note: actual error handling code implementation is outside the scope of this skill.
- **rest-api-conventions**: REST API design conventions reference. An extension skill for api-architect that provides URL naming, HTTP method mapping, status code selection, pagination/filtering/sorting patterns, HATEOAS, and versioning strategies. Use when designing RESTful APIs involving 'REST conventions', 'URL design', 'HTTP status codes', 'pagination', 'API versioning', 'HATEOAS', etc. Note: GraphQL design and actual server implementation are outside the scope of this skill.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient domain information | API architect starts with generic CRUD resources; designs an extensible structure |
| REST vs GraphQL undecided | Default to REST; present GraphQL extension options in an appendix |
| Agent failure | Retry once -> If still fails, proceed without that artifact; note the omission in the review report |
| 🔴 found during review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| Existing schema parsing failure | Manually extract endpoints and proceed |
