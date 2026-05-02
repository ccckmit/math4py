# 隨機過程定理 (Stochastic Process Theorems)

## 概述

本模組驗證隨機過程的核心性質：布朗運動特性、伊藤引理、Black-Scholes 性質及軩性質。

## 數學原理

### 1. 布朗運動基本性質

**均值**：$E[W(t)] = 0$

**變異數**：$\text{Var}[W(t)] = t$

**增量分布**：$W(t) - W(s) \sim N(0, t-s)$

### 2. 幾何布朗運動

**SDE**：$dS = \mu S \, dt + \sigma S \, dW$

**解析解**：$S(t) = S_0 \exp\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W(t)\right]$

**期望值**：
$$E[S(t)] = S_0 e^{\mu t}$$

### 3. 伊藤積分的軩性

對於-adapted 過程 $f(t, W(t))$：
$$E\left[\int_0^t f(s, W(s)) dW(s) \mid \mathcal{F}_u\right] = \int_0^u f(s, W(s)) dW(s)$$

即條件期望等於當前值。

### 4. 伊藤引理 (Itô's Lemma)

對於 $f(S_t)$，其中 $dS = \mu S dt + \sigma S dW$：
$$df = \left(\mu S f'(S) + \frac{1}{2}\sigma^2 S^2 f''(S)\right) dt + \sigma S f'(S) dW$$

### 5. Black-Scholes 平價關係 (Call-Put Parity)

$$C - P = S - K e^{-rT}$$

### 6. 二次變差 (Quadratic Variation)

對布朗運動：
$$[W, W]_T = \lim_{|\Delta| \to 0} \sum W(t_i)^2 = T$$

## 實作細節

```python
def brownian_motion_properties(n_steps=1000, dt=0.01):
    """驗證 E[W(t)]=0, Var[W(t)]=t"""
    n_paths = 500
    W_T_samples = []
    for _ in range(n_paths):
        dW = np.random.normal(0, np.sqrt(dt), n_steps)
        W = np.cumsum(dW)
        W_T_samples.append(W[-1])
    
    W_T = np.array(W_T_samples)
    final_time = n_steps * dt
    
    mean = np.mean(W_T)
    var = np.var(W_T)
    
    return {
        "pass": abs(mean) < threshold and abs(var - final_time) < threshold2,
        "expected_mean": 0,
        "observed_mean": float(mean),
        "expected_var": final_time,
        "observed_var": float(var)
    }

def black_scholes_call_put_parity(S, K, r, sigma, T):
    """驗證 C - P = S - K e^{-rT}"""
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    call = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    put = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
    
    parity_left = call - put
    parity_right = S - K*np.exp(-r*T)
    
    return {"pass": abs(parity_left - parity_right) < 1e-10, ...}

def quadratic_variation(n_steps=1000):
    """驗證 [W,W]_T = T"""
    dt = 1.0 / n_steps
    dW = np.random.normal(0, np.sqrt(dt), n_steps)
    
    QV = np.sum(dW**2)  # 離散近似
    return {"pass": abs(QV - 1.0) < 0.2, "expected_QV": 1.0, "observed_QV": QV}

def ito_lemma_verify(f, S0, mu, sigma, T, n_paths=1000):
    """驗證伊藤引理"""
    dt = T
    dW = np.random.normal(0, np.sqrt(dt), n_paths)
    S_T = S0 * np.exp((mu - 0.5*sigma**2)*T + sigma*dW)
    f_S_T = f(S_T)
    
    def f_prime(x): return 2*x      # 示例：f(x) = x²
    def f_double_prime(x): return 2
    
    drift = (f_prime(S0)*mu*S0 + 0.5*f_double_prime(S0)*sigma**2*S0**2)*T
    expected_f = f(S0) + drift
    
    observed_mean = np.mean(f_S_T)
    error = abs(observed_mean - expected_f)
    
    return {"pass": error < threshold, ...}
```

## 使用方式

```python
from math4py.stochastic.theorem import (
    brownian_motion_properties, black_scholes_call_put_parity,
    quadratic_variation, ito_lemma_verify
)

# 驗證布朗運動性質
result = brownian_motion_properties(n_steps=1000, dt=0.01)
print(result["pass"])  # True/False

# 驗證 Black-Scholes 平價關係
result = black_scholes_call_put_parity(S=100, K=100, r=0.05, sigma=0.2, T=1)
print(result["pass"])  # True

# 驗證二次變差
result = quadratic_variation(n_steps=10000)
print(result["observed_QV"])  # 約 1.0

# 驗證 Black-Scholes Greeks
from math4py.stochastic.theorem import black_scholes_greeks
g = black_scholes_greeks(S=100, K=100, r=0.05, sigma=0.2, T=1)
print(g)  # delta, gamma, vega, theta, rho
```