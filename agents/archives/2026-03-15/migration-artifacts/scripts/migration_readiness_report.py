"""Generate a lightweight migration readiness report from repository artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List


AGENTS_ROOT = Path(__file__).resolve().parents[1]


def parse_deprecation_modes(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8")
    modes: Dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 3:
            continue
        legacy_agent = parts[0].strip("`")
        mode = parts[2]
        modes[legacy_agent] = mode
    return modes


def required_paths() -> List[Path]:
    return [
        AGENTS_ROOT / "quality" / "agent.json",
        AGENTS_ROOT / "packaging" / "agent.json",
        AGENTS_ROOT / "course" / "agent.json",
        AGENTS_ROOT / "research" / "agent.json",
        AGENTS_ROOT / "branding" / "agent.json",
        AGENTS_ROOT / "content" / "agent.json",
        AGENTS_ROOT / "infrastructure" / "agent.json",
        AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py",
        AGENTS_ROOT / "agent0" / "scripts" / "routed_call_helper.py",
        AGENTS_ROOT / "migration_smoke_tests.py",
        AGENTS_ROOT / "MIGRATION_STATUS.md",
        AGENTS_ROOT / "DEPRECATION_MATRIX.md",
        AGENTS_ROOT / "MIGRATION_TELEMETRY.md",
        AGENTS_ROOT / "MIGRATION_FUNCTIONAL_COVERAGE.md",
        AGENTS_ROOT / "archives" / "2026-03-15" / "README.md",
        AGENTS_ROOT / "scripts" / "oldjson_reconciliation_check.py",
    ]


def build_report() -> Dict[str, object]:
    dep_path = AGENTS_ROOT / "DEPRECATION_MATRIX.md"
    modes = parse_deprecation_modes(dep_path) if dep_path.exists() else {}

    checks = []
    for item in required_paths():
        checks.append({"path": str(item.relative_to(AGENTS_ROOT)).replace("\\", "/"), "exists": item.exists()})

    existing_count = sum(1 for item in checks if item["exists"])
    report = {
        "total_checks": len(checks),
        "passed_checks": existing_count,
        "missing_checks": len(checks) - existing_count,
        "legacy_modes": modes,
        "checks": checks,
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate migration readiness report.")
    parser.add_argument("--output", help="Optional output JSON path.")
    args = parser.parse_args()

    report = build_report()
    payload = json.dumps(report, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(payload, encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
