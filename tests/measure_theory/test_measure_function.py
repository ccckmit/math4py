"""Test measure theory function module."""

import math4py.measure_theory.function as mt
import numpy as np


class TestSigmaAlgebra:
    def test_valid_sigma_algebra(self):
        """檢查有效的 σ-代數。"""
        universal = frozenset({1, 2, 3})
        sets = {frozenset(), frozenset({1, 2, 3})}
        assert mt.is_sigma_algebra(sets, universal) == True

    def test_missing_complement(self):
        """缺少補集則不是 σ-代數。"""
        universal = frozenset({1, 2, 3})
        sets = {frozenset(), frozenset({1})}
        assert mt.is_sigma_algebra(sets, universal) == False


class TestMeasureAdditivity:
    def test_additive(self):
        """不相交集合的測度可加。"""
        A1 = frozenset({1})
        A2 = frozenset({2})
        measure = {A1: 1.0, A2: 2.0, frozenset({1, 2}): 3.0}
        assert mt.measure_additivity([A1, A2], measure) == True


class TestLebesgueMeasure:
    def test_interval_measure(self):
        """區間 [a, b] 的勒貝格測度為 b-a。"""
        result = mt.lebesgue_measure_interval(0.0, 5.0)
        assert abs(result - 5.0) < 1e-10

    def test_empty_interval(self):
        """空區間的測度為 0。"""
        result = mt.lebesgue_measure_interval(3.0, 3.0)
        assert abs(result) < 1e-10


class TestLebesgueIntegrable:
    def test_continuous_function(self):
        """連續函數在閉區間上可積。"""
        f = lambda x: x**2
        assert mt.is_lebesgue_integrable(f, 0.0, 1.0) == True


class TestLebesgueIntegral:
    def test_constant_function(self):
        """常數函數的積分。"""
        f = lambda x: 2.0
        result = mt.lebesgue_integral(f, 0.0, 1.0)
        assert abs(result - 2.0) < 0.01

    def test_linear_function(self):
        """f(x) = x 在 [0,1] 的積分應為 0.5。"""
        f = lambda x: x
        result = mt.lebesgue_integral(f, 0.0, 1.0)
        assert abs(result - 0.5) < 0.01


class TestSigmaFinite:
    def test_finite_measure(self):
        """有限測度是 σ-有限的。"""
        measure = {frozenset({1}): 1.0, frozenset({2}): 1.0}
        universal = frozenset({1, 2})
        assert mt.sigma_finite_measure(measure, universal) == True


class TestLPNorm:
    def test_l2_norm(self):
        """L^2 範數計算。"""
        f = lambda x: x
        result = mt.l_p_norm(f, 0.0, 1.0, p=2.0)
        expected = np.sqrt(1.0/3.0)
        assert abs(result - expected) < 0.01

    def test_l1_norm(self):
        """L^1 範數。"""
        f = lambda x: 1.0
        result = mt.l_p_norm(f, 0.0, 1.0, p=1.0)
        assert abs(result - 1.0) < 0.01


class TestHolderInequality:
    def test_holder_p2_q2(self):
        """赫爾德不等式 p=q=2。"""
        f = lambda x: x
        g = lambda x: x**2
        result = mt.holder_inequality(f, g, p=2.0, q=2.0, a=0.0, b=1.0)
        assert result["pass"] == True


class TestMinkowskiInequality:
    def test_minkowski_p2(self):
        """閔可夫斯基不等式 p=2。"""
        f = lambda x: x
        g = lambda x: x**2
        result = mt.minkowski_inequality(f, g, p=2.0, a=0.0, b=1.0)
        assert result["pass"] == True
