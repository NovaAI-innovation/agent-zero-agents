"""Marketplace listing helpers for packaging workflows."""

from typing import Dict, List


def build_listing(title: str, summary: str, audience: str) -> Dict[str, str]:
    """Return normalized listing metadata."""
    return {
        "title": title.strip(),
        "summary": summary.strip(),
        "audience": audience.strip(),
    }


def build_listing_bundle(
    product_name: str,
    niche: str,
    audience: str,
    outcomes: List[str],
    deliverables: List[str],
) -> Dict[str, object]:
    """Build a listing bundle aligned with packer/template standards."""
    title = f"{product_name}: {niche}"
    hook = f"Production-ready system for {audience} to achieve {outcomes[0] if outcomes else 'faster results'}."
    features = [
        "Clear structure and implementation-ready artifacts",
        "Beginner-safe onboarding and usage guidance",
        "Quality validation integrated before delivery",
    ]
    faq = [
        {
            "q": "Is this beginner friendly?",
            "a": "Yes. The package includes setup and usage guidance with practical defaults.",
        },
        {
            "q": "Can I customize it for my workflow?",
            "a": "Yes. Artifacts are modular and can be adapted without breaking core structure.",
        },
    ]

    return {
        "title": title,
        "hook": hook,
        "audience": audience,
        "outcomes": outcomes,
        "features": features,
        "deliverables": deliverables,
        "faq": faq,
    }
