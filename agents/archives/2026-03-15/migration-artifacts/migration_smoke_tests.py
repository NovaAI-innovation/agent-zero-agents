"""Smoke tests for domain-migration scaffolding."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


AGENTS_ROOT = Path(__file__).resolve().parent
REPO_ROOT = AGENTS_ROOT.parent
COMPONENTS_ROOT = REPO_ROOT / "a0" / "components"

sys.path.insert(0, str(REPO_ROOT))


def assert_exists(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"Missing required path: {path}")


def run() -> None:
    required_paths = [
        AGENTS_ROOT / "quality" / "agent.json",
        AGENTS_ROOT / "quality" / "prompts" / "role.md",
        AGENTS_ROOT / "packaging" / "agent.json",
        AGENTS_ROOT / "packaging" / "prompts" / "role.md",
        AGENTS_ROOT / "course" / "agent.json",
        AGENTS_ROOT / "course" / "scripts" / "orchestrate.py",
        AGENTS_ROOT / "research" / "agent.json",
        AGENTS_ROOT / "research" / "scripts" / "analyze.py",
        AGENTS_ROOT / "branding" / "agent.json",
        AGENTS_ROOT / "branding" / "scripts" / "compose_brand.py",
        AGENTS_ROOT / "content" / "agent.json",
        AGENTS_ROOT / "content" / "scripts" / "orchestrate_content.py",
        AGENTS_ROOT / "infrastructure" / "agent.json",
        AGENTS_ROOT / "infrastructure" / "scripts" / "execute_ops.py",
        AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py",
        AGENTS_ROOT / "agent0" / "scripts" / "routed_call_helper.py",
        COMPONENTS_ROOT / "quality" / "evaluator.py",
        COMPONENTS_ROOT / "packaging" / "package_builder.py",
        COMPONENTS_ROOT / "packaging" / "schemas.py",
        COMPONENTS_ROOT / "course" / "orchestrator.py",
        COMPONENTS_ROOT / "course" / "stage_contracts.py",
        COMPONENTS_ROOT / "research" / "synthesizer.py",
        COMPONENTS_ROOT / "content" / "workflow_orchestrator.py",
        COMPONENTS_ROOT / "content" / "asset_manager.py",
        COMPONENTS_ROOT / "content" / "quality_checks.py",
        COMPONENTS_ROOT / "content" / "script_pipeline.py",
        COMPONENTS_ROOT / "content" / "visuals_pipeline.py",
        COMPONENTS_ROOT / "content" / "voice_pipeline.py",
        COMPONENTS_ROOT / "content" / "pdf_pipeline.py",
        COMPONENTS_ROOT / "content" / "publisher_pipeline.py",
        COMPONENTS_ROOT / "infrastructure" / "readiness_checks.py",
        COMPONENTS_ROOT / "infrastructure" / "ops_planner.py",
        COMPONENTS_ROOT / "infrastructure" / "safety_gates.py",
        COMPONENTS_ROOT / "infrastructure" / "contracts.py",
        COMPONENTS_ROOT / "infrastructure" / "agent_profile_builder.py",
        COMPONENTS_ROOT / "infrastructure" / "dev_security_ops.py",
        COMPONENTS_ROOT / "research" / "heuristics.py",
        AGENTS_ROOT / "LEGACY_ARCHIVE_CHECKLIST.md",
        AGENTS_ROOT / "MIGRATION_FUNCTIONAL_COVERAGE.md",
        AGENTS_ROOT / "scripts" / "migration_readiness_report.py",
        AGENTS_ROOT / "scripts" / "oldjson_reconciliation_check.py",
    ]
    for path in required_paths:
        assert_exists(path)

    readiness_run = subprocess.run(
        [sys.executable, str(AGENTS_ROOT / "scripts" / "migration_readiness_report.py")],
        capture_output=True,
        text=True,
        check=True,
    )
    readiness_payload = json.loads(readiness_run.stdout)
    if readiness_payload.get("missing_checks", 1) != 0:
        raise AssertionError("migration readiness report indicates missing required checks")

    reconciliation_run = subprocess.run(
        [sys.executable, str(AGENTS_ROOT / "scripts" / "oldjson_reconciliation_check.py")],
        capture_output=True,
        text=True,
        check=True,
    )
    reconciliation_payload = json.loads(reconciliation_run.stdout)
    if not reconciliation_payload.get("all_old_agents_covered", False):
        raise AssertionError(
            "old.json reconciliation failed; missing mappings: "
            + ",".join(reconciliation_payload.get("missing_from_coverage", []))
        )

    # Guard: disallow direct domain profile subordinate calls in prompts/docs,
    # so routing remains centralized through agent0.
    banned_patterns = [
        "call_subordinate(profile='quality'",
        'call_subordinate(profile="quality"',
        "call_subordinate(profile='packaging'",
        'call_subordinate(profile="packaging"',
        "call_subordinate(profile='course'",
        'call_subordinate(profile="course"',
        "call_subordinate(profile='research'",
        'call_subordinate(profile="research"',
    ]
    scan_files = [
        p
        for p in AGENTS_ROOT.rglob("*")
        if p.is_file() and p.suffix.lower() in {".md", ".json"}
    ]
    excluded_names = {"new-structure.md", "prompts-index.md", "MIGRATION_STATUS.md"}
    for file_path in scan_files:
        if file_path.name in excluded_names:
            continue
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        for pattern in banned_patterns:
            if pattern in content:
                raise AssertionError(f"Banned direct domain routing pattern found in {file_path}: {pattern}")

    quality_agent = json.loads((AGENTS_ROOT / "quality" / "agent.json").read_text(encoding="utf-8"))
    packaging_agent = json.loads((AGENTS_ROOT / "packaging" / "agent.json").read_text(encoding="utf-8"))
    if quality_agent["name"] != "quality":
        raise AssertionError("quality agent name mismatch")
    if packaging_agent["name"] != "packaging":
        raise AssertionError("packaging agent name mismatch")

    from a0.components.quality.evaluator import (
        evaluate_agent_profile,
        evaluate_package_manifest,
        evaluate_prompt_text,
    )
    from a0.components.packaging.documentation_gen import build_docs_bundle
    from a0.components.packaging.eval_integrator import quality_check_request
    from a0.components.packaging.package_builder import build_manifest
    from a0.components.packaging.validator import validate_package
    from a0.components.course.orchestrator import CourseOrchestrator
    from a0.components.course.stages.assessment_gen import run as assessment_stage
    from a0.components.course.stages.blueprint_gen import run as blueprint_stage
    from a0.components.course.stages.content_dev import run as content_stage
    from a0.components.course.stages.package_del import run as delivery_stage
    from a0.components.course.stages.marketing_strat import run as marketing_stage
    from a0.components.course.stages.multimedia_src import run as multimedia_stage
    from a0.components.course.stages.pricing_ana import run as pricing_stage
    from a0.components.course.stages.validate_qa import run as validate_stage
    from a0.components.content.asset_manager import build_asset_manifest
    from a0.components.content.quality_checks import evaluate_content_quality
    from a0.components.content.workflow_orchestrator import orchestrate_workflow
    from a0.components.infrastructure.ops_planner import build_operation_plan
    from a0.components.infrastructure.contracts import domain_boundaries, handoff_contracts
    from a0.components.infrastructure.readiness_checks import evaluate_readiness
    from a0.components.infrastructure.safety_gates import assess_risks

    prompt_report = evaluate_prompt_text(
        "You are a QA assistant. Input: text. Output: JSON. "
        "Must validate edge case handling and redact PII."
    )
    if "overall_score" not in prompt_report:
        raise AssertionError("prompt evaluation missing overall score")

    profile_report = evaluate_agent_profile(
        {"name": "demo", "title": "Demo", "type": "specialized", "version": "1.0.0", "description": "Example profile", "prompts": {"role": "prompts/role.md", "override": "prompts/override.md"}},
        ["agent.json", "_context.md", "prompts/role.md", "prompts/override.md"],
    )
    if not isinstance(profile_report.get("passed"), bool):
        raise AssertionError("agent profile evaluation missing pass status")

    manifest = build_manifest("prompt_pack", ["README.md", "EVAL_OVERVIEW.md", "listing.md"])
    if not manifest["complete"]:
        raise AssertionError("manifest should be complete for prompt_pack sample")

    package_report = evaluate_package_manifest(manifest)
    if package_report["rubric"] != "packaging-default":
        raise AssertionError("unexpected packaging rubric")

    request = quality_check_request(manifest)
    if request["target"] != "quality":
        raise AssertionError("quality integration target mismatch")
    packaging_validation = validate_package("prompt_pack", ["README.md", "listing.md", "EVAL_OVERVIEW.md"])
    if not packaging_validation["valid"]:
        raise AssertionError(f"packaging validator unexpectedly failed: {packaging_validation['errors']}")

    docs = build_docs_bundle(
        "Demo Package",
        ["README.md", "listing.md"],
        ["Python environment available"],
        ["Run validation", "Deliver artifacts"],
    )
    if "README.md" not in docs or "build-guide.md" not in docs:
        raise AssertionError("docs bundle missing expected files")

    orchestrator = CourseOrchestrator(
        handlers={
            "blueprint": blueprint_stage,
            "content": content_stage,
            "assessment": assessment_stage,
            "multimedia": multimedia_stage,
            "marketing": marketing_stage,
            "pricing": pricing_stage,
            "validate": validate_stage,
            "delivery": delivery_stage,
        }
    )
    course_results = orchestrator.run({"course_id": "demo-001", "topic": "Python", "audience": "Beginners"})
    if course_results["delivery"]["status"] != "ok":
        raise AssertionError("course orchestrator delivery stage did not execute")
    blueprint_output = course_results["blueprint"]["output"]
    if len(blueprint_output.get("modules", [])) < 10:
        raise AssertionError("blueprint stage did not generate minimum modules")
    validate_output = course_results["validate"]["output"]
    if not validate_output.get("passed", False):
        raise AssertionError("validate stage did not pass expected baseline checks")
    multimedia_output = course_results["multimedia"]["output"]
    if not multimedia_output.get("multimedia"):
        raise AssertionError("multimedia stage produced no module assets")
    if not all(item["meets_targets"]["images_3_to_5"] for item in multimedia_output["multimedia"]):
        raise AssertionError("multimedia stage failed image target checks")
    marketing_output = course_results["marketing"]["output"]
    if not marketing_output.get("meets_2000_word_target", False):
        raise AssertionError("marketing stage did not meet 2000-word baseline")
    pricing_output = course_results["pricing"]["output"]
    if not pricing_output.get("meets_min_competitor_count", False):
        raise AssertionError("pricing stage competitor baseline not met")
    delivery_output = course_results["delivery"]["output"]
    if not delivery_output.get("ready_for_deployment", False):
        raise AssertionError("delivery stage did not mark deployment readiness")

    content_workflow = orchestrate_workflow("Python Automation", "Beginners", "YouTube")
    if content_workflow.get("stage_count") != 7:
        raise AssertionError("content workflow orchestrator returned unexpected stage count")
    content_manifest = build_asset_manifest("Python Automation", "YouTube")
    content_gates = evaluate_content_quality(content_manifest)
    if not all(content_gates.values()):
        raise AssertionError("content quality gates did not pass expected baseline checks")
    content_cli_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "content" / "scripts" / "orchestrate_content.py"),
            "--topic",
            "Python Automation",
            "--audience",
            "Beginners",
            "--channel",
            "YouTube",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    content_cli_payload = json.loads(content_cli_run.stdout)
    if "production_plan" not in content_cli_payload:
        raise AssertionError("content CLI output missing production_plan")
    if "pdf_export" not in content_cli_payload["production_plan"]:
        raise AssertionError("content CLI output missing pdf_export plan")

    infra_checks = evaluate_readiness("staging")
    infra_plan = build_operation_plan("application", "staging")
    infra_risks = assess_risks(infra_checks)
    if "run-unit-tests" not in infra_plan:
        raise AssertionError("infrastructure plan missing run-unit-tests step")
    if len(infra_risks) == 0:
        raise AssertionError("infrastructure risk assessment returned no entries")
    infra_boundaries = domain_boundaries()
    if "developer" not in infra_boundaries or "hacker" not in infra_boundaries:
        raise AssertionError("infrastructure boundary contracts missing developer/hacker ownership")
    if "developer_to_infrastructure" not in handoff_contracts():
        raise AssertionError("infrastructure handoff contract missing developer_to_infrastructure")

    cli_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "course" / "scripts" / "orchestrate.py"),
            "--topic",
            "Python",
            "--audience",
            "Beginners",
            "--module-count",
            "10",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    cli_payload = json.loads(cli_run.stdout)
    if "results" not in cli_payload or "artifacts" not in cli_payload:
        raise AssertionError("course CLI output missing expected keys")

    signals_file = AGENTS_ROOT / "tmp_research_signals.json"
    signals_file.write_text(
        json.dumps(
            [
                {"title": "Prompt Pack A", "category": "prompts", "price_usd": 49, "source": "gumroad"},
                {"title": "Prompt Pack B", "category": "prompts", "price_usd": 79, "source": "gumroad"},
                {"title": "Template X", "category": "templates", "price_usd": 39, "source": "gumroad"},
            ],
            indent=2,
        ),
        encoding="utf-8",
    )
    research_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "research" / "scripts" / "analyze.py"),
            "--signals-file",
            str(signals_file),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    research_payload = json.loads(research_run.stdout)
    if "ranking" not in research_payload or "recommendations" not in research_payload:
        raise AssertionError("research CLI output missing expected keys")
    if "niche_ranking_table" not in research_payload:
        raise AssertionError("research CLI output missing niche_ranking_table")
    signals_file.unlink(missing_ok=True)

    quality_payload_file = AGENTS_ROOT / "tmp_quality_payload.json"
    quality_payload_file.write_text(
        json.dumps(
            {
                "mode": "criteria",
                "rubric": "prompt-eval",
                "scores": {
                    "clarity": 0.9,
                    "specificity": 0.8,
                    "structure": 0.8,
                    "bias_free": 0.9,
                    "robustness": 0.8,
                    "efficiency": 0.85,
                },
            }
        ),
        encoding="utf-8",
    )
    dispatch_quality_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"),
            "--domain",
            "quality",
            "--payload-file",
            str(quality_payload_file),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    dispatch_quality_payload = json.loads(dispatch_quality_run.stdout)
    if dispatch_quality_payload.get("domain") != "quality":
        raise AssertionError("agent0 dispatch did not run quality domain")
    quality_payload_file.unlink(missing_ok=True)

    research_payload_file = AGENTS_ROOT / "tmp_research_payload.json"
    research_payload_file.write_text(
        json.dumps(
            {
                "signals": [
                    {"title": "Offer A", "category": "prompts", "price_usd": 29, "source": "gumroad"},
                    {"title": "Offer B", "category": "templates", "price_usd": 59, "source": "gumroad"},
                ]
            }
        ),
        encoding="utf-8",
    )
    dispatch_research_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"),
            "--intent",
            "market trend analysis",
            "--payload-file",
            str(research_payload_file),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    dispatch_research_payload = json.loads(dispatch_research_run.stdout)
    if dispatch_research_payload.get("domain") != "research":
        raise AssertionError("agent0 dispatch intent routing failed for research")
    research_payload_file.unlink(missing_ok=True)

    branding_payload_file = AGENTS_ROOT / "tmp_branding_payload.json"
    branding_payload_file.write_text(
        json.dumps({"niche": "Productivity", "audience": "Creators", "product_name": "Prompt Kit"}),
        encoding="utf-8",
    )
    branding_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"),
            "--domain",
            "branding",
            "--payload-file",
            str(branding_payload_file),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    branding_payload = json.loads(branding_run.stdout)
    if branding_payload.get("domain") != "branding":
        raise AssertionError("agent0 dispatch did not run branding domain")
    branding_payload_file.unlink(missing_ok=True)

    content_payload_file = AGENTS_ROOT / "tmp_content_payload.json"
    content_payload_file.write_text(
        json.dumps({"topic": "Python Automation", "audience": "Beginners", "channel": "YouTube"}),
        encoding="utf-8",
    )
    content_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"),
            "--domain",
            "content",
            "--payload-file",
            str(content_payload_file),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    content_payload = json.loads(content_run.stdout)
    if content_payload.get("domain") != "content":
        raise AssertionError("agent0 dispatch did not run content domain")
    content_payload_file.unlink(missing_ok=True)

    infra_payload_file = AGENTS_ROOT / "tmp_infra_payload.json"
    infra_payload_file.write_text(
        json.dumps({"target": "application", "environment": "staging", "mode": "agent-build"}),
        encoding="utf-8",
    )
    infra_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"),
            "--domain",
            "infrastructure",
            "--payload-file",
            str(infra_payload_file),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    infra_payload = json.loads(infra_run.stdout)
    if infra_payload.get("domain") != "infrastructure":
        raise AssertionError("agent0 dispatch did not run infrastructure domain")
    if "extras" not in infra_payload.get("output", {}):
        raise AssertionError("infrastructure dispatch output missing extras")
    if "agent_profile_scaffold" not in infra_payload["output"]["extras"]:
        raise AssertionError("infrastructure agent-build mode missing scaffold output")
    infra_payload_file.unlink(missing_ok=True)

    helper_payload_file = AGENTS_ROOT / "tmp_helper_payload.json"
    helper_payload_file.write_text(
        json.dumps(
            {
                "mode": "criteria",
                "rubric": "prompt-eval",
                "scores": {
                    "clarity": 0.85,
                    "specificity": 0.8,
                    "structure": 0.8,
                    "bias_free": 0.9,
                    "robustness": 0.8,
                    "efficiency": 0.8,
                },
            }
        ),
        encoding="utf-8",
    )
    helper_run = subprocess.run(
        [
            sys.executable,
            str(AGENTS_ROOT / "agent0" / "scripts" / "routed_call_helper.py"),
            "--domain",
            "quality",
            "--intent",
            "evaluate rubric",
            "--payload-file",
            str(helper_payload_file),
            "--execute",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    helper_payload = json.loads(helper_run.stdout)
    if helper_payload.get("profile") != "agent0":
        raise AssertionError("routed helper did not emit agent0 profile envelope")
    dispatch_result = helper_payload.get("dispatch_result", {})
    if dispatch_result.get("domain") != "quality":
        raise AssertionError("routed helper execute path did not dispatch quality domain")
    message = helper_payload.get("message", "")
    if not message.startswith("ROUTE_DOMAIN_V1:"):
        raise AssertionError("routed helper message missing ROUTE_DOMAIN_V1 prefix")
    envelope = json.loads(message.split(":", 1)[1])
    if envelope.get("domain") != "quality":
        raise AssertionError("routed helper envelope missing expected domain")
    helper_payload_file.unlink(missing_ok=True)

    print("MIGRATION_SMOKE_OK")


if __name__ == "__main__":
    run()
