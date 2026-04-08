# Mobile App Builder (17)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to perform UI/UX design, native code generation, API integration, and store deployment preparation for mobile apps.

## Expert Roles
- **api-integrator**: API integration specialist. Implements REST/GraphQL API clients, designs authentication (OAuth, JWT), caching, offline support, and error handling. Optimizes the data flow between server and app.
- **app-developer**: Mobile app developer. Generates native/cross-platform code using Swift/SwiftUI, Kotlin/Jetpack Compose, Flutter, or React Native. Applies architecture patterns (MVVM, Clean Architecture) and implements testable structures.
- **qa-engineer**: Mobile QA engineer. Performs UI testing, performance testing, accessibility verification, security checks, and platform compatibility testing. Cross-verifies consistency across all deliverables.
- **store-manager**: App store deployment manager. Prepares metadata, screenshot guides, privacy policies, and review response strategies needed for App Store Connect and Google Play Console.
- **ux-designer**: Mobile UX/UI designer. Designs wireframes, design systems, navigation structures, and interaction patterns. Follows iOS HIG and Material Design guidelines while incorporating accessibility (A11y) considerations.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
   - **App Type**: What kind of app (social, commerce, utility, game, etc.)
   - **Platform**: iOS / Android / Cross-platform
   - **Framework Preference** (optional): Flutter, React Native, SwiftUI, Jetpack Compose
   - **Backend API** (optional): If an existing API spec exists
   - **Existing Files** (optional): Design, code, API specs, etc.
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on request scope (see "Scale-Based Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverables |
|-------|------|-------|-------------|--------------|
| 1 | UX/UI Design | ux-designer | None | `_workspace/01_ux_design.md` |
| 2a | App Code Generation | app-developer | Task 1 | `_workspace/02_app_code/`, `02_app_architecture.md` |
| 2b | Store Metadata | store-manager | Task 1 | `_workspace/04_store_listing.md` |
| 3 | API Integration | api-integrator | Tasks 1, 2a | `_workspace/03_api_integration.md` |
| 4 | QA Verification | qa-engineer | Tasks 2a, 2b, 3 | `_workspace/05_qa_report.md` |

Tasks 2a (app code) and 2b (store metadata) run **in parallel**.

**Inter-team Communication Flow:**
- ux-designer completes → delivers screen structure/design tokens to app-developer, screenshot scenarios to store-manager, data fields to api-integrator
- app-developer completes → delivers Repository interfaces to api-integrator, permission list to store-manager
- api-integrator completes → delivers API client code to app-developer
- qa-engineer cross-verifies all deliverables. On 🔴 required fix: requests fix from relevant agent → rework → re-verify (max 2 rounds)

### Phase 3: Integration and Final Deliverables

Organize final deliverables based on the QA report:

1. Verify all files in `_workspace/`
2. Confirm all 🔴 required fixes from the QA report have been addressed
3. Report final summary to the user:
   - UX Design — `01_ux_design.md`
   - App Architecture — `02_app_architecture.md`
   - App Code — `02_app_code/`
   - API Integration — `03_api_integration.md`
   - Store Deployment — `04_store_listing.md`
   - QA Report — `05_qa_report.md`

## Deliverables
- `00_input.md` — Organized user input
- `01_ux_design.md` — UX/UI design document
- `02_app_code/` — App source code
- `02_app_architecture.md` — App architecture document
- `03_api_integration.md` — API integration specification
- `04_store_listing.md` — Store deployment metadata
- `05_qa_report.md` — QA verification report

## Extension Skills
- **app-store-optimization**: App Store Optimization (ASO) guide. Provides App Store/Google Play metadata optimization, keyword strategy, screenshot guidelines, review rejection response, and category selection as a store-manager extension skill. Use for requests like 'ASO', 'app store optimization', 'keyword strategy', 'screenshot guide', 'review response', 'app description writing', and other store deployment optimization tasks. However, actual store submission or ad management is outside this skill's scope.
- **mobile-ux-patterns**: Mobile UX design pattern library. Provides iOS HIG/Material Design 3 guidelines, navigation patterns, gesture interactions, responsive layouts, and accessibility checklists as a ux-designer extension skill. Use for requests like 'mobile UX', 'iOS guidelines', 'Material Design', 'navigation patterns', 'gestures', 'design tokens', 'mobile accessibility', and other mobile UI/UX design tasks. However, actual design file creation or code implementation is outside this skill's scope.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Platform unspecified | UX designer defaults to cross-platform (Flutter), reflecting both platform guidelines |
| No backend API | API integrator designs mock API, structured for easy replacement with real API |
| Agent failure | Retry once → proceed without that deliverable if failed, note in QA report |
| 🔴 found in QA | Request fix from relevant agent → rework → re-verify (max 2 rounds) |
| Framework compatibility | App developer suggests alternative framework with pros/cons comparison |
