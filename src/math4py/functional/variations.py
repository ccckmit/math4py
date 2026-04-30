"""變分法（Calculus of Variations）基礎函數。"""

import numpy as np
from typing import Callable


def shortest_path_length(f: Callable, a: float, b: float, n: int = 1000) -> float:
    """計算路徑 y=f(x) 的長度 ∫√(1 + (f')²) dx。"""
    x = np.linspace(a, b, n)
    y = f(x)
    # 確保 y 是數組
    y = np.asarray(y)
    # 使用 np.gradient 計算導數
    dy_dx = np.gradient(y, x)
    integrand = np.sqrt(1.0 + dy_dx**2)
    return np.trapezoid(integrand, x)


def geodesic_plane(a: float, b: float) -> float:
    """平面上的最短路徑（直線）長度。"""
    return abs(b - a)


def brachistochrone_time(y0: float, y1: float, g: float = 9.81) -> float:
    """最速降線時間（簡化版）。"""
    h = abs(y1 - y0)
    if h == 0:
        return 0.0
    return np.sqrt(2.0 * h / g)


def euler_lagrange_simple(y_prime: np.ndarray, x: np.ndarray) -> np.ndarray:
    """簡化版歐拉-拉格朗日方程，適用於 L = L(y') 的情況。
    
    對於 L = F(y')，方程為 d/dx(∂L/∂y') = 0。
    返回 d/dx(y') = y''。
    """
    return np.gradient(y_prime, x)


__all__ = [
    "shortest_path_length",
    "geodesic_plane",
    "brachistochrone_time",
    "euler_lagrange_simple",
]
