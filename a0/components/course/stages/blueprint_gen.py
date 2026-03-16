"""Stage implementation: blueprint generation."""

from __future__ import annotations

from typing import Dict, List


def _default_personas(audience: str) -> List[Dict[str, object]]:
    return [
        {
            "name": f"{audience} Beginner",
            "pain_points": ["Lacks structured path", "Overwhelmed by tools"],
            "goals": ["Ship first practical outcome", "Build confidence"],
            "budget": "low",
        },
        {
            "name": f"{audience} Practitioner",
            "pain_points": ["Inconsistent execution", "Knowledge gaps"],
            "goals": ["Standardize workflow", "Increase quality"],
            "budget": "medium",
        },
        {
            "name": f"{audience} Lead",
            "pain_points": ["Scaling training", "Quality drift"],
            "goals": ["Create repeatable playbooks", "Improve team outcomes"],
            "budget": "high",
        },
    ]


def _module_spec(index: int, topic: str) -> Dict[str, object]:
    return {
        "id": f"M{index:02d}",
        "title": f"{topic} Module {index}",
        "duration_minutes": 35 + index * 5,
        "difficulty": "foundational" if index <= 3 else "intermediate" if index <= 7 else "advanced",
        "objectives": [
            f"Apply core {topic} concept {index}",
            f"Explain tradeoffs for {topic} decision {index}",
            f"Implement practical workflow for {topic} module {index}",
        ],
        "prerequisites": [] if index == 1 else [f"M{index - 1:02d}"],
    }


def run(payload: dict, artifacts) -> dict:
    topic = str(payload.get("topic", "General Topic")).strip() or "General Topic"
    audience = str(payload.get("audience", "General Audience")).strip() or "General Audience"
    module_count = int(payload.get("module_count", 10))
    module_count = max(10, min(module_count, 50))

    modules = [_module_spec(i, topic) for i in range(1, module_count + 1)]

    result = {
        "course_title": f"{topic} for {audience}",
        "topic": topic,
        "audience": audience,
        "positioning": f"Practical {topic} system for {audience} with production-ready outcomes.",
        "competitor_count_target": 5,
        "personas": _default_personas(audience),
        "modules": modules,
        "success_metrics": {
            "completion_rate_target": 0.7,
            "assessment_pass_target": 0.8,
            "satisfaction_target": 4.5,
        },
    }
    artifacts.add("blueprint", "blueprint.json")
    return result
