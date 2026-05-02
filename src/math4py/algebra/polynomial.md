# algebra/polynomial.md

## 概述

多項式運算模組，實現多項式的求值、加法、乘法。

## 數學原理

### 霍納法則 (Horner's Method)
多項式求值的高效算法：
$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$$
改寫為：
$$P(x) = ((\cdots(a_n x + a_{n-1})x + \cdots)a_1)x + a_0$$

只需 n 次乘法和 n 次加法。

### 多項式加法
同次冪係數相加，結果次數為 max(deg₁, deg₂)。

### 多項式乘法 (卷積)
$$(f * g)_k = \sum_{i=0}^{k} f_i \cdot g_{k-i}$$
即係數向量的離散卷積。

## 實作細節

| 函數 | 說明 |
|------|------|
| `polynomial_eval(coeffs, x)` | 霍納法則求值，coeffs 為 [a_n, ..., a_0] |
| `polynomial_add(coeffs1, coeffs2)` | 多項式加法 |
| `polynomial_multiply(coeffs1, coeffs2)` | 多項式乘法（離散卷積） |

## 使用方式

```python
from math4py.algebra.polynomial import polynomial_eval, polynomial_add, polynomial_multiply

# P(x) = 2x² + 3x + 1, evaluate at x=2
polynomial_eval([2, 3, 1], 2)  # 2*4 + 3*2 + 1 = 15

# (x + 1) + (x - 1) = 2x
polynomial_add([1, 1], [1, -1])  # [1, 0] (係數)

# (x + 1)(x - 1) = x² - 1
polynomial_multiply([1, 1], [1, -1])  # [1, 0, -1]
```