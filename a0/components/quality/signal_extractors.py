"""Deterministic score extractors for Quality domain evaluations."""

from __future__ import annotations

import re
from typing import Dict, Iterable


def _contains_any(text: str, patterns: Iterable[str]) -> bool:
    lower = text.lower()
    return any(pattern in lower for pattern in patterns)


def _ratio(matched: int, total: int) -> float:
    if total <= 0:
        return 0.0
    return matched / total


def prompt_criteria_scores(prompt_text: str) -> Dict[str, float]:
    """Return normalized criterion scores for prompt quality."""
    text = prompt_text.strip()
    lower = text.lower()

    clarity_checks = [
        "you are",
        "output",
        "input",
    ]
    specificity_checks = [
        "must",
        "exact",
        "format",
        "constraints",
        "requirements",
    ]
    structure_checks = [
        "##",
        "1.",
        "2.",
        "steps",
    ]
    safety_checks = [
        "ethical",
        "redact pii",
        "gdpr",
        "safe",
        "privacy",
    ]
    robustness_checks = [
        "edge case",
        "if no",
        "fallback",
        "error",
        "validate",
    ]

    clarity = _ratio(sum(1 for c in clarity_checks if c in lower), len(clarity_checks))
    specificity = _ratio(sum(1 for c in specificity_checks if c in lower), len(specificity_checks))
    structure = _ratio(sum(1 for c in structure_checks if c in lower), len(structure_checks))
    bias_free = _ratio(sum(1 for c in safety_checks if c in lower), len(safety_checks))
    robustness = _ratio(sum(1 for c in robustness_checks if c in lower), len(robustness_checks))

    estimated_tokens = max(1, len(text) // 4)
    if 300 <= estimated_tokens <= 700:
        efficiency = 1.0
    elif 200 <= estimated_tokens <= 900:
        efficiency = 0.75
    elif 100 <= estimated_tokens <= 1100:
        efficiency = 0.5
    else:
        efficiency = 0.25

    return {
        "clarity": round(clarity, 3),
        "specificity": round(specificity, 3),
        "structure": round(structure, 3),
        "bias_free": round(bias_free, 3),
        "robustness": round(robustness, 3),
        "efficiency": round(efficiency, 3),
    }


def agent_profile_criteria_scores(profile: Dict[str, object], file_index: Iterable[str]) -> Dict[str, float]:
    """Return normalized criterion scores for agent profile quality."""
    files = set(file_index)
    prompts = profile.get("prompts", {}) if isinstance(profile, dict) else {}

    clarity = 1.0 if isinstance(profile.get("description"), str) and len(str(profile.get("description"))) >= 24 else 0.4

    logic_checks = [
        isinstance(profile.get("name"), str),
        isinstance(profile.get("title"), str),
        isinstance(profile.get("type"), str),
        isinstance(profile.get("version"), str),
    ]
    logic = _ratio(sum(1 for check in logic_checks if check), len(logic_checks))

    tools = 1.0 if "prompts/tools.md" in files else 0.6 if isinstance(prompts, dict) else 0.3

    robustness_checks = [
        "_context.md" in files,
        "agent.json" in files,
        isinstance(prompts, dict) and "role" in prompts,
        isinstance(prompts, dict) and "override" in prompts,
    ]
    robustness = _ratio(sum(1 for check in robustness_checks if check), len(robustness_checks))

    optimization = 1.0 if _contains_any("\n".join(files).lower(), ["testing", "qa", "validation"]) else 0.6

    return {
        "clarity": round(clarity, 3),
        "logic": round(logic, 3),
        "tools": round(tools, 3),
        "robustness": round(robustness, 3),
        "optimization": round(optimization, 3),
    }


def packaging_criteria_scores(manifest: Dict[str, object]) -> Dict[str, float]:
    """Return normalized criterion scores for package quality."""
    artifact_count = int(manifest.get("artifact_count", 0))
    missing = manifest.get("missing_required_artifacts", [])
    required = manifest.get("required_artifacts", [])

    clarity = 1.0 if artifact_count >= 3 else 0.5
    structure = 1.0 if artifact_count >= len(required) and len(required) > 0 else 0.6
    compliance = 1.0 if "README.md" in manifest.get("artifacts", []) else 0.6
    robustness = 1.0 if not missing else max(0.2, 1.0 - _ratio(len(missing), max(1, len(required))))

    return {
        "clarity": round(clarity, 3),
        "structure": round(structure, 3),
        "compliance": round(compliance, 3),
        "robustness": round(robustness, 3),
    }
