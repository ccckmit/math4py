"""統計力學（Statistical Mechanics）基礎函數。"""

import numpy as np

from .thermodynamics import BOLTZMANN_CONSTANT


def boltzmann_distribution(E, T: float):
    """玻爾茲曼分布 P(E) ∝ exp(-E/kT)。"""
    kT = BOLTZMANN_CONSTANT * T
    E = np.asarray(E)
    return np.exp(-E / kT)


def partition_function(energies, T: float) -> float:
    """配分函數 Z = Σ exp(-E_i/kT)。"""
    kT = BOLTZMANN_CONSTANT * T
    energies = np.asarray(energies)
    return np.sum(np.exp(-energies / kT))


def average_energy(energies: np.ndarray, T: float) -> float:
    """平均能量 ⟨E⟩ = Σ E_i * P(E_i)。"""
    kT = BOLTZMANN_CONSTANT * T
    weights = np.exp(-energies / kT)
    Z = np.sum(weights)
    return np.sum(energies * weights) / Z


def entropy_statistical(energies: np.ndarray, T: float) -> float:
    """統計熵 S = k * ln(W) 或 S = -k Σ p_i ln(p_i)。"""
    kT = BOLTZMANN_CONSTANT * T
    probs = np.exp(-energies / kT)
    probs = probs / np.sum(probs)
    # 移除零概率
    probs = probs[probs > 0]
    return -BOLTZMANN_CONSTANT * np.sum(probs * np.log(probs))


def fermi_dirac_distribution(E: np.ndarray, E_F: float, T: float) -> np.ndarray:
    """費米-狄拉克分布 f(E) = 1/(exp((E-E_F)/kT) + 1)。"""
    kT = BOLTZMANN_CONSTANT * T
    return 1.0 / (np.exp((E - E_F) / kT) + 1.0)


def bose_einstein_distribution(E: np.ndarray, mu: float, T: float) -> np.ndarray:
    """玻色-愛因斯坦分布 n(E) = 1/(exp((E-μ)/kT) - 1)。"""
    kT = BOLTZMANN_CONSTANT * T
    return 1.0 / (np.exp((E - mu) / kT) - 1.0)


def maxwell_boltzmann_speed(v: np.ndarray, m: float, T: float) -> np.ndarray:
    """麥克斯韋-玻爾茲曼速率分布 f(v) = 4π (m/(2πkT))^(3/2) v² exp(-mv²/2kT)。"""
    kT = BOLTZMANN_CONSTANT * T
    prefactor = 4.0 * np.pi * (m / (2.0 * np.pi * kT)) ** 1.5
    return prefactor * v**2 * np.exp(-m * v**2 / (2.0 * kT))


def canonical_ensemble_energy_fluctuation(energies: np.ndarray, T: float) -> float:
    """正則繫的能量漲落 ⟨(ΔE)²⟩ = kT² C_V。"""
    BOLTZMANN_CONSTANT * T
    avg_E = average_energy(energies, T)
    avg_E2 = average_energy(energies**2, T)
    return avg_E2 - avg_E**2


def chemical_potential_ideal_gas(n: float, T: float, m: float) -> float:
    """理想氣體的化學勢 μ = kT ln(nλ³)，其中 λ 是熱波長。"""
    kT = BOLTZMANN_CONSTANT * T
    # 熱德布羅意波長
    lambda_th = np.sqrt(2.0 * np.pi * BOLTZMANN_CONSTANT * T / m)
    return kT * np.log(n * lambda_th**3)


__all__ = [
    "boltzmann_distribution",
    "partition_function",
    "average_energy",
    "entropy_statistical",
    "fermi_dirac_distribution",
    "bose_einstein_distribution",
    "maxwell_boltzmann_speed",
    "chemical_potential_ideal_gas",
]
