# Vector Operations

## 概述

向量運算函數模組，提供向量長度、內積、外積等基本運算。

## 數學原理

### 向量範數 (Euclidean Norm)
$$\|\vec{v}\| = \sqrt{\sum_{i=1}^{n} v_i^2}$$

### 點積 (Dot Product)
$$\vec{u} \cdot \vec{v} = \sum_{i=1}^{n} u_i v_i = \|\vec{u}\|\|\vec{v}\|\cos\theta$$

### 外積 (Cross Product, 3D only)
$$\vec{u} \times \vec{v} = \begin{pmatrix} u_y v_z - u_z v_y \\ u_z v_x - u_x v_z \\ u_x v_y - u_y v_x \end{pmatrix}$$

幾何意義：平行四邊形面積向量，方向遵守右手定則。

## 實作細節

| 函數 | 說明 | 公式 |
|------|------|------|
| `norm_vector(v)` | 向量長度 | $\sqrt{\sum v_i^2}$ |
| `dot_product(v1, v2)` | 內積 | $\sum v_{1i} v_{2i}$ |
| `cross_product(v1, v2)` | 外積 (3D) | 見上方 |

## 使用方式

```python
from math4py.linear_algebra.vector import norm_vector, dot_product, cross_product

# 向量長度
v = [3, 4]
length = norm_vector(v)  # 5.0

# 內積
v1 = [1, 2, 3]
v2 = [4, 5, 6]
dot = dot_product(v1, v2)  # 32

# 外積 (3D)
v1 = [1, 0, 0]
v2 = [0, 1, 0]
cross = cross_product(v1, v2)  # [0, 0, 1]
```