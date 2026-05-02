# Vector Class

## 概述

N 維向量類別，支援向量的基本運算、內積、外積、歸一化等。

## 數學原理

### 向量表示
$$\vec{v} = (v_x, v_y, v_z)$$

### 向量加法
$$\vec{u} + \vec{v} = (u_x + v_x, u_y + v_y, u_z + v_z)$$

### 向量減法
$$\vec{u} - \vec{v} = (u_x - v_x, u_y - v_y, u_z - v_z)$$

### 純量乘法
$$c \cdot \vec{v} = (c \cdot v_x, c \cdot v_y, c \cdot v_z)$$

### 點積 (Dot Product)
$$\vec{u} \cdot \vec{v} = u_x v_x + u_y v_y + u_z v_z = \|\vec{u}\|\|\vec{v}\|\cos\theta$$

### 外積 (Cross Product, 3D only)
$$\vec{u} \times \vec{v} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ u_x & u_y & u_z \\ v_x & v_y & v_z \end{vmatrix}$$

### 向量範數 (Magnitude/Norm)
$$\|\vec{v}\| = \sqrt{v_x^2 + v_y^2 + v_z^2}$$

### 單位向量
$$\hat{v} = \frac{\vec{v}}{\|\vec{v}\|}$$

### 夾角
$$\theta = \arccos\left(\frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\|\|\vec{v}\|}\right)$$

## 實作細節

### 核心屬性
- `_data`: numpy 陣列儲存向量分量
- `x`, `y`, `z`: 快速存取前三維分量
- `n`: 維度

### 關鍵方法

| 方法 | 數學含義 |
|------|----------|
| `dot(other)` | 點積 $\vec{u} \cdot \vec{v}$ |
| `cross(other)` | 外積 $\vec{u} \times \vec{v}$ (3D) |
| `norm()` | 向量長度 $\|\vec{v}\|$ |
| `normalize()` | 單位向量 $\hat{v}$ |
| `angle_to(other)` | 夾角 $\theta$ |
| `is_parallel(other)` | 判定平行 |
| `is_perpendicular(other)` | 判定垂直 |

### 平行/垂直判定
- 平行: $\vec{u} \times \vec{v} = \vec{0}$ 或 $|\vec{u} \cdot \vec{v}| = \|\vec{u}\|\|\vec{v}\|$
- 垂直: $\vec{u} \cdot \vec{v} = 0$

## 使用方式

```python
from math4py.geometry.vector import Vector

# 創建向量
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# 基本運算
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 3

# 點積與外積
dot = v1.dot(v2)
cross = v1.cross(v2)

# 長度與歸一化
norm = v1.norm()
unit = v1.normalize()

# 夾角
angle = v1.angle_to(v2)

# 平行/垂直判定
is_parallel = v1.is_parallel(v2)
is_perpendicular = v1.is_perpendicular(v2)
```