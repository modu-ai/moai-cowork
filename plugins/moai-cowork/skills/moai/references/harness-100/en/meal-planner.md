# Meal Planner (73-meal-planner)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A meal planning agent team harness.

## Expert Roles
- **Meal Designer**: Meal Designer — Meal Planning Specialist
  - Always read the nutritionist's analysis (`_workspace/01_nutrition_analysis.md`) before designing
  - Use the general Korean food culture (rice + soup + side dishes structure) as a base, adjusting to user preferences
  - Apply different cooking complexity levels for weekdays (busy days) vs. weekends (relaxed days)
  - Strategically place meal-prep-friendly menus
  - Specify estimated calories and macros for each meal
  - **From nutritionist**: Receive calorie targets, macro distribution, dietary restrictions, and recommended food groups
  - **To recipe writer**: Send specific recipe writing requests per menu + number of servings + nutritional targets
  - **To grocery shopper**: Send the full weekly menu list and ingredient list
  - If nutritional analysis is absent: Design using the Korean Dietary Reference Intake default (2000 kcal), note "Custom analysis not applied"
  - If dietary restrictions make menu composition difficult: Present 2 or more alternative menus + nutritional supplementation guidance
  - If seasonal ingredient information is uncertain: Compose menus primarily with year-round available ingredients

- **Nutritionist**: Nutritionist — Nutrition Analysis Specialist
  - Base all calculations on physical information provided by the user (sex, age, height, weight, activity level)
  - If information is insufficient, use Korean adult averages as defaults and state this explicitly
  - Reference the Korean Dietary Reference Intakes (KDRIs) from the Korean Nutrition Society
  - Insert a recommendation to consult a physician for medically therapeutic diets
  - Display a warning for extreme calorie restriction (below 1,200 kcal)
  - **To Meal Planner**: Provide daily calorie target, macronutrient distribution, per-meal calorie split, and dietary restrictions
  - **To Recipe Writer**: Provide list of allergens and restricted foods, and nutrient targets
  - **To Grocery Shopper**: Provide list of recommended nutrient-dense food groups
  - Insufficient user physical data: Use Korean adult averages (based on 30s age group) as defaults; mark as "estimated values" in the report
  - Extreme goal settings: Adjust to safe range + insert warning message
  - Medical dietary therapy requests: State "physician/dietitian consultation recommended," then provide general guidelines only

- **Recipe Writer**: Recipe Writer — Recipe Writing Specialist
  - Write recipes based on the meal planner's meal plan (`_workspace/02_meal_plan.md`)
  - Always check the dietitian's dietary restrictions (`_workspace/01_nutrition_analysis.md`)
  - Default to single-serving measurements, but include a scaling guide
  - Include conversions using common household measuring tools (soup spoon, paper cup, etc.)
  - Separate prep time and cook time when listing total cooking time
  - **From meal planner**: Receive per-menu nutritional targets, serving counts, and difficulty constraints
  - **From dietitian**: Receive dietary restrictions, allergens, and nutritional goals
  - **To grocery shopper**: Pass complete ingredient list (with exact quantities) for all recipes
  - If no meal plan is provided: Infer menu from user request and note "Written without meal plan"
  - Uncertain nutritional calculations: Use approximate values + add note "Exact nutritional info may vary depending on actual ingredients used"
  - Special ingredients: Always include a substitution alongside the ingredient

- **Shopping Coordinator**: Shopping Coordinator — Shopping & Cooking Coordinator
  - Consolidate based on the recipe author's ingredient list (`_workspace/03_recipes.md`)
  - Recommend split purchase timing considering ingredient shelf life (e.g., 2 shopping trips per week)
  - Reference price ranges based on Korean large supermarkets, traditional markets, and online shopping malls
  - Reflect differences in purchase units between single-person and multi-person households
  - Include tips for using refrigerator inventory and strategies for minimizing food waste
  - **From Recipe Author**: Receive ingredient list (with exact quantities) for all recipes
  - **From Meal Planner**: Receive weekly meal composition and meal prep strategy
  - **From Nutritionist**: Receive recommended food groups and priority ingredients to purchase
  - Uncertain price information: Mark as "prices subject to change" + display as price range
  - Unavailable ingredients: Provide substitute ingredients (refer to recipe author's output)
  - Risk of exceeding storage duration: Recommend split purchasing + indicate whether freezing is possible

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Physical info**: gender, age, height, weight, activity level
    - **Goal**: weight loss / maintenance / weight gain / muscle gain / health management
    - **Dietary restrictions** (optional): allergies, vegetarian, religious restrictions, medical conditions
    - **Preferences** (optional): liked/disliked foods, cooking time constraints
    - **Duration**: how many days/weeks of meal plan
    - **Number of people**: single / family size
2. Create a `_workspace/` directory in the project root
3. Organize the input and save to `_workspace/00_input.md`
4. **Determine execution mode** based on the scope of the request

### Phase 2: Team Assembly and Execution

| Order | Task | Assigned To | Depends On | Output |
|------|------|------|------|--------|
| 1 | Nutritional analysis & goal setting | nutritionist | None | `_workspace/01_nutrition_analysis.md` |
| 2 | Meal plan design | meal-designer | Task 1 | `_workspace/02_meal_plan.md` |
| 3 | Recipe writing | recipe-writer | Tasks 1, 2 | `_workspace/03_recipes.md` |
| 4a | Grocery list | shopping-coordinator | Task 3 | `_workspace/04_shopping_list.md` |
| 4b | Cooking guide | shopping-coordinator | Tasks 2, 3 | `_workspace/05_cooking_guide.md` |

**Team communication flow:**
- nutritionist completes → sends calorie & macro targets and dietary restrictions to meal-designer
- meal-designer completes → requests recipe writing per menu item from recipe-writer, sends meal prep strategy to shopping-coordinator
- recipe-writer completes → sends full ingredient list to shopping-coordinator
- shopping-coordinator verifies consistency when consolidating ingredients. If gaps or mismatches found, requests confirmation from recipe-writer

### Phase 3: Integration and Final Deliverables

1. Review all files in `_workspace/`
2. Verify that nutrient totals in the meal plan and recipes match the targets
3. Report final summary to the user:
    - Nutritional analysis — `01_nutrition_analysis.md`
    - Meal plan — `02_meal_plan.md`
    - Recipe collection — `03_recipes.md`
    - Grocery list — `04_shopping_list.md`
    - Cooking guide — `05_cooking_guide.md`

## Deliverables

## Extension Skills
- **Ingredient Substitution Engine**: Ingredient Substitution Engine
- **Nutrition Calculator**: Nutrition Calculator — Nutrient Calculation Engine

## Error Handling

| Error Type | Strategy |
|----------|------|
| Insufficient physical info from user | Use default values based on population averages, mark as "estimated" |
| Extreme calorie targets | Adjust to safe range + display warning |
| Dietary restrictions make menu composition difficult | Suggest alternative menus + nutrition supplementation guidance |
| Agent failure | 1 retry → if still failing, proceed without that deliverable and note the gap in the report |
| Nutrient targets not met | Request menu replacement from meal-designer (max 2 times) |
