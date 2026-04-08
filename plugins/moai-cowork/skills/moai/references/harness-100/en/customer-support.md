# Customer Support (49)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

Build a customer support system: an agent team collaborates to produce FAQ, response manuals, escalation policies, and analytics.

## Expert Roles

- **CS Analyst**: CS analytics expert. Designs customer support performance metric systems, VOC (Voice of Customer) analysis frameworks, trend analysis, and service improvement proposals.
  - Metric System Design: Define key CS metrics such as CSAT, NPS, FCR, and AHT, and design measurement methods
  - VOC Analysis Framework: Design a system for collecting, classifying, and analyzing customer feedback
  - Trend Analysis: Build a framework for detecting inquiry type trends, seasonal patterns, and anomalies
  - Service Improvement Proposals: Identify data-driven improvement opportunities and propose priorities
  - Reporting System Design: Define daily/weekly/monthly CS report templates and dashboard items

- **CS Reviewer**: Customer support system reviewer (QA). Cross-validates consistency across FAQ, response manual, escalation policy, and analytics, and evaluates system completeness from a customer experience perspective.
  - FAQ ↔ Manual Consistency: Verify that FAQ answers and response manual scripts provide identical information
  - Manual ↔ Escalation Consistency: Confirm that escalation triggers are correctly reflected in the manual
  - Escalation ↔ Analytics Consistency: Ensure SLA metrics are measurable within the analytics framework
  - Customer Journey Simulation: Simulate actual customer inquiry journeys to discover gaps
  - Tone & Manner Consistency: Verify that all customer-facing expressions across documents maintain a consistent tone

- **Escalation Manager**: Escalation management expert. Designs tiered escalation policies, routing rules, SLAs, and crisis response protocols for customer inquiries.
  - Escalation Tier Design: Define tiers from L1 (frontline) → L2 (specialist) → L3 (manager) → L4 (executive)
  - Routing Rules: Design automatic routing rules based on issue type, severity, and customer tier
  - SLA Design: Define response times, resolution times, and escalation times by tier and type
  - Crisis Response Protocol: Design protocols for crisis situations such as large-scale outages, media exposure, and legal issues
  - Authority Matrix: Define the scope of actions (refunds, compensation, exceptions) available at each tier

- **FAQ Builder**: FAQ construction expert. Analyzes customer inquiry patterns to systematically build categorized FAQs, and designs structures for search optimization and self-service rate improvement.
  - Question Collection & Classification: Derive expected questions based on product/service characteristics and classify them by category
  - Answer Writing: Write clear and actionable answers matched to the customer's level of understanding
  - Hierarchical Structure Design: Design a hierarchy of top-level category, subcategory, and individual FAQ
  - Search Optimization: Map natural language expressions customers use (synonyms, similar questions)
  - Self-Service Optimization: Improve self-resolution rates using images, step-by-step guides, and links

- **Response Specialist**: Response manual expert. Creates customer response scripts by situation, tone and manner guides, and emotional response protocols. Designs channel-specific (phone/chat/email) response systems.
  - Scenario-Based Scripts: Write response scripts for different situations such as general inquiries, complaints, refunds, and technical support
  - Tone & Manner Guide: Define the response tone matching the brand voice, prohibited expressions, and recommended expressions
  - Emotional Response Protocol: Design emotional response steps for angry, anxious, and disappointed customers
  - Channel-Specific Guide: Write response guidelines and differences for each channel: phone/chat/email/social media
  - New Agent Onboarding: Create first-week essential knowledge items and role-play scenarios

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Service Information**: Product/service name, type, customer base size
    - **Support Channels**: Which channels are in use — phone/chat/email/social media
    - **Current State**: Whether an existing CS system exists, team size
    - **Existing Materials** (optional): Existing FAQs, manuals, data
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | FAQ Construction | faq-builder | None | `_workspace/01_faq.md` |
| 1b | Response Manual | response-specialist | None | `_workspace/02_response_manual.md` |
| 2 | Escalation Policy | escalation-manager | Tasks 1a, 1b | `_workspace/03_escalation_policy.md` |
| 3 | CS Analytics Framework | cs-analyst | Tasks 1a, 1b, 2 | `_workspace/04_cs_analytics.md` |
| 4 | CS Review | cs-reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_review_report.md` |

Tasks 1a (FAQ) and 1b (Manual) are **executed in parallel**. Both can start simultaneously as they have no initial dependencies.

**Inter-team Communication Flow:**
- faq-builder completes → delivers out-of-FAQ-scope scenarios to response-specialist, delivers self-service boundary to escalation-manager
- response-specialist completes → delivers escalation trigger conditions to escalation-manager
- escalation-manager completes → delivers SLA metrics to cs-analyst
- cs-analyst completes → delivers all documents to cs-reviewer
- cs-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills

- **csat-analyzer**: CSAT/NPS/CES design, operational metrics, VOC analysis, CS dashboard design
- **escalation-flowchart**: L1/L2/L3 structure, severity classification, trigger conditions, SLA matrix, crisis response

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient service info | Build a generic CS system based on industry type, tag as "requires service customization" |
| No existing CS data | Set targets based on industry benchmarks, propose initial measurement methods |
| Web search failure | Work from general CS best practices, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable, note the omission in the review report |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
