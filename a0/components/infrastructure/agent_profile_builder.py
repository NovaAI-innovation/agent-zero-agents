"""Agent profile scaffold/build helpers for Infrastructure domain."""

from __future__ import annotations

from typing import Dict


def scaffold_agent_profile(name: str, title: str, description: str, domain: str) -> Dict[str, str]:
    """Return deterministic scaffold files for a new agent profile."""
    role_text = (
        f"You are {title}.\n"
        f"You specialize in {domain} tasks.\n"
        "Provide concise, structured, action-ready outputs.\n"
    )
    override_text = (
        "## Override Rules\n\n"
        "- Keep responses concise and operational.\n"
        "- Prefer deterministic output structures over prose.\n"
    )
    context_text = (
        f"# {title}\n\n"
        "Purpose:\n"
        f"- {description}\n\n"
        "Capabilities:\n"
        f"- Domain-focused {domain} execution.\n"
    )
    agent_json = (
        "{\n"
        f"  \"name\": \"{name}\",\n"
        f"  \"title\": \"{title}\",\n"
        f"  \"description\": \"{description}\",\n"
        "  \"type\": \"specialized\",\n"
        "  \"version\": \"1.0.0\",\n"
        "  \"prompts\": {\n"
        "    \"role\": \"prompts/role.md\",\n"
        "    \"override\": \"prompts/override.md\"\n"
        "  },\n"
        "  \"skills\": [],\n"
        "  \"config\": {}\n"
        "}\n"
    )
    return {
        "agent.json": agent_json,
        "_context.md": context_text,
        "prompts/role.md": role_text,
        "prompts/override.md": override_text,
    }


def validate_scaffold(files: Dict[str, str]) -> Dict[str, object]:
    required = {"agent.json", "_context.md", "prompts/role.md", "prompts/override.md"}
    missing = sorted([key for key in required if key not in files])
    return {
        "valid": len(missing) == 0,
        "missing": missing,
        "file_count": len(files),
    }
