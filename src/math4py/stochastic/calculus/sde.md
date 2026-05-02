# stochastic/calculus/sde.md

## 概述

隨機微分方程 (SDE) 數值求解器，實現 Euler-Maruyama、Milstein、隨機 RK4。

## 數學原理

### SDE 形式
$$dX = a(t, X) dt + b(t, X) dW$$

a(t, X) = 漂移係數 (drift)，b(t, X) = 擴散係數 (diffusion)

### Euler-Maruyama (強收斂階 0.5)
$$X_{n+1} = X_n + a(t_n, X_n)\Delta t + b(t_n, X_n)\Delta W_n$$

### Milstein (強收斂階 1.0)
$$X_{n+1} = X_n + a \Delta t + b \Delta W + \frac{1}{2} b \cdot b' \cdot ((\Delta W)^2 - \Delta t)$$

額外項 b·b'·((ΔW)²-Δt) 來自伊藤引理。

### 強收斂階
$$E\left[|X_T - X_T^{\text{ref}}|\right] \leq C (\Delta t)^\alpha$$

α=0.5 (Euler), α=1.0 (Milstein), α=2.0 (SRK4)。

## 實作細節

| 方法 | 說明 |
|------|------|
| `euler_maruyama(T, n_steps, n_paths)` | Euler-Maruyama 格式 |
| `milstein(T, n_steps, n_paths, b_prime)` | Milstein 格式（可選提供 b' 或自動差分） |
| `convergence_study(T, steps_list)` | 強收斂誤差研究，計算 log-log 斜率 |

## 使用方式

```python
from math4py.stochastic.calculus.sde import SDESolver

# dX = rX dt + sigma X dW (GBM)
drift = lambda t, x: 0.05 * x
diffusion = lambda t, x: 0.2 * x

sde = SDESolver(drift, diffusion, X0=100.0, seed=42)
t, paths = sde.euler_maruyama(T=1.0, n_steps=1000, n_paths=5)
```