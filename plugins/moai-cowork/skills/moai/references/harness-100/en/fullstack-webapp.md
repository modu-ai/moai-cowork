# Full-Stack Web App (16)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to develop fullstack web apps through the pipeline of requirements, design, frontend, backend, testing, and deployment.

## Expert Roles
- **architect**: System architect. Analyzes requirements and performs system architecture, technology stack selection, DB modeling, and API design. Produces design documents that enable frontend/backend/QA/DevOps teams to begin work immediately.
- **backend-dev**: Backend developer. Implements APIs, database integration, authentication/authorization, and business logic. Translates the architecture design's API spec and DB schema into code.
- **devops-engineer**: DevOps engineer. Handles CI/CD pipeline setup, infrastructure configuration, deployment automation, and monitoring. Designs and implements the deployment path from development to production.
- **frontend-dev**: Frontend developer. Implements React/Next.js frontend based on the architecture design. Handles UI components, page routing, state management, API integration, and responsive design.
- **qa-engineer**: QA engineer. Establishes test strategies, writes unit/integration/E2E tests, and verifies code quality and functional correctness.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
   - **App Description**: Purpose and core features of the web app to build
   - **Technology Stack** (optional): Preferred frameworks/libraries
   - **Scale** (optional): MVP/small/medium/large
   - **Existing Code** (optional): Existing project to extend
   - **Deployment Platform** (optional): Vercel/AWS/Docker, etc.
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing code is provided, analyze it and adjust relevant phases
5. Determine **execution mode** based on request scope (see "Scale-Based Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverables |
|-------|------|-------|-------------|--------------|
| 1 | Architecture Design | architect | None | `01_architecture.md`, `02_api_spec.md`, `03_db_schema.md` |
| 2a | Frontend Development | frontend | Task 1 | `src/` frontend code |
| 2b | Backend Development | backend | Task 1 | `src/` backend code |
| 2c | Deployment Setup | devops | Task 1 | `05_deploy_guide.md`, CI/CD config |
| 3 | Testing & Review | qa | Tasks 2a, 2b | `04_test_plan.md`, `06_review_report.md`, test code |

Tasks 2a (frontend), 2b (backend), and 2c (DevOps) run **in parallel**. All depend only on Task 1 (design).

**Inter-team Communication Flow:**
- architect completes → delivers component structure/routing to frontend, API/DB/auth to backend, infrastructure requirements to devops, functional requirements to qa
- frontend ↔ backend: Real-time communication during API integration (endpoint changes, error formats, etc.)
- devops completes → shares environment variables and deployment URLs with all
- qa reviews all code and tests. On 🔴 required fix: requests fix from the relevant developer → rework → re-verify (max 2 rounds)

### Phase 3: Integration and Final Deliverables

Organize final deliverables based on the QA review:

1. Verify all code and documents
2. Confirm all 🔴 required fixes from the review have been addressed
3. Report final summary to the user:
   - Architecture Design — `_workspace/01_architecture.md`
   - API Specification — `_workspace/02_api_spec.md`
   - DB Schema — `_workspace/03_db_schema.md`
   - Test Plan — `_workspace/04_test_plan.md`
   - Deployment Guide — `_workspace/05_deploy_guide.md`
   - Review Report — `_workspace/06_review_report.md`
   - Source Code — `src/` directory

## Deliverables
- `_workspace/00_input.md` — Organized user input
- `_workspace/01_architecture.md` — Architecture design document
- `_workspace/02_api_spec.md` — API specification
- `_workspace/03_db_schema.md` — DB schema
- `_workspace/04_test_plan.md` — Test plan
- `_workspace/05_deploy_guide.md` — Deployment guide
- `_workspace/06_review_report.md` — Review report
- `src/` — Source code (frontend + backend)

## Extension Skills
- **api-security-checklist**: Web app API security checklist. Provides OWASP Top 10-based vulnerability checks, authentication/authorization patterns, input validation, Rate Limiting, CORS, CSRF, and SQL Injection defense as a backend-dev extension skill. Use for requests like 'API security', 'OWASP', 'auth implementation', 'SQL Injection', 'XSS defense', 'CORS configuration', 'security checklist', and other backend security design tasks. However, penetration testing or WAF configuration is outside this skill's scope.
- **component-patterns**: React/Next.js component design pattern library. Provides Compound/Render Props/HOC/Custom Hooks patterns, state management strategies (Zustand/React Query/Context), and folder structure conventions as a frontend-dev extension skill. Use for requests like 'component patterns', 'React patterns', 'state management', 'folder structure', 'Custom Hook', 'component separation', and other frontend architecture design tasks. However, actual code implementation or backend logic is outside this skill's scope.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Ambiguous requirements | Apply the most common CRUD pattern, document assumptions |
| Unspecified tech stack | Apply default stack by scale (MVP: Next.js + SQLite) |
| Build errors | Analyze error logs → relevant developer fixes → QA re-verifies |
| Agent failure | Retry once → proceed without that deliverable if failed, note in review |
| 🔴 found in review | Request fix from relevant developer → rework → re-verify (max 2 rounds) |
