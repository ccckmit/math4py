"""Test thermodynamics module theorems."""

import math4py.physics.thermodynamics as thermo


class TestIdealGasLaw:
    def test_ideal_gas_law_pv_nt(self):
        # PV = nRT, 求 P
        result = thermo.ideal_gas_law(V=0.024, n=1.0, T=293.15)
        expected = 1.0 * 8.314462618 * 293.15 / 0.024
        assert abs(result["P"] - expected) < 0.01

    def test_ideal_gas_law_inverse(self):
        # 給定 P, n, T 求 V
        result = thermo.ideal_gas_law(P=101325, n=1.0, T=273.15)
        expected = 1.0 * 8.314462618 * 273.15 / 101325
        assert abs(result["V"] - expected) < 1e-5


class TestCarnotEfficiency:
    def test_carnot_efficiency_max(self):
        # 相同溫度時效率為 0
        eta = thermo.carnot_efficiency(500, 500)
        assert eta == 0.0

    def test_carnot_efficiency_positive(self):
        # Th > Tc 時效率為正
        eta = thermo.carnot_efficiency(500, 300)
        assert 0 < eta < 1.0
