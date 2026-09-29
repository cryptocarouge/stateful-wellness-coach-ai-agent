# Production Evidence

This document records non-sensitive engineering facts verified from the private active deployment.

## Verification date

**2026-09-29**

## Workflow-scale facts

| Metric | Verified value |
| --- | ---: |
| Active workflow nodes | 87 |
| Trigger nodes | 12 |
| Code nodes | 33 |
| Distinct Telegram callback actions found in code | 118 |
| Central domain-engine size | ~6,100 lines |
| AI-response extraction/handling engine | ~2,600 lines |

## Verified operational mechanisms

The production workflow contains implemented paths for:

- Telegram authorization and normalization
- intent routing before AI
- deterministic nutrition parsing
- confidence-based unknown-food handling
- corrections and duplicate protection
- adaptive training generation
- post-training response logging
- RPE tracking
- symptom-aware training gating
- pending/confirmed specialist-rule memory
- walking history
- daily/weekly/monthly reports
- visual workout-card rendering
- rendering fallback
- multimodal photo input
- final daily persistence before reset
- daily state reset
- longitudinal-state preservation
- Google Sheets persistence
- live-state bootstrap recovery
- undo snapshots
- stale callback protection

## What this evidence does not mean

It is not a clinical validation study.

It does not disclose private user outcomes.

It does not claim that this architecture should be copied into a medical product without domain, legal, privacy and safety review.

It demonstrates that the architecture described in this repository is derived from an actually deployed system rather than a hypothetical diagram.
