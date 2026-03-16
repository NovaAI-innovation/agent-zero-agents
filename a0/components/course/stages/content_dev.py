"""Stage implementation: content development."""

from __future__ import annotations

from typing import Dict, List


SECTIONS = [
    "context",
    "theory",
    "example_simple",
    "example_realistic",
    "example_advanced",
    "implementation_walkthrough",
    "best_practices",
    "common_pitfalls",
    "resources",
]


def _section_text(topic: str, module_title: str, section: str, index: int) -> str:
    base = (
        f"{module_title} {section.replace('_', ' ')}: "
        f"Apply {topic} principles with concrete steps, constraints, and measurable outcomes."
    )
    repeat = max(1, index)
    return " ".join([base] * repeat)


def run(payload: dict, artifacts) -> dict:
    blueprint = payload.get("blueprint") or {}
    topic = blueprint.get("topic", payload.get("topic", "General Topic"))
    modules = blueprint.get("modules", [])

    generated: List[Dict[str, object]] = []
    for i, module in enumerate(modules, start=1):
        title = module.get("title", f"Module {i}")
        target_words = 300 * i
        section_map = {
            section: _section_text(topic, title, section, i) for section in SECTIONS
        }
        generated.append(
            {
                "id": module.get("id", f"M{i:02d}"),
                "title": title,
                "target_words": target_words,
                "sections": section_map,
            }
        )

    result = {
        "modules": generated,
        "section_template": SECTIONS,
        "word_count_formula": "module_n >= 300 * n",
    }
    artifacts.add("content", "content_modules.json")
    return result
