# 非歐幾何（Non-Euclidean Geometry）

## 概述

本模組處理非歐幾何，包括雙曲幾何（龐加萊半平面模型）、球面幾何、橢圓幾何的距離計算和面積公式。

## 數學原理

### 三種幾何比較

| 幾何 | 平行公設 | 內角和 | 曲率 |
|------|----------|--------|------|
| 歐氏 | 一條 | = π | 0 |
| 球面 | 零條 | > π | > 0 |
| 雙曲 | 無窮多條 | < π | < 0 |

### 距離公式

1. **龐加萊半平面雙曲距離**：
   ```
   d(p1, p2) = arccosh(1 + |z1-z2|² / (2 Im(z1) Im(z2)))
   ```
   其中 z = x + iy

2. **球面距離**（大圓距離）：
   ```
   d(p1, p2) = arccos(p1 · p2)    (單位球面)
   ```

3. **橢圓距離**（投影空間 RP²）：
   ```
   d = min(arccos(|p1·p2|), π - arccos(|p1·p2|))
   ```

### 面積公式（Gauss-Bonnet）

- 球面三角形：Area = (α + β + γ) - π
- 雙曲三角形：Area = π - (α + β + γ)

## 實作細節

### 類別

| 類別 | 幾何 |
|------|------|
| `HyperbolicPoint` | 龐加萊半平面模型 (x, y), y > 0 |
| `SphericalPoint` | 單位球面 (θ, φ) |

### 主要函數

| 函數 | 數學含義 |
|------|----------|
| `hyperbolic_distance(p1, p2)` | 雙曲距離（龐加萊半平面） |
| `spherical_distance(p1, p2)` | 球面大圓距離 |
| `elliptic_distance(p1, p2)` | 橢圓幾何距離 |
| `spherical_triangle_area(p1, p2, p3)` | 球面三角形面積 |
| `hyperbolic_area_triangle(p1, p2, p3)` | 雙曲三角形面積（公式） |

## 使用方式

```python
import numpy as np
from math4py.non_euclidean_geometry.function import (
    HyperbolicPoint, SphericalPoint,
    hyperbolic_distance, spherical_distance, elliptic_distance,
    spherical_triangle_area
)

# 雙曲幾何（龐加萊半平面）
p1 = HyperbolicPoint(0, 1)
p2 = HyperbolicPoint(1, 1)
d = hyperbolic_distance(p1, p2)

# 球面幾何
p1 = SphericalPoint(theta=np.pi/4, phi=0)
p2 = SphericalPoint(theta=np.pi/4, phi=np.pi)
d = spherical_distance(p1, p2)  # = π/2

# 球面三角形面積
p1 = SphericalPoint(np.pi/3, 0)
p2 = SphericalPoint(np.pi/3, 2*np.pi/3)
p3 = SphericalPoint(np.pi/3, 4*np.pi/3)
area = spherical_triangle_area(p1, p2, p3)
# 內角和 > π，所以面積 > 0

# 從直角座標建立球面點
cart = np.array([0, 0, 1])
p = SphericalPoint.from_cartesian(cart)  # theta=0, phi=0
```