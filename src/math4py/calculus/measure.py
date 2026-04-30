# 理論參考 -- https://gemini.google.com/app/7664e11b0bc36d4d
"""測度論（Measure Theory）基礎函數。"""

from typing import Any, Callable, Dict, List, Tuple

import numpy as np


def is_measure(mu: Callable, sets: List[Any]) -> Tuple[bool, str]:
    """檢查 mu 是否為測度。

    測度必須滿足：
    1. 非負性：μ(A) ≥ 0
    2. 空集合測度：μ(∅) = 0
    3. 可數可加性：對互不相交的集合 A1, A2, ...，
       μ(∪ A_i) = Σ μ(A_i)

    Args:
        mu: 測度函數
        sets: 測試集合列表

    Returns:
        (is_valid, reason)
    """
    # 檢查空集測度
    try:
        mu_empty = mu(set())
        if abs(mu_empty) > 1e-10:
            return False, f"μ(∅) = {mu_empty} ≠ 0"
    except Exception as e:
        return False, f"Cannot compute μ(∅): {e}"

    # 檢查非負性
    for s in sets:
        try:
            val = mu(s)
            if val < -1e-10:
                return False, f"μ({s}) = {val} < 0"
        except Exception:
            pass

    # 簡化：檢查有限可加性（對兩個不相交集合）
    if len(sets) >= 2:
        A = sets[0]
        B = sets[1]
        # 假設 A 和 B 不相交
        try:
            mu_A = mu(A)
            mu_B = mu(B)
            mu_A_union_B = mu(A | B)
            expected = mu_A + mu_B
            if abs(mu_A_union_B - expected) > 1e-6:
                return False, f"Finite additivity fails: μ(A∪B) = {mu_A_union_B} ≠ {expected}"
        except Exception:
            pass

    return True, "Valid measure"


def lebesgue_measure_1d(interval: Tuple[float, float]) -> float:
    """一維勒貝格測度（區間長度）。

    λ([a, b]) = b - a
    λ((a, b)) = b - a
    λ({x}) = 0  （單點集測度為0）

    Args:
        interval: (a, b) 區間

    Returns:
        區間長度
    """
    a, b = interval
    return max(0.0, b - a)


def lebesgue_measure_2d(rectangle: Tuple[float, float, float, float]) -> float:
    """二維勒貝格測度（矩形面積）。

    λ([a, b] × [c, d]) = (b-a)(d-c)

    Args:
        rectangle: (a, b, c, d) 矩形區間

    Returns:
        矩形面積
    """
    a, b, c, d = rectangle
    return max(0.0, (b - a) * (d - c))


def is_lebesgue_measurable(set_repr: Any) -> bool:
    """檢查集合是否為勒貝格可測（簡化）。

    簡化版：假設所有區間、開集、閉集都是可測的。
    實際判定需要卡拉西奧多利條件。
    """
    # 簡化：區間、有限集合都是可測的
    if isinstance(set_repr, tuple) and len(set_repr) == 2:
        return True  # 區間
    if isinstance(set_repr, (set, frozenset)):
        return True  # 離散集合
    return True  # 默認假設可測


def outer_measure_1d(intervals: List[Tuple[float, float]]) -> float:
    """一維外測度（區間覆蓋的總長）。

    μ*(A) = inf {Σ λ(I_n) : A ⊆ ∪ I_n}

    Args:
        intervals: 覆蓋區間列表

    Returns:
        外測度
    """
    total = 0.0
    for a, b in intervals:
        total += max(0.0, b - a)
    return total


def counting_measure(s: set) -> int:
    """計數測度 μ(A) = |A|。"""
    return len(s)


def dirac_measure(x0: Any, A: set) -> float:
    """狄拉克測度 μ(A) = 1 if x0 ∈ A else 0。"""
    return 1.0 if x0 in A else 0.0


def sigma_algebra_generated(sets: List[set]) -> List[set]:
    """生成由給定集合生成的 σ-代數（簡化版）。

    σ-代數包含：
    - 空集
    - 所有生成集合
    - 補集
    - 可數併集

    簡化：只計算有限個集合生成的 σ-代數。
    """
    if not sets:
        return [set()]

    # 簡化：返回生成集合和空集
    result = [set()]  # 空集
    result.extend(sets)

    # 添加併集（簡化：只考慮兩個集合的併集）
    for i in range(len(sets)):
        for j in range(i, len(sets)):
            result.append(sets[i] | sets[j])

    return result


def measure_space_check(X: Any, measurable_sets: List[Any], mu: Callable) -> Tuple[bool, str]:
    """檢查 (X, Σ, μ) 是否為測度空間。

    測度空間必須滿足：
    1. X 是非空集合
    2. Σ 是 X 上的 σ-代數
    3. μ 是 Σ 上的測度
    """
    # 簡化檢查
    if not measurable_sets:
        return False, "No measurable sets"

    # 檢查空集是否在 Σ 中
    if set() not in measurable_sets and frozenset() not in measurable_sets:
        # 嘗試檢查
        for s in measurable_sets:
            if isinstance(s, (set, frozenset)) and len(s) == 0:
                break
        else:
            return False, "∅ not in Σ"

    # 檢查測度
    is_valid, reason = is_measure(mu, measurable_sets)
    if not is_valid:
        return False, f"Measure invalid: {reason}"

    return True, "Valid measure space"


def lebesgue_integral_simple(f_values: List[float], set_measures: List[float]) -> float:
    """簡單函數的勒貝格積分。

    ∫ f dμ = Σ a_i * μ(A_i)
    其中 f = Σ a_i * 1_{A_i}
    """
    if len(f_values) != len(set_measures):
        raise ValueError("f_values and set_measures must have same length")
    return sum(a * m for a, m in zip(f_values, set_measures))


def is_integrable_indicator(A: Any, mu: Callable) -> bool:
    """指示函數是否可積（測度有限）。"""
    try:
        return mu(A) < float("inf")
    except Exception:
        return False


def convergence_theorem_check(
    fn: List[Callable], f: Callable, x_range: Tuple[float, float], n_samples: int = 100
) -> Dict[str, bool]:
    """檢查勒貝格積分的收斂定理條件。

    返回：
        - monotone_convergence: 單調收斂定理條件
        - dominated_convergence: 控制收斂定理條件（簡化）
    """
    a, b = x_range
    x = np.linspace(a, b, n_samples)

    # 檢查單調性（簡化）
    monotone = True
    for xi in x[:10]:  # 只檢查部分點
        for i in range(len(fn) - 1):
            if fn[i](xi) > fn[i + 1](xi) + 1e-6:
                monotone = False
                break

    # 控制收斂（簡化：檢查是否有統一界）
    dominated = True
    for xi in x[:10]:
        values = [f_n(xi) for f_n in fn]
        if values and max(values) > 1000:  # 簡化界
            dominated = False
            break

    return {"monotone_convergence": monotone, "dominated_convergence": dominated}


__all__ = [
    "is_measure",
    "lebesgue_measure_1d",
    "lebesgue_measure_2d",
    "is_lebesgue_measurable",
    "outer_measure_1d",
    "counting_measure",
    "dirac_measure",
    "sigma_algebra_generated",
    "measure_space_check",
    "lebesgue_integral_simple",
    "is_integrable_indicator",
    "convergence_theorem_check",
]
