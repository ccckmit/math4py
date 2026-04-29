"""微分方程定理驗證。

驗證數值解法是否滿足理論性質。
"""

import numpy as np
from typing import Callable, Tuple
from math4py.differential_equation.function import (
    euler_method,
    rk4_method,
    heat_equation_explicit,
    wave_equation_explicit,
    lyapunov_exponent,
)


def euler_convergence_order(f: Callable, y0: np.ndarray, t_span: Tuple[float, float]) -> float:
    """驗證歐拉法收斂階為 1。

    當步長減半時，誤差應減半。

    Args:
        f: 導函數
        y0: 初始值
        t_span: (t0, tf)

    Returns:
        實際收斂階
    """
    dts = [0.01, 0.005, 0.0025]
    errors = []
    for dt in dts:
        t, y = euler_method(f, y0, t_span[0], t_span[1], dt)
        exact = np.exp(-t[-1]) if y0[0] == 1.0 else 0.0
        errors.append(abs(y[-1, 0] - exact))
    # 計算收斂階 log(e1/e2) / log(dt1/dt2)
    order = np.log(errors[0] / errors[1]) / np.log(dts[0] / dts[1])
    return order


def rk4_superior_to_euler(f: Callable, y0: np.ndarray, t_span: Tuple[float, float], dt: float = 0.01) -> bool:
    """驗證 RK4 比歐拉法更精確。

    Args:
        f: 導函數
        y0: 初始值
        t_span: 時間範圍
        dt: 步長

    Returns:
        True 如果 RK4 誤差更小
    """
    t_eu, y_eu = euler_method(f, y0, t_span[0], t_span[1], dt)
    t_rk, y_rk = rk4_method(f, y0, t_span[0], t_span[1], dt)
    exact = np.exp(-t_eu[-1])
    err_eu = abs(y_eu[-1, 0] - exact)
    err_rk = abs(y_rk[-1, 0] - exact)
    return err_rk < err_eu


def heat_equation_decay_rate(alpha: float = 0.01) -> float:
    """熱傳導方程解應以 e^{-απ²t} 速率衰減。

    Args:
        alpha: 熱擴散係數

    Returns:
        衰減常數估計值
    """
    x, t, u = heat_equation_explicit(L=1.0, T=1.0, alpha=alpha, nt=200)
    max_amplitudes = np.max(np.abs(u), axis=1)
    log_amplitudes = np.log(max_amplitudes + 1e-12)
    # 線性擬合 log(A) = -λ t + C
    coeffs = np.polyfit(t, log_amplitudes, 1)
    return -coeffs[0]


def wave_equation_energy_conservation(c: float = 1.0) -> float:
    """波動方程應保持能量守恒。

    離散能量 E_n = Σ (u_t)² + c² (u_x)² 應近似常數。

    Args:
        c: 波速

    Returns:
        能量變化率（應接近 0）
    """
    x, t, u = wave_equation_explicit(L=1.0, T=0.5, c=c, nx=100, nt=200)
    dx = x[1] - x[0]
    dt = t[1] - t[0]
    energies = []
    for n in range(1, len(t)-1):
        ut = (u[n+1] - u[n-1]) / (2*dt)
        ux = (u[n, 1:] - u[n, :-1]) / dx
        E = np.sum(ut**2) + c**2 * np.sum(ux**2)
        energies.append(E)
    return np.std(energies) / np.mean(energies)


def stability_criterion_heat(r: float) -> bool:
    """顯式熱方程穩定條件 r = αΔt/Δx² ≤ 0.5。

    Args:
        r: 網格比

    Returns:
        True 如果穩定
    """
    return r <= 0.5


def stability_criterion_wave(r: float) -> bool:
    """顯式波動方程穩定條件 r = (cΔt/Δx)² ≤ 1。

    Args:
        r: 網格比

    Returns:
        True 如果穩定
    """
    return r <= 1.0


def lyapunov_negative_stable_fixed_point() -> bool:
    """穩定固定點的李雅普諾夫指數應為負。"""
    t = np.linspace(0, 5, 200)
    traj = np.array([[np.exp(-t_i), 0.0] for t_i in t])
    lyap = lyapunov_exponent(traj, dt=0.025)
    return lyap < 0


def lyapunov_positive_unstable_spiral() -> bool:
    """發散軌跡的李雅普諾夫指數應為正。"""
    t = np.linspace(0, 3, 300)
    traj = np.array([[np.exp(t_i) * np.cos(t_i), np.exp(t_i) * np.sin(t_i)] for t_i in t])
    lyap = lyapunov_exponent(traj, dt=0.01)
    return lyap > 0


__all__ = [
    "euler_convergence_order",
    "rk4_superior_to_euler",
    "heat_equation_decay_rate",
    "wave_equation_energy_conservation",
    "stability_criterion_heat",
    "stability_criterion_wave",
    "lyapunov_negative_stable_fixed_point",
    "lyapunov_positive_unstable_spiral",
]
