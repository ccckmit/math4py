# Line2D Class

## 概述

二維直線類別，由點和方向向量定義，支援直線的各種幾何運算。

## 數學原理

### 直線表示 (Parametric Form)
$$\vec{P}(t) = \vec{P}_0 + t\vec{d}$$

其中 $\vec{P}_0$ 是直線上一點，$\vec{d}$ 是方向向量。

### 點到直線距離
$$d = \frac{|(P - P_0) \times d|}{\|d\|}$$

2D 情況下：
$$d = |(P - P_0)_x \cdot d_y - (P - P_0)_y \cdot d_x|$$

### 最近點
找到 $t$ 使得 $(P - (P_0 + t\vec{d}))$ 與 $\vec{d}$ 垂直：
$$t = (P - P_0) \cdot \vec{d}$$

### 兩直線交點
求解引數 $t$:
$$t = \frac{(P_2 - P_1) \times \vec{d}_2}{\vec{d}_1 \times \vec{d}_2}$$

其中 $\times$ 為 2D 行列式。

## 實作細節

### 建構函式
```python
Line2D(point: Point, direction: Vector)
```

### 核心方法

| 方法 | 說明 |
|------|------|
| `point_at(t)` | 取得引數 $t$ 對應的點 |
| `distance_to_point(p)` | 點到直線距離 |
| `closest_point(p)` | 直線上最近的點 |
| `from_points(p1, p2)` | 過兩點建立直線 |
| `is_parallel_to(other)` | 判定平行 |
| `is_perpendicular_to(other)` | 判定垂直 |
| `intersection(l1, l2)` | 兩直線交點 |

### 交點計算 (行列式法)
```python
det = dx1 * dy2 - dy1 * dx2
if abs(det) < tol:
    return None  # 平行
t = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / det
```

## 使用方式

```python
from math4py.geometry._2d.line2d import Line2D
from math4py.geometry.point import Point
from math4py.geometry.vector import Vector

# 由點和方向向量建立
line = Line2D(Point(0, 0), Vector(1, 1))

# 由兩點建立
line = Line2D.from_points(Point(0, 0), Point(3, 4))

# 取得直線上點
p = line.point_at(2.5)

# 點到直線距離
d = line.distance_to_point(Point(1, 1))

# 最近點
closest = line.closest_point(Point(1, 1))

# 平行/垂直判定
is_parallel = line1.is_parallel_to(line2)
is_perpendicular = line1.is_perpendicular_to(line2)

# 兩直線交點
intersection = Line2D.intersection(line1, line2)
```