"""Course domain runtime entrypoint backed by shared components."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from a0.components.course.orchestrator import CourseOrchestrator  # noqa: E402
from a0.components.course.stages.assessment_gen import run as assessment_stage  # noqa: E402
from a0.components.course.stages.blueprint_gen import run as blueprint_stage  # noqa: E402
from a0.components.course.stages.content_dev import run as content_stage  # noqa: E402
from a0.components.course.stages.marketing_strat import run as marketing_stage  # noqa: E402
from a0.components.course.stages.multimedia_src import run as multimedia_stage  # noqa: E402
from a0.components.course.stages.package_del import run as delivery_stage  # noqa: E402
from a0.components.course.stages.pricing_ana import run as pricing_stage  # noqa: E402
from a0.components.course.stages.validate_qa import run as validate_stage  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Course domain orchestrator CLI.")
    parser.add_argument("--course-id", default="course-001", help="Course identifier.")
    parser.add_argument("--topic", required=True, help="Course topic.")
    parser.add_argument("--audience", required=True, help="Target audience.")
    parser.add_argument("--module-count", type=int, default=10, help="Target module count (10-50).")
    parser.add_argument("--output", help="Optional output JSON file path.")
    args = parser.parse_args()

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

    payload = {
        "course_id": args.course_id,
        "topic": args.topic,
        "audience": args.audience,
        "module_count": args.module_count,
        "artifacts": {},
    }
    results = orchestrator.run(payload)
    output = {
        "results": results,
        "artifacts": orchestrator.artifacts.all(),
    }

    if args.output:
        Path(args.output).write_text(json.dumps(output, indent=2), encoding="utf-8")
    else:
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
