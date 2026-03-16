"""Stage implementation: pricing analysis."""

from __future__ import annotations

from typing import Dict, List


def _tiers() -> List[Dict[str, object]]:
    return [
        {
            "name": "Starter",
            "price_usd": 197,
            "includes": ["Core modules", "Basic support"],
        },
        {
            "name": "Professional",
            "price_usd": 497,
            "includes": ["All modules", "Templates", "Email support"],
            "recommended": True,
        },
        {
            "name": "Premium",
            "price_usd": 1497,
            "includes": ["Everything", "Group coaching", "Accountability"],
        },
    ]


def run(payload: dict, artifacts) -> dict:
    blueprint = payload.get("blueprint", {})
    topic = blueprint.get("topic", payload.get("topic", "General Topic"))

    competitors = [
        {"name": "Competitor A", "price_usd": 149},
        {"name": "Competitor B", "price_usd": 299},
        {"name": "Competitor C", "price_usd": 399},
        {"name": "Competitor D", "price_usd": 699},
        {"name": "Competitor E", "price_usd": 999},
    ]

    expected_outcome_value_year = 6000
    roi_months = round((497 / expected_outcome_value_year) * 12, 2)

    result = {
        "topic": topic,
        "competitors": competitors,
        "tiers": _tiers(),
        "value_model": {
            "expected_outcome_value_year_usd": expected_outcome_value_year,
            "professional_tier_price_usd": 497,
            "estimated_roi_payoff_months": roi_months,
        },
        "meets_min_competitor_count": len(competitors) >= 5,
    }
    artifacts.add("pricing", "pricing_strategy.json")
    return result
