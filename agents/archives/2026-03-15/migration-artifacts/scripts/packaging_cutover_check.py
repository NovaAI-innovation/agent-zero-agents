"""Packaging cutover parity check for prompt-packer successor."""

from __future__ import annotations

import json
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def run() -> dict[str, object]:
    import sys

    repo_root = _repo_root()
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    from a0.components.packaging.validator import validate_package

    samples = [
        ("prompt_pack", ["README.md", "listing.md", "EVAL_OVERVIEW.md"]),
        ("prompt_pack", ["EVAL_OVERVIEW.md", "README.md", "listing.md"]),
        ("prompt_pack", ["README.md", "listing.md", "EVAL_OVERVIEW.md", "extras.md"]),
        ("notion_template_pack", ["README.md", "listing.md", "blueprint.md", "build-guide.md", "cover-prompt.txt", "qa-checklist.md"]),
        ("notion_template_pack", ["blueprint.md", "build-guide.md", "README.md", "listing.md", "cover-prompt.txt", "qa-checklist.md", "notes.txt"]),
        ("course_pack", ["README.md", "sales_page.md", "pricing_strategy.json", "content_modules.json", "assessments.json", "multimedia_manifest.json", "delivery_manifest.json"]),
        ("course_pack", ["README.md", "sales_page.md", "pricing_strategy.json", "content_modules.json", "assessments.json", "multimedia_manifest.json", "delivery_manifest.json", "appendix.md"]),
        ("prompt_pack", ["README.md", "listing.md", "EVAL_OVERVIEW.md", "usage-guide.md"]),
        ("notion_template_pack", ["README.md", "listing.md", "blueprint.md", "build-guide.md", "cover-prompt.txt", "qa-checklist.md", "faq.md"]),
        ("course_pack", ["README.md", "sales_page.md", "pricing_strategy.json", "content_modules.json", "assessments.json", "multimedia_manifest.json", "delivery_manifest.json", "changelog.md"]),
    ]

    results = []
    all_passed = True
    for index, (package_type, artifacts) in enumerate(samples, start=1):
        report = validate_package(package_type, artifacts)
        passed = bool(report.get("valid", False))
        all_passed = all_passed and passed
        results.append(
            {
                "sample_id": index,
                "package_type": package_type,
                "artifact_count": len(artifacts),
                "passed": passed,
                "errors": report.get("errors", []),
            }
        )

    summary = {
        "sample_count": len(samples),
        "passed_count": sum(1 for item in results if item["passed"]),
        "all_passed": all_passed,
        "results": results,
    }
    return summary


def main() -> None:
    summary = run()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

