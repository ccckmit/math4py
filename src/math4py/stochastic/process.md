# stochastic/process.md

## 概述

隨機過程核心模組，實現標準布朗運動、幾何布朗運動、Ornstein-Uhlenbeck 過程、布朗橋。

## 數學原理

### 標準布朗運動 (Wiener Process) W(t)
定義：
- W(0) = 0
- 增量 W(t)-W(s) ~ N(0, t-s)（獨立增量）
- 路徑連續但處處不可微

性質：E[W(s)W(t)] = min(s, t)，[W]_t = t（二次變分）。

### 幾何布朗運動 (GBM)
$$dS = \mu S dt + \sigma S dW$$
解析解：
$$S(t) = S_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W(t)\right)$$

E[S(t)] = S₀e^(μt)，Var[S(t)] = S₀²e^(2μt)(e^(σ²t)-1)

### Ornstein-Uhlenbeck (均值回歸) 過程
$$dX = \theta(\mu - X)dt + \sigma dW$$
長期均值 = μ，長期方差 = σ²/(2θ)

### 布朗橋 (Brownian Bridge)
條件化布朗運動：B(t) = W(t) | W(0)=a, W(T)=b

## 實作細節

| 類別 | 說明 |
|------|------|
| `BrownianMotion(mu, sigma)` | 標準布朗運動，`.simulate()` 產生路徑 |
| `GeometricBrownianMotion(S0, mu, sigma)` | GBM，`.expected_value(t)`, `.variance(t)` |
| `OrnsteinUhlenbeck(mu, theta, sigma)` | O-U 過程，`.stationary_mean()`, `.stationary_variance()` |
| `BrownianBridge(a, b)` | 布朗橋，條件化布朗運動 |

## 使用方式

```python
from math4py.stochastic.process import BrownianMotion, GeometricBrownianMotion

bm = BrownianMotion(seed=42)
t, paths = bm.simulate(T=1.0, n_steps=1000, n_paths=5)

gbm = GeometricBrownianMotion(S0=100, mu=0.05, sigma=0.2, seed=42)
t, paths = gbm.simulate(T=1.0, n_steps=252)
gbm.expected_value(1.0)  # 100*e^0.05 ≈ 105.127
```