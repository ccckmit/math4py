"""核物理（Nuclear Physics）基礎函數。"""

import numpy as np

# 物理常數
ATOMIC_MASS_UNIT = 1.66053906660e-27  # kg (1 u)
AVOGADRO = 6.02214076e23  # mol⁻¹
ELECTRON_VOLT = 1.602176634e-19  # J


def mass_defect(Z: int, N: int, A: int, m_nucleus: float) -> float:
    """質量虧損 Δm = Z*m_p + N*m_n - m_nucleus。"""
    m_p = 1.007276466621 * ATOMIC_MASS_UNIT  # 質子質量
    m_n = 1.00866491588 * ATOMIC_MASS_UNIT  # 中子質量
    return Z * m_p + N * m_n - m_nucleus


def binding_energy(mass_defect: float) -> float:
    """結合能 E = Δm c²。"""
    c = 299792458
    return mass_defect * c**2


def binding_energy_per_nucleon(binding_energy: float, A: int) -> float:
    """每核子結合能。"""
    if A == 0:
        return 0.0
    return binding_energy / A


def radioactive_decay(N0: float, lambda_: float, t: np.ndarray) -> np.ndarray:
    """放射性衰變 N(t) = N0 exp(-λt)。"""
    return N0 * np.exp(-lambda_ * t)


def decay_constant(half_life: float) -> float:
    """衰變常數 λ = ln(2)/T₁/₂。"""
    if half_life <= 0:
        return float("inf")
    return np.log(2.0) / half_life


def half_life(lambda_: float) -> float:
    """半衰期 T₁/₂ = ln(2)/λ。"""
    if lambda_ == 0:
        return float("inf")
    return np.log(2.0) / lambda_


def activity(N: float, lambda_: float) -> float:
    """放射性活度 A = λN。"""
    return lambda_ * N


def nuclear_radius(A: int, R0: float = 1.2e-15) -> float:
    """原子核半徑 R = R0 * A^(1/3)。"""
    return R0 * (A ** (1.0 / 3.0))


def q_value(reaction_mass_initial: float, reaction_mass_final: float) -> float:
    """核反應 Q 值 Q = (m_initial - m_final) c²。"""
    c = 299792458
    return (reaction_mass_initial - reaction_mass_final) * c**2


def fission_energy_per_nucleon() -> float:
    """裂變平均每核子釋放能量（約 0.9 MeV）。"""
    return 0.9e6 * ELECTRON_VOLT  # J


def fusion_energy_per_nucleon() -> float:
    """聚變平均每核子釋放能量（約 6.7 MeV）。"""
    return 6.7e6 * ELECTRON_VOLT  # J


__all__ = [
    "mass_defect",
    "binding_energy",
    "binding_energy_per_nucleon",
    "radioactive_decay",
    "decay_constant",
    "half_life",
    "activity",
    "nuclear_radius",
    "q_value",
    "fission_energy_per_nucleon",
]
