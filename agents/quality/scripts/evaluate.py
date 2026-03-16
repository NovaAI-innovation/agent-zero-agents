"""Quality domain runtime entrypoint backed by shared components."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from a0.components.quality.evaluator import (  # noqa: E402
    evaluate,
    evaluate_agent_profile,
    evaluate_package_manifest,
    evaluate_prompt_text,
)


def _read_text(text: str | None, file_path: str | None) -> str:
    if text:
        return text
    if file_path:
        return Path(file_path).read_text(encoding="utf-8")
    raise ValueError("Provide either --text or --file")


def _file_index(profile_dir: Path) -> Iterable[str]:
    return [
        str(path.relative_to(profile_dir)).replace("\\", "/")
        for path in profile_dir.rglob("*")
        if path.is_file()
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Quality domain evaluator CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_prompt = subparsers.add_parser("prompt", help="Evaluate a prompt.")
    p_prompt.add_argument("--text", help="Prompt text to evaluate.")
    p_prompt.add_argument("--file", help="Path to prompt text file.")

    p_agent = subparsers.add_parser("agent-profile", help="Evaluate an agent profile.")
    p_agent.add_argument("--profile-dir", required=True, help="Path to agent directory.")

    p_package = subparsers.add_parser("package", help="Evaluate a package manifest.")
    p_package.add_argument("--manifest", required=True, help="Path to manifest JSON.")

    p_criteria = subparsers.add_parser("criteria", help="Evaluate explicit criterion scores against a rubric.")
    p_criteria.add_argument("--rubric", required=True, help="Rubric name (without .json).")
    p_criteria.add_argument("--scores", required=True, help="JSON object of criterion scores.")

    args = parser.parse_args()

    if args.command == "prompt":
        text = _read_text(args.text, args.file)
        result = evaluate_prompt_text(text)
    elif args.command == "agent-profile":
        profile_dir = Path(args.profile_dir)
        profile = json.loads((profile_dir / "agent.json").read_text(encoding="utf-8"))
        result = evaluate_agent_profile(profile, _file_index(profile_dir))
    elif args.command == "package":
        manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
        result = evaluate_package_manifest(manifest)
    else:
        criteria_scores = json.loads(args.scores)
        result = evaluate(args.rubric, criteria_scores)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
