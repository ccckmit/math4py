"""爬山演算法（Hill Climbing）實現。"""

from typing import Callable, Optional, Tuple

import numpy as np


def hill_climbing(
    f: Callable,
    x0: np.ndarray,
    step_size: float = 0.1,
    max_iter: int = 1000,
    tol: float = 1e-6,
    maximize: bool = True,
    neighbor_std: float = 0.1,
    restarts: int = 0,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, float, int]:
    """爬山演算法求局部極值。

    爬山演算法是一種局部搜索方法，每次迭代在當前點附近尋找更好的解。

    Args:
        f: 目標函數 f(x)
        x0: 初始點
        step_size: 初始步長（用於確定性搜索）
        max_iter: 最大迭代次數
        tol: 收斂容忍度
        maximize: True 表示求最大值，False 表示求最小值
        neighbor_std: 隨機鄰域的標準差
        restarts: 隨機重啟次數（0 表示不重啟）
        seed: 隨機種子

    Returns:
        (x_opt, f_opt, n_iter)
    """
    if seed is not None:
        np.random.seed(seed)

    x_best = np.array(x0, dtype=float)
    f_best = f(x_best)

    # 記錄所有重啟中的最佳解
    overall_best_x = x_best.copy()
    overall_best_f = f_best

    for restart in range(restarts + 1):
        if restart > 0:
            # 隨機重啟
            x_current = x_best + np.random.randn(len(x0)) * neighbor_std * 5
        else:
            x_current = x_best.copy()

        f_current = f(x_current)
        x_prev = x_current.copy()

        for i in range(max_iter):
            improved = False

            # 生成鄰域候選點（確定性方向 + 隨機擾動）
            candidates = []

            # 確定性方向：沿每個維度正負方向探索
            for dim in range(len(x_current)):
                for direction in [-1, 1]:
                    candidate = x_current.copy()
                    candidate[dim] += direction * step_size
                    candidates.append(candidate)

            # 隨機擾動
            for _ in range(len(x_current) * 2):
                candidate = x_current + np.random.randn(len(x_current)) * neighbor_std
                candidates.append(candidate)

            # 評估所有候選點
            for candidate in candidates:
                f_candidate = f(candidate)

                is_better = (f_candidate > f_current) if maximize else (f_candidate < f_current)

                if is_better:
                    x_current = candidate
                    f_current = f_candidate
                    improved = True
                    break # 找到改進就移動

            if not improved:
                # 無法改進，停止
                break

            # 檢查收斂
            if i > 0 and np.linalg.norm(x_current - x_prev) < tol:
                break
            x_prev = x_current.copy()

        # 更新最佳解
        if maximize and f_current > overall_best_f:
            overall_best_x = x_current.copy()
            overall_best_f = f_current
        elif not maximize and f_current < overall_best_f:
            overall_best_x = x_current.copy()
            overall_best_f = f_current

        x_best = overall_best_x
        f_best = overall_best_f

    return x_best, f_best, max_iter


def hill_climbing_simple(
    f: Callable,
    x0: np.ndarray,
    step_size: float = 0.1,
    max_iter: int = 1000,
    tol: float = 1e-6,
    maximize: bool = True,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, float, int]:
    """簡化版爬山演算法（只使用確定性鄰域搜索）。

    Args:
        f: 目標函數
        x0: 初始點
        step_size: 步長
        max_iter: 最大迭代次數
        tol: 收斂容忍度
        maximize: True 求最大值，False 求最小值
        seed: 隨機種子（此版本未使用）

    Returns:
        (x_opt, f_opt, n_iter)
    """
    x = np.array(x0, dtype=float)
    f_current = f(x)
    x_prev = x.copy()

    for i in range(max_iter):
        improved = False

        # 沿每個維度的正負方向探索
        for dim in range(len(x)):
            for direction in [-1, 1]:
                candidate = x.copy()
                candidate[dim] += direction * step_size
                f_candidate = f(candidate)

                is_better = (f_candidate > f_current) if maximize else (f_candidate < f_current)

                if is_better:
                    x = candidate
                    f_current = f_candidate
                    improved = True
                    break
            if improved:
                break

        if not improved:
            break  # 局部最優，停止

        # 檢查收斂（需要上一輪的位置）
        if i > 0 and np.linalg.norm(x - x_prev) < tol:
            break
        x_prev = x.copy()

    return x, f_current, i + 1


def random_restart_hill_climbing(
    f: Callable,
    bounds: list,
    n_restarts: int = 10,
    step_size: float = 0.1,
    max_iter: int = 1000,
    maximize: bool = True,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, float]:
    """隨機重啟爬山演算法。

    多次從隨機初始點開始爬山，返回最佳解。

    Args:
        f: 目標函數
        bounds: 變量邊界列表 [(min1, max1), (min2, max2), ...]
        n_restarts: 重啟次數
        step_size: 步長
        max_iter: 每次最大迭代次數
        maximize: True 求最大值
        seed: 隨機種子

    Returns:
        (x_best, f_best)
    """
    if seed is not None:
        np.random.seed(seed)

    len(bounds)
    best_x = None
    best_f = float("-inf") if maximize else float("inf")

    for _ in range(n_restarts):
        # 隨機初始點
        x0 = np.array([np.random.uniform(b[0], b[1]) for b in bounds])

        # 執行爬山
        x_opt, f_opt, _ = hill_climbing_simple(f, x0, step_size, max_iter, maximize=maximize)

        # 更新最佳解
        is_better = (f_opt > best_f) if maximize else (f_opt < best_f)
        if is_better:
            best_x = x_opt
            best_f = f_opt

    return best_x, best_f


def simulated_annealing(
    f: Callable,
    x0: np.ndarray,
    bounds: list,
    temperature: float = 1.0,
    cooling_rate: float = 0.95,
    max_iter: int = 1000,
    maximize: bool = True,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, float, int]:
    """模擬退火演算法（結合爬山與隨機接受）。

    允許以一定概率接受較差的解，避免陷入局部最優。

    Args:
        f: 目標函數
        x0: 初始點
        bounds: 變量邊界
        temperature: 初始溫度
        cooling_rate: 冷卻率
        max_iter: 最大迭代次數
        maximize: True 求最大值
        seed: 隨機種子

    Returns:
        (x_opt, f_opt, n_iter)
    """
    if seed is not None:
        np.random.seed(seed)

    x_current = np.array(x0, dtype=float)
    f_current = f(x_current)

    x_best = x_current.copy()
    f_best = f_current

    T = temperature

    for i in range(max_iter):
        # 生成新候選點（在邊界內隨機擾動）
        x_new = x_current + np.random.randn(len(x0)) * T

        # 確保在邊界內
        for dim in range(len(x0)):
            x_new[dim] = np.clip(x_new[dim], bounds[dim][0], bounds[dim][1])

        f_new = f(x_new)

        # 計算接受概率
        if maximize:
            delta = f_new - f_current
            accept = delta > 0 or np.random.random() < np.exp(delta / T)
        else:
            delta = f_current - f_new
            accept = delta > 0 or np.random.random() < np.exp(delta / T)

        if accept:
            x_current = x_new
            f_current = f_new

            if maximize and f_current > f_best:
                x_best = x_current.copy()
                f_best = f_current
            elif not maximize and f_current < f_best:
                x_best = x_current.copy()
                f_best = f_current

        # 降溫
        T *= cooling_rate

        if T < 1e-10:
            break

    return x_best, f_best, i + 1


__all__ = [
    "hill_climbing",
    "hill_climbing_simple",
    "random_restart_hill_climbing",
    "simulated_annealing",
]
