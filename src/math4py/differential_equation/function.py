"""微分方程數值解法。

包含常微分方程(ODE)與偏微分方程(PDE)的數值解法。
"""

from typing import Callable, Tuple

import numpy as np

# ODE 解法


def euler_method(
    f: Callable[[float, np.ndarray], np.ndarray],
    y0: np.ndarray,
    t0: float,
    tf: float,
    dt: float = 0.01,
) -> Tuple[np.ndarray, np.ndarray]:
    """歐拉法求解 ODE: dy/dt = f(t, y)。

    Args:
        f: 導函數函數 f(t, y) -> dy/dt
        y0: 初始條件
        t0: 起始時間
        tf: 終止時間
        dt: 時間步長

    Returns:
        (t_array, y_array)
    """
    n_steps = int((tf - t0) / dt)
    t_arr = np.linspace(t0, tf, n_steps + 1)
    y_arr = np.zeros((n_steps + 1, len(y0)))
    y_arr[0] = y0

    for i in range(n_steps):
        y_arr[i + 1] = y_arr[i] + dt * f(t_arr[i], y_arr[i])

    return t_arr, y_arr


def rk2_method(
    f: Callable[[float, np.ndarray], np.ndarray],
    y0: np.ndarray,
    t0: float,
    tf: float,
    dt: float = 0.01,
) -> Tuple[np.ndarray, np.ndarray]:
    """二階龍格-庫塔法 (RK2/ midpoint method)。

    Args:
        f: 導函數函數
        y0: 初始條件
        t0, tf: 時間範圍
        dt: 步長

    Returns:
        (t_array, y_array)
    """
    n_steps = int((tf - t0) / dt)
    t_arr = np.linspace(t0, tf, n_steps + 1)
    y_arr = np.zeros((n_steps + 1, len(y0)))
    y_arr[0] = y0

    for i in range(n_steps):
        k1 = f(t_arr[i], y_arr[i])
        k2 = f(t_arr[i] + dt / 2, y_arr[i] + dt / 2 * k1)
        y_arr[i + 1] = y_arr[i] + dt * k2

    return t_arr, y_arr


def rk4_method(
    f: Callable[[float, np.ndarray], np.ndarray],
    y0: np.ndarray,
    t0: float,
    tf: float,
    dt: float = 0.01,
) -> Tuple[np.ndarray, np.ndarray]:
    """四階龍格-庫塔法 (RK4)。

    Args:
        f: 導函數函數
        y0: 初始條件
        t0, tf: 時間範圍
        dt: 步長

    Returns:
        (t_array, y_array)
    """
    n_steps = int((tf - t0) / dt)
    t_arr = np.linspace(t0, tf, n_steps + 1)
    y_arr = np.zeros((n_steps + 1, len(y0)))
    y_arr[0] = y0

    for i in range(n_steps):
        k1 = f(t_arr[i], y_arr[i])
        k2 = f(t_arr[i] + dt / 2, y_arr[i] + dt / 2 * k1)
        k3 = f(t_arr[i] + dt / 2, y_arr[i] + dt / 2 * k2)
        k4 = f(t_arr[i] + dt, y_arr[i] + dt * k3)
        y_arr[i + 1] = y_arr[i] + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return t_arr, y_arr


# PDE 解法


def heat_equation_explicit(
    L: float = 1.0, T: float = 1.0, nx: int = 50, nt: int = 100, alpha: float = 0.01
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """顯式有限差分法解熱傳導方程 ∂u/∂t = α ∂²u/∂x²。

    Args:
        L: 空間範圍 [0, L]
        T: 時間範圍 [0, T]
        nx: 空間格點數
        nt: 時間步數
        alpha: 熱擴散係數

    Returns:
        (x_grid, t_grid, u_solution)
    """
    dx = L / (nx - 1)
    dt = T / nt
    r = alpha * dt / (dx**2)

    x = np.linspace(0, L, nx)
    t = np.linspace(0, T, nt + 1)
    u = np.zeros((nt + 1, nx))

    # 初始條件: u(x,0) = sin(πx)
    u[0] = np.sin(np.pi * x)

    for n in range(nt):
        for i in range(1, nx - 1):
            u[n + 1, i] = u[n, i] + r * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])
        # 邊界條件: u(0,t) = u(L,t) = 0
        u[n + 1, 0] = 0
        u[n + 1, -1] = 0

    return x, t, u


def wave_equation_explicit(
    L: float = 1.0, T: float = 1.0, nx: int = 50, nt: int = 100, c: float = 1.0
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """顯式有限差分法解波動方程 ∂²u/∂t² = c² ∂²u/∂x²。

    Args:
        L: 空間範圍
        T: 時間範圍
        nx, nt: 格點數
        c: 波速

    Returns:
        (x_grid, t_grid, u_solution)
    """
    dx = L / (nx - 1)
    dt = T / nt
    r = (c * dt / dx) ** 2

    x = np.linspace(0, L, nx)
    t = np.linspace(0, T, nt + 1)
    u = np.zeros((nt + 1, nx))

    # 初始條件: u(x,0) = sin(πx), ∂u/∂t(x,0) = 0
    u[0] = np.sin(np.pi * x)
    # 第一時間步
    for i in range(1, nx - 1):
        u[1, i] = u[0, i] + 0.5 * r * (u[0, i + 1] - 2 * u[0, i] + u[0, i - 1])
    u[1, 0] = 0
    u[1, -1] = 0

    for n in range(1, nt):
        for i in range(1, nx - 1):
            u[n + 1, i] = 2 * u[n, i] - u[n - 1, i] + r * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])
        u[n + 1, 0] = 0
        u[n + 1, -1] = 0

    return x, t, u


# 系統分析


def stability_matrix(A: np.ndarray) -> Tuple[np.ndarray, bool]:
    """計算線性系統 dy/dt = A y 的穩定性。

    Args:
        A: 係數矩陣

    Returns:
        (eigenvalues, is_stable)
    """
    eigvals = np.linalg.eigvals(A)
    is_stable = np.all(np.real(eigvals) < 0)
    return eigvals, is_stable


def lyapunov_exponent(traj: np.ndarray, dt: float = 0.01) -> float:
    """估算軌跡的最大李雅普諾夫指數。

    Args:
        traj: 軌跡數組 (n_steps, n_dim)
        dt: 時間步長

    Returns:
        最大李雅普諾夫指數
    """
    n = len(traj)
    divergences = []

    for i in range(1, n):
        delta = traj[i] - traj[i - 1]
        norm = np.linalg.norm(delta)
        if norm > 1e-12:
            divergences.append(np.log(norm / dt))

    return np.mean(divergences) if divergences else 0.0


def solve_ivp(
    f: Callable[[float, np.ndarray], np.ndarray],
    y0: np.ndarray,
    t_span: Tuple[float, float],
    method: str = "rk4",
    dt: float = 0.01,
) -> Tuple[np.ndarray, np.ndarray]:
    """統一介面求解初值問題。

    Args:
        f: 導函數
        y0: 初始值
        t_span: (t0, tf)
        method: "euler", "rk2", "rk4"
        dt: 步長

    Returns:
        (t, y)
    """
    if method == "euler":
        return euler_method(f, y0, t_span[0], t_span[1], dt)
    elif method == "rk2":
        return rk2_method(f, y0, t_span[0], t_span[1], dt)
    elif method == "rk4":
        return rk4_method(f, y0, t_span[0], t_span[1], dt)
    else:
        raise ValueError(f"Unknown method: {method}")


__all__ = [
    "euler_method",
    "rk2_method",
    "rk4_method",
    "heat_equation_explicit",
    "wave_equation_explicit",
    "stability_matrix",
    "lyapunov_exponent",
    "solve_ivp",
]
