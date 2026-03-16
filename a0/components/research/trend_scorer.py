"""Deterministic trend scoring for Research domain."""

from __future__ import annotations

from typing import Dict


def score_opportunity(count: int, avg_price: float, confidence: float) -> float:
    """Return normalized opportunity score (0-1)."""
    count_factor = min(1.0, count / 10)
    price_factor = min(1.0, max(0.0, avg_price / 500))
    confidence_factor = min(1.0, max(0.0, confidence))
    return round((0.45 * count_factor) + (0.35 * price_factor) + (0.20 * confidence_factor), 3)


def rank_categories(stats: Dict[str, Dict[str, float]]) -> Dict[str, float]:
    """Rank categories by deterministic opportunity score."""
    ranked: Dict[str, float] = {}
    for category, values in stats.items():
        ranked[category] = score_opportunity(
            int(values.get("count", 0)),
            float(values.get("avg_price", 0.0)),
            float(values.get("confidence", 0.5)),
        )
    return dict(sorted(ranked.items(), key=lambda item: item[1], reverse=True))
