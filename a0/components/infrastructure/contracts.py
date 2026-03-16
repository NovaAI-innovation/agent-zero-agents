"""Infrastructure ownership boundaries and shared contracts."""

from __future__ import annotations

from typing import Dict, List


def domain_boundaries() -> Dict[str, List[str]]:
    """Return ownership boundaries for legacy infrastructure-related agents."""
    return {
        "developer": [
            "application code changes",
            "build and test automation",
            "dependency and runtime troubleshooting",
        ],
        "hacker": [
            "security review and threat modeling",
            "hardening recommendations",
            "vulnerability triage and exploit-risk analysis",
        ],
        "infrastructure": [
            "deployment readiness checks",
            "operational runbooks and rollout safety",
            "environment-level configuration validation",
        ],
    }


def handoff_contracts() -> Dict[str, Dict[str, List[str]]]:
    """Return expected input/output contracts for infra-domain handoffs."""
    return {
        "developer_to_infrastructure": {
            "inputs": ["test-results", "build-artifacts", "deployment-config"],
            "outputs": ["readiness-status", "operation-plan"],
        },
        "hacker_to_infrastructure": {
            "inputs": ["risk-findings", "severity-map", "recommended-controls"],
            "outputs": ["risk-acknowledgement", "mitigation-checklist"],
        },
    }
