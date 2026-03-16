"""Branding domain runtime entrypoint."""

from __future__ import annotations

import argparse
import json


def compose_brand(niche: str, audience: str, product_name: str) -> dict[str, object]:
    return {
        "positioning": {
            "tagline": f"{product_name}: practical {niche} outcomes for {audience}",
            "promise": "Clear outcomes, fast implementation, credible guidance.",
        },
        "voice": {
            "tone": ["clear", "practical", "confident"],
            "avoid": ["hype-heavy claims", "unclear jargon"],
        },
        "visual_direction": {
            "palette": ["#12324A", "#1F7A8C", "#F4F7FA", "#F2A541"],
            "typography": {"heading": "Poppins", "body": "Source Sans 3"},
            "motif": "structured cards with accent highlights",
            "svg_logo_guidance": {
                "wordmark_style": "geometric sans with balanced x-height",
                "icon_motif": "modular grid + forward motion accent",
                "stroke_width": "2px baseline for 24-48px exports",
            },
        },
        "asset_checklist": [
            "logo-wordmark.svg",
            "logo-icon.svg",
            "social-banner-1500x500.png",
            "palette-and-type-guide.md",
            "brand-voice-guide.md",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compose a deterministic brand kit summary.")
    parser.add_argument("--niche", default="General")
    parser.add_argument("--audience", default="General Audience")
    parser.add_argument("--product-name", default="Product")
    args = parser.parse_args()
    print(json.dumps(compose_brand(args.niche, args.audience, args.product_name), indent=2))


if __name__ == "__main__":
    main()
