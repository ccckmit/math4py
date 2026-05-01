"""Pytest tests for physics theorems."""

import math

from math4py.physics.theorem import (
    boyle_law,
    conservation_energy,
    einstein_energy,
    first_law_thermodynamics,
    newton_second_law,
    ohms_law,
    snells_law,
)


class TestNewtonSecondLaw:
    def test_basic(self):
        result = newton_second_law(mass=2.0, acceleration=3.0, force=6.0)
        assert result["pass"]

    def test_fail(self):
        result = newton_second_law(mass=2.0, acceleration=3.0, force=7.0)
        assert not result["pass"]


class TestConservationEnergy:
    def test_basic(self):
        result = conservation_energy(ke_initial=10.0, pe_initial=20.0, ke_final=15.0, pe_final=15.0)
        assert result["pass"]


class TestOhmsLaw:
    def test_basic(self):
        result = ohms_law(voltage=12.0, current=2.0, resistance=6.0)
        assert result["pass"]


class TestSnellsLaw:
    def test_basic(self):
        # n1=1.0, theta1=30°, n2=1.5, theta2≈19.47°
        theta1 = math.radians(30)
        theta2 = math.asin(1.0 * math.sin(theta1) / 1.5)
        result = snells_law(n1=1.0, theta1=theta1, n2=1.5, theta2=theta2)
        assert result["pass"]


class TestEinsteinEnergy:
    def test_basic(self):
        c = 299792458
        m = 1.0
        e = m * c**2
        result = einstein_energy(mass=m, energy=e, c=c)
        assert result["pass"]


class TestBoyleLaw:
    def test_basic(self):
        result = boyle_law(p1=100.0, v1=2.0, p2=200.0, v2=1.0)
        assert result["pass"]


class TestFirstLawThermodynamics:
    def test_basic(self):
        # ΔU = Q - W: 10 = 15 - 5
        result = first_law_thermodynamics(q=15.0, delta_u=10.0, w=5.0)
        assert result["pass"]
