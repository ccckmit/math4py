"""optimization - 最優化模組（梯度下降、牛頓法、凸優化、爬山演算法、線性規劃）。"""

from .function import (
    gradient_descent,
    newton_method,
    is_convex_function,
    lagrange_multiplier,
    conjugate_gradient,
)
from .hill_climbing import (
    hill_climbing,
    hill_climbing_simple,
    random_restart_hill_climbing,
    simulated_annealing,
)
from .linear_programming import (
    simplex_method,
    solve_lp,
    is_feasible_point,
    duality_gap,
)
from .theorem import (
    convex_first_order_condition,
    convex_second_order_condition,
    weierstrass_extreme_value,
    kkt_conditions,
)

__all__ = [
    "gradient_descent",
    "newton_method",
    "is_convex_function",
    "lagrange_multiplier",
    "conjugate_gradient",
    "hill_climbing",
    "hill_climbing_simple",
    "random_restart_hill_climbing",
    "simulated_annealing",
    "simplex_method",
    "solve_lp",
    "is_feasible_point",
    "duality_gap",
    "convex_first_order_condition",
    "convex_second_order_condition",
    "weierstrass_extreme_value",
    "kkt_conditions",
]
