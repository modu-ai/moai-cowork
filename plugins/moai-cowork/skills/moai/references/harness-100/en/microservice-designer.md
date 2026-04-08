# Microservice Designer (23)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for designing, decomposing, communicating, and monitoring microservice architectures. Automates the full pipeline from domain analysis to observability design.

## Expert Roles
- **Architecture Reviewer**: Microservice architecture reviewer (QA). Cross-validates consistency across domain, service, communication, and observability designs, and identifies potential risks in distributed systems.
  - **Domain-Service Consistency**: Do bounded contexts align with service boundaries?
  - **Service-Communication Consistency**: Are API contracts consistent with communication design? Are Sagas designed without gaps?
  - **Communication-Observability Consistency**: Is tracing configured for all communication paths? Are alerts complete?
  - **Distributed System Anti-pattern Detection**: Distributed monolith, shared DB, excessive synchronous calls, etc.
  - **Operational Readiness Assessment**: 12-Factor compliance, health checks, graceful shutdown, configuration management
- **Communication Designer**: Inter-service communication design expert. Selects synchronous/asynchronous communication patterns, designs event buses, and configures API gateways and service meshes.
  - **Communication Pattern Selection**: Choose the appropriate pattern from request-response (sync), event-driven (async), CQRS, and Saga
  - **Event Bus Design**: Establish message broker (Kafka/RabbitMQ/NATS) topology, topic design, and partitioning strategy
  - **API Gateway Design**: Configure routing, authentication, rate limiting, caching, and request transformation
  - **Service Mesh Configuration**: Design sidecar proxies, mTLS, traffic management, and circuit breakers
  - **Data Consistency Strategy**: Design Saga patterns (Choreography/Orchestration) and compensating transactions
- **Domain Analyst**: Domain analysis expert. Analyzes business domains from a DDD perspective, identifies bounded contexts, and derives domain events and aggregates through event storming.
  - **Bounded Context Identification**: Separate business areas into independent contexts and create context maps
  - **Event Storming**: Derive domain events, commands, aggregates, and policies
  - **Aggregate Design**: Define consistency boundaries and identify aggregate roots
  - **Ubiquitous Language Definition**: Organize core domain-specific terms to establish a shared language across the team
  - **Inter-context Relationship Mapping**: Determine relationship patterns such as Upstream/Downstream, ACL, Shared Kernel
- **Observability Engineer**: Observability design expert. Establishes metrics, logging, and tracing strategies for distributed systems, and designs alerting rules and dashboards.
  - **Metrics Design**: Define RED (Rate, Errors, Duration) / USE (Utilization, Saturation, Errors) metrics per service
  - **Distributed Tracing**: Establish OpenTelemetry-based trace propagation, span design, and sampling strategies
  - **Structured Logging**: Design log levels, formats, correlation ID propagation, and centralized logging pipelines
  - **Alerting System**: Design alert thresholds, escalation policies, and on-call rotations
  - **Dashboard Design**: Define per-service and per-business dashboard layouts and key panels
- **Service Architect**: Microservice design expert. Maps bounded contexts to services, defines API contracts, and designs data ownership and deployment units.
  - **Service Decomposition**: Map bounded contexts to deployable service units
  - **API Contract Design**: Define inter-service interfaces as OpenAPI/gRPC/AsyncAPI specs
  - **Data Ownership**: Determine data ownership and sharing strategies following the Database-per-Service principle
  - **Service Templates**: Determine each service's internal architecture (Hexagonal/Clean/Layered)
  - **Deployment Strategy**: Design per-service scaling policies, containerization, and service mesh configuration

## Workflow
### Phase 1: Preparation (Performed directly by Orchestrator)

1. Extract from user input:
    - **Business Domain**: What system/service is being designed
    - **Current State** (optional): Whether this is a monolith migration or a greenfield design
    - **Scale/Constraints** (optional): Expected traffic, team size, technology stack limitations
    - **Existing Documentation** (optional): ERD, architecture documents, API documentation, etc.
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assignee | Dependencies | Deliverable |
|-------|------|----------|-------------|-------------|
| 1 | Domain Analysis | analyst | None | `_workspace/01_domain_analysis.md` |
| 2 | Service Design | architect | Task 1 | `_workspace/02_service_design.md` |
| 3a | Communication Design | comm-designer | Tasks 1, 2 | `_workspace/03_communication_design.md` |
| 3b | Observability Design | obs-engineer | Task 2 | `_workspace/04_observability_design.md` |
| 4 | Architecture Review | reviewer | Tasks 1-3b | `_workspace/05_review_report.md` |

Tasks 3a (communication) and 3b (observability) can be **executed in parallel**.

**Inter-team Communication Flow:**
- analyst completes -> delivers bounded contexts and aggregates to architect; delivers domain events to comm-designer
- architect completes -> delivers service catalog and API contracts to comm-designer; delivers service list and dependencies to obs-engineer
- comm-designer completes -> delivers communication matrix and Saga flows to obs-engineer
- reviewer cross-validates all deliverables. When RED Must Fix items are found, requests fixes from the relevant agent -> rework -> re-verification (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Check all files in `_workspace/`
2. Verify that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_domain_analysis.md` — Domain analysis report
- `02_service_design.md` — Service design document
- `03_communication_design.md` — Communication design document
- `04_observability_design.md` — Observability design document
- `05_review_report.md` — Final review report

## Extension Skills
- **ddd-context-mapping**: Detailed methodology for DDD (Domain-Driven Design) bounded context identification, context map creation, and event storming execution. Use this skill for 
- **distributed-patterns**: Implementation guide and selection matrix for core distributed system patterns (Saga, CQRS, Circuit Breaker, Event Sourcing, etc.). Use this skill for 

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Insufficient domain information | Draft using similar domain reference patterns, request user validation |
| Too many services | Suggest modular monolith -> gradual decomposition roadmap |
| Agent failure | Retry once -> if fails, proceed without that deliverable, note omission in review |
| RED found in review | Request fix from relevant agent -> rework -> re-verify (up to 2 times) |
| Distributed monolith signs | Request service boundary readjustment from architect |
