# Design System Harness (36-design-system)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

UI design system construction: a harness in which an agent team collaborates to create design tokens, a component library, Storybook, accessibility verification, and documentation.

## Expert Roles

- **A11y Auditor — Accessibility Verification Specialist**: Accessibility (A11y) verification specialist. Verifies WCAG 2.1 AA/AAA compliance and systematically audits ARIA patterns, keyboard navigation, screen reader compatibility, and color contrast.

- **Component Developer — UI Component Development Specialist**: UI component development specialist. Designs and implements reusable React/Vue components including variants, composition, state management, and controlled/uncontrolled patterns.

- **Doc Writer — Design System Documentation Specialist**: Design system documentation specialist. Writes design principles, component usage guides, design-development handoff guides, contribution guides, and versioning policies.

- **Storybook Builder — Storybook Specialist**: Storybook builder. Creates stories, interaction tests, and documentation pages for each component, and implements design token visualization and theme switching in Storybook.

- **Token Designer — Design Token Specialist**: Design token specialist. Systematically designs the foundational tokens of the design system: colors, typography, spacing, shadows, motion, and responsive breakpoints.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Brand information**: Brand colors, logo, tone and manner
    - **Framework**: React/Vue/Angular/Web Components
    - **Component scope**: Required component list (or "all")
    - **Accessibility level**: WCAG AA (default) / AAA
    - **Existing system** (optional): Existing design system to migrate from
2. Create the `_workspace/` directory and subdirectories
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Token design | token-designer | None | `01_design_tokens/` |
| 2 | Component development | component-developer | Task 1 | `02_components/` |
| 3a | Storybook setup | storybook-builder | Tasks 1, 2 | `03_storybook/` |
| 3b | Accessibility verification | a11y-auditor | Tasks 1, 2 | `04_a11y_report.md` |
| 4 | Documentation | doc-writer | Tasks 1, 2, 3a, 3b | `05_docs/` |

Tasks 3a (Storybook) and 3b (accessibility) run **in parallel**.

**Inter-agent communication flow:**
- token-designer completes > passes token import methods to component-developer, contrast verification to a11y-auditor
- component-developer completes > passes props types to storybook-builder, ARIA status to a11y-auditor
- a11y-auditor > requests fixes from component-developer for P0/P1 issues (up to 2 rounds)
- storybook-builder completes > passes Storybook structure to doc-writer
- a11y-auditor completes > passes accessibility guide to doc-writer
- doc-writer performs final consistency verification across all deliverables

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all accessibility P0 issues are resolved
3. Present the final summary to the user:
    - Token system — `01_design_tokens/`
    - Components — `02_components/`
    - Storybook — `03_storybook/`
    - Accessibility report — `04_a11y_report.md`
    - Documentation — `05_docs/`

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build a complete design system" | **Full pipeline** | All 5 agents |
| "Just design tokens" | **Token mode** | token-designer only |
| "Build components from these tokens" | **Component mode** | component-developer + storybook-builder |
| "Accessibility verification only" | **Verification mode** | a11y-auditor only |
| "Just add Storybook" | **Storybook mode** | storybook-builder only |
| "Just write documentation" | **Doc mode** | doc-writer only |
| "Add just a Button component" | **Single component** | component-developer + a11y-auditor + storybook-builder |

**Reusing existing systems**: If existing tokens are available, skip token-designer. If only adding Storybook to existing components, deploy storybook-builder only.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Code, configuration, documentation |
| Message-based | SendMessage | Key information, fix requests, verification results |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Brand color not provided | Start with neutral palette (slate); request colors from user |
| Framework unspecified | Default to React + TypeScript; change after user confirmation |
| Contrast ratio not met | Auto-adjust and report both original and adjusted values |
| Accessibility P0 unresolved | Block release; request re-fix from component-developer |
| Agent failure | Retry once; if still failing, proceed without that deliverable |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Brand information**: Brand colors, logo, tone and manner
    - **Framework**: React/Vue/Angular/Web Components
    - **Component scope**: Required component list (or "all")
    - **Accessibility level**: WCAG AA (default) / AAA
    - **Existing system** (optional): Existing design system to migrate from
2. Create the `_workspace/` directory and subdirectories
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Token design | token-designer | None | `01_design_tokens/` |
| 2 | Component development | component-developer | Task 1 | `02_components/` |
| 3a | Storybook setup | storybook-builder | Tasks 1, 2 | `03_storybook/` |
| 3b | Accessibility verification | a11y-auditor | Tasks 1, 2 | `04_a11y_report.md` |
| 4 | Documentation | doc-writer | Tasks 1, 2, 3a, 3b | `05_docs/` |

Tasks 3a (Storybook) and 3b (accessibility) run **in parallel**.

**Inter-agent communication flow:**
- token-designer completes > passes token import methods to component-developer, contrast verification to a11y-auditor
- component-developer completes > passes props types to storybook-builder, ARIA status to a11y-auditor
- a11y-auditor > requests fixes from component-developer for P0/P1 issues (up to 2 rounds)
- storybook-builder completes > passes Storybook structure to doc-writer
- a11y-auditor completes > passes accessibility guide to doc-writer
- doc-writer performs final consistency verification across all deliverables

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm all accessibility P0 issues are resolved
3. Present the final summary to the user:
    - Token system — `01_design_tokens/`
    - Components — `02_components/`
    - Storybook — `03_storybook/`
    - Accessibility report — `04_a11y_report.md`
    - Documentation — `05_docs/`

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build a complete design system" | **Full pipeline** | All 5 agents |
| "Just design tokens" | **Token mode** | token-designer only |
| "Build components from these tokens" | **Component mode** | component-developer + storybook-builder |
| "Accessibility verification only" | **Verification mode** | a11y-auditor only |
| "Just add Storybook" | **Storybook mode** | storybook-builder only |
| "Just write documentation" | **Doc mode** | doc-writer only |
| "Add just a Button component" | **Single component** | component-developer + a11y-auditor + storybook-builder |

**Reusing existing systems**: If existing tokens are available, skip token-designer. If only adding Storybook to existing components, deploy storybook-builder only.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Code, configuration, documentation |
| Message-based | SendMessage | Key information, fix requests, verification results |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Brand color not provided | Start with neutral palette (slate); request colors from user |
| Framework unspecified | Default to React + TypeScript; change after user confirmation |
| Contrast ratio not met | Auto-adjust and report both original and adjusted values |
| Accessibility P0 unresolved | Block release; request re-fix from component-developer |
| Agent failure | Retry once; if still failing, proceed without that deliverable |

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input and brand information
- `01_design_tokens/` — Design token definition files
- `02_components/` — Component library code
- `03_storybook/` — Storybook stories and configuration
- `04_a11y_report.md` — Accessibility verification report
- `05_docs/` — Design system documentation

## Extension Skills

Skills that enhance each agent's domain expertise:

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| wcag-checker | `.claude/skills/wcag-checker/skill.md` | a11y-auditor, component-developer | WCAG 2.1 accessibility checklist, contrast calculation, ARIA patterns, keyboard matrix |
| token-generator | `.claude/skills/token-generator/skill.md` | token-designer, component-developer | Design token 3-tier structure, color scale algorithm, typography/spacing/motion system |
