"""Artifact tracking for Course domain orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ArtifactManager:
    """In-memory artifact registry for stage outputs."""

    artifacts: Dict[str, List[str]] = field(default_factory=dict)

    def add(self, stage: str, path: str) -> None:
        self.artifacts.setdefault(stage, []).append(path)

    def get(self, stage: str) -> List[str]:
        return self.artifacts.get(stage, [])

    def all(self) -> Dict[str, List[str]]:
        return dict(self.artifacts)
