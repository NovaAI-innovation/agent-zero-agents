"""Routing policy compliance tests."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
TARGET_DOMAINS = ("quality", "packaging", "course", "research", "branding", "content", "infrastructure")


class RoutingPolicyTests(unittest.TestCase):
    def test_no_direct_domain_profile_subordinate_calls(self) -> None:
        pattern = re.compile(
            r"call_subordinate\s*\(?\s*profile\s*=\s*['\"](" + "|".join(TARGET_DOMAINS) + r")['\"]",
            re.IGNORECASE,
        )
        excluded_names = {
            "new-structure.md",
            "prompts-index.md",
            "MIGRATION_STATUS.md",
            "migration_smoke_tests.py",
            "test_routing_policy.py",
        }
        scan_files = [
            p for p in AGENTS_ROOT.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".json", ".py"}
        ]
        violations: list[str] = []

        for file_path in scan_files:
            if file_path.name in excluded_names:
                continue
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            if pattern.search(content):
                violations.append(str(file_path))

        self.assertEqual(
            violations,
            [],
            msg="Found direct domain profile subordinate calls:\n" + "\n".join(violations),
        )


if __name__ == "__main__":
    unittest.main()
