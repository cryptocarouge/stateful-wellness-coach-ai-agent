# Privacy Boundary

The production system is personal by design. The public repository is therefore built from a **clean-room architecture description**, not from a scrubbed production export.

## Why no sanitized production JSON is published

Search-and-replace sanitization is not sufficient for a workflow that may contain:

- values embedded in Code nodes
- URLs assembled at runtime
- media file IDs
- user-specific prompt fragments
- private state defaults
- credential references
- spreadsheet identifiers
- comments containing personal context

A superficially sanitized export can still leak data.

The safer publication model is:

```text
private production workflow
        ↓ inspect
architecture + capability inventory
        ↓ rewrite from clean public assumptions
public documentation and generic schemas
```

## Private categories removed

### Identity

No real user name, relationship, employer, contact information, chat identifier or personal profile is published.

### Health

No real condition history, symptoms, measurements, clinician notes or user-specific health rules are published.

### Media

No progress photographs, private images, Telegram media IDs or visual baselines are published.

### Relationship wellbeing

The production system contains a private optional wellbeing module. Its private text, media and user-specific implementation are intentionally excluded.

### Infrastructure

No tokens, keys, webhook URLs, credentials, spreadsheet IDs, private domains or internal endpoints are published.

### Prompts and logic

Public docs explain the control architecture without reproducing private prompts or user-specific decision parameters.

## Public safety scan

Every push to the default branch runs an automated scanner for common secret patterns and known private-reference categories.

The scanner is an additional guard, not a substitute for manual review.

## Production remains separate

Nothing in this repository is read by, written to or imported into the private production workflow.
