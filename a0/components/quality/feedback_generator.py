"""Feedback generation helpers for the Quality domain."""

from typing import Dict, List


CRITERION_ACTIONS = {
    "clarity": "Clarify instructions, define terms, and remove ambiguity.",
    "specificity": "Add explicit constraints, scope, and expected outputs.",
    "structure": "Reorganize into ordered steps and consistent sections.",
    "bias_free": "Remove leading assumptions and add neutral framing.",
    "robustness": "Add edge-case handling and fallback behavior.",
    "efficiency": "Reduce token waste and remove redundant instructions.",
    "logic": "Align task flow and decision points with desired outcomes.",
    "tools": "Specify valid tools, boundaries, and invocation criteria.",
    "optimization": "Tighten defaults and improve execution reliability.",
    "compliance": "Add explicit safety/privacy/compliance guardrails.",
}


def top_actions(criteria_scores: Dict[str, float], limit: int = 3) -> List[str]:
    """Return improvement actions for lowest-scored criteria first."""
    ranked = sorted(criteria_scores.items(), key=lambda item: item[1])
    actions: List[str] = []
    for name, _ in ranked[:limit]:
        actions.append(CRITERION_ACTIONS.get(name, f"Improve '{name}' criterion quality."))
    return actions
