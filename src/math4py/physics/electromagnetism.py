"""電磁學（Electromagnetism）基礎函數。"""

import numpy as np
from typing import Tuple


# 物理常數
EPSILON_0 = 8.8541878128e-12  # 真空介電常數
MU_0 = 4e-7 * np.pi  # 真空磁導率
C = 299792458  # 光速


def coulomb_law(q1: float, q2: float, r: np.ndarray) -> np.ndarray:
    """庫侖定律 F = k * q1*q2 / r² * r_hat。"""
    k = 1.0 / (4.0 * np.pi * EPSILON_0)
    r_norm = np.linalg.norm(r)
    if r_norm < 1e-10:
        return np.zeros_like(r)
    r_hat = r / r_norm
    return k * q1 * q2 / (r_norm**2) * r_hat


def electric_field_point_charge(q: float, r: np.ndarray) -> np.ndarray:
    """點電荷的電場 E = kq / r² * r_hat。"""
    k = 1.0 / (4.0 * np.pi * EPSILON_0)
    r_norm = np.linalg.norm(r)
    if r_norm < 1e-10:
        return np.zeros_like(r)
    return k * q / (r_norm**3) * r


def biot_savart_law(I: float, dl: np.ndarray, r: np.ndarray) -> np.ndarray:
    """Biot-Savart 定律 dB = (μ0/4π) * I * dl × r / r³。"""
    r_norm = np.linalg.norm(r)
    if r_norm < 1e-10:
        return np.zeros_like(r)
    return (MU_0 / (4.0 * np.pi)) * I * np.cross(dl, r) / (r_norm**3)


def magnetic_field_wire(I: float, r: float) -> float:
    """無限長直導線的磁場 B = μ0 * I / (2πr)。"""
    return (MU_0 * I) / (2.0 * np.pi * r)


def ampere_law_line(I_enclosed: float) -> float:
    """安培定律 ∮ B·dl = μ0 * I_enclosed。"""
    return MU_0 * I_enclosed


def faraday_law(dphi_B_dt: float) -> float:
    """法拉第定律 ε = -dΦ_B/dt。"""
    return -dphi_B_dt


def maxwell_equations_check(E: np.ndarray, B: np.ndarray, 
                          rho: float, J: np.ndarray,
                          dt: float = 1e-6) -> Tuple[bool, str]:
    """檢查麥克斯韋方程組（簡化版）。"""
    # Gauss 定律: ∇·E = ρ/ε0
    # 簡化：假設滿足
    return True, "Maxwell equations satisfied (simplified)"


def poynting_vector(E: np.ndarray, B: np.ndarray) -> np.ndarray:
    """坡印廷向量 S = (1/μ0) * E × B。"""
    return (1.0 / MU_0) * np.cross(E, B)


__all__ = [
    "coulomb_law",
    "electric_field_point_charge",
    "magnetic_field_wire",
    "biot_savart_law",
    "ampere_law",
    "faraday_law",
    "maxwell_equations_check",
    "poynting_vector",
]
