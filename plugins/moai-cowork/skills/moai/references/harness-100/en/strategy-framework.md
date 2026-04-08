# Strategy Framework (47)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to generate an organizational strategy framework in sequence: OKR Design, BSC Mapping, SWOT Analysis, Vision & Mission Statement, and Strategy Execution Roadmap.

## Expert Roles

- **BSC Analyst**: BSC (Balanced Scorecard) Analyst. Maps the OKR system across the four perspectives — Financial, Customer, Internal Process, and Learning & Growth — and designs the causal relationships and strategy map.
  - Four-Perspective Mapping: Classify each KR from the OKR into Financial, Customer, Internal Process, and Learning & Growth perspectives
  - Strategy Map Design: Visually represent the causal relationships between the four perspectives
  - KPI System Design: Define lead indicators and lag indicators for each perspective
  - Balance Verification: Check that KPIs are not disproportionately concentrated in any single perspective
  - Measurement System Design: Define data sources, measurement frequency, and dashboard items

- **OKR Designer**: OKR design expert. Structures the organization's strategic direction into Objectives and Key Results, and designs alignment (cascading) between upper and lower-level OKRs.
  - Objective Derivation: Extract inspiring, qualitative goals from the organizational information provided by the user
  - Key Result Design: Define 3-5 measurable key results for each Objective
  - OKR Alignment: Design OKR cascading across company, department, and team levels
  - Cadence Setting: Recommend annual/quarterly OKR rhythms and check-in cycles
  - Quality Verification: Self-check compliance with SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)

- **Strategy Reviewer**: Strategy Framework Reviewer (QA). Cross-validates logical consistency across OKR, BSC, SWOT, vision/mission, and roadmap, and identifies strategic contradictions, gaps, and quality issues.
  - OKR-BSC Consistency: Verify that all OKR KRs are mapped to BSC perspectives with no blind spots
  - OKR-SWOT Consistency: Verify that the OKR leverages key opportunities from the SWOT and addresses threats
  - Vision-OKR Consistency: Verify that the vision and mission logically connect to the OKR Objectives
  - Roadmap-BSC Consistency: Verify that roadmap milestones are measurable through BSC KPIs
  - End-to-End Logic Flow: Comprehensively verify the logical consistency of Vision → Strategy → OKR → BSC → Execution Roadmap

- **Strategy Writer**: Strategy Document Writer. Synthesizes OKR, BSC, and SWOT results to produce the vision & mission statement and strategy execution roadmap. Finalizes strategy documents for executive reporting.
  - Vision Statement Authoring: Compress the organization's long-term aspirational future into approximately 10-20 words
  - Mission Statement Authoring: Clearly articulate the organization's reason for existence, core customers, and value proposition
  - Core Values Derivation: Define 3-5 core values that represent the organizational culture
  - Strategy Execution Roadmap: Include quarterly milestones, responsible teams, required resources, and success metrics
  - Strategy Summary Report: Summarize the entire strategy as an executive 1-pager

- **SWOT Specialist**: SWOT analysis expert. Systematically analyzes the organization's internal strengths/weaknesses and external opportunities/threats, and derives actionable strategies through the TOWS matrix.
  - Internal Environment Analysis: Analyze the organization's Strengths and Weaknesses from the perspectives of resources, capabilities, and processes
  - External Environment Analysis: Analyze Opportunities and Threats from the perspectives of market, competition, technology, and regulation
  - TOWS Matrix Development: Derive S-O (offensive), W-O (redirectional), S-T (diversification), and W-T (defensive) strategy combinations
  - Strategy Prioritization: Evaluate the impact and feasibility of each TOWS strategy to determine priority
  - OKR/BSC Alignment Verification: Confirm that derived strategies are consistent with existing OKRs and BSC

## Workflow

### Phase 1: Preparation (Performed directly by the orchestrator)

1. Extract from user input:
    - **Organization Info**: Name, industry, size, current situation
    - **Strategy Period**: Annual/3-year/5-year
    - **Existing Strategy Assets** (optional): Existing OKRs, vision & mission, analytical materials
    - **Special Requirements** (optional): Emphasis on specific frameworks, focus on certain perspectives
2. Create the `_workspace/` directory at the project root
3. Organize input and save as `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | OKR design | okr-designer | None | `_workspace/01_okr_design.md` |
| 2a | BSC mapping | bsc-analyst | Task 1 | `_workspace/02_bsc_mapping.md` |
| 2b | SWOT analysis | swot-specialist | Task 1 | `_workspace/03_swot_analysis.md` |
| 3 | Vision & Mission + Roadmap | strategy-writer | Tasks 1, 2a, 2b | `_workspace/04_vision_mission.md`, `_workspace/05_strategy_roadmap.md` |
| 4 | Strategy review | strategy-reviewer | Tasks 1, 2a, 2b, 3 | `_workspace/06_review_report.md` |

Tasks 2a (BSC) and 2b (SWOT) execute **in parallel**. Both depend only on Task 1 (OKR), so they can start simultaneously.

**Inter-agent communication flow:**
- okr-designer completes → sends OKR system to bsc-analyst; sends strategic assumptions to swot-specialist
- bsc-analyst completes → sends strategic blind spots to swot-specialist; sends KPI system to strategy-writer
- swot-specialist completes → sends TOWS strategy priorities to strategy-writer
- strategy-writer completes → sends all documents to strategy-reviewer
- strategy-reviewer cross-verifies all deliverables. When RED Must Fix items are found, sends revision requests to the relevant agent → rework → re-verify (up to 2 iterations)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
    - OKR Design Document — `01_okr_design.md`
    - BSC Mapping Table — `02_bsc_mapping.md`
    - SWOT Analysis Report — `03_swot_analysis.md`
    - Vision & Mission Statement — `04_vision_mission.md`
    - Strategy Execution Roadmap — `05_strategy_roadmap.md`
    - Review Report — `06_review_report.md`

## Deliverables


## Extension Skills

- **okr-quality-checker**: QSIM/SMART-V criteria, OKR structure verification, scoring system, anti-patterns
- **tows-matrix-builder**: TOWS matrix structure, SO/WO/ST/WT strategy derivation guide, priority evaluation

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Insufficient organization info | Design hypothesis-based OKR using industry benchmarks, tag with "HYPOTHESIS-BASED" |
| Web search failure | Proceed with general knowledge, tag with "DATA LIMITED" |
| Agent failure | Retry once → if still failing, proceed without that deliverable and note the omission in the review report |
| RED found in review | Send revision request to the relevant agent → rework → re-verify (up to 2 iterations) |
| OKR-SWOT contradiction | Identify the contradiction point and coordinate between okr-designer and swot-specialist |
