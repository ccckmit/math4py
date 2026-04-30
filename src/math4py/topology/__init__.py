"""topology - 拓撲學模組。"""

from .function import (
    is_open_set,
    is_closed_set,
    is_connected,
    euler_characteristic,
    is_compact,
    is_hausdorff,
    closure,
    interior,
    boundary,
    homeomorphism_check,
    fundamental_group_trivial,
    topological_sort,
)
from .theorem import (
    euler_characteristic_theorem,
    hausdorff_separation_theorem,
    compactness_heine_borel,
    connectedness_continuum,
    homeomorphism_invariance,
    urey_lefschetz_fixed_point,
    brouwer_fixed_point_theorem,
)

__all__ = [
    "is_open_set",
    "is_closed_set",
    "is_connected",
    "euler_characteristic",
    "is_compact",
    "is_hausdorff",
    "closure",
    "interior",
    "boundary",
    "homeomorphism_check",
    "fundamental_group_trivial",
    "topological_sort",
    "euler_characteristic_theorem",
    "hausdorff_separation_theorem",
    "compactness_heine_borel",
    "connectedness_continuum",
    "homeomorphism_invariance",
    "urey_lefschetz_fixed_point",
    "brouwer_fixed_point_theorem",
]
