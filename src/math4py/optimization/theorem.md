# optimization/theorem.md

## 概述

優化定理驗證模組，驗證凸優化、最優性條件、收斂性等理論。

## 數學原理

### 凸函數的一階條件 (First-Order Condition)
f 為凸函數當且僅當：
$$f(y) \geq f(x) + \nabla f(x) \cdot (y-x), \quad \forall x,y$$

### 凸函數的二階條件 (Second-Order Condition)
f 為凸函數當且僅當 Hessian 矩陣 H(x) 半正定：
$$H(x) \succeq 0, \quad \forall x$$

### Weierstrass 極值定理
連續函數在緊集（閉有界集合）上必有最大值和最小值。

### KKT 條件 (Karush-Kuhn-Tucker)
對於約束優化問題：
$$\min f(x) \quad \text{s.t.} \quad g_i(x) \leq 0, h_j(x) = 0$$

KKT 條件：
1. **穩定性**：∇f(x*) + Σ λᵢ∇gᵢ(x*) + Σ μⱼ∇hⱼ(x*) = 0
2. **互補鬆弛**：λᵢgᵢ(x*) = 0
3. **原始可行性**：gᵢ(x*) ≤ 0, hⱼ(x*) = 0
4. **對偶可行性**：λᵢ ≥ 0

### 下降方向定理
若 ∇f(x)·d < 0，則 d 為 f 在 x 的下降方向。

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `convex_first_order_condition(f, grad_f, x, y)` | 凸函數一階條件 |
| `convex_second_order_condition(hess_f, x)` | Hessian 半正定（二階條件） |
| `weierstrass_extreme_value(f, domain_bounds)` | Weierstrass 定理（抽樣驗證） |
| `kkt_conditions(f, constraints, x_star)` | 基本可行性檢查 |
| `gradient_vanishing_at_optimum(f, grad_f, x_opt)` | 極值點梯度為零 |
| `convex_optimality_condition(f, grad_f, x_star, bounds)` | 凸優化最優性條件 |
| `descent_direction_theorem(grad_f, x, direction)` | 下降方向判斷 |

## 使用方式

```python
from math4py.optimization.theorem import convex_first_order_condition, kkt_conditions
import numpy as np

def f(x): return x[0]**2 + x[1]**2
def grad_f(x): return np.array([2*x[0], 2*x[1]])

convex_first_order_condition(f, grad_f, np.array([0., 0.]), np.array([1., 1.]))
# {'pass': True, 'lhs': 2.0, 'rhs': 0.0}
```