"""電漿體物理（Plasma Physics）基礎函數。"""

import numpy as np

# 物理常數
ELECTRON_CHARGE = 1.602176634e-19  # C
ELECTRON_MASS = 9.10938356e-31  # kg
EPSILON_0 = 8.8541878128e-12  # F/m


def debye_length(T_e: float, n_e: float, T_i: float = None, Z: int = 1) -> float:
    """德拜長度 λ_D = sqrt(ε0 k T_e / (n_e e²))。"""
    k = 1.380649e-23
    if T_i is None:
        T_i = T_e
    return np.sqrt(EPSILON_0 * k * T_e / (n_e * ELECTRON_CHARGE**2))


def plasma_frequency(n_e: float) -> float:
    """電漿體頻率 ω_p = sqrt(n_e e² / (ε0 m_e))。"""
    return np.sqrt(n_e * ELECTRON_CHARGE**2 / (EPSILON_0 * ELECTRON_MASS))


def cyclotron_frequency(B: float, q: float = ELECTRON_CHARGE, m: float = ELECTRON_MASS) -> float:
    """迴旋頻率 ω_c = qB/m。"""
    return q * B / m


def larmor_radius(
    v_perp: float, B: float, m: float = ELECTRON_MASS, q: float = ELECTRON_CHARGE
) -> float:
    """拉莫爾半徑 r_L = mv_perp / (qB)。"""
    if B == 0:
        return float("inf")
    return m * v_perp / (q * B)


def alfven_speed(B: float, mu0: float, rho: float) -> float:
    """阿爾芬速度 v_A = B / sqrt(μ0 ρ)。"""
    if rho == 0:
        return float("inf")
    return B / np.sqrt(mu0 * rho)


def sound_speed_ionacoustic(T_e: float, T_i: float, m_i: float) -> float:
    """離子聲速 c_s = sqrt(k(T_e + γ T_i) / m_i)。"""
    k = 1.380649e-23
    return np.sqrt(k * (T_e + 1.67 * T_i) / m_i)


def collision_frequency(n_e: float, T_e: float) -> float:
    """碰撞頻率 ν_ei（簡化）。"""
    k = 1.380649e-23
    m_e = 9.10938356e-31  # 電子質量
    return (
        n_e
        * ELECTRON_CHARGE**4
        / (4.0 * EPSILON_0**2 * np.sqrt(k**3 * T_e**3 / m_e))
        * 4.0
        * np.sqrt(np.pi)
    )


def plasma_beta(B: float, n_e: float, T_e: float) -> float:
    """電漿體比 β = nkT / (B²/(2μ0))。"""
    mu0 = 4.0e-7 * np.pi
    k = 1.380649e-23
    return (n_e * k * T_e) / (B**2 / (2.0 * mu0))


def debye_number(n_e: float, lambda_D: float) -> float:
    """德拜數 N_D = n_e λ_D³。"""
    return n_e * lambda_D**3


def magnetization_parameter(sigma: float, B: float) -> float:
    """磁化參數 β = σ/(ω_p ε0)。"""
    omega_p = plasma_frequency(sigma)  # 簡化：假設 sigma 是 n_e
    return sigma / (omega_p * EPSILON_0)


def two_stream_instability_growth(omega_p: float, v0: float, k: float) -> complex:
    """雙流不穩定性增長率 γ = Im(ω)。"""
    # 簡化：γ = k v0 - ω_p
    return 1j * max(0, k * v0 - omega_p)


__all__ = [
    "debye_length",
    "plasma_frequency",
    "cyclotron_frequency",
    "larmor_radius",
    "alfven_speed",
    "sound_speed_ionacoustic",
    "collision_frequency",
    "plasma_beta",
    "debye_number",
]
