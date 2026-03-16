"""Infrastructure operation plan builder."""

from __future__ import annotations

from typing import List


def build_operation_plan(target: str, environment: str) -> List[str]:
    """Return deterministic plan steps for deployment readiness."""
    return [
        f"validate-{environment}-config",
        "run-unit-tests",
        "run-smoke-tests",
        f"prepare-{target}-deployment",
    ]
