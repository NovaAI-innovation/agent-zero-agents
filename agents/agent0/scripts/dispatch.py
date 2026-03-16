"""Agent0 runtime dispatcher for domain scripts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict


AGENTS_ROOT = Path(__file__).resolve().parents[2]


DOMAIN_SCRIPT = {
    "quality": AGENTS_ROOT / "quality" / "scripts" / "evaluate.py",
    "packaging": AGENTS_ROOT / "packaging" / "scripts" / "prepare_package.py",
    "course": AGENTS_ROOT / "course" / "scripts" / "orchestrate.py",
    "research": AGENTS_ROOT / "research" / "scripts" / "analyze.py",
    "branding": AGENTS_ROOT / "branding" / "scripts" / "compose_brand.py",
    "content": AGENTS_ROOT / "content" / "scripts" / "orchestrate_content.py",
    "infrastructure": AGENTS_ROOT / "infrastructure" / "scripts" / "execute_ops.py",
}


def detect_domain(intent: str) -> str:
    text = intent.lower()
    if any(key in text for key in ["evaluate", "rubric", "score", "quality"]):
        return "quality"
    if any(key in text for key in ["package", "listing", "template", "bundle"]):
        return "packaging"
    if any(key in text for key in ["course", "module", "curriculum", "assessment"]):
        return "course"
    if any(key in text for key in ["research", "trend", "market", "niche"]):
        return "research"
    if any(key in text for key in ["brand", "branding", "logo", "identity"]):
        return "branding"
    if any(key in text for key in ["content", "script", "voice", "publish", "video"]):
        return "content"
    if any(key in text for key in ["infra", "infrastructure", "deploy", "environment", "ops"]):
        return "infrastructure"
    return "research"


def load_payload(path: str | None) -> Dict[str, Any]:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run_domain(domain: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    script = DOMAIN_SCRIPT[domain]
    if not script.exists():
        raise FileNotFoundError(f"Missing domain script: {script}")

    if domain == "quality":
        mode = payload.get("mode", "criteria")
        if mode == "prompt":
            cmd = [sys.executable, str(script), "prompt", "--text", payload["text"]]
        elif mode == "agent-profile":
            cmd = [sys.executable, str(script), "agent-profile", "--profile-dir", payload["profile_dir"]]
        elif mode == "package":
            cmd = [sys.executable, str(script), "package", "--manifest", payload["manifest"]]
        else:
            cmd = [
                sys.executable,
                str(script),
                "criteria",
                "--rubric",
                payload.get("rubric", "prompt-eval"),
                "--scores",
                json.dumps(payload.get("scores", {})),
            ]
    elif domain == "packaging":
        cmd = [
            sys.executable,
            str(script),
            "--package-type",
            payload.get("package_type", "prompt_pack"),
            "--product-name",
            payload.get("product_name", "Package"),
            "--niche",
            payload.get("niche", "General"),
            "--audience",
            payload.get("audience", "General Audience"),
            "--artifacts",
            *payload.get("artifacts", ["README.md", "listing.md", "EVAL_OVERVIEW.md"]),
        ]
    elif domain == "course":
        cmd = [
            sys.executable,
            str(script),
            "--topic",
            payload.get("topic", "General Topic"),
            "--audience",
            payload.get("audience", "General Audience"),
            "--module-count",
            str(payload.get("module_count", 10)),
        ]
    elif domain == "branding":
        cmd = [
            sys.executable,
            str(script),
            "--niche",
            payload.get("niche", "General"),
            "--audience",
            payload.get("audience", "General Audience"),
            "--product-name",
            payload.get("product_name", "Product"),
        ]
    elif domain == "content":
        cmd = [
            sys.executable,
            str(script),
            "--topic",
            payload.get("topic", "General Topic"),
            "--audience",
            payload.get("audience", "General Audience"),
            "--channel",
            payload.get("channel", "YouTube"),
        ]
    elif domain == "infrastructure":
        cmd = [
            sys.executable,
            str(script),
            "--target",
            payload.get("target", "application"),
            "--environment",
            payload.get("environment", "staging"),
            "--mode",
            payload.get("mode", "standard"),
        ]
    else:
        signals = payload.get(
            "signals",
            [
                {"title": "Sample Product", "category": "prompts", "price_usd": 49, "source": "gumroad"},
            ],
        )
        temp_path: Path | None = None
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False) as temp:
            temp_path = Path(temp.name)
            json.dump(signals, temp)
        cmd = [sys.executable, str(script), "--signals-file", str(temp_path)]

    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = json.loads(completed.stdout)
    finally:
        if domain == "research" and "temp_path" in locals() and temp_path:
            temp_path.unlink(missing_ok=True)
    return {"domain": domain, "command": cmd, "output": output}


def main() -> None:
    parser = argparse.ArgumentParser(description="Dispatch requests to domain runtime scripts.")
    parser.add_argument(
        "--domain",
        choices=["quality", "packaging", "course", "research", "branding", "content", "infrastructure"],
        help="Domain override.",
    )
    parser.add_argument("--intent", default="", help="Intent text used for routing when --domain is omitted.")
    parser.add_argument("--payload-file", help="Path to JSON payload.")
    args = parser.parse_args()

    payload = load_payload(args.payload_file)
    domain = args.domain or detect_domain(args.intent)
    result = run_domain(domain, payload)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
