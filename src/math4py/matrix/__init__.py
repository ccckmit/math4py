"""matrix - 矩陣運算模組 (re-export from linear_algebra)."""

from math4py.linear_algebra.matrix import Matrix
from math4py.linear_algebra.function import (
    det,
    inverse_2x2,
    matrix_add,
    matrix_multiply,
    matrix_scalar_mul,
    trace,
    transpose,
)

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
