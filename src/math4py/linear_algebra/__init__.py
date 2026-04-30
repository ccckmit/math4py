"""Linear Algebra Module.

Provides vector and matrix operations, vector spaces, and linear algebra theorems.
"""

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
    determinant_theorem,
    eigenvalues_theorem,
    linear_independence_theorem,
    rank_nullity_theorem,
    svd_theorem,
)
from .vector import cross_product, dot_product, norm_vector
from .vector_space import VectorSpace

__all__ = [
    "norm_vector",
    "dot_product",
    "cross_product",
    "Matrix",
    "det",
    "inverse_2x2",
    "matrix_add",
    "matrix_multiply",
    "matrix_scalar_mul",
    "transpose",
    "trace",
    "VectorSpace",
    "rank_nullity_theorem",
    "eigenvalues_theorem",
    "svd_theorem",
    "determinant_theorem",
    "linear_independence_theorem",
]
