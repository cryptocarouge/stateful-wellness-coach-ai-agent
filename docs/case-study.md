# Case Study — Stateful Wellness Coach AI Agent

## Problem

A useful long-running coach cannot be only a chat prompt.

It must remember what happened, avoid double-counting actions, adapt to changing state, separate high-risk decisions from motivational language, survive workflow restarts and remain usable through simple daily interactions.

The private production system was built around those requirements.

## Main architecture decision

The most important decision was to make the **workflow state machine authoritative** and the LLM advisory.

The model is not asked to decide whether an action already happened, whether a meal was counted, whether a training button is stale, whether state should be reset or whether an external record was persisted.

Those are deterministic responsibilities.

## Why this matters

Without deterministic control, a conversational agent can:

- count the same meal twice
- advance a training plan from an old button
- forget a restriction after a restart
- overwrite historical state
- generate advice from incomplete inputs
- persist something that never actually happened

The production architecture directly guards against these failure modes.

## Nutrition as structured state

Natural-language food logging is converted into structured items before totals are mutated.

The parser uses a FoodDB and aliases, quantity handling, confidence levels and duplicate hashes.

A correction is handled as a state transition: remove the previous contribution, apply the corrected one, then persist the new confirmed state.

## Specialist rules as confirmed memory

Potential specialist instructions are detected from free text but remain pending.

The user must explicitly confirm before the rule becomes durable.

This creates a clean difference between:

- something the model inferred from a sentence
- something the user confirmed should govern future behaviour

## Training as a guarded state machine

The training cycle does not simply increment on button click.

The current session contains date, cycle position and eligibility. The completion handler verifies that the card is current and still allowed before state changes.

That protects the system from stale Telegram callbacks and from safety state changing after the card was created.

## AI after decision

When free-form coaching is needed, the prompt receives:

- bounded current state
- recent trends
- the already-computed operating mode
- confirmed constraints
- explicit safety ordering

The AI communicates within that frame rather than recreating the engine in prose.

## Visual output with graceful degradation

Adaptive training can be rendered as a structured visual card.

The system assembles HTML/CSS, combines exercise media and diagrams, renders through Gotenberg and sends the PNG through Telegram.

A rendering failure falls back to simpler output so that the workflow remains operational.

## Memory that survives reset

Daily state must be cleared without deleting long-term intelligence.

The workflow first persists the final day, then resets transient state while preserving longitudinal memory.

A bootstrap path can rebuild the live state from durable Google Sheets history.

## Production validation

The public architecture was derived by inspecting the active private workflow on 2026-09-29.

At that point the workflow contained:

- 87 nodes
- 12 triggers
- 33 Code nodes
- 118 distinct callback actions

Two central code engines together contained thousands of lines of workflow logic.

The public repository does not claim medical outcomes or expose private user results. The production evidence here is evidence of deployed engineering behaviour.

## Takeaway

The reusable pattern is:

> **state first, deterministic rules second, AI only where it adds value, validation before mutation, persistence after confirmation, and recovery designed from the beginning.**
