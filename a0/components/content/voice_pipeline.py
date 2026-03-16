"""Voiceover planning helpers for Content domain."""

from __future__ import annotations

from typing import Dict


def voice_plan(style: str = "clear-confident") -> Dict[str, object]:
    return {
        "style": style,
        "pacing_wpm": 145,
        "emotion_profile": "engaged",
        "quality_gate": "no clipping, no long silence gaps",
    }
