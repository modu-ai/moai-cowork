# Ecommerce Launcher (97-ecommerce-launcher)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
An e-commerce launch harness. An agent team collaborates to produce product planning, product detail pages, pricing strategy, marketing plans, and customer service architecture for online store launches.

## Expert Roles
- **Cs Architect**: E-commerce CS architect. Designs FAQ, response manuals, return/exchange policies, VOC collection systems, and escalation processes to complete CS infrastructure before launch.
  - FAQ Design: Write 20-30 anticipated pre- and post-purchase questions and answers
  - Response Manual: Situational response scripts (inquiries/complaints/exchanges/refunds/wrong shipments)
  - Return/Exchange Policy: Comply with e-commerce regulations and reflect platform-specific policy differences
  - VOC Collection System: Customer feedback classification system and escalation criteria
  - CS Quality Metrics: Set targets for response time, resolution rate, and CSAT
- **Detail Page Writer**: E-commerce detail page writer. Creates product detail page copy designed to maximize purchase conversion, based on the product planning brief. Includes headline copy, content structure, SEO, and persuasion logic.
  - Headline Copy: The first screen that stops the scroll — core benefit + emotional trigger
  - Content Structure Design: Information flow design (problem statement -> solution -> evidence -> call to action)
  - Benefit-Focused Copy: Transform specs into customer language (benefits)
  - Trust Elements: Place certification marks, test reports, review citations, and warranty policies
  - SEO Optimization: Compose text that naturally incorporates search keywords
- **Marketing Manager**: E-commerce marketing manager. Designs launch campaigns, channel-specific advertising strategies, content marketing, influencer collaborations, and performance marketing KPIs.
  - Launch Campaign Design: Launch roadmap from D-30 through D+30
  - Channel Strategy: Budget allocation across channels (Naver SA/DA, Kakao, Meta, Google, etc.)
  - Content Marketing: Blog, social media, and short-form video content planning
  - Ad Copy Creation: Produce channel-specific ad creatives (copy + visual direction)
  - KPI Setting: Define core metrics and targets for ROAS, CPA, CVR, CTR, etc.
- **Pricing Strategist**: E-commerce pricing strategist. Develops cost analysis, competitive pricing research, margin design, promotional pricing, and bundle strategies to achieve both profitability and competitiveness.
  - Cost Analysis: Calculate total cost including manufacturing cost, logistics, platform fees, advertising, and packaging
  - Competitive Pricing Research: Research actual selling prices, discount rates, and coupon strategies of competing products in the same category
  - Price Positioning: Determine optimal position on the price-quality matrix
  - Margin Design: Calculate effective margin rates reflecting channel-specific commission rates
  - Promotion Design: Design pricing promotions including launch pricing, early-bird offers, bundles, and subscription discounts
- **Product Planner**: E-commerce product planner. Conducts market research, target customer analysis, competitive benchmarking, product positioning, and USP development.
  - Market Research: Identify the market size, growth rate, and trends for the relevant category using web searches
  - Target Customer Analysis: Define the core buyer demographic, purchase motivations, and pain points
  - Competitive Benchmarking: Research 3-5 competing products in the same category and compare pricing, reviews, and strengths/weaknesses
  - Product Positioning: Determine placement on the price-quality matrix and establish differentiation points (USP)
  - Product Spec Definition: Specify key features, included components, and option/SKU structure

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Product Information**: Product name, category, key features
    - **Target Market** (optional): Target customer segment, price range
    - **Platform** (optional): Naver/Coupang/Own Store, etc.
    - **Constraints** (optional): Budget, timeline, special considerations
    - **Existing Files** (optional): Existing briefs, detail pages, etc.
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request (see "Execution Modes by Scope" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Product Planning | planner | None | `_workspace/01_product_brief.md` |
| 2a | Detail Page Writing | writer | Task 1 | `_workspace/02_detail_page.md` |
| 2b | Pricing Strategy | pricing | Task 1 | `_workspace/03_pricing_plan.md` |
| 3 | Marketing Plan | marketing | Tasks 1, 2a, 2b | `_workspace/04_marketing_plan.md` |
| 4 | CS Manual | cs | Tasks 1, 2b | `_workspace/05_cs_manual.md` |
| 5 | Integrated Review | orchestrator | All | `_workspace/06_review_report.md` |

Tasks 2a (Detail Page) and 2b (Pricing) run **in parallel**. Both depend only on Task 1 (Planning) and can start simultaneously.

**Inter-Agent Communication Flow:**
- planner completes -> delivers USP and target to writer, competitive pricing and costs to pricing, target and trends to marketing, specs and certifications to cs
- writer completes -> delivers detail page keywords to marketing, FAQ section to cs
- pricing completes -> delivers price display format to writer, promotion strategy to marketing, pricing policy to cs
- marketing completes -> delivers promotion-related anticipated inquiries to cs
- orchestrator cross-validates all deliverables and produces the review report

### Phase 3: Integration and Final Deliverables

Cross-validate all deliverables for consistency and finalize:

1. Verify all files in `_workspace/`
2. Detect inconsistencies across detail page, pricing, marketing, and CS
3. Generate the integrated review report (`_workspace/06_review_report.md`)
4. Report the final summary to the user:
    - Product Planning Brief — `01_product_brief.md`
    - Detail Page Copy — `02_detail_page.md`
    - Pricing Strategy Document — `03_pricing_plan.md`
    - Marketing Plan — `04_marketing_plan.md`
    - CS Operations Manual — `05_cs_manual.md`
    - Review Report — `06_review_report.md`

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Product information and launch conditions
- `01_product_plan.md` — Product planning document
- `02_detail_page.md` — Product detail page
- `03_pricing_strategy.md` — Pricing strategy
- `04_marketing_plan.md` — Marketing plan
- `05_cs_guide.md` — Customer service guide
- `06_launch_checklist.md` — Launch checklist

## Extension Skills
- **Conversion Optimization**: Purchase conversion optimization framework. Referenced by the detail-page-writer and pricing-strategist agents when designing detail pages and pricing with a conversion focus. Use for 'conversion rate optimization', 'CRO', or 'purchase psychology' requests. A/B testing tool setup and funnel automation are out of scope.
- **Product Copy Formulas**: Product copy formula library. Referenced by the detail-page-writer and marketing-manager agents when writing purchase-driving copy. Use for 'product copy', 'marketing copy', or 'ad copy' requests. Ad placement and design mockup creation are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Web search failure | Planner works from general knowledge, notes "Data limitations" in report |
| Cost information absent | Reverse-engineer from category-average margin rate, request user confirmation |
| Platform unspecified | Write based on Naver Smart Store standards + append multi-platform guide |
| Agent failure | Retry once -> if still fails, proceed without that deliverable, note omission in review report |
| Consistency discrepancy found | Request corrections from relevant agent -> rework (up to 2 rounds) |
