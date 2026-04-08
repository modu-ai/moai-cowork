# Knowledge Base Builder (64-knowledge-base-builder)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview
An agent team harness for building organizational knowledge management systems.

## Expert Roles
- **knowledge-collector**: Knowledge Collector. Systematically extracts knowledge from diverse sources within the organization including documents, codebases, processes, and tacit knowledge, and builds an inventory.
  - Source Identification: Identify all sources where knowledge resides (documents, code, wikis, Slack, meeting notes, etc.)
  - Knowledge Extraction: Extract key knowledge items from each source
  - Knowledge Type Classification: Classify into procedural knowledge (How-to), conceptual knowledge (What/Why), and reference knowledge (Reference)
  - Gap Analysis: Identify areas of undocumented tacit knowledge
  - Priority Setting: Prioritize based on documentation urgency and usage frequency
- **maintenance-planner**: Maintenance Planner. Establishes governance models, update cycles, quality management processes, and contribution guidelines to ensure the long-term quality of the knowledge base.
  - Governance Model: Design content ownership, review processes, and approval workflows
  - Update Cycle: Set appropriate review and update cycles for each content type
  - Quality Management: Define quality standards and design regular auditing processes
  - Contribution Guidelines: Create clear guidelines for knowledge base contributors
  - Archival Strategy: Set criteria for deprecating and archiving outdated content
- **search-optimizer**: Search Optimizer. Optimizes the knowledge base for search by designing search indexes, synonym mappings, popular query optimization, and findability improvements.
  - Search Index Design: Design an efficient search index based on article metadata and content
  - Synonym Mapping: Build a synonym dictionary that maps user search terms to article terminology
  - Popular Query Optimization: Analyze frequently searched queries and optimize results for them
  - Findability Audit: Evaluate and improve whether key articles appear at the top of search results
  - Search Analytics Design: Design metrics to measure and improve search effectiveness
- **taxonomy-designer**: Taxonomy Designer. Designs the information architecture for structuring knowledge, including category systems, tag schemes, navigation structures, and search optimization.
  - Category System Design: Design a hierarchical classification structure, balancing depth and breadth
  - Tag Scheme Design: Create a flat tag system to complement the hierarchical structure with cross-cutting themes
  - Navigation Structure: Design the primary navigation, breadcrumbs, and related article links that users will follow
  - Naming Convention: Set clear, consistent naming rules for articles and categories
  - Metadata Schema: Define the metadata (author, date, tags, status, audience) that each article should carry
- **wiki-builder**: Wiki Builder. Transforms extracted knowledge items into actual wiki articles following templates and writing guidelines to build the knowledge base content.
  - Template Design: Create standardized article templates by content type (tutorial, reference, troubleshooting, etc.)
  - Article Writing: Write actual wiki articles based on the knowledge inventory
  - Writing Style Guide: Establish consistent tone, terminology usage, and formatting standards
  - Cross-linking: Create links between related articles to build a knowledge network
  - Visual Element Design: Plan diagrams, screenshots, code blocks, and other visual aids

## Workflow
### Phase 1: Preparation (Performed Directly by Orchestrator)

1. Extract from user input:
    - **Target Organization/Project**: What knowledge to manage
    - **Target Audience**: Who will use it
    - **Existing Documents** (optional): Currently available documents, codebase
    - **Platform Preference** (optional): MkDocs, Docusaurus, Notion, GitHub Wiki, etc.
2. Create the `_workspace/` directory in the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. If existing documents are available, designate them for analysis
5. Determine the **execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Knowledge Collection | knowledge-collector | None | `_workspace/01_knowledge_inventory.md` |
| 2 | Taxonomy Design | taxonomy-designer | Task 1 | `_workspace/02_taxonomy.md` |
| 3a | Wiki Page Generation | wiki-builder | Tasks 1, 2 | `_workspace/03_wiki/` |
| 3b | Search Index | search-optimizer | Tasks 1, 2 | `_workspace/04_search_index.md` (draft) |
| 4 | Search Index Finalization | search-optimizer | Task 3a | `_workspace/04_search_index.md` (final) |
| 5 | Maintenance Guide | maintenance-planner | Tasks 1, 2, 3a | `_workspace/05_maintenance_guide.md` |

Tasks 3a (wiki generation) and 3b (search index draft) are executed **in parallel**.

**Inter-agent Communication Flow:**
- knowledge-collector completes -> Delivers inventory to taxonomy-designer; delivers original content to wiki-builder
- taxonomy-designer completes -> Delivers structure and naming conventions to wiki-builder; delivers tag scheme to search-optimizer
- wiki-builder completes -> Delivers page list to search-optimizer; delivers structure info to maintenance-planner
- maintenance-planner writes guide based on all deliverables

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify no broken links or missing pages in the wiki
3. Present the final summary to the user:
    - Knowledge Inventory — `01_knowledge_inventory.md`
    - Taxonomy — `02_taxonomy.md`
    - Markdown Wiki — `03_wiki/`
    - Search Index — `04_search_index.md`
    - Maintenance Guide — `05_maintenance_guide.md`

## Deliverables


## Extension Skills
- **content-lifecycle-manager**: A specialized skill for systematizing knowledge base content lifecycle management and quality governance. Used by the maintenance-planner and wiki-builder agents when managing content update cycles, ownership, and quality scores. Automatically applied in contexts involving 'content lifecycle,' 'governance,' 'update cycle,' 'document quality,' or 'knowledge management process.' Note: CMS server operations and automation script deployment are outside the scope of this skill.
- **information-architecture**: A specialized skill for designing the information architecture (IA) of knowledge bases. Used by the taxonomy-designer agent when designing classification systems, navigation, and labeling systems. Automatically applied in contexts involving 'information architecture,' 'IA design,' 'category design,' 'navigation,' 'sitemap,' or 'card sorting.' Note: UX research execution and UI prototyping are outside the scope of this skill.
- **knowledge-base-builder**: A pipeline where an agent team builds organizational knowledge management systems. Use this skill for requests such as 'build a knowledge base,' 'wiki setup,' 'knowledge management system,' 'internal wiki,' 'organize team documentation,' 'technical documentation wiki,' 'create onboarding docs,' 'organize organizational knowledge,' or 'build documentation system.' Note: CMS server setup, database installation, and search engine deployment are outside the scope of this skill.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Source inaccessible | Infer knowledge based on user description; mark as "inference-based" |
| Excessive knowledge scope | Propose MVP scope; take a phased approach based on priorities |
| Existing taxonomy conflict | Respect existing structure while presenting improvement proposals in parallel |
| Agent failure | Retry once; if still failing, proceed without that deliverable; note omission in report |
| Wiki platform unspecified | Default to pure Markdown (GitHub/MkDocs compatible) |
