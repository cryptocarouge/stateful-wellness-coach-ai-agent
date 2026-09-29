# State Model

The production design separates **ephemeral daily state** from **longitudinal durable state**.

The example below is intentionally fictional and incomplete.

## Example public schema

```json
{
  "profile": {
    "clientId": "demo-user",
    "target": "generic-wellness-goal"
  },
  "daily": {
    "date": "YYYY-MM-DD",
    "macros": {
      "kcal": 0,
      "protein": 0,
      "carbs": 0,
      "fat": 0
    },
    "trainingCompleted": false,
    "lowEnergy": false,
    "sleepHours": null,
    "waterLitres": 0,
    "steps": 0
  },
  "training": {
    "cycleDay": 1,
    "mode": "normal",
    "recentRpe": [],
    "recentResponses": []
  },
  "safety": {
    "reviewRequired": false,
    "trainingAllowed": true,
    "confirmedRules": []
  },
  "behaviour": {
    "consistencyTrend": "unknown",
    "energyTrend": "unknown",
    "recoveryTrend": "unknown"
  },
  "memory": {
    "dailyLogs": [],
    "weeklyReports": [],
    "monthlyReports": []
  }
}
```

## Why separate state classes

Daily data should reset.

Longitudinal learning should not.

A robust daily reset therefore follows this pattern:

1. finalize the current day
2. persist the final row
3. snapshot the durable fields
4. clear ephemeral values
5. restore durable fields
6. initialize the new day

## Idempotency

The system stores per-day action flags and processed-entry hashes.

That allows the workflow to answer repeated button presses or duplicated Telegram events without mutating totals twice.

## Undo

For supported state mutations, a pre-mutation snapshot is pushed to a bounded undo stack.

Undo restores the previous state instead of attempting to reverse every field independently.

## Durable recovery

The live workflow state is convenient but not treated as the only copy of truth.

Persisted history can be used to reconstruct:

- current operating mode
- recent logs
- training position
- longitudinal trends
- confirmed rules
- milestone state

This makes the agent recoverable after workflow restarts or volatile-state loss.
