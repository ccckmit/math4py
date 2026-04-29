"""matrix - 矩陣運算模組。"""

from .function import (
    det,
    inverse_2x2,
    matrix_add,
    matrix_multiply,
    matrix_scalar_mul,
    trace,
    transpose,
)
from .matrix import Matrix

__all__ = [
    "Matrix",
    "det",
    "inverse_2x2",
    "matrix_multiply",
    "matrix_add",
    "matrix_scalar_mul",
    "transpose",
    "trace",
]
