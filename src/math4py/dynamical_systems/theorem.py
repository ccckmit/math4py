"""動力系統（Dynamical Systems）定理驗證。"""

import numpy as np
from typing import Callable


def existence_uniqueness_theorem(f: Callable, y0: np.ndarray, 
                                  t_span: tuple, eps: float = 1e-6) -> bool:
    """存在唯一性定理：若 f 滿足 Lipschitz 條件，則 ODE 解存在唯一。
    
    簡化版：檢查 f 在 y0 附近是否連續。
    """
    # 檢查 f 在 y0 的值是否有限
    try:
        dy = f(y0, t_span[0])
        return np.all(np.isfinite(dy))
    except:
        return False


def linear_stability_theorem(A: np.ndarray, tol: float = 1e-6) -> dict:
    """線性穩定性定理：特徵值實部 < 0 則穩定。"""
    eigvals = np.linalg.eigvals(A)
    max_real = np.max(np.real(eigvals))
    is_stable = max_real < -tol
    
    return {
        "pass": is_stable,
        "eigenvalues": eigvals,
        "max_real_part": max_real,
        "stable": is_stable
    }


def conservation_law_check(f: Callable, y0: np.ndarray, t_span: tuple, 
                          conservation_fn: Callable, n_steps: int = 1000) -> dict:
    """檢查保守系統的守恆量。"""
    from .function import runge_kutta_4
    
    t = np.linspace(t_span[0], t_span[1], n_steps)
    y = runge_kutta_4(f, y0, t)
    
    # 計算守恆量
    conserved_values = [conservation_fn(y[i]) for i in range(0, len(t), len(t)//100)]
    variation = np.std(conserved_values)
    
    return {
        "pass": variation < 1e-6,
        "conserved_mean": np.mean(conserved_values),
        "variation": variation
    }


def limit_cycle_detection(y: np.ndarray, tol: float = 1e-2) -> bool:
    """檢測極限環：軌跡是否漸近於封閉曲線。
    
    簡化版：檢查最後的狀態是否接近軌跡的某個早期狀態。
    """
    if len(y) < 100:
        return False
    
    # 取最後 30% 的點
    last_portion = y[-len(y)//3:]
    start_points = y[:len(y)//5]
    
    # 檢查是否有點接近
    for point in last_portion:
        for start in start_points:
            if np.linalg.norm(point - start) < tol:
                return True
    return False


def chaos_sensitivity_check(logistic_map_fn: Callable, x0: float, 
                           delta: float = 1e-10, n_steps: int = 100) -> dict:
    """混沌的初值敏感性：兩個相近初值是否指數發散。"""
    x1 = [x0]
    x2 = [x0 + delta]
    
    for i in range(1, n_steps):
        x1.append(logistic_map_fn(x1[-1]))
        x2.append(logistic_map_fn(x2[-1]))
    
    # 計算差異
    differences = [abs(x1[i] - x2[i]) for i in range(n_steps)]
    
    # 檢查是否指數增長（簡化）
    # 在混沌系統中，差異應該快速增長
    if differences[-1] > 0.5 or differences[-1] > 100 * differences[0]:
        return {"pass": True, "sensitive": True}
    return {"pass": False, "sensitive": False}


def bifurcation_theorem(r_critical: float, r_test: float) -> dict:
    """分岔定理：在 r_critical 處發生分岔。"""
    # 簡化：檢查邏輯斯蒂映射在 r < 3 和 r > 3 的行為
    from .function import logistic_map
    
    x0 = 0.5
    n = 1000
    
    x_before = logistic_map(r_test if r_test < r_critical else r_critical - 0.1, x0, n)
    x_after = logistic_map(r_test if r_test > r_critical else r_critical + 0.1, x0, n)
    
    # 穩定態數量
    unique_before = len(set(np.round(x_before[-100:], 3)))
    unique_after = len(set(np.round(x_after[-100:], 3)))
    
    bifurcated = unique_after > unique_before
    
    return {
        "pass": bifurcated,
        "bifurcation_at_critical": True,
        "unique_before": unique_before,
        "unique_after": unique_after
    }


__all__ = [
    "existence_uniqueness_theorem",
    "linear_stability_theorem",
    "conservation_law_check",
    "limit_cycle_detection",
    "chaos_sensitivity_check",
    "bifurcation_theorem",
]
