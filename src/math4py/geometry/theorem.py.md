# Geometry Theorems

## 概述

幾何定理驗證模組，透過實際計算驗證幾何學中的重要定理和公式。

## 數學原理

### 畢氏定理 (Pythagorean Theorem)
$$c^2 = a^2 + b^2$$

### 距離公式
$$d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2$$

### 中點公式
$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

### 斜率公式
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

### 海龍公式 (Heron's Formula)
$$A = \sqrt{s(s-a)(s-b)(s-c)}, \quad s = \frac{a+b+c}{2}$$

### 餘弦定理 (Law of Cosine)
$$c^2 = a^2 + b^2 - 2ab\cos(C)$$

### 正弦定理 (Law of Sine)
$$\frac{a}{\sin(A)} = \frac{b}{\sin(B)}$$

### 歐拉特徵 (Euler Characteristic)
$$V - E + F = 2$$ (凸多面體)

### 多邊形內角和
- 三角形: $\pi$ 弧度
- n 邊形: $(n-2)\pi$ 弧度
- 正 n 邊形內角: $\frac{(n-2)\pi}{n}$

### 向量平行判定 (2D Cross Product)
$$\vec{v}_1 \times \vec{v}_2 = 0 \implies \text{平行}$$

### 向量垂直判定 (Dot Product)
$$\vec{v}_1 \cdot \vec{v}_2 = 0 \implies \text{垂直}$$

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `pythagorean_theorem(a, b, c)` | 畢氏定理 |
| `distance_formula(p1, p2)` | 距離公式 |
| `midpoint_formula(p1, p2, m)` | 中點公式 |
| `slope_formula(p1, p2)` | 斜率公式 |
| `area_triangle_heron(a, b, c, area)` | 海龍公式 |
| `law_of_cosine(a, b, angle_c, c)` | 餘弦定理 |
| `law_of_sine(a, angle_a, b, angle_b)` | 正弦定理 |
| `euler_theorem(V, E, F)` | 歐拉特徵 |
| `angle_sum_triangle(sum_angle)` | 三角形內角和 |
| `angle_sum_polygon(n, sum_angle)` | 多邊形內角和 |
| `interior_angle(n, angle)` | 正多邊形內角 |
| `point_on_line(p, line_p1, line_p2)` | 點是否在線上 |
| `three_points_collinear(p1, p2, p3)` | 三點共線 |
| `parallel_vectors(v1, v2)` | 向量平行 |
| `perpendicular_vectors(v1, v2)` | 向量垂直 |
| `vector_magnitude(v)` | 向量長度 |

## 使用方式

```python
from math4py.geometry.theorem import pythagorean_theorem, law_of_cosine
from math4py.geometry.point import Point

# 驗證畢氏定理
result = pythagorean_theorem(3, 4, 5)
# {"pass": True, "c_sq": 25, "a_sq_plus_b_sq": 25}

# 驗證餘弦定理
result = law_of_cosine(a=3, b=4, angle_c=math.pi/2, c=5)
# {"pass": True, "c_sq": 25, "right": 25}
```