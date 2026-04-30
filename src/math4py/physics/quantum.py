"""量子力學（Quantum Mechanics）基礎函數。"""

from typing import Tuple

import numpy as np


def planck_constant():
    """普朗克常數 h = 6.62607015 × 10^-34 J·s。"""
    return 6.62607015e-34


def reduced_planck_constant():
    """約化普朗克常數 ħ = h/(2π)。"""
    return planck_constant() / (2.0 * np.pi)


def de_broglie_wavelength(p: float) -> float:
    """德布羅意波長 λ = h/p。

    Args:
        p: 動量（kg·m/s）

    Returns:
        波長（米）
    """
    return planck_constant() / p


def energy_photon(frequency: float) -> float:
    """光子能量 E = hf。

    Args:
        frequency: 頻率（Hz）

    Returns:
        能量（焦耳）
    """
    return planck_constant() * frequency


def wave_function_free_particle(x: np.ndarray, k: float, t: float = 0.0) -> np.ndarray:
    """自由粒子的波函數 ψ(x,t) = A * exp(i(kx - ωt))。

    ω = E/ħ = (ħk²)/(2m)  for non-relativistic.

    Args:
        x: 位置數組
        k: 波數
        t: 時間

    Returns:
        波函數值（複數）
    """
    hbar = reduced_planck_constant()
    # 假設質量 m=1 用於 ω
    omega = (hbar * k**2) / (2.0 * 1.0)
    return np.exp(1j * (k * x - omega * t))


def probability_density(psi: np.ndarray) -> np.ndarray:
    """概率密度 |ψ(x)|²。

    Args:
        psi: 波函數

    Returns:
        概率密度
    """
    return np.abs(psi) ** 2


def uncertainty_position(wave_func: np.ndarray, x: np.ndarray) -> float:
    """位置不確定性 Δx = sqrt(⟨x²⟩ - ⟨x⟩²)。"""
    psi = wave_func(x) if callable(wave_func) else wave_func
    prob = probability_density(psi)

    # 正規化
    norm = np.trapz(prob, x)
    prob_norm = prob / norm

    # ⟨x⟩
    x_exp = np.trapz(x * prob_norm, x)
    # ⟨x²⟩
    x2_exp = np.trapz(x**2 * prob_norm, x)

    return np.sqrt(x2_exp - x_exp**2)


def uncertainty_momentum(psi: np.ndarray, x: np.ndarray) -> float:
    """動量不確定性 Δp = sqrt(⟨p²⟩ - ⟨p⟩²)。

    動量算符 p = -iħ d/dx（數值近似）。
    """
    hbar = reduced_planck_constant()

    # 數值計算導數
    x[1] - x[0] if len(x) > 1 else 1.0

    # 動量空間波函數（簡化）
    # Δp ≈ ħ * Δk (k 是波數)
    # 簡化：假設波包寬度
    delta_x = uncertainty_position(psi, x)
    if delta_x > 0:
        return hbar / (2.0 * delta_x)  # 最小不確定性
    return 0.0


def heisenberg_uncertainty_check(delta_x: float, delta_p: float) -> Tuple[bool, float]:
    """海森堡不確定性原理 Δx·Δp ≥ ħ/2。

    Returns:
        (satisfied, product)
    """
    hbar = reduced_planck_constant()
    product = delta_x * delta_p
    return product >= hbar / 2.0, product


def schrodinger_equation_time_dependent(
    psi: np.ndarray, V: np.ndarray, x: np.ndarray, t: float, dt: float
) -> np.ndarray:
    """含時薛丁格方程 iħ ∂ψ/∂t = Hψ = (-ħ²/2m ∇² + V)ψ。

    使用簡化的數值格式（一維）。

    Args:
        psi: 當前波函數
        V: 勢能（與 x 同維度）
        x: 位置
        t: 當前時間
        dt: 時間步長

    Returns:
        更新後的波函數
    """
    hbar = reduced_planck_constant()
    m = 1.0  # 質量

    # 數值計算二階導數（拉普拉斯算符）
    dx = x[1] - x[0]
    laplacian = np.zeros_like(psi)
    laplacian[1:-1] = (psi[:-2] - 2 * psi[1:-1] + psi[2:]) / dx**2

    # 哈密頓算符作用
    H_psi = -(hbar**2 / (2.0 * m)) * laplacian + V * psi

    # 時間演化（簡化：顯式歐拉）
    psi_new = psi - (1j * dt / hbar) * H_psi

    return psi_new


def particle_in_box_wave_function(n: int, L: float, x: np.ndarray) -> np.ndarray:
    """一維無限深方阱的波函數。

    ψ_n(x) = sqrt(2/L) * sin(nπx/L), 0 < x < L

    Args:
        n: 量子數
        L: 阱寬
        x: 位置

    Returns:
        波函數
    """
    # 只考慮阱內
    psi = np.zeros_like(x, dtype=complex)
    mask = (x > 0) & (x < L)
    psi[mask] = np.sqrt(2.0 / L) * np.sin(n * np.pi * x[mask] / L)
    return psi


def energy_levels_particle_in_box(n: int, L: float, m: float = 1.0) -> float:
    """一維無限深方阱的能級。

    E_n = n²π²ħ² / (2mL²)
    """
    hbar = reduced_planck_constant()
    return (n**2 * np.pi**2 * hbar**2) / (2.0 * m * L**2)


def hydrogen_atom_wave_function(n: int, l: int, m: int, r: np.ndarray) -> np.ndarray:
    """氫原子波函數（簡化版）。

    只返回徑向部分 R_nl(r) 的簡化版本。
    基態 (n=1, l=0): R_10(r) = 2 * a0^(-3/2) * exp(-r/a0)
    """
    a0 = 5.29177210903e-11  # 波爾半徑

    if n == 1 and l == 0:
        # 基態
        return 2.0 * a0 ** (-1.5) * np.exp(-r / a0)
    else:
        # 簡化：返回高斯型
        return np.exp(-(r**2) / (2.0 * a0**2))


def tunneling_probability(V0: float, E: float, a: float) -> float:
    """量子穿隧機率（一維方勢壘）。

    對於 E < V0，穿隧機率 T ≈ exp(-2a√(2m(V0-E))/ħ)

    Args:
        V0: 勢壘高度
        E: 粒子能量
        a: 勢壘寬度

    Returns:
        穿隧機率（0到1）
    """
    if E >= V0:
        return 1.0  # 古典允許區

    hbar = reduced_planck_constant()
    m = 1.0  # 質量

    kappa = np.sqrt(2.0 * m * (V0 - E)) / hbar
    T = np.exp(-2.0 * a * kappa)

    return min(T, 1.0)


def spin_state_representation(s: str = "up") -> np.ndarray:
    """自旋態表示（泡利自旋）。

    |↑⟩ = [1, 0]^T
    |↓⟩ = [0, 1]^T
    """
    if s == "up":
        return np.array([1.0, 0.0])
    elif s == "down":
        return np.array([0.0, 1.0])
    else:
        raise ValueError(f"Unknown spin state: {s}")


def pauli_matrices() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """泡利矩陣 σ_x, σ_y, σ_z。"""
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]])
    sigma_y = np.array([[0.0, -1.0j], [1.0j, 0.0]])
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]])
    return sigma_x, sigma_y, sigma_z


__all__ = [
    "planck_constant",
    "reduced_planck_constant",
    "de_broglie_wavelength",
    "energy_photon",
    "wave_function_free_particle",
    "probability_density",
    "uncertainty_position",
    "uncertainty_momentum",
    "heisenberg_uncertainty_check",
    "schrodinger_equation_time_dependent",
    "particle_in_box_wave_function",
    "energy_levels_particle_in_box",
    "hydrogen_atom_wave_function",
    "tunneling_probability",
    "spin_state_representation",
    "pauli_matrices",
]
