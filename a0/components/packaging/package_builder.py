"""Package manifest and assembly helpers."""

from __future__ import annotations

from typing import Dict, List


REQUIRED_ARTIFACTS = {
    "prompt_pack": [
        "EVAL_OVERVIEW.md",
        "README.md",
        "listing.md",
    ],
    "notion_template_pack": [
        "blueprint.md",
        "build-guide.md",
        "README.md",
        "listing.md",
        "cover-prompt.txt",
        "qa-checklist.md",
    ],
    "course_pack": [
        "README.md",
        "sales_page.md",
        "pricing_strategy.json",
        "content_modules.json",
        "assessments.json",
        "multimedia_manifest.json",
        "delivery_manifest.json",
    ],
}


SUPPORTED_PACKAGE_TYPES = sorted(REQUIRED_ARTIFACTS.keys())


def build_manifest(package_type: str, artifacts: List[str]) -> Dict[str, object]:
    """Return a package manifest with requirement coverage."""
    required = REQUIRED_ARTIFACTS.get(package_type, [])
    artifact_set = set(artifacts)
    missing = [name for name in required if name not in artifact_set]

    return {
        "package_type": package_type,
        "artifacts": artifacts,
        "artifact_count": len(artifacts),
        "required_artifacts": required,
        "missing_required_artifacts": missing,
        "complete": len(missing) == 0,
        "supported_package_types": SUPPORTED_PACKAGE_TYPES,
    }
