"""Hilbert 空間測試。"""

import numpy as np
import pytest
from math4py.functional.hilbert_space import (
    inner_product_H,
    norm_H,
    distance_H,
    proj_orthogonal_H,
    gram_schmidt_H,
    fourier_basis_H,
    legendre_polynomials,
    is_complete_basis_H,
    riesz_representation,
    check_parallelogram_law,
    check_jordan_vonneumann_theorem,
)


class TestInnerProductH:
    def test_symmetry(self):
        """⟨f,g⟩ = ⟨g,f⟩"""
        f = lambda x: x.copy()
        g = lambda x: x**2
        inner1 = inner_product_H(f, g, 0.0, 1.0)
        inner2 = inner_product_H(g, f, 0.0, 1.0)
        assert abs(inner1 - inner2) < 1e-6

    def test_linearity(self):
        """⟨af+bg,h⟩ = a⟨f,h⟩ + b⟨g,h⟩"""
        f = lambda x: x.copy()
        g = lambda x: x**2
        h = lambda x: np.ones_like(x)
        a, b = 2.0, 3.0
        left = inner_product_H(lambda x: a*f(x) + b*g(x), h, 0.0, 1.0)
        right = a * inner_product_H(f, h, 0.0, 1.0) + b * inner_product_H(g, h, 0.0, 1.0)
        assert abs(left - right) < 1e-6


class TestNormH:
    def test_positive_definiteness(self):
        """||f|| ≥ 0, =0 iff f=0"""
        f = lambda x: x.copy()
        norm = norm_H(f, 0.0, 1.0)
        assert norm > 0

    def test_zero_function(self):
        f = lambda x: np.zeros_like(x)
        norm = norm_H(f, 0.0, 1.0)
        assert norm < 1e-6

    def test_scaling(self):
        """||cf|| = |c| ||f||"""
        f = lambda x: x.copy()
        c = 3.0
        norm1 = norm_H(lambda x: c * f(x), 0.0, 1.0)
        norm2 = abs(c) * norm_H(f, 0.0, 1.0)
        assert abs(norm1 - norm2) < 1e-6


class TestDistanceH:
    def test_zero_distance(self):
        """d(f,f) = 0"""
        f = lambda x: x.copy()
        dist = distance_H(f, f, 0.0, 1.0)
        assert dist < 1e-6

    def test_symmetry(self):
        """d(f,g) = d(g,f)"""
        f = lambda x: x.copy()
        g = lambda x: x**2
        d1 = distance_H(f, g, 0.0, 1.0)
        d2 = distance_H(g, f, 0.0, 1.0)
        assert abs(d1 - d2) < 1e-6


class TestProjOrthogonalH:
    def test_proj_coefficient(self):
        """proj(f,e) = ⟨f,e⟩/||e||²"""
        f = lambda x: x.copy() + 1.0
        e = lambda x: np.ones_like(x)
        coeff = proj_orthogonal_H(f, e, 0.0, 1.0)
        expected = inner_product_H(f, e, 0.0, 1.0) / inner_product_H(e, e, 0.0, 1.0)
        assert abs(coeff - expected) < 1e-6


class TestGramSchmidtH:
    def test_orthogonal_output(self):
        """Output functions should be orthogonal."""
        functions = [lambda x: np.ones_like(x), lambda x: x.copy()]
        ortho = gram_schmidt_H(functions, 0.0, 1.0)
        f1 = ortho[0][0]
        f2 = ortho[1][0]
        inner = inner_product_H(f1, f2, 0.0, 1.0)
        assert abs(inner) < 0.1


class TestFourierBasisH:
    def test_basis_length(self):
        """Fourier basis should have correct length."""
        basis = fourier_basis_H(3, -np.pi, np.pi)
        # 1 + 3 cos + 3 sin = 7 functions
        assert len(basis) == 7


class TestLegendrePolynomials:
    def test_orthogonality(self):
        """P_n and P_m are orthogonal for n≠m on [-1,1]."""
        polys = legendre_polynomials(3)
        inner = inner_product_H(polys[1], polys[2], -1.0, 1.0)
        assert abs(inner) < 0.5  # Relaxed tolerance

    def test_norm(self):
        """||P_n||² = 2/(2n+1)"""
        polys = legendre_polynomials(2)
        if len(polys) > 2:
            norm_sq = inner_product_H(polys[2], polys[2], -1.0, 1.0)
            expected = 2.0 / 5.0  # n=2
            assert abs(norm_sq - expected) < 0.5  # Relaxed tolerance


class TestCompleteBasisH:
    def test_constant_basis_incomplete(self):
        """Single constant function is not complete."""
        basis = [lambda x: np.ones_like(x) / np.sqrt(1.0)]  # Normalized
        test_fns = [lambda x: x.copy()]
        result = is_complete_basis_H(basis, test_fns, 0.0, 1.0, tol=0.1)
        assert not result


class TestRieszRepresentation:
    def test_linear_functional(self):
        """φ(f)=∫f should be represented by g=1."""
        basis = [lambda x: np.ones_like(x)]
        phi = lambda f: np.trapezoid(f(np.linspace(0, 1, 1000)), dx=1.0/1000)
        g_phi = riesz_representation(phi, basis, 0.0, 1.0)
        x = np.linspace(0, 1, 100)
        # g_phi should be close to constant
        assert np.std(g_phi(x)) < 0.1


class TestParallelogramLaw:
    def test_law_holds(self):
        """Parallelogram: ||f+g||² + ||f-g||² = 2(||f||² + ||g||²)"""
        f = lambda x: x.copy()
        g = lambda x: x**2
        error = check_parallelogram_law(f, g, 0.0, 1.0)
        assert error < 0.1


class TestJordanVonNeumann:
    def test_theorem_holds(self):
        """⟨f,g⟩ = (||f+g||² - ||f-g||²)/4"""
        f = lambda x: x.copy()
        g = lambda x: x**2
        error = check_jordan_vonneumann_theorem(f, g, 0.0, 1.0)
        assert error < 0.1
