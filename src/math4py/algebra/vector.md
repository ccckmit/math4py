# algebra/vector.md

## 概述

向量運算包覆模組，向後相容性重導出 `linear_algebra.vector` 的功能。

## 數學原理

本模組為包覆層，實際功能由 `math4py.linear_algebra.vector` 提供，包括：
- 向量點積 (dot product)
- 向量叉積 (cross product)
- 向量範數 (norm)

## 使用方式

```python
from math4py.algebra.vector import dot_product, cross_product, norm_vector

dot_product([1, 2, 3], [4, 5, 6])    # 32
cross_product([1, 0, 0], [0, 1, 0])  # [0, 0, 1]
norm_vector([3, 4])                  # 5.0
```