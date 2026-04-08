# Infra As Code (26)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for Infrastructure as Code (IaC) design and implementation. Automates Terraform/Pulumi-based environment configuration, security, and cost optimization pipelines.

## Expert Roles
- **Cost Optimizer**: Cloud cost optimization expert. Optimizes infrastructure costs based on resource sizing, reserved instances, spot utilization, and FinOps culture.
  - **Resource Sizing**: Determine optimal instance types and sizes for the workload
  - **Purchase Option Strategy**: Determine the optimal mix of On-Demand, Reserved, Savings Plan, and Spot
  - **Cost Estimation**: Estimate monthly/annual costs per environment and visualize the cost structure
  - **Cost Reduction Opportunities**: Identify idle resources, over-provisioning, and scheduling-based savings opportunities
  - **Cost Governance**: Design budget alerts, cost tagging, and cost allocation reports
- **Drift Detector**: Drift detection expert. Detects differences between IaC state and actual infrastructure, verifies policy compliance, and establishes auto-remediation strategies.
  - **Configuration Drift Detection**: Detect differences between code and actual state using terraform plan/pulumi preview
  - **Policy Compliance Verification**: Verify adherence to security policies, tagging policies, and naming conventions
  - **Auto-remediation Strategy**: Design automatic/manual remediation methods per drift type
  - **Change Tracking**: Establish processes for tracking manual changes and reflecting them in code
  - **Regular Audits**: Design drift detection schedules, reports, and escalation policies
- **Iac Reviewer**: IaC reviewer (QA). Cross-validates consistency across design, security, cost, and drift, and verifies IaC best practices adherence.
  - **Design-Security Consistency**: Are security groups correctly mapped to the network design?
  - **Design-Cost Consistency**: Are resource specifications appropriate for the workload and cost-efficient?
  - **Security-Drift Consistency**: Are security policies reflected in drift detection?
  - **IaC Code Quality**: Modularization, DRY, naming, version pinning, and other code quality checks
  - **Operational Readiness**: Are failure response, DR, backup, and monitoring included in the design?
- **Infra Architect**: Infrastructure design expert. Designs cloud architecture, defines Terraform/Pulumi module structures, and establishes environment separation strategies and state management.
  - **Architecture Design**: Design the entire infrastructure topology including VPC, subnets, load balancers, compute, storage, and DB
  - **IaC Module Structure**: Organize reusable Terraform/Pulumi modules hierarchically
  - **Environment Separation**: Separate dev/staging/prod environments through code and manage per-environment variables
  - **State Management**: Establish remote state backend, state locking, and workspace strategy
  - **Provisioning Pipeline**: Design the plan -> apply -> verify pipeline
- **Security Engineer**: Infrastructure security expert. Designs IAM policies, network security, data encryption, and compliance adherence, implementing security policies as code.
  - **IAM Design**: Design roles, policies, and service accounts following the principle of least privilege
  - **Network Security**: Configure security groups, NACLs, WAF, and DDoS protection
  - **Data Protection**: Design encryption at-rest and in-transit
  - **Secret Management**: Establish strategies for managing sensitive information via Vault/SSM/Secrets Manager
  - **Compliance**: Implement compliance policies as code for CIS Benchmark, SOC 2, ISMS, etc.

## Workflow
### Phase 1: Preparation (Performed directly by Orchestrator)

1. Extract from user input:
    - **Infrastructure Requirements**: What service the infrastructure is for
    - **Cloud Provider** (optional): AWS / GCP / Azure
    - **IaC Tool** (optional): Terraform / Pulumi / OpenTofu
    - **Constraints** (optional): Budget, compliance, existing infrastructure
    - **Existing Code** (optional): Existing IaC code, architecture documents
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are available, copy them to `_workspace/` and skip the corresponding Phase
5. Determine **execution mode** based on the scope of the request (see "Modes by Task Scale" below)

### Phase 2: Team Assembly and Execution

| Order | Task | Assignee | Dependencies | Deliverable |
|-------|------|----------|-------------|-------------|
| 1 | Infrastructure Design | architect | None | `_workspace/01_infra_design.md` |
| 2a | Security Design | security | Task 1 | `_workspace/02_security_design.md` |
| 2b | Cost Analysis | cost | Task 1 | `_workspace/03_cost_analysis.md` |
| 3 | Drift Policy | drift | Tasks 1, 2a | `_workspace/04_drift_policy.md` |
| 4 | Final Review | reviewer | Tasks 1-3 | `_workspace/05_review_report.md` |

Tasks 2a (security) and 2b (cost) can be **executed in parallel**.

**Inter-team Communication Flow:**
- architect completes -> delivers network, IAM, data stores to security; delivers resource specs and scaling to cost; delivers module structure and core resources to drift
- security completes -> delivers security policies and compliance checks to drift; delivers security cost items to cost
- cost completes -> delivers cost anomaly detection criteria to drift
- reviewer cross-validates all deliverables. Requests fixes for RED Must Fix items (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Check all files in `_workspace/`
2. Verify all RED Must Fix items have been addressed
3. Report the final summary to the user

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_infra_design.md` — Infrastructure design document
- `02_security_design.md` — Security design document
- `03_cost_analysis.md` — Cost analysis report
- `04_drift_policy.md` — Drift detection policy
- `05_review_report.md` — Final review report

## Extension Skills
- **cloud-cost-models**: AWS/GCP/Azure cost models, sizing guides, Reserved Instance/Savings Plan strategies, and FinOps framework guide. Use this skill for 
- **terraform-module-patterns**: Detailed guide on Terraform module design patterns, directory structures, state management, and environment separation strategies. Use this skill for 

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Provider undecided | Design with AWS as default, note multi-cloud considerations |
| Scale unestimable | Start small + Auto Scaling for elastic response |
| Agent failure | Retry once -> if fails, proceed without that deliverable, note omission in review |
| RED found in review | Request fix from relevant agent -> rework -> re-verify (up to 2 times) |
| Existing infrastructure conflict | Include terraform import strategy, establish gradual migration plan |
