# Linear Algebra Functions

## 概述

線性代數基本函數模組，提供矩陣的基本運算，包括行列式、反矩陣、矩陣乘法等。

## 數學原理

### 2x2 行列式
$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

### 2x2 反矩陣
$$A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

### 矩陣乘法
$$(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$$

### 矩陣加法
$$(A + B)_{ij} = A_{ij} + B_{ij}$$

### 純量乘法
$$(cA)_{ij} = c \cdot A_{ij}$$

### 轉置
$$(A^T)_{ij} = A_{ji}$$

### 矩陣跡 (Trace)
$$\text{tr}(A) = \sum_{i=1}^{n} A_{ii}$$

## 實作細節

| 函數 | 說明 |
|------|------|
| `det(matrix)` | 2x2 矩陣行列式 |
| `inverse_2x2(matrix)` | 2x2 矩陣反矩陣 |
| `matrix_multiply(A, B)` | 矩陣乘法 |
| `matrix_add(A, B)` | 矩陣加法 |
| `matrix_scalar_mul(A, s)` | 純量乘法 |
| `transpose(A)` | 轉置 |
| `trace(A)` | 跡 |

## 使用方式

```python
from math4py.linear_algebra.function import (
    det, inverse_2x2, matrix_multiply, 
    matrix_add, matrix_scalar_mul, transpose, trace
)

# 2x2 行列式
d = det([[1, 2], [3, 4]])  # -2

# 2x2 反矩陣
inv = inverse_2x2([[1, 2], [3, 4]])

# 矩陣乘法
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = matrix_multiply(A, B)

# 矩陣加法
D = matrix_add(A, B)

# 純量乘法
E = matrix_scalar_mul(A, 3)

# 轉置
AT = transpose(A)

# 跡
tr = trace([[1, 2], [3, 4]])  # 5
```