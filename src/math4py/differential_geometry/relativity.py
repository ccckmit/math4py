"""相對論數學函數。

狹義相對論與廣義相對論的基本數學運算。
"""

from typing import Tuple
import numpy as np
from .function import (
    metric_inverse,
    schwarzschild_metric,
    friedmann_metric,
    metric_determinant,
    sqrt_metric_det,
    christoffel,
    ricci_tensor,
    ricci_scalar,
    riemann_curvature,
    kretschmann_scalar,
    einstein_tensor,
    geodesic_equation,
    energy_momentum_perfect_fluid,
    Weyl_tensor,
)
from ..tensor.tensor import Tensor


# 光速常數 (簡化取 c=1)
_C = 1.0


def lorentz_factor(v: np.ndarray) -> float:
    """勞侖茲因子 γ = 1/√(1 - v²/c²)。

    Args:
        v: 速度向量

    Returns:
        勞侖茲因子 γ
    """
    v_norm = np.linalg.norm(v)
    if v_norm >= _C:
        raise ValueError("速度不可超過光速")
    return 1.0 / np.sqrt(1.0 - (v_norm / _C) ** 2)


def lorentz_boost(beta: np.ndarray) -> np.ndarray:
    """勞侖茲變換矩陣 Λ。

    沿給定方向以速度 v = βc 進行勞侖茲變換。
    此處實現沿 x 軸的 boost，β = v/c。

    Args:
        beta: 速度除以光速 (β = v/c)

    Returns:
        4x4 勞侖茲變換矩陣
    """
    beta_x = beta[0] if len(beta) >= 1 else 0.0
    gamma = 1.0 / np.sqrt(1.0 - beta_x ** 2)
    Lambda = np.eye(4)
    Lambda[0, 0] = gamma
    Lambda[0, 1] = -gamma * beta_x
    Lambda[1, 0] = -gamma * beta_x
    Lambda[1, 1] = gamma
    return Lambda


def time_dilation(gamma: float) -> float:
    """時間膨脹 Δt' = γ Δt。

    Args:
        gamma: 勞侖茲因子

    Returns:
        時間膨脹因子
    """
    return gamma


def length_contraction(gamma: float) -> float:
    """長度收縮 L' = L/γ。

    Args:
        gamma: 勞侖茲因子

    Returns:
        長度收縮因子 (1/γ)
    """
    return 1.0 / gamma


def relativistic_momentum(m: float, v: np.ndarray) -> np.ndarray:
    """相對論動量 p = γ m v。

    Args:
        m: 靜止質量
        v: 速度向量

    Returns:
        相對論動量向量
    """
    gamma = lorentz_factor(v)
    return gamma * m * v


def relativistic_energy(m: float, v: np.ndarray) -> float:
    """相對論能量 E = γ m c² (c=1 時為 γ m)。

    Args:
        m: 靜止質量
        v: 速度向量

    Returns:
        相對論能量
    """
    gamma = lorentz_factor(v)
    return gamma * m * (_C ** 2)


def mass_energy_equivalence(m: float) -> float:
    """質能等價 E = m c²。

    Args:
        m: 質量

    Returns:
        能量 E
    """
    return m * (_C ** 2)


def four_velocity(v: np.ndarray) -> np.ndarray:
    """四維速度 U^μ = γ(c, v)。

    Args:
        v: 三維速度向量

    Returns:
        四維速度 (ct, vx, vy, vz)
    """
    gamma = lorentz_factor(v)
    U = np.zeros(4)
    U[0] = gamma * _C
    U[1:1+len(v)] = gamma * v
    return U


def four_momentum(m: float, v: np.ndarray) -> np.ndarray:
    """四維動量 P^μ = (E/c, p)。

    Args:
        m: 靜止質量
        v: 三維速度向量

    Returns:
        四維動量 (E/c, px, py, pz)
    """
    gamma = lorentz_factor(v)
    E = relativistic_energy(m, v)
    p = relativistic_momentum(m, v)
    P = np.zeros(4)
    P[0] = E / _C
    P[1:1+len(p)] = p
    return P


def schwarzschild_radius(m: float) -> float:
    """史瓦西半徑 r_s = 2GM/c² (取 G=1, c=1 時為 2M)。

    Args:
        m: 質量

    Returns:
        史瓦西半徑
    """
    G = 1.0
    return 2.0 * G * m / (_C ** 2)


def proper_time(minkowski_metric: Tensor, dx: np.ndarray) -> float:
    """原時 dτ² = -η_μν dx^μ dx^ν (c=1, 號差 -+++)。

    Args:
        minkowski_metric: 閔可夫斯基度規
        dx: 四維位移向量

    Returns:
        原時 dτ
    """
    ds2 = np.dot(dx, np.dot(minkowski_metric.data, dx))
    if ds2 < 0:
        return np.sqrt(-ds2)
    return np.sqrt(ds2)


def geodesic_in_schwarzschild(L: float, tau: float, initial_pos: np.ndarray) -> Tensor:
    """在史瓦西度規下的測地線方程。

    Args:
        L: 角動量
        tau: 仿射參數
        initial_pos: 初始位置

    Returns:
        位置張量
    """
    return geodesic_equation(
        schwarzschild_metric(1.0, 1.0),
        Tensor(np.zeros(4)),
        Tensor(initial_pos),
        L,
        tau
    )


def hubble_law(D: float, H0: float = 70.0) -> float:
    """哈伯定律 v = H0 D。

    Args:
        D: 距離 (Mpc)
        H0: 哈伯常數 (km/s/Mpc)

    Returns:
        退行速度 v (km/s)
    """
    return H0 * D


def friedmann_equation(a: float, rho: float, k: float = 0.0, Lambda: float = 0.0) -> float:
    """弗里德曼方程 H² = (8πG/3c²)ρ + Λ/3 - k/a²。

    簡化取 G=c=1: H² = (8π/3)ρ + Λ/3 - k/a²

    Args:
        a: 尺度因子
        rho: 能量密度
        k: 曲率 (0, ±1)
        Lambda: 宇宙學常數

    Returns:
        H² 值
    """
    G = 1.0
    H2 = (8.0 * np.pi * G / 3.0) * rho + Lambda / 3.0 - k / (a ** 2)
    return H2


__all__ = [
    "lorentz_factor",
    "lorentz_boost",
    "time_dilation",
    "length_contraction",
    "relativistic_momentum",
    "relativistic_energy",
    "mass_energy_equivalence",
    "four_velocity",
    "four_momentum",
    "schwarzschild_radius",
    "proper_time",
    "geodesic_in_schwarzschild",
    "hubble_law",
    "friedmann_equation",
]
