"""Template-pack parity sampling for notion-template successor path."""

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

    from a0.components.packaging.documentation_gen import build_docs_bundle
    from a0.components.packaging.marketplace_lister import build_listing_bundle
    from a0.components.packaging.validator import validate_package

    samples = [
        ("Creator OS", "Productivity", "Solo creators"),
        ("Team Dashboard", "Operations", "Small teams"),
        ("Freelancer CRM", "Sales", "Freelancers"),
        ("Study Vault", "Education", "Students"),
        ("Launch Planner", "Marketing", "Indie founders"),
    ]

    results = []
    all_passed = True
    required_docs = {"README.md", "build-guide.md", "assumptions.md"}
    for i, (product, niche, audience) in enumerate(samples, start=1):
        artifacts = [
            "README.md",
            "listing.md",
            "blueprint.md",
            "build-guide.md",
            "cover-prompt.txt",
            "qa-checklist.md",
        ]
        validation = validate_package("notion_template_pack", artifacts)
        listing = build_listing_bundle(
            product_name=product,
            niche=niche,
            audience=audience,
            outcomes=["faster setup", "clear execution"],
            deliverables=artifacts,
        )
        docs = build_docs_bundle(
            product_name=product,
            artifacts=artifacts,
            assumptions=["Notion workspace access"],
            setup_steps=["Duplicate template", "Configure properties", "Run QA checklist"],
        )
        docs_ok = required_docs.issubset(set(docs.keys()))
        listing_ok = all(key in listing for key in ["title", "hook", "audience", "outcomes", "features", "deliverables", "faq"])
        passed = bool(validation.get("valid", False) and docs_ok and listing_ok)
        all_passed = all_passed and passed
        results.append(
            {
                "sample_id": i,
                "product_name": product,
                "validation_passed": bool(validation.get("valid", False)),
                "docs_ok": docs_ok,
                "listing_ok": listing_ok,
                "passed": passed,
            }
        )

    return {
        "sample_count": len(samples),
        "passed_count": sum(1 for r in results if r["passed"]),
        "all_passed": all_passed,
        "results": results,
    }


def main() -> None:
    print(json.dumps(run(), indent=2))


if __name__ == "__main__":
    main()

