"""Stage implementation: validation and QA."""

from __future__ import annotations

from collections import Counter


REQUIRED_SECTIONS = {
    "context",
    "theory",
    "example_simple",
    "example_realistic",
    "example_advanced",
    "implementation_walkthrough",
    "best_practices",
    "common_pitfalls",
    "resources",
}


REQUIRED_DISTRIBUTION = {
    "mcq": 2,
    "true_false": 2,
    "fill_blank": 2,
    "short_answer": 2,
    "code_challenge": 1,
}


def run(payload: dict, artifacts) -> dict:
    content = payload.get("content", {})
    assessment = payload.get("assessment", {})

    module_checks = []
    for module in content.get("modules", []):
        section_keys = set(module.get("sections", {}).keys())
        missing_sections = sorted(REQUIRED_SECTIONS - section_keys)
        module_checks.append(
            {
                "module_id": module.get("id"),
                "missing_sections": missing_sections,
                "sections_ok": len(missing_sections) == 0,
            }
        )

    assessment_checks = []
    for module_assessment in assessment.get("assessments", []):
        counts = Counter(q["type"] for q in module_assessment.get("questions", []))
        dist_ok = all(counts.get(kind, 0) >= required for kind, required in REQUIRED_DISTRIBUTION.items())
        assessment_checks.append(
            {
                "module_id": module_assessment.get("module_id"),
                "question_count": module_assessment.get("question_count", 0),
                "distribution_ok": dist_ok,
            }
        )

    passed = all(check["sections_ok"] for check in module_checks) and all(
        check["distribution_ok"] and check["question_count"] >= 9 for check in assessment_checks
    )

    result = {
        "passed": passed,
        "module_checks": module_checks,
        "assessment_checks": assessment_checks,
    }
    artifacts.add("validate", "validation_report.json")
    return result
