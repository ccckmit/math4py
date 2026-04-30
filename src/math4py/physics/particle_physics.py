"""粒子物理（Particle Physics）基礎函數。"""

import numpy as np
from typing import List, Dict


# 基本粒子質量 (MeV/c²)
ELECTRON_MASS = 0.511  # MeV
MUON_MASS = 105.7  # MeV
TAU_MASS = 1776.86  # MeV
QUARK_U_MASS = 2.2  # MeV (上夸克)
QUARK_D_MASS = 4.7  # MeV (下夸克)
QUARK_STRANGE_MASS = 96.0  # MeV (奇夸克)


def lorentz_invariant_mass(particles: List[Dict]) -> float:
    """不變質量 m² = (ΣE)² - |Σp|²c²。
    
    Args:
        particles: [{"E": energy, "px": px, "py": py, "pz": pz}, ...]
    
    Returns:
        不變質量 (MeV/c²)
    """
    total_E = sum(p["E"] for p in particles)
    total_px = sum(p["px"] for p in particles)
    total_py = sum(p["py"] for p in particles)
    total_pz = sum(p["pz"] for p in particles)
    
    m2 = total_E**2 - (total_px**2 + total_py**2 + total_pz**2)
    return np.sqrt(max(0, m2))


def decay_width_to_lifetime(Gamma: float) -> float:
    """衰變寬度與壽命關係 τ = ℏ/Γ。"""
    hbar = 6.582119569e-22  # MeV·s
    if Gamma == 0:
        return float('inf')
    return hbar / Gamma


def branching_ratio(width_partial: float, width_total: float) -> float:
    """分支比 BR = Γ_i/Γ_total。"""
    if width_total == 0:
        return 0.0
    return width_partial / width_total


def center_of_mass_energy(sqrt_s: float) -> float:
    """質心能量 √s。"""
    return sqrt_s


def relativistic_kinetic_energy(m0: float, p: float) -> float:
    """相對論動能 T = sqrt(p²c² + m0²c⁴) - m0c²。"""
    c = 299792458e-3  # m/s to mm/ns (簡化)
    m0c2 = m0  # 假設輸入為 MeV，c=1 單位
    pc = p  # 簡化
    return np.sqrt(pc**2 + m0c2**2) - m0c2


def cross_section_point_like(sqrt_s: float, m0: float) -> float:
    """點狀粒子散射截面（簡化）。"""
    if sqrt_s <= 2 * m0:
        return 0.0  # 閾值
    # 簡化公式
    return 1.0 / (sqrt_s**2)


def ckms_matrix_element(V_us: float, V_ub: float, V_cb: float) -> np.ndarray:
    """CKM 矩陣（Cabibbo-Kobayashi-Maskawa）。"""
    V_cd = np.sqrt(1.0 - V_us**2 - V_ub**2)  # 近似
    V_cs = -V_us * V_cd / V_ud if V_ud != 0 else 0  # 簡化
    V_td = 0.0  # 簡化
    V_ts = 0.0
    V_tb = 1.0
    
    return np.array([
        [V_ud, V_us, V_ub],
        [V_cd, V_cs, V_cb],
        [V_td, V_ts, V_tb]
    ])


def particle_composition(particle: str) -> List[str]:
    """粒子組成（標準模型）。"""
    compositions = {
        "proton": ["u", "u", "d"],
        "neutron": ["u", "d", "d"],
        "pion+": ["u", "anti-d"],
        "kaon+": ["u", "anti-s"],
        "electron": ["e-"],
        "photon": ["γ"],
        "gluon": ["g"],
    }
    return compositions.get(particle, [])


__all__ = [
    "lorentz_invariant_mass",
    "decay_width_to_lifetime",
    "branching_ratio",
    "center_of_mass_energy",
    "cross_section_point_like",
    "particle_composition",
]
