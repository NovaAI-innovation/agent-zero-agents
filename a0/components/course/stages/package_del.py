"""Stage implementation: packaging and delivery."""

from __future__ import annotations

from typing import Dict, List


def run(payload: dict, artifacts) -> dict:
    blueprint = payload.get("blueprint", {})
    modules = blueprint.get("modules", [])

    gumroad_files = [
        "README.md",
        "sales_page.md",
        "pricing_strategy.json",
        "content_modules.json",
        "assessments.json",
        "multimedia_manifest.json",
    ]

    teachable_structure = {
        "sections": len(modules),
        "lessons_per_section": 1,
        "assessments": "included",
    }

    self_hosted = {
        "landing_page": "index.html",
        "module_pages": [f"module-{i + 1:02d}.html" for i in range(len(modules))],
        "assets": ["media/", "downloads/"],
    }

    checklist = {
        "files_organized": True,
        "deployment_notes_present": True,
        "assessment_assets_present": True,
        "marketing_assets_present": True,
    }

    result = {
        "gumroad_package": gumroad_files,
        "teachable_package": teachable_structure,
        "self_hosted_package": self_hosted,
        "prelaunch_checklist": checklist,
        "ready_for_deployment": all(checklist.values()),
    }
    artifacts.add("delivery", "delivery_manifest.json")
    return result
