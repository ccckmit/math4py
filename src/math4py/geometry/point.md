# Point Class

## 概述

N 維點類別，支援二維和三維點的創建與基本幾何運算。

## 數學原理

### 點的表示
- 2D 點: $P = (x, y)$
- 3D 點: $P = (x, y, z)$
- N 維點: $P = (x_1, x_2, ..., x_n)$

### 點到點距離 (Euclidean Distance)
$$d(P_1, P_2) = \|P_1 - P_2\| = \sqrt{\sum_{i=1}^{n}(x_i^{(1)} - x_i^{(2)})^2}$$

### 點加減向量
$$P + \vec{v} = (x + v_x, y + v_y, z + v_z)$$
$$P_2 - P_1 = \vec{v} \text{ (從 } P_1 \text{ 到 } P_2 \text{ 的向量)}$$

## 實作細節

### 核心屬性
- `_data`: numpy 陣列儲存座標
- `x`, `y`, `z`: 快速存取前三維座標
- `n`: 維度

### 關鍵方法

```python
class Point:
    def distance_to(self, other: Point) -> float:
        """計算到另一點的距離"""
        return float(np.linalg.norm(self._data - other._data))
    
    def to_vector(self) -> Vector:
        """轉換為從原點出發的向量"""
        return Vector(self._data)
    
    def __sub__(self, other) -> "Point | Vector":
        """點減點 = 向量，點減向量 = 點"""
```

### 運算
- 加法: `Point + Vector = Point`
- 減法: `Point - Point = Vector`
- 減法: `Point - Vector = Point`

## 使用方式

```python
from math4py.geometry.point import Point

# 創建 2D 點
p1 = Point(1, 2)
p2 = Point(4, 6)

# 創建 3D 點
p3 = Point(1, 2, 3)

# 從列表創建
p4 = Point([1, 2, 3, 4])  # 4D 點

# 計算距離
d = p1.distance_to(p2)

# 轉換為向量
v = p1.to_vector()

# 點運算
p3 = p1 + Vector(1, 1)
v = p2 - p1
p4 = p1 - Vector(1, 1)
```