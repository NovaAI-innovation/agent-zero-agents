"""Tests for cutover guidance scripts."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


AGENTS_ROOT = Path(__file__).resolve().parents[1]


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load module spec: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CutoverGuideTests(unittest.TestCase):
    def test_packaging_cutover_check(self) -> None:
        module = _load_module(AGENTS_ROOT / "scripts" / "packaging_cutover_check.py", "packaging_cutover_check")
        summary = module.run()
        self.assertEqual(summary["sample_count"], 10)
        self.assertEqual(summary["passed_count"], 10)
        self.assertTrue(summary["all_passed"])

    def test_research_legacy_parity_check(self) -> None:
        module = _load_module(AGENTS_ROOT / "scripts" / "research_legacy_parity_check.py", "research_legacy_parity_check")
        summary = module.run()
        self.assertGreaterEqual(summary["fixture_count"], 3)
        self.assertTrue(summary["all_passed"])

    def test_notion_template_parity_check(self) -> None:
        module = _load_module(AGENTS_ROOT / "scripts" / "notion_template_parity_check.py", "notion_template_parity_check")
        summary = module.run()
        self.assertEqual(summary["sample_count"], 5)
        self.assertEqual(summary["passed_count"], 5)
        self.assertTrue(summary["all_passed"])

    def test_agent_profile_parity_check(self) -> None:
        module = _load_module(AGENTS_ROOT / "scripts" / "agent_profile_parity_check.py", "agent_profile_parity_check")
        summary = module.run()
        self.assertGreaterEqual(summary["sample_count"], 6)
        self.assertTrue(summary["all_expected"])


if __name__ == "__main__":
    unittest.main()
