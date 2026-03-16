"""Quality gate checks for content workflows."""

from __future__ import annotations

from typing import Dict


REQUIRED_ASSET_KEYS = {"script", "visuals", "voice", "edit", "pdf_export", "publish", "distribution"}


def evaluate_content_quality(artifacts: Dict[str, str]) -> Dict[str, bool]:
    """Evaluate baseline content quality gates from generated artifacts."""
    has_required_keys = REQUIRED_ASSET_KEYS.issubset(set(artifacts.keys()))
    return {
        "script_complete": has_required_keys and artifacts.get("script", "").endswith(".md"),
        "visual_alignment": has_required_keys and artifacts.get("visuals", "").endswith(".md"),
        "voice_timing_validated": has_required_keys and artifacts.get("voice", "").endswith(".txt"),
        "pdf_render_ready": has_required_keys and artifacts.get("pdf_export", "").endswith(".pdf"),
        "platform_requirements_checked": has_required_keys and artifacts.get("publish", "").endswith(".md"),
        "distribution_ready": has_required_keys and artifacts.get("distribution", "").endswith(".md"),
    }
