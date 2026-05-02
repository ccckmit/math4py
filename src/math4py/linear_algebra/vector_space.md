# VectorSpace Class

## 概述

向量空間基礎類別，定義向量空間的基本操作：加法、純量乘法、零向量、加法逆元。

## 數學原理

### 向量空間定義

向量空間 $V$ 定義在域 $\mathbb{F}$ (如 $\mathbb{R}$ 或 $\mathbb{C}$) 上，需滿足：

1. **加法封閉性**: $\vec{u}, \vec{v} \in V \implies \vec{u} + \vec{v} \in V$
2. **純量乘法封閉性**: $c \in \mathbb{F}, \vec{v} \in V \implies c\vec{v} \in V$
3. **零向量存在**: $\exists \vec{0} \in V, \vec{v} + \vec{0} = \vec{v}$
4. **加法逆元**: $\forall \vec{v}, \exists -\vec{v}, \vec{v} + (-\vec{v}) = \vec{0}$

### 線性組合
$$\vec{y} = c_1 \vec{v}_1 + c_2 \vec{v}_2 + \cdots + c_n \vec{v}_n$$

### 線性獨立
向量組 $\{\vec{v}_1, ..., \vec{v}_n\}$ 線性獨立當且僅當：
$$c_1 \vec{v}_1 + c_2 \vec{v}_2 + \cdots + c_n \vec{v}_n = \vec{0} \implies c_1 = c_2 = \cdots = c_n = 0$$

### 基底
向量空間的一組基是線性獨立且生成整個空間的向量組。

## 實作細節

### 核心屬性
- `dimension`: 向量空間維度
- `field`: 域 (預設 "real")
- `vectors`: 向量列表

### 核心方法

| 方法 | 說明 |
|------|------|
| `add(u, v)` | 向量加法 |
| `scalar_mul(c, v)` | 純量乘法 |
| `zero()` | 零向量 |
| `neg(v)` | 加法逆元 |
| `linear_combination(scalars, vectors)` | 線性組合 |
| `is_linearly_independent(vectors)` | 判定線性獨立 |
| `basis()` | 標準基底 |
| `dimension_of_subspace(vectors)` | 子空間維度 |

## 使用方式

```python
from math4py.linear_algebra.vector_space import VectorSpace

# 建立 R^3 向量空間
vs = VectorSpace(dimension=3, field="real")

# 向量加法
u = [1, 2, 3]
v = [4, 5, 6]
w = vs.add(u, v)  # [5, 7, 9]

# 純量乘法
scaled = vs.scalar_mul(2, u)  # [2, 4, 6]

# 零向量
z = vs.zero()  # [0, 0, 0]

# 加法逆元
neg = vs.neg(u)  # [-1, -2, -3]

# 線性組合
vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
scalars = [2, 3, 4]
combo = vs.linear_combination(scalars, vectors)  # [2, 3, 4]

# 線性獨立判定
is_ind = vs.is_linearly_independent([[1, 0], [0, 1]])  # True

# 標準基底
basis = vs.basis()
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# 子空間維度
dim = vs.dimension_of_subspace([[1, 2, 3], [2, 4, 6]])  # 1
```