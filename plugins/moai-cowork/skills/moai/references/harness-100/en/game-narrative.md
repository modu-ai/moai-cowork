# Game Narrative (05-game-narrative)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview

A harness where an agent team collaborates to design game story, quests, dialogue, and branching scenarios.

## Expert Roles

- **Branch Architect**: Game branch architect. Designs story branching structures, ending variations, flag systems, and consequence frameworks.
  - Branch Structure Design: Design the story's key branching points and the outcomes of each path
  - Ending Design: Design multiple endings based on the player's cumulative choices
  - Flag System: Define variables (flags) that track choices and conditional branching logic
  - Consequence Weighting: Define the magnitude of each choice's impact on the story
  - Convergence Points: Design where and how divergent paths reconverge

- **Dialogue Writer**: Game dialogue writer. Writes NPC dialogue, player choices, emotional direction, and cutscene dialogue tailored to each character's personality.
  - NPC Dialogue Writing: Write unique dialogue matching each NPC's personality, background, and emotional state
  - Player Choice Design: Design choices that express character personality, not simple yes/no options
  - Cutscene Dialogue: Write cinematic dialogue for key story moments
  - Bark Writing: Write short situational lines (barks) for combat, exploration, reactions, etc.
  - Emotion Tags: Assign emotion/tone tags to each line to provide voice acting guidance

- **Narrative Reviewer**: Game narrative reviewer (QA). Cross-validates consistency, plot holes, and balance across world-building, quests, dialogue, and branches.
  - Plot Hole Detection: Find logical contradictions, timeline errors, and causal disconnections in the story
  - Character Consistency: Do characters' actions/dialogue match their established personality and motivations?
  - Branch Balance: Is the content quantity and quality balanced across each branching path?
  - World-Building Compliance: Do quests/dialogue violate world-building rules?
  - Player Experience: Is the overall narrative flow immersive and satisfying?

- **Quest Designer**: Game quest designer. Designs main/side quests and concretely defines objectives, steps, rewards, and failure conditions.
  - Main Quest Line: Design the core quest chain that runs through the entire story
  - Side Quests: Design optional quests that enrich the world-building
  - Objectives & Steps: Concretely define start conditions, intermediate goals, and completion conditions for each quest
  - Reward System: Design rewards including experience points, items, story unlocks, reputation, etc.
  - Failure & Alternatives: Design consequences of quest failure and alternative paths

- **Worldbuilder**: Game world designer. Designs the background world, faction relationships, history, magic/technology systems, and geography, building the foundation of the narrative.
  - World Setting: Define the era, genre, and physical/supernatural rules of the world
  - Factions & Organizations: Design the relationships and conflict structures between major powers, organizations, and nations
  - Historical Timeline: Organize key historical events that influence the current story
  - Magic/Technology Systems: Define the rules and limitations of the world's supernatural or technological systems
  - Key Characters: Design the backgrounds, motivations, and personalities of the protagonist, antagonist, and major NPCs

## Workflow

### Phase 1: Preparation (Performed Directly by the Orchestrator)

1. Extract from user input:
   - **Game Genre**: RPG/Adventure/Visual Novel/MMORPG, etc.
   - **World-Building Direction**: Fantasy/Sci-Fi/Modern/Historical, etc.
   - **Story Tone**: Dark/Light/Humorous/Epic
   - **Expected Scale**: Playtime, number of quests
   - **Existing Settings** (optional): World-building, characters, etc. provided by the user
2. Create the `_workspace/` directory in the project root
3. Organize the input and save it to `_workspace/00_input.md`
4. If existing files are present, copy them to `_workspace/` and skip the corresponding Phase
5. **Determine the execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Dependencies | Deliverable |
|-------|------|------------|--------------|-------------|
| 1 | World-building | worldbuilder | None | `_workspace/01_worldbuilding.md` |
| 2 | Quest design | quest-designer | Task 1 | `_workspace/02_quest_design.md` |
| 3a | Dialogue writing | dialogue-writer | Tasks 1, 2 | `_workspace/03_dialogue_script.md` |
| 3b | Branch design | branch-architect | Tasks 1, 2 | `_workspace/04_branch_map.md` |
| 4 | Narrative review | narrative-reviewer | Tasks 2, 3a, 3b | `_workspace/05_review_report.md` |

Tasks 3a (dialogue) and 3b (branching) are **executed in parallel**. Since both depend on Task 2 (quests), they can start simultaneously after quest design is complete.

**Inter-team communication flow:**
- worldbuilder complete -> Deliver factions, characters, and locations to quest-designer; deliver character personalities and speech patterns to dialogue-writer; deliver faction relationships and world rules to branch-architect
- quest-designer complete -> Deliver per-quest dialogue lists to dialogue-writer; deliver branching points to branch-architect
- dialogue-writer <-> branch-architect: Coordinate choices and branching flags with each other
- reviewer cross-validates all deliverables. When RED Must Fix is found, request revisions from the relevant agent -> rework -> re-verify (up to 2 times)

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm that all RED Must Fix items from the review report have been addressed
3. Report the final summary to the user:
   - World-building settings — `01_worldbuilding.md`
   - Quest design — `02_quest_design.md`
   - Dialogue script — `03_dialogue_script.md`
   - Branch structure map — `04_branch_map.md`
   - Review report — `05_review_report.md`

## Deliverables

- `00_input.md` — Organized user input
- `01_worldbuilding.md` — World-building document
- `02_quest_design.md` — Quest design document
- `03_dialogue_script.md` — Dialogue script
- `04_branch_map.md` — Branching structure map
- `05_review_report.md` — Review report

## Extension Skills

- **branching-logic**: A specialized skill for the branch-architect agent covering branching logic. Provides branching structure patterns, flag system design, ending architecture, and state management methodology. Use for 'branch design,' 'multiple endings,' 'flag systems,' 'branching structures,' and similar topics.
- **dialogue-systems**: A specialized skill for the dialogue-writer agent covering game dialogue systems. Provides character voice design, choice psychology, bark systems, cutscene direction, and emotion tag systems. Use for 'game dialogue,' 'NPC conversations,' 'choice design,' 'character voice,' and similar topics.
- **quest-design-patterns**: A specialized skill for the quest-designer agent covering quest design patterns. Provides quest archetypes, reward psychology, difficulty curves, and player motivation frameworks. Use for 'quest design,' 'reward systems,' 'mission structure,' 'quest patterns,' and similar topics.

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Genre/setting unclear | Worldbuilder proposes 3 concepts, proceed after user selection |
| Request based on existing IP | Respect original settings, create only in expandable areas, note copyright considerations |
| Agent failure | 1 retry -> if still fails, proceed without that deliverable, note omission in review report |
| RED found in review | Request revision from relevant agent -> rework -> re-verify (up to 2 times) |
