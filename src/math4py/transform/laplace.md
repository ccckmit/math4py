# 拉普拉斯轉換 (Laplace Transform)

## 概述

拉普拉斯轉換模組提供拉普拉斯轉換的數值計算與應用，包括轉換、逆轉換、ODE 求解、摺積定理、部分分式分解等。

## 數學原理

### 1. 拉普拉斯轉換
$$F(s) = \mathcal{L}\{f(t)\} = \int_0^{\infty} f(t) e^{-st} dt$$

$s = \sigma + i\omega$ 為複數頻率參數。

### 2. 逆拉普拉斯轉換 (Bromwich 積分)
$$f(t) = \frac{1}{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty} F(s) e^{st} ds$$

簡化形式：
$$f(t) \approx \frac{e^{\sigma t}}{\pi}\int_0^{\infty} \text{Re}(F(\sigma+i\omega)e^{i\omega t}) d\omega$$

### 3. 常見轉換對

| $f(t)$ | $F(s)$ |
|--------|--------|
| $u(t)$（單位階躍） | $1/s$ |
| $e^{-at}$ | $1/(s+a)$ |
| $\sin(\omega t)$ | $\omega/(s^2+\omega^2)$ |
| $\cos(\omega t)$ | $s/(s^2+\omega^2)$ |
| $t^n$ | $n!/s^{n+1}$ |

### 4. 導數定理
$$\mathcal{L}\{f'(t)\} = sF(s) - f(0)$$
$$\mathcal{L}\{f''(t)\} = s^2F(s) - sf(0) - f'(0)$$

### 5. 摺積定理
$$\mathcal{L}\{f * g\} = \mathcal{L}\{f\} \cdot \mathcal{L}\{g\}$$

### 6. ODE 求解應用

對於 $y' + ay = b$, $y(0) = y_0$:
$$Y(s) = \frac{y_0 + b/s}{s + a}$$
$$y(t) = y_0 e^{-at} + \frac{b}{a}(1 - e^{-at})$$

### 7. 部分分式分解
$$\frac{P(s)}{Q(s)} = \sum_i \frac{R_i}{s - p_i}$$

便於逆轉換。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `laplace_transform()` | 數值拉普拉斯轉換 |
| `inverse_laplace_bromwich()` | 數值逆拉普拉斯轉換 |
| `laplace_transform_pairs()` | 返回轉換對字典 |
| `laplace_derivative_property()` | 驗證導數定理 |
| `solve_ode_laplace()` | 解一階線性 ODE |
| `convolution_theorem_laplace()` | 驗證摺積定理 |
| `partial_fraction_decomposition()` | 部分分式分解 |

## 使用方式

```python
from math4py.transform.laplace import *
import numpy as np

# 拉普拉斯轉換
f = lambda t: np.exp(-2*t)
F = laplace_transform(f, s=1+1j)

# 逆拉普拉斯轉換
F = lambda s: 1/(s+1)  # e^(-t) 的轉換
f_t = inverse_laplace_bromwich(F, t=1.0)

# 轉換對
pairs = laplace_transform_pairs()
for name, (f, F) in pairs.items():
    print(f"{name}: F(1) = {F(1)}")

# 解 ODE: y' + 2y = 5, y(0) = 1
y = solve_ode_laplace(a=2, b=5, y0=1)
print(y(0.5))  # t=0.5 時的 y 值

# 驗證導數定理
f = lambda t: np.sin(2*t)
error = laplace_derivative_property(f, s=1+1j, f0=0)

# 部分分式
coeffs = partial_fraction_decomposition([1], [1, 2, 1])  # 1/(s²+2s+1)
```