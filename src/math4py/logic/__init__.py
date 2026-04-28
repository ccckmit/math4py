"""logic - 邏輯推論模組。"""

from .rete_inference import (
    Fact,
    ReteEngine,
    Rule,
    create_fact,
)

__all__ = [
    "Fact",
    "Rule",
    "ReteEngine",
    "create_fact",
]
