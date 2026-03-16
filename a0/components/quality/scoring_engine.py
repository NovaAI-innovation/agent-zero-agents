"""Core scoring utilities for the Quality domain."""

from typing import Dict


def clamp_score(value: float) -> float:
    """Clamp score to 0-1 range."""
    return max(0.0, min(1.0, value))


def score_criteria(criteria_scores: Dict[str, float], weights: Dict[str, float] | None = None) -> float:
    """Return weighted normalized score from criterion-level scores (0-1 scale)."""
    if not criteria_scores:
        return 0.0

    if not weights:
        total = sum(clamp_score(score) for score in criteria_scores.values())
        return total / len(criteria_scores)

    weighted_total = 0.0
    weight_total = 0.0
    for criterion, score in criteria_scores.items():
        weight = max(0.0, weights.get(criterion, 0.0))
        weighted_total += clamp_score(score) * weight
        weight_total += weight

    if weight_total == 0.0:
        total = sum(clamp_score(score) for score in criteria_scores.values())
        return total / len(criteria_scores)

    return weighted_total / weight_total
