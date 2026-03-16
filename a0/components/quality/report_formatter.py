"""Structured report formatter for Quality domain outputs."""

from typing import Dict, List

from .scoring_engine import score_criteria


def build_report(
    rubric: str,
    criteria_scores: Dict[str, float],
    actions: List[str],
    weights: Dict[str, float] | None = None,
    pass_threshold: float = 0.8,
) -> Dict[str, object]:
    """Create a normalized quality report payload."""
    overall = score_criteria(criteria_scores, weights=weights)
    failed = [name for name, score in criteria_scores.items() if score < pass_threshold]

    return {
        "rubric": rubric,
        "overall_score": round(overall, 3),
        "pass_threshold": pass_threshold,
        "passed": overall >= pass_threshold,
        "failed_criteria": failed,
        "criteria_scores": criteria_scores,
        "actions": actions,
    }
