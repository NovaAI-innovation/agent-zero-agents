"""Reconcile archived old.json capabilities against migration coverage mapping."""

from __future__ import annotations

import json
import re
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
OLD_JSON_PATH = AGENTS_ROOT / "archives" / "2026-03-15" / "old.json"
COVERAGE_PATH = AGENTS_ROOT / "MIGRATION_FUNCTIONAL_COVERAGE.md"


def _load_old_agent_names() -> list[str]:
    lines = OLD_JSON_PATH.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].strip() == "old.json":
        lines = lines[1:]
    payload = json.loads("\n".join(lines))
    return sorted(payload.get("agents", {}).keys())


def _load_coverage_agent_names() -> list[str]:
    text = COVERAGE_PATH.read_text(encoding="utf-8")
    pattern = re.compile(r"^\|\s*`([^`]+)`\s*\|", re.MULTILINE)
    return sorted(set(pattern.findall(text)))


def run() -> dict[str, object]:
    old_agents = _load_old_agent_names()
    covered_agents = _load_coverage_agent_names()

    missing = sorted([name for name in old_agents if name not in covered_agents])
    extra = sorted([name for name in covered_agents if name not in old_agents])
    return {
        "old_agent_count": len(old_agents),
        "covered_agent_count": len(covered_agents),
        "missing_from_coverage": missing,
        "extra_in_coverage": extra,
        "all_old_agents_covered": len(missing) == 0,
    }


def main() -> None:
    import json as _json

    print(_json.dumps(run(), indent=2))


if __name__ == "__main__":
    main()

