"""Test linear algebra vector module."""

import pytest
import math4py.linear_algebra.vector as lv


class TestNormVector:
    def test_2d_vector(self):
        """2D vector norm."""
        v = [3.0, 4.0]
        assert abs(lv.norm_vector(v) - 5.0) < 1e-10

    def test_zero_vector(self):
        """Zero vector norm."""
        v = [0.0, 0.0, 0.0]
        assert lv.norm_vector(v) == 0.0


class TestDotProduct:
    def test_orthogonal(self):
        """Orthogonal vectors."""
        v1 = [1.0, 0.0]
        v2 = [0.0, 1.0]
        assert lv.dot_product(v1, v2) == 0.0

    def test_parallel(self):
        """Parallel vectors."""
        v1 = [2.0, 0.0]
        v2 = [3.0, 0.0]
        assert lv.dot_product(v1, v2) == 6.0


class TestCrossProduct:
    def test_standard_basis(self):
        """i × j = k."""
        v1 = [1.0, 0.0, 0.0]
        v2 = [0.0, 1.0, 0.0]
        result = lv.cross_product(v1, v2)
        assert abs(result[0]) < 1e-10
        assert abs(result[1]) < 1e-10
        assert abs(result[2] - 1.0) < 1e-10
