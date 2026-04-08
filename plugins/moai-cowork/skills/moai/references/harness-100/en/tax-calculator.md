# Tax Calculator (75-tax-calculator)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A tax calculation agent team harness.

## Expert Roles
- **Deduction Optimizer**: Deduction Optimizer — Deduction Optimization Specialist
  - Always read the income analyst's report (`_workspace/01_income_analysis.md`) before working
  - Income deductions reduce the tax base; tax credits reduce the calculated tax — reflect this distinction accurately
  - For items exceeding deduction limits, verify whether carryover deductions are available
  - For dual-income couples, provide guidance on optimal allocation of deduction items
  - Reflect differences between year-end tax settlement and comprehensive income tax filing
  - **From Income Analyst**: Receive comprehensive income amount, tax bracket, and income type breakdown
  - **To Tax Calculation Engine**: Deliver total income deductions, total tax credits, and exemption items
  - **To Tax Savings Strategist**: Deliver remaining deduction capacity, additional deductible items, and carryover deduction information
  - Insufficient deduction documentation: Mark as "Documentation verification required" + calculate with estimated deduction amount
  - Risk of duplicate deductions: Issue a clear warning and provide guidance on correct application
  - Impact of tax law amendments: Specify the applicable tax year + notify of potential changes

- **Income Analyst**: Income Analyst — Income Analysis Specialist
  - Apply the standards of the Income Tax Act and Special Tax Treatment Control Act for the relevant year
  - Accurately separate non-taxable items by income type (meal allowances, car maintenance allowances, childbirth allowances, etc.)
  - Guide the reflection of the individual's share of four major insurance premiums as income deductions
  - Accurately determine whether multiple income sources should be aggregated for global taxation
  - Check for conversion to global taxation when financial income exceeds 20 million KRW
  - **To Deduction Optimization Specialist**: Deliver total comprehensive income, income breakdown by type, and tax bracket boundary information
  - **To Tax Calculation Engine**: Deliver tax base amount, applicable tax rates, and separately taxed items
  - **To Tax Strategy Advisor**: Deliver income structure, tax bracket boundary analysis, and income splitting possibilities
  - Insufficient income information: Analyze with provided information only, note "Additional income verification required"
  - Unclear tax year: Apply latest tax law standards, note "Attribution year verification required"
  - Complex income structure: Recommend consulting a tax accountant + provide general analysis

- **Strategy Advisor**: Strategy Advisor — Tax Savings Strategy Advisor
  - Formulate strategies based on the results of the tax calculation engine (`_workspace/03_tax_calculation.md`)
  - Advise on **legal tax savings only** — tax evasion or avoidance is never suggested
  - Always calculate tax savings in monetary amounts to aid decision-making
  - Compare a minimum of 3 scenarios in simulations
  - Evaluate implementation difficulty and risk together
  - **From Tax Calculation Engine**: Receives determined tax amount, effective tax rate, and tax bracket analysis
  - **From Deduction Optimization Specialist**: Receives unused deduction items and remaining deduction limits
  - **From Income Analyst**: Receives income structure and tax bracket boundary analysis
  - Insufficient simulation variables: Simulate within possible range; note "Additional information required"
  - Possibility of tax law revision: Note "Based on current tax law" + provide revision trend guidance
  - Complex tax savings structures: Note "Recommend consulting a tax accountant" + present only basic direction

- **Tax Engine**: Tax Engine
  - Base all calculations on the income analyst's report (`_workspace/01_income_analysis.md`) and the deduction specialist's report (`_workspace/02_deduction_optimization.md`)
  - Document every calculation step-by-step to allow verification
  - Calculate accurately to the won (including rounding rules such as truncating amounts below 10 won)
  - Separately compute and aggregate tax amounts for separately taxed income
  - Check whether any penalty taxes apply
  - **From Income Analyst**: Receive base tax amount, applicable tax rate, and separately taxed items
  - **From Deduction Optimization Specialist**: Receive total income deductions, total tax credits, and reduction items
  - **To Tax Strategy Specialist**: Deliver determined tax, effective tax rate, tax bracket boundary analysis, and refund/payable amounts
  - Input figure discrepancy: Cross-validate figures from income analyst and deduction specialist; flag any discrepancies explicitly
  - Calculation error possibility: Perform double verification on critical calculations
  - If penalty taxes apply: Provide separate guidance on non-filing, underreporting, and late-payment penalty taxes

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Income information**: Employment income (gross salary), business income, financial income, miscellaneous income
    - **Family composition**: Spouse, dependents (for personal exemptions)
    - **Deduction items** (optional): Insurance premiums, medical expenses, education costs, donations, pension savings, etc.
    - **Pre-paid tax** (optional): Withheld tax at source, interim prepayment
    - **Tax year**: Attribution year
2. Create a `_workspace/` directory in the project root
3. Organize input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends On | Output |
|------|------|------|------|--------|
| 1 | Income analysis | analyst | None | `_workspace/01_income_analysis.md` |
| 2 | Deduction optimization | optimizer | Task 1 | `_workspace/02_deduction_optimization.md` |
| 3 | Tax calculation | engine | Tasks 1, 2 | `_workspace/03_tax_calculation.md` |
| 4 | Tax strategy + filing prep | advisor | Tasks 1, 2, 3 | `_workspace/04_tax_strategy.md`, `_workspace/05_filing_preparation.md` |

This workflow is **sequential** — each step depends on the previous one.

**Inter-agent communication flow:**
- analyst completes → passes comprehensive income amount & tax bracket to optimizer, passes taxable income basis to engine
- optimizer completes → passes deduction totals to engine, passes unused deduction items to advisor
- engine completes → passes final tax amount, effective tax rate & tax bracket analysis to advisor
- advisor synthesizes all results to build tax-saving strategies + filing guide

### Phase 3: Integration and Final Outputs

1. Review all files in `_workspace/`
2. Validate consistency of calculated figures (accuracy of the income → deduction → tax chain)
3. Report final summary to user:
    - Income analysis — `01_income_analysis.md`
    - Deduction optimization — `02_deduction_optimization.md`
    - Tax calculation statement — `03_tax_calculation.md`
    - Tax-saving strategy — `04_tax_strategy.md`
    - Filing preparation — `05_filing_preparation.md`

## Deliverables

## Extension Skills
- **Deduction Optimizer Engine**: Deduction Optimizer Engine
- **Tax Bracket Simulator**: Tax Bracket Simulator

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient income information | Calculate with information provided, note "additional income verification required" |
| Unclear tax year | Apply latest tax law, note "attribution year verification required" |
| Calculated figure mismatch | Request re-validation of prior step (max 2 times) |
| Agent failure | 1 retry → if still failing, proceed without that output and note the omission in the report |
| Complex tax structure | Note "tax accountant consultation recommended" + provide basic analysis only |
