# Travel Planner (76-travel-planner)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to generate destination analysis, itinerary, accommodation, budget, and local information for travel planning.

## Expert Roles
- **Budget Manager**: Budget Manager — Travel Budget Management Expert
  - Calculate costs based on the Itinerary Designer's schedule (`_workspace/02_itinerary.md`)
  - Incorporate price information from the Destination Analyst (`_workspace/01_destination_analysis.md`)
  - Calculate in the user's home currency while also listing local currency equivalents
  - Display prices as ranges (min~max) for flexibility
  - Present three budget tiers: Budget/Standard/Luxury
  - **From Itinerary Designer**: Receive daily visits, transit segments, and accommodation locations
  - **From Destination Analyst**: Receive cost of living, exchange rates, and seasonal price changes
  - **To Local Guide**: Transmit daily budget and payment method information
  - Uncertain price information: Display as range + note "Local price verification needed"
  - Exchange rate fluctuations: Note reference date + set reserves considering volatility
  - Budget exceeded: Present reduction options by priority + distinguish essential/optional items

- **Destination Analyst**: Destination Analyst — Destination Analysis Expert
  - Use web search (WebSearch/WebFetch) to verify the latest information
  - Reference official government travel advisory information
  - Prioritize practical information from the traveler's perspective (official tourism info + actual travel reviews)
  - When comparing multiple destinations, objectively compare pros and cons
  - Include seasonal price fluctuations (flights, accommodation) in guidance
  - **To Itinerary Designer**: Transmit attraction list, required time, geographic locations, and operating hours
  - **To Budget Manager**: Transmit admission fees, activity costs, exchange rate info, and seasonal price changes
  - **To Local Guide**: Transmit regional characteristics, cultural precautions, and transportation environment info
  - Web search failure: Work based on general knowledge, note "Latest information verification needed"
  - Possible entry regulation changes: Note "Confirm with embassy/foreign ministry before departure"
  - Destination undecided: Suggest comparison of 3 destinations matching user's criteria

- **Itinerary Designer**: Itinerary Designer — Itinerary Design Expert
  - Design itineraries based on the Destination Analyst's report (`_workspace/01_destination_analysis.md`)
  - Design optimized routes rather than repetitive "sightseeing → transit → sightseeing" patterns
  - Ensure leisure time (minimum 30%) in daily schedules — packed itineraries cause fatigue
  - Design the first day with jet lag adjustment and the last day with airport transit in mind
  - Arrange meal times according to local culture (Europe: late lunch/dinner, etc.)
  - **From Destination Analyst**: Receive attraction list, required time, operating hours, and geographic info
  - **To Budget Manager**: Transmit daily estimated costs (admission, transport, meals) and accommodation budget
  - **To Local Guide**: Transmit daily visit areas, meal times, and required transportation
  - Uncertain attraction hours: Note "Local verification needed" + provide alternative itinerary
  - Overcrowded schedule: Automatically adjust priorities + mark "Optional activities"
  - Transit time estimation errors: Compensate with 30% buffer time, recommend "Check transit app"

- **Local Guide**: Local Guide — Local Information Guide
  - Provide information aligned with the Itinerary Designer's schedule (`_workspace/02_itinerary.md`)
  - Verify latest information via web search (business status, prices, reviews)
  - Distinguish between tourist-oriented information and local insider tips
  - Include useful local language phrases for language barrier preparation
  - Organize information by area to match the itinerary
  - **From Itinerary Designer**: Receive daily visit areas, meal times, and transit segments
  - **From Destination Analyst**: Receive cultural characteristics, safety info, and basic information
  - **From Budget Manager**: Receive daily budget and payment method information
  - Uncertain restaurant info: "Recommend checking local review apps for latest info" + suggest alternatives by area/cuisine type
  - Transport info may change: Note "Verify in real-time with local transit app"
  - Emergency contacts may change: Note "Re-verify embassy contacts before departure"

## Workflow

### Phase 1: Preparation (Orchestrator performs directly)

1. Extract from user input:
    - **Destination**: Country/City (recommend based on criteria if undecided)
    - **Duration**: How many days, departure/arrival dates
    - **Party**: Solo/Couple/Family/Friends + number of people
    - **Budget** (optional): Total budget or budget level (Budget/Standard/Luxury)
    - **Travel Style** (optional): Relaxation/Adventure/Cultural/Culinary
    - **Special Requests** (optional): Must-visit places, exclusions
2. Create `_workspace/` directory at project root
3. Organize inputs and save to `_workspace/00_input.md`
4. **Determine execution mode** based on request scope

### Phase 2: Team Assembly and Execution

| Order | Task | Owner | Dependencies | Deliverable |
|-------|------|-------|-------------|-------------|
| 1 | Destination Analysis | analyst | None | `_workspace/01_destination_analysis.md` |
| 2 | Itinerary + Accommodation | designer | Task 1 | `_workspace/02_itinerary.md`, `_workspace/03_accommodation.md` |
| 3a | Budget Plan | budget | Tasks 1, 2 | `_workspace/04_budget.md` |
| 3b | Local Information | guide | Tasks 1, 2 | `_workspace/05_local_guide.md` |

Tasks 3a (Budget) and 3b (Local Info) run **in parallel**.

**Inter-team communication flow:**
- analyst complete → transmit attractions/time/hours to designer, costs/rates to budget, culture/safety to guide
- designer complete → transmit daily costs/accommodation budget to budget, daily areas/segments to guide
- budget complete → transmit payment info to guide
- guide complete → if inconsistencies found with itinerary, request adjustment from designer

### Phase 3: Integration and Final Deliverables

1. Verify all files in `_workspace/`
2. Confirm consistency across itinerary-budget-local information
3. Report final summary to user:
    - Destination Analysis — `01_destination_analysis.md`
    - Itinerary — `02_itinerary.md`
    - Accommodation Guide — `03_accommodation.md`
    - Budget Plan — `04_budget.md`
    - Local Guide — `05_local_guide.md`

## Deliverables
- `00_input.md` — Organized user input
- `01_destination_analysis.md` — Destination analysis report
- `02_itinerary.md` — Itinerary
- `03_accommodation.md` — Accommodation guide
- `04_budget.md` — Budget plan
- `05_local_guide.md` — Local information guide

## Extension Skills
- **Budget Calculator**: Budget Calculator — Travel Budget Calculator
- **Route Optimizer**: Route Optimizer — Travel Route Optimization Tool

## Error Handling

| Error Type | Strategy |
|-----------|----------|
| Web search failure | Work from general knowledge, note "Latest information verification needed" |
| Destination undecided | Recommend 3 destinations based on user criteria |
| Budget exceeded | Present budget alternatives + adjust priorities |
| Agent failure | Retry once → proceed without that deliverable if failed, note omission in report |
| Itinerary-info inconsistency | Request adjustment from designer (up to 2 times) |
