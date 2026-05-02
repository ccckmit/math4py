# 變分法 (Calculus of Variations)

## 概述

變分法模組提供變分學基礎函數，包括最短路徑、最速降線問題、歐拉-拉格朗日方程等。

## 數學原理

### 1. 路徑長度泛函
$$J[y] = \int_a^b \sqrt{1 + (y')^2} \, dx$$

二維平面上曲線 $y = f(x)$ 的弧長。

### 2. 最速降線問題（Brachistochrone）

在重力場中，求質點從 A 到 B 最快到达的曲線。

能量守恆：$v = \sqrt{2gh}$

時間泛函：
$$T[y] = \int_{x_0}^{x_1} \frac{\sqrt{1+(y')^2}}{\sqrt{2g(y_0-y)}} dx$$

擺線為解。

### 3. 歐拉-拉格朗日方程
$$\frac{\partial L}{\partial y} - \frac{d}{dx}\left(\frac{\partial L}{\partial y'}\right) = 0$$

泛函 $J[y] = \int_a^b L(x, y, y') dx$ 極值的必要條件。

當 $L = F(y')$（不含 x 和 y）時：
$$\frac{d}{dx}(F'(y')) = 0 \implies y'' = 0$$

即直線。

### 4. 測地線

曲面上的最短路徑。如平面上的直線。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `shortest_path_length()` | 計算曲線長度 $\int\sqrt{1+(y')^2}dx$ |
| `geodesic_plane()` | 平面測地線長度 |
| `brachistochrone_time()` | 簡化最速降線時間 |
| `euler_lagrange_simple()` | 簡化歐拉-拉格朗日方程 |

## 使用方式

```python
from math4py.functional.variations import *
import numpy as np

# 最短路徑（圓弧）
f = lambda x: np.sqrt(1 - x**2)  # 單位圓上半部
length = shortest_path_length(f, a=-0.5, b=0.5, n=1000)

# 平面測地線（直線）
length = geodesic_plane(a=0, b=1)  # = 1

# 最速降線時間
t = brachistochrone_time(y0=0, y1=10, g=9.81)

# 歐拉-拉格朗日
x = np.linspace(0, 1, 100)
y_prime = np.sin(2*np.pi*x)
y_second = euler_lagrange_simple(y_prime, x)
```