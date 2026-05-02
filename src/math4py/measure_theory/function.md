# 測度論（Measure Theory）基礎函數

## 概述

本模組提供測度論的基礎運算，包括 σ-代數、勒貝格測度、勒貝格積分、L^p 範數、赫爾德不等式、閔可夫斯基不等式等。

## 數學原理

### 核心定義

1. **σ-代數**：滿足
   - ∅ 在其中
   - 封閉於補集
   - 封閉於可數並

2. **測度的可數可加性**：
   ```
   μ(∪ A_i) = Σ μ(A_i)  (A_i 兩兩不交)
   ```

3. **勒貝格積分**（梯形法）：
   ```
   ∫_a^b f dλ ≈ Σ (x_{i+1}-x_i) · (f(x_i)+f(x_{i+1}))/2
   ```

4. **L^p 範數**：
   ```
   ||f||_p = (∫ |f|^p dλ)^{1/p}
   ||f||_∞ = ess sup |f(x)|
   ```

5. **赫爾德不等式**：
   ```
   ||fg||_1 ≤ ||f||_p · ||g||_q    (1/p + 1/q = 1)
   ```

6. **閔可夫斯基不等式**：
   ```
   ||f + g||_p ≤ ||f||_p + ||g||_p
   ```

## 實作細節

### 主要函數

| 函數 | 數學含義 |
|------|----------|
| `is_sigma_algebra(sets, universal)` | 檢查是否為 σ-代數 |
| `measure_additivity(sets, measure)` | 可數可加性 |
| `lebesgue_measure_interval(a, b)` | λ([a,b]) = b-a |
| `is_lebesgue_integrable(f, a, b)` | 是否勒貝格可積 |
| `lebesgue_integral(f, a, b, n)` | ∫_a^b f dλ（梯形法） |
| `sigma_finite_measure(measure, universal)` | σ-有限性 |
| `l_infty_norm(f, a, b)` | ||f||_∞ |
| `l_p_norm(f, a, b, p)` | ||f||_p |
| `holder_inequality(f, g, p, q, a, b)` | 赫爾德不等式 |
| `minkowski_inequality(f, g, p, a, b)` | 閔可夫斯基不等式 |

## 使用方式

```python
import numpy as np
from math4py.measure_theory.function import (
    is_sigma_algebra, lebesgue_measure_interval,
    lebesgue_integral, l_p_norm, l_infty_norm,
    holder_inequality, minkowski_inequality
)

# σ-代數檢查
sets = {frozenset(), frozenset({1,2}), frozenset({3}), frozenset({1,2,3})}
universal = frozenset({1,2,3})
is_sigma_algebra(sets, universal)  # True

# 勒貝格測度
lebesgue_measure_interval(0, 5)  # 5
lebesgue_measure_interval(3, 1)  # 0

# 勒貝格積分
f = lambda x: x**2
integral = lebesgue_integral(f, 0, 1, 10000)  # ≈ 1/3

# L^p 範數
g = lambda x: np.exp(-x**2)
norm_2 = l_p_norm(g, -10, 10, 2)  # ||g||_2
norm_inf = l_infty_norm(g, -10, 10)  # ||g||_∞

# 赫爾德不等式
f = lambda x: x**0.5
g = lambda x: 1/(1+x**2)
result = holder_inequality(f, g, p=2, q=2, a=0, b=1)
# result["pass"] = True

# 閔可夫斯基不等式
h1 = lambda x: x
h2 = lambda x: x**2
result = minkowski_inequality(h1, h2, p=2, a=0, b=1)
# result["pass"] = True
```