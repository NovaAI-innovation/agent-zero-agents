"""Integration contract between Packaging and Quality domains."""

from typing import Dict


RUBRIC_BY_PACKAGE_TYPE = {
    "prompt_pack": "packaging-default",
    "notion_template_pack": "packaging-default",
}


def quality_check_request(artifact_manifest: Dict[str, object], rubric: str | None = None) -> Dict[str, object]:
    """Build a normalized Quality-domain request payload."""
    package_type = str(artifact_manifest.get("package_type", ""))
    resolved_rubric = rubric or RUBRIC_BY_PACKAGE_TYPE.get(package_type, "packaging-default")
    return {
        "target": "quality",
        "operation": "evaluate_package",
        "rubric": resolved_rubric,
        "payload": artifact_manifest,
    }
