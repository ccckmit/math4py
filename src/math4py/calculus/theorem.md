# 概述

微積分定理驗證模組，使用數值方法驗證微積分學中的基本定理，包括微積分基本定理、均值定理、Rolle定理、Taylor級數等。

# 數學原理

## 微積分基本定理 (Fundamental Theorem of Calculus)

若 $F'(x) = f(x)$，則：
$$\int_a^b f(x) dx = F(b) - F(a)$$

分為兩部分：
1. 若 $F(x) = \int_a^x f(t) dt$，則 $F'(x) = f(x)$
2. $\int_a^b f(x) dx = F(b) - F(a)$ 其中 $F' = f$

## 均值定理 (Mean Value Theorem)

若 $f$ 在 $[a,b]$ 連續且在 $(a,b)$ 可導，則 $\exists c \in (a,b)$ 使得：
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

## Rolle 定理

若 $f$ 在 $[a,b]$ 連續，在 $(a,b)$ 可導，且 $f(a) = f(b)$，則 $\exists c \in (a,b)$ 使得 $f'(c) = 0$。

## Taylor 定理

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n(x)$$

其中餘項 $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$。

## Leibniz 級數（交錯調和級數）

$$\sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = \frac{\pi}{4}$$

## Wallis 積

$$\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{4n^2}{4n^2 - 1}$$

# 實作細節

## 微積分基本定理驗證
```python
def fundamental_theorem():
    def F(x): return -math.cos(x)  # F'(x) = sin(x) = f(x)
    def f(x): return math.sin(x)
    exact = -math.cos(b) - (-math.cos(a))
    # 使用梯形法和辛普森法數值積分
    num_int = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    error_int = abs(num_int - exact)
    return {"pass": error_int < 1e-3 and error_sim < 1e-3}
```

## 均值定理驗證
```python
def mean_value_theorem():
    def f(x): return x**2
    slope = (f(b) - f(a)) / (b - a)  # (4-0)/(2-0) = 2
    c = (a + b) / 2  # 1
    deriv_at_c = (f(c+h) - f(c-h)) / (2*h)  # 2
    return {"pass": abs(deriv_at_c - slope) < 1e-5}
```

## Taylor 級數驗證
```python
def taylor_theorem():
    x_val = 0.5
    exact = math.exp(x_val)
    # e^x = 1 + x + x^2/2! + x^3/3! + ...
    approx = 1 + x_val + x_val**2/2 + x_val**3/6 + x_val**4/24 + x_val**5/120
    return {"pass": abs(approx - exact) < 0.01}
```

## Leibniz 級數
```python
def leibniz_rule(limit=1000):
    total = 0.0
    for i in range(limit):
        term = ((-1)**i) / (2*i + 1)
        total += term
    exact = math.pi / 4
    return {"pass": abs(total - exact) < 1e-3}
```

## Wallis 積
```python
def wallis_product(limit=1000):
    total = 1.0
    for i in range(1, limit + 1):
        term = (4*i*i) / ((4*i*i) - 1)
        total *= term
    return {"pass": abs(total*2 - math.pi) < 0.1}
```

# 使用方式

```python
from math4py.calculus.theorem import (
    fundamental_theorem, mean_value_theorem, rolle_theorem,
    taylor_theorem, leibniz_rule, wallis_product
)

# 驗證微積分基本定理
result = fundamental_theorem()
print(result["pass"])  # True

# 驗證均值定理
result = mean_value_theorem()
print(result["c"])  # 1.0, f'(1) = 2 = slope

# 驗證 Taylor 級數逼近
result = taylor_theorem()
print(result["error"])  # < 0.01

# 驗證 Leibniz 級數
result = leibniz_rule()
print(result["error"])  # < 0.001
```