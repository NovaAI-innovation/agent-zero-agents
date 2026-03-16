"""Research parity-oriented edge case tests."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = AGENTS_ROOT / "tests" / "fixtures" / "routes"


class ResearchParityCaseTests(unittest.TestCase):
    def test_sparse_and_mixed_research_fixtures(self) -> None:
        from a0.components.research.market_analyzer import normalize_signal
        from a0.components.research.synthesizer import synthesize

        for fixture_name in ("research_sparse.json", "research_mixed.json"):
            payload = json.loads((FIXTURES_DIR / fixture_name).read_text(encoding="utf-8"))
            raw_signals = payload["payload"]["signals"]
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
            self.assertIn("ranking", report, f"{fixture_name} missing ranking")
            self.assertIn("niche_ranking_table", report, f"{fixture_name} missing niche table")
            self.assertGreaterEqual(len(report["niche_ranking_table"]), 1, f"{fixture_name} empty niche table")
            self.assertIn("recommendations", report, f"{fixture_name} missing recommendations")
            first_row = report["niche_ranking_table"][0]
            for key in ("niche", "signal_strength", "competition", "price_range", "confidence"):
                self.assertIn(key, first_row, f"{fixture_name} missing key {key}")


if __name__ == "__main__":
    unittest.main()

