# CI/CD Pipeline (20)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to design, build, monitor, and optimize CI/CD pipelines.

## Expert Roles
- **infra-engineer**: Infrastructure Engineer. Designs and implements CI/CD runner configuration, container builds (Dockerfile, docker-compose), environment variable/secret management, artifact repositories, and infrastructure provisioning (Terraform).
- **monitoring-specialist**: CI/CD Monitoring Specialist. Designs pipeline metrics (build time, success rate, deployment frequency), alert configuration (Slack, PagerDuty), dashboards, DORA metrics, and SLA/SLO.
- **pipeline-designer**: CI/CD Pipeline Designer. Designs build, test, security scan, and deployment stages; defines branch strategies (GitFlow, Trunk-based), trigger conditions, and per-environment deployment strategies (Blue-Green, Canary, Rolling).
- **pipeline-reviewer**: CI/CD Pipeline Reviewer (QA). Cross-validates pipeline efficiency, reliability, security, and design-implementation alignment.
- **security-scanner**: CI/CD Security Scanner. Integrates SAST (static analysis), DAST (dynamic analysis), SCA (dependency vulnerability), container image scanning, and secret detection into the pipeline.

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
   - **Project Type**: Language/framework (Node.js, Python, Go, Java, etc.)
   - **CI/CD Tool**: GitHub Actions / GitLab CI / Jenkins
   - **Deployment Target**: AWS / GCP / Azure / Kubernetes / Docker
   - **Branch Strategy** (optional): GitFlow, Trunk-based
   - **Existing Files** (optional): Existing CI/CD configuration, Dockerfile, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Artifact |
|-------|------|-------|-------------|----------|
| 1 | Pipeline Design | pipeline-designer | None | `_workspace/01_pipeline_design.md` |
| 2a | Infrastructure Config | infra-engineer | Task 1 | `_workspace/02_pipeline_config/`, `02_infra_config.md` |
| 2b | Security Scan Design | security-scanner | Task 1 | `_workspace/04_security_scan.md` |
| 3 | Monitoring Design | monitoring-specialist | Tasks 1, 2a | `_workspace/03_monitoring.md` |
| 4 | Pipeline Review | pipeline-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (infrastructure) and 2b (security) are **executed in parallel**.

**Inter-team communication flow:**
- pipeline-designer completes -> Delivers stage requirements to infra-engineer, scan placement to security-scanner, deployment strategy to monitoring-specialist
- infra-engineer completes -> Delivers log/metric points to monitoring-specialist, image/dependency paths to security-scanner
- security-scanner completes -> Delivers security alert rules to monitoring-specialist
- pipeline-reviewer cross-validates all artifacts. When 🔴 must-fix issues are found, requests revisions from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: Integration and Final Artifacts

Organize the final artifacts based on the review report:

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 must-fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills
- **deployment-strategies**: Deployment strategy catalog. An extension skill for pipeline-designer that provides pros/cons, implementation patterns, rollback procedures, health check design, and DORA metrics for Blue-Green/Canary/Rolling/A-B Test/Shadow deployment strategies. Use when designing deployment pipelines involving 'deployment strategy', 'Blue-Green', 'Canary', 'Rolling', 'rollback', 'zero-downtime deployment', 'DORA metrics', etc. Note: actual infrastructure configuration and monitoring tool setup are outside the scope of this skill.
- **pipeline-security-gates**: CI/CD pipeline security gate design guide. An extension skill for security-scanner that provides scan tool selection for SAST/DAST/SCA/container scanning/secret detection, gate placement strategies, threshold configuration, and vulnerability classification criteria. Use when integrating pipeline security involving 'security gates', 'SAST', 'DAST', 'SCA', 'container scanning', 'secret detection', 'vulnerability thresholds', etc. Note: actual scan execution and vulnerability remediation are outside the scope of this skill.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| CI/CD tool not specified | Default to GitHub Actions |
| Deployment target not specified | Docker container-based generic configuration |
| Agent failure | Retry once -> If still fails, proceed without that artifact; note the omission in the review report |
| 🔴 found during review | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| Existing YAML parsing failure | Manually analyze and create new configuration files |
