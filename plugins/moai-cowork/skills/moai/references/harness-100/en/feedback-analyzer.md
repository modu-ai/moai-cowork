# Feedback Analyzer (93-feedback-analyzer)

> MoAI-Cowork V0.1.3 Harness Reference

## Overview
A customer/employee feedback analysis harness. An agent team collaborates to handle everything from data collection through sentiment analysis, topic classification, trend detection, and insight reporting.

## Expert Roles
- **Data Collector**: Feedback data collection and cleansing expert. Integrates feedback from multiple channels (surveys, reviews, support logs, interviews), performs deduplication, normalization, and anonymization to build analysis-ready datasets.
  - Multi-channel Integration: Unify data from surveys, app reviews, support tickets, interview notes, social media mentions, and other sources into a single format
  - Data Cleansing: Remove duplicates, filter spam, and eliminate meaningless responses (blanks, "N/A," etc.)
  - Normalization: Standardize date formats, unify rating scales (5-point/10-point/100-point → 5-point), clean text encoding
  - Metadata Tagging: Tag each piece of feedback with channel, date, customer/employee classification, and product/service area
  - Basic Statistics: Calculate basic statistics including data count, channel distribution, time period distribution, and response rates
- **Insight Writer**: Insight report writing expert. Synthesizes sentiment analysis, topic classification, and trend results to produce tailored insight reports for executives and practitioners with specific action items.
  - Synthesized Insight Derivation: Cross-reference sentiment, topic, and trend analysis results to derive key insights
  - Action Item Recommendations: Propose specific, actionable items for each insight
  - Priority Matrix: Prioritize action items by impact × ease of implementation
  - Audience-specific Reports: Produce separate versions for executives (1-page summary) and practitioners (detailed report)
  - Monitoring Dashboard Design: Propose KPIs and dashboard configurations for ongoing feedback management
- **Sentiment Analyst**: Sentiment analysis expert. Determines positive/negative/neutral polarity of feedback text, scores emotional intensity, and analyzes sentiment changes over time.
  - Polarity Classification: Classify each piece of feedback as Positive/Negative/Neutral/Mixed
  - Emotion Intensity Scoring: Score on a scale from -1.0 (extremely negative) to +1.0 (extremely positive)
  - Detailed Emotion Tagging: Identify specific emotions such as satisfaction, dissatisfaction, anger, gratitude, disappointment, confusion, and anticipation
  - Sentiment Trend Tracking: Track sentiment score changes along a timeline to identify deterioration/improvement periods
  - Key Expression Extraction: Extract key phrases that reveal emotions from the original text
- **Topic Classifier**: Topic classification expert. Classifies feedback by semantic meaning, designs category systems, performs keyword clustering, tag mapping, and topic-by-sentiment cross-analysis.
  - Category System Design: Derive topic categories bottom-up from feedback content (major → mid → sub-categories)
  - Keyword Clustering: Group similar keywords and define representative keywords for each category
  - Multi-tagging: Assign multiple tags when a single piece of feedback spans several topics
  - Topic × Sentiment Cross-analysis: Analyze sentiment distribution per topic to identify problem areas
  - Tag Map Visualization: Visualize topic relationships and frequencies as Mermaid mindmaps
- **Trend Detector**: Trend analysis expert. Analyzes time-series patterns in feedback data to identify rising/falling trends, anomalies, seasonality, and event correlations.
  - Time-series Trend Analysis: Analyze topic-level and sentiment-level trends over time to identify rising/falling/stable patterns
  - Anomaly Detection: Detect unusual periods such as sudden feedback spikes or sharp sentiment score changes
  - Event Correlation: Analyze correlations between trend changes and external events (product launches, policy changes, seasons)
  - Seasonality/Cyclicality Analysis: Identify recurring patterns by day of week, month, or quarter
  - Forecasting and Alerts: Present projected direction if current trends continue and early warning signals

## Workflow
### Phase 1: Preparation (performed directly by the orchestrator)

1. Extract from user input:
    - **Feedback data**: Text files, CSV, paste, or verbal description
    - **Data source type**: Customer reviews/surveys/support logs/employee feedback/social media
    - **Analysis purpose**: Product improvement/service quality/employee satisfaction/competitive analysis
    - **Comparison baseline** (optional): Previous period, competitors, targets
    - **Existing categories** (optional): User-defined classification system
2. Create the `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. Determine the **execution mode** based on the request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Data collection/cleansing | collector | None | `_workspace/01_data_collection.md` |
| 2a | Sentiment analysis | sentiment | Task 1 | `_workspace/02_sentiment_analysis.md` |
| 2b | Topic classification | classifier | Task 1 | `_workspace/03_topic_classification.md` |
| 3 | Trend analysis | trend | Tasks 2a, 2b | `_workspace/04_trend_report.md` |
| 4 | Insight report | writer | Tasks 2a, 2b, 3 | `_workspace/05_insight_report.md` |

Tasks 2a (sentiment) and 2b (topic) run **in parallel**. Both depend only on Task 1.

**Inter-team communication flow:**
- collector completes → sends cleansed data to sentiment, dataset/keywords to classifier, distribution data to trend
- sentiment completes → sends emotion-tagged data to classifier (for cross-analysis), time-series emotion data to trend
- classifier completes → sends topic time-series to trend, categories/urgent issues to writer
- trend completes → sends key trends/anomalies/forecasts to writer
- writer synthesizes all agent results into the insight report

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Cross-validation:
    - [ ] Sentiment analysis count matches data collection count
    - [ ] Topic classification unclassified rate is 10% or below
    - [ ] Insights cite data evidence
    - [ ] Action items follow SMART principles
3. Request corrections from the relevant agent if discrepancies are found (up to 2 rounds)
4. Report the final summary to the user

## Deliverables
All outputs are saved to the `_workspace/` directory:
- `00_input.md` — Raw feedback data and analysis requirements
- `01_data_collection.md` — Data collection and cleansing results
- `02_sentiment_analysis.md` — Sentiment analysis results
- `03_topic_classification.md` — Topic classification results
- `04_trend_report.md` — Trend analysis results
- `05_insight_report.md` — Comprehensive insight report

## Extension Skills
- **Sentiment Scoring**: Sentiment analysis scoring framework. Referenced by the sentiment-analyst agent for systematic sentiment classification and scoring of text data. Used for 'sentiment analysis', 'emotion score', 'NPS analysis' requests. Note: ML model training and NLP pipeline development are out of scope.
- **Text Analytics Methods**: Text analytics methodology. Referenced by topic-classifier and trend-detector agents when extracting topics and deriving trends from unstructured text. Used for 'topic classification', 'keyword analysis', 'text mining' requests. Note: NLP model training and large-scale data processing pipeline development are out of scope.

## Error Handling
| Error Type | Strategy |
|-----------|----------|
| Data parsing failure | collector processes text-extractable portions only, notes failure sections |
| Extremely small data (fewer than 5) | Include "insufficient for statistical significance" warning, switch to qualitative analysis |
| Mixed languages | Separate analysis by language, analyze primary language only if cross-comparison is not possible |
| High sentiment analysis uncertainty | Tag with "[Confidence: Low]", recommend manual review |
| Agent failure | 1 retry → proceed without that deliverable if still failing, note omission in report |
