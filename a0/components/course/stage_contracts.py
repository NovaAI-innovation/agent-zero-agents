"""Input/output contracts for Course domain stages."""

from __future__ import annotations

from typing import Dict, List


STAGE_ORDER: List[str] = [
    "blueprint",
    "content",
    "assessment",
    "multimedia",
    "marketing",
    "pricing",
    "validate",
    "delivery",
]


DEFAULT_REQUIRED = ["course_id", "artifacts"]


STAGE_REQUIRED: Dict[str, List[str]] = {
    "blueprint": ["topic", "audience"],
    "content": ["blueprint"],
    "assessment": ["modules"],
    "multimedia": ["modules"],
    "marketing": ["course_summary"],
    "pricing": ["positioning"],
    "validate": ["all_stage_outputs"],
    "delivery": ["validated_package"],
}


def stage_input_contract(stage: str) -> Dict[str, object]:
    """Return required and optional keys for a given stage input."""
    return {
        "required": DEFAULT_REQUIRED + STAGE_REQUIRED.get(stage, []),
        "optional": ["notes"],
    }


def validate_stage_input(stage: str, payload: Dict[str, object]) -> Dict[str, object]:
    """Validate stage payload keys and return status payload."""
    required = stage_input_contract(stage)["required"]
    missing = [key for key in required if key not in payload]
    return {
        "stage": stage,
        "valid": len(missing) == 0,
        "missing": missing,
    }
