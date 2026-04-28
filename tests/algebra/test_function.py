"""Tests for algebra/vector.py and algebra/polynomial.py."""

from math4py.algebra.polynomial import polynomial_add, polynomial_eval, polynomial_multiply
from math4py.algebra.vector import cross_product, dot_product, norm_vector


class TestVectorFunctions:
    def test_norm_vector(self):
        v = [3, 4]
        assert norm_vector(v) == 5.0

    def test_dot_product(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        assert dot_product(v1, v2) == 32

    def test_cross_product(self):
        v1 = [1, 0, 0]
        v2 = [0, 1, 0]
        result = cross_product(v1, v2)
        assert result == [0, 0, 1]


class TestPolynomialFunctions:
    def test_polynomial_eval(self):
        coeffs = [2, 3, 1]  # 2x² + 3x + 1
        assert polynomial_eval(coeffs, 2) == 15

    def test_polynomial_add(self):
        p1 = [1, 2]  # x + 2
        p2 = [1, 1, 1]  # x² + x + 1
        result = polynomial_add(p1, p2)
        assert result == [1.0, 2.0, 3.0]

    def test_polynomial_multiply(self):
        p1 = [1, 1]  # x + 1
        p2 = [1, -1]  # x - 1
        result = polynomial_multiply(p1, p2)
        assert result == [1, 0, -1]
