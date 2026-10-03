# Architecture

## Design goal

Build a personal coaching system that can operate continuously without turning the LLM into the workflow controller.

The production system separates deterministic control, mutable state, domain rules, AI interpretation, visual generation and persistence.

## Layer 1 — Input and authorization

Telegram events are normalized into one internal event shape.

The production path includes an authorization guard before any user event can mutate state. Scheduled triggers bypass the Telegram path and enter only their dedicated branches.

## Layer 2 — Intent routing

High-confidence operational intents are detected before the LLM:

- nutrition logging
- nutrition summary
- nutrition correction
- menu callbacks
- training actions
- health check-ins
- progress queries
- undo
- structured measurements

Only unresolved free text is routed to AI conversation.

## Layer 3 — Domain engine

The domain engine owns the operational truth.

It maintains:

- current daily state
- longitudinal state
- nutrition mode
- training mode
- symptom flags
- recovery mode
- confirmed specialist rules
- behaviour trends
- pause/holiday context
- stale-action protection

The model receives decisions from this layer. It does not replace it.

## Layer 4 — Nutrition engine

The nutrition path uses a FoodDB plus alias table.

It supports:

- canonical foods
- aliases and multilingual normalization
- per-100g and fixed-unit foods
- explicit quantities
- explicit calorie values
- macro calculation
- confidence classification
- low-confidence fallback
- meal correction
- duplicate prevention
- daily totals

Unknown or ambiguous foods are stored for later resolution rather than silently invented.

## Layer 5 — Safety and clinical support

Health-oriented state is explicit and separate from free-form conversation.

A conservative gating layer can:

- suspend training
- reduce training volume
- switch to recovery
- suppress lower-priority wellbeing content
- avoid automatic nutrition changes
- surface a clinical-review message

Specialist instructions are not silently absorbed. A detected instruction becomes pending state and requires explicit confirmation before it becomes durable.

## Layer 6 — Adaptive training

The production system uses a four-session strength cycle.

A session is generated from:

- current cycle position
- current symptoms
- recovery state
- recent training response
- RPE history
- confirmed restrictions
- pause/holiday mode

The cycle advances only after a valid current-session completion.

Old buttons or blocked sessions cannot advance state.

## Layer 7 — Behaviour and recovery

The engine evaluates multiple time windows instead of only the latest message.

Production logic includes 3-day, 7-day and 30-day views for patterns such as:

- low energy
- training consistency
- digestive difficulty
- night-time adherence problems
- recovery trend

These patterns alter context and intervention level.

## Layer 8 — AI and vision

AI is used for tasks where deterministic logic is insufficient:

- natural-language coaching
- bounded interpretation
- multimodal health-metric extraction
- baseline-vs-current progress analysis
- narrative reporting

The model receives bounded state and explicit safety constraints.

## Layer 9 — Visual rendering

Training output can become a visual card.

The workflow builds HTML/CSS from the current adaptive session, adds exercise media or a safe diagram fallback and sends the result to Gotenberg for PNG rendering.

If rendering fails, the system degrades to a simpler visual/text fallback instead of losing the response.

## Layer 10 — Persistence and recovery

Before daily state is reset, the final state is persisted.

Long-lived state is preserved separately from ephemeral daily state.

Google Sheets acts as durable operational history. A bootstrap path can rebuild live workflow state if volatile state is lost. A phase restart archives the previous visual baseline, resets only current-period operating state and requests a new three-photo baseline while retaining longitudinal history.

## Core pattern

```text
Normalize
  → authorize
  → classify intent
  → load state
  → deterministic decision
  → call AI only when needed
  → validate
  → deliver
  → persist confirmed state
  → recover from durable history when necessary
```
