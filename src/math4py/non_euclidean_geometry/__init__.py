"""non_euclidean_geometry - 非歐幾何模組（雙曲、橢圓、球面幾何）。"""

from .function import (
    HyperbolicPoint,
    SphericalPoint,
    elliptic_distance,
    hyperbolic_distance,
    spherical_distance,
)
from .theorem import (
    hyperbolic_parallel_postulate,
    spherical_triangle_angle_sum,
)

__all__ = [
    "HyperbolicPoint",
    "SphericalPoint",
    "elliptic_distance",
    "hyperbolic_distance",
    "spherical_distance",
    "hyperbolic_parallel_postulate",
    "spherical_triangle_angle_sum",
]
