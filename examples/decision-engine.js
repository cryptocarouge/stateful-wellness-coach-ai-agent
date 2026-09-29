/**
 * Public architecture example.
 * This is intentionally generic and does not contain production thresholds,
 * personal health rules or private prompts.
 */
export function decideMode(state) {
  const decision = {
    trainingMode: "normal",
    nutritionMode: "normal",
    interventionLevel: "normal",
    aiAllowed: true,
    requiresReview: false
  };

  if (state.safety?.redFlag === true) {
    decision.trainingMode = "blocked";
    decision.nutritionMode = "review";
    decision.interventionLevel = "safety";
    decision.aiAllowed = false;
    decision.requiresReview = true;
    return decision;
  }

  if (state.recovery?.lowEnergy === true || state.recovery?.poorSleep === true) {
    decision.trainingMode = "recovery";
    decision.nutritionMode = "support";
    decision.interventionLevel = "recovery";
    return decision;
  }

  if (state.training?.recentResponse === "worse") {
    decision.trainingMode = "reduced";
    decision.interventionLevel = "support";
    return decision;
  }

  if (state.training?.consistent === true && state.recovery?.stable === true) {
    decision.trainingMode = "progress_slowly";
  }

  return decision;
}

export function canCompleteTraining(session, state, today) {
  if (!session) return false;
  if (session.date !== today) return false;
  if (session.cycleDay !== state.training?.cycleDay) return false;
  if (state.safety?.redFlag === true) return false;
  if (session.allowTraining !== true) return false;
  return true;
}
