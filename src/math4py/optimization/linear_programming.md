# 線性規劃 (Linear Programming)

## 概述

本模組實現線性規劃的單形法（Simplex Method）及相關輔助函數，用於求解標準形式的 LP 問題。

## 數學原理

### 1. 線性規劃標準形式

$$\min c^T x$$
$$\text{s.t. } Ax = b$$
$$x \geq 0$$

其中：
- $c \in \mathbb{R}^n$：目標函數係數向量
- $A \in \mathbb{R}^{m \times n}$：約束矩陣（假設 $m \leq n$，且行滿秩）
- $b \in \mathbb{R}^m$：約束右端向量

### 2. 單形法核心概念

**基與非基變量**：
- 基本變量（Basic）：恰好 m 個，構成基矩陣 B
- 非基本變量（Non-basic）：其餘 n-m 個，設為 0

**基本可行解 (BFS)**：
$$x_B = B^{-1} b, \quad x_N = 0$$

**單形法表**：

|  | 基本變量 | 非基變量 | RHS |
|--|---------|---------|-----|
| 目標 | $c_B^T B^{-1} N - c_N^T$ | 簡化成本 | $c_B^T B^{-1} b$ |

**入基選擇**：最小簡化成本（最負值）

**出基選擇**（最小比率檢驗）：
$$\min_i \left\{\frac{x_{B,i}}{a_{ik}} : a_{ik} > 0\right\}$$

### 3. 兩階段法 (Two-Phase Simplex)

當無法直接獲得初始 BFS 時使用：

**階段一**：加入人工變量 $a_1, ..., a_m$，求解：
$$\min \sum_{i=1}^m a_i$$
$$\text{s.t. } Ax + Ia = b, x \geq 0, a \geq 0$$

若最優值 > 0，則原問題無可行解。

**階段二**：移除人工變量，用原目標函數繼續求解。

### 4. 對偶理論

**原問題 (P)**：
$$\min c^T x \quad \text{s.t. } Ax = b, x \geq 0$$

**對偶問題 (D)**：
$$\max \lambda^T b \quad \text{s.t. } A^T \lambda \leq c$$

**弱對偶性**：對任意可行 x, λ：
$$c^T x \geq \lambda^T b$$

**強對偶性**：若原問題有最優解，則對偶問題也有，且：
$$c^T x^* = \lambda^{*T} b$$

**對偶間隙 (Duality Gap)**：
$$\text{gap} = c^T x - \lambda^T b$$

### 5. 可行性檢查

點 x 可行若：
$$A_{ub} x \leq b_{ub} + \epsilon$$
$$|A_{eq} x - b_{eq}| \leq \epsilon$$

## 實作細節

```python
def simplex_method(c, A, b, max_iter=1000, tol=1e-10):
    """單形法（兩階段）"""
    m, n = A.shape
    
    # ===== 階段一：添加人工變量 =====
    A_phase1 = np.hstack([A, np.eye(m)])
    c_phase1 = np.concatenate([np.zeros(n), np.ones(m))])
    
    basic = list(range(n, n + m))  # 人工變量索引
    non_basic = list(range(n))
    
    # 迭代直到階段一完成
    for iteration in range(max_iter):
        B = A_phase1[:, basic]
        x_B = np.linalg.solve(B, b)
        c_B = c_phase1[basic]
        lambda_vec = np.linalg.solve(B.T, c_B)
        
        # 計算簡化成本
        reduced_costs = np.zeros(n + m)
        for j in non_basic:
            reduced_costs[j] = c_phase1[j] - np.dot(lambda_vec, A_phase1[:, j])
        
        # 最優性檢查
        if np.all(reduced_costs >= -tol):
            # 檢查人工變量是否為零
            artificial_sum = sum(x_B[i] for i, idx in enumerate(basic) if idx >= n)
            if artificial_sum > tol:
                return np.zeros(n), 0.0, "infeasible"
            break
        
        # 入基
        entering = min(non_basic, key=lambda j: reduced_costs[j])
        
        # 計算方向
        d = np.linalg.solve(B, A_phase1[:, entering])
        
        # 無界檢查
        if np.all(d <= tol):
            return np.zeros(n), float("-inf"), "unbounded"
        
        # 出基（最小比率）
        ratios = [x_B[i]/d[i] if d[i] > tol else float("inf") for i in range(m)]
        leaving_idx = int(np.argmin(ratios))
        
        # 更新基
        basic[leaving_idx] = entering
    
    # ===== 階段二：原目標函數 =====
    # ... 類似迭代 ...
    
    return x, obj_value, "optimal"

def solve_lp(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    """LP 求解包裝函數"""
    # 處理不等式約束：添加鬆弛變量
    if A_ub is not None:
        m_ub = A_ub.shape[0]
        A_aug = np.hstack([A_ub, np.eye(m_ub)])
        c = np.concatenate([c, np.zeros(m_ub)])
        # ... 組合 ...
    
    # 呼叫 simplex_method
    x_aug, fun, status = simplex_method(c, A, b)
    
    # 移除鬆弛變量
    n_orig = ...
    return {"x": x_orig, "fun": fun, "status": status}

def duality_gap(c, x_primal, lambda_dual, A, b):
    """計算對偶間隙"""
    primal_obj = np.dot(c, x_primal)
    dual_obj = np.dot(lambda_dual, b)
    return primal_obj - dual_obj
```

## 使用方式

```python
from math4py.optimization import simplex_method, solve_lp, is_feasible_point, duality_gap

# 標準形式：min c^T x, Ax = b, x >= 0
# max z = 2x1 + 3x2 + 4x3
# s.t. x1 + 2x2 + x3 <= 10
#      2x1 + x2 + 3x3 <= 15
#      x1, x2, x3 >= 0

# 轉換為標準形式後呼叫
c = np.array([2, 3, 4])
A_ub = np.array([[1, 2, 1], [2, 1, 3]])
b_ub = np.array([10, 15])

result = solve_lp(c, A_ub=A_ub, b_ub=b_ub)
print(result)  # {'x': array([...]), 'fun': ..., 'status': 'optimal'}

# 檢查可行性
x_test = np.array([2, 3, 1])
is_feas = is_feasible_point(x_test, A_ub, b_ub)
print(is_feas)  # True/False

# 直接使用單形法
c = np.array([2, 3, 4, 0, 0])  # 添加鬆弛變量
A = np.array([[1, 2, 1, 1, 0], [2, 1, 3, 0, 1]])
b = np.array([10, 15])
x, obj, status = simplex_method(c, A, b)
```

## 限制

本實現為教學用途，處理情況有限：
- 假設 b ≥ 0（可通過乘以 -1 處理）
- 未完整處理混合邊界 bounds
- 未實現內點法