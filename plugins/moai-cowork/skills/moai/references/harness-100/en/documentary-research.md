# Documentary Research (09-documentary-research)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to produce documentary research, treatment plans, interview questions, and narration scripts.

## Expert Roles

- **Fact Checker**: Documentary fact checker (QA). Cross-verifies factual accuracy and consistency across research, treatment, interviews, and narration. Checks sources, logical errors, and bias, providing feedback.
  - Factual Accuracy Verification: Cross-reference all facts/statistics in the narration and research against their sources
  - Source Reliability Assessment: Evaluate each source's reliability according to academic standards
  - Logical Error Check: Detect causation errors, overgeneralizations, selective citation, etc.
  - Bias Verification: Confirm that the narrative is balanced and not skewed toward a particular perspective
  - Legal/Ethical Risk: Check for defamation, privacy violations, and copyright issues

- **Interviewer**: Documentary interviewer. Designs customized questions per interviewee, and creates an interview guide including strategy, sequence, and follow-up questions.
  - Finalize Interview Subjects: Select and prioritize final interview subjects from the candidates proposed by the researcher
  - Question Design: Write customized, open-ended questions for each subject
  - Interview Strategy: Design the flow of rapport building -> core questions -> sensitive questions -> closing
  - Follow-Up Question Tree: Design follow-up question branches based on anticipated responses
  - Interview Operations Guide: Organize location, timing, filming setup, and precautions

- **Narrator**: Documentary narrator. Writes narration scripts according to the treatment. Produces completed narration scripts including scene-by-scene tone, rhythm, emotional transitions, and fact delivery.
  - Narration Script Writing: Write narration matching each scene in the treatment
  - Tone Adjustment: Adjust tone to match each scene — objective reporting, emotional reflection, tense investigation, etc.
  - Fact Delivery: Naturally weave accurate information such as statistics, dates, and names into the narration
  - Interview Bridging: Provide context and connections through narration before and after interview clips
  - Emotional Rhythm Design: Design the narration's rhythm through sentence length, breathing, and pauses

- **Researcher**: Documentary researcher. Conducts in-depth research on the subject, collects statistics, compiles expert lists, analyzes historical context, and organizes references.
  - In-Depth Subject Research: Investigate the topic's historical background, current situation, and future outlook from multiple angles
  - Statistics & Data Collection: Collect quantitative data, statistics, and research findings to support claims
  - Expert & Witness List: Compile a list of potential interviewees including experts, stakeholders, and witnesses
  - Multi-Perspective Collection: Collect diverse perspectives in a balanced manner — for, against, and neutral
  - Reference Organization: Organize all source materials according to academic standards

- **Story Architect**: Documentary story architect. Converts research results into a 3-act treatment, designing scene division, narrative arc, emotion curves, and sequence structure.
  - 3-Act Structure Design: Design a treatment with introduction (setup/hook) -> development (conflict/deepening) -> conclusion (resolution/resonance)
  - Scene Division: Divide each act into scene units, defining each scene's purpose, content, and connections
  - Narrative Arc Design: Design the topic's emotional journey (curiosity -> empathy -> anger/surprise -> understanding -> call to action)
  - Sequence Composition: Specify the mix ratio of interview + narration + archive + field footage per scene
  - Emotion Curve Design: Map viewer emotional changes along the time axis to prevent boredom

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Topic**: The subject the documentary will cover
   - **Format**: Investigative/Character-driven/Historical/Observational
   - **Length**: 15 min/30 min/60 min/90 min
   - **Tone** (optional): Objective/Emotional/Tense/Reflective
   - **Existing Files** (optional): Research materials, proposals, etc.
2. Create the `_workspace/` directory in the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding Phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|------------|--------------|-------------|
| 1 | Research | researcher | None | `_workspace/01_research_brief.md` |
| 2 | Treatment writing | story-architect | Task 1 | `_workspace/02_structure.md` |
| 3a | Interview guide | interviewer | Tasks 1, 2 | `_workspace/03_interview_guide.md` |
| 3b | Narration script | narrator | Tasks 1, 2 | `_workspace/04_narration_script.md` |
| 4 | Fact-check/Review | fact-checker | Tasks 1, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (interview) and 3b (narration) are **executed in parallel**. Both depend on Tasks 1 (research) and 2 (treatment).

**Inter-team communication flow:**
- researcher complete -> Deliver timelines and key facts to story-architect, deliver expert list to interviewer
- story-architect complete -> Deliver scene-by-scene interview needs to interviewer, deliver tone and emotional flow to narrator
- interviewer <-> narrator: Share interview topics to prevent overlap with narration
- fact-checker cross-validates all deliverables. When RED Must Fix is found, request revisions from the relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - Research brief — `01_research_brief.md`
   - Treatment — `02_structure.md`
   - Interview guide — `03_interview_guide.md`
   - Narration script — `04_narration_script.md`
   - Fact-check report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_research_brief.md` — Research brief
- `02_structure.md` — Treatment/structure design
- `03_interview_guide.md` — Interview guide
- `04_narration_script.md` — Narration script
- `05_review_report.md` — Fact-check/review report

## Extension Skills

- **interview-design**: A specialized skill for the interviewer agent covering documentary interview design. Provides interviewee selection, question sequence design, emotional elicitation techniques, and ethical interview principles. Use for 'interview questions,' 'interview subjects,' 'testimony collection,' 'interview design,' and similar topics.
- **investigative-research**: A specialized skill for the researcher and fact-checker agents covering investigative research. Provides primary/secondary source collection, source reliability assessment, data triangulation, and bias analysis methodologies. Use for 'research,' 'fact-checking,' 'source verification,' 'investigative techniques,' and similar topics.
- **narrative-structure**: A specialized skill for the story-architect and narrator agents covering documentary narrative structure. Provides 3-act structure, emotion curves, scene arrangement, and narrative patterns by documentary type. Use for 'treatment,' 'narrative structure,' '3-act,' 'emotion curve,' and similar topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Work based on general knowledge, note "data limitations" in report |
| Only one perspective found | Intentionally search for opposing perspectives, note in report if not found |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
| Sensitive topic | Note legal/ethical risks in report, recommend professional legal counsel |
