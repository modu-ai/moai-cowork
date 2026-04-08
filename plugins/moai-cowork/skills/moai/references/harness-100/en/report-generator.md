# Report Generator (82-report-generator)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
work report datacollection→analysis→visualization→→summary A harness where an agent team collaborates to produce deliverables.

## Expert Roles
- **analyst**: work report analysis. collectiondone datafrom statisticsquality analysis, trend identify, comparison analysis, insight derive performto report core supporting argument composition.
  - pyeongbalanced, during, rate, point etc. core indicator calculation
  - whentotal datafrom // pattern identification
  - durationby, departmentfromby, competitorby, total pyeongbalanced versus comparison perform
  - key cause data basedas
  - "So What?" execution possibleKorean whencompanypoint present
- **data-collector**: work report data collection. report neededKorean ·nature data web search, file analysis, user provide materialfrom systematicas collectionand refinement.
  - report week data identify (data, report, companywithindocument, web material)
  - sales, KPI, marketscale, naturerate etc. figure data
  - trend, case, expert , client feedback etc. collection
  - during , day, source specify, timing perform
  - each data source etc.grade(officialstatistics/report/press coverage/estimationvalue) specify
- **executive-summarizer**: work report summary and cross-verification expert(QA). management 1degree summary writingand, data-analysis-visualization-body text between consistency cross-verification.
  - report overall 1degree within
  - collectiondone data and analysis result dayvaluedegree verify
  - chart figure analysis body text and dayvaluedegree confirm
  - data→insight→ flow Koreandegree inspection
  - proposaldone task specific possibleKoreandegree confirm
- **report-writer**: work report writingspecialist. analysis result and visualization integrationto quality persuasioncapability report . reporting target(management/actualspecialist/external) tone and structure applied.
  - reporting target and purpose document structure decision
  - analysis result qualityas beforeitems body text writing
  - visualizationexpert chart/ body text flow specialistannual
  - all argument data basis annual
  - report from specific execution task present
- **visualizer**: work report visualization expert. analysis result chart, , diagramas exchange peopletax writingand, Mermaid/ASCII chart visualization implementation.
  - data nature quality chart type decision (versus//KRW//)
  - process, , timeline Mermaid code writing
  - comparison analysis result readability composition
  - betweenKorean based chart tablecurrent
  - Excel/PowerPointfrom re-currentto do number chart peopletax provide

## Workflow
### Phase 1: preparation (Orchestrator directly perform)

1. Extract from user input:
 - **report week**: regarding reportperson
 - **reporting type**: basis(monthbetween/minutebasis/annualbetween) / project / analysis
 - **reporting target**: management / team / actualspecialist / external
 - **duration**: reporting target duration
 - **existing material** (optional): user provideKorean data, analysis result, before report
2. `_workspace/` Create the directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are provided, copy them to `_workspace/`and skip the corresponding Phase
5. Determine the **execution mode** based on the scope of the request ( "task scaleby mode" reference)

### Phase 2: team composition and execution

| order | task | responsible | dependency | deliverable |
|------|------|------|------|--------|
| 1 | data collection | collector | None | `_workspace/01_data_collection.md` |
| 2 | data analysis | analyst | task 1 | `_workspace/02_analysis_report.md` |
| 3a | visualization peopletax | visualizer | task 2 | `_workspace/03_visualization_spec.md` |
| 3b | report | writer | task 2 | `_workspace/04_full_report.md` |
| 4 | summary and verify | summarizer | task 3a, 3b | `_workspace/05_executive_summary.md` |

task 3a(visualization) and 3b ** execution**. task 2(analysis) only dependency.

**teamKRW between flow:**
- collector complete → analystto data+quality deliver, visualizerto data deliver
- analyst complete → visualizerto visualization proposal deliver, writerto insight+ beforeitems proposal deliver
- visualizer complete → writerto visualization peopletax+ position deliver
- writer complete → summarizerto report specialist deliver
- summarizer all deliverable cross-verification. 🔴 required revision findings when Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds)

### Phase 3: integration and final deliverable

1. `_workspace/` Verify all files in the directory
2. verify reportConfirm that all critical revisions from the review report have been addressed
3. Report the final summary to the user:
 - data collection — `01_data_collection.md`
 - analysis report — `02_analysis_report.md`
 - visualization peopletax — `03_visualization_spec.md`
 - final report — `04_full_report.md`
 - management summary — `05_executive_summary.md`

## Deliverables
all deliverable `_workspace/` save:
- `00_input.md` — user input organization
- `01_data_collection.md` — collectiondone data organization
- `02_analysis_report.md` — analysis result
- `03_visualization_spec.md` — visualization peopletax
- `04_full_report.md` — final report
- `05_executive_summary.md` — management summary and verify reporting

## Extension Skills
- **data-visualization-guide**: `.claude/skills/data-visualization-guide/skill.md`
- **kpi-dashboard-patterns**: `.claude/skills/kpi-dashboard-patterns/skill.md`

## Error Handling
| error type | strategy |
|----------|------|
| web search failure | collection user provide material basedas task, "external data un-secure" specify |
| data insufficient | report data scope within analysis perform, addition secure possible item specify |
| agent failure | Retry once -> proceed without that deliverable, verify report specify |
| verifyfrom 🔴 findings | Request revision from the relevant agent -> rework -> re-verify (up to 2 rounds) |
| reporting target people | management reporting (PREP structure) basicas applied |
