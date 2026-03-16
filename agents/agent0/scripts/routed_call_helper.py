"""Build and optionally execute routed Agent0 domain calls.

This helper avoids direct `call_subordinate(profile='<domain>')` usage.
Use `profile='agent0'` and pass the generated route envelope as message.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


AGENTS_ROOT = Path(__file__).resolve().parents[2]
DISPATCH_SCRIPT = AGENTS_ROOT / "agent0" / "scripts" / "dispatch.py"
ROUTE_PREFIX = "ROUTE_DOMAIN_V1:"


def build_route_message(domain: str, intent: str, payload: dict[str, Any]) -> str:
    envelope = {
        "version": 1,
        "domain": domain,
        "intent": intent,
        "payload": payload,
    }
    return f"{ROUTE_PREFIX}{json.dumps(envelope, separators=(',', ':'))}"


def run_dispatch(domain: str, intent: str, payload: dict[str, Any]) -> dict[str, Any]:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False) as temp:
        temp_path = Path(temp.name)
        json.dump(payload, temp)

    cmd = [sys.executable, str(DISPATCH_SCRIPT), "--domain", domain, "--payload-file", str(temp_path)]
    if intent:
        cmd.extend(["--intent", intent])
    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(completed.stdout)
    finally:
        temp_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create and execute routed Agent0 domain calls.")
    parser.add_argument(
        "--domain",
        choices=["quality", "packaging", "course", "research", "branding", "content", "infrastructure"],
        required=True,
    )
    parser.add_argument("--intent", default="", help="Intent text to pass through route envelope.")
    parser.add_argument("--payload-file", help="Optional JSON payload file path.")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Execute `agent0/scripts/dispatch.py` with the same route payload.",
    )
    args = parser.parse_args()

    payload: dict[str, Any] = {}
    if args.payload_file:
        payload = json.loads(Path(args.payload_file).read_text(encoding="utf-8"))

    message = build_route_message(args.domain, args.intent, payload)
    output: dict[str, Any] = {"profile": "agent0", "message": message}
    if args.execute:
        output["dispatch_result"] = run_dispatch(args.domain, args.intent, payload)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
