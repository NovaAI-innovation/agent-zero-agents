"""Research domain runtime entrypoint backed by shared components."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from a0.components.research.market_analyzer import normalize_signal  # noqa: E402
from a0.components.research.synthesizer import synthesize  # noqa: E402


def _load_signals(path: Path) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("Input JSON must be a list of signal objects")
    normalized = []
    for item in payload:
        normalized.append(
            normalize_signal(
                title=str(item.get("title", "")),
                category=str(item.get("category", "unknown")),
                price_usd=float(item.get("price_usd", 0.0)),
                source=str(item.get("source", "unknown")),
                creator=str(item.get("creator", "unknown")),
                sales_badge=item.get("sales_badge", item.get("sales_badges", [])),
                timeframe=str(item.get("timeframe", "unknown")),
            )
        )
    return normalized


def main() -> None:
    parser = argparse.ArgumentParser(description="Research domain analyzer CLI.")
    parser.add_argument("--signals-file", required=True, help="Path to JSON list of signals.")
    parser.add_argument("--output", help="Optional output JSON file path.")
    args = parser.parse_args()

    signals = _load_signals(Path(args.signals_file))
    result = synthesize(signals)

    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2), encoding="utf-8")
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
