"""Research scoring heuristics derived from legacy trend analysis behavior."""

from __future__ import annotations

from typing import Iterable


BADGE_WEIGHTS = {
    "bestseller": 1.0,
    "trending": 0.9,
    "popular": 0.8,
    "hot": 0.75,
    "new": 0.6,
}


def badge_signal_strength(sales_badges: Iterable[str]) -> float:
    """Return normalized badge signal strength (0-1)."""
    badges = [str(item).strip().lower() for item in sales_badges if str(item).strip()]
    if not badges:
        return 0.4
    score = max(BADGE_WEIGHTS.get(badge, 0.5) for badge in badges)
    return min(1.0, max(0.0, score))


def demand_signal(count: int, repeat_presence: int, badge_signal: float) -> float:
    """Estimate demand from category count, repeat presence, and badge strength."""
    count_factor = min(1.0, count / 12)
    repeat_factor = min(1.0, repeat_presence / 8)
    return round((0.45 * count_factor) + (0.35 * repeat_factor) + (0.20 * badge_signal), 3)


def competition_intensity(count: int, unique_creators: int) -> float:
    """Estimate competition: many offers with low creator diversity indicates crowding."""
    if count <= 0:
        return 0.0
    count_pressure = min(1.0, count / 14)
    creator_diversity = min(1.0, unique_creators / max(1, count))
    crowdedness = 1.0 - (0.6 * creator_diversity)
    return round(min(1.0, max(0.0, (0.65 * count_pressure) + (0.35 * crowdedness))), 3)


def monetization_quality(avg_price: float, max_price: float) -> float:
    """Estimate monetization quality from observed pricing depth."""
    avg_factor = min(1.0, max(0.0, avg_price / 120))
    max_factor = min(1.0, max(0.0, max_price / 300))
    return round((0.7 * avg_factor) + (0.3 * max_factor), 3)


def confidence_score(count: int, unknown_ratio: float) -> float:
    """Confidence rises with sample size and drops with unknown field ratio."""
    sample_factor = min(1.0, count / 10)
    known_factor = min(1.0, max(0.0, 1.0 - unknown_ratio))
    return round((0.6 * sample_factor) + (0.4 * known_factor), 3)
