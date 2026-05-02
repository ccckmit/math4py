# 泛函分析 (Functional Analysis)

## 概述

泛函分析模組提供泛函分析基礎函數，包括 L^p 範數、內積、Gram-Schmidt 正交化、線性算子、譜半徑、弱收斂測試等。

## 數學原理

### 1. L^p 範數
$$\|f\|_p = \left(\int_a^b |f(x)|^p dx\right)^{1/p}$$

當 $p=2$ 時為 L² 範數。

### 2. L² 內積
$$\langle f, g \rangle = \int_a^b f(x) g(x) dx$$

### 3. Gram-Schmidt 正交化
Given $\{f_1, f_2, \ldots\}$:
$$e_1 = f_1$$
$$e_n = f_n - \sum_{i=1}^{n-1} \frac{\langle f_n, e_i \rangle}{\langle e_i, e_i \rangle} e_i$$

### 4. 線性算子
$$(Tf)(x) = \int_a^b K(x,y) f(y) dy$$

積分算子，核函數 $K(x,y)$。

### 5. 譜半徑
$$\rho(A) = \max_i |\lambda_i|$$

矩陣 A 的最大特徵值模長。

### 6. 解集
$$R(z) = (A - zI)^{-1}$$

算子 A 的預解式。

### 7. 弱收斂
$$f_n \rightharpoonup f \iff \int (f_n - f)\phi \, dx \to 0 \quad \forall \phi \in C_c^\infty$$

### 8. 緊緻算子
通過奇異值衰減判定：有限秩逼近。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `norm_Lp()` | 計算 L^p 範數 |
| `norm_L2()` | 計算 L² 範數 |
| `inner_product_L2()` | 計算 L² 內積 |
| `gram_schmidt_L2()` | Gram-Schmidt 正交化 |
| `is_orthogonal_L2()` | 檢查正交性 |
| `linear_operator_apply()` | 應用積分算子 |
| `spectral_radius()` | 計算譜半徑 |
| `resolvent_set()` | 計算預解式 |
| `function_space_basis()` | 生成多項式基 |
| `weak_convergence_test()` | 弱收斂測試 |
| `compact_operator_test()` | 緊緻算子測試 |

## 使用方式

```python
from math4py.functional.function import *
import numpy as np

# L^2 範數
f = lambda x: np.sin(x)
norm = norm_L2(f, a=0, b=np.pi)

# L^2 內積
g = lambda x: np.cos(x)
inner = inner_product_L2(f, g, a=0, b=np.pi)

# Gram-Schmidt 正交化
funcs = [lambda x: 1+x, lambda x: x+x**2, lambda x: x**2]
ortho = gram_schmidt_L2(funcs, a=0, b=1)

# 線性算子
K = lambda x, y: np.exp(-(x-y)**2)
x_out = np.linspace(0, 1, 50)
f_in = lambda y: np.ones_like(y)
result = linear_operator_apply(K, f_in, x_out, a=0, b=1)

# 譜半徑
A = np.array([[0.5, 0.2], [0.1, 0.8]])
rho = spectral_radius(A)

# 多項式基
basis = function_space_basis(n_terms=5)

# 弱收斂測試
f_n = [lambda x, i=i: np.sin(i*x) for i in range(1, 5)]
f = lambda x: np.zeros_like(x)
error = weak_convergence_test(f_n, f, a=0, b=np.pi)
```