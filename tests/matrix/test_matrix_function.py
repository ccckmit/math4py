"""Tests for matrix/function.py."""

from math4py.matrix.function import (
    det,
    inverse_2x2,
    matrix_add,
    matrix_multiply,
    matrix_scalar_mul,
    trace,
    transpose,
)


class TestMatrixFunctions:
    def test_det(self):
        m = [[1, 2], [3, 4]]
        assert det(m) == -2

    def test_inverse_2x2(self):
        m = [[4, 7], [2, 6]]
        inv = inverse_2x2(m)
        assert abs(inv[0][0] - 0.6) < 1e-9
        assert abs(inv[0][1] - (-0.7)) < 1e-9
        assert abs(inv[1][0] - (-0.2)) < 1e-9
        assert abs(inv[1][1] - 0.4) < 1e-9

    def test_matrix_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = matrix_multiply(A, B)
        assert result == [[19, 22], [43, 50]]

    def test_matrix_add(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        result = matrix_add(A, B)
        assert result == [[6, 8], [10, 12]]

    def test_matrix_scalar_mul(self):
        A = [[1, 2], [3, 4]]
        result = matrix_scalar_mul(A, 2)
        assert result == [[2, 4], [6, 8]]

    def test_transpose(self):
        A = [[1, 2, 3], [4, 5, 6]]
        result = transpose(A)
        assert result == [[1, 4], [2, 5], [3, 6]]

    def test_trace(self):
        A = [[1, 2], [3, 4]]
        assert trace(A) == 5
