"""Matrix functions - re-export from linear_algebra.function.

This file is kept for backward compatibility.
Use math4py.linear_algebra.function instead.
"""

from math4py.linear_algebra.function import (
    det,
    inverse_2x2,
    matrix_multiply,
    matrix_add,
    matrix_scalar_mul,
    transpose,
    trace,
)

__all__ = [
    "det",
    "inverse_2x2",
    "matrix_multiply",
    "matrix_add",
    "matrix_scalar_mul",
    "transpose",
    "trace",
]
