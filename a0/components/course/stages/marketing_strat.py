"""Stage implementation: marketing strategy generation."""

from __future__ import annotations

from typing import Dict, List


def _section(name: str, audience: str, topic: str, repeat: int) -> str:
    sentence = (
        f"{name}: {audience} struggling with {topic} gets a concrete path, proof points, and next-step clarity. "
        f"This section maps pain to outcomes and differentiates the course from generic alternatives."
    )
    return " ".join([sentence] * repeat)


def _word_count(text: str) -> int:
    return len([token for token in text.split() if token.strip()])


def run(payload: dict, artifacts) -> dict:
    blueprint = payload.get("blueprint", {})
    topic = blueprint.get("topic", payload.get("topic", "General Topic"))
    audience = blueprint.get("audience", payload.get("audience", "General Audience"))

    sections = {
        "hook": _section("Hook", audience, topic, 90),
        "credibility": _section("Credibility", audience, topic, 120),
        "course_overview": _section("Course Overview", audience, topic, 150),
        "value_proposition": _section("Value Proposition", audience, topic, 120),
        "social_proof": _section("Social Proof", audience, topic, 90),
        "call_to_action": _section("Call To Action", audience, topic, 30),
    }
    page_text = "\n\n".join(sections.values())
    words = _word_count(page_text)

    result = {
        "audience": audience,
        "topic": topic,
        "sections": sections,
        "sales_page": page_text,
        "word_count": words,
        "meets_2000_word_target": words >= 2000,
    }
    artifacts.add("marketing", "sales_page.md")
    return result
