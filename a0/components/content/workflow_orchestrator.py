"""Content workflow orchestrator shared component."""

from __future__ import annotations

from typing import Dict, List


CONTENT_STAGES: List[str] = [
    "script",
    "visuals",
    "voice",
    "edit",
    "pdf_export",
    "publish",
    "distribution",
]


def orchestrate_workflow(topic: str, audience: str, channel: str) -> Dict[str, object]:
    """Return deterministic stage ordering and metadata for content workflows."""
    return {
        "topic": topic,
        "audience": audience,
        "channel": channel,
        "stages": CONTENT_STAGES,
        "stage_count": len(CONTENT_STAGES),
    }
