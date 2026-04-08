# Sales Enablement (48)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

A sales enablement pipeline where an agent team collaborates to produce: Customer Analysis, Proposal, Presentation, and Follow-up Plan.

## Expert Roles

- **Customer Analyst**: Customer Analysis Expert. Analyzes the target customer's business situation, needs, decision-making structure, budget, and competitive solution usage to provide the foundation for a tailored sales strategy.
  - Customer Profiling: Comprehensively analyze company size, industry, revenue, organizational structure, and recent news
  - Needs Analysis: Identify the customer's business challenges (pain points) and strategic priorities
  - Decision-Making Mapping: Identify the DMU (Decision Making Unit) — decision-makers, influencers, gatekeepers, and end users
  - Competitive Landscape Assessment: Analyze the solutions the customer currently uses and barriers to switching
  - Budget & Timeline Estimation: Estimate purchase budget, decision-making timeline, and procurement process

- **Follow-up Manager**: Sales Follow-up Management Expert. Develops post-proposal follow-up schedules, email templates, objection handling scripts, and action plans through to contract closure.
  - Follow-up Schedule Design: Define touchpoint actions for Day 1/3/7/14/30 after the proposal
  - Email Template Creation: Write situation-specific emails (thank you/reminder/additional materials/objection response/closing push)
  - Objection Handling: Prepare response scripts for each anticipated objection
  - Negotiation Strategy: Set response ranges and red lines for price and terms negotiation scenarios
  - Pipeline Management: Provide transition criteria and checklists for each deal stage

- **Presenter**: Sales Presentation Design Expert. Converts proposal content into a persuasive presentation storyline and slide structure. Designs tailored messaging for each DMU role.
  - Storyline Design: Design a persuasion structure following Customer Challenge → Solution → Evidence → CTA
  - Slide Structure: Create key messages, visual guides, and speaker notes for each slide
  - DMU-Specific Messaging: Differentiate emphasis for each audience type — executives, operational leads, technical teams
  - Demo Scenario Design: When live demonstrations are needed, design the demo scenario
  - Q&A Preparation: Prepare anticipated questions and recommended answers

- **Proposal Writer**: Sales Proposal Writing Expert. Creates customized solution proposals based on customer analysis results, including value proposition, solution matching, ROI calculation, and pricing.
  - Value Proposition Design: Structure solution matching and expected outcomes for each customer pain point
  - ROI Calculation: Compute quantitative benefits (cost savings, revenue increase, productivity improvement) relative to adoption costs
  - Solution Architecture Design: Configure product/service packages aligned with customer needs
  - Pricing Proposal: Design competitive pricing options (tiered, bundled, annual/monthly)
  - Implementation Plan: Present implementation timeline, milestones, and success criteria

- **Sales Reviewer**: Sales Enablement Reviewer (QA). Cross-validates consistency across customer analysis, proposal, presentation, and follow-up, and evaluates the persuasiveness, coherence, and completeness of the sales strategy.
  - Customer to Proposal Consistency: Are all customer pain points addressed in the proposal without gaps?
  - Proposal to Presentation Consistency: Are the proposal's core value points effectively reflected in the presentation?
  - Presentation to Follow-up Consistency: Does the post-presentation follow-up naturally continue the presentation flow?
  - Pricing Consistency: Do all price references across proposal, presentation, and follow-up materials match?
  - Customer Language Consistency: Do all documents consistently use the customer's business terminology?

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
    - **Customer Info**: Customer company name, industry, size, contact person
    - **Our Info**: Product/service, strengths, price range
    - **Sales Situation**: Deal stage, competitive landscape, timeline
    - **Existing Materials** (optional): Customer analysis, existing proposals, etc.
2. Create the `_workspace/` directory at the project root
3. Organize input and save as `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding phase

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Customer analysis | customer-analyst | None | `_workspace/01_customer_analysis.md` |
| 2 | Proposal writing | proposal-writer | Task 1 | `_workspace/02_proposal.md` |
| 3a | Presentation design | presenter | Tasks 1, 2 | `_workspace/03_presentation.md` |
| 3b | Follow-up planning | followup-manager | Tasks 1, 2 | `_workspace/04_followup_plan.md` |
| 4 | Sales review | sales-reviewer | Tasks 1, 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (Presentation) and 3b (Follow-up) execute **in parallel**. Both depend on Tasks 1 (Customer Analysis) and 2 (Proposal), so they start simultaneously after the proposal is complete.

**Inter-agent communication flow:**
- customer-analyst completes → sends pain points and BANT assessment to proposal-writer
- proposal-writer completes → sends value proposition and ROI to presenter; sends pricing and objections to followup-manager
- presenter completes → sends Q&A predictions to followup-manager
- sales-reviewer cross-verifies all deliverables. When RED Must Fix items are found, sends revision requests to the relevant agent → rework → re-verify (up to 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills

- **roi-calculator**: ROI/TCO/Payback formulas, value quantification framework, 3-stage presentation
- **objection-handler**: BANT+C objection classification, LAER response framework, severity assessment, negotiation strategy

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient customer info | Build a hypothesis-based profile using industry/size, tag with "HYPOTHESIS-BASED" |
| Insufficient product info | Draft using a general B2B solution framework, tag with "PRODUCT INFO NEEDED" |
| Web search failure | Proceed with general knowledge, tag with "DATA LIMITED" |
| Agent failure | Retry once → if still failing, proceed without that deliverable and note the omission in the review report |
| RED found in review | Send revision request to the relevant agent → rework → re-verify (up to 2 iterations) |
