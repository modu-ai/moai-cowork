# Pricing Strategy (50)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

Develop a pricing strategy: an agent team collaborates to produce cost analysis, competitive pricing, value-based pricing, and simulations.

## Expert Roles

- **Competitive Analyst**: Competitive pricing analysis expert. Investigates competitor pricing structures in the market and analyzes price positioning maps, feature-price comparisons, and pricing strategy patterns.
  - Competitor Price Research: Investigate pricing structures of direct and indirect competitors via web search
  - Price Positioning Map: Place competitors on a 2D map with price-value axes
  - Feature-Price Comparison: Create comparison tables with pricing aligned to equivalent features
  - Pricing Strategy Pattern Analysis: Identify competitor pricing strategies (penetration/skimming/bundle/premium)
  - Price Positioning Recommendation: Propose optimal price positioning based on market analysis

- **Cost Analyst**: Cost analysis expert. Analyzes direct and indirect costs of products/services, and calculates break-even point (BEP), margin structure, and cost-based price floor.
  - Cost Structure Analysis: Classify and calculate direct costs (COGS), indirect costs (overhead), variable costs, and fixed costs
  - BEP Calculation: Calculate the break-even point in both unit quantity and revenue terms
  - Margin Structure Design: Derive price ranges based on target margin rates
  - Cost Driver Analysis: Identify the factors with the greatest impact on costs
  - Economies of Scale Analysis: Predict unit cost changes as production/sales volume varies

- **Pricing Reviewer**: Pricing strategy reviewer (QA). Cross-validates consistency across cost, competitive, value, and simulation analyses, and evaluates the logical coherence and feasibility of the pricing strategy.
  - Cost ↔ Price Consistency: Verify that the recommended price exceeds the cost floor and achieves the target margin
  - Competitive ↔ Price Consistency: Confirm that price positioning is consistent with competitive analysis findings
  - Value ↔ Price Consistency: Ensure the price falls within the customer-perceived value and WTP range
  - Simulation Validity: Verify that assumptions are reasonable and sensitivity analysis covers key risks
  - Numerical Consistency: Cross-check that all price, cost, and margin figures match across documents

- **Pricing Simulator**: Pricing simulation expert. Designs various pricing scenarios and performs demand elasticity, P&L impact, and sensitivity analysis to derive optimal pricing strategy.
  - Scenario Design: Design conservative/baseline/aggressive pricing scenarios
  - Demand Elasticity Estimation: Estimate demand changes in response to price variations
  - P&L Impact Analysis: Calculate the impact on revenue, costs, and profit for each scenario
  - Sensitivity Analysis: Analyze profit changes based on fluctuations in key variables (price, volume, cost, conversion rate)
  - Final Pricing Strategy Recommendation: Synthesize all analyses to recommend the optimal pricing strategy

- **Value Assessor**: Value-based pricing expert. Analyzes perceived customer value (WTP, Willingness to Pay), value drivers, and derives optimal pricing by customer segment.
  - Value Driver Analysis: Identify the real reasons customers pay (value elements)
  - WTP (Willingness to Pay) Estimation: Estimate customer willingness-to-pay price ranges by segment
  - Segment-Based Pricing Strategy: Design differentiated pricing based on perceived value differences across segments
  - Value-Cost Gap Analysis: Analyze the gap between perceived customer value and cost to find profit maximization points
  - Pricing Model Design: Design billing models (subscription/usage-based/hybrid/tiered) that match value delivery methods

## Workflow

### Phase 1: Preparation (Performed directly by orchestrator)

1. Extract from user input:
    - **Product/Service Information**: Type, features, target customers
    - **Cost Data** (optional): Known cost items
    - **Competitive Information** (optional): Known competitors, prices
    - **Objectives**: Revenue targets, market share targets, margin targets
2. Create `_workspace/` directory at the project root
3. Organize the input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding Phase

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|-------------|-------------|-------------|
| 1a | Cost Analysis | cost-analyst | None | `_workspace/01_cost_analysis.md` |
| 1b | Competitive Pricing Analysis | competitive-analyst | None | `_workspace/02_competitive_pricing.md` |
| 2 | Value-Based Pricing | value-assessor | Tasks 1a, 1b | `_workspace/03_value_pricing.md` |
| 3 | Pricing Simulation | pricing-simulator | Tasks 1a, 1b, 2 | `_workspace/04_pricing_simulation.md` |
| 4 | Pricing Review | pricing-reviewer | Tasks 1a, 1b, 2, 3 | `_workspace/05_review_report.md` |

Tasks 1a (Cost) and 1b (Competitive) are **executed in parallel**. Both can start simultaneously as they have no initial dependencies.

**Inter-team Communication Flow:**
- cost-analyst completes → delivers price floor to competitive-analyst, delivers cost structure to value-assessor
- competitive-analyst completes → delivers competitive price range to value-assessor
- value-assessor completes → delivers WTP and pricing model recommendations to pricing-simulator
- pricing-simulator completes → delivers all documents to pricing-reviewer
- pricing-reviewer cross-validates all deliverables. If 🔴 Must Fix items are found, sends revision requests to the relevant agent → rework → re-validate (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all 🔴 Must Fix items from the review report have been addressed
3. Report the final summary to the user

## Deliverables


## Extension Skills

- **psm-analyzer**: Van Westendorp PSM 4 questions, intersection derivation, Gabor-Granger supplement, segment analysis
- **price-elasticity-calculator**: PED/XED formulas, optimal price derivation, scenario simulation, price increase strategy

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient cost data | Estimate based on industry benchmarks, tag as "estimates" |
| Competitor pricing undisclosed | Estimate using industry average range, tag as "undisclosed pricing" |
| Web search failure | Work from general knowledge, note "data limited" |
| Agent failure | Retry once → if still fails, proceed without that deliverable |
| 🔴 found in review | Send revision request to the relevant agent → rework → re-validate (up to 2 times) |
| Numerical contradiction found | Request numerical reconciliation from all related agents |
