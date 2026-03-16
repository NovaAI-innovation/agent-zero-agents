"""Research synthesis helpers for consolidated outputs."""

from __future__ import annotations

from collections import defaultdict
from statistics import median
from typing import Dict, List

from .heuristics import (
    badge_signal_strength,
    competition_intensity,
    confidence_score,
    demand_signal,
    monetization_quality,
)
from .market_analyzer import summarize_categories
from .trend_scorer import rank_categories


def _price_range(prices: List[float]) -> str:
    if not prices:
        return "$0-$0"
    return f"${int(min(prices))}-${int(max(prices))}"


def synthesize(signals: List[Dict[str, object]]) -> Dict[str, object]:
    """Produce category ranking and top opportunities from signals."""
    category_counts = summarize_categories(signals)

    per_category: Dict[str, Dict[str, object]] = defaultdict(lambda: {"prices": [], "creators": set(), "badges": [], "unknowns": 0})
    for signal in signals:
        category = str(signal.get("category", "unknown"))
        per_category[category]["prices"].append(float(signal.get("price_usd", 0.0)))
        per_category[category]["creators"].add(str(signal.get("creator", "unknown")))
        per_category[category]["badges"].extend(signal.get("sales_badges", []))
        per_category[category]["unknowns"] += len(signal.get("unknown_fields", []))

    category_stats: Dict[str, Dict[str, float]] = {}
    niche_table: List[Dict[str, object]] = []
    for category, count in category_counts.items():
        prices = [float(value) for value in per_category[category]["prices"]]
        creators = [creator for creator in per_category[category]["creators"] if creator and creator != "unknown"]
        badges = [str(b) for b in per_category[category]["badges"]]
        avg_price = sum(prices) / len(prices) if prices else 0.0
        max_price = max(prices) if prices else 0.0
        med_price = median(prices) if prices else 0.0
        unknown_ratio = per_category[category]["unknowns"] / max(1, (count * 4))

        demand = demand_signal(count=count, repeat_presence=min(count, len(prices)), badge_signal=badge_signal_strength(badges))
        competition = competition_intensity(count=count, unique_creators=len(creators))
        monetization = monetization_quality(avg_price=avg_price, max_price=max_price)
        confidence = confidence_score(count=count, unknown_ratio=unknown_ratio)

        category_stats[category] = {
            "count": float(count),
            "avg_price": float(avg_price),
            "confidence": float(confidence),
        }
        niche_table.append(
            {
                "niche": category,
                "signal_strength": demand,
                "competition": competition,
                "price_range": _price_range(prices),
                "median_price": round(float(med_price), 2),
                "monetization_quality": monetization,
                "confidence": confidence,
            }
        )

    ranking = rank_categories(category_stats)
    top_category = next(iter(ranking.keys()), "none")
    niche_table_sorted = sorted(niche_table, key=lambda item: (item["signal_strength"], item["monetization_quality"]), reverse=True)

    recommendations = [
        {
            "category": item["niche"],
            "score": ranking.get(item["niche"], 0.0),
            "action": (
                f"Launch a {item['niche']} offer at {item['price_range']} with differentiation against "
                f"competition={item['competition']}."
            ),
        }
        for item in niche_table_sorted[:3]
    ]

    return {
        "category_counts": category_counts,
        "ranking": ranking,
        "top_category": top_category,
        "niche_ranking_table": niche_table_sorted,
        "recommendations": recommendations,
    }
