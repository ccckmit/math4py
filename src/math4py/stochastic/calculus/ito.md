# stochastic/calculus/ito.md

## 概述

伊藤積分数值計算，實現伊藤引理驗證與二次變分研究。

## 數學原理

### 伊藤積分定義
$$\int_0^T f(t, W(t)) dW(t) = \lim_{\|\Pi\| \to 0} \sum_{i} f(t_i, W(t_i))(W(t_{i+1})-W(t_i))$$

使用左端點 Riemann 求和。

### 伊藤引理 (Itô's Lemma)
若 X(t) 為伊藤過程，f(t, X) 為 C² 函數，則：
$$df = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial x}dX + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(dX)^2$$

對 f(x) = x² 且 dX = dW：
$$df = 2W dW + dt$$

### 經典恆等式
$$\int_0^T W(t) dW(t) = \frac{1}{2}W(T)^2 - \frac{1}{2}T$$

注意：普通微積分的 ∫x dx = x²/2 不同，多了 -½T 項（伊藤修正項）。

### 二次變分
$$[W]_T = \lim_{\|\Pi\| \to 0} \sum (W(t_{i+1})-W(t_i))^2 = T$$

## 實作細節

| 類別/函數 | 說明 |
|----------|------|
| `ItoIntegral(integrand)` | 數值伊藤積分器，`.compute()` 返回路徑 |
| `ItoIntegral.expected_value()` | 驗證 E[∫ f dW] = 0（軔性） |
| `ito_lemma_demo(T, n_steps)` | 驗證 ∫W dW = ½W² - ½T |
| `quadratic_variation_demo(T, n_steps)` | 驗證 [W]_T = T |

## 使用方式

```python
from math4py.stochastic.calculus.ito import ItoIntegral, ito_lemma_demo

# 計算 ∫ W dW
integrand = lambda t, W: W
ito = ItoIntegral(integrand, seed=42)
t, W, I = ito.compute(T=1.0, n_steps=10000)

# 驗證伊藤引理
result = ito_lemma_demo(T=1.0, n_steps=10000)
# result["ito_integral"] ≈ result["analytic"] = 0.5*W² - 0.5*T
```