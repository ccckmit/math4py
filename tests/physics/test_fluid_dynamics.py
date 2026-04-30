"""Test fluid dynamics module theorems."""

import math4py.physics.fluid_dynamics as fd


class TestContinuityEquation:
    def test_continuity_holds(self):
        # ρ1A1v1 = ρ2A2v2
        assert fd.continuity_equation(1.0, 1.0, 2.0, 1.0, 0.5, 4.0)

    def test_continuity_fails(self):
        # 不相等時應返回 False
        assert not fd.continuity_equation(1.0, 1.0, 2.0, 1.0, 1.0, 3.0)


class TestBernoulliEquation:
    def test_bernoulli_holds(self):
        # 簡單情況：靜止流體 P + ρgh
        assert fd.bernoulli_equation(101325, 1000, 0, 10, 101325 + 1000 * 9.81 * 10, 0, 0)


class TestReynoldsNumber:
    def test_reynolds_laminar(self):
        # 低雷諾數為層流
        Re = fd.reynolds_number(1000, 0.1, 0.01, 0.001)
        assert Re < 2000
