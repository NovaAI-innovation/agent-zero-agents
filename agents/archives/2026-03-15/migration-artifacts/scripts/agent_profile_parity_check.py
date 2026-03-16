"""Agent profile evaluation parity sampling for quality cutover decisions."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[2]


def _file_index(profile_dir: Path) -> list[str]:
    return [
        str(path.relative_to(profile_dir)).replace("\\", "/")
        for path in profile_dir.rglob("*")
        if path.is_file()
    ]


def run() -> dict[str, object]:
    import sys

    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))

    from a0.components.quality.evaluator import evaluate_agent_profile

    sample_agents = ["quality", "packaging", "course", "research", "content"]
    results = []
    all_expected = True

    for name in sample_agents:
        profile_dir = AGENTS_ROOT / name
        profile = json.loads((profile_dir / "agent.json").read_text(encoding="utf-8"))
        report = evaluate_agent_profile(profile, _file_index(profile_dir))
        passed = bool(report.get("passed", False))
        expected = True
        all_expected = all_expected and (passed == expected)
        results.append({"sample": name, "passed": passed, "expected": expected})

    with tempfile.TemporaryDirectory() as tmp:
        bad_dir = Path(tmp)
        bad_profile = {
            "name": "broken",
            "title": "",
            "description": "",
            "type": "specialized",
            "version": "1.0.0",
            "prompts": {"role": "prompts/role.md", "override": "prompts/override.md"},
        }
        report = evaluate_agent_profile(bad_profile, ["agent.json"])
        passed = bool(report.get("passed", False))
        expected = False
        all_expected = all_expected and (passed == expected)
        results.append({"sample": "synthetic-broken-profile", "passed": passed, "expected": expected})

    return {"sample_count": len(results), "all_expected": all_expected, "results": results}


def main() -> None:
    print(json.dumps(run(), indent=2))


if __name__ == "__main__":
    main()

