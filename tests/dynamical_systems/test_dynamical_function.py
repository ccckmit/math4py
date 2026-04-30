"""Test dynamical systems function module theorems."""

import numpy as np

import math4py.dynamical_systems.function as ds


class TestEulerMethod:
    def test_linear_ode(self):
        """dy/dt = -y, y(0)=1 的解應為 e^{-t}。"""

        def f(y, t):
            return -y

        t = np.linspace(0, 1, 100)
        y0 = np.array([1.0])
        sol = ds.euler_method(f, y0, t)

        # 檢查最終值是否接近 e^{-1}
        expected = np.exp(-1.0)
        assert abs(sol[-1][0] - expected) < 0.05

    def test_constant_ode(self):
        """dy/dt = 0, y(0)=1 的解應為恆為 1。"""

        def f(y, t):
            return 0.0 * y

        t = np.linspace(0, 1, 50)
        y0 = np.array([1.0])
        sol = ds.euler_method(f, y0, t)

        assert np.allclose(sol[:, 0], 1.0, atol=1e-10)


class TestRungeKutta4:
    def test_linear_ode_rk4(self):
        """RK4 對 dy/dt = -y 應更精確。"""

        def f(y, t):
            return -y

        t = np.linspace(0, 1, 20)
        y0 = np.array([1.0])
        sol = ds.runge_kutta_4(f, y0, t)

        expected = np.exp(-1.0)
        assert abs(sol[-1][0] - expected) < 0.001


class TestPhaseSpaceTrajectory:
    def test_harmonic_oscillator(self):
        """簡諧振子的相空間軌跡。"""

        def f(y, t):
            return np.array([y[1], -y[0]])  # d²x/dt² = -x

        y0 = np.array([1.0, 0.0])
        t, y = ds.phase_space_trajectory(f, y0, (0, 10), n_steps=1000)

        # 能量應守恆
        energy = 0.5 * (y[:, 0] ** 2 + y[:, 1] ** 2)
        assert np.std(energy) < 0.01


class TestFixedPointAnalysis:
    def test_stable_fixed_point(self):
        """f(y) = y - 0.5 的不動點在 y=0.5。"""

        def f(y, t):
            return y - 0.5

        y0 = np.array([0.6])
        fp = ds.fixed_point_analysis(f, y0)
        assert abs(fp[0] - 0.5) < 0.01

    def test_unstable_fixed_point(self):
        """f(y) = y 的不動點在 y=0。"""

        def f(y, t):
            return y

        y0 = np.array([0.1])
        fp = ds.fixed_point_analysis(f, y0)
        # 應收斂到 0
        assert abs(fp[0]) < 0.1


class TestLinearStability:
    def test_stable_matrix(self):
        """特徵值實部 < 0 表示穩定。"""
        A = np.array([[-1.0, 0.0], [0.0, -2.0]])
        eigvals = ds.linear_stability_analysis(A)

        assert np.all(np.real(eigvals) < 0)

    def test_unstable_matrix(self):
        """特徵值實部 > 0 表示不穩定。"""
        A = np.array([[1.0, 0.0], [0.0, -1.0]])
        eigvals = ds.linear_stability_analysis(A)

        assert np.any(np.real(eigvals) > 0)


class TestLorenzSystem:
    def test_lorenz_derivative(self):
        """洛倫茲系統的導數計算。"""
        y = np.array([1.0, 1.0, 1.0])
        dy = ds.lorenz_system(y, 0.0)

        assert len(dy) == 3
        assert dy[0] == 0.0  # sigma*(y-x) = 10*(1-1) = 0

    def test_lorenz_trajectory(self):
        """洛倫茲吸引子的軌跡計算。"""

        def f(y, t):
            return ds.lorenz_system(y, t)

        y0 = np.array([1.0, 1.0, 1.0])
        t, y = ds.phase_space_trajectory(f, y0, (0, 10), n_steps=500)

        assert len(t) == 500
        assert y.shape == (500, 3)


class TestLogisticMap:
    def test_logistic_fixed_point(self):
        """邏輯斯蒂映射在 r=2 時收斂到 0.5。"""
        x = ds.logistic_map(2.0, 0.1, n=1000)

        # 最後的值應接近固定點 1 - 1/r = 0.5
        assert abs(x[-1] - 0.5) < 0.01

    def test_logistic_period_doubling(self):
        """r=3.2 時應出現週期 2。"""
        x = ds.logistic_map(3.2, 0.5, n=1000)
        last_100 = x[-100:]

        # 檢查是否只有兩個值
        unique_vals = np.unique(np.round(last_100, 3))
        assert len(unique_vals) <= 5  # 允許數值誤差


class TestBifurcationDiagram:
    def test_bifurcation_data_shape(self):
        """分岔圖數據形狀正確。"""
        r_vals, x_vals = ds.bifurcation_diagram((2.5, 4.0), n_r=50)

        assert len(r_vals) == len(x_vals)
        assert len(r_vals) == 50 * 100  # n_r * n_plot
