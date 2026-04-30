"""logic - 邏輯推論模組。"""

from .rete_inference import (
    Fact,
    ReteEngine,
    Rule,
    create_fact,
)
from .zfc import (
    EMPTY_SET,
    Set,
    choice_axiom,
    construct_natural_numbers,
    extensionality_axiom,
    pair_set_axiom,
    power_set_axiom,
    union_axiom,
    verify_zfc_axioms,
)

__all__ = [
    "Fact",
    "Rule",
    "ReteEngine",
    "create_fact",
    "Set",
    "EMPTY_SET",
    "extensionality_axiom",
    "pair_set_axiom",
    "union_axiom",
    "power_set_axiom",
    "choice_axiom",
    "construct_natural_numbers",
    "verify_zfc_axioms",
]
