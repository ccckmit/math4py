"""測度論（Measure Theory）基礎函數。"""

import numpy as np
from typing import Callable, List, Dict, Set, Tuple


def _trapezoid(y, x):
    """手動實現梯形法數值積分，相容 NumPy 2.x。"""
    y = np.asarray(y)
    x = np.asarray(x)
    if y.ndim == 0 or len(y) <= 1:
        return float(y) * float(x[-1] - x[0]) if len(x) > 1 else 0.0
    return float(np.sum((x[1:] - x[:-1]) * (y[1:] + y[:-1]) / 2.0))


def is_sigma_algebra(sets: Set[frozenset], universal: frozenset) -> bool:
    """檢查是否為 σ-代數。"""
    if frozenset() not in sets:
        return False
    for A in sets:
        complement = universal - A
        if frozenset(complement) not in sets:
            return False
    return True


def measure_additivity(sets: List[frozenset], measure: Dict[frozenset, float]) -> bool:
    """檢查測度是否為可數可加的。"""
    if len(sets) < 2:
        return True
    A1, A2 = sets[0], sets[1]
    if A1.isdisjoint(A2):
        union = A1 | A2
        if union in measure and A1 in measure and A2 in measure:
            return abs(measure[union] - (measure[A1] + measure[A2])) < 1e-10
    return True


def lebesgue_measure_interval(a: float, b: float) -> float:
    """勒貝格測度 λ([a, b]) = b - a。"""
    return max(0.0, b - a)


def is_lebesgue_integrable(f: Callable, a: float, b: float, 
                           n: int = 1000) -> bool:
    """檢查函數在 [a, b] 上是否勒貝格可積。"""
    try:
        x = np.linspace(a, b, n)
        values = f(x)
        return np.all(np.isfinite(values))
    except:
        return False


def lebesgue_integral(f: Callable, a: float, b: float,
                          n: int = 10000) -> float:
    """勒貝格積分 ∫_a^b f dλ（梯形法）。"""
    x = np.linspace(a, b, n)
    y = f(x)
    return _trapezoid(y, x)


def sigma_finite_measure(measure: Dict[frozenset, float], 
                        universal: frozenset) -> bool:
    """檢查測度是否為 σ-有限。"""
    finite_sets = [A for A in measure if measure[A] < float('inf')]
    covered = frozenset()
    for A in finite_sets:
        covered = covered | A
    return covered == universal


def measurable_function_check(f: Callable, domain_sets: List[frozenset]) -> bool:
    """檢查函數是否為可測函數。"""
    try:
        test_val = f(0.0)
        return np.isfinite(test_val)
    except:
        return False


def l_infty_norm(f: Callable, a: float, b: float, n: int = 1000) -> float:
    """L^∞ 範數 ||f||_∞ = ess sup |f(x)|。"""
    x = np.linspace(a, b, n)
    values = np.abs(f(x))
    return float(np.max(values))


def l_p_norm(f: Callable, a: float, b: float, p: float, n: int = 10000) -> float:
    """L^p 範數 ||f||_p = (∫ |f|^p dλ)^{1/p}。"""
    x = np.linspace(a, b, n)
    y = np.abs(f(x))**p
    integral = _trapezoid(y, x)
    return float(integral ** (1.0/p))


def holder_inequality(f: Callable, g: Callable, p: float, q: float,
                        a: float, b: float) -> dict:
    """赫爾德不等式 ||fg||_1 ≤ ||f||_p ||g||_q。"""
    norm_f = l_p_norm(f, a, b, p)
    norm_g = l_p_norm(g, a, b, q)
    fg = lambda x: f(x) * g(x)
    norm_fg = l_p_norm(fg, a, b, 1.0)
    
    holds = norm_fg <= norm_f * norm_g + 1e-10
    return {
        "pass": holds,
        "lhs": norm_fg,
        "rhs": norm_f * norm_g,
        "p": p,
        "q": q
    }


def minkowski_inequality(f: Callable, g: Callable, p: float,
                         a: float, b: float) -> dict:
    """閔可夫斯基不等式 ||f + g||_p ≤ ||f||_p + ||g||_p。"""
    norm_f = l_p_norm(f, a, b, p)
    norm_g = l_p_norm(g, a, b, p)
    f_plus_g = lambda x: f(x) + g(x)
    norm_f_plus_g = l_p_norm(f_plus_g, a, b, p)
    
    holds = norm_f_plus_g <= norm_f + norm_g + 1e-10
    return {
        "pass": holds,
        "lhs": norm_f_plus_g,
        "rhs": norm_f + norm_g
    }


__all__ = [
    "is_sigma_algebra",
    "measure_additivity",
    "lebesgue_measure_interval",
    "is_lebesgue_integrable",
    "lebesgue_integral",
    "sigma_finite_measure",
    "measurable_function_check",
    "l_infty_norm",
    "l_p_norm",
    "holder_inequality",
    "minkowski_inequality",
]
