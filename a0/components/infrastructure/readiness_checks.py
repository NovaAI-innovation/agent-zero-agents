"""Infrastructure readiness check helpers."""

from __future__ import annotations

from typing import Dict


def evaluate_readiness(environment: str) -> Dict[str, bool]:
    """Return baseline readiness checks for a target environment."""
    normalized_env = environment.lower().strip()
    is_prod = normalized_env == "production"
    return {
        "repo_clean_enough": not is_prod,
        "tests_available": True,
        "deployment_config_present": True,
    }
