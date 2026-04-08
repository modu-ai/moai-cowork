# IP Portfolio (100-ip-portfolio)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
An intellectual property portfolio management harness. An agent team collaborates to produce IP analysis, patent mapping, protection strategy, licensing strategy, and renewal scheduling.

## Expert Roles
- **Ip Analyst**: IP analyst. Assesses the organization's intellectual property portfolio, evaluates IP asset value, and creates strategic portfolio maps.
  - IP Status Assessment: Create a complete inventory of patents, trademarks, designs, copyrights, and trade secrets
  - Value Assessment: Evaluate the business, legal, and strategic value of each IP asset both qualitatively and quantitatively
  - Portfolio Map: Visualize IP distribution by technology domain, market, and lifecycle stage
  - Competitive IP Analysis: Research competitor IP holdings and conduct patent landscape analysis
  - Gap Analysis: Identify areas requiring protection where no IP coverage currently exists
- **License Strategist**: IP license strategist. Develops IP asset monetization strategies, cross-licensing, technology transfer, and open source strategies, and designs license agreement terms.
  - Monetization Strategy: Determine optimal monetization method per IP (licensing/sale/technology transfer/commercialization)
  - Royalty Design: Design license terms including royalty rates, minimum guarantees, and upfront payments
  - Cross-Licensing: Develop mutual license strategies with competitors, review patent pool participation
  - Open Source Strategy: Assess open source license compatibility, contribution policies, and risk management
  - Technology Transfer: Define technology transfer terms with universities/research institutions, joint research IP allocation
- **Patent Mapper**: Patent, trademark, and copyright mapper. Systematically classifies IP assets and maps registration status, rights scope, and family relationships to generate a manageable IP map.
  - Patent Mapping: IPC/CPC classification, claims analysis, patent family relationships, citation networks
  - Trademark Mapping: Nice classification (designated goods/services), usage status, similar trademark monitoring
  - Copyright Mapping: Work types, registration status, license status, digital assets
  - Design Mapping: Locarno classification, protection scope, similar designs
  - IP Relationship Diagram: Visualize connections between technology, products, markets, and IP
- **Protection Advisor**: IP protection strategy advisor. Develops infringement monitoring, defense strategies, dispute response, and protection enhancement measures, and produces a comprehensive protection strategy report.
  - Infringement Monitoring System: Design surveillance systems for patent/trademark/copyright infringement
  - Defense Strategy: Proactive IP acquisition, defensive filings, defensive publication strategies
  - Dispute Response: Cease-and-desist letters, litigation strategy, ADR (alternative dispute resolution), NPE defense
  - Trade Secret Protection: Confidentiality management framework, NDAs, access controls
  - Protection Strategy Report: Final report encompassing comprehensive protection strategy and execution plan
- **Renewal Scheduler**: IP renewal schedule manager. Manages patent annuity, trademark renewal, and design renewal deadlines, calculates costs, and supports retention/abandonment decision-making.
  - Renewal Calendar: Manage all IP asset renewal deadlines in a unified calendar
  - Cost Calculation: Estimate annuity fees, renewal fees, and agent fees on annual and multi-year bases
  - Retention/Abandonment Decision Support: Analyze IP value versus maintenance costs to support decision-making
  - Alert System Design: Pre-deadline N-month notifications, escalation criteria by tier
  - Cost Optimization: Prune unnecessary IP, optimize jurisdiction-specific maintenance strategies

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Company Information**: Company name, industry, size
    - **IP Information** (optional): IP list, registration numbers, filing status
    - **Areas of Interest** (optional): Specific technology domains, specific IP types
    - **Objectives** (optional): Monetization, enhanced protection, cost optimization, dispute preparedness
    - **Existing Materials** (optional): IP register, license agreements, dispute history
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it as `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/` and use as reference materials
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | IP Status Analysis | analyst | None | `_workspace/01_ip_analysis.md` |
| 2 | IP Asset Mapping | mapper | Task 1 | `_workspace/02_ip_map.md` |
| 3a | Renewal Schedule | scheduler | Tasks 1, 2 | `_workspace/03_renewal_schedule.md` |
| 3b | License Strategy | license | Tasks 1, 2 | `_workspace/04_license_strategy.md` |
| 4 | Protection Strategy Report | protection | Tasks 1, 2, 3a, 3b | `_workspace/05_protection_report.md` |
| 5 | Integrated Review | orchestrator | All | `_workspace/06_review_report.md` |

Tasks 3a (Renewal) and 3b (License) run **in parallel**. Both depend only on Tasks 1 and 2.

**Inter-Agent Communication Flow:**
- analyst completes -> delivers inventory and classification to mapper, ratings to scheduler, monetization candidates to license, core IP and threats to protection
- mapper completes -> delivers registration/expiration dates to scheduler, rights scope to license, claims analysis to protection
- scheduler <-> license: Cross-verify which abandonment candidates are still licensable
- protection synthesizes everything into the final protection strategy

### Phase 3: Integration and Final Deliverables

1. Verify consistency across all files in `_workspace/`
2. Detect discrepancies across valuation, renewal strategy, licensing, and protection
3. Generate the integrated review report
4. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — IP portfolio information and analysis scope
- `01_ip_analysis.md` — IP portfolio analysis report
- `02_patent_map.md` — Patent mapping report
- `03_protection_strategy.md` — Protection strategy
- `04_licensing_strategy.md` — Licensing strategy
- `05_renewal_schedule.md` — Renewal schedule and cost plan
- `06_ip_summary.md` — IP portfolio summary report

## Extension Skills
- **Ip Landscape Analysis**: IP landscape analysis guide. Referenced by the patent-mapper and protection-advisor agents when analyzing technology-specific patent landscapes and developing strategies. Use for 'IP landscape', 'patent map', or 'technology trends' requests. Patent filing services and patent search database access are out of scope.
- **Patent Valuation**: Patent valuation framework. Referenced by the ip-analyst and license-strategist agents when calculating the economic value of IP assets. Use for 'patent value', 'IP valuation', or 'royalty calculation' requests. Legal patent infringement assessment and litigation representation are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| IP list not provided | Collect via company name search on public KIPRIS/USPTO databases |
| Web search failure | Work with user-provided information only, note "Data limitations" |
| Foreign IP information unavailable | Prioritize domestic IP analysis, tag with "Foreign verification needed" |
| Agent failure | Retry once -> if still fails, proceed without that deliverable |
| Valuation-protection strategy mismatch | Detected in cross-validation -> request corrections (up to 2 rounds) |
