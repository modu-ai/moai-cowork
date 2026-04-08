# ML Experiment Harness (31-ml-experiment)

> MoAI-Cowork v0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to perform the full ML experiment lifecycle: data preparation → model design → training → evaluation → deployment.

## Expert Roles

- **Data Engineer — ML Data Engineer**: ML Data Engineer. Performs data collection, exploratory analysis (EDA), preprocessing, feature engineering, data splitting, and data version management to build optimized datasets for training.

- **Evaluation Analyst — Evaluation Analyst**: Evaluation Analyst. Analyzes model performance metrics, performs error analysis, bias verification, interpretability (XAI), deployment readiness assessment, and A/B test design.

- **Experiment Reviewer — Experiment Reviewer**: Experiment Reviewer (QA). Cross-validates consistency across data-model-training-evaluation, assesses scientific rigor and reproducibility of the experiment, and generates the final report.

- **Model Designer — Model Designer**: Model Designer. Designs ML/DL model architectures, defines hyperparameter spaces, selects loss functions, establishes regularization strategies, and implements model code.

- **Training Manager — Training Manager**: Training Manager. Handles experiment tracking (MLflow/W&B), GPU resource management, training loop implementation, checkpoint management, reproducibility assurance, and hyperparameter tuning.

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Problem Definition**: Classification/regression/generation/recommendation/time-series, etc.
    - **Data**: Data source, files, format, scale
    - **Target Metric**: Specific goals such as accuracy, F1, RMSE
    - **Constraints** (optional): Framework, GPU, inference speed, model size
    - **Existing Code** (optional): Existing models, preprocessing code, experiment results
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are present, copy to `_workspace/` and skip the corresponding Phase
5. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Data Preparation | data-engineer | None | `_workspace/01_data_preparation.md` |
| 2 | Model Design | model-designer | Task 1 | `_workspace/02_model_design.md` |
| 3 | Training Setup | training-manager | Tasks 1, 2 | `_workspace/03_training_config.md` |
| 4 | Evaluation Analysis | evaluation-analyst | Tasks 1, 2, 3 | `_workspace/04_evaluation_report.md` |
| 5 | Experiment Review | experiment-reviewer | Tasks 1-4 | `_workspace/05_review_report.md` |

**Inter-team communication flow:**
- data-engineer completes → Sends feature/shape/data characteristics to model-designer, data loader to training, class distribution to evaluation
- model-designer completes → Sends model code/hyperparameter space to training, model structure/evaluation metrics to evaluation
- training completes → Sends training curves/best model/experiment logs to evaluation
- evaluation completes → Sends evaluation report to reviewer
- reviewer cross-validates all outputs. If 🔴 must-fix issues found, sends correction requests to the relevant agent → rework → re-verify (up to 2 times)

### Phase 3: Integration and Final Outputs

1. Check all files in `_workspace/`
2. Verify that all 🔴 must-fix items from the review report have been addressed
3. Report final summary to the user:
    - Data Preparation — `01_data_preparation.md`
    - Model Design — `02_model_design.md`
    - Training Configuration — `03_training_config.md`
    - Evaluation Report — `04_evaluation_report.md`
    - Review Report — `05_review_report.md`
    - Experiment Code — `experiment_code/`

## Scale-Based Modes

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|-----------------|
| "Design the full ML experiment" | **Full Pipeline** | All 5 |
| "Preprocess the data" | **Data Mode** | data-engineer + reviewer |
| "Design the model architecture" | **Model Mode** | model-designer + reviewer |
| "Evaluate this model" (existing results) | **Evaluation Mode** | evaluation-analyst + reviewer |
| "Review this experiment" | **Review Mode** | reviewer only |

**Leveraging existing files**: If the user provides preprocessing code, trained models, etc., skip the corresponding steps.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Primary output storage and sharing |
| Code-based | `_workspace/experiment_code/` | Executable code |
| Message-based | SendMessage | Real-time key information transfer, correction requests |

File naming convention: `{order}_{agent}_{output}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Data not provided | Recommend public datasets + provide synthetic data generation code |
| No GPU | CPU-optimized settings + prioritize lightweight models |
| Problem type unclear | Infer from data characteristics + request user confirmation |
| Training divergence | Suggest LR reduction, Gradient Clipping, batch size adjustment |
| Agent failure | 1 retry → proceed without that output if failed, note omission in review report |
| 🔴 found in review | Send correction request to relevant agent → rework → re-verify (up to 2 times) |

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Problem Definition**: Classification/regression/generation/recommendation/time-series, etc.
    - **Data**: Data source, files, format, scale
    - **Target Metric**: Specific goals such as accuracy, F1, RMSE
    - **Constraints** (optional): Framework, GPU, inference speed, model size
    - **Existing Code** (optional): Existing models, preprocessing code, experiment results
2. Create `_workspace/` directory at the project root
3. Organize input and save to `_workspace/00_input.md`
4. If existing files are present, copy to `_workspace/` and skip the corresponding Phase
5. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Output |
|-------|------|-------|-------------|--------|
| 1 | Data Preparation | data-engineer | None | `_workspace/01_data_preparation.md` |
| 2 | Model Design | model-designer | Task 1 | `_workspace/02_model_design.md` |
| 3 | Training Setup | training-manager | Tasks 1, 2 | `_workspace/03_training_config.md` |
| 4 | Evaluation Analysis | evaluation-analyst | Tasks 1, 2, 3 | `_workspace/04_evaluation_report.md` |
| 5 | Experiment Review | experiment-reviewer | Tasks 1-4 | `_workspace/05_review_report.md` |

**Inter-team communication flow:**
- data-engineer completes → Sends feature/shape/data characteristics to model-designer, data loader to training, class distribution to evaluation
- model-designer completes → Sends model code/hyperparameter space to training, model structure/evaluation metrics to evaluation
- training completes → Sends training curves/best model/experiment logs to evaluation
- evaluation completes → Sends evaluation report to reviewer
- reviewer cross-validates all outputs. If 🔴 must-fix issues found, sends correction requests to the relevant agent → rework → re-verify (up to 2 times)

### Phase 3: Integration and Final Outputs

1. Check all files in `_workspace/`
2. Verify that all 🔴 must-fix items from the review report have been addressed
3. Report final summary to the user:
    - Data Preparation — `01_data_preparation.md`
    - Model Design — `02_model_design.md`
    - Training Configuration — `03_training_config.md`
    - Evaluation Report — `04_evaluation_report.md`
    - Review Report — `05_review_report.md`
    - Experiment Code — `experiment_code/`

## Scale-Based Modes

| User Request Pattern | Execution Mode | Agents Deployed |
|---------------------|---------------|-----------------|
| "Design the full ML experiment" | **Full Pipeline** | All 5 |
| "Preprocess the data" | **Data Mode** | data-engineer + reviewer |
| "Design the model architecture" | **Model Mode** | model-designer + reviewer |
| "Evaluate this model" (existing results) | **Evaluation Mode** | evaluation-analyst + reviewer |
| "Review this experiment" | **Review Mode** | reviewer only |

**Leveraging existing files**: If the user provides preprocessing code, trained models, etc., skip the corresponding steps.

## Data Transfer Protocol

| Strategy | Method | Purpose |
|----------|--------|---------|
| File-based | `_workspace/` directory | Primary output storage and sharing |
| Code-based | `_workspace/experiment_code/` | Executable code |
| Message-based | SendMessage | Real-time key information transfer, correction requests |

File naming convention: `{order}_{agent}_{output}.{extension}`

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Data not provided | Recommend public datasets + provide synthetic data generation code |
| No GPU | CPU-optimized settings + prioritize lightweight models |
| Problem type unclear | Infer from data characteristics + request user confirmation |
| Training divergence | Suggest LR reduction, Gradient Clipping, batch size adjustment |
| Agent failure | 1 retry → proceed without that output if failed, note omission in review report |
| 🔴 found in review | Send correction request to relevant agent → rework → re-verify (up to 2 times) |

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_data_preparation.md` — Data preparation plan and pipeline
- `02_model_design.md` — Model architecture design
- `03_training_config.md` — Training configuration and experiment tracking
- `04_evaluation_report.md` — Evaluation report
- `05_review_report.md` — Experiment review report
- `experiment_code/` — Experiment implementation code

## Extension Skills

| Skill | Path | Enhanced Agent | Role |
|-------|------|---------------|------|
| feature-engineering-cookbook | `.claude/skills/feature-engineering-cookbook/skill.md` | data-engineer | Numeric/categorical/time-series transformations, feature selection, data leakage prevention |
| model-selection-guide | `.claude/skills/model-selection-guide/skill.md` | model-designer, evaluation-analyst | Model recommendations by problem, hyperparameter tuning, ensembles |
| experiment-tracking-setup | `.claude/skills/experiment-tracking-setup/skill.md` | training-manager | MLflow setup, reproducibility, model registry, experiment comparison |
