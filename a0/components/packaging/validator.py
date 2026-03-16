"""Validation helpers for packaging outputs."""

from __future__ import annotations

from typing import Dict

from .package_builder import build_manifest
from .schemas import validate_artifacts_list, validate_manifest_schema, validate_package_type


def validate_package(package_type: str, artifacts: list[str]) -> Dict[str, object]:
    """Validate package type, artifacts, and manifest schema."""
    type_ok, type_error = validate_package_type(package_type)
    artifact_validation = validate_artifacts_list(artifacts)

    manifest = build_manifest(package_type, artifacts)
    schema_validation = validate_manifest_schema(manifest)

    errors = []
    if not type_ok and type_error:
        errors.append(type_error)
    errors.extend(artifact_validation.get("errors", []))
    errors.extend(schema_validation.get("errors", []))

    valid = len(errors) == 0 and bool(manifest.get("complete", False))
    return {
        "valid": valid,
        "errors": errors,
        "type_ok": type_ok,
        "artifacts_ok": artifact_validation.get("valid", False),
        "schema_ok": schema_validation.get("valid", False),
        "manifest": manifest,
    }
