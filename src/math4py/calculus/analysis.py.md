# 概述

分析學（Analysis）基礎函數模組，提供極限、連續性、一致連續性、收斂性以及定理驗證等功能。

# 數學原理

## 極限 (Limit)

$$\lim_{x \to x_0} f(x) = L$$

若左極限和右極限存在且相等，則極限存在。

## 連續性 (Continuity)

函數 $f$ 在 $x_0$ 處連續：
$$\lim_{x \to x_0} f(x) = f(x_0)$$

## 一致連續 (Uniform Continuity)

$f$ 在區間 $I$ 上一致連續：
$$\forall \varepsilon > 0, \exists \delta > 0, \forall x_1, x_2 \in I: |x_1 - x_2| < \delta \Rightarrow |f(x_1) - f(x_2)| < \varepsilon$$

## 函數序列收斂

### 點態收斂 (Pointwise Convergence)
$$\forall x, \forall \varepsilon > 0, \exists N, \forall n > N: |f_n(x) - f(x)| < \varepsilon$$

### 一致收斂 (Uniform Convergence)
$$\forall \varepsilon > 0, \exists N, \forall n > N, \forall x: |f_n(x) - f(x)| < \varepsilon$$

即 $\sup_x |f_n(x) - f(x)| \to 0$

## 重要定理

### 介值定理 (Intermediate Value Theorem)
若 $f$ 在 $[a,b]$ 連續且 $f(a) \cdot f(b) < 0$，則 $\exists c \in (a,b)$ 使得 $f(c) = 0$。

### 均值定理 (Mean Value Theorem)
若 $f$ 在 $[a,b]$ 連續且在 $(a,b)$ 可導，則 $\exists c \in (a,b)$ 使得：
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### 極值定理 (Extreme Value Theorem)
連續函數在閉區間上必有最大值和最小值。

### 柯西數列 (Cauchy Sequence)
$$a_n$ 為柯西數列：$\forall \varepsilon > 0, \exists N, \forall m,n > N: |a_m - a_n| < \varepsilon$$

# 實作細節

## 極限計算
```python
def limit(f, x0, direction="both", h=1e-6):
    if direction == "both":
        left_val = f(x0 - h)
        right_val = f(x0 + h)
        if abs(left_val - right_val) < 1e-4:
            return (left_val + right_val) / 2.0, "exists"
        return float("nan"), "does_not_exist"
```

## 介值定理（二分法）
```python
def intermediate_value_theorem(f, a, b, tol=1e-6):
    f_a, f_b = f(a), f(b)
    if f_a * f_b < 0:
        left, right = (a, b) if f_a < 0 else (b, a)
        for _ in range(50):
            mid = (left + right) / 2.0
            if abs(f(mid)) < tol:
                return True, mid
            if f(mid) < 0:
                left = mid
            else:
                right = mid
```

## 均值定理驗證
```python
def mean_value_theorem(f, a, b, f_prime):
    slope = (f(b) - f(a)) / (b - a)
    x_samples = np.linspace(a + 0.01, b - 0.01, 100)
    for c in x_samples:
        if abs(f_prime(c) - slope) < 0.1:
            return True, c
```

# 使用方式

```python
from math4py.calculus.analysis import (
    limit, is_continuous, is_uniformly_continuous,
    intermediate_value_theorem, mean_value_theorem
)

# 極限計算
f = lambda x: (x**2 - 4) / (x - 2)
lim_val, status = limit(f, 2.0)  # 趨近於 4

# 連續性檢查
f = lambda x: x**2
is_cont = is_continuous(f, 1.0)  # True

# 介值定理（找零點）
f = lambda x: x**2 - 2
exists, root = intermediate_value_theorem(f, 0, 2)  # root ≈ √2
```