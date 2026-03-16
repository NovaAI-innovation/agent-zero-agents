"""Asset manifest helpers for content workflows."""

from __future__ import annotations

from typing import Dict


def _slug(value: str) -> str:
    return "-".join(value.lower().strip().split())


def build_asset_manifest(topic: str, channel: str) -> Dict[str, str]:
    """Return deterministic artifact naming for content outputs."""
    topic_slug = _slug(topic)
    channel_slug = _slug(channel)
    return {
        "script": f"{topic_slug}-script.md",
        "visuals": f"{topic_slug}-visual-plan.md",
        "voice": f"{topic_slug}-voiceover.txt",
        "edit": "edit-checklist.md",
        "pdf_export": f"{topic_slug}-sale-ready.pdf",
        "publish": f"{channel_slug}-publish-checklist.md",
        "distribution": f"{channel_slug}-distribution-plan.md",
    }
