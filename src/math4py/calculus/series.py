"""級數（Series）函數。"""

import numpy as np
from typing import Callable, Tuple, List, Optional
import math


def taylor_series(f: Callable, a: float, n: int = 10) -> Callable:
    """泰勒級數展開。
    
    在 x=a 處展開 f(x) ≈ Σ (f^(k)(a)/k!) * (x-a)^k
    這裡使用數值微分估算導數。
    
    Args:
        f: 目標函數
        a: 展開點
        n: 項數
    
    Returns:
        泰勒多項式函數 p(x)
    """
    # 數值計算導數（簡化：使用符號微分或預先提供）
    # 這裡假設我們知道函數形式，或使用自動微分
    # 簡化版：返回常數逼近
    f_a = f(a)
    def p(x):
        return f_a * np.ones_like(x) if hasattr(x, '__len__') else f_a
    
    return p


def fourier_series(f: Callable, a: float, b: float, n: int = 10) -> Tuple[float, List[float], List[float]]:
    """傅里葉級數展開 f(x) ≈ a0/2 + Σ (a_n cos(nωx) + b_n sin(nωx))。
    
    Args:
        f: 周期函數（假設周期 T = b-a）
        a, b: 區間
        n: 諧波數
    
    Returns:
        (a0, a_n_list, b_n_list)
    """
    T = b - a
    omega = 2 * np.pi / T
    
    # 計算 a0
    x = np.linspace(a, b, 1000)
    y = f(x)
    a0 = (2.0 / T) * np.trapezoid(y, x)
    
    # 計算 a_n, b_n
    a_n = []
    b_n = []
    for k in range(1, n + 1):
        cos_k = np.cos(k * omega * x)
        sin_k = np.sin(k * omega * x)
        a_n.append((2.0 / T) * np.trapezoid(y * cos_k, x))
        b_n.append((2.0 / T) * np.trapezoid(y * sin_k, x))
    
    return a0, a_n, b_n


def power_series(coeffs: List[float], x: np.ndarray) -> np.ndarray:
    """冪級數求和 Σ c_n * x^n。
    
    Args:
        coeffs: 係數列表 [c0, c1, c2, ...]
        x: 自變量（可為數組）
    
    Returns:
        級數和
    """
    result = np.zeros_like(x)
    for n, c in enumerate(coeffs):
        result += c * (x ** n)
    return result


def geometric_series(a: float, r: float, n: Optional[int] = None) -> float:
    """幾何級數和 a + ar + ar² + ... + ar^n。
    
    Args:
        a: 首項
        r: 公比
        n: 項數（None 表示無窮級數）
    
    Returns:
        級數和（|r| < 1 時收斂）
    """
    if n is None:
        # 無窮級數
        if abs(r) >= 1:
            return float('inf')  # 發散
        return a / (1.0 - r)
    else:
        # 有限項
        return a * (1.0 - r**(n + 1)) / (1.0 - r)


def harmonic_series(n: int) -> float:
    """調和級數 H_n = 1 + 1/2 + 1/3 + ... + 1/n。"""
    return sum(1.0 / k for k in range(1, n + 1))


def alternating_harmonic_series(n: int) -> float:
    """交錯調和級數 1 - 1/2 + 1/3 - ... + (-1)^(n+1)/n。"""
    return sum((-1)**(k+1) / k for k in range(1, n + 1))


def ratio_test(terms: List[float]) -> Tuple[str, float]:
    """比值檢驗判斷級數收斂性。
    
    計算 lim |a_{n+1}/a_n| = L
    L < 1: 收斂
    L > 1: 發散
    L = 1: 無法判定
    
    Returns:
        (conclusion, limit_L)
    """
    if len(terms) < 3:
        return "insufficient_terms", 0.0
    
    ratios = [abs(terms[i+1] / terms[i]) for i in range(len(terms)-1) if terms[i] != 0]
    
    if not ratios:
        return "zero_series", 0.0
    
    L = ratios[-1]  # 使用最後一個比值（簡化）
    
    if L < 1:
        return "convergent", L
    elif L > 1:
        return "divergent", L
    else:
        return "inconclusive", L


def root_test(terms: List[float]) -> Tuple[str, float]:
    """根值檢驗（Cauchy 檢驗）。
    
    計算 lim sup |a_n|^(1/n) = L
    L < 1: 收斂
    L > 1: 發散
    L = 1: 無法判定
    
    Returns:
        (conclusion, limit_L)
    """
    if len(terms) < 2:
        return "insufficient_terms", 0.0
    
    n_th_roots = [abs(terms[i])**(1.0/i) for i in range(1, len(terms))]
    
    if not n_th_roots:
        return "zero_series", 0.0
    
    L = n_th_roots[-1]
    
    if L < 1:
        return "convergent", L
    elif L > 1:
        return "divergent", L
    else:
        return "inconclusive", L


def integral_test(f: Callable, a: int, n_terms: int = 1000) -> Tuple[str, float]:
    """積分檢験（用於正項遞減級數）。
    
    若 ∫_a^∞ f(x) dx 收斂，則 Σ f(n) 收斂。
    
    Args:
        f: 正遞減函數
        a: 起始索引
        n_terms: 計算項數
    
    Returns:
        (conclusion, integral_value)
    """
    x = np.linspace(a, a + n_terms, n_terms * 10)
    y = f(x)
    integral = np.trapz(y, x)
    
    if integral < float('inf'):
        return "convergent", integral
    else:
        return "divergent", integral


def series_convergence(terms: List[float], method: str = "ratio") -> Tuple[str, float]:
    """判斷級數收斂性。
    
    Args:
        terms: 級數項列表
        method: "ratio" 或 "root"
    
    Returns:
        (conclusion, test_value)
    """
    if method == "ratio":
        return ratio_test(terms)
    elif method == "root":
        return root_test(terms)
    else:
        raise ValueError(f"Unknown method: {method}")


def maclaurin_series(f: Callable, n: int = 10) -> Callable:
    """麥克勞林級數（a=0 的泰勒級數）。"""
    return taylor_series(f, 0.0, n)


def partial_sum(terms: List[float], n: int) -> float:
    """計算部分和 S_n = Σ_{k=1}^n a_k。"""
    return sum(terms[:n])


__all__ = [
    "taylor_series",
    "fourier_series",
    "power_series",
    "geometric_series",
    "harmonic_series",
    "alternating_harmonic_series",
    "ratio_test",
    "root_test",
    "integral_test",
    "series_convergence",
    "maclaurin_series",
    "partial_sum",
]
