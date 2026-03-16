"""Helpers for dispatching domain profiles to runtime scripts."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


RUNTIME_DOMAINS = {"quality", "packaging", "course", "research"}


def can_dispatch(profile: str) -> bool:
    return profile in RUNTIME_DOMAINS


def _agents_root() -> Path:
    return Path(__file__).resolve().parents[2] / "agents"


def _dispatch_script() -> Path:
    return _agents_root() / "agent0" / "scripts" / "dispatch.py"


def _build_payload(profile: str, message: str, kwargs: dict[str, Any]) -> dict[str, Any]:
    if profile == "quality":
        payload = {
            "mode": kwargs.get("mode", "prompt" if message else "criteria"),
            "text": kwargs.get("text", message),
            "file": kwargs.get("file"),
            "profile_dir": kwargs.get("profile_dir"),
            "manifest": kwargs.get("manifest"),
            "rubric": kwargs.get("rubric", "prompt-eval"),
            "scores": kwargs.get("scores", {}),
        }
        if payload["mode"] == "criteria" and not payload["scores"]:
            payload["scores"] = {
                "clarity": 0.8,
                "specificity": 0.8,
                "structure": 0.8,
                "bias_free": 0.8,
                "robustness": 0.8,
                "efficiency": 0.8,
            }
        return payload

    if profile == "packaging":
        artifacts = kwargs.get("artifacts", ["README.md", "listing.md", "EVAL_OVERVIEW.md"])
        if isinstance(artifacts, str):
            artifacts = [part.strip() for part in artifacts.split(",") if part.strip()]
        return {
            "package_type": kwargs.get("package_type", "prompt_pack"),
            "product_name": kwargs.get("product_name", "Package"),
            "niche": kwargs.get("niche", "General"),
            "audience": kwargs.get("audience", "General Audience"),
            "artifacts": artifacts,
        }

    if profile == "course":
        return {
            "topic": kwargs.get("topic", message or "General Topic"),
            "audience": kwargs.get("audience", "General Audience"),
            "module_count": int(kwargs.get("module_count", 10)),
        }

    return {
        "signals": kwargs.get(
            "signals",
            [
                {
                    "title": "Sample Signal",
                    "category": "prompts",
                    "price_usd": 49,
                    "source": "runtime-dispatch",
                }
            ],
        )
    }


def dispatch(profile: str, message: str, kwargs: dict[str, Any]) -> str:
    script = _dispatch_script()
    if not script.exists():
        raise FileNotFoundError(f"Dispatch script not found: {script}")

    payload = _build_payload(profile, message, kwargs)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", encoding="utf-8", delete=False) as temp:
        temp_path = Path(temp.name)
        json.dump(payload, temp)

    cmd = [
        sys.executable,
        str(script),
        "--domain",
        profile,
        "--payload-file",
        str(temp_path),
    ]

    try:
        completed = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return completed.stdout.strip()
    finally:
        temp_path.unlink(missing_ok=True)
