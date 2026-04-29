"""optimization - 最優化模組（梯度下降、牛頓法、凸優化）。"""

from .function import (
    gradient_descent,
    newton_method,
    is_convex_function,
    lagrange_multiplier,
    conjugate_gradient,
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
    "convex_first_order_condition",
    "convex_second_order_condition",
    "weierstrass_extreme_value",
    "kkt_conditions",
]
