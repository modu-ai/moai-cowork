# Real Estate Analyst (96-real-estate-analyst)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
A real estate analysis harness. An agent team collaborates to produce market research, location analysis, profitability analysis, risk assessment, and investment reports.

## Expert Roles
- **Location Analyst**: Location analysis expert. Evaluates location competitiveness by analyzing transit access, school districts, commercial areas, amenities, development catalysts, and natural environment from multiple angles.
  - Transit Accessibility: Analyze distance to subway/metro stations and bus stops, access to major roads, and regional transit networks
  - School District Analysis: Research school assignments, academic achievement, tutoring center access, and selective school admission rates
  - Commercial District/Amenities: Analyze proximity to supermarkets, hospitals, parks, cultural facilities, and other daily conveniences
  - Development Catalysts: Research new transit lines, redevelopment/reconstruction projects, and urban development plans
  - Natural Environment/Nuisances: Check views, noise levels, air quality, and proximity to undesirable facilities
- **Market Researcher**: Real estate market research expert. Analyzes the market environment by researching macroeconomic indicators, regional real estate market trends, supply/demand analysis, price trends, and policy changes.
  - Macroeconomic Analysis: Analyze how macro indicators such as interest rates, GDP, inflation, and household debt affect the real estate market
  - Regional Market Trends: Research market data including sale prices, lease prices, transaction volume, and unsold inventory for the target area
  - Supply/Demand Analysis: Analyze new developments, expected move-ins, population inflow/outflow, and household changes
  - Price Trend Analysis: Identify price change trends and inflection points over the past 1/3/5 years
  - Policy/Regulation Analysis: Research changes in real estate taxation, mortgage regulations, redevelopment policies, and related legislation
- **Profitability Analyst**: Profitability analysis expert. Precisely analyzes financial returns of real estate investment including rental yields, capital gains, cash flow, leverage effects, IRR, and NPV.
  - Rental Yield Analysis: Calculate gross rental yield, net operating income (NOI), and Cap Rate
  - Capital Gains Analysis: Estimate expected capital gains and average annual appreciation based on historical price trends
  - Cash Flow Analysis: Calculate monthly/annual cash flow and determine the break-even point
  - Leverage Analysis: Analyze return on equity (ROE) changes and leverage effects when using debt financing
  - Investment Return Metrics: Calculate IRR (Internal Rate of Return), NPV (Net Present Value), and Payback Period
- **Report Writer**: Investment report writing expert. Synthesizes market research, location analysis, profitability, and risk analysis results to produce reports with investment opinions, scenario-based return comparisons, and final investment recommendations.
  - Integrated Analysis: Combine market, location, profitability, and risk analyses into a coherent narrative
  - Investment Opinion: Present a Buy/Hold/Avoid investment opinion with supporting rationale
  - Scenario Comparison: Compare investment outcomes across optimistic/neutral/pessimistic scenarios
  - Checklist: Provide a final pre-investment verification checklist
  - Executive Summary: Write a one-page summary enabling decision-makers to grasp the essentials
- **Risk Assessor**: Real estate risk assessment expert. Comprehensively evaluates regulatory, market, liquidity, structural/physical, and legal risks and develops risk response strategies.
  - Regulatory Risk: Evaluate risks from changes in mortgage regulations (LTV/DTI/DSR), taxation, reconstruction regulations, and tenant protection laws
  - Market Risk: Evaluate market risks from price declines, transaction volume drops, oversupply, and interest rate increases
  - Liquidity Risk: Analyze sale liquidity, transaction duration, and distressed sale discount rates
  - Structural/Physical Risk: Evaluate building aging, reconstruction/renovation needs, and natural disaster exposure
  - Legal Risk: Analyze title encumbrances (liens, attachments), zoning restrictions, and dispute potential

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Analysis Target**: Specific property (address, listing) or area/type
    - **Investment Objective**: Owner-occupancy / rental income / capital gains / mixed
    - **Budget**: Equity, financing plan
    - **Investment Horizon**: Short-term (1-2 years) / Medium-term (3-5 years) / Long-term (5+ years)
    - **Constraints** (optional): Specific requirements (school district, transit, area, etc.)
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Market Research | researcher | None | `_workspace/01_market_research.md` |
| 1b | Location Analysis | location | None | `_workspace/02_location_analysis.md` |
| 2 | Profitability Analysis | profitability | Tasks 1a, 1b | `_workspace/03_profitability_analysis.md` |
| 3 | Risk Assessment | risk | Tasks 1a, 1b, 2 | `_workspace/04_risk_assessment.md` |
| 4 | Investment Report | writer | Tasks 1a, 1b, 2, 3 | `_workspace/05_investment_report.md` |

Tasks 1a (Market Research) and 1b (Location Analysis) run **in parallel**.

**Inter-Agent Communication Flow:**
- researcher + location complete in parallel -> deliver price, interest rate, and location data to profitability
- researcher -> deliver policy and market risk data to risk
- location -> deliver development catalyst uncertainties and environmental risks to risk
- profitability completes -> deliver leverage and cash flow risk data to risk
- risk completes -> deliver overall risk rating and stress test results to writer
- writer synthesizes all results into the investment report

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Cross-validation:
    - [ ] Do the market research price data and the profitability analysis purchase price match?
    - [ ] Is the location score accurately reflected in the report?
    - [ ] Do the risk assessment scenarios align with the profitability analysis scenarios?
    - [ ] Is the investment opinion supported by the analysis results?
3. If discrepancies are found, request corrections from the relevant agent (up to 2 times)
4. Present the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Analysis target and investment conditions
- `01_market_research.md` — Market research report
- `02_location_analysis.md` — Location analysis report
- `03_profitability_analysis.md` — Profitability analysis report
- `04_risk_assessment.md` — Risk assessment report
- `05_investment_report.md` — Comprehensive investment report

## Extension Skills
- **Cap Rate Calculator**: Real estate yield calculator. Reference formulas and models used by the profitability-analyst agent for quantitative investment return analysis. Use for requests involving 'Cap Rate', 'yield analysis', 'DCF', or 'cash flow analysis'. Tax advisory and loan underwriting are out of scope.
- **Location Scoring**: Location scoring scorecard. Referenced by the location-analyst agent for systematic real estate location evaluation. Use for requests involving 'location analysis', 'location assessment', or 'commercial area analysis'. On-site inspections and surveying are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Market data retrieval failure | Work with most recent available data, note the reference date |
| Insufficient property details | Analyze using regional averages, request property specifics from user |
| Tax/legal judgment required | Note "Professional consultation recommended", estimate using standard criteria |
| Unable to form investment opinion | Issue "Hold (additional data needed)" opinion, list required data |
| Agent failure | Retry once -> if still fails, proceed without that deliverable, note in report |
