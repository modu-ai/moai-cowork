# Chatbot Builder Harness (38-chatbot-builder)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

Chatbot construction: a harness where an agent team collaborates to perform intent analysis, conversation design, NLU development, integration, and testing.

## Expert Roles

- **Conversation Designer — Dialog Flow Specialist**: Conversation designer. Designs the chatbot's conversation scenarios, flowcharts, fallback strategies, and multi-turn dialog management. Builds a conversation structure that covers the entire user journey.

- **Dialog Tester — Chatbot Quality Assurance Specialist**: Dialog tester. Performs chatbot conversation scenario testing, edge case verification, persona consistency checks, and performance measurement. Serves as the quality gate.

- **Integration Engineer — System Integration Specialist**: Integration engineer. Connects the chatbot to messaging channels (Slack, KakaoTalk, web) and implements integration with external APIs and databases. Responsible for deployment and infrastructure.

- **NLU Developer — Natural Language Understanding Developer**: NLU developer. Designs and implements the natural language understanding pipeline. Responsible for intent classification models, entity extraction, context management, and prompt engineering.

- **Persona Architect — Chatbot Persona Designer**: Chatbot persona designer. Defines the bot's personality, speech style, tone and manner, and brand alignment. Establishes persona guidelines to ensure consistent user experience.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Chatbot purpose**: Customer service/FAQ/reservations/orders/consultation, etc.
    - **Target users**: Age, digital literacy, expectation level
    - **Integration channels**: Slack/KakaoTalk/Telegram/Web/multi-channel
    - **Domain knowledge**: Business rules, FAQ list, product information, etc.
    - **Constraints** (optional): Technology stack, response time requirements
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request (see "Execution Modes by Request Scope" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Persona design | persona | None | `_workspace/01_persona_spec.md` |
| 2 | Conversation design | designer | Task 1 | `_workspace/02_conversation_design.md` |
| 3a | NLU implementation | nlu-dev | Task 2 | `_workspace/03_nlu_config.md` + `src/` |
| 3b | Integration design | integrator | Task 2 | `_workspace/04_integration_spec.md` + `src/` |
| 4 | Testing | tester | Tasks 3a, 3b | `_workspace/05_test_report.md` |

Tasks 3a (NLU) and 3b (integration) run **in parallel**.

**Inter-agent communication flow:**
- persona completes > passes tone and manner guide to designer, passes domain keywords to nlu-dev
- designer completes > passes intent/entity catalog to nlu-dev, passes external integration flows to integrator
- nlu-dev completes > passes NLU interface to integrator, passes test data to tester
- integrator completes > passes test environment info to tester
- tester cross-validates all deliverables. On CRITICAL findings, requests corrections from the relevant agent > rework > re-verification (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Finalize deliverables based on the tester's report:

1. Verify all files in `_workspace/` and `src/` code
2. Confirm that all CRITICAL findings have been resolved
3. Report the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build me a chatbot", "full build" | **Full pipeline** | All 5 agents |
| "Just do the conversation design", "write scenarios" | **Design mode** | persona + designer |
| "Just develop the NLU" (design complete) | **NLU mode** | nlu-dev + tester |
| "Integrate chatbot with KakaoTalk" (implementation complete) | **Integration mode** | integrator + tester |
| "Test the chatbot" (implementation complete) | **Test mode** | tester only |

**Reusing existing files**: If the user provides an existing conversation design document or NLU configuration, copy those files to `_workspace/` and skip the corresponding steps.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Design documents and configuration sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Code-based | `_workspace/src/` | Executable source code |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient domain knowledge | Request additional FAQ list/business information from user, supplement with web search |
| Channel API changes | Verify latest API documentation via WebFetch, then update integration code |
| NLU accuracy below threshold | Augment training data > redesign prompts > strengthen fallback, in that order |
| Agent failure | Retry once > if still failing, proceed without that deliverable and note in report |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Chatbot purpose**: Customer service/FAQ/reservations/orders/consultation, etc.
    - **Target users**: Age, digital literacy, expectation level
    - **Integration channels**: Slack/KakaoTalk/Telegram/Web/multi-channel
    - **Domain knowledge**: Business rules, FAQ list, product information, etc.
    - **Constraints** (optional): Technology stack, response time requirements
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request (see "Execution Modes by Request Scope" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Persona design | persona | None | `_workspace/01_persona_spec.md` |
| 2 | Conversation design | designer | Task 1 | `_workspace/02_conversation_design.md` |
| 3a | NLU implementation | nlu-dev | Task 2 | `_workspace/03_nlu_config.md` + `src/` |
| 3b | Integration design | integrator | Task 2 | `_workspace/04_integration_spec.md` + `src/` |
| 4 | Testing | tester | Tasks 3a, 3b | `_workspace/05_test_report.md` |

Tasks 3a (NLU) and 3b (integration) run **in parallel**.

**Inter-agent communication flow:**
- persona completes > passes tone and manner guide to designer, passes domain keywords to nlu-dev
- designer completes > passes intent/entity catalog to nlu-dev, passes external integration flows to integrator
- nlu-dev completes > passes NLU interface to integrator, passes test data to tester
- integrator completes > passes test environment info to tester
- tester cross-validates all deliverables. On CRITICAL findings, requests corrections from the relevant agent > rework > re-verification (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

Finalize deliverables based on the tester's report:

1. Verify all files in `_workspace/` and `src/` code
2. Confirm that all CRITICAL findings have been resolved
3. Report the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build me a chatbot", "full build" | **Full pipeline** | All 5 agents |
| "Just do the conversation design", "write scenarios" | **Design mode** | persona + designer |
| "Just develop the NLU" (design complete) | **NLU mode** | nlu-dev + tester |
| "Integrate chatbot with KakaoTalk" (implementation complete) | **Integration mode** | integrator + tester |
| "Test the chatbot" (implementation complete) | **Test mode** | tester only |

**Reusing existing files**: If the user provides an existing conversation design document or NLU configuration, copy those files to `_workspace/` and skip the corresponding steps.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Design documents and configuration sharing |
| Message-based | SendMessage | Real-time key information transfer, correction requests |
| Code-based | `_workspace/src/` | Executable source code |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient domain knowledge | Request additional FAQ list/business information from user, supplement with web search |
| Channel API changes | Verify latest API documentation via WebFetch, then update integration code |
| NLU accuracy below threshold | Augment training data > redesign prompts > strengthen fallback, in that order |
| Agent failure | Retry once > if still failing, proceed without that deliverable and note in report |

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input summary
- `01_persona_spec.md` — Bot persona specification
- `02_conversation_design.md` — Conversation design document
- `03_nlu_config.md` — NLU configuration and training data
- `04_integration_spec.md` — Integration specification
- `05_test_report.md` — Test report
- `src/` — Chatbot source code

## Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| intent-taxonomy-builder | `.claude/skills/intent-taxonomy-builder/skill.md` | nlu-developer, conversation-designer | Intent taxonomy design, entity-slot mapping, training data generation, confusion matrix |
| conversation-flow-validator | `.claude/skills/conversation-flow-validator/skill.md` | dialog-tester, conversation-designer | Dialog flow defect detection, Happy/Sad/Edge testing, fallback hierarchy, quality metrics |
