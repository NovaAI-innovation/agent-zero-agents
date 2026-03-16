"""Stage implementation: assessment generation."""

from __future__ import annotations

from typing import Dict, List


QUESTION_TYPES = [
    "mcq",
    "mcq",
    "true_false",
    "true_false",
    "fill_blank",
    "fill_blank",
    "short_answer",
    "short_answer",
    "code_challenge",
]


def _question(module_title: str, q_type: str, index: int) -> Dict[str, object]:
    return {
        "id": f"Q{index:02d}",
        "type": q_type,
        "prompt": f"{module_title}: {q_type} question {index}",
        "explanation": "Model explanation aligned with module objective and common pitfalls.",
    }


def run(payload: dict, artifacts) -> dict:
    modules = payload.get("content", {}).get("modules", payload.get("modules", []))
    assessments: List[Dict[str, object]] = []

    for module in modules:
        title = module.get("title", "Module")
        questions = [_question(title, q_type, i + 1) for i, q_type in enumerate(QUESTION_TYPES)]
        assessments.append(
            {
                "module_id": module.get("id", "M00"),
                "module_title": title,
                "question_count": len(questions),
                "questions": questions,
            }
        )

    result = {
        "assessments": assessments,
        "minimum_questions_per_module": 9,
        "required_distribution": {
            "mcq": 2,
            "true_false": 2,
            "fill_blank": 2,
            "short_answer": 2,
            "code_challenge": 1,
        },
    }
    artifacts.add("assessment", "assessments.json")
    return result
