# Startup Launcher (43)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

Startup launch planning: a harness where an agent team collaborates to perform market analysis → business modeling → MVP architecture → pitch deck creation → launch review.

## Expert Roles

- **Business Modeler**: Business modeler. Creates Business Model Canvas, designs revenue models, performs unit economics analysis, and builds financial projections.
  - Business Model Canvas: Visualize the entire business structure by filling out all 9 blocks concretely
  - Revenue Model Design: Pricing approach (subscription/transaction fees/ads/freemium, etc.), pricing strategy, revenue diversification
  - Unit Economics: Calculate CAC, LTV, LTV/CAC ratio, payback period, gross margin
  - Financial Projections: 3-year revenue/cost/P&L forecast (optimistic/base/conservative scenarios)
  - Funding Requirements: Burn rate, runway, staged investment needs

- **Launch Reviewer**: Launch reviewer (QA). Cross-validates logical consistency between market analysis, business model, MVP, and pitch deck. Assesses investment readiness and execution feasibility.
  - Market <> Business Model Consistency: Does the market size support the revenue projections?
  - Business Model <> MVP Consistency: Can the MVP validate the core revenue model?
  - Overall <> Pitch Deck Consistency: Do pitch deck figures match the analysis reports?
  - Investment Readiness Assessment: Is this at a level suitable for investor meetings? (VC associate perspective)
  - Execution Feasibility: Is the proposed roadmap realistic? Have risks been identified?

- **Market Analyst**: Startup market analyst. Performs idea validation, market sizing (TAM/SAM/SOM), competitive analysis, customer persona definition, and PMF hypothesis formulation.
  - Idea Validation: Problem-Solution Fit analysis, differentiation from existing alternatives
  - Market Sizing: Top-Down (TAM > SAM > SOM) + Bottom-Up cross-validation
  - Competitive Analysis: Direct/indirect competitor mapping, positioning map, entry barrier analysis
  - Customer Persona: Define initial target customer demographics, pain points, and behavior
  - PMF Hypothesis: Propose key hypotheses to validate and validation methods (interviews, surveys, landing pages, etc.)

- **MVP Architect**: MVP architect. Performs core feature prioritization, technology stack selection, development roadmap creation, and user flow design.
  - Core Feature Prioritization: MoSCoW method or RICE scoring for feature prioritization
  - Technology Stack Selection: Select optimal stack considering development speed, cost, and scalability
  - User Flow Design: Core user journey mapping, key screen wireframes
  - Development Roadmap: Phase-by-phase development plan with milestones, timeline, and resource requirements
  - Success Metrics Definition: Define quantitative metrics to validate PMF hypothesis through the MVP

- **Pitch Creator**: Pitch deck creator. Designs investor presentation storylines, slide structures, and core narratives.
  - Storyline Design: Problem > Solution > Market > Traction > Business Model > Team > Ask narrative arc
  - Slide Structure: 10-15 slide deck following investor expectations
  - Data Visualization: Transform complex data into clear, impactful visuals for each slide
  - Investor Q&A Preparation: Anticipate key questions and prepare clear answers
  - Multiple Formats: Full deck, executive summary (2-page), elevator pitch (30 seconds)

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Startup idea**: Problem to solve, proposed solution
    - **Target market**: Industry, geography, customer segment
    - **Stage**: Idea/Validation/MVP/Growth
    - **Funding goal** (optional): Investment round, target amount
    - **Existing assets** (optional): Market research, business plan, prototype, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Market validation | market-analyst | None | `_workspace/01_market_validation.md` |
| 2 | Business model | business-modeler | Task 1 | `_workspace/02_business_model.md` |
| 3 | MVP design | mvp-architect | Task 2 | `_workspace/03_mvp_design.md` |
| 4 | Pitch deck | pitch-creator | Tasks 1, 2, 3 | `_workspace/04_pitch_deck.md` |
| 5 | Launch review | launch-reviewer | Task 4 | `_workspace/05_review_report.md` |

**Inter-agent communication flow:**
- market-analyst completes > passes market data to business-modeler, pain points to mvp-architect
- business-modeler completes > passes financials to mvp-architect and pitch-creator
- mvp-architect completes > passes MVP plan to pitch-creator
- pitch-creator completes > passes deck to launch-reviewer
- launch-reviewer cross-validates all deliverables. On CRITICAL findings, requests corrections > rework > re-verify (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all CRITICAL findings have been addressed
3. Report the final summary to the user

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and startup idea
- `01_market_analysis.md` — Market analysis report
- `02_business_model.md` — Business model and revenue plan
- `03_mvp_plan.md` — MVP architecture and development roadmap
- `04_pitch_deck.md` — Pitch deck content
- `05_launch_review.md` — Launch feasibility review report

## Extension Skills

- **unit-economics-calculator**: LTV, CAC, margin, BEP calculation methodology
- **pitch-deck-framework**: Pitch deck structure, storytelling, slide design framework

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Idea too vague | Request clarification on problem/solution/target customer |
| No market data available | Use analogous market estimation, note assumptions |
| Agent failure | Retry once > proceed without that deliverable |
| CRITICAL in review | Request correction > rework > re-verify (up to 2 rounds) |
