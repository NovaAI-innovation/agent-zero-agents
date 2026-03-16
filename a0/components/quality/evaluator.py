"""Rubric-driven evaluation entrypoints for the Quality domain."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable

from .feedback_generator import top_actions
from .report_formatter import build_report
from .signal_extractors import (
    agent_profile_criteria_scores,
    packaging_criteria_scores,
    prompt_criteria_scores,
)


RUBRICS_DIR = Path(__file__).parent / "rubrics"


def load_rubric(name: str) -> Dict[str, object]:
    """Load rubric JSON by name."""
    path = RUBRICS_DIR / f"{name}.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def evaluate(rubric_name: str, criteria_scores: Dict[str, float]) -> Dict[str, object]:
    """Evaluate a score payload against a named rubric."""
    rubric = load_rubric(rubric_name)
    criteria_weights = rubric.get("criteria", {})
    threshold = float(rubric.get("pass_threshold", 0.8))
    actions = top_actions(criteria_scores)
    return build_report(
        rubric=rubric_name,
        criteria_scores=criteria_scores,
        actions=actions,
        weights=criteria_weights,
        pass_threshold=threshold,
    )


def evaluate_prompt_text(prompt_text: str) -> Dict[str, object]:
    """Evaluate prompt text using the prompt rubric."""
    return evaluate("prompt-eval", prompt_criteria_scores(prompt_text))


def evaluate_agent_profile(profile: Dict[str, object], file_index: Iterable[str]) -> Dict[str, object]:
    """Evaluate an agent profile and file manifest."""
    return evaluate("agent-profile", agent_profile_criteria_scores(profile, file_index))


def evaluate_package_manifest(manifest: Dict[str, object]) -> Dict[str, object]:
    """Evaluate a package manifest using packaging rubric."""
    return evaluate("packaging-default", packaging_criteria_scores(manifest))
