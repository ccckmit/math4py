# Stochastic Process Plotting Functions

## 概述

本模組提供隨機過程的視覺化功能，包括布朗運動路徑圖、伊藤積分圖、期權定價圖等，適用於金融數學和隨機微分方程教學。

## 數學原理

### 布朗運動（維納過程）W(t)

- W(0) = 0
- W(t) - W(s) ~ N(0, t-s)（獨立增量）
- 路徑連續但處處不可微

### 伊藤積分

```
∫₀ᵀ W(t) dW(t) = ½ W(T)² - ½ T
```

這來自於伊藤引理：
```
df(W) = 2W dW + dt  (f(W) = W²)
```

### Black-Scholes 模型

股價服從幾何布朗運動：
```
dS = μS dt + σS dW
```

歐式 Put 價格：
```
P = K e^{-rT} N(-d₂) - S₀ N(-d₁)
d₁ = (ln(S/K) + (r + σ²/2)T) / (σ√T)
d₂ = d₁ - σ√T
```

## 實作細節

### 主要函數

| 函數 | 視覺化內容 |
|------|------------|
| `brownian_motion(t, paths, title)` | 多條布朗運動路徑 + 均值 ± 標準差帶 |
| `ito_integral_plot(result, figsize)` | 伊藤積分：路徑、數值vs解析、誤差、公式 |
| `options_plot(bs_result, am_result, t_paths, S_paths, figsize)` | 期權比較：GBM路徑、收益、價格、 Greeks |

### 圖形布局

- `brownian_motion`: 多路徑 + 帶狀均值
- `ito_integral_plot`: 2×2 子圖（布朗路徑、積分比較、誤差、公式）
- `options_plot`: 2×3 子圖（路徑、收益、價格、Delta、比較表、Greeks）

## 使用方式

```python
import numpy as np
from math4py.plot.rplot_stochastic import (
    brownian_motion, ito_integral_plot, options_plot
)

# 布朗運動
n_steps = 100
n_paths = 50
t = np.linspace(0, 1, n_steps)
dt = t[1] - t[0]

# 生成布朗路徑
np.random.seed(42)
paths = np.cumsum(np.random.randn(n_paths, n_steps) * np.sqrt(dt), axis=1)

brownian_motion(t, paths, title="布朗運動 W(t)")

# 伊藤積分圖
W = paths[:3]  # 取 3 條路徑
ito_integral = np.cumsum(W * np.sqrt(dt), axis=1)  # 數值
analytic = 0.5 * W**2 - 0.5 * np.arange(n_steps) * dt  # 解析

result = {
    "t": t, "W": W, "ito_integral": ito_integral, "analytic": analytic
}
ito_integral_plot(result)

# 期權圖（需要 stochastic.calculus.options）
# 假設已有 Black-Scholes 和美式期權結果
# options_plot(bs_result, am_result, t_paths, S_paths)
```