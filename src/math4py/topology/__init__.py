"""topology - 拓撲學模組。"""

from .function import (
    boundary,
    closure,
    euler_characteristic,
    fundamental_group_trivial,
    homeomorphism_check,
    interior,
    is_closed_set,
    is_compact,
    is_connected,
    is_hausdorff,
    is_open_set,
    topological_sort,
)
from .theorem import (
    brouwer_fixed_point_theorem,
    compactness_heine_borel,
    connectedness_continuum,
    euler_characteristic_theorem,
    hausdorff_separation_theorem,
    homeomorphism_invariance,
    urey_lefschetz_fixed_point,
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
