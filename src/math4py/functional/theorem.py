"""泛函分析定理驗證。"""

import numpy as np
from typing import Callable
from math4py.functional.function import (
    norm_Lp,
    norm_L2,
    inner_product_L2,
    gram_schmidt_L2,
    is_orthogonal_L2,
    spectral_radius,
    resolvent_set,
    function_space_basis,
    weak_convergence_test,
    compact_operator_test,
)


def cauchy_schwarz_inequality(f, g, a, b):
    """柯西-施瓦茲不等式 |⟨f,g⟩| ≤ ||f||₂ ||g||₂。

    Returns:
        不等式殘差（應 ≥ 0）
    """
    inner = inner_product_L2(f, g, a, b)
    norm_f = norm_L2(f, a, b)
    norm_g = norm_L2(g, a, b)
    return norm_f * norm_g - abs(inner)


def triangle_inequality_L2(f, g, a, b):
    """三角不等式 ||f+g||₂ ≤ ||f||₂ + ||g||₂。

    Returns:
        不等式殘差（應 ≥ 0）
    """
    def f_plus_g(x):
        return f(x) + g(x)
    norm_sum = norm_L2(f_plus_g, a, b)
    return norm_sum - (norm_L2(f, a, b) + norm_L2(g, a, b))


def bessel_inequality(f, basis, a, b):
    """貝塞爾不等式 Σ|⟨f,e_i⟩|² ≤ ||f||₂²。

    Returns:
        殘差（應 ≥ 0）
    """
    norm_f_sq = norm_L2(f, a, b) ** 2
    sum_squares = 0.0
    for e in basis:
        inner = inner_product_L2(f, e, a, b)
        sum_squares += inner ** 2
    return norm_f_sq - sum_squares


def parseval_identity(f, orthonormal_basis, a, b):
    """帕塞瓦爾恆等式 Σ|⟨f,e_i⟩|² = ||f||₂²（完備正交基）。

    Returns:
        誤差（應接近 0）
    """
    norm_f_sq = norm_L2(f, a, b) ** 2
    sum_squares = 0.0
    for e in orthonormal_basis:
        inner = inner_product_L2(f, e, a, b)
        sum_squares += inner ** 2
    return abs(sum_squares - norm_f_sq)


def riesz_representation_test(phi, a, b):
    """黎茨表示定理：∀φ∈(L²)*, ∃g∈L² s.t. φ(f)=⟨f,g⟩。

    簡化測試：線性泛函 φ(f)=∫ f(x)dx 應由 g=1 表示。

    Returns:
        表示誤差
    """
    def g_representative(x):
        return np.ones_like(x)

    x = np.linspace(a, b, 100)
    f_test = lambda x: x
    phi_f = phi(f_test) if callable(phi(f_test)) else phi(f_test)
    inner = inner_product_L2(f_test, g_representative, a, b)
    return abs(phi_f - inner)


def spectral_radius_theorem(A):
    """譜半徑定理 ρ(A) = lim ||A^n||^(1/n)。

    對於有限維，ρ(A) = max|λ_i|。

    Returns:
        定理驗證誤差
    """
    rho = spectral_radius(A)
    # 簡化：檢查 ρ(A) ≤ ||A||₂
    norm_A = np.linalg.norm(A, 2)
    return norm_A - rho


def resolvent_analytic(A, z1, z2):
    """預解集是開集，預解式在預解集中解析。

    簡化：檢查 R(z1) - R(z2) = (z2-z1)R(z1)R(z2)。

    Returns:
        殘差
    """
    R1 = resolvent_set(A, z1)
    R2 = resolvent_set(A, z2)
    diff = R1 - R2
    expected = (z2 - z1) * R1 @ R2
    return np.max(np.abs(diff - expected))


def weak_convergence_characterization(f_n, f, a, b):
    """弱收敛等价于逐点有界且对某个稠密子集收敛。

    Returns:
        是否弱收敛
    """
    error = weak_convergence_test(f_n, f, a, b)
    return bool(error < 0.1)


def compact_operator_spectrum(A, tol=1e-6):
    """緊緻算子的譜由特征值組成（0 除外），且特征值趨於 0。

    Returns:
        是否滿足緊緻算子譜性質
    """
    eigvals = np.linalg.eigvals(A)
    # 檢查非零特征值的模是否遞減
    non_zero = eigvals[np.abs(eigvals) > tol]
    if len(non_zero) <= 1:
        return True
    moduli = np.sort(np.abs(non_zero))[::-1]
    return np.all(np.diff(moduli) >= 0)  # 應該遞減


__all__ = [
    "cauchy_schwarz_inequality",
    "triangle_inequality_L2",
    "bessel_inequality",
    "parseval_identity",
    "riesz_representation_test",
    "spectral_radius_theorem",
    "resolvent_analytic",
    "weak_convergence_characterization",
    "compact_operator_spectrum",
]
