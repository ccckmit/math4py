# 拓撲學定理驗證

## 概述

本模組驗證拓撲學中的重要定理，包括歐拉多面體定理、豪斯多夫分離定理、海涅-博雷爾定理等。

## 數學原理

### 核心定理

1. **歐拉多面體定理**：V - E + F = 2 - 2g
   - g 為虧格數（ genus）
   - 球面 g=0，環面 g=1

2. **豪斯多夫分離定理**：T₂ 空間中任意兩不同點可用不相交開集分離

3. **海涅-博雷爾定理**：Rⁿ 中子集緊緻 ⟺ 閉且有界

4. **布勞維爾不動點定理**：從閉單位球到自身的連續映射必有不動點

5. **尤瑞-萊夫謝茨不動點定理**：
   - Λ_f = Σ(-1)ⁱ Tr(Df|H_i) = Σ 1（不動點數）

## 實作細節

### 定理驗證函數

| 函數 | 驗證內容 |
|------|----------|
| `euler_characteristic_theorem(v, e, f, g)` | V - E + F = 2 - 2g |
| `hausdorff_separation_theorem(points, distance_fn)` | 點可被開集分離 |
| `compactness_heine_borel(closed, bounded)` | 閉且有界 ⟺ 緊緻 |
| `connectedness_continuum(connected, path_connected)` | 道路連通 ⇒ 連通 |
| `homeomorphism_invariance(t1, t2, f, f_inv)` | 同胚不變性 |
| `urey_lefschetz_fixed_point(chi, fixed_points)` | 萊夫謝茨數 = 不動點數 |
| `brouwer_fixed_point_theorem(dim)` | 存在不動點 |

## 使用方式

```python
from math4py.topology.theorem import (
    euler_characteristic_theorem,
    compactness_heine_borel,
    brouwer_fixed_point_theorem
)

# 歐拉多面體定理（立方體，g=0）
result = euler_characteristic_theorem(vertices=8, edges=12, faces=6, genus=0)
# result["pass"] = True, chi = 2

# 海涅-博雷爾定理
result = compactness_heine_borel(closed=True, bounded=True)
# result["pass"] = True（緊緻）

# 布勞維爾不動點定理
result = brouwer_fixed_point_theorem(dim=2)
# result["pass"] = True
```