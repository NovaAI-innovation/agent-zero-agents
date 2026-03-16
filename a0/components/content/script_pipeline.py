"""Script generation helpers for Content domain."""

from __future__ import annotations

from typing import Dict, List


def script_outline(topic: str, audience: str) -> Dict[str, object]:
    sections: List[str] = [
        "hook",
        "problem",
        "framework",
        "walkthrough",
        "cta",
    ]
    return {
        "topic": topic,
        "audience": audience,
        "sections": sections,
        "retention_strategy": "open-loop transitions every 20-30 seconds",
    }
