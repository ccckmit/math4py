"""Vector operations - re-export from linear_algebra.vector.

This file is kept for backward compatibility.
Use math4py.linear_algebra.vector instead.
"""

from math4py.linear_algebra.vector import cross_product, dot_product, norm_vector

__all__ = ["norm_vector", "dot_product", "cross_product"]
