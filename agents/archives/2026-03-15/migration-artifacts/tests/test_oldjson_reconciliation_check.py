"""Tests for old.json capability reconciliation."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


AGENTS_ROOT = Path(__file__).resolve().parents[1]


class OldJsonReconciliationTests(unittest.TestCase):
    def test_oldjson_capabilities_are_covered(self) -> None:
        module_path = AGENTS_ROOT / "scripts" / "oldjson_reconciliation_check.py"
        spec = importlib.util.spec_from_file_location("oldjson_reconciliation_check", module_path)
        if spec is None or spec.loader is None:
            self.fail("Could not load oldjson_reconciliation_check")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        report = module.run()
        self.assertTrue(report["all_old_agents_covered"], msg=f"Missing mappings: {report['missing_from_coverage']}")


if __name__ == "__main__":
    unittest.main()

