"""Schema checks for route fixture payloads."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = AGENTS_ROOT / "tests" / "fixtures" / "routes"
ALLOWED_DOMAINS = {"quality", "packaging", "course", "research", "branding", "content", "infrastructure"}

DOMAIN_REQUIRED_KEYS = {
    "quality": {"mode"},
    "packaging": {"package_type", "product_name", "niche", "audience", "artifacts"},
    "course": {"topic", "audience", "module_count"},
    "research": {"signals"},
    "branding": {"niche", "audience", "product_name"},
    "content": {"topic", "audience", "channel"},
    "infrastructure": {"target", "environment", "mode"},
}


class RouteFixtureSchemaTests(unittest.TestCase):
    def test_route_fixtures_have_required_structure(self) -> None:
        fixture_files = sorted(FIXTURES_DIR.glob("*.json"))
        self.assertGreater(len(fixture_files), 0, "No route fixtures found")

        for fixture in fixture_files:
            data = json.loads(fixture.read_text(encoding="utf-8"))
            self.assertIsInstance(data, dict, f"{fixture.name} must be an object")
            self.assertIn("domain", data, f"{fixture.name} missing domain")
            self.assertIn("payload", data, f"{fixture.name} missing payload")
            self.assertIsInstance(data.get("payload"), dict, f"{fixture.name} payload must be object")
            self.assertIn(data["domain"], ALLOWED_DOMAINS, f"{fixture.name} has unknown domain")

            if "intent" in data:
                self.assertIsInstance(data["intent"], str, f"{fixture.name} intent must be string")

            required_keys = DOMAIN_REQUIRED_KEYS[data["domain"]]
            payload_keys = set(data["payload"].keys())
            missing = sorted(required_keys - payload_keys)
            self.assertEqual(missing, [], f"{fixture.name} missing payload keys: {missing}")
            if data["domain"] == "research":
                self.assertIsInstance(data["payload"]["signals"], list, f"{fixture.name} signals must be a list")
                self.assertGreater(len(data["payload"]["signals"]), 0, f"{fixture.name} signals list is empty")


if __name__ == "__main__":
    unittest.main()
