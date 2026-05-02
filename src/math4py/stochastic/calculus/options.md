# stochastic/calculus/options.md

## 概述

期權定價模組，實現 Black-Scholes 歐式期權定價與美式期權數值方法。

## 數學原理

### Black-Scholes 公式 (1973)
風險中立定價，假設股價服從 GBM：
$$dS = r S dt + \sigma S dW$$

歐式Call價格：
$$C = S e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S/K) + (r-q+\sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

### Greeks 敏感度
| Greek | 定義 |
|-------|------|
| Δ = ∂V/∂S | 現貨價格敏感度 |
| Γ = ∂²V/∂S² | Delta 的變化率 |
| Θ = -∂V/∂T | 時間衰減 |
| ν = ∂V/∂σ | 波動率敏感度 |
| ρ = ∂V/∂r | 利率敏感度 |

### Put-Call Parity
$$C - P = S e^{-qT} - K e^{-rT}$$

### 美式期權 (American Option)
可在到期日前任何時間執行，最優停止問題。

**Longstaff-Schwartz LSM**：
- 向後遞推，每步對 ITM 路徑做最小二乘回歸
- 估計 continuation value，比較 immediate exercise

**CRR 二項樹**：
- u = e^(σ√dt), d = 1/u
- p = (e^((r-q)dt)-d)/(u-d)

### 隱含波動率
由市場價格反推 σ，用牛頓-拉夫森法：
$$\sigma_{n+1} = \sigma_n - \frac{C(\sigma_n) - C_{market}}{\partial C/\partial \sigma}$$

## 實作細節

| 類別/方法 | 說明 |
|----------|------|
| `BlackScholes.price(option_type)` | 解析價格 + Greeks |
| `BlackScholes.implied_volatility(market_price)` | 隱含波動率 |
| `BlackScholes.parity_check()` | 驗證 Put-Call Parity |
| `BlackScholes.monte_carlo()` | 對偶變量 MC |
| `AmericanOption.lsm()` | Longstaff-Schwartz LSM |
| `AmericanOption.binomial_tree()` | CRR 二項樹 |
| `AmericanOption.early_exercise_premium()` | 提前執行溢價 |

## 使用方式

```python
from math4py.stochastic.calculus.options import BlackScholes, AmericanOption

bs = BlackScholes(S=100, K=100, T=1, r=0.05, sigma=0.2)
result = bs.price("call")
print(result.price, result.delta, result.gamma)

iv = bs.implied_volatility(12.0)  # 市價12元，反推隱含波動率

am = AmericanOption(S=100, K=100, T=1, r=0.05, sigma=0.2)
price_lsm, se = am.lsm(option_type="put")
```