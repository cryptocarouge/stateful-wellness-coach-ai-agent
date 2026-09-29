# Sanitization Audit

## Publication strategy

The public edition was created **from a capability and architecture audit**, not by exporting and cleaning the private workflow.

This matters because the private production workflow contains sensitive data in more places than credential objects alone.

## Risk classes checked

### Credentials and infrastructure

Checked for:

- API keys
- bot tokens
- OAuth secrets
- credential objects
- webhook URLs
- private domains/endpoints
- spreadsheet/document URLs

**Decision:** none are permitted in the public repository.

### Direct identifiers

Checked for:

- names
- chat IDs
- contact information
- account identifiers
- Telegram media identifiers

**Decision:** replaced by generic concepts or omitted.

### Sensitive personal state

Checked for:

- health history
- symptom history
- measurements
- user-specific restrictions
- clinician instructions
- private behavioural history

**Decision:** represented only as generic schema fields and architectural patterns.

### Private media and sensitive personal content

Checked for:

- personal photographs
- visual baselines
- private media IDs
- sensitive personal cards, messages and private wellbeing content

**Decision:** excluded. Only the existence of an optional private wellbeing module is acknowledged.

### Production prompts

Checked for:

- personal profile data
- user-specific tone
- sensitive thresholds
- exact private rules
- private system instructions

**Decision:** not published.

### Production workflow export

**Decision:** not published.

A full n8n JSON export is considered too risky because embedded code, comments, expressions and defaults can leak information even after credentials are removed.

## Public-safe content

The repository publishes:

- verified scale metrics
- architecture
- data-flow concepts
- state-management strategy
- safety ordering
- failure-mode handling
- generic state examples
- generic decision-engine examples
- privacy methodology

## Automated check

The default branch is protected by a repository-level public safety scan executed by GitHub Actions.

Latest public-safety run should be green before this repository is referenced from the public profile.
