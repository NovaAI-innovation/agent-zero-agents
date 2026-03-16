"""Safety gate and risk summaries for infrastructure actions."""

from __future__ import annotations

from typing import Dict, List


def assess_risks(checks: Dict[str, bool]) -> List[Dict[str, str]]:
    """Generate simple risk labels from readiness check results."""
    risks: List[Dict[str, str]] = []
    if not checks.get("repo_clean_enough", False):
        risks.append({"item": "repo cleanliness below release threshold", "level": "medium"})
    if not checks.get("tests_available", False):
        risks.append({"item": "tests unavailable", "level": "high"})
    if not checks.get("deployment_config_present", False):
        risks.append({"item": "deployment config missing", "level": "high"})
    if not risks:
        risks.append({"item": "no blocking risks detected", "level": "low"})
    return risks
