# 希爾伯特空間理論 (Hilbert Space Theory)

## 概述

希爾伯特空間模組提供希爾伯特空間（無限維完备內積空間）的基礎理論實現，包括內積、範數、距離、投影、正交化、正交基（傅立葉基、Legendre 多項式）、Riesz 表示、平行四邊形法則等。

## 數學原理

### 1. 內積（帶權重）
$$\langle f, g \rangle_w = \int_a^b w(x) f(x) g(x) dx$$

$w(x)$ 為非負權函數。預設 $w(x) = 1$。

### 2. 範數
$$\|f\| = \sqrt{\langle f, f \rangle}$$

### 3. 距離
$$d(f, g) = \|f - g\|$$

### 4. 正交投影係數
$$c = \frac{\langle f, e \rangle}{\langle e, e \rangle}$$

將 f 投影到 e 方向的係數。

### 5. Gram-Schmidt 正交化
與 L² 空間版本相同，但使用一般內積。

### 6. Fourier 基（標準正交）
在 $[-\pi, \pi]$ 上：
$$\left\{\frac{1}{\sqrt{2\pi}}, \frac{\cos(nx)}{\sqrt{\pi}}, \frac{\sin(nx)}{\sqrt{\pi}}\right\}_{n=1}^{\infty}$$

### 7. Legendre 多項式
遞推關係：
$$P_0(x) = 1, \quad P_1(x) = x$$
$$P_n(x) = \frac{2n-1}{n} x P_{n-1}(x) - \frac{n-1}{n} P_{n-2}(x)$$

在 $[-1, 1]$ 上兩兩正交。

### 8. 完備性檢查
基 $\mathcal{B}$ 完備當且僅當任意函數可用基的線性組合逼近。

### 9. Riesz 表示定理
連續線性泛函 $\phi$ 可唯一表示為：
$$\phi(f) = \langle f, g_\phi \rangle$$

其中 $g_\phi$ 由基展開係數確定。

### 10. 平行四邊形法則
$$\|f+g\|^2 + \|f-g\|^2 = 2(\|f\|^2 + \|g\|^2)$$

內積空間的特徵恆等式。

### 11. Jordan-von Neumann 定理
內積可由範數恢復：
$$\langle f, g \rangle = \frac{\|f+g\|^2 - \|f-g\|^2}{4}$$

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `inner_product_H()` | 加權內積計算 |
| `norm_H()` | 範數計算 |
| `distance_H()` | 距離計算 |
| `proj_orthogonal_H()` | 正交投影係數 |
| `gram_schmidt_H()` | Gram-Schmidt 正交化 |
| `fourier_basis_H()` | Fourier 標準正交基 |
| `legendre_polynomials()` | Legendre 多項式 |
| `is_complete_basis_H()` | 基的完備性檢查 |
| `riesz_representation()` | Riesz 表示 |
| `check_parallelogram_law()` | 驗證平行四邊形法則 |
| `check_jordan_vonneumann_theorem()` | 驗證 Jordan-von Neumann |

## 使用方式

```python
from math4py.functional.hilbert_space import *
import numpy as np

f = lambda x: np.sin(x)
g = lambda x: np.cos(x)

# 內積與範數
inner = inner_product_H(f, g, a=0, b=np.pi)
norm_f = norm_H(f, a=0, b=np.pi)

# 距離
d = distance_H(f, g, a=0, b=np.pi)

# 正交投影
e = lambda x: np.sin(2*x)
coeff = proj_orthogonal_H(f, e, a=0, b=np.pi)

# Gram-Schmidt
funcs = [lambda x: 1, lambda x: x, lambda x: x**2]
ortho = gram_schmidt_H(funcs, a=-1, b=1)
# ortho = [(e1, ||e1||²), (e2, ||e2||²), ...]

# Fourier 基
basis = fourier_basis_H(n_max=3)  # 在 [-π,π] 上

# Legendre 多項式
P = legendre_polynomials(n_max=5)  # P_0 到 P_5

# 基的完備性
test_fns = [lambda x: x**2, lambda x: x**3]
is_complete = is_complete_basis_H(basis, test_fns, a=-np.pi, b=np.pi)

# Riesz 表示
phi = lambda f: inner_product_H(f, lambda x: np.ones_like(x), a=0, b=1)
g_phi = riesz_representation(phi, basis, a=0, b=np.pi)

# 平行四邊形法則
residual = check_parallelogram_law(f, g, a=0, b=np.pi)

# Jordan-von Neumann
residual = check_jordan_vonneumann_theorem(f, g, a=0, b=np.pi)
```