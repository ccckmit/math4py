"""相對論（Special & General Relativity）計算。"""

import numpy as np
from typing import Tuple

# 光速常數
_C = 299792458  # m/s


def lorentz_factor(v: np.ndarray) -> float:
    """勞侖茲因子 γ = 1/√(1 - v²/c²)。"""
    v_norm = np.linalg.norm(v)
    if v_norm >= _C:
        raise ValueError("速度不可超過光速")
    return 1.0 / np.sqrt(1.0 - (v_norm / _C) ** 2)


def lorentz_transformation(beta: np.ndarray) -> np.ndarray:
    """勞侖茲變換矩陣 Λ。"""
    beta_x = beta[0] if len(beta) >= 1 else 0.0
    gamma = 1.0 / np.sqrt(1.0 - beta_x ** 2)
    Lambda = np.eye(4)
    Lambda[0, 0] = gamma
    Lambda[0, 1] = -gamma * beta_x
    Lambda[1, 0] = -gamma * beta_x
    Lambda[1, 1] = gamma
    return Lambda


def time_dilation(gamma: float) -> float:
    """時間膨脹 Δt' = γ Δt。"""
    return gamma


def length_contraction(gamma: float) -> float:
    """長度收縮 L' = L/γ。"""
    return 1.0 / gamma


def relativistic_momentum(m: float, v: np.ndarray) -> np.ndarray:
    """相對論動量 p = γ m v。"""
    gamma = lorentz_factor(v)
    return gamma * m * v


def relativistic_energy(m: float, v: np.ndarray) -> float:
    """相對論能量 E = γ m c²。"""
    gamma = lorentz_factor(v)
    return gamma * m * _C ** 2


def mass_energy_equivalence(m: float) -> float:
    """質能方程 E = mc²。"""
    return m * _C ** 2


def spacetime_interval(x1, x2) -> float:
    """時空間隔 ds² = -c²dt² + dx² + dy² + dz²（號差 -+++）。"""
    dt = x2[0] - x1[0]
    dx = x2[1] - x1[1]
    dy = x2[2] - x1[2]
    dz = x2[3] - x1[3]
    return -(_C * dt)**2 + dx**2 + dy**2 + dz**2


def schwarzschild_metric(r: float, theta: float = np.pi/2) -> np.ndarray:
    """史瓦西度規。"""
    M = 1.0  # 簡化質量
    Rs = 2 * 6.67430e-11 * M / _C**2  # 史瓦西半徑
    g = np.zeros((4, 4))
    g[0, 0] = -(1 - Rs/r)
    g[1, 1] = 1.0 / (1 - Rs/r)
    g[2, 2] = r**2
    g[3, 3] = r**2 * np.sin(theta)**2
    return g


def friedmann_metric(a: float, t: float) -> np.ndarray:
    """弗里德曼度規（FLRW）。"""
    g = np.zeros((4, 4))
    g[0, 0] = -1.0
    g[1, 1] = a**2
    g[2, 2] = a**2
    g[3, 3] = a**2
    return g


__all__ = [
    "lorentz_factor",
    "lorentz_transformation",
    "time_dilation",
    "length_contraction",
    "relativistic_momentum",
    "relativistic_energy",
    "mass_energy_equivalence",
    "spacetime_interval",
    "schwarzschild_metric",
    "friedmann_metric",
]
