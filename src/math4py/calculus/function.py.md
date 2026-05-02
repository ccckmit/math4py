# 概述

數值微積分函數模組，提供數值微分、數值積分、極限計算與泰勒級數逼近等基本數值計算功能。

# 數學原理

## 數值微分 (Numerical Differentiation)

### 中央差分法 (Central Difference)
$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$$

誤差的數量級為 $O(h^2)$。

### 二階導數
$$f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$$

## 數值積分 (Numerical Integration)

### 梯形法 (Trapezoidal Rule)
$$\int_a^b f(x)dx \approx \frac{h}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

其中 $h = (b-a)/n$。

### 辛普森法 (Simpson's Rule)
$$\int_a^b f(x)dx \approx \frac{h}{3} \left[ f(x_0) + f(x_n) + 4\sum_{i \text{ odd}} f(x_i) + 2\sum_{i \text{ even}} f(x_i) \right]$$

要求 $n$ 為偶數，精度為 $O(h^4)$。

### 中點法 (Midpoint Rule)
$$\int_a^b f(x)dx \approx h \sum_{i=0}^{n-1} f\left(x_i + \frac{h}{2}\right)$$

## 泰勒級數 (Taylor Series)
$$f(x) \approx f(x_0) + \frac{f'(x_0)}{1!}(x-x_0) + \frac{f''(x_0)}{2!}(x-x_0)^2 + \cdots + \frac{f^{(n)}(x_0)}{n!}(x-x_0)^n$$

# 實作細節

## 導數計算

```python
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h=1e-5):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)
```

- 使用中央差分近似，誤差不包含 $O(h)$ 項
- 預設步長 $h = 10^{-5}$，在浮點精度和逼近精度間取得平衡

## 積分計算

```python
def integral(f, a, b, n=1000):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

def simpson(f, a, b, n=100):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))
```

- `integral`: 標準梯形法，適合一般函數
- `simpson`: 自動確保 $n$ 為偶數，對平滑函數精度更高

## 級數逼近

```python
def taylor_series(f, x0, n=5):
    def poly(x):
        result = f(x0)
        for i in range(1, n + 1):
            result += (x - x0)**i / np.math.factorial(i)
        return result
    return poly
```

# 使用方式

```python
from math4py.calculus.function import derivative, integral, taylor_series

# 數值微分
f = lambda x: x**3
df = derivative(f, 2.0)  # f'(2) ≈ 12

# 數值積分
integral_f = lambda x: x**2
result = integral(integral_f, 0, 1)  # ≈ 1/3

# 泰勒級數逼近
import math
exp_taylor = taylor_series(math.exp, 0, 10)
approx = exp_taylor(0.5)  # e^0.5 的逼近值
```