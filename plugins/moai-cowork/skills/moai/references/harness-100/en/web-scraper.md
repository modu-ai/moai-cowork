# Web Scraper Harness (37-web-scraper)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

Web scraping system construction: a harness in which an agent team collaborates to build target analysis, crawler design, parsing, storage, and monitoring.

## Expert Roles

- **Crawler Developer — Crawler Developer**: Web crawler developer. Designs and implements efficient, reliable crawlers based on target analysis results. Handles request strategies, session management, retry logic, and proxy rotation.

- **Data Manager — Data Manager**: Data manager. Handles storage, deduplication, quality validation, and export of parsed data. Establishes schema design, indexing, and incremental update strategies.

- **Monitor Operator — Monitoring Operator**: Monitoring operator. Handles health checks, site change detection, logging, alerting, and scheduling for the scraping system. Ensures stable system operation.

- **Parser Engineer — Parsing Engineer**: Parsing engineer. Designs and implements parsing logic to accurately extract target data from crawled raw data. Handles CSS selectors, XPath, regex, and JSON parsing.

- **Target Analyst — Target Site Analyst**: Web scraping target analyst. Performs target site structure analysis, robots.txt/ToS review, tech stack analysis, anti-bot mechanism identification, and legal risk assessment.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Target site URL**: Website to scrape
    - **Target data**: What data to extract
    - **Purpose**: Intended use of collected data (analysis/monitoring/archiving)
    - **Scale**: Expected data volume, collection frequency
    - **Constraints** (optional): Tech stack limitations, budget, legal requirements
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request (see "Execution Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Inter-task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Target site analysis | analyst | None | `_workspace/01_target_analysis.md` |
| 2a | Crawler design and implementation | crawler | Task 1 | `_workspace/02_crawler_design.md` + `src/` |
| 2b | Parsing logic design and implementation | parser | Task 1 | `_workspace/03_parser_logic.md` + `src/` |
| 3 | Data storage design | data-mgr | Task 2b | `_workspace/04_data_storage.md` + `src/` |
| 4 | Monitoring configuration | monitor | Tasks 2a, 2b, 3 | `_workspace/05_monitor_config.md` + `src/` |

Tasks 2a (crawler) and 2b (parser) run **in parallel** since both depend only on Task 1 (analysis).

**Inter-agent communication flow:**
- analyst completes > passes URL patterns, anti-bot info, rate limits to crawler; data points and DOM structure to parser
- crawler completes > passes raw data format to parser; crawler health checkpoints to monitor
- parser completes > passes data schema to data-mgr; parsing metrics to monitor
- data-mgr completes > passes data quality metrics to monitor
- monitor integrates all components to finalize operations configuration

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/` and `_workspace/src/`
2. Validate cross-deliverable consistency (analysis > crawler > parser > storage > monitoring)
3. Present the final summary and execution instructions to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build a full scraping system" | **Full pipeline** | All 5 agents |
| "Analyze target site only" | **Analysis mode** | target-analyst only |
| "Build crawler only" | **Crawler mode** | target-analyst + crawler-developer |
| "Design parser only" | **Parser mode** | target-analyst + parser-engineer |
| "Monitor existing scraper" | **Monitor mode** | monitor-operator only |

**Reusing existing files**: If the user provides existing analysis results or crawler code, copy to `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Design documents |
| Code-based | `_workspace/src/` | Executable scraping code |
| Message-based | SendMessage | Key information transfer, feedback |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Target site inaccessible | Analyze via cached/archived versions; explore alternative URLs |
| robots.txt blocks all crawling | Check for public API; propose API-based approach |
| Anti-bot blocks all requests | Escalate difficulty; propose headless browser or API alternatives |
| Dynamic rendering failure | Switch to Playwright; increase timeouts |
| Agent failure | Retry once; if still failing, proceed without that deliverable |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Target site URL**: Website to scrape
    - **Target data**: What data to extract
    - **Purpose**: Intended use of collected data (analysis/monitoring/archiving)
    - **Scale**: Expected data volume, collection frequency
    - **Constraints** (optional): Tech stack limitations, budget, legal requirements
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request (see "Execution Modes" below)

### Phase 2: Team Assembly and Execution

Assemble the team and assign tasks. Inter-task dependencies are as follows:

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Target site analysis | analyst | None | `_workspace/01_target_analysis.md` |
| 2a | Crawler design and implementation | crawler | Task 1 | `_workspace/02_crawler_design.md` + `src/` |
| 2b | Parsing logic design and implementation | parser | Task 1 | `_workspace/03_parser_logic.md` + `src/` |
| 3 | Data storage design | data-mgr | Task 2b | `_workspace/04_data_storage.md` + `src/` |
| 4 | Monitoring configuration | monitor | Tasks 2a, 2b, 3 | `_workspace/05_monitor_config.md` + `src/` |

Tasks 2a (crawler) and 2b (parser) run **in parallel** since both depend only on Task 1 (analysis).

**Inter-agent communication flow:**
- analyst completes > passes URL patterns, anti-bot info, rate limits to crawler; data points and DOM structure to parser
- crawler completes > passes raw data format to parser; crawler health checkpoints to monitor
- parser completes > passes data schema to data-mgr; parsing metrics to monitor
- data-mgr completes > passes data quality metrics to monitor
- monitor integrates all components to finalize operations configuration

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/` and `_workspace/src/`
2. Validate cross-deliverable consistency (analysis > crawler > parser > storage > monitoring)
3. Present the final summary and execution instructions to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Build a full scraping system" | **Full pipeline** | All 5 agents |
| "Analyze target site only" | **Analysis mode** | target-analyst only |
| "Build crawler only" | **Crawler mode** | target-analyst + crawler-developer |
| "Design parser only" | **Parser mode** | target-analyst + parser-engineer |
| "Monitor existing scraper" | **Monitor mode** | monitor-operator only |

**Reusing existing files**: If the user provides existing analysis results or crawler code, copy to `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Design documents |
| Code-based | `_workspace/src/` | Executable scraping code |
| Message-based | SendMessage | Key information transfer, feedback |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Target site inaccessible | Analyze via cached/archived versions; explore alternative URLs |
| robots.txt blocks all crawling | Check for public API; propose API-based approach |
| Anti-bot blocks all requests | Escalate difficulty; propose headless browser or API alternatives |
| Dynamic rendering failure | Switch to Playwright; increase timeouts |
| Agent failure | Retry once; if still failing, proceed without that deliverable |

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input summary
- `01_target_analysis.md` — Target site analysis report
- `02_crawler_design.md` — Crawler design and code
- `03_parser_logic.md` — Parsing logic and code
- `04_data_storage.md` — Data storage design
- `05_monitor_config.md` — Monitoring configuration
- `src/` — Actual scraping source code

## Extension Skills

| Skill | Path | Enhanced Agent | Role |
|-------|------|---------------|------|
| selector-generator | `.claude/skills/selector-generator/skill.md` | parser-engineer | CSS/XPath selector generation, robustness scoring, change detection |
| anti-bot-analyzer | `.claude/skills/anti-bot-analyzer/skill.md` | target-analyst, crawler-developer | Anti-bot defense layer analysis, rate limit detection, legal risk assessment |
