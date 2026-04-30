"""分析學（Analysis）基礎函數。"""

import numpy as np
from typing import Callable, Tuple, List
import math


def limit(f: Callable, x0: float, direction: str = "both", 
          h: float = 1e-6) -> Tuple[float, str]:
    """計算函數極限 lim_{x→x0} f(x)。
    
    Args:
        f: 函數
        x0: 極限點
        direction: "left", "right", "both"
        h: 逼近步長
    
    Returns:
        (limit_value, status)
        status: "exists", "does_not_exist", "infinite"
    """
    try:
        if direction in ["left", "both"]:
            left_val = f(x0 - h)
            if abs(left_val) > 1e10:
                return float('inf'), "infinite"
        
        if direction in ["right", "both"]:
            right_val = f(x0 + h)
            if abs(right_val) > 1e10:
                return float('inf'), "infinite"
        
        if direction == "both":
            if abs(left_val - right_val) < 1e-4:
                return (left_val + right_val) / 2.0, "exists"
            else:
                return float('nan'), "does_not_exist"
        elif direction == "left":
            return left_val, "exists"
        else:  # right
            return right_val, "exists"
    except Exception:
        return float('nan'), "does_not_exist"


def is_continuous(f: Callable, x0: float, h: float = 1e-6, 
                  tol: float = 1e-6) -> bool:
    """檢查函數在 x0 是否連續。
    
    連續定義：lim_{x→x0} f(x) = f(x0)
    """
    try:
        f_x0 = f(x0)
        lim, status = limit(f, x0, direction="both", h=h)
        
        if status != "exists":
            return False
        
        return abs(lim - f_x0) < tol
    except Exception:
        return False


def is_uniformly_continuous(f: Callable, interval: Tuple[float, float], 
                            n_samples: int = 100, tol: float = 1e-6) -> bool:
    """檢查函數在區間上是否一致連續。
    
    簡化檢查：取足夠密的點，檢查 δ-ε 條件。
    """
    a, b = interval
    x_samples = np.linspace(a, b, n_samples)
    
    for x1 in x_samples:
        for x2 in x_samples:
            if abs(x1 - x2) < tol:
                if abs(f(x1) - f(x2)) > np.sqrt(tol):
                    return False
    return True


def pointwise_convergence(f_n: List[Callable], f: Callable, 
                         x_range: Tuple[float, float], 
                         n_samples: int = 50) -> float:
    """檢查函數序列是否點態收斂。
    
    計算 max_x |f_n(x) - f(x)| 對不同的 n。
    
    Returns:
        最大誤差（應隨 n 增大而減小）
    """
    a, b = x_range
    x = np.linspace(a, b, n_samples)
    
    max_error = 0.0
    for xi in x:
        f_target = f(xi)
        for fn in f_n:
            error = abs(fn(xi) - f_target)
            max_error = max(max_error, error)
    
    return max_error


def uniform_convergence(f_n: List[Callable], f: Callable,
                        x_range: Tuple[float, float],
                        n_samples: int = 50) -> Tuple[bool, float]:
    """檢查函數序列是否一致收斂。
    
    一致收斂：sup_x |f_n(x) - f(x)| → 0
    
    Returns:
        (is_uniform, sup_error)
    """
    a, b = x_range
    x = np.linspace(a, b, n_samples)
    
    errors = []
    for xi in x:
        f_target = f(xi)
        for fn in f_n:
            errors.append(abs(fn(xi) - f_target))
    
    sup_error = max(errors) if errors else 0.0
    
    return sup_error < 0.1, sup_error


def intermediate_value_theorem(f: Callable, a: float, b: float, 
                               tol: float = 1e-6) -> Tuple[bool, float]:
    """介值定理：若 f 連續且 f(a)f(b) < 0，則 ∃c∈(a,b) s.t. f(c)=0。
    
    也會檢查區間內是否有符號變化。
    
    Returns:
        (exists_zero, c_approximate)
    """
    f_a = f(a)
    f_b = f(b)
    
    # 如果端點已經是零
    if abs(f_a) < tol:
        return True, a
    if abs(f_b) < tol:
        return True, b
    
    # 標準介值定理：端點異號
    if f_a * f_b < 0:
        # 二分法找零點
        left, right = (a, b) if f_a < 0 else (b, a)
        
        for _ in range(50):
            mid = (left + right) / 2.0
            f_mid = f(mid)
            
            if abs(f_mid) < tol:
                return True, mid
            
            if f_mid < 0:
                left = mid
            else:
                right = mid
        
        return True, (left + right) / 2.0
    
    # 端點同號，但可能區間內有零點（如拋物線）
    # 使用更密集的採樣和二分法
    x_samples = np.linspace(a, b, 20)
    for i in range(len(x_samples) - 1):
        x1, x2 = x_samples[i], x_samples[i+1]
        f1, f2 = f(x1), f(x2)
        
        if abs(f1) < tol:
            return True, x1
        if abs(f2) < tol:
            return True, x2
        
        # 檢查子區間內是否有符號變化
        if f1 * f2 < 0:
            # 在這個子區間內用二分法
            left, right = (x1, x2) if f1 < 0 else (x2, x1)
            for _ in range(50):
                mid = (left + right) / 2.0
                f_mid = f(mid)
                if abs(f_mid) < tol:
                    return True, mid
                if f_mid < 0:
                    left = mid
                else:
                    right = mid
            return True, (left + right) / 2.0
    
    return False, float('nan')


def mean_value_theorem(f: Callable, a: float, b: float, 
                      f_prime: Callable) -> Tuple[bool, float]:
    """均值定理：∃c∈(a,b) s.t. f'(c) = (f(b)-f(a))/(b-a)。
    
    Returns:
        (theorem_holds, c_value)
    """
    if abs(b - a) < 1e-10:
        return True, a
    
    slope = (f(b) - f(a)) / (b - a)
    
    # 在區間內找 c 使得 f'(c) ≈ slope
    # 簡化：採樣檢查
    x_samples = np.linspace(a + 0.01, b - 0.01, 100)
    
    for c in x_samples:
        if abs(f_prime(c) - slope) < 0.1:
            return True, c
    
    return False, float('nan')


def extreme_value_theorem(f: Callable, interval: Tuple[float, float], 
                          n_samples: int = 1000) -> Tuple[float, float]:
    """極值定理：連續函數在閉區間上有最大值和最小值。
    
    Returns:
        (min_value, max_value)
    """
    a, b = interval
    x = np.linspace(a, b, n_samples)
    y = f(x)
    
    return np.min(y), np.max(y)


def riemann_integral(f: Callable, a: float, b: float, 
                     n: int = 1000) -> float:
    """黎曼積分（數值逼近）。
    
    使用梯形法計算 ∫_a^b f(x) dx。
    """
    x = np.linspace(a, b, n)
    y = f(x)
    return np.trapz(y, x)


def sequence_limit(a_n: List[float], method: str = "definition", 
                  eps: float = 1e-6) -> Tuple[float, bool]:
    """計算數列極限 lim_{n→∞} a_n。
    
    Args:
        a_n: 數列項
        method: "definition" 使用 ε-N 定義
        eps: ε 值
    
    Returns:
        (limit, converges)
    """
    if len(a_n) < 10:
        return float('nan'), False
    
    # 檢查最後幾項是否穩定
    last_values = a_n[-10:]
    variance = np.var(last_values)
    
    if variance < eps:
        return np.mean(last_values), True
    else:
        return float('nan'), False


def cauchy_sequence(terms: List[float], eps: float = 1e-6) -> bool:
    """檢查是否為柯西數列。
    
    ∀ε>0, ∃N s.t. |a_m - a_n| < ε for all m,n > N
    """
    if len(terms) < 10:
        return False
    
    n = len(terms)
    for i in range(n - 10, n):
        for j in range(n - 10, n):
            if abs(terms[i] - terms[j]) > eps:
                return False
    
    return True


__all__ = [
    "limit",
    "is_continuous",
    "is_uniformly_continuous",
    "pointwise_convergence",
    "uniform_convergence",
    "intermediate_value_theorem",
    "mean_value_theorem",
    "extreme_value_theorem",
    "riemann_integral",
    "sequence_limit",
    "cauchy_sequence",
]
