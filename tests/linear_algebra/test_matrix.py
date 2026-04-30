"""Test linear algebra matrix module."""

import math4py.linear_algebra.matrix as lm


class TestMatrixCreation:
    def test_from_list(self):
        """Create matrix from list."""
        m = lm.Matrix([[1, 2], [3, 4]])
        assert m.shape == (2, 2)

    def test_eye(self):
        """Identity matrix."""
        m = lm.Matrix.eye(3)
        assert m.shape == (3, 3)
        assert m._np_mat[0, 0] == 1.0
        assert m._np_mat[1, 1] == 1.0


class TestMatrixOperations:
    def test_add(self):
        """Matrix addition."""
        A = lm.Matrix([[1, 2], [3, 4]])
        B = lm.Matrix([[10, 20], [30, 40]])
        C = A + B
        assert C._np_mat[0, 0] == 11.0

    def test_multiply(self):
        """Matrix multiplication."""
        A = lm.Matrix([[1, 2], [3, 4]])
        B = lm.Matrix([[5, 6], [7, 8]])
        C = A @ B
        # [1*5+2*7, 1*6+2*8; 3*5+4*7, 3*6+4*8]
        assert abs(C._np_mat[0, 0] - 19.0) < 1e-10

    def test_transpose(self):
        """Matrix transpose."""
        A = lm.Matrix([[1, 2, 3], [4, 5, 6]])
        assert A.T.shape == (3, 2)

    def test_det(self):
        """Matrix determinant."""
        A = lm.Matrix([[1, 2], [3, 4]])
        assert abs(A.det() - (-2.0)) < 1e-10

    def test_inv(self):
        """Matrix inverse."""
        A = lm.Matrix([[1, 2], [3, 4]])
        A_inv = A.inv()
        I = A @ A_inv
        assert abs(I._np_mat[0, 0] - 1.0) < 0.01


class TestMatrixDecomposition:
    def test_qr(self):
        """QR decomposition."""
        A = lm.Matrix([[1, 2], [3, 4]])
        Q, R = A.qr()
        assert Q.shape == (2, 2)
        assert R.shape == (2, 2)

    def test_svd(self):
        """SVD decomposition."""
        A = lm.Matrix([[1, 2], [3, 4]])
        U, S, Vh = A.svd()
        assert len(S) == 2
