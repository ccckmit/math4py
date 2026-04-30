"""algebra - 代數模組，包裝 numpy/sympy 提供一致 API."""

from .complex import (
    argument,
    complex_add,
    complex_div,
    complex_exp,
    complex_log,
    complex_mul,
    complex_pow,
    complex_sub,
    conjugate,
    create_complex,
    from_polar,
    imag_part,
    modulus,
    real_part,
    solve_quadratic,
    to_polar,
)
from .function import (
    AlgebraicStructure,
    Field,
    Group,
    Ring,
)
from .polynomial import polynomial_add, polynomial_eval, polynomial_multiply
from .theorem import (
    associativity,
    closure_axiom,
    commutativity,
    distributivity,
    identity_element,
    inverse_element,
)
from math4py.linear_algebra.vector import cross_product, dot_product, norm_vector
from math4py.linear_algebra.vector_space import VectorSpace

__all__ = [
    "closure_axiom",
    "associativity",
    "identity_element",
    "inverse_element",
    "commutativity",
    "distributivity",
    "AlgebraicStructure",
    "Group",
    "Ring",
    "Field",
    "norm_vector",
    "dot_product",
    "cross_product",
    "polynomial_eval",
    "polynomial_add",
    "polynomial_multiply",
    "create_complex",
    "real_part",
    "imag_part",
    "conjugate",
    "modulus",
    "argument",
    "to_polar",
    "from_polar",
    "complex_add",
    "complex_sub",
    "complex_mul",
    "complex_div",
    "complex_exp",
    "complex_log",
    "complex_pow",
    "solve_quadratic",
    "VectorSpace",
]
