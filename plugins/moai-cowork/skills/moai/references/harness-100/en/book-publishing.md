# Book Publishing (11)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to produce e-book publishing deliverables: manuscript editing, cover design, table of contents, metadata, and distribution setup.

## Expert Roles
- **cover-designer**: Cover designer. Designs cover concepts matching the book's genre, tone, and target audience, and produces covers using Gemini image generation. Includes typography, color, and composition.
- **manuscript-editor**: Manuscript editor. Performs structural editing (chapter organization, flow), style correction (tone unification, readability), and content consistency verification. Includes both developmental editing and line editing.
- **metadata-manager**: Metadata manager. Handles ISBN, book classification (BISAC/KDC), book descriptions, keywords, pricing, and distribution platform settings. Manages all metadata required for e-book distribution.
- **proofreader**: Proofreader. Reviews spelling, grammar, spacing, foreign word notation, number notation, punctuation, and terminology standardization. Performs precise proofreading based on language conventions.
- **publishing-reviewer**: Publishing reviewer (QA). Cross-validates consistency across manuscript, proofreading, cover, and metadata. Performs final verification of publishing spec compliance, legal requirements, and distribution readiness.

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Manuscript**: Manuscript file to edit
   - **Genre**: Business/Self-Help/Fiction/Essay/Technical
   - **Publishing Goal**: Self-publishing/Publisher submission/Internal distribution
   - **Distribution Platforms** (optional): Kyobo, Ridibooks, Amazon KDP, etc.
   - **Existing Files** (optional): Edited manuscript, cover, etc.
2. Create `_workspace/` directory and `_workspace/covers/` subdirectory
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding Phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|------------|--------------|-------------|
| 1 | Manuscript editing | manuscript-editor | None | `_workspace/01_edited_manuscript.md` |
| 2a | Proofreading | proofreader | Task 1 | `_workspace/02_proofread_report.md` |
| 2b | Cover design | cover-designer | Task 1 | `_workspace/03_cover_concept.md` |
| 3 | Metadata | metadata-manager | Tasks 1, 2a | `_workspace/04_metadata.md` |
| 4 | Publishing review | publishing-reviewer | Tasks 2a, 2b, 3 | `_workspace/05_review_report.md` |

Tasks 2a (proofreading) and 2b (cover) are **executed in parallel**. Both depend on Task 1 (editing).

**Inter-team communication flow:**
- manuscript-editor complete -> Deliver terminology list to proofreader, tone/genre/target to cover-designer, title/keywords to metadata-manager
- proofreader complete -> Deliver finalized notation to metadata-manager
- cover-designer <-> metadata-manager: Cross-confirm exact title/subtitle/author name notation
- publishing-reviewer cross-validates all deliverables. When RED Must Fix is found, request revisions from the relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Edited manuscript — `01_edited_manuscript.md`
   - Proofreading report — `02_proofread_report.md`
   - Cover concept/images — `03_cover_concept.md`
   - Metadata/distribution — `04_metadata.md`
   - Review report — `05_review_report.md`

## Deliverables
- `00_input.md` — Organized user input
- `01_edited_manuscript.md` — Edited manuscript
- `02_proofread_report.md` — Proofreading report
- `03_cover_concept.md` — Cover concept/images
- `04_metadata.md` — Metadata/distribution settings
- `05_review_report.md` — Review report

## Extension Skills
- **book-metadata-seo**: A specialized skill for the metadata-manager agent covering e-book metadata SEO. Provides BISAC/KDC classification, keyword optimization, bookstore-specific description strategies, pricing psychology, and platform-specific distribution settings. Use for 'metadata,' 'book classification,' 'keywords,' 'e-book distribution,' and similar topics.
- **cover-design-psychology**: A specialized skill for the cover-designer agent covering cover design psychology. Provides genre-specific cover conventions, typography strategy, color psychology, thumbnail testing, and AI image generation prompt design. Use for 'cover design,' 'book cover,' 'genre covers,' 'cover concept,' and similar topics.
- **developmental-editing**: A specialized skill for the manuscript-editor agent covering developmental editing. Provides manuscript structure analysis, narrative arc diagnostics, character arc design, pacing adjustment, and genre-specific editing standards. Use for 'manuscript editing,' 'structural editing,' 'narrative analysis,' 'manuscript feedback,' and similar topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No manuscript provided | Switch to "planning mode" where manuscript-editor designs ToC and chapter outlines from title/topic |
| Cover image generation failure | Proceed with text concept and prompt only, available for user retry |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| ISBN not issued | Include issuance procedure guidance, proceed normally with remaining metadata |
