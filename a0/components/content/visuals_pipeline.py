"""Visual planning helpers for Content domain."""

from __future__ import annotations

from typing import Dict, List


def visuals_plan(topic: str) -> Dict[str, object]:
    shots: List[str] = [
        "establishing-broll",
        "on-screen-annotation",
        "comparison-graphic",
        "results-overlay",
    ]
    return {
        "topic": topic,
        "shot_types": shots,
        "licensing": "royalty-free sources only",
    }
