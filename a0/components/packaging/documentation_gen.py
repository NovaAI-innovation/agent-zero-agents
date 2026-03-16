"""Documentation helpers for packaged outputs."""

from typing import Dict, List


def build_usage_notes(artifacts: List[str], assumptions: List[str]) -> Dict[str, object]:
    """Create concise usage notes payload for delivery docs."""
    return {
        "artifacts": artifacts,
        "assumptions": assumptions,
    }


def build_docs_bundle(
    product_name: str,
    artifacts: List[str],
    assumptions: List[str],
    setup_steps: List[str],
) -> Dict[str, str]:
    """Generate baseline docs aligned with packaging standards."""
    readme_lines = [
        f"# {product_name}",
        "",
        "## Included Artifacts",
    ] + [f"- {artifact}" for artifact in artifacts]

    guide_lines = [
        "# Build Guide",
        "",
        "## Setup Steps",
    ] + [f"{i + 1}. {step}" for i, step in enumerate(setup_steps)]

    assumptions_lines = [
        "# Assumptions",
        "",
    ] + [f"- {item}" for item in assumptions]

    return {
        "README.md": "\n".join(readme_lines).strip() + "\n",
        "build-guide.md": "\n".join(guide_lines).strip() + "\n",
        "assumptions.md": "\n".join(assumptions_lines).strip() + "\n",
    }
