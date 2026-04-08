# Text Processor Harness (33-text-processor)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

Text processing pipeline: a harness in which an agent team collaborates to transform bulk text into summaries, classifications, entity extractions, and sentiment analyses, producing structured data and reports.

## Expert Roles

- **Classifier — Text Classification Engine**: Text classification engine. Performs topic classification, intent classification, multi-label tagging, and document type identification. Automatically designs classification taxonomies or applies user-defined schemes.

- **Extractor — Information Extraction Specialist**: Information extraction specialist. Performs named entity recognition (NER), keyword extraction, relation extraction, and automatic summarization to extract structured information from unstructured text.

- **Preprocessor — Text Preprocessing Specialist**: Text preprocessing specialist. Performs noise removal, tokenization, normalization, language detection, sentence segmentation, and encoding handling on raw text to prepare it for downstream NLP tasks.

- **Report Writer — Text Processing Report Specialist**: Text processing report writing specialist. Integrates preprocessing, classification, extraction, and sentiment analysis results to produce a final report centered on actionable business insights.

- **Sentiment Analyzer — Sentiment Analysis Specialist**: Sentiment analysis specialist. Performs polarity analysis (positive/negative/neutral), emotion classification (joy/anger/sadness, etc.), aspect-based sentiment analysis (by product feature), and opinion mining.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Text source**: File path, format, document count, language
    - **Analysis objective**: What the user wants to learn (classification, sentiment, keywords, etc.)
    - **Domain information** (optional): Industry, text type (reviews/news/social media/documents)
    - **Classification taxonomy** (optional): User-defined classification categories
2. Create the `_workspace/` directory and the `_workspace/structured_data/` subdirectory
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Preprocessing | preprocessor | None | `01_preprocessing_result.md` |
| 2a | Classification | classifier | Task 1 | `02_classification_result.md` |
| 2b | Extraction | extractor | Task 1 | `03_extraction_result.md` |
| 3 | Sentiment analysis | sentiment-analyzer | Tasks 1, 2a, 2b | `04_sentiment_result.md` |
| 4 | Report | report-writer | Tasks 2a, 2b, 3 | `05_final_report.md` |

Tasks 2a (classification) and 2b (extraction) run **in parallel**. Sentiment analysis leverages classification and extraction results to improve aspect-level analysis accuracy.

**Inter-agent communication flow:**
- preprocessor completes > passes cleaned text and metadata to classifier, extractor, and sentiment-analyzer
- classifier completes > passes topic classification results to extractor (for topic-specific extraction) and sentiment-analyzer
- extractor completes > passes entity lists to sentiment-analyzer (for entity-level sentiment analysis)
- sentiment-analyzer completes > passes results to report-writer
- report-writer cross-validates all deliverables; requests corrections from the relevant agent if discrepancies are found (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/` and the `structured_data/` directory
2. Confirm that all required corrections have been incorporated into the report
3. Present the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Analyze this text", "full pipeline" | **Full pipeline** | All 5 agents |
| "Just classify", "categorize" | **Classification mode** | preprocessor + classifier |
| "Sentiment analysis only", "review sentiment" | **Sentiment mode** | preprocessor + sentiment-analyzer |
| "Extract keywords", "named entity recognition" | **Extraction mode** | preprocessor + extractor |
| "Summarize", "text summary" | **Summary mode** | preprocessor + extractor (summary function) |
| "Write a report" (existing analyses available) | **Report mode** | report-writer only |

**Reusing existing files**: If the user provides pre-processed text or existing classification results, copy those files to the appropriate location in `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Markdown deliverables |
| Structured data | `_workspace/structured_data/` | JSON/CSV data for programmatic use |
| Message-based | SendMessage | Key information transfer, correction requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Encoding errors | Auto-detect with chardet > force UTF-8 conversion, log losses |
| Large text volumes (>100K documents) | Batch processing; analyze a sample first, then apply to full dataset |
| Mixed languages | Separate into language-specific segments and process individually |
| NER domain mismatch | Supplement with pattern-based extraction; propose custom dictionary creation |
| Agent failure | Retry once; if still failing, proceed without that deliverable |
| Report discrepancy found | Request correction from the relevant agent (up to 2 rounds) |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Text source**: File path, format, document count, language
    - **Analysis objective**: What the user wants to learn (classification, sentiment, keywords, etc.)
    - **Domain information** (optional): Industry, text type (reviews/news/social media/documents)
    - **Classification taxonomy** (optional): User-defined classification categories
2. Create the `_workspace/` directory and the `_workspace/structured_data/` subdirectory
3. Organize the input and save it to `_workspace/00_input.md`
4. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Preprocessing | preprocessor | None | `01_preprocessing_result.md` |
| 2a | Classification | classifier | Task 1 | `02_classification_result.md` |
| 2b | Extraction | extractor | Task 1 | `03_extraction_result.md` |
| 3 | Sentiment analysis | sentiment-analyzer | Tasks 1, 2a, 2b | `04_sentiment_result.md` |
| 4 | Report | report-writer | Tasks 2a, 2b, 3 | `05_final_report.md` |

Tasks 2a (classification) and 2b (extraction) run **in parallel**. Sentiment analysis leverages classification and extraction results to improve aspect-level analysis accuracy.

**Inter-agent communication flow:**
- preprocessor completes > passes cleaned text and metadata to classifier, extractor, and sentiment-analyzer
- classifier completes > passes topic classification results to extractor (for topic-specific extraction) and sentiment-analyzer
- extractor completes > passes entity lists to sentiment-analyzer (for entity-level sentiment analysis)
- sentiment-analyzer completes > passes results to report-writer
- report-writer cross-validates all deliverables; requests corrections from the relevant agent if discrepancies are found (up to 2 rounds)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/` and the `structured_data/` directory
2. Confirm that all required corrections have been incorporated into the report
3. Present the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Analyze this text", "full pipeline" | **Full pipeline** | All 5 agents |
| "Just classify", "categorize" | **Classification mode** | preprocessor + classifier |
| "Sentiment analysis only", "review sentiment" | **Sentiment mode** | preprocessor + sentiment-analyzer |
| "Extract keywords", "named entity recognition" | **Extraction mode** | preprocessor + extractor |
| "Summarize", "text summary" | **Summary mode** | preprocessor + extractor (summary function) |
| "Write a report" (existing analyses available) | **Report mode** | report-writer only |

**Reusing existing files**: If the user provides pre-processed text or existing classification results, copy those files to the appropriate location in `_workspace/` and skip the corresponding agent.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Markdown deliverables |
| Structured data | `_workspace/structured_data/` | JSON/CSV data for programmatic use |
| Message-based | SendMessage | Key information transfer, correction requests |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Encoding errors | Auto-detect with chardet > force UTF-8 conversion, log losses |
| Large text volumes (>100K documents) | Batch processing; analyze a sample first, then apply to full dataset |
| Mixed languages | Separate into language-specific segments and process individually |
| NER domain mismatch | Supplement with pattern-based extraction; propose custom dictionary creation |
| Agent failure | Retry once; if still failing, proceed without that deliverable |
| Report discrepancy found | Request correction from the relevant agent (up to 2 rounds) |

## Deliverables

All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — User input and text source summary
- `01_preprocessing_result.md` — Preprocessing results and text statistics
- `02_classification_result.md` — Classification results
- `03_extraction_result.md` — Extraction results (entities, keywords, summaries)
- `04_sentiment_result.md` — Sentiment analysis results
- `05_final_report.md` — Final integrated report
- `structured_data/` — JSON/CSV structured data

## Extension Skills

| Skill | Path | Enhanced Agent | Role |
|-------|------|---------------|------|
| nlp-preprocessing-toolkit | `.claude/skills/nlp-preprocessing-toolkit/skill.md` | preprocessor, extractor | Tokenization, morphological analysis, embedding selection, vectorization |
| sentiment-lexicon-builder | `.claude/skills/sentiment-lexicon-builder/skill.md` | sentiment-analyzer | Sentiment lexicon construction, ABSA, negation/intensity correction, emoji mapping |
