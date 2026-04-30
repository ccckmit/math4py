"""動力系統（Dynamical Systems）基礎函數。"""

import numpy as np
from typing import Callable, Tuple, List


def euler_method(f: Callable, y0: np.ndarray, t: np.ndarray) -> np.ndarray:
    """歐拉法求解常微分方程 dy/dt = f(y, t)。
    
    Args:
        f: 導函數函數 f(y, t)
        y0: 初始條件
        t: 時間陣列
    
    Returns:
        形狀為 (len(t), len(y0)) 的數組
    """
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        y[i] = y[i-1] + dt * f(y[i-1], t[i-1])
    
    return y


def runge_kutta_4(f: Callable, y0: np.ndarray, t: np.ndarray) -> np.ndarray:
    """四階龍格-庫塔法（RK4）求解 ODE。"""
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        h = dt
        
        k1 = f(y[i-1], t[i-1])
        k2 = f(y[i-1] + h*k1/2, t[i-1] + h/2)
        k3 = f(y[i-1] + h*k2/2, t[i-1] + h/2)
        k4 = f(y[i-1] + h*k3, t[i-1] + h)
        
        y[i] = y[i-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return y


def phase_space_trajectory(f: Callable, y0: np.ndarray, t_span: Tuple[float, float], 
                          n_steps: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
    """計算相空間軌跡。"""
    t = np.linspace(t_span[0], t_span[1], n_steps)
    y = runge_kutta_4(f, y0, t)
    return t, y


def fixed_point_analysis(f: Callable, y0: np.ndarray, tol: float = 1e-6, 
                        max_iter: int = 10000) -> np.ndarray:
    """尋找不動點 f(y) = 0（牛頓法）。"""
    y = y0.copy()
    for _ in range(max_iter):
        fy = f(y, 0.0)
        if np.linalg.norm(fy) < tol:
            return y
        # 數值導數
        h = 1e-6
        if y.ndim == 0 or len(y) == 1:
            # 標量情況
            fy_h = f(y + h, 0.0)
            df = (fy_h - fy) / h
            if abs(df) < 1e-10:
                return y
            y = y - fy/df
        else:
            # 向量情況，簡化處理
            y = y - 0.1 * fy
    return y


def linear_stability_analysis(A: np.ndarray) -> np.ndarray:
    """線性穩定性分析：計算雅可比矩陣 A 的特徵值。
    
    特徵值實部 < 0 表示穩定。
    """
    return np.linalg.eigvals(A)


def lyapunov_exponent(f: Callable, y0: np.ndarray, t_span: Tuple[float, float],
                       n_steps: int = 10000) -> float:
    """計算最大李雅普諾夫指數（簡化版）。"""
    t = np.linspace(t_span[0], t_span[1], n_steps)
    y = runge_kutta_4(f, y0, t)
    
    # 簡化：計算軌跡的散度
    dt = t[1] - t[0]
    divergence = np.sum([np.trace(np.eye(len(y0))) for _ in t]) / (n_steps * dt)
    
    return divergence / len(y0)


def lorenz_system(y: np.ndarray, t: float, sigma: float = 10.0, 
                   rho: float = 28.0, beta: float = 8.0/3.0) -> np.ndarray:
    """洛倫茲吸引子 dx/dt = σ(y-x), dy/dt = x(ρ-z) - y, dz/dt = xy - βz。"""
    x, y_coord, z = y
    dx = sigma * (y_coord - x)
    dy = x * (rho - z) - y_coord
    dz = x * y_coord - beta * z
    return np.array([dx, dy, dz])


def logistic_map(r: float, x0: float, n: int = 1000) -> np.ndarray:
    """邏輯斯蒂映射 x_{n+1} = r * x_n * (1 - x_n)。"""
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x


def bifurcation_diagram(r_range: Tuple[float, float], n_r: int = 100, 
                        n_transient: int = 100, n_plot: int = 100) -> Tuple[np.ndarray, np.ndarray]:
    """分岔圖數據（簡化版）。"""
    r_vals = np.linspace(r_range[0], r_range[1], n_r)
    bifurcation_data = []
    
    for r in r_vals:
        x = 0.5
        # 去除瞬態
        for _ in range(n_transient):
            x = r * x * (1 - x)
        # 收集數據
        for _ in range(n_plot):
            x = r * x * (1 - x)
            bifurcation_data.append((r, x))
    
    r_points = np.array([d[0] for d in bifurcation_data])
    x_points = np.array([d[1] for d in bifurcation_data])
    return r_points, x_points


__all__ = [
    "euler_method",
    "runge_kutta_4",
    "phase_space_trajectory",
    "fixed_point_analysis",
    "linear_stability_analysis",
    "lyapunov_exponent",
    "lorenz_system",
    "logistic_map",
    "bifurcation_diagram",
]
