"""Market signal normalization helpers for Research domain."""

from __future__ import annotations

from typing import Dict, List, Sequence


def _normalize_badges(value: object) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        items: Sequence[str] = [part.strip() for part in value.split(",")]
    elif isinstance(value, list):
        items = [str(item).strip() for item in value]
    else:
        items = [str(value).strip()]
    return [item for item in items if item]


def normalize_signal(
    title: str,
    category: str,
    price_usd: float,
    source: str,
    creator: str = "unknown",
    sales_badge: object = None,
    timeframe: str = "unknown",
) -> Dict[str, object]:
    """Normalize a single product/market signal."""
    normalized = {
        "title": title.strip(),
        "category": category.strip().lower(),
        "price_usd": float(price_usd),
        "source": source.strip(),
        "creator": creator.strip() if creator else "unknown",
        "sales_badges": _normalize_badges(sales_badge),
        "timeframe": timeframe.strip().lower() if timeframe else "unknown",
    }
    normalized["unknown_fields"] = [
        key for key in ("title", "category", "source", "creator") if normalized.get(key) in {"", "unknown"}
    ]
    return normalized


def summarize_categories(signals: List[Dict[str, object]]) -> Dict[str, int]:
    """Count normalized signals by category."""
    counts: Dict[str, int] = {}
    for signal in signals:
        category = str(signal.get("category", "unknown"))
        counts[category] = counts.get(category, 0) + 1
    return counts
