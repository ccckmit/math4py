"""凝聚態物理（Condensed Matter Physics）基礎函數。"""

from typing import List, Tuple

import numpy as np

# 物理常數
ELECTRON_CHARGE = 1.602176634e-19  # C
PLANCK_CONSTANT = 6.62607015e-34  # J·s
HBAR = PLANCK_CONSTANT / (2.0 * np.pi)


def band_gap_to_wavelength(E_g: float) -> float:
    """能隙對應波長 λ = hc/E_g（E_g 單位為 J）。"""
    h = PLANCK_CONSTANT
    c = 299792458
    return h * c / E_g


def band_gap_ev_to_wavelength(E_g_eV: float) -> float:
    """能隙對應波長 λ = hc/E_g（E_g 單位為 eV）。"""
    eV_to_J = 1.602176634e-19
    return band_gap_to_wavelength(E_g_eV * eV_to_J)


def fermi_energy(n: float, m: float = 9.10938356e-31) -> float:
    """費米能 E_F = (ℏ²/2m)(3π²n)^(2/3)。"""
    return (HBAR**2 / (2.0 * m)) * (3.0 * np.pi**2 * n) ** (2.0 / 3.0)


def density_of_states_3d(E: np.ndarray, m: float = 9.10938356e-31) -> np.ndarray:
    """3D 態密度 g(E) = (1/2π²)(2m/ℏ²)^(3/2) √E。"""
    prefactor = (1.0 / (2.0 * np.pi**2)) * (2.0 * m / HBAR**2) ** 1.5
    return prefactor * np.sqrt(E)


def drude_conductivity(tau: float, n: float, m: float = 9.10938356e-31) -> float:
    """德魯德電導率 σ = n e² τ / m。"""
    return n * ELECTRON_CHARGE**2 * tau / m


def london_penetration_depth(n_s: float, m: float = 9.10938356e-31) -> float:
    """倫敦穿透深度 λ_L = sqrt(m/(μ0 n_s e²))。"""
    mu0 = 4.0e-7 * np.pi
    return np.sqrt(m / (mu0 * n_s * ELECTRON_CHARGE**2))


def cooper_pair_size(
    xi: float = None, hbar: float = None, delta: float = None, v_F: float = None
) -> float:
    """庫珀對相干長度 ξ = ℏv_F/(πΔ)。"""
    if hbar is None:
        hbar = HBAR
    if delta is None or v_F is None:
        return 100e-9  # 典型值 ~100 nm
    return hbar * v_F / (np.pi * delta)


def hall_resistance(B: float, n: float, t: float) -> float:
    """霍爾電阻 R_H = B/(n e t)。"""
    return B / (n * ELECTRON_CHARGE * t)


def bloch_theorem_wavefunction(k: np.ndarray, x: np.ndarray, u_k: np.ndarray = None) -> np.ndarray:
    """布洛赫波函數 ψ_k(x) = e^(ikx) u_k(x)。"""
    if u_k is None:
        u_k = np.ones_like(x)
    return np.exp(1j * k * x) * u_k


def crystal_structure_factor(
    h: int, k: int, l: int, basis: List[Tuple[float, float, float]]
) -> complex:
    """晶體結構因子 S = Σ_j f_j exp(-2πi(hx_j + ky_j + lz_j))。"""
    S = 0j
    for x_j, y_j, z_j in basis:
        S += np.exp(-2.0j * np.pi * (h * x_j + k * y_j + l * z_j))
    return S


def meissner_effect_penetration(B0: float, x: np.ndarray, lambda_L: float) -> np.ndarray:
    """邁斯納效應 B(x) = B0 exp(-x/λ_L)。"""
    return B0 * np.exp(-x / lambda_L)


__all__ = [
    "band_gap_to_wavelength",
    "fermi_energy",
    "density_of_states_3d",
    "drude_conductivity",
    "london_penetration_depth",
    "hall_resistance",
    "bloch_theorem_wavefunction",
    "crystal_structure_factor",
    "meissner_effect_penetration",
]
