"""Focused unit tests for migrated domain components."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = AGENTS_ROOT.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


class DomainComponentTests(unittest.TestCase):
    def test_quality_rubric_loads_and_evaluates(self) -> None:
        from a0.components.quality.evaluator import evaluate, load_rubric

        rubric = load_rubric("prompt-eval")
        self.assertIn("criteria", rubric)
        report = evaluate(
            "prompt-eval",
            {
                "clarity": 0.9,
                "specificity": 0.85,
                "structure": 0.8,
                "bias_free": 0.9,
                "robustness": 0.85,
                "efficiency": 0.8,
            },
        )
        self.assertIn("overall_score", report)
        self.assertIn("passed", report)

    def test_packaging_schema_validation(self) -> None:
        from a0.components.packaging.validator import validate_package

        valid_report = validate_package("prompt_pack", ["README.md", "listing.md", "EVAL_OVERVIEW.md"])
        self.assertTrue(valid_report["valid"])

        invalid_report = validate_package("prompt_pack", ["README", "listing.md", "listing.md"])
        self.assertFalse(invalid_report["valid"])
        self.assertGreater(len(invalid_report["errors"]), 0)

    def test_course_stage_contract_validation(self) -> None:
        from a0.components.course.stage_contracts import validate_stage_input

        valid_payload = {
            "course_id": "course-001",
            "artifacts": {},
            "topic": "Python",
            "audience": "Beginners",
        }
        valid = validate_stage_input("blueprint", valid_payload)
        self.assertTrue(valid["valid"])

        invalid_payload = {"course_id": "course-001", "artifacts": {}}
        invalid = validate_stage_input("blueprint", invalid_payload)
        self.assertFalse(invalid["valid"])
        self.assertIn("topic", invalid["missing"])

    def test_research_ranking_is_deterministic(self) -> None:
        from a0.components.research.synthesizer import synthesize
        from a0.components.research.trend_scorer import rank_categories

        stats = {
            "prompts": {"count": 12, "avg_price": 59, "confidence": 0.9},
            "templates": {"count": 6, "avg_price": 39, "confidence": 0.8},
            "workflows": {"count": 3, "avg_price": 129, "confidence": 0.7},
        }
        first = rank_categories(stats)
        second = rank_categories(stats)
        self.assertEqual(first, second)
        self.assertEqual(list(first.keys())[0], "prompts")

        signals = [
            {
                "title": "Offer A",
                "category": "prompts",
                "price_usd": 49.0,
                "source": "gumroad",
                "creator": "Creator One",
                "sales_badges": ["bestseller"],
                "unknown_fields": [],
            },
            {
                "title": "Offer B",
                "category": "templates",
                "price_usd": 79.0,
                "source": "gumroad",
                "creator": "Creator Two",
                "sales_badges": ["trending"],
                "unknown_fields": [],
            },
        ]
        synthesized = synthesize(signals)
        self.assertIn("niche_ranking_table", synthesized)
        self.assertGreaterEqual(len(synthesized["niche_ranking_table"]), 1)
        self.assertIn("signal_strength", synthesized["niche_ranking_table"][0])

    def test_content_shared_components(self) -> None:
        from content.scripts.orchestrate_content import orchestrate
        from a0.components.content.asset_manager import build_asset_manifest
        from a0.components.content.quality_checks import evaluate_content_quality
        from a0.components.content.workflow_orchestrator import orchestrate_workflow

        workflow = orchestrate_workflow("Python Automation", "Beginners", "YouTube")
        self.assertEqual(workflow["stage_count"], 7)
        self.assertIn("script", workflow["stages"])
        self.assertIn("pdf_export", workflow["stages"])
        self.assertIn("distribution", workflow["stages"])

        manifest = build_asset_manifest("Python Automation", "YouTube")
        self.assertTrue(manifest["script"].endswith(".md"))
        self.assertTrue(manifest["pdf_export"].endswith(".pdf"))
        gates = evaluate_content_quality(manifest)
        self.assertTrue(all(gates.values()))
        runtime_payload = orchestrate("Python Automation", "Beginners", "YouTube")
        self.assertIn("production_plan", runtime_payload)
        self.assertIn("publish", runtime_payload["production_plan"])

    def test_infrastructure_shared_components(self) -> None:
        from infrastructure.scripts.execute_ops import execute_ops
        from a0.components.infrastructure.ops_planner import build_operation_plan
        from a0.components.infrastructure.contracts import domain_boundaries, handoff_contracts
        from a0.components.infrastructure.agent_profile_builder import scaffold_agent_profile, validate_scaffold
        from a0.components.infrastructure.readiness_checks import evaluate_readiness
        from a0.components.infrastructure.safety_gates import assess_risks

        checks = evaluate_readiness("staging")
        self.assertTrue(checks["tests_available"])
        plan = build_operation_plan("application", "staging")
        self.assertIn("run-unit-tests", plan)
        risks = assess_risks(checks)
        self.assertGreater(len(risks), 0)
        boundaries = domain_boundaries()
        self.assertIn("developer", boundaries)
        self.assertIn("hacker", boundaries)
        self.assertIn("infrastructure", boundaries)
        contracts = handoff_contracts()
        self.assertIn("developer_to_infrastructure", contracts)
        self.assertIn("hacker_to_infrastructure", contracts)
        scaffold = scaffold_agent_profile("demo-agent", "Demo Agent", "Demo description", "general")
        scaffold_validation = validate_scaffold(scaffold)
        self.assertTrue(scaffold_validation["valid"])
        runtime_payload = execute_ops("application", "staging", "agent-build")
        self.assertIn("agent_profile_scaffold", runtime_payload["extras"])


if __name__ == "__main__":
    unittest.main()
