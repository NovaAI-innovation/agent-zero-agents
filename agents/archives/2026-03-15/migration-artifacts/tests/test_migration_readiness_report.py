"""Tests for migration readiness reporting utility."""

from __future__ import annotations

import unittest
import importlib.util
from pathlib import Path


class MigrationReadinessReportTests(unittest.TestCase):
    def test_report_shape(self) -> None:
        module_path = Path(__file__).resolve().parents[1] / "scripts" / "migration_readiness_report.py"
        spec = importlib.util.spec_from_file_location("migration_readiness_report", module_path)
        if spec is None or spec.loader is None:
            self.fail("Could not load migration_readiness_report module spec")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        build_report = module.build_report

        report = build_report()
        self.assertIn("total_checks", report)
        self.assertIn("passed_checks", report)
        self.assertIn("checks", report)
        self.assertGreaterEqual(report["total_checks"], report["passed_checks"])
        self.assertIsInstance(report["legacy_modes"], dict)


if __name__ == "__main__":
    unittest.main()
