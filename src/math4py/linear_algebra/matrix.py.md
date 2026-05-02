# Matrix Class

## 概述

矩陣類別，包裝 numpy.ndarray，提供統一的矩陣運算接口，專注數值計算。

## 數學原理

### 矩陣基本運算
- 加法: $A + B$
- 減法: $A - B$
- 乘法: $A \times B$ (矩陣乘法)
- 轉置: $A^T$

### 反矩陣
$$A A^{-1} = I$$
使用高斯消去或 LU 分解計算。

### 特徵值與特徵向量
$$Av = \lambda v$$
其中 $\lambda$ 為特徵值，$v$ 為特徵向量。

### SVD 分解
$$A = U \Sigma V^T$$
- $U$, $V$: 正交矩陣
- $\Sigma$: 奇異值對角矩陣

### QR 分解
$$A = QR$$
- $Q$: 正交矩陣
- $R$: 上三角矩陣

### LU 分解
$$A = LU$$
- $L$: 下三角矩陣
- $U$: 上三角矩陣

## 實作細節

### 核心方法

| 方法 | 說明 |
|------|------|
| `inv()` | 反矩陣 |
| `det()` | 行列式 |
| `eigvals()` | 特徵值 |
| `eig()` | 特徵值與特徵向量 |
| `svd()` | SVD 分解 |
| `rank()` | 秩 |
| `norm()` | 範數 |
| `solve(b)` | 解線性方程組 $Ax = b$ |
| `qr()` | QR 分解 |
| `lu()` | LU 分解 |

### 工廠方法

| 方法 | 說明 |
|------|------|
| `eye(n)` | $n \times n$ 單位矩陣 |
| `zeros(shape)` | 零矩陣 |
| `ones(shape)` | 全一矩陣 |
| `random(shape)` | 隨機矩陣 |

## 使用方式

```python
from math4py.linear_algebra.matrix import Matrix

# 創建矩陣
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

# 基本運算
C = A + B
D = A - B
E = A @ B  # 矩陣乘法

# 轉置
AT = A.T

# 反矩陣
A_inv = A.inv()

# 行列式
d = A.det()

# 特徵值
vals = A.eigvals()

# 特徵值與特徵向量
vals, vecs = A.eig()

# SVD 分解
U, S, Vh = A.svd()

# 秩
r = A.rank()

# 範數
n = A.norm()

# 解線性方程組 Ax = b
b = Matrix([[1], [2]])
x = A.solve(b)

# QR 分解
Q, R = A.qr()

# LU 分解
P, L, U = A.lu()

# 工廠方法
I = Matrix.eye(3)
Z = Matrix.zeros((3, 3))
O = Matrix.ones((3, 3))
R = Matrix.random((3, 3))
```