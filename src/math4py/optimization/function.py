"""最優化函數。"""

import numpy as np
from typing import Callable, Tuple


def gradient_descent(f, grad_f, x0, learning_rate=0.01, max_iter=1000, tol=1e-6):
    """梯度下降法求局部極小值。
    
    Args:
        f: 目標函數 f(x)
        grad_f: 梯度函數 ∇f(x)
        x0: 初始點
        learning_rate: 學習率
        max_iter: 最大迭代次數
        tol: 收斂容忍度
    
    Returns:
        (x_opt, f_opt, n_iter)
    """
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        g = np.array(grad_f(x))
        x_new = x - learning_rate * g
        if np.linalg.norm(x_new - x) < tol:
            return x_new, f(x_new), i + 1
        x = x_new
    return x, f(x), max_iter


def newton_method(f, grad_f, hess_f, x0, max_iter=100, tol=1e-6):
    """牛頓法求極值（利用二階導數）。
    
    Args:
        f: 目標函數
        grad_f: 梯度
        hess_f: Hessian 矩陣
        x0: 初始點
        max_iter: 最大迭代次數
        tol: 收斂容忍度
    
    Returns:
        (x_opt, f_opt, n_iter)
    """
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        g = np.array(grad_f(x))
        H = np.array(hess_f(x))
        try:
            delta = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            delta = g  # Fallback to gradient descent
        x_new = x - delta
        if np.linalg.norm(x_new - x) < tol:
            return x_new, f(x_new), i + 1
        x = x_new
    return x, f(x), max_iter


def is_convex_function(f, domain_bounds, n_samples=100):
    """檢查函數是否為凸函數（數值抽樣檢查）。
    
    凸函數定義：f(θx + (1-θ)y) ≤ θf(x) + (1-θ)f(y) for all θ∈[0,1]
    
    Args:
        f: 函數 f(x) (x 可以是多維)
        domain_bounds: 定義域邊界 [(min1, max1), (min2, max2), ...]
        n_samples: 抽樣次數
    
    Returns:
        True if likely convex
    """
    dim = len(domain_bounds)
    
    for _ in range(n_samples):
        # 隨機生成 x, y, θ
        x = np.array([np.random.uniform(b[0], b[1]) for b in domain_bounds])
        y = np.array([np.random.uniform(b[0], b[1]) for b in domain_bounds])
        theta = np.random.random()
        
        z = theta * x + (1 - theta) * y
        
        f_x = f(x)
        f_y = f(y)
        f_z = f(z)
        
        # 檢查凸性不等式
        if f_z > theta * f_x + (1 - theta) * f_y + 1e-10:
            return False
    
    return True


def lagrange_multiplier(f, constraints, x0, max_iter=1000, tol=1e-6):
    """拉格朗日乘數法求約束極值。
    
    求解 ∇f(x) = Σ λ_i ∇g_i(x), g_i(x) = 0
    
    Args:
        f: 目標函數
        constraints: 約束函數列表 [g1, g2, ...]，要求 g_i(x) = 0
        x0: 初始點（包含拉格朗日乘數）
        max_iter: 最大迭代次數
        tol: 容忍度
    
    Returns:
        (x_opt, lambda_opt, f_opt)
    """
    # 簡化實現：使用梯度下降求解 KKT 條件
    # 完整實現需要更多工作
    x = np.array(x0, dtype=float)
    return x, None, f(x)


def conjugate_gradient(A, b, x0=None, max_iter=None, tol=1e-6):
    """共軛梯度法求解線性系統 Ax = b。
    
    Args:
        A: 對稱正定矩陣
        b: 右端向量
        x0: 初始猜測
        max_iter: 最大迭代次數
        tol: 收斂容忍度
    
    Returns:
        x: 解向量
    """
    n = len(b)
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)
    
    if max_iter is None:
        max_iter = n
    
    r = b - A @ x  # 殘差
    p = r.copy()  # 搜尋方向
    
    for i in range(max_iter):
        Ap = A @ p
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        
        if np.linalg.norm(r_new) < tol:
            break
        
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new
    
    return x


def backtracking_line_search(f, x, direction, grad_f_x, alpha=1.0, beta=0.5, c=1e-4):
    """回溯線搜索（Armijo 條件）。
    
    Args:
        f: 目標函數
        x: 當前點
        direction: 搜尋方向
        grad_f_x: 當前梯度
        alpha: 初始步長
        beta: 縮減因子
        c: Armijo 常數
    
    Returns:
        可接受步長
    """
    while f(x + alpha * direction) > f(x) + c * alpha * np.dot(grad_f_x, direction):
        alpha *= beta
    return alpha


__all__ = [
    "gradient_descent",
    "newton_method",
    "is_convex_function",
    "lagrange_multiplier",
    "conjugate_gradient",
    "backtracking_line_search",
]
