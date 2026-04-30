"""拉普拉斯轉換分析。"""

from typing import Callable, Tuple

import numpy as np


def laplace_transform(f: Callable, s: complex, t_max: float = 10.0, dt: float = 0.001) -> complex:
    """數值拉普拉斯轉換 L{f}(s) = ∫_0^∞ f(t) e^{-st} dt。

    Args:
        f: 時域函數 f(t)
        s: 複數頻率 s
        t_max: 積分上限
        dt: 積分步長

    Returns:
        L{f}(s)
    """
    t = np.arange(0, t_max, dt)
    f_values = np.array([f(ti) for ti in t])
    integrand = f_values * np.exp(-s * t)
    return np.trapezoid(integrand, t)


def inverse_laplace_bromwich(
    F: Callable, t: float, sigma: float = 1.0, omega_max: float = 100.0, domega: float = 0.1
) -> float:
    """數值逆拉普拉斯轉換 (Bromwich 積分)。

    f(t) = (1/2πi) ∫_{σ-i∞}^{σ+i∞} F(s) e^{st} ds

    簡化：f(t) ≈ (e^{σt}/π) ∫_0^∞ Re(F(σ+iω) e^{iωt}) dω
    """
    omegas = np.arange(0, omega_max, domega)
    F_values = np.array([F(sigma + 1j * w) for w in omegas])
    integrand = np.real(F_values * np.exp(1j * omegas * t))
    integral = np.trapezoid(integrand, omegas)
    return (np.exp(sigma * t) / np.pi) * integral


def laplace_transform_pairs() -> dict:
    """常見拉普拉斯轉換對。

    Returns:
        字典 {名稱: (f(t), L{f}(s)}
    """
    return {
        "unit_step": (lambda t: 1.0 if t >= 0 else 0.0, lambda s: 1.0 / s),
        "exponential": (lambda t: np.exp(-2.0 * t), lambda s: 1.0 / (s + 2.0)),
        "sine": (lambda t: np.sin(3.0 * t), lambda s: 3.0 / (s**2 + 9.0)),
        "cosine": (lambda t: np.cos(2.0 * t), lambda s: s / (s**2 + 4.0)),
        "t_n": (lambda t: t**2, lambda s: 2.0 / s**3),
    }


def laplace_derivative_property(f: Callable, s: complex, f0: float, t_max: float = 10.0) -> complex:
    """驗證導數性質：L{f'}(s) = sL{f}(s) - f(0)。

    Args:
        f: 函數 f(t)
        s: 複數頻率
        f0: f(0)
        t_max: 積分上限

    Returns:
        L{f'}(s) - [sL{f}(s) - f0] 應接近 0
    """

    def f_prime(t):
        h = 1e-5
        return (f(t + h) - f(t - h)) / (2 * h)

    L_f = laplace_transform(f, s, t_max)
    L_fp = laplace_transform(f_prime, s, t_max)
    return L_fp - (s * L_f - f0)


def solve_ode_laplace(a: float, b: float, y0: float) -> Callable:
    """用拉普拉斯轉換解 y' + ay = b, y(0) = y0。

    Returns:
        解 y(t) 的函數
    """

    # L{y} = (y0 + b/s) / (s + a)
    # y(t) = y0 e^{-at} + (b/a)(1 - e^{-at})
    def y(t):
        return y0 * np.exp(-a * t) + (b / a) * (1 - np.exp(-a * t))

    return y


def convolution_theorem_laplace(
    f: Callable, g: Callable, t: float, s: complex
) -> Tuple[complex, complex]:
    """驗證摺積定理：L{f * g} = L{f} · L{g}。

    Returns:
        (L{f*g}(s), L{f}(s) · L{g}(s))
    """

    def convolution(t):
        # 數值摺積 (f * g)(t) = ∫_0^t f(τ) g(t-τ) dτ
        tau = np.linspace(0, t, 1000)
        integrand = f(tau) * g(t - tau)
        return np.trapezoid(integrand, tau)

    L_f = laplace_transform(f, s)
    L_g = laplace_transform(g, s)
    L_conv = laplace_transform(
        lambda tau: (
            convolution(tau)
            if isinstance(tau, (int, float))
            else np.array([convolution(t_i) for t_i in tau])
        ),
        s,
    )

    return L_conv, L_f * L_g


def partial_fraction_decomposition(num_coeffs: list, den_coeffs: list) -> list:
    """簡單部分分式分解（二階以下）。

    Args:
        num_coeffs: 分子系數 [a_n, ..., a_0]
        den_coeffs: 分母系數 [b_m, ..., b_0]

    Returns:
        分解項列表 [(residue, pole), ...]
    """
    # 簡化實現：假設分母可分解為 (s-p1)(s-p2)
    if len(den_coeffs) == 3:  # 二階
        a, b, c = den_coeffs
        disc = b**2 - 4 * a * c
        if disc >= 0:
            p1 = (-b + np.sqrt(disc)) / (2 * a)
            p2 = (-b - np.sqrt(disc)) / (2 * a)
            # 簡化：假設分子為常數
            residue1 = num_coeffs[0] / (p1 - p2)
            residue2 = -residue1
            return [(residue1, p1), (residue2, p2)]
    return []


__all__ = [
    "laplace_transform",
    "inverse_laplace_bromwich",
    "laplace_transform_pairs",
    "laplace_derivative_property",
    "solve_ode_laplace",
    "convolution_theorem_laplace",
    "partial_fraction_decomposition",
]
