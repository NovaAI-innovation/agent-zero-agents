"""Research legacy-parity sampling against consolidated research components."""

from __future__ import annotations

import json
from pathlib import Path


def _agents_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _legacy_contracts() -> dict[str, set[str]]:
    return {
        "researcher": {"ranking", "recommendations"},
        "gumroad-trend-analyzer": {"niche_ranking_table", "recommendations", "category_counts"},
    }


def run() -> dict[str, object]:
    import sys

    repo_root = _repo_root()
    agents_root = _agents_root()
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))

    from a0.components.research.market_analyzer import normalize_signal
    from a0.components.research.synthesizer import synthesize

    fixtures = sorted((agents_root / "tests" / "fixtures" / "routes").glob("research*.json"))
    contracts = _legacy_contracts()
    runs = []
    all_passed = True

    for fixture in fixtures:
        payload = json.loads(fixture.read_text(encoding="utf-8"))
        raw_signals = payload.get("payload", {}).get("signals", [])
        normalized = [
            normalize_signal(
                title=str(item.get("title", "")),
                category=str(item.get("category", "unknown")),
                price_usd=float(item.get("price_usd", 0.0)),
                source=str(item.get("source", "unknown")),
                creator=str(item.get("creator", "unknown")),
                sales_badge=item.get("sales_badge", item.get("sales_badges", [])),
                timeframe=str(item.get("timeframe", "unknown")),
            )
            for item in raw_signals
        ]
        report = synthesize(normalized)

        contract_results = {}
        for legacy_agent, required_fields in contracts.items():
            missing = sorted([field for field in required_fields if field not in report])
            passed = len(missing) == 0
            all_passed = all_passed and passed
            contract_results[legacy_agent] = {"passed": passed, "missing_fields": missing}

        runs.append(
            {
                "fixture": fixture.name,
                "signal_count": len(raw_signals),
                "top_category": report.get("top_category", "none"),
                "contract_results": contract_results,
            }
        )

    return {"fixture_count": len(fixtures), "all_passed": all_passed, "runs": runs}


def main() -> None:
    print(json.dumps(run(), indent=2))


if __name__ == "__main__":
    main()

