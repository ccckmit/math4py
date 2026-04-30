"""Test linear algebra theorems module."""

import pytest
import math4py.linear_algebra.theorem as lt


class TestRankNullity:
    def test_full_rank_square(self):
        """Full rank square matrix."""
        A = [[1, 0], [0, 1]]
        result = lt.rank_nullity_theorem(A)
        assert result["pass"]
        assert result["rank"] == 2

    def test_rank_deficient(self):
        """Rank deficient matrix."""
        A = [[1, 2], [2, 4]]
        result = lt.rank_nullity_theorem(A)
        assert result["rank"] == 1
        assert result["nullity"] == 1


class TestEigenvalues:
    def test_diagonal_matrix(self):
        """Diagonal matrix eigenvalues."""
        A = [[2, 0], [0, 3]]
        result = lt.eigenvalues_theorem(A)
        assert result["pass"]

    def test_identity(self):
        """Identity matrix."""
        A = [[1, 0], [0, 1]]
        result = lt.eigenvalues_theorem(A)
        assert result["trace"] == 2.0
        assert result["det"] == 1.0


class TestSVD:
    def test_reconstruction(self):
        """SVD reconstruction."""
        A = [[1, 2], [3, 4]]
        result = lt.svd_theorem(A)
        assert result["pass"]
        assert result["reconstruction_error"] < 1e-8


class TestDeterminant:
    def test_det_product(self):
        """det(AB) = det(A)det(B)."""
        A = [[1, 2], [3, 4]]
        result = lt.determinant_theorem(A)
        assert result["pass"]


class TestLinearIndependence:
    def test_independent(self):
        """Independent vectors."""
        vectors = [[1, 0], [0, 1]]
        result = lt.linear_independence_theorem(vectors)
        assert result["is_independent"]

    def test_dependent(self):
        """Dependent vectors."""
        vectors = [[1, 2], [2, 4]]
        result = lt.linear_independence_theorem(vectors)
        assert not result["is_independent"]
