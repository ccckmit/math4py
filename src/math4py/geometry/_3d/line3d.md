# Line3D Class

## 概述

三維直線類別，由點和方向向量定義，支援三維空間中直線的各種幾何運算。

## 數學原理

### 直線表示 (Parametric Form)
$$\vec{P}(t) = \vec{P}_0 + t\vec{d}$$

其中 $\vec{P}_0$ 是直線上一點，$\vec{d}$ 是方向向量。

### 點到直線距離
$$d = \|(P - P_0) \times \vec{d}\|$$

利用外積的幾何意義：平行四邊形面積等於底乘高。

### 最近點
找到 $t$ 使得 $(P - (P_0 + t\vec{d})) \perp \vec{d}$：
$$t = (P - P_0) \cdot \vec{d}$$

## 實作細節

### 建構函式
```python
Line3D(point: Point, direction: Vector)
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

### 距離計算 (利用外積)
```python
v = p - self._point
cross = v.cross(self._direction)
return cross.norm()
```

## 使用方式

```python
from math4py.geometry._3d.line3d import Line3D
from math4py.geometry.point import Point
from math4py.geometry.vector import Vector

# 由點和方向向量建立
line = Line3D(Point(0, 0, 0), Vector(1, 2, 3))

# 由兩點建立
line = Line3D.from_points(Point(0, 0, 0), Point(1, 2, 3))

# 取得直線上點
p = line.point_at(2.0)

# 點到直線距離
d = line.distance_to_point(Point(1, 1, 1))

# 最近點
closest = line.closest_point(Point(1, 1, 1))

# 平行/垂直判定
is_parallel = line1.is_parallel_to(line2)
is_perpendicular = line1.is_perpendicular_to(line2)
```