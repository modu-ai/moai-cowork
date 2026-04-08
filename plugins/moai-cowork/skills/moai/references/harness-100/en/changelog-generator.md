# Changelog Generator Harness (39-changelog-generator)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

Changelog generation: a harness where an agent team collaborates to perform commit analysis → change classification → release note writing → migration guide → announcement.

## Expert Roles

- **Announcement Writer — Release Announcement Specialist**: Announcement writer. Crafts release information into formats suitable for various channels including blog posts, social media posts, and email newsletters.

- **Change Classifier — Software Change Classification Specialist**: Change classifier. Groups all changes into semantic units based on commit analysis results and classifies them by user impact level.

- **Commit Analyst — Git History Analyst**: Commit analyst. Analyzes git history to extract all changes between two versions. Examines commit messages, PRs, branch strategies, and contributor information.

- **Migration Guide Writer — Migration Guide Specialist**: Migration guide writer. Creates detailed upgrade guides for Breaking Changes. Provides code transformation examples, step-by-step procedures, and compatibility matrices.

- **Release Note Writer — Release Note Specialist**: Release note writer. Creates user-friendly release notes based on change classification results. Supports CHANGELOG.md and GitHub Release formats.

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Version range**: Previous version tag ~ current commit/tag
    - **Project information**: Project name, repository URL, language/framework
    - **Release type**: Regular/hotfix/pre-release
    - **Announcement channels**: Which channels are needed among blog/social media/email/Slack
    - **Existing CHANGELOG** (optional): Existing CHANGELOG.md to follow its format
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Verify the git repository and finalize the version range
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Commit analysis | analyst | None | `_workspace/01_commit_analysis.md` |
| 2 | Change classification | classifier | Task 1 | `_workspace/02_change_classification.md` |
| 3a | Release notes | note-writer | Task 2 | `_workspace/03_release_notes.md` |
| 3b | Migration guide | migration-writer | Task 2 | `_workspace/04_migration_guide.md` |
| 4 | Announcement | announcement | Tasks 3a, 3b | `_workspace/05_announcement.md` |

Tasks 3a (release notes) and 3b (migration guide) run **in parallel**.

**Inter-agent communication flow:**
- analyst completes > passes commit list and diffs to classifier
- classifier completes > passes classification results to note-writer, passes Breaking Changes details to migration-writer
- note-writer completes > passes highlights and version number to announcement
- migration-writer completes > passes migration key summary to announcement, passes guide link to note-writer

### Phase 3: Integration and Final Deliverables

1. Verify version number consistency across all deliverables
2. Validate that Breaking Change information is consistent across release notes, migration guide, and announcements
3. If an existing CHANGELOG.md exists, add the new version at the top
4. Report the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Full release prep", "changelog + announcement" | **Full pipeline** | All 5 agents |
| "Just create a CHANGELOG" | **Notes mode** | analyst + classifier + note-writer |
| "Migration guide only" | **Migration mode** | analyst + classifier + migration-writer |
| "Just write the release announcement" (notes complete) | **Announcement mode** | announcement only |
| "Classify these commits" | **Classification mode** | analyst + classifier |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time key information transfer |
| Git commands | bash execution | Extract commit logs, diffs, tag information |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No git repository | Request user to directly input commit list/change history |
| No tags | Substitute with most recent N commits or date range |
| Conventional Commits not used | LLM-based classification from commit messages + diffs |
| No Breaking Changes | migration-writer produces only a "not required" confirmation document |
| Agent failure | Retry once > if still failing, proceed without that deliverable |

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **Version range**: Previous version tag ~ current commit/tag
    - **Project information**: Project name, repository URL, language/framework
    - **Release type**: Regular/hotfix/pre-release
    - **Announcement channels**: Which channels are needed among blog/social media/email/Slack
    - **Existing CHANGELOG** (optional): Existing CHANGELOG.md to follow its format
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Verify the git repository and finalize the version range
5. If pre-existing files are available, copy them to `_workspace/` and skip the corresponding phase
6. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Commit analysis | analyst | None | `_workspace/01_commit_analysis.md` |
| 2 | Change classification | classifier | Task 1 | `_workspace/02_change_classification.md` |
| 3a | Release notes | note-writer | Task 2 | `_workspace/03_release_notes.md` |
| 3b | Migration guide | migration-writer | Task 2 | `_workspace/04_migration_guide.md` |
| 4 | Announcement | announcement | Tasks 3a, 3b | `_workspace/05_announcement.md` |

Tasks 3a (release notes) and 3b (migration guide) run **in parallel**.

**Inter-agent communication flow:**
- analyst completes > passes commit list and diffs to classifier
- classifier completes > passes classification results to note-writer, passes Breaking Changes details to migration-writer
- note-writer completes > passes highlights and version number to announcement
- migration-writer completes > passes migration key summary to announcement, passes guide link to note-writer

### Phase 3: Integration and Final Deliverables

1. Verify version number consistency across all deliverables
2. Validate that Breaking Change information is consistent across release notes, migration guide, and announcements
3. If an existing CHANGELOG.md exists, add the new version at the top
4. Report the final summary to the user

## Execution Modes by Request Scope

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|----------------|
| "Full release prep", "changelog + announcement" | **Full pipeline** | All 5 agents |
| "Just create a CHANGELOG" | **Notes mode** | analyst + classifier + note-writer |
| "Migration guide only" | **Migration mode** | analyst + classifier + migration-writer |
| "Just write the release announcement" (notes complete) | **Announcement mode** | announcement only |
| "Classify these commits" | **Classification mode** | analyst + classifier |

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Store and share primary deliverables |
| Message-based | SendMessage | Real-time key information transfer |
| Git commands | bash execution | Extract commit logs, diffs, tag information |

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No git repository | Request user to directly input commit list/change history |
| No tags | Substitute with most recent N commits or date range |
| Conventional Commits not used | LLM-based classification from commit messages + diffs |
| No Breaking Changes | migration-writer produces only a "not required" confirmation document |
| Agent failure | Retry once > if still failing, proceed without that deliverable |

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and repository information
- `01_commit_analysis.md` — Commit analysis results
- `02_change_classification.md` — Change classification and semver recommendation
- `03_release_notes.md` — Release notes (changelog)
- `04_migration_guide.md` — Migration guide for breaking changes
- `05_announcement.md` — Release announcement drafts

## Extension Skills

Extension skills that enhance agent domain expertise:

| Skill | File | Target Agent | Role |
|-------|------|-------------|------|
| semver-analyzer | `.claude/skills/semver-analyzer/skill.md` | change-classifier, release-note-writer | SemVer rules, Breaking Change assessment matrix, Conventional Commits mapping |
| commit-parser | `.claude/skills/commit-parser/skill.md` | commit-analyst, change-classifier | Commit parsing regex, non-conventional commit classification, PR/issue mapping, impact scoring |
