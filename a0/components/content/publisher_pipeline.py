"""Publishing/distribution planning helpers for Content domain."""

from __future__ import annotations

from typing import Dict, List


def publish_plan(channel: str) -> Dict[str, object]:
    normalized = channel.lower().strip()
    hashtags: List[str] = ["#creator", "#digitalproducts", "#buildinpublic"]
    return {
        "channel": normalized,
        "checklist": ["title-optimized", "thumbnail-ready", "description-with-cta", "scheduled-release"],
        "distribution": [normalized, "crosspost-short-form", "newsletter-blast"],
        "hashtags": hashtags,
    }
