"""PDF export planning helpers for Content domain."""

from __future__ import annotations

from typing import Dict


def pdf_export_plan(topic: str) -> Dict[str, object]:
    slug = "-".join(topic.lower().split())
    return {
        "output_file": f"{slug}-sale-ready.pdf",
        "layout": "print-first",
        "branding_required": True,
    }
