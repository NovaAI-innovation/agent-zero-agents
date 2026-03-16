"""Packaging domain runtime entrypoint backed by shared components."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from a0.components.packaging.documentation_gen import build_docs_bundle  # noqa: E402
from a0.components.packaging.eval_integrator import quality_check_request  # noqa: E402
from a0.components.packaging.marketplace_lister import build_listing_bundle  # noqa: E402
from a0.components.packaging.package_builder import SUPPORTED_PACKAGE_TYPES, build_manifest  # noqa: E402
from a0.components.packaging.validator import validate_package  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Packaging domain builder CLI.")
    parser.add_argument("--package-type", required=True, help="Package type (e.g. prompt_pack).")
    parser.add_argument("--product-name", required=True, help="Product name.")
    parser.add_argument("--niche", required=True, help="Niche description.")
    parser.add_argument("--audience", required=True, help="Target audience.")
    parser.add_argument(
        "--artifacts",
        required=True,
        nargs="+",
        help="Artifact names (space-separated).",
    )
    parser.add_argument(
        "--outcomes",
        nargs="*",
        default=["better quality", "faster delivery"],
        help="Outcome statements.",
    )
    parser.add_argument(
        "--assumptions",
        nargs="*",
        default=["Environment has Python 3.10+", "User can edit markdown files"],
        help="Assumptions for docs.",
    )
    parser.add_argument(
        "--setup-steps",
        nargs="*",
        default=["Review README.md", "Follow build guide", "Run quality checks"],
        help="Setup steps for docs.",
    )
    parser.add_argument("--output", help="Optional JSON output path.")
    args = parser.parse_args()

    validation = validate_package(args.package_type, args.artifacts)
    manifest = validation["manifest"]
    listing = build_listing_bundle(
        product_name=args.product_name,
        niche=args.niche,
        audience=args.audience,
        outcomes=args.outcomes,
        deliverables=args.artifacts,
    )
    docs = build_docs_bundle(
        product_name=args.product_name,
        artifacts=args.artifacts,
        assumptions=args.assumptions,
        setup_steps=args.setup_steps,
    )
    quality_request = quality_check_request(manifest)

    result = {
        "supported_package_types": SUPPORTED_PACKAGE_TYPES,
        "manifest": manifest,
        "validation": validation,
        "listing": listing,
        "docs": docs,
        "quality_request": quality_request,
    }

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
