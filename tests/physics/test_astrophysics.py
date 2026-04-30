"""Test astrophysics module theorems."""

import math4py.physics.astrophysics as ap


class TestSchwarzschildRadius:
    def test_schwarzschild_radius_earth(self):
        # 地球史瓦西半徑約 9 mm
        Rs = ap.schwarzschild_radius(5.97e24)
        assert 0.005 < Rs < 0.015

    def test_schwarzschild_radius_proportional_to_mass(self):
        # Rs ∝ M
        Rs1 = ap.schwarzschild_radius(1e30)
        Rs2 = ap.schwarzschild_radius(2e30)
        assert abs(Rs2 - 2 * Rs1) / Rs1 < 1e-10


class TestOrbitalVelocity:
    def test_orbital_velocity_earth(self):
        # 地球軌道速度約 30 km/s
        v = ap.orbital_velocity(1.989e30, 1.496e11)
        assert 20000 < v < 40000


class TestEscapeVelocity:
    def test_escape_velocity_earth(self):
        # 地球逃逸速度約 11.2 km/s
        v_esc = ap.escape_velocity(5.97e24, 6.371e6)
        assert 10000 < v_esc < 12000
