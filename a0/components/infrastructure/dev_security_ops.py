"""Developer and security operation planning helpers."""

from __future__ import annotations

from typing import Dict, List


def developer_ops_plan(task_type: str) -> List[str]:
    plans = {
        "feature": ["confirm-requirements", "implement-feature", "run-tests", "prepare-release-notes"],
        "bugfix": ["reproduce-issue", "apply-fix", "run-regression-tests", "document-root-cause"],
        "refactor": ["identify-risk-areas", "refactor-module", "run-full-tests", "update-docs"],
    }
    return plans.get(task_type, ["triage-task", "execute-change", "run-tests", "document-outcome"])


def security_ops_plan(scope: str) -> Dict[str, object]:
    checks = [
        "threat-model-review",
        "dependency-vulnerability-scan",
        "secret-exposure-check",
        "hardening-recommendations",
    ]
    return {
        "scope": scope,
        "checks": checks,
        "severity_policy": {"critical": "block", "high": "block", "medium": "review", "low": "monitor"},
    }
