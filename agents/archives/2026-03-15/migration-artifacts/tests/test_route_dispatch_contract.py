"""Golden-style routing contract tests using fixed route fixtures."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = AGENTS_ROOT / "tests" / "fixtures" / "routes"
DISPATCH_SCRIPT = AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"
HELPER_SCRIPT = AGENTS_ROOT / "agent0" / "scripts" / "routed_call_helper.py"


class RouteDispatchContractTests(unittest.TestCase):
    def _run_dispatch(self, domain: str, intent: str, payload: dict[str, object]) -> dict[str, object]:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False) as temp:
            temp_path = Path(temp.name)
            json.dump(payload, temp)
        try:
            cmd = [sys.executable, str(DISPATCH_SCRIPT), "--domain", domain, "--payload-file", str(temp_path)]
            if intent:
                cmd.extend(["--intent", intent])
            completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(completed.stdout)
        finally:
            temp_path.unlink(missing_ok=True)

    def _run_helper(self, domain: str, intent: str, payload: dict[str, object]) -> dict[str, object]:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False) as temp:
            temp_path = Path(temp.name)
            json.dump(payload, temp)
        try:
            cmd = [
                sys.executable,
                str(HELPER_SCRIPT),
                "--domain",
                domain,
                "--intent",
                intent,
                "--payload-file",
                str(temp_path),
                "--execute",
            ]
            completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return json.loads(completed.stdout)
        finally:
            temp_path.unlink(missing_ok=True)

    def test_dispatch_and_helper_contracts_for_all_fixtures(self) -> None:
        for fixture in sorted(FIXTURES_DIR.glob("*.json")):
            route = json.loads(fixture.read_text(encoding="utf-8"))
            domain = route["domain"]
            intent = route.get("intent", "")
            payload = route.get("payload", {})

            dispatch_result = self._run_dispatch(domain, intent, payload)
            self.assertEqual(dispatch_result.get("domain"), domain, msg=f"dispatch mismatch for {fixture.name}")
            self.assertIn("output", dispatch_result, msg=f"dispatch missing output for {fixture.name}")
            if domain == "research":
                output = dispatch_result["output"]
                self.assertIn("niche_ranking_table", output, msg="research output missing niche_ranking_table")
                self.assertGreaterEqual(len(output["niche_ranking_table"]), 1, msg="research niche table is empty")
            if domain == "infrastructure":
                output = dispatch_result["output"]
                self.assertIn("ownership", output, msg="infrastructure output missing ownership")
                self.assertIn("handoff_contracts", output, msg="infrastructure output missing handoff_contracts")
                self.assertIn("extras", output, msg="infrastructure output missing extras")
                if payload.get("mode") == "agent-build":
                    self.assertIn("agent_profile_scaffold", output["extras"], msg="agent-build scaffold missing")
            if domain == "content":
                output = dispatch_result["output"]
                self.assertIn("production_plan", output, msg="content output missing production_plan")
                self.assertIn("pdf_export", output["production_plan"], msg="content production plan missing pdf_export")

            helper_result = self._run_helper(domain, intent, payload)
            self.assertEqual(helper_result.get("profile"), "agent0", msg=f"helper profile mismatch for {fixture.name}")
            self.assertTrue(
                str(helper_result.get("message", "")).startswith("ROUTE_DOMAIN_V1:"),
                msg=f"helper message prefix mismatch for {fixture.name}",
            )
            self.assertIn("dispatch_result", helper_result, msg=f"helper missing dispatch_result for {fixture.name}")
            self.assertEqual(
                helper_result["dispatch_result"].get("domain"),
                domain,
                msg=f"helper dispatch mismatch for {fixture.name}",
            )


if __name__ == "__main__":
    unittest.main()
