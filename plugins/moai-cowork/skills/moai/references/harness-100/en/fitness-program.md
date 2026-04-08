# Fitness Program (74-fitness-program)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A fitness program design agent team harness.

## Expert Roles
- **Exercise Guide**: Exercise Guide — Exercise Guide Writer
  - Work based on the program designer's exercise list (`_workspace/01_program_design.md`)
  - Use both anatomical and everyday terminology side by side (e.g., "latissimus dorsi (broad back muscle)")
  - Prioritize injury prevention above all; insert ⚠️ warnings for risky movements
  - Always include warm-up routines and cool-down stretching
  - Display difficulty in 3 levels: easy / moderate / hard
  - **From Program Designer**: Receive exercise list, purpose of each exercise, and precautions
  - **To Nutrition Coordinator**: Send list of high-intensity exercises (for pre/post-workout nutrition timing)
  - **To Template Builder**: Send per-exercise tracking fields (weight, reps, RPE, notes)
  - If program design document not provided: infer exercise type from user request, note "written without program integration"
  - Exercise matching injury history: ⚠️ warning + prioritize alternative exercises + recommend "perform only after consulting a professional"
  - Equipment not available: automatically substitute with alternatives (bodyweight / band / dumbbell)

- **Nutrition Linker**: Nutrition Linker — Nutrition Integration Specialist
  - Design based on the exercise intensity and volume from the program designer (`_workspace/01_program_design.md`)
  - Reference ISSN (International Society of Sports Nutrition) position stands
  - Clearly state evidence grade (A/B/C) for all supplements
  - Default to a food-first principle, with supplements offered as additional options
  - Note any relevant doping-related precautions when applicable
  - **From Program Designer**: Receive exercise intensity, volume, periodization schedule, and goals
  - **From Exercise Guide**: Receive list of high-intensity exercises and session durations
  - **To Template Builder**: Deliver nutrition tracking items (calories, hydration, body weight, etc.)
  - User body weight not provided: Provide total amount-based recommendations when g/kg calculation is not possible; note "body weight-based adjustment required"
  - Special dietary restrictions: Assess feasibility of reaching goals within those restrictions + propose alternatives
  - Supplement allergies / refusal: Prioritize food-based alternatives

- **Program Architect**: Program Architect — Exercise Program Designer
  - Design programs based on scientific evidence (ACSM, NSCA guidelines)
  - Always reflect the Progressive Overload principle
  - Build programs suited to available equipment (home gym/commercial gym/bodyweight)
  - When injury history exists, specify precautions for exercises targeting that area
  - Always include Deload cycles
  - **To Exercise Guide**: Deliver the list of exercises in the program along with each exercise's purpose and precautions
  - **To Nutrition Coordinator**: Deliver training intensity, volume, and goals (for calorie and macro calculations)
  - **To Template Builder**: Deliver variables to track (weight, reps, RPE, etc.) and periodization schedule
  - Insufficient user information: Design conservatively (beginner standard), note "Fitness level unconfirmed"
  - Existing injury history: Exclude exercises for that area or substitute rehabilitation exercises + "Recommend consulting a specialist"
  - Equipment limitations: Program using bodyweight/dumbbell/band substitution exercises
  - Equipment limitations: Program with bodyweight / dumbbell / band substitution exercises

- **Template Builder**: Template Builder
  - Design templates aligned with the periodization schedule from the program designer (`_workspace/01_program_design.md`)
  - Reflect the logging items from the exercise guide (`_workspace/03_exercise_guide.md`)
  - Integrate tracking items from the nutrition plan (`_workspace/04_nutrition_plan.md`)
  - Write in markdown tables using structures that are easy to convert to spreadsheets
  - Balance minimizing recording burden while ensuring all essential data is captured
  - **From Program Designer**: Receive periodization schedule, tracking variables (weight, reps, RPE), and evaluation timing
  - **From Exercise Guide**: Receive per-exercise logging items and key observation points
  - **From Nutrition Planner**: Receive nutrition tracking items (calories, hydration, body weight, etc.)
  - Insufficient program information: Provide a general-purpose log template and note "can be customized once program is linked"
  - Excessive tracking items: Categorize as required/optional to reduce recording burden
  - Missing measurement tools: Provide alternative measurement methods (e.g., waist circumference instead of body fat calipers)

## Workflow

### Phase 1: Preparation (Orchestrator handles directly)

1. Extract from user input:
    - **Goal**: hypertrophy / strength / fat loss / fitness improvement / rehabilitation
    - **Fitness level**: beginner / intermediate / advanced, training history
    - **Available resources**: X sessions/week, X minutes/session, equipment (gym / home / bodyweight)
    - **Physical info** (optional): sex, age, height, weight
    - **Injury history** (optional): area, current condition
    - **Existing program** (optional): currently running program
2. Create a `_workspace/` directory at the project root
3. Organize inputs and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Depends on | Output |
|------|------|------|------|--------|
| 1 | Program design + weekly schedule | architect | none | `01_program_design.md`, `02_weekly_schedule.md` |
| 2a | Exercise guide document | guide | Task 1 | `03_exercise_guide.md` |
| 2b | Nutrition pairing chart | linker | Task 1 | `04_nutrition_plan.md` |
| 3 | Progress tracking template | builder | Tasks 1, 2a, 2b | `05_tracking_template.md` |

Tasks 2a (exercise guide) and 2b (nutrition pairing) run **in parallel**.

**Inter-agent communication flow:**
- architect completes → sends exercise list and precautions to guide, sends intensity/volume/goal to linker, sends periodization schedule to builder
- guide completes → sends high-intensity exercise list to linker, sends logging items to builder
- linker completes → sends nutrition tracking items to builder
- builder integrates all information to create the template; if missing items are found, requests clarification from the relevant agent

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify consistency across program–schedule–guide–nutrition–template
3. Report final summary to the user:
    - Program design doc — `01_program_design.md`
    - Weekly schedule — `02_weekly_schedule.md`
    - Exercise guide — `03_exercise_guide.md`
    - Nutrition pairing chart — `04_nutrition_plan.md`
    - Tracking template — `05_tracking_template.md`

## Deliverables

## Extension Skills
- **Exercise Biomechanics**: Exercise Biomechanics — Exercise Biomechanics Guide
- **Periodization Engine**: Periodization Engine

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient user info | Design using conservative (beginner) baseline; note "fitness level unconfirmed" |
| Injury history | Exclude or substitute exercises for the affected area + "consult a specialist" note |
| Equipment limitations | Compose with substitute exercises within available equipment |
| Agent failure | Retry once → if still failing, proceed without that deliverable and note the omission in the report |
| Program inconsistency | Request revision from architect (up to 2 times) |
