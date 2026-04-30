"""泛函分析函數測試。"""

import numpy as np

from math4py.functional.function import (
    compact_operator_test,
    function_space_basis,
    gram_schmidt_L2,
    inner_product_L2,
    is_orthogonal_L2,
    norm_L2,
    norm_Lp,
    spectral_radius,
    weak_convergence_test,
)


class TestNormLp:
    def test_constant_function(self):
        """||1||_p = (b-a)^{1/p}"""

        def f(x):
            return np.ones_like(x)

        norm = norm_Lp(f, 0.0, 2.0, p=2.0)
        expected = np.sqrt(2.0)
        assert abs(norm - expected) < 0.1

    def test_zero_norm(self):
        """Zero function should have zero norm."""

        def f(x):
            return np.zeros_like(x)

        norm = norm_L2(f, 0.0, 1.0)
        assert abs(norm) < 1e-6


class TestNormL2:
    def test_sine_norm(self):
        """||sin(πx)||₂ = 1/√2 for x∈[0,1]"""

        def f(x):
            return np.sin(np.pi * x)

        norm = norm_L2(f, 0.0, 1.0)
        assert abs(norm - 1.0 / np.sqrt(2.0)) < 0.05

    def test_polynomial_norm(self):
        """||x||₂ = 1/√3 for x∈[0,1]"""

        def f(x):
            return x.copy()

        norm = norm_L2(f, 0.0, 1.0)
        assert abs(norm - 1.0 / np.sqrt(3.0)) < 0.05


class TestInnerProductL2:
    def test_orthogonal_sine_cosine(self):
        """sin(πx) and cos(πx) are orthogonal on [0,1]."""

        def f(x):
            return np.sin(np.pi * x)

        def g(x):
            return np.cos(np.pi * x)

        inner = inner_product_L2(f, g, 0.0, 1.0)
        assert abs(inner) < 0.05

    def test_inner_product_symmetry(self):
        def f(x):
            return x.copy()

        def g(x):
            return x**2

        inner1 = inner_product_L2(f, g, 0.0, 1.0)
        inner2 = inner_product_L2(g, f, 0.0, 1.0)
        assert abs(inner1 - inner2) < 1e-6


class TestGramSchmidtL2:
    def test_orthogonal_output(self):
        """Output functions should be orthogonal."""
        functions = [lambda x: np.ones_like(x), lambda x: x.copy()]
        ortho = gram_schmidt_L2(functions, 0.0, 1.0)
        f1 = ortho[0]
        f2 = ortho[1]
        inner = inner_product_L2(f1, f2, 0.0, 1.0)
        assert abs(inner) < 0.1

    def test_preservation_norm(self):
        """After GS, norms should be non-zero."""
        functions = [lambda x: np.ones_like(x), lambda x: x.copy()]
        ortho = gram_schmidt_L2(functions, 0.0, 1.0)
        for f in ortho:
            norm_sq = inner_product_L2(f, f, 0.0, 1.0)
            assert norm_sq > 0


class TestIsOrthogonalL2:
    def test_orthogonal_functions(self):
        def f(x):
            return np.sin(np.pi * x)

        def g(x):
            return np.cos(np.pi * x)

        assert is_orthogonal_L2(f, g, 0.0, 1.0)

    def test_non_orthogonal(self):
        def f(x):
            return np.ones_like(x)

        def g(x):
            return x.copy()

        assert not is_orthogonal_L2(f, g, 0.0, 1.0)


class TestSpectralRadius:
    def test_diagonal_matrix(self):
        """ρ(diag(1,2,3)) = 3"""
        A = np.diag([1.0, 2.0, 3.0])
        rho = spectral_radius(A)
        assert abs(rho - 3.0) < 1e-6

    def test_identity(self):
        """ρ(I) = 1"""
        A = np.eye(3)
        rho = spectral_radius(A)
        assert abs(rho - 1.0) < 1e-6


class TestFunctionSpaceBasis:
    def test_basis_length(self):
        basis = function_space_basis(n_terms=5)
        assert len(basis) == 5

    def test_polynomial_basis(self):
        """x^k should be polynomials."""
        basis = function_space_basis(n_terms=3)
        x = np.linspace(0, 1, 10)
        np.testing.assert_allclose(basis[2](x), x**2, atol=1e-6)


class TestWeakConvergence:
    def test_constant_sequence(self):
        """Constant sequence f_n=1 converges weakly to 1."""
        f_n = [lambda x: np.ones_like(x) for _ in range(5)]

        def f(x):
            return np.ones_like(x)

        error = weak_convergence_test(f_n, f, 0.0, 1.0)
        assert error < 0.1


class TestCompactOperator:
    def test_smooth_kernel(self):
        """Smooth kernel should give compact operator."""

        def K(x, y):
            return np.sin(x - y)

        sv_min = compact_operator_test(K, 0.0, np.pi)
        assert sv_min < 0.1
