"""天體物理（Astrophysics）基礎函數。"""

import numpy as np
from typing import Tuple


# 物理常數
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³ kg⁻¹ s⁻²
SOLAR_MASS = 1.9885e30  # kg
SOLAR_RADIUS = 6.957e8  # m
LUMINOSITY_SUN = 3.828e26  # W
PARSEC = 3.085677581e16  # m


def schwarzschild_radius(M: float) -> float:
    """史瓦西半徑 R_s = 2GM/c²。"""
    c = 299792458
    return 2.0 * GRAVITATIONAL_CONSTANT * M / c**2


def orbital_velocity(M: float, r: float) -> float:
    """軌道速度 v = sqrt(GM/r)。"""
    if r == 0:
        return float('inf')
    return np.sqrt(GRAVITATIONAL_CONSTANT * M / r)


def escape_velocity(M: float, r: float) -> float:
    """逃逸速度 v_esc = sqrt(2GM/r)。"""
    return np.sqrt(2.0 * GRAVITATIONAL_CONSTANT * M / r)


def hubble_law(v: float = None, d: float = None, 
                 H0: float = 70.0) -> dict:
    """哈勃定律 v = H0 * d。
    
    H0: 哈勃常數 (km/s/Mpc)，預設 70
    """
    if v is None and d is not None:
        return {"v": H0 * d / 3.086e19}  # 轉換 Mpc to m
    elif d is None and v is not None:
        return {"d": v * 3.086e19 / H0}  # 轉換 to Mpc
    return {"H0": H0}


def stefan_boltzmann_luminosity(R: float, T: float) -> float:
    """恆星光度 L = 4πR² σ T⁴。"""
    sigma = 5.670374419e-8
    return 4.0 * np.pi * R**2 * sigma * T**4


def cosmological_redshift(d: float, H0: float = 70.0) -> float:
    """宇宙學紅移 z = H0 * d / c（哈勃定律近似）。"""
    c = 299792458e-3  # km/s
    return H0 * d / c


def kepler_third_law(P: float = None, a: float = None, 
                     M: float = None) -> dict:
    """克卜勒第三定律 P² = 4π² a³/(GM)。"""
    if P is None and all([a, M]):
        return {"P": np.sqrt(4.0 * np.pi**2 * a**3 / (GRAVITATIONAL_CONSTANT * M))}
    elif a is None and all([P, M]):
        return {"a": (GRAVITATIONAL_CONSTANT * M * P**2 / (4.0 * np.pi**2))**(1.0/3.0)}
    elif M is None and all([P, a]):
        return {"M": 4.0 * np.pi**2 * a**3 / (GRAVITATIONAL_CONSTANT * P**2)}
    return {}


def tov_near_parsec(d_pc: float, M: float = SOLAR_MASS) -> float:
    """托爾曼-歐本彩距離修正（簡化）。"""
    return d_pc * (1.0 + d_pc / (2.0 * PARSEC))  # 簡化


def main_sequence_lifetime(M: float) -> float:
    """主序星壽命 t ∝ M^-2.5（年）。"""
    return 1e10 * (M / SOLAR_MASS)**(-2.5)  # 年


def jeans_mass(T: float, rho: float, mu: float = 1.67e-27) -> float:
    """金斯質量 M_J = (π/6) (π kT / Gμρ)^(3/2) ρ^(-1/2)。"""
    k = 1.380649e-23
    return (np.pi / 6.0) * (np.pi * k * T / (GRAVITATIONAL_CONSTANT * mu * rho))**1.5 / np.sqrt(rho)


__all__ = [
    "schwarzschild_radius",
    "orbital_velocity",
    "escape_velocity",
    "hubble_law",
    "stefan_boltzmann_luminosity",
    "cosmological_redshift",
    "kepler_third_law",
    "main_sequence_lifetime",
    "jeans_mass",
]
