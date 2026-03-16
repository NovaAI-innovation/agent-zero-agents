"""Course domain stage orchestrator scaffold."""

from __future__ import annotations

from typing import Callable, Dict

from .artifact_manager import ArtifactManager
from .stage_contracts import STAGE_ORDER


class CourseOrchestrator:
    """Executes stage handlers in canonical order."""

    def __init__(self, handlers: Dict[str, Callable[[dict, ArtifactManager], dict]]):
        self.handlers = handlers
        self.artifacts = ArtifactManager()

    def run(self, payload: dict) -> Dict[str, dict]:
        results: Dict[str, dict] = {}
        current = payload
        for stage in STAGE_ORDER:
            handler = self.handlers.get(stage)
            if handler is None:
                results[stage] = {"status": "skipped", "reason": "no handler"}
                continue
            output = handler(current, self.artifacts)
            results[stage] = {"status": "ok", "output": output}
            current = {**current, **{stage: output}}
        return results
