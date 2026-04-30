"""微分方程函數測試。"""

import numpy as np
import pytest

from math4py.differential_equation.function import (
    euler_method,
    heat_equation_explicit,
    lyapunov_exponent,
    rk2_method,
    rk4_method,
    solve_ivp,
    stability_matrix,
    wave_equation_explicit,
)


class TestEulerMethod:
    def test_linear_ode(self):
        """dy/dt = -y, y(0)=1 => y(t)=exp(-t)"""

        def f(t, y):
            return -y

        t, y = euler_method(f, np.array([1.0]), 0.0, 1.0, dt=0.001)
        exact = np.exp(-1.0)
        assert abs(y[-1, 0] - exact) < 0.05

    def test_zero_derivative(self):
        """dy/dt = 0"""

        def f(t, y):
            return np.array([0.0])

        t, y = euler_method(f, np.array([1.0]), 0.0, 1.0)
        assert abs(y[-1, 0] - 1.0) < 1e-6

    def test_constant_slope(self):
        """dy/dt = 2"""

        def f(t, y):
            return np.array([2.0])

        t, y = euler_method(f, np.array([0.0]), 0.0, 1.0, dt=0.01)
        assert abs(y[-1, 0] - 2.0) < 0.05


class TestRK2Method:
    def test_linear_ode(self):
        def f(t, y):
            return -y

        t, y = rk2_method(f, np.array([1.0]), 0.0, 1.0, dt=0.01)
        exact = np.exp(-1.0)
        assert abs(y[-1, 0] - exact) < 0.01

    def test_polynomial(self):
        """dy/dt = 2t, y(0)=0 => y=t^2"""

        def f(t, y):
            return np.array([2.0 * t])

        t, y = rk2_method(f, np.array([0.0]), 0.0, 1.0, dt=0.01)
        assert abs(y[-1, 0] - 1.0) < 0.02


class TestRK4Method:
    def test_linear_ode(self):
        def f(t, y):
            return -y

        t, y = rk4_method(f, np.array([1.0]), 0.0, 1.0, dt=0.01)
        exact = np.exp(-1.0)
        assert abs(y[-1, 0] - exact) < 0.001

    def test_harmonic_oscillator(self):
        """Harmonic oscillator: d²x/dt² = -x"""

        def f(t, y):
            x, v = y
            return np.array([v, -x])

        t, y = rk4_method(f, np.array([1.0, 0.0]), 0.0, 10.0, dt=0.01)
        energy = y[:, 0] ** 2 + y[:, 1] ** 2
        assert np.allclose(energy, 1.0, atol=0.1)

    def test_exponential_growth(self):
        def f(t, y):
            return y

        t, y = rk4_method(f, np.array([1.0]), 0.0, 1.0, dt=0.005)
        exact = np.exp(1.0)
        assert abs(y[-1, 0] - exact) < 0.01


class TestHeatEquation:
    def test_heat_decay(self):
        """Heat should decay over time."""
        x, t, u = heat_equation_explicit(L=1.0, T=0.5, nx=50, nt=100)
        assert u[-1].max() < u[0].max()

    def test_boundary_conditions(self):
        """Boundaries should stay at zero."""
        x, t, u = heat_equation_explicit(L=1.0, T=1.0, nx=50, nt=100)
        assert abs(u[:, 0]).max() < 1e-10
        assert abs(u[:, -1]).max() < 1e-10

    def test_initial_condition(self):
        """Initial condition should be sin(pi*x)."""
        x, t, u = heat_equation_explicit(L=1.0, T=0.01, nx=50, nt=1)
        expected = np.sin(np.pi * x)
        np.testing.assert_allclose(u[0], expected, atol=1e-4)


class TestWaveEquation:
    def test_wave_boundary_conditions(self):
        """Boundaries should stay at zero."""
        x, t, u = wave_equation_explicit(L=1.0, T=1.0, nx=50, nt=100)
        assert abs(u[:, 0]).max() < 1e-10
        assert abs(u[:, -1]).max() < 1e-10

    def test_wave_symmetry(self):
        """Initial sin(pi*x) should maintain symmetry."""
        x, t, u = wave_equation_explicit(L=1.0, T=0.5, nx=50, nt=100)
        mid = len(x) // 2
        assert abs(u[-1, mid]) < 0.1


class TestStabilityMatrix:
    def test_stable_system(self):
        """Both eigenvalues negative -> stable."""
        A = np.array([[-1.0, 0.0], [0.0, -2.0]])
        eigvals, is_stable = stability_matrix(A)
        assert is_stable

    def test_unstable_system(self):
        """Positive real part eigenvalue -> unstable."""
        A = np.array([[1.0, 0.0], [0.0, -1.0]])
        eigvals, is_stable = stability_matrix(A)
        assert not is_stable

    def test_neutral_stability(self):
        """Pure imaginary eigenvalues -> marginal (not strictly stable)."""
        A = np.array([[0.0, -1.0], [1.0, 0.0]])
        eigvals, is_stable = stability_matrix(A)
        # 实部为0，通常不算严格稳定
        assert not is_stable


class TestLyapunovExponent:
    def test_negative_exponent_stable(self):
        """Stable trajectory should have negative exponent."""
        t = np.linspace(0, 5, 100)
        traj = np.array([[np.exp(-t_i), 0.0] for t_i in t])
        lyap = lyapunov_exponent(traj, dt=0.05)
        assert lyap < 0

    def test_positive_exponent_divergence(self):
        """Divergent trajectory should have positive exponent."""
        t = np.linspace(0, 2, 100)
        traj = np.array([[np.exp(t_i), 0.0] for t_i in t])
        lyap = lyapunov_exponent(traj, dt=0.02)
        assert lyap > 0


class TestSolveIVP:
    def test_solve_ivp_euler(self):
        def f(t, y):
            return -y

        t, y = solve_ivp(f, np.array([1.0]), (0.0, 1.0), method="euler", dt=0.001)
        assert len(t) > 0

    def test_solve_ivp_rk4(self):
        def f(t, y):
            return -y

        t, y = solve_ivp(f, np.array([1.0]), (0.0, 1.0), method="rk4", dt=0.01)
        exact = np.exp(-1.0)
        assert abs(y[-1, 0] - exact) < 0.001

    def test_solve_ivp_invalid_method(self):
        def f(t, y):
            return -y

        with pytest.raises(ValueError):
            solve_ivp(f, np.array([1.0]), (0.0, 1.0), method="invalid")
