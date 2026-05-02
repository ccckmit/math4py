# 隨機過程函數 (Stochastic Process Functions)

## 概述

本模組提供隨機過程的核心計算：布朗運動、幾何布朗運動、伊藤積分及 Black-Scholes 期權定價模型。

## 數學原理

### 1. 布朗運動 (Brownian Motion)

**定義**：標準布朗運動 W(t) 滿足：
1. W(0) = 0
2. 增量 W(t) - W(s) ~ N(0, t-s)
3. 增量獨立

**離散模擬**：
$$W(t_{i+1}) = W(t_i) + \sqrt{\Delta t} \cdot Z_i$$

其中 $Z_i \sim N(0,1)$，$\Delta t = T/n$。

### 2. 幾何布朗運動 (Geometric Brownian Motion, GBM)

**SDE**：
$$dS = \mu S \, dt + \sigma S \, dW$$

**解析解**：
$$S(t) = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W(t)\right]$$

**對數回報**：
$$\ln S(t) = \ln S_0 + \left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W(t)$$

### 3. 伊藤積分 (Itô Integral)

**定義**：
$$\int_0^T f(t, W(t)) \, dW(t)$$

**性質**：
- 為軩 (martingale)：$E[\int f dW] = 0$
- 等距性：$E[(\int f dW)^2] = E[\int f^2 dt]$

### 4. Black-Scholes 模型

**假設**：
- 股價服從幾何布朗運動
- 無風險利率 r 為常數
- 無交易成本

**歐式看漲期權定價**：
$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

其中：
$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$
$$d_2 = d_1 - \sigma\sqrt{T}$$

**歐式看跌期權**：
$$P = K e^{-rT} N(-d_2) - S_0 N(-d_1)$$

**Greeks**：

| Greek | Call | Put |
|-------|------|-----|
| Delta | $N(d_1)$ | $N(d_1) - 1$ |
| Gamma | $\frac{N'(d_1)}{S\sigma\sqrt{T}}$ | 相同 |
| Vega | $S N'(d_1) \sqrt{T}$ | 相同 |
| Theta | $-\frac{S N'(d_1) \sigma}{2\sqrt{T}} - rK e^{-rT}N(d_2)$ | $-\frac{S N'(d_1) \sigma}{2\sqrt{T}} + rK e^{-rT}N(-d_2)$ |
| Rho | $K T e^{-rT} N(d_2)$ | $-K T e^{-rT} N(-d_2)$ |

其中 $N'(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ 為標準常態 PDF。

## 實作細節

```python
def brownian_motion(T, n_steps=100, seed=None):
    """標準布朗運動模擬"""
    dt = T / n_steps
    t = np.linspace(0, T, n_steps + 1)
    dW = np.sqrt(dt) * np.random.randn(n_steps + 1)
    W = np.cumsum(dW)
    W[0] = 0
    return t, W

def geometric_brownian_motion(S0, mu, sigma, T, n_steps=100, n_paths=1):
    """幾何布朗運動"""
    dt = T / n_steps
    t = np.linspace(0, T, n_steps + 1)
    Z = np.random.randn(n_paths, n_steps + 1)
    dW = np.sqrt(dt) * Z
    W = np.cumsum(dW, axis=1)
    W[:, 0] = 0
    
    drift = (mu - 0.5 * sigma**2) * t
    diffusion = sigma * W
    S = S0 * np.exp(drift + diffusion)
    return t, S

def black_scholes_call(S0, K, T, r, sigma):
    """Black-Scholes 歐式看漲期權"""
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S0*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

def greeks(S0, K, T, r, sigma, option_type="call"):
    """計算 Greeks"""
    d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    if option_type == "call":
        delta = norm.cdf(d1)
        rho = K*T*np.exp(-r*T)*norm.cdf(d2)
    else:
        delta = norm.cdf(d1) - 1
        rho = -K*T*np.exp(-r*T)*norm.cdf(-d2)
    
    gamma = norm.pdf(d1) / (S0*sigma*np.sqrt(T))
    vega = S0*norm.pdf(d1)*np.sqrt(T)
    theta = -S0*norm.pdf(d1)*sigma/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2 if option_type=="call" else -d2)
    
    return {"delta": delta, "gamma": gamma, "vega": vega, "theta": theta, "rho": rho}
```

## 使用方式

```python
from math4py.stochastic import (
    brownian_motion, geometric_brownian_motion,
    black_scholes_call, black_scholes_put, greeks
)

# 布朗運動
t, W = brownian_motion(T=1.0, n_steps=100)

# 幾何布朗運動
t, S = geometric_brownian_motion(S0=100, mu=0.05, sigma=0.2, T=1.0, n_paths=10)

# Black-Scholes 期權定價
S0, K, T, r, sigma = 100, 100, 1, 0.05, 0.2
call_price = black_scholes_call(S0, K, T, r, sigma)
put_price = black_scholes_put(S0, K, T, r, sigma)

# Greeks
g = greeks(S0, K, T, r, sigma, option_type="call")
print(g)  # {'delta': 0.638..., 'gamma': 0.018..., 'vega': 38.2..., 'theta': -6.5..., 'rho': 54.3...}
```