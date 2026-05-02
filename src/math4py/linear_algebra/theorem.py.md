# Linear Algebra Theorems

## 概述

線性代數定理驗證模組，驗證線性代數中的重要定理。

## 數學原理

### 秩-零化度定理 (Rank-Nullity Theorem)
$$\text{rank}(A) + \text{nullity}(A) = n$$
其中 $A$ 為 $m \times n$ 矩陣，nullity = dim(null space)。

### 特徵值定理
對於方陣 $A$：
- $\text{tr}(A) = \sum \lambda_i$ (特徵值之和)
- $\det(A) = \prod \lambda_i$ (特徵值之積)

### SVD 分解定理
$$A = U \Sigma V^T$$
- $U$: $m \times m$ 正交矩陣
- $\Sigma$: $m \times n$ 對角矩陣 (奇異值)
- $V^T$: $n \times n$ 正交矩陣

### 行列式乘法定理
$$\det(AB) = \det(A) \det(B)$$

### 線性獨立判定
向量組線性獨立 $\iff$ 矩陣秩 = 向量個數

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `rank_nullity_theorem(matrix)` | 秩-零化度定理 |
| `eigenvalues_theorem(matrix)` | 特徵值定理 |
| `svd_theorem(matrix)` | SVD 分解定理 |
| `determinant_theorem(matrix)` | 行列式乘法定理 |
| `linear_independence_theorem(vectors)` | 線性獨立判定 |

## 使用方式

```python
from math4py.linear_algebra.theorem import (
    rank_nullity_theorem,
    eigenvalues_theorem,
    svd_theorem,
    determinant_theorem,
    linear_independence_theorem
)

# 秩-零化度定理
A = [[1, 2, 3], [4, 5, 6]]
result = rank_nullity_theorem(A)
# {"pass": True, "rank": 2, "nullity": 1, "n": 3, "sum": 3}

# 特徵值定理
A = [[4, 2], [1, 3]]
result = eigenvalues_theorem(A)

# SVD 定理
A = [[1, 2], [3, 4], [5, 6]]
result = svd_theorem(A)

# 行列式定理
A = [[1, 2], [3, 4]]
result = determinant_theorem(A)

# 線性獨立判定
vectors = [[1, 0], [0, 1]]
result = linear_independence_theorem(vectors)
```