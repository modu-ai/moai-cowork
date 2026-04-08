# Market Research (44)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

Market research: a harness where an agent team collaborates to perform industry analysis → competitor analysis → consumer analysis → trend analysis → research review.

## Expert Roles

- **Competitor Analyst**: Competitive analyst. Performs competitor mapping, strategic group analysis, SWOT analysis, positioning map creation, and competitive advantage identification.
  - Competitor Mapping: Identify and categorize direct, indirect, and potential competitors
  - Strategic Group Analysis: Group competitors by strategy and identify strategic positioning
  - SWOT Analysis: Evaluate strengths, weaknesses, opportunities, and threats for key competitors
  - Positioning Map: Create 2x2 positioning maps on key competitive dimensions
  - Competitive Advantage: Identify sources of sustainable competitive advantage (moat)

- **Consumer Analyst**: Consumer analyst. Performs customer segmentation, purchase journey mapping, needs analysis, persona design, and research methodology proposals.
  - Customer Segmentation: Segment customers by demographics, psychographics, and behavior
  - Purchase Journey Mapping: Map the end-to-end customer decision and purchase journey
  - Needs Analysis: Identify unmet needs, pain points, and jobs-to-be-done
  - Persona Design: Create detailed customer personas based on research insights
  - Research Methodology: Propose appropriate research methods (surveys, interviews, ethnography, etc.)

- **Industry Analyst**: Industry analyst. Performs market size and growth rate estimation, value chain analysis, industry structure (Porter's 5 Forces), and regulatory environment analysis.
  - Market Size and Growth: Estimate current market size, CAGR, and growth drivers/inhibitors
  - Value Chain Analysis: Map the industry value chain, identify high-margin segments
  - Industry Structure: Porter's 5 Forces analysis for competitive dynamics
  - Regulatory Environment: Identify key regulations, compliance requirements, and policy trends
  - Market Segmentation: Break down the market by product, geography, customer type, etc.

- **Research Reviewer**: Research reviewer (QA). Cross-validates consistency across industry, competitive, consumer, and trend analyses. Integrates insights and derives strategic recommendations.
  - Cross-Analysis Consistency: Verify data and conclusions are consistent across all four analysis areas
  - Insight Synthesis: Identify cross-cutting themes and integrated insights not visible in individual analyses
  - Strategic Recommendations: Derive actionable strategic recommendations from the combined research
  - Data Quality Verification: Check source credibility, methodology soundness, and logical reasoning
  - Gap Identification: Identify areas requiring additional research or data

- **Trend Analyst**: Trend analyst. Performs macro environment (PESTLE), micro trend, technology trend, scenario analysis, and future outlook assessments.
  - PESTLE Analysis: Political, Economic, Social, Technological, Legal, Environmental macro environment assessment
  - Micro Trends: Industry-specific emerging trends, consumer behavior shifts
  - Technology Trends: Emerging technologies, adoption curves, disruption potential
  - Scenario Analysis: Multiple future scenarios (optimistic, base, pessimistic) with implications
  - Future Outlook: 3-5 year industry outlook with key inflection points

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Research objective**: What business decision will this inform?
    - **Industry/Market**: Target industry, geography, market segment
    - **Existing data** (optional): Prior research, internal data
    - **Deliverable focus**: Full research or specific analysis area
2. Create `_workspace/` directory and save input to `_workspace/00_input.md`
3. Determine execution mode based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Industry analysis | industry-analyst | None | `_workspace/01_industry_analysis.md` |
| 1b | Competitor analysis | competitor-analyst | None | `_workspace/02_competitor_analysis.md` |
| 2a | Consumer analysis | consumer-analyst | Tasks 1a, 1b | `_workspace/03_consumer_analysis.md` |
| 2b | Trend analysis | trend-analyst | Tasks 1a, 1b | `_workspace/04_trend_analysis.md` |
| 3 | Research review | research-reviewer | Tasks 2a, 2b | `_workspace/05_research_report.md` |

Tasks 1a and 1b run in parallel. Tasks 2a and 2b run in parallel.

### Phase 3: Integration and Final Deliverables

1. Verify all files, confirm CRITICAL findings addressed
2. Report final summary to user

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and research scope
- `01_industry_analysis.md` — Industry analysis report
- `02_competitor_analysis.md` — Competitor analysis report
- `03_consumer_analysis.md` — Consumer analysis report
- `04_trend_analysis.md` — Trend analysis report
- `05_research_summary.md` — Integrated research summary and recommendations

## Extension Skills

- **tam-sam-som-calculator**: Market sizing methodology
- **porter-five-forces**: Industry structure analysis framework

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Industry not specified | Request clarification or propose 3 related industries |
| Insufficient data | Use analogous markets, clearly note assumptions |
| Agent failure | Retry once > proceed without that deliverable |
