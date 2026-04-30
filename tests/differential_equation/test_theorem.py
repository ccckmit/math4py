"""微分方程定理驗證測試。"""

import numpy as np

from math4py.differential_equation.theorem import (
    euler_convergence_order,
    heat_equation_decay_rate,
    lyapunov_negative_stable_fixed_point,
    lyapunov_positive_unstable_spiral,
    rk4_superior_to_euler,
    stability_criterion_heat,
    stability_criterion_wave,
    wave_equation_energy_conservation,
)


class TestEulerConvergenceOrder:
    def test_convergence_order_near_one(self):
        """Euler method convergence order should be ~1."""

        def f(t, y):
            return -y

        order = euler_convergence_order(f, np.array([1.0]), (0.0, 1.0))
        assert 0.8 < order < 1.2

    def test_zero_slope(self):
        """For zero slope, error should be small."""

        def f(t, y):
            return np.array([0.0])

        order = euler_convergence_order(f, np.array([1.0]), (0.0, 1.0))
        assert order >= 0


class TestRK4SuperiorToEuler:
    def test_rk4_more_accurate(self):
        def f(t, y):
            return -y

        result = rk4_superior_to_euler(f, np.array([1.0]), (0.0, 1.0), dt=0.01)
        assert result


class TestHeatEquationDecayRate:
    def test_decay_rate_positive(self):
        """Heat equation should decay."""
        rate = heat_equation_decay_rate(alpha=0.01)
        assert rate > 0

    def test_decay_rate_increases_with_alpha(self):
        rate1 = heat_equation_decay_rate(alpha=0.01)
        rate2 = heat_equation_decay_rate(alpha=0.02)
        assert rate2 > rate1


class TestWaveEquationEnergyConservation:
    def test_energy_conservation_low(self):
        """Energy variation should be small."""
        variation = wave_equation_energy_conservation(c=1.0)
        assert variation < 0.1

    def test_energy_conservation_higher_c(self):
        variation = wave_equation_energy_conservation(c=2.0)
        assert variation < 0.1


class TestStabilityCriterionHeat:
    def test_stable_case(self):
        assert stability_criterion_heat(0.25)

    def test_unstable_case(self):
        assert not stability_criterion_heat(0.6)


class TestStabilityCriterionWave:
    def test_stable_case(self):
        assert stability_criterion_wave(0.81)

    def test_unstable_case(self):
        assert not stability_criterion_wave(1.2)


class TestLyapunovNegativeStableFixedPoint:
    def test_stable_lyapunov_negative(self):
        result = lyapunov_negative_stable_fixed_point()
        assert result


class TestLyapunovPositiveUnstableSpiral:
    def test_unstable_lyapunov_positive(self):
        result = lyapunov_positive_unstable_spiral()
        assert result
