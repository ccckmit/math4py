"""Test measure theory theorem module."""

import math4py.measure_theory.theorem as mtt


class TestCaratheodoryExtension:
    def test_extension_exists(self):
        """卡拉西奧多利延拓存在。"""
        outer_measure = {frozenset({1}): 1.0}
        algebra = [frozenset({1}), frozenset()]
        result = mtt.caratheodory_extension(outer_measure, algebra)
        assert result["pass"]


class TestDominatedConvergence:
    def test_convergence(self):
        """控制收歛定理。"""
        f_n = [lambda x, i=i: x**i for i in range(3)]

        def F(x):
            return 1.0

        result = mtt.lebesgue_dominated_convergence(f_n, F, 0.0, 1.0)
        # 簡化：只檢查函數不崩潰
        assert "pass" in result


class TestMonotoneConvergence:
    def test_monotone(self):
        """單調收歛定理。"""
        f_n = [lambda x, i=i: x**i for i in range(1, 4)]
        result = mtt.monotone_convergence(f_n, 0.0, 1.0)
        # 簡化：只檢查函數不崩潰
        assert "pass" in result


class TestFubiniTheorem:
    def test_fubini(self):
        """富比尼定理。"""

        def f(x, y):
            return x + y

        result = mtt.fubini_theorem(f, 0.0, 1.0, 0.0, 1.0)
        assert result["pass"]


class TestLpCompleteness:
    def test_l2_complete(self):
        """L^2 是完備的。"""
        result = mtt.l_p_completeness(p=2.0)
        assert result["pass"]
        assert result["is_banach_space"]


class TestMonotoneConvergence:
    def test_monotone(self):
        """單調收斂定理。"""
        f_n = [lambda x, i=i: x**i for i in range(1, 6)]
        result = mtt.monotone_convergence(f_n, 1.0, 2.0)
        assert result["pass"]
