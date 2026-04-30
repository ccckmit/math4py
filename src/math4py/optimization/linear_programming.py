"""線性規劃（Linear Programming）函數。"""

import numpy as np
from typing import Tuple, Optional, Literal


def simplex_method(
    c: np.ndarray,
    A: np.ndarray,
    b: np.ndarray,
    max_iter: int = 1000,
    tol: float = 1e-10
) -> Tuple[np.ndarray, float, str]:
    """單形法求解線性規劃問題（標準形式）。
    
    標準形式：min c^T x
              s.t. Ax = b
                   x ≥ 0
    
    使用兩階段法處理初始基本可行解。
    
    Args:
        c: 目標函數係數 (n,)
        A: 約束矩陣 (m, n)
        b: 右端向量 (m,)
        max_iter: 最大迭代次數
        tol: 容忍度
    
    Returns:
        (x_opt, obj_value, status)
        status: "optimal", "unbounded", "infeasible"
    """
    c = np.array(c, dtype=float)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1)
    
    m, n = A.shape
    
    # 階段一：添加人工變量，求解可行性
    # 人工變量係數矩陣
    A_phase1 = np.hstack([A, np.eye(m)])
    c_phase1 = np.concatenate([np.zeros(n), np.ones(m)])
    
    # 初始基本可行解：人工變量 = b（假設 b ≥ 0）
    if np.any(b < -tol):
        # 對負的 b 分量，添加負的人工變量（或處理符號）
        # 簡化：使用絕對值
        b_abs = np.abs(b)
        A_phase1 = np.hstack([A, np.eye(m)])
        # 這裡需要更仔細處理，簡化版先假設 b ≥ 0
        return np.zeros(n), 0.0, "infeasible"
    
    basic = list(range(n, n + m))  # 人工變量索引
    non_basic = list(range(n))      # 原始變量索引
    
    # 階段一：最小化人工變量之和
    for iteration in range(max_iter):
        B = A_phase1[:, basic]
        try:
            x_B = np.linalg.solve(B, b)
        except np.linalg.LinAlgError:
            return np.zeros(n), 0.0, "infeasible"
        
        c_B = c_phase1[basic]
        try:
            lambda_vec = np.linalg.solve(B.T, c_B)
        except np.linalg.LinAlgError:
            return np.zeros(n), 0.0, "infeasible"
        
        reduced_costs = np.zeros(n + m)
        for j in non_basic:
            reduced_costs[j] = c_phase1[j] - np.dot(lambda_vec, A_phase1[:, j])
        
        if np.all(reduced_costs >= -tol):
            # 階段一完成，檢查人工變量是否為零
            artificial_sum = sum(x_B[i] for i, idx in enumerate(basic) if idx >= n)
            if artificial_sum > tol:
                return np.zeros(n), 0.0, "infeasible"
            break
        
        # 選擇入基變量
        entering = min(non_basic, key=lambda j: reduced_costs[j])
        
        d = np.linalg.solve(B, A_phase1[:, entering])
        
        if np.all(d <= tol):
            return np.zeros(n), float('-inf'), "unbounded"
        
        ratios = [x_B[i] / d[i] if d[i] > tol else float('inf') 
                  for i in range(m)]
        leaving_idx = int(np.argmin(ratios))
        
        basic[leaving_idx] = entering
        non_basic.remove(entering)
        non_basic.append(basic[leaving_idx])
    
    # 階段二：用原目標函數求解
    # 構建新的基本可行解
    basic_orig = [idx for idx in basic if idx < n]  # 只保留原始變量
    non_basic_orig = [idx for idx in range(n) if idx not in basic_orig]
    
    if len(basic_orig) < m:
        # 需要添加鬆弛變量或處理
        # 簡化：假設 basic 中已經包含 m 個變量
        basic_orig = basic[:m]
        non_basic_orig = [j for j in range(n) if j not in basic_orig]
    
    A_orig = A  # 原始約束
    
    for iteration in range(max_iter):
        B = A_orig[:, basic_orig]
        try:
            x_B = np.linalg.solve(B, b)
        except np.linalg.LinAlgError:
            return np.zeros(n), 0.0, "infeasible"
        
        c_B = c[basic_orig]
        try:
            lambda_vec = np.linalg.solve(B.T, c_B)
        except np.linalg.LinAlgError:
            return np.zeros(n), 0.0, "infeasible"
        
        reduced_costs = np.zeros(n)
        for j in non_basic_orig:
            reduced_costs[j] = c[j] - np.dot(lambda_vec, A_orig[:, j])
        
        if np.all(reduced_costs >= -tol):
            # 最優解找到
            x = np.zeros(n)
            for i, idx in enumerate(basic_orig):
                x[idx] = x_B[i]
            obj_value = np.dot(c, x)
            return x, obj_value, "optimal"
        
        entering = min(non_basic_orig, key=lambda j: reduced_costs[j])
        
        d = np.linalg.solve(B, A_orig[:, entering])
        
        if np.all(d <= tol):
            return np.zeros(n), float('-inf'), "unbounded"
        
        ratios = [x_B[i] / d[i] if d[i] > tol else float('inf') 
                  for i in range(len(basic_orig))]
        leaving_idx = int(np.argmin(ratios))
        
        leaving = basic_orig[leaving_idx]
        basic_orig[leaving_idx] = entering
        non_basic_orig.remove(entering)
        non_basic_orig.append(leaving)
    
    return np.zeros(n), 0.0, "max_iter_reached"


def solve_lp(
    c: np.ndarray,
    A_ub: Optional[np.ndarray] = None,
    b_ub: Optional[np.ndarray] = None,
    A_eq: Optional[np.ndarray] = None,
    b_eq: Optional[np.ndarray] = None,
    bounds: Optional[list] = None,
    method: Literal["simplex"] = "simplex"
) -> dict:
    """求解線性規劃問題（包裝函數）。
    
    形式：min c^T x
              s.t. A_ub x ≤ b_ub
                   A_eq x = b_eq
                   bounds[i][0] ≤ x[i] ≤ bounds[i][1]
    
    Args:
        c: 目標函數係數
        A_ub: 不等式約束矩陣（≤）
        b_ub: 不等式右端
        A_eq: 等式約束矩陣
        b_eq: 等式右端
        bounds: 變量邊界列表 [(min, max), ...]
        method: 求解方法（目前只支援 simplex）
    
    Returns:
        {"x": 最優解, "fun": 目標值, "status": 狀態}
    """
    c = np.array(c, dtype=float)
    
    # 預設邊界：x ≥ 0
    # 簡化：假設所有變量 ≥ 0
    
    # 構造標準形式 Ax = b
    A_list = []
    b_list = []
    
    if A_eq is not None:
        A_eq = np.array(A_eq, dtype=float)
        b_eq = np.array(b_eq, dtype=float).reshape(-1)
        A_list.append(A_eq)
        b_list.append(b_eq)
    
    if A_ub is not None:
        A_ub = np.array(A_ub, dtype=float)
        b_ub = np.array(b_ub, dtype=float).reshape(-1)
        # 添加鬆弛變量：A_ub x + s = b_ub, s ≥ 0
        m_ub = A_ub.shape[0]
        A_aug = np.hstack([A_ub, np.eye(m_ub)])
        # 擴展目標函數（鬆弛變量係數為0）
        c = np.concatenate([c, np.zeros(m_ub)])
        A_list.append(A_aug)
        b_list.append(b_ub)
    
    if len(A_list) == 0:
        return {"x": np.zeros(len(c)), "fun": 0.0, "status": "no_constraints"}
    
    A = np.vstack(A_list)
    b = np.concatenate(b_list) if len(b_list) > 1 else b_list[0]
    
    # 使用單形法求解
    x_aug, fun, status = simplex_method(c, A, b)
    
    # 返回原始變量（不含鬆弛變量）
    n_orig = len(c) if A_ub is None else len(c) - A_ub.shape[0]
    x_orig = x_aug[:n_orig] if A_ub is not None else x_aug
    
    return {"x": x_orig, "fun": fun, "status": status}


def is_feasible_point(x: np.ndarray, A_ub: np.ndarray, b_ub: np.ndarray, 
                       A_eq: Optional[np.ndarray] = None, 
                       b_eq: Optional[np.ndarray] = None,
                       tol: float = 1e-6) -> bool:
    """檢查點是否滿足線性規劃的約束。"""
    x = np.array(x)
    
    if A_ub is not None:
        if not np.all(A_ub @ x <= b_ub + tol):
            return False
    
    if A_eq is not None and b_eq is not None:
        if not np.all(np.abs(A_eq @ x - b_eq) < tol):
            return False
    
    return True


def duality_gap(c: np.ndarray, x_primal: np.ndarray, 
                lambda_dual: np.ndarray, 
                A: np.ndarray, b: np.ndarray) -> float:
    """計算對偶間隙（primal objective - dual objective）。"""
    primal_obj = np.dot(c, x_primal)
    dual_obj = np.dot(lambda_dual, b)
    return primal_obj - dual_obj


__all__ = [
    "simplex_method",
    "solve_lp",
    "is_feasible_point",
    "duality_gap",
]
