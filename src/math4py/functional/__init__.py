"""functional - 泛函分析與變分法模組。"""

from .variations import (
    brachistochrone_time,
    euler_lagrange_simple,
    geodesic_plane,
    shortest_path_length,
)

__all__ = [
    "shortest_path_length",
    "geodesic_plane",
    "brachistochrone_time",
    "euler_lagrange_simple",
]
