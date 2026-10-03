# Feature Matrix

This matrix describes verified production capabilities while keeping implementation details that could reveal private data or sensitive production logic out of the public repository.

| Capability | Production behaviour | Public treatment |
| --- | --- | --- |
| Telegram interaction | Persistent menu plus inline callbacks | Documented |
| Authorization guard | Only the intended private chat may mutate state | Documented generically |
| Scheduled coaching | Multiple daily and periodic triggers | Documented |
| Nutrition FoodDB | Canonical foods + aliases + macros | Schema only |
| Natural meal logging | Parses food and quantities from text | Architecture only |
| Meal correction | Reverses previous macros before applying correction | Documented |
| Duplicate protection | Prevents repeated free-entry logging | Documented |
| Unknown-food handling | Low-confidence entries are captured for review | Documented |
| Daily macro totals | kcal, protein, carbs and fat | Documented |
| Recovery nutrition | Protects intake when recovery state is active | Abstracted |
| Specialist instructions | Pending → explicit confirmation → active rule | Documented |
| Rule supersession | New confirmed rules can supersede conflicting older rules | Documented |
| Digestive symptom state | Dedicated symptom and red-flag fields | Abstracted |
| Lower-limb symptom state | Pain, heaviness, swelling and supportive-care tracking | Abstracted |
| Clinical gating | Can block or downgrade training | Documented |
| Walking history | Minutes, distance, steps and response | Documented |
| Four-session training cycle | Strength-oriented adaptive cycle | Documented |
| Exercise metadata | cue, target feel, easier variant, rest | Documented |
| Training response learning | Recent post-session response changes future load | Documented |
| RPE history | Effort history contributes to recovery/deload logic | Documented |
| Stale training guard | Old/invalid card cannot advance cycle | Documented |
| Undo snapshots | Reversible state changes for supported actions | Documented |
| Daily closure | Consolidates day state and trends | Documented |
| 3/7/30-day analysis | Behaviour and recovery patterns | Documented |
| Context-aware coaching | Travel, shift work, illness, social context, stress | Abstracted |
| Cycle-aware context | Female-cycle context can affect advice | Abstracted |
| Dynamic workout cards | HTML → Gotenberg → PNG | Documented |
| Visual fallback | Simpler output if rendering fails | Documented |
| Health-metric vision | Extracts only clearly visible structured metrics | Abstracted |
| Baseline photo comparison | Baseline vs current monthly comparison | Architecture only |
| Phase restart | Archives prior baseline, preserves longitudinal history and starts a new 3-photo baseline | Documented |
| Daily reports | Persistent operational log | Documented |
| Weekly reports | Trend summary and adaptation | Documented |
| Monthly reports | Data + check-in + visual analysis | Documented |
| Daily reset | Clears ephemeral state, preserves longitudinal state | Documented |
| Untracked-day semantics | Missing activity is not counted as nutrition compliance | Documented |
| Google Sheets backup | Durable state and history | Documented |
| Bootstrap recovery | Rebuilds live state from durable history | Documented |
| Private relationship wellbeing | Optional production module | Excluded from public implementation |

## Deliberate exclusions

The public repository does not publish:

- personal prompts
- real food preferences
- real symptom thresholds tied to a person
- real photographs
- private relationship content
- exact production identifiers
- full workflow export
- credentials or credential references
