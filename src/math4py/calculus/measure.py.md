# 概述

測度論（Measure Theory）基礎函數模組，提供測度驗證、勒貝格測度、σ-代數生成以及勒貝格積分等功能的數值計算。

# 數學原理

## 測度 (Measure) 定義

測度 $\mu$ 是滿足以下條件的函數：
1. **非負性**: $\mu(A) \geq 0$ 對所有可測集 $A$
2. **空集合**: $\mu(\emptyset) = 0$
3. **可數可加性**: 對互不相交的集合 $A_1, A_2, \ldots$
   $$\mu\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \mu(A_i)$$

## 勒貝格測度 (Lebesgue Measure)

一維勒貝格測度：
$$\lambda([a, b]) = b - a$$
$$\lambda((a, b)) = b - a$$
$$\lambda(\{x\}) = 0$$

二維勒貝格測度（矩形面積）：
$$\lambda([a,b] \times [c,d]) = (b-a)(d-c)$$

## 外測度 (Outer Measure)
$$\mu^*(A) = \inf\left\{ \sum_{n} \lambda(I_n) : A \subseteq \bigcup_n I_n \right\}$$

## 特殊測度

### 計數測度
$$\mu(A) = |A|$$

### 狄拉克測度 (Dirac Measure)
$$\delta_{x_0}(A) = \begin{cases} 1 & x_0 \in A \\ 0 & x_0 \notin A \end{cases}$$

## σ-代數 (Sigma-Algebra)

由集合族 $\mathcal{C}$ 生成的 σ-代數 $\sigma(\mathcal{C})$ 包含：
- 空集 $\emptyset$
- 所有生成集合
- 所有補集
- 所有可數併集

## 勒貝格積分 (Lebesgue Integral)

對簡單函數 $f = \sum_i a_i \mathbf{1}_{A_i}$：
$$\int f d\mu = \sum_i a_i \mu(A_i)$$

# 實作細節

## 測度驗證
```python
def is_measure(mu, sets):
    # 檢查空集測度
    mu_empty = mu(set())
    if abs(mu_empty) > 1e-10:
        return False, f"μ(∅) = {mu_empty} ≠ 0"
    # 檢查非負性
    # 檢查有限可加性
    return True, "Valid measure"
```

## 勒貝格測度
```python
def lebesgue_measure_1d(interval):
    a, b = interval
    return max(0.0, b - a)

def lebesgue_measure_2d(rectangle):
    a, b, c, d = rectangle
    return max(0.0, (b - a) * (d - c))
```

## σ-代數生成
```python
def sigma_algebra_generated(sets):
    result = [set()]  # 空集
    result.extend(sets)
    # 添加有限併集
    for i in range(len(sets)):
        for j in range(i, len(sets)):
            result.append(sets[i] | sets[j])
    return result
```

# 使用方式

```python
from math4py.calculus.measure import (
    is_measure, lebesgue_measure_1d, lebesgue_measure_2d,
    counting_measure, dirac_measure, sigma_algebra_generated
)

# 一維測度
length = lebesgue_measure_1d((0, 5))  # 5

# 二維測度
area = lebesgue_measure_2d((0, 2, 0, 3))  # 6

# 計數測度
cnt_mu = counting_measure
cnt_mu({1, 2, 3})  # 3

# 狄拉克測度
delta = lambda A: dirac_measure(2.5, A)
delta({2.5})  # 1.0
delta({1, 2, 3})  # 0.0
```