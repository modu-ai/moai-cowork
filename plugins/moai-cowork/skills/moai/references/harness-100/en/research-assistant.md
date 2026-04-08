# Research Assistant (63-research-assistant)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
An agent team harness for academic research assistance.

## Expert Roles
- **critic-synthesizer**: Critical Analysis and Synthesis Specialist. Critically analyzes collected literature, identifies research gaps, and constructs the core narrative of the literature review through thematic synthesis.
  - Critical Evaluation: Assess each study's methodological rigor, logical consistency, and generalizability
  - Thematic Synthesis: Identify and organize key themes, patterns, and trends that run through the literature
  - Research Gap Identification: Identify unexplored areas, contradictory findings, and unresolved questions in existing research
  - Theoretical Framework Analysis: Compare major theoretical perspectives and evaluate their applicability to the research topic
  - Synthesis Narrative Construction: Design the logical flow and storyline of the literature review
- **literature-searcher**: Literature Search Specialist. Systematically explores academic databases and the web to collect papers, books, and reports related to the research topic, and evaluates their relevance.
  - Search Strategy Development: Derive core keywords, synonyms, and related terms from the research question
  - Database Exploration: Search Google Scholar, arXiv, PubMed, SSRN, and others via web search
  - Snowballing: Track backward references and forward citations from key papers
  - Relevance Filtering: Evaluate relevance based on abstracts and apply inclusion/exclusion criteria
  - Literature Map Generation: Classify literature by sub-topic within the research area
- **note-taker**: Note-Taking Specialist. Reads each piece of literature thoroughly and organizes key arguments, methodology, major findings, and quotable passages into a structured format.
  - Core Summary: Summarize each source's research question, methodology, key findings, and conclusions
  - Quote Extraction: Extract key passages worth direct citation along with page numbers
  - Methodology Analysis: Document the strengths and limitations of the research design, data collection, and analysis methods
  - Connection Identification: Tag commonalities, contradictions, and developmental relationships between sources
  - Research Question Linkage: Specify how each source contributes to the user's research question
- **reference-manager**: Reference Management Specialist. Accurately manages bibliographic information for all cited sources, converts to requested citation formats (APA, MLA, Chicago, etc.), and verifies duplicates and omissions.
  - Bibliographic Information Collection: Accurately record each source's author, year, title, source, DOI, and URL
  - Citation Format Conversion: Convert to requested formats such as APA 7th, MLA 9th, Chicago, Harvard, and IEEE
  - In-text Citation Generation: Generate in-text citation formats (author-year, footnotes, etc.) for use in the body text
  - Duplicate/Omission Verification: Cross-verify consistency between the reference list and in-text citations
  - BibTeX/RIS Generation: Support export to formats compatible with reference management software
- **research-coordinator**: Research Coordinator (QA). Cross-verifies consistency across literature search, notes, critical analysis, and references, confirms research quality standards are met, and produces the final report.
  - Search Comprehensiveness Verification: Confirm that the literature search is sufficiently comprehensive and no key sources are missing
  - Note-Synthesis Consistency: Verify that reading note content is accurately reflected in the synthesis analysis
  - Citation Accuracy Verification: Cross-verify between in-text citations and the reference list
  - Logical Consistency: Evaluate the logical flow and adequacy of evidence in the synthesis narrative
  - Final Report Writing: Summarize the entire research assistance process and suggest follow-up actions

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Research Topic/Question**: What to investigate
    - **Research Purpose** (optional): Paper writing, presentation, report, etc.
    - **Citation Format** (optional): APA, MLA, Chicago, etc. (default: APA 7th)
    - **Scope Limitations** (optional): Time period, language, field, number of sources
    - **Existing Materials** (optional): Already collected papers, notes
2. Create the `_workspace/` directory in the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If existing materials are provided, copy them to `_workspace/` and skip the relevant phase
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Literature Search | literature-searcher | None | `_workspace/01_literature_search.md` |
| 2a | Reading Notes | note-taker | Task 1 | `_workspace/02_reading_notes.md` |
| 2b | Draft Bibliography | reference-manager | Task 1 | `_workspace/04_bibliography.md` (draft) |
| 3 | Critical Synthesis | critic-synthesizer | Task 2a | `_workspace/03_critical_synthesis.md` |
| 4 | Final Bibliography | reference-manager | Task 3 | `_workspace/04_bibliography.md` (final) |
| 5 | Research Coordination | research-coordinator | Tasks 2a, 3, 4 | `_workspace/05_research_summary.md` |

Tasks 2a (notes) and 2b (draft bibliography) are executed **in parallel**.

**Inter-agent Communication Flow:**
- literature-searcher completes -> Delivers source list and priorities to note-taker; delivers bibliographic info to reference-manager
- note-taker completes -> Delivers notes and connections to critic-synthesizer
- critic-synthesizer completes -> Delivers citation list to reference-manager
- research-coordinator cross-verifies all deliverables. When RED issues are found, sends correction requests to the relevant agent -> rework -> re-verification (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Confirm all RED items from the research coordination report have been addressed
3. Present the final summary to the user:
    - Literature Search Results — `01_literature_search.md`
    - Reading Notes — `02_reading_notes.md`
    - Critical Synthesis — `03_critical_synthesis.md`
    - Bibliography — `04_bibliography.md`
    - Research Report — `05_research_summary.md`

## Deliverables


## Extension Skills
- **citation-formatter**: A specialized skill for accurately converting academic citations and references across major styles including APA, MLA, and Chicago. Used by the reference-manager agent when collecting bibliographic information and standardizing formats. Automatically applied in contexts involving 'citation format,' 'APA,' 'MLA,' 'Chicago,' 'references,' 'BibTeX,' or 'bibliography management.' Note: automatic bibliographic extraction from academic databases and Zotero/EndNote software operation are outside the scope of this skill.
- **research-assistant**: A pipeline where an agent team systematically performs academic research assistance. Use this skill for requests such as 'search for papers,' 'literature review,' 'organize research materials,' 'academic research,' 'organize references,' 'prior research analysis,' 'research trend analysis,' 'literature search,' or 'academic note organization.' Note: experiment execution, statistical analysis execution, final paper writing, and journal submission are outside the scope of this skill.
- **systematic-review-protocol**: A specialized skill providing PRISMA protocols and literature search strategies for systematic reviews. Used by the literature-searcher and critic-synthesizer agents when systematically searching, screening, and synthesizing academic literature. Automatically applied in contexts involving 'systematic review,' 'PRISMA,' 'literature search strategy,' 'inclusion/exclusion criteria,' or 'Boolean search.' Note: direct access to academic databases (Scopus, WoS) and meta-analysis statistical execution are outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Web search failure | Recommend based on known major journals and authors; note "search limitations" |
| Full text inaccessible | Work based on abstracts; mark "full text unverified" |
| Insufficient sources | Expand search to adjacent fields; label as "preliminary synthesis" |
| Agent failure | Retry once; if still failing, proceed without that deliverable; note omission in report |
| Citation format unknown | Apply APA 7th as default; request confirmation from the user |
