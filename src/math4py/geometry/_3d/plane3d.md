# Plane3D Class

## 概述

三維平面類別，由平面上和一點和平面法向量定義，支援三維空間中平面的各種幾何運算。

## 數學原理

### 平面表示
- 點法式: $P_0$ 為平面上點，$\vec{n}$ 為法向量
- 平面方程: $\vec{n} \cdot (P - P_0) = 0$

### 點是否在平面上
$$P \in \text{Plane} \iff (P - P_0) \cdot \vec{n} = 0$$

### 點到平面距離
$$d = |(P - P_0) \cdot \vec{n}|$$

### 點在平面上的投影
$$P_{proj} = P - ((P - P_0) \cdot \vec{n}) \vec{n}$$

### 直線與平面交點
直線 $P(t) = P_l + t\vec{d}$
$$t = \frac{(P_0 - P_l) \cdot \vec{n}}{\vec{d} \cdot \vec{n}}$$

### 由三點建立平面
利用兩向量叉積求法向量：
$$\vec{n} = (P_2 - P_1) \times (P_3 - P_1)$$

## 實作細節

### 建構函式
```python
Plane3D(point: Point, normal: Vector)
```

### 核心方法

| 方法 | 說明 |
|------|------|
| `contains_point(p)` | 點是否在平面上 |
| `distance_to_point(p)` | 點到平面距離 |
| `project_point(p)` | 點在平面上投影 |
| `line_intersection(line)` | 直線與平面交點 |
| `from_points(p1, p2, p3)` | 由三點建立平面 |
| `is_parallel_to(other)` | 判定平行 |
| `is_perpendicular_to(other)` | 判定垂直 |

### 投影計算
```python
d = self.distance_to_point(p)
sign = 1 if (p - self._point).dot(self._normal) > 0 else -1
offset = self._normal * (sign * d)
return p - offset
```

## 使用方式

```python
from math4py.geometry._3d.plane3d import Plane3D
from math4py.geometry._3d.line3d import Line3D
from math4py.geometry.point import Point
from math4py.geometry.vector import Vector

# 由點和法向量建立
plane = Plane3D(Point(0, 0, 0), Vector(0, 0, 1))

# 由三點建立
plane = Plane3D.from_points(
    Point(1, 0, 0),
    Point(0, 1, 0),
    Point(0, 0, 1)
)

# 點是否在平面上
on_plane = plane.contains_point(Point(1, 1, 0))

# 點到平面距離
d = plane.distance_to_point(Point(0, 0, 5))

# 投影
proj = plane.project_point(Point(0, 0, 5))

# 直線與平面交點
line = Line3D.from_points(Point(0, 0, -1), Point(0, 0, 1))
intersection = plane.line_intersection(line)

# 平行/垂直判定
is_parallel = plane1.is_parallel_to(plane2)
is_perpendicular = plane1.is_perpendicular_to(plane2)
```