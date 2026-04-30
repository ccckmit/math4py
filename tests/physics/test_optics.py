"""Test optics module theorems."""

import numpy as np

import math4py.physics.optics as optics


class TestSnellsLaw:
    def test_snells_law_normal_incidence(self):
        # 法線入射，θ2 = 0
        theta2 = optics.snells_law(1.0, 1.5, 0.0)
        assert abs(theta2) < 1e-10

    def test_snells_law_total_internal_reflection(self):
        # 全反射
        theta2 = optics.snells_law(1.5, 1.0, np.radians(50))
        assert theta2 == float("inf")


class TestCriticalAngle:
    def test_critical_angle_exists(self):
        # n1 > n2 時有臨界角
        theta_c = optics.critical_angle(1.5, 1.0)
        assert 0 < theta_c < np.pi / 2

    def test_critical_angle_no_tir(self):
        # n1 <= n2 時無全反射
        theta_c = optics.critical_angle(1.0, 1.5)
        assert theta_c == float("inf")


class TestMagnification:
    def test_magnification_negative(self):
        # 實像放大率為負
        m = optics.magnification(20.0, 10.0)
        assert m == -2.0
