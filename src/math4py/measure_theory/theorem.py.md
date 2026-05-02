# 測度論定理驗證

## 概述

本模組驗證測度論中的核心定理，包括卡拉西奧多利延拓定理、勒貝格控制收斂定理、富比尼定理、拉東-尼科迪姆定理等。

## 數學原理

### 核心定理

1. **卡拉西奧多利延拓定理**：
   - 外測度在 σ-代數上可延拓為測度

2. **勒貝格控制收斂定理**：
   - 若 f_n → F 且 |f_n| ≤ g（g 可積），則 ∫ f_n → ∫ F

3. **富比尼定理**：
   - 若 ∫∫ |f(x,y)| dxy < ∞，則可交換積分順序

4. **拉東-尼科迪姆定理**：
   - 若 ν << μ，則存在 f 使得 dν = f dμ

5. **L^p 空間完備性**（里斯-費舍爾定理）：
   - L^p 空間是巴拿赫空間

6. **單調收斂定理**：
   - 若 0 ≤ f_n ↑ f，則 ∫ f_n ↑ ∫ f

## 實作細節

### 定理驗證函數

| 函數 | 驗證內容 |
|------|----------|
| `caratheodory_extension(outer_measure, algebra)` | 外測度可延拓 |
| `lebesgue_dominated_convergence(f_n, F, a, b)` | 控制收斂定理 |
| `fubini_theorem(f, a1, b1, a2, b2)` | 富比尼定理 |
| `radon_nikodym(finite_measure, absolute_continuous)` | RN 導數存在 |
| `l_p_completeness(p)` | L^p 完備性 |
| `monotone_convergence(f_n, a, b)` | 單調收斂 |

## 使用方式

```python
import numpy as np
from math4py.measure_theory.theorem import (
    caratheodory_extension,
    lebesgue_dominated_convergence,
    fubini_theorem,
    radon_nikodym,
    l_p_completeness,
    monotone_convergence
)

# 卡拉西奧多利延拓
outer_measure = {frozenset({1}): 0.5, frozenset({2}): 0.5}
algebra = [frozenset({1}), frozenset({2}), frozenset({1,2}), frozenset()]
result = caratheodory_extension(outer_measure, algebra)

# 勒貝格控制收斂定理
f_n = [lambda x: x**2 + 1/n for n in [1, 2, 3]]
F = lambda x: x**2
result = lebesgue_dominated_convergence(f_n, F, 0, 1)

# 富比尼定理
f = lambda x, y: x * y
result = fubini_theorem(f, 0, 1, 0, 1)
# result["integral_xy"] ≈ result["integral_yx"]

# 拉東-尼科迪姆
result = radon_nikodym(finite_measure=1.0, absolute_continuous=True)

# L^p 完備性
result = l_p_completeness(p=2)

# 單調收斂
f_n = [lambda x: (1 - 1/n) * x**2 for n in [1, 2, 3]]
result = monotone_convergence(f_n, 0, 1)
```