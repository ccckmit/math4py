# Geometry Functions

## 概述

幾何函數模組，提供基本的幾何計算函數，包括距離、面積、體積等計算。

## 數學原理

### Euclidean 距離公式
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

### 中點公式
$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}, \frac{z_1 + z_2}{2}\right)$$

### 直線斜率
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

### 三角形面積 (Shoelace Formula)
$$A = \frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$$

### 圓面積與周長
- 面積: $A = \pi r^2$
- 周長: $C = 2\pi r$

### 球體積與表面積
- 體積: $V = \frac{4}{3}\pi r^3$
- 表面積: $S = 4\pi r^2$

### 圓柱體積
$$V = \pi r^2 h$$

### 圓錐體積
$$V = \frac{1}{3}\pi r^2 h$$

## 實作細節

| 函數 | 說明 |
|------|------|
| `distance(p1, p2)` | 計算兩點間距離 |
| `midpoint(p1, p2)` | 計算兩點中點 |
| `slope(p1, p2)` | 計算直線斜率 |
| `area_triangle(p1, p2, p3)` | 計算三角形面積 |
| `perimeter_triangle(p1, p2, p3)` | 計算三角形周長 |
| `area_circle(radius)` | 計算圓面積 |
| `circumference(radius)` | 計算圓周長 |
| `volume_sphere(radius)` | 計算球體積 |
| `surface_area_sphere(radius)` | 計算球表面積 |
| `volume_cylinder(radius, height)` | 計算圓柱體積 |
| `volume_cone(radius, height)` | 計算圓錐體積 |

## 使用方式

```python
from math4py.geometry.function import distance, midpoint, area_triangle

# 計算兩點距離
p1 = Point(0, 0)
p2 = Point(3, 4)
d = distance(p1, p2)  # 5.0

# 計算中點
m = midpoint(p1, p2)  # Point(1.5, 2.0)

# 計算三角形面積
p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(0, 3)
area = area_triangle(p1, p2, p3)  # 6.0
```