# 微分幾何定理驗證

## 概述

本模組驗證微分幾何中的重要定理，包括高斯-博內定理、斯托克斯定理、散度定理、黎曼張量對稱性等。

## 數學原理

### 核心定理

1. **高斯-博內定理**（曲面）：
   ```
   ∫_M K dA = 2π χ(M)
   ```
   閉曲面的總曲率等於 2π 乘以歐拉示性數。

2. **斯托克斯定理**：
   ```
   ∫_∂S F·dr = ∫_S (∇×F)·dS
   ```

3. **散度定理**（高斯定理）：
   ```
   ∫_∂V F·dS = ∫_V (∇·F) dV
   ```

4. **黎曼張量對稱性**：
   - R^i_jkl = -R^i_jlk（反對稱於後兩指標）
   - R^i_jkl + R^i_klj + R^i_ljk = 0（第一比安基恆等式）

5. **里奇張量跡**：
   ```
   R = g^{ij} Ric_ij
   ```

## 實作細節

### 定理驗證函數

| 函數 | 驗證內容 |
|------|----------|
| `gauss_bonnet_theorem(g, K, chi)` | ∫_M K dA = 2π χ(M) |
| `stokes_theorem_check(F, curl_F, surface_vertices)` | ∫_∂S F·dr = ∫_S (∇×F)·dS |
| `divergence_theorem_check(F, div_F, volume_vertices)` | ∫_∂V F·dS = ∫_V (∇·F) dV |
| `riemann_tensor_symmetry(R, d)` | 反對稱性、第一比安基恆等式 |
| `ricci_tensor_trace(Ric, g_inv, d)` | R = g^{ij} Ric_ij |

## 使用方式

```python
import numpy as np
from math4py.differential_geometry.theorem import (
    gauss_bonnet_theorem,
    stokes_theorem_check,
    divergence_theorem_check,
    riemann_tensor_symmetry
)

# 高斯-博內定理（單位球面）
# 球面曲率 K = 1，面積 = 4π，歐拉示性數 χ = 2
g = np.eye(2)
K = 1.0
chi = 2
result = gauss_bonnet_theorem(g, K, chi)
# total_curvature = 4π, expected = 4π, pass = True

# 斯托克斯定理驗證
def F(x):
    return np.array([-x[1], x[0]])

def curl_F(x):
    return 2.0

vertices = [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]
result = stokes_theorem_check(F, curl_F, vertices)

# 黎曼張量對稱性
d = 2
R = np.zeros((d, d, d, d))
R[0, 1, 0, 1] = 1
R[0, 1, 1, 0] = -1
result = riemann_tensor_symmetry(R, d)
```