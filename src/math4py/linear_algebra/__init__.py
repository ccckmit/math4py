"""Linear Algebra Module.

Provides vector and matrix operations, vector spaces, and linear algebra theorems.
"""

from .vector import norm_vector, dot_product, cross_product
from .matrix import Matrix
from .function import (
    det, inverse_2x2, matrix_add, matrix_multiply,
    matrix_scalar_mul, transpose, trace,
)
from .vector_space import VectorSpace
from .theorem import (
    rank_nullity_theorem, eigenvalues_theorem,
    svd_theorem, determinant_theorem,
    linear_independence_theorem,
)

__all__ = [
    "norm_vector", "dot_product", "cross_product",
    "Matrix",
    "det", "inverse_2x2", "matrix_add", "matrix_multiply",
    "matrix_scalar_mul", "transpose", "trace",
    "VectorSpace",
    "rank_nullity_theorem", "eigenvalues_theorem",
    "svd_theorem", "determinant_theorem",
    "linear_independence_theorem",
]
