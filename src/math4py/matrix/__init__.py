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
from .theorem import (
    determinant_properties,
    inverse_properties,
    matrix_addition_associative,
    matrix_addition_commutative,
    matrix_class_properties,
    matrix_multiplication_associative,
    trace_properties,
    transpose_properties,
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
    "matrix_multiplication_associative",
    "matrix_addition_commutative",
    "matrix_addition_associative",
    "transpose_properties",
    "determinant_properties",
    "inverse_properties",
    "trace_properties",
    "matrix_class_properties",
]
