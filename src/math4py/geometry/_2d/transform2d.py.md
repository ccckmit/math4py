# Transform2D Class

## 概述

二維仿射變換類別，支援平移、旋轉、縮放等變換，通過 3x3 齊次座標矩陣實現。

## 數學原理

### 齊次座標 (Homogeneous Coordinates)
2D 點 $(x, y)$ 用三維向量 $(x, y, 1)$ 表示。

### 平移矩陣 (Translation)
$$T(t_x, t_y) = \begin{pmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{pmatrix}$$

### 旋轉矩陣 (Rotation, 逆時針)
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

### 縮放矩陣 (Scaling)
$$S(s_x, s_y) = \begin{pmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

### 變換合成
矩陣乘法右乘：
$$P' = T \cdot R \cdot S \cdot P$$

注意代碼中 `other._matrix @ self._matrix` 表示「先 self，後 other」。

## 實作細節

### 工廠方法

| 方法 | 矩陣 |
|------|------|
| `translation(tx, ty)` | 平移矩陣 |
| `rotation(angle)` | 旋轉矩陣 (弧度) |
| `scaling(sx, sy)` | 縮放矩陣 |
| `scaling_uniform(s)` | 均勻縮放 |

### 變換應用
- `apply_point(p)`: 變換點 (含平移)
- `apply_vector(v)`: 變換向量 (不含平移)

### 變換合成
```python
T = Transform2D.translation(1, 0)
R = Transform2D.rotation(math.pi/2)
S = Transform2D.scaling(2, 2)

# T 然後 R 然後 S
combined = S @ R @ T
```

## 使用方式

```python
from math4py.geometry._2d.transform2d import Transform2D
from math4py.geometry.point import Point
from math4py.geometry.vector import Vector

# 平移
T = Transform2D.translation(3, 4)
p_transformed = T.apply_point(Point(1, 1))

# 旋轉 (45度)
R = Transform2D.rotation(math.pi/4)
p_rotated = R.apply_point(Point(1, 0))

# 縮放
S = Transform2D.scaling(2, 2)
p_scaled = S.apply_point(Point(1, 1))

# 均勻縮放
U = Transform2D.scaling_uniform(3)

# 向量變換 (無平移)
v = Vector(1, 0)
v_rotated = R.apply_vector(v)

# 變換合成
combined = S @ R @ T
p_final = combined.apply_point(Point(1, 1))

# 逆變換
inverse = combined.inverse()
p_original = inverse.apply_point(p_final)
```