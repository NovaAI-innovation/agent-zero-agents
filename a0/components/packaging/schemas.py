"""Schema validation helpers for packaging manifests and artifacts."""

from __future__ import annotations

from typing import Dict, List, Tuple

from .package_builder import SUPPORTED_PACKAGE_TYPES


VALID_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".zip",
    ".pdf",
    ".html",
}


def validate_package_type(package_type: str) -> Tuple[bool, str | None]:
    if package_type not in SUPPORTED_PACKAGE_TYPES:
        return False, f"Unsupported package_type '{package_type}'. Supported: {', '.join(SUPPORTED_PACKAGE_TYPES)}"
    return True, None


def validate_artifacts_list(artifacts: List[str]) -> Dict[str, object]:
    errors: List[str] = []

    if not isinstance(artifacts, list) or not artifacts:
        errors.append("artifacts must be a non-empty list")
        return {"valid": False, "errors": errors}

    seen = set()
    for index, item in enumerate(artifacts):
        if not isinstance(item, str):
            errors.append(f"artifacts[{index}] must be a string")
            continue
        if item.strip() != item:
            errors.append(f"artifacts[{index}] contains leading/trailing whitespace")
        if "/" in item or "\\" in item:
            errors.append(f"artifacts[{index}] must be a filename, not a path")
        if item in seen:
            errors.append(f"duplicate artifact: {item}")
        seen.add(item)

        extension_ok = any(item.lower().endswith(ext) for ext in VALID_EXTENSIONS)
        if not extension_ok:
            errors.append(f"artifacts[{index}] has unsupported extension: {item}")

    return {"valid": len(errors) == 0, "errors": errors}


def validate_manifest_schema(manifest: Dict[str, object]) -> Dict[str, object]:
    errors: List[str] = []

    expected_keys = {
        "package_type",
        "artifacts",
        "artifact_count",
        "required_artifacts",
        "missing_required_artifacts",
        "complete",
        "supported_package_types",
    }
    missing_keys = [key for key in expected_keys if key not in manifest]
    if missing_keys:
        errors.append(f"manifest missing keys: {', '.join(sorted(missing_keys))}")

    if "artifact_count" in manifest and "artifacts" in manifest:
        if manifest["artifact_count"] != len(manifest.get("artifacts", [])):
            errors.append("artifact_count does not match number of artifacts")

    return {"valid": len(errors) == 0, "errors": errors}
