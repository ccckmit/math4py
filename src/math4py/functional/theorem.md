# 泛函分析定理驗證 (Functional Analysis Theorems)

## 概述

泛函分析定理驗證模組提供泛函分析核心定理的數值驗證，包括柯西-施瓦茲不等式、三角不等式、貝塞爾不等式、帕塞瓦爾恆等式、黎茨表示定理、譜半徑定理等。

## 數學原理

### 1. 柯西-施瓦茲不等式
$$|\langle f, g \rangle| \leq \|f\| \|g\|$$

內積空間的基本不等式。

### 2. 三角不等式
$$\|f + g\| \leq \|f\| + \|g\|$$

### 3. 貝塞爾不等式
$$\sum_{i=1}^n |\langle f, e_i \rangle|^2 \leq \|f\|^2$$

正交基下的能量約束。

### 4. 帕塞瓦爾恆等式
$$\sum_{i=1}^\infty |\langle f, e_i \rangle|^2 = \|f\|^2$$

適用於完備正交基（Parseval's Identity）。

### 5. 黎茨表示定理
每個連續線性泛函 $\phi \in (L^2)^*$ 可唯一表示為：
$$\phi(f) = \langle f, g_\phi \rangle$$

對於 $\phi(f) = \int_a^b f(x)dx$，表示函數為 $g_\phi(x) = 1$。

### 6. 譜半徑定理
$$\rho(A) = \lim_{n\to\infty} \|A^n\|^{1/n} = \max_i |\lambda_i|$$

### 7. 預解式解析性
$$R(z_1) - R(z_2) = (z_2 - z_1) R(z_1) R(z_2)$$

### 8. 平行四邊形法則
$$\|f+g\|^2 + \|f-g\|^2 = 2(\|f\|^2 + \|g\|^2)$$

內積空間的特徵性質。

### 9. Jordan-von Neumann 定理
內積可由範數表示：
$$\langle f, g \rangle = \frac{\|f+g\|^2 - \|f-g\|^2}{4}$$

### 10. 緊緻算子譜
緊緻算子的譜（除 0 外）由离散特征值組成，趨於 0。

## 實作細節

### 關鍵函數

| 函數 | 驗證內容 |
|------|----------|
| `cauchy_schwarz_inequality()` | $\|f\|\|g\| - \|\langle f,g\rangle\| \geq 0$ |
| `triangle_inequality_L2()` | $\|f+g\| - (\|f\|+\|g\|) \leq 0$ |
| `bessel_inequality()` | $\sum \|\langle f,e_i\rangle\|^2 \leq \|f\|^2$ |
| `parseval_identity()` | $\sum \|\langle f,e_i\rangle\|^2 = \|f\|^2$（誤差趨近0） |
| `riesz_representation_test()` | 黎茨表示驗證 |
| `spectral_radius_theorem()` | $\rho(A) \leq \|A\|$ |
| `resolvent_analytic()` | $R(z_1)-R(z_2) = (z_2-z_1)R(z_1)R(z_2)$ |
| `weak_convergence_characterization()` | 弱收斂判斷 |
| `compact_operator_spectrum()` | 緊緻算子譜性質 |

## 使用方式

```python
from math4py.functional.theorem import *
import numpy as np

f = lambda x: np.sin(x)
g = lambda x: np.cos(x)

# 柯西-施瓦茲不等式
residual = cauchy_schwarz_inequality(f, g, a=0, b=np.pi)

# 三角不等式
residual = triangle_inequality_L2(f, g, a=0, b=np.pi)

# 帕塞瓦爾恆等式
basis = [lambda x: np.sqrt(2/np.pi)*np.sin(n*x) for n in range(1, 6)]
error = parseval_identity(f, basis, a=0, b=np.pi)

# 譜半徑定理
A = np.array([[0.5, 0.2], [0.1, 0.8]])
error = spectral_radius_theorem(A)

# 預解式解析性
z1, z2 = 1+1j, 2+1j
error = resolvent_analytic(A, z1, z2)

# 平行四邊形法則
h = lambda x: np.exp(x)
residual = check_parallelogram_law(f, h, a=0, b=1)

# Jordan-von Neumann
residual = check_jordan_vonneumann_theorem(f, g, a=0, b=np.pi)
```