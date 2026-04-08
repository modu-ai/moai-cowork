# LLM App Builder (41)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview

LLM application construction: a harness where an agent team collaborates to perform prompt engineering → RAG architecture → optimization → evaluation → deployment.

## Expert Roles

- **Deploy Engineer**: LLM app deployment engineer. Configures production deployment including API server, scaling, monitoring, and guardrail runtime.
  - API Server Construction: FastAPI/Flask-based API endpoints, streaming SSE support
  - Infrastructure Configuration: Docker, Kubernetes, serverless deployment setup
  - Scaling: Autoscaling, rate limiting, queue-based request processing
  - Monitoring: LLM call logging, cost tracking, error rate, latency dashboards
  - Production Guardrails: Input/output validation, request filtering, cost ceiling configuration

- **Eval Specialist**: LLM evaluation specialist. Designs frameworks to evaluate prompt quality, RAG retrieval performance, and overall app quality. Builds benchmarks, A/B tests, and regression tests.
  - Evaluation Dataset Design: Golden sets, edge cases, adversarial inputs
  - Automated Evaluation Metrics: Implement automated evaluation for accuracy, faithfulness, relevance, consistency, etc.
  - LLM-as-Judge: Design automated quality evaluation systems using LLMs
  - RAG Retrieval Evaluation: Retrieval quality metrics including Recall@K, MRR, NDCG
  - Regression Testing: Detect quality degradation when prompts/models change

- **Optimization Engineer**: LLM app optimization engineer. Optimizes the tradeoffs between cost, latency, and quality. Handles prompt compression, caching, model routing, and batch processing.
  - Cost Optimization: Minimize token usage, leverage lower-cost models, caching strategies
  - Latency Optimization: Streaming, parallel processing, prompt compression, precomputation
  - Model Routing: Route queries to appropriate models (large/small) based on query complexity
  - Caching Strategy: Semantic caching, exact-match caching, TTL-based expiration
  - Batch Processing: Batch processing for bulk requests, queue-based async processing

- **Prompt Engineer**: Prompt engineer. Designs system prompts, few-shot examples, output formats, and guardrails for LLM apps. Ensures prompt stability and quality.
  - System Prompt Design: Role definition, behavioral guidelines, constraints, output format specification
  - Few-Shot Example Design: Input/output example pairs, edge case coverage, negative examples
  - Output Format Definition: JSON/markdown/structured text schema, ensuring parseability
  - Guardrail Design: Jailbreak prevention, harmful content filtering, hallucination reduction techniques
  - Prompt Version Management: Track prompt change history, create variants for A/B testing

- **RAG Architect**: RAG pipeline designer. Designs and implements the full RAG pipeline including document processing, chunking, embedding, vector store, retrieval, and reranking.
  - Document Preprocessing: PDF/HTML/Markdown parsing, metadata extraction, cleaning
  - Chunking Strategy: Split documents into appropriately sized chunks — semantic/fixed-size/recursive splitting
  - Embedding Pipeline: Embedding model selection, batch processing, caching
  - Vector Store: Selection and configuration of Chroma/Pinecone/Weaviate/pgvector
  - Retrieval and Reranking: Hybrid search (vector + keyword), reranking models, context compression

## Workflow

### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract the following from user input:
    - **App purpose**: What the LLM app does
    - **Data sources**: Documents/data for RAG (optional)
    - **LLM model**: Model to use (default: Claude/GPT-4o)
    - **Deployment environment**: API/web app/chatbot/internal tool
    - **Budget**: Monthly API cost budget
    - **Constraints** (optional): Security, regulatory, performance requirements
2. Create the `_workspace/` directory at the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. Create the `_workspace/src/` directory
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1a | Prompt design | prompt | None | `_workspace/01_prompt_design.md` |
| 1b | RAG pipeline | rag | None | `_workspace/02_rag_pipeline.md` + `src/` |
| 2 | Evaluation framework | eval | Tasks 1a, 1b | `_workspace/03_eval_framework.md` + `src/` |
| 3 | Optimization | optimizer | Task 2 | `_workspace/04_optimization.md` + `src/` |
| 4 | Deployment config | deploy | Tasks 1b, 3 | `_workspace/05_deploy_config.md` + `src/` |

Tasks 1a (prompt) and 1b (RAG) run **in parallel**.

**Inter-agent communication flow:**
- prompt completes > passes context injection format to rag, passes expected outputs to eval
- rag completes > passes retrieval test data to eval, passes vector DB infra requirements to deploy
- eval completes > passes performance baseline to optimizer, passes weakness feedback to prompt
- optimizer completes > passes cache/routing config to deploy
- deploy integrates all components to complete the production deployment configuration

### Phase 3: Integration and Final Deliverables

1. Verify that the code in `_workspace/src/` is executable
2. Confirm that evaluation metrics meet the standards
3. Validate that deployment configuration is complete
4. Report the final summary to the user:
    - Prompt design — `01_prompt_design.md`
    - RAG pipeline — `02_rag_pipeline.md`
    - Evaluation framework — `03_eval_framework.md`
    - Optimization strategy — `04_optimization.md`
    - Deployment config — `05_deploy_config.md`
    - Source code — `src/`

## Deliverables

All outputs are stored in the `_workspace/` directory:
- `00_input.md` — User input and application requirements
- `01_prompt_design.md` — Prompt templates and engineering document
- `02_rag_architecture.md` — RAG pipeline architecture
- `03_optimization_plan.md` — Performance optimization plan
- `04_eval_report.md` — Evaluation results and quality metrics
- `05_deploy_config/` — Deployment configuration and infrastructure
- `src/` — Application source code

## Extension Skills

- **prompt-optimizer**: CRISP rubric, RCTF template, guardrail patterns, A/B testing, token optimization
- **chunking-strategy-guide**: Chunking strategy comparison, semantic chunking algorithm, per-document preprocessing, quality metrics

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| No LLM API key | Provide environment variable setup guide, suggest local model alternatives |
| No RAG data source | Build as a pure LLM app without RAG, provide guide for adding RAG later |
| No evaluation dataset | Generate synthetic data with LLM, provide manual verification guide |
| Projected budget overrun | Suggest small model routing, enhanced caching, request limits |
| Agent failure | Retry once > if still failing, proceed without that deliverable |
