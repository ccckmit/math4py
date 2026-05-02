# 非歐幾何定理驗證

## 概述

本模組驗證非歐幾何中的核心定理，包括雙曲平行公設、球面三角形內角和、Gauss-Bonnet 定理等。

## 數學原理

### 核心定理

1. **雙曲平行公設**：過直線外一點存在無窮多條平行線
   - 等價於：三角形內角和 < π

2. **球面幾何**：三角形內角和 > π
   - Girard's theorem: Area = α + β + γ - π

3. **橢圓幾何**：三角形內角和 > π（類似球面，但點對被識別）

4. **Gauss-Bonnet 定理**（非歐幾何）：
   - 球面：∫_M K dA = 2π - (α+β+γ)
   - 雙曲：∫_M K dA = (α+β+γ) - 2π

5. **雙曲畢氏定理**：
   ```
   cosh(c) = cosh(a) · cosh(b)  （理想直角三角形）
   ```

## 實作細節

### 定理驗證函數

| 函數 | 驗證內容 |
|------|----------|
| `hyperbolic_parallel_postulate()` | 雙曲三角形內角和 < π |
| `spherical_triangle_angle_sum(p1, p2, p3)` | 球面三角形內角和 > π |
| `elliptic_triangle_angle_sum(p1, p2, p3)` | 橢圓三角形內角和 > π |
| `gauss_bonnet_hyperbolic(area, angle_sum)` | Area = π - (α+β+γ) |
| `gauss_bonnet_spherical(area, angle_sum)` | Area = (α+β+γ) - π |
| `pythagorean_hyperbolic(a, b)` | cosh(c) = cosh(a)cosh(b) |

## 使用方式

```python
import numpy as np
from math4py.non_euclidean_geometry.function import HyperbolicPoint, SphericalPoint
from math4py.non_euclidean_geometry.theorem import (
    hyperbolic_parallel_postulate,
    spherical_triangle_angle_sum,
    gauss_bonnet_hyperbolic,
    gauss_bonnet_spherical
)

# 雙曲平行公設驗證
result = hyperbolic_parallel_postulate()
# 三角形內角和 < π，pass = True

# 球面三角形內角和
p1 = SphericalPoint(np.pi/3, 0)
p2 = SphericalPoint(np.pi/3, 2*np.pi/3)
p3 = SphericalPoint(np.pi/3, 4*np.pi/3)
result = spherical_triangle_angle_sum(p1, p2, p3)
# result["pass"] = True（內角和 > π）

# Gauss-Bonnet 定理驗證
area = 0.5  # 假設面積
angle_sum = np.pi + 0.5
error_h = gauss_bonnet_hyperbolic(area, angle_sum)  # 應接近 0

error_s = gauss_bonnet_spherical(area, angle_sum)
# 假設 area = angle_sum - π，則 error_s ≈ 0
```