# 微分幾何（Differential Geometry）基礎函數

## 概述

本模組提供微分幾何的核心運算，包括克里斯托費爾符號、黎曼曲率張量、測地線方程、協變導數等。

## 數學原理

### 核心公式

1. **克里斯托費爾符號**（Levi-Civita 聯絡）：
   ```
   Γ^k_ij = ½ g^{kl} (∂_i g_jl + ∂_j g_il - ∂_l g_ij)
   ```

2. **黎曼曲率張量**：
   ```
   R^i_jkl = ∂_k Γ^i_jl - ∂_l Γ^i_jk + Γ^i_mk Γ^m_jl - Γ^i_ml Γ^m_jk
   ```

3. **里奇張量**：
   ```
   Ric_jl = R^i_jil  (對 i 收縮)
   ```

4. **標量曲率**：
   ```
   R = g^{ij} Ric_ij
   ```

5. **測地線方程**：
   ```
   d²x^μ/dτ² + Γ^μ_νρ dx^ν/dτ dx^ρ/dτ = 0
   ```

6. **協變導數**：
   ```
   ∇_j V^i = ∂_j V^i + Γ^i_jk V^k
   ```

## 實作細節

### 主要函數

| 函數 | 數學含義 |
|------|----------|
| `christoffel_symbols(g, g_inv, d)` | 計算 Γ^k_ij |
| `riemann_curvature_tensor(g, Gamma, d)` | 計算 R^i_jkl |
| `ricci_tensor(R, d)` | Ric_jl = R^i_jil |
| `scalar_curvature(Ric, g_inv, d)` | R = g^{ij} Ric_ij |
| `geodesic_equation(t, y, Gamma)` | 測地線 ODE 系統 |
| `levi_civita_connection(g, d)` | 列維-奇維塔聯絡 |
| `lie_derivative(X, Y, coord_diff)` | L_X Y = [X, Y] |
| `covariant_derivative(V, Gamma, coord_diff)` | ∇_j V^i |
| `metric_tensor_sphere(R)` | 球面度量 g_ij |
| `geodesic_distance_sphere(p1, p2, R)` | 大圓距離 |

### 測地線方程的狀態向量

```
y = [x^0, x^1, ..., x^{d-1}, dx^0/dτ, dx^1/dτ, ...]
```

前 d 個分量為位置，後 d 個為速度。

## 使用方式

```python
import numpy as np
from math4py.differential_geometry.function import (
    christoffel_symbols, riemann_curvature_tensor,
    ricci_tensor, scalar_curvature, geodesic_equation
)

# 歐氏平面度量
g = np.eye(2)
g_inv = np.eye(2)

# 克里斯托費爾符號（平直空間為 0）
Gamma = christoffel_symbols(g, g_inv, 2)
# Gamma[i,j,k] = 0 for Euclidean

# 黎曼曲率張量
R = riemann_curvature_tensor(g, Gamma, 2)

# 里奇張量
Ric = ricci_tensor(R, 2)

# 標量曲率
R_scalar = scalar_curvature(Ric, g_inv, 2)

# 測地線（使用 scipy.integrate.odeint 求解）
# d = 2
# y0 = [1, 0, 0, 1]  # 位置和速度
# sol = integrate.odeint(geodesic_equation, y0, t, args=(Gamma,))
```