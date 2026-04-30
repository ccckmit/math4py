"""測度論測試。"""

import pytest
import math
from math4py.calculus.measure import (
    is_measure,
    lebesgue_measure_1d,
    lebesgue_measure_2d,
    is_lebesgue_measurable,
    outer_measure_1d,
    counting_measure,
    dirac_measure,
    sigma_algebra_generated,
    measure_space_check,
    lebesgue_integral_simple,
    is_integrable_indicator,
)


class TestLebesgueMeasure1D:
    def test_interval_length(self):
        """區間 [a,b] 的測度為 b-a。"""
        assert lebesgue_measure_1d((0.0, 5.0)) == 5.0
        assert lebesgue_measure_1d((-2.0, 2.0)) == 4.0

    def test_single_point(self):
        """單點集測度為0。"""
        # 簡化：用長度為0的區間表示
        assert lebesgue_measure_1d((3.0, 3.0)) == 0.0

    def test_empty_set(self):
        """空集測度為0。"""
        assert lebesgue_measure_1d((0.0, 0.0)) == 0.0


class TestLebesgueMeasure2D:
    def test_rectangle_area(self):
        """矩形測度為面積。"""
        assert lebesgue_measure_2d((0.0, 2.0, 0.0, 3.0)) == 6.0

    def test_unit_square(self):
        """單位正方形測度為1。"""
        assert lebesgue_measure_2d((0.0, 1.0, 0.0, 1.0)) == 1.0


class TestIsLebesgueMeasurable:
    def test_interval_measurable(self):
        """區間是勒貝格可測的。"""
        assert is_lebesgue_measurable((0.0, 1.0))

    def test_discrete_set_measurable(self):
        """離散集合是可測的。"""
        assert is_lebesgue_measurable({1, 2, 3})


class TestOuterMeasure1D:
    def test_single_interval(self):
        """單個區間的外測度。"""
        assert outer_measure_1d([(0.0, 2.0)]) == 2.0

    def test_multiple_intervals(self):
        """多個區間的外測度為總長。"""
        total = outer_measure_1d([(0.0, 1.0), (2.0, 4.0)])
        assert abs(total - 3.0) < 1e-10


class TestCountingMeasure:
    def test_finite_set(self):
        """有限集合的計數測度。"""
        assert counting_measure({1, 2, 3}) == 3
        assert counting_measure(set()) == 0

    def test_empty_set(self):
        """空集的計數測度為0。"""
        assert counting_measure(set()) == 0


class TestDiracMeasure:
    def test_contains_point(self):
        """包含 x0 的集合測度為1。"""
        assert dirac_measure(0, {0, 1, 2}) == 1.0

    def test_not_contains(self):
        """不包含 x0 的集合測度為0。"""
        assert dirac_measure(5, {0, 1, 2}) == 0.0


class TestSigmaAlgebra:
    def test_generated_simple(self):
        """生成簡單的 σ-代數。"""
        sets = [{'a'}, {'b'}]
        sigma = sigma_algebra_generated(sets)
        assert len(sigma) > 0
        assert set() in sigma or any(len(s) == 0 for s in sigma)


class TestIsMeasure:
    def test_counting_is_measure(self):
        """計數測度是合法的測度。"""
        mu = counting_measure
        sets = [{1}, {2}, {1, 2}]
        is_valid, reason = is_measure(mu, sets)
        assert is_valid, reason

    def test_dirac_is_measure(self):
        """狄拉克測度是合法的測度。"""
        mu = lambda A: dirac_measure(0, A)
        sets = [{0}, {1}, {0, 1}]
        is_valid, reason = is_measure(mu, sets)
        assert is_valid, reason


class TestMeasureSpace:
    def test_valid_space(self):
        """檢查測度空間。"""
        X = {1, 2, 3}
        measurable = [set(), {1}, {2}, {1, 2}]
        mu = counting_measure
        is_valid, reason = measure_space_check(X, measurable, mu)
        assert is_valid, reason


class TestLebesgueIntegral:
    def test_simple_function(self):
        """簡單函數的勒貝格積分。"""
        # f = 2 * 1_{A1} + 3 * 1_{A2}
        values = [2.0, 3.0]
        measures = [1.0, 2.0]  # A1 測度=1, A2 測度=2
        result = lebesgue_integral_simple(values, measures)
        assert result == 8.0  # 2*1 + 3*2


class TestIntegrableIndicator:
    def test_finite_measure(self):
        """測度有限的集合指示函數可積。"""
        mu = lambda A: lebesgue_measure_1d((0.0, 1.0))  # 測度=1
        assert is_integrable_indicator({0.5}, mu)

    def test_infinite_measure(self):
        """測度無限的集合指示函數不可積（簡化）。"""
        mu = lambda A: float('inf')
        assert not is_integrable_indicator({0.5}, mu)
