"""Content domain runtime entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from a0.components.content.asset_manager import build_asset_manifest  # noqa: E402
from a0.components.content.pdf_pipeline import pdf_export_plan  # noqa: E402
from a0.components.content.publisher_pipeline import publish_plan  # noqa: E402
from a0.components.content.quality_checks import evaluate_content_quality  # noqa: E402
from a0.components.content.script_pipeline import script_outline  # noqa: E402
from a0.components.content.visuals_pipeline import visuals_plan  # noqa: E402
from a0.components.content.voice_pipeline import voice_plan  # noqa: E402
from a0.components.content.workflow_orchestrator import orchestrate_workflow  # noqa: E402


def orchestrate(topic: str, audience: str, channel: str) -> dict[str, object]:
    workflow_payload = orchestrate_workflow(topic, audience, channel)
    workflow = workflow_payload["stages"]
    artifacts = build_asset_manifest(topic, channel)
    quality_gates = evaluate_content_quality(artifacts)
    production_plan = {
        "script": script_outline(topic, audience),
        "visuals": visuals_plan(topic),
        "voice": voice_plan(),
        "pdf_export": pdf_export_plan(topic),
        "publish": publish_plan(channel),
    }
    return {
        "workflow": workflow,
        "artifacts": artifacts,
        "audience": audience,
        "channel": channel,
        "production_plan": production_plan,
        "quality_gates": quality_gates,
        "ready_for_publish": all(quality_gates.values()),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Orchestrate deterministic content workflow.")
    parser.add_argument("--topic", default="General Topic")
    parser.add_argument("--audience", default="General Audience")
    parser.add_argument("--channel", default="YouTube")
    args = parser.parse_args()
    print(json.dumps(orchestrate(args.topic, args.audience, args.channel), indent=2))


if __name__ == "__main__":
    main()
