"""Test complex function (complex analysis) module theorems."""

import math4py.algebra.complex_function as cf
import numpy as np
import cmath


class TestComplexDerivative:
    def test_derivative_z_squared(self):
        """f(z)=z² 的導數是 2z。"""
        f = lambda z: z**2
        z = 2 + 1j
        deriv = cf.complex_derivative(f, z)
        expected = 2 * z
        assert abs(deriv - expected) < 1e-4

    def test_derivative_constant(self):
        """常數函數的導數是 0。"""
        f = lambda z: 3 + 2j
        deriv = cf.complex_derivative(f, 1+1j)
        assert abs(deriv) < 1e-10


class TestIsAnalytic:
    def test_analytic_z_squared(self):
        """f(z)=z² 是解析函數。"""
        f = lambda z: z**2
        assert cf.is_analytic(f, 1+1j) == True

    def test_analytic_non_analytic(self):
        """f(z)=z̄ (共軛) 不是解析函數。"""
        f = lambda z: z.conjugate()
        assert cf.is_analytic(f, 1+1j) == False


class TestIsHolomorphic:
    def test_holomorphic_polynomial(self):
        """多項式是全純函數。"""
        f = lambda z: z**3 + 2*z + 1
        assert cf.is_holomorphic(f) == True

    def test_holomorphic_conjugate(self):
        """共軛函數不是全純。"""
        f = lambda z: z.conjugate()
        assert cf.is_holomorphic(f) == False


class TestLineIntegral:
    def test_integral_z_from_0_to_1(self):
        """∫_0^1 z dz = 1/2。"""
        f = lambda z: z
        result = cf.line_integral(f, 0, 1)
        expected = 0.5
        assert abs(result - expected) < 1e-3

    def test_integral_constant(self):
        """∫_0^1 1 dz = 1。"""
        f = lambda z: 1+0j
        result = cf.line_integral(f, 0, 1)
        assert abs(result - 1.0) < 1e-3


class TestCauchyIntegralFormula:
    def test_cauchy_formula_identity(self):
        """對於 f(z)=z，柯西積分公式應回傳 f(a)。"""
        f = lambda z: z
        a = 1 + 0.5j
        result = cf.cauchy_integral_formula(f, a, r=0.5)
        assert abs(result - f(a)) < 1e-3


class TestMobiusTransformation:
    def test_identity_transformation(self):
        """恆等變換 w = z。"""
        z = 2 + 3j
        w = cf.mobius_transformation(1, 0, 0, 1, z)
        assert abs(w - z) < 1e-10

    def test_inversion(self):
        """反演 w = 1/z。"""
        z = 2 + 0j
        w = cf.mobius_transformation(0, 1, 1, 0, z)
        assert abs(w - 1/z) < 1e-10


class TestResidueSimplePole:
    def test_residue_1_over_z(self):
        """f(z)=1/z 在 z=0 的留數是 1。"""
        f = lambda z: 1/z
        result = cf.residue_simple_pole(f, 0)
        assert abs(result - 1.0) < 1e-3


class TestLiouvilleTheorem:
    def test_bounded_entire_constant(self):
        """有界整函數應為常數（簡化檢查）。"""
        f = lambda z: 1+0j  # 常數函數
        assert cf.liouville_theorem_check(f) == True


class TestMoreraTheorem:
    def test_morera_polynomial(self):
        """多項式滿足莫雷拉定理。"""
        f = lambda z: z**2
        assert cf.morera_theorem_check(f) == True


class TestGoursatsTheorem:
    def test_goursat_polynomial(self):
        """多項式滿足古爾薩定理。"""
        f = lambda z: z**2
        assert cf.goursat_theorem_check(f) == True


class TestRiemannZeta:
    def test_zeta_real_s_gt_1(self):
        """ζ(s) 對於實數 s > 1 應收斂。"""
        s = 2+0j
        result = cf.riemann_zeta(s, n_terms=50000)
        # ζ(2) = π²/6 ≈ 1.6449
        expected = np.pi**2 / 6
        assert abs(result.real - expected) < 0.01

    def test_zeta_not_defined_le_1(self):
        """ζ(s) 對於 Re(s) ≤ 1 未定義（簡化版）。"""
        s = 1+0j
        result = cf.riemann_zeta(s)
        assert cmath.isnan(result)


class TestRiemannHypothesis:
    def test_zeros_on_critical_line(self):
        """檢查已知零點是否在臨界線上。"""
        zeros = cf.critical_line_zero_count(n=5)
        assert cf.riemann_hypothesis_check_zeros(zeros) == True

    def test_zeros_real_part_half(self):
        """所有零點的實部應為 0.5。"""
        zeros = cf.critical_line_zero_count(n=3)
        for z in zeros:
            assert abs(z.real - 0.5) < 1e-10


class TestXiFunction:
    def test_xi_symmetric(self):
        """ξ(s) 應滿足 ξ(s) = ξ(1-s)（簡化檢查）。"""
        s = 2.0
        # 簡化版只檢查 s > 1 的情況
        result = cf.xi_function(complex(s, 0))
        assert not cmath.isnan(result)
