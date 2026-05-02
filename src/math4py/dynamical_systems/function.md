# 概述

動力系統（Dynamical Systems）基礎函數模組，提供微分方程數值解法、相空間分析、不動點分析、穩定性分析、李雅普諾夫指數計算以及經典混沌系統（如Lorenz系統、邏輯斯蒂映射）的實現。

# 數學原理

## 常微分方程數值解法

### 歐拉法
$$y_{n+1} = y_n + \Delta t \cdot f(y_n, t_n)$$

### 四階龍格-庫塔法 (RK4)
$$y_{n+1} = y_n + \frac{\Delta t}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

其中：
- $k_1 = f(y_n, t_n)$
- $k_2 = f(y_n + \frac{\Delta t}{2}k_1, t_n + \frac{\Delta t}{2})$
- $k_3 = f(y_n + \frac{\Delta t}{2}k_2, t_n + \frac{\Delta t}{2})$
- $k_4 = f(y_n + \Delta t \cdot k_3, t_n + \Delta t)$

## 不動點與穩定性

### 不動點 (Fixed Point)
滿足 $f(y) = 0$ 的點 $y^*$。

牛頓法迭代：
$$y_{n+1} = y_n - \frac{f(y_n)}{f'(y_n)}$$

### 線性穩定性分析

對系統 $\dot{y} = f(y)$，在定點 $y^*$ 處線性化：
$$\dot{\delta} = J_f(y^*) \delta$$

其中 $J_f$ 為雅可比矩陣。穩定性由 $J_f(y^*)$ 的特徵值決定：
- 所有 $\text{Re}(\lambda_i) < 0$：穩定（吸引）
- 任何 $\text{Re}(\lambda_i) > 0$：不穩定（排斥）
- 有零特徵值：臨界情況

## 李雅普諾夫指數 (Lyapunov Exponent)

衡量相空間中鄰近軌跡的指數發散/收斂速率：
$$\lambda = \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^{n} \ln \frac{|\delta_i|}{dt}$$

- $\lambda < 0$：軌跡收斂（穩定）
- $\lambda > 0$：軌跡發散（混沌/不穩定）
- $\lambda = 0$：臨界情況

## Lorenz 系統

$$\begin{cases} \dot{x} = \sigma(y - x) \\ \dot{y} = x(\rho - z) - y \\ \dot{z} = xy - \beta z \end{cases}$$

典型參數：$\sigma = 10, \rho = 28, \beta = 8/3$

當 $\rho > 1$ 時系統展現混沌行為，存在奇怪吸引子。

## 邏輯斯蒂映射 (Logistic Map)

$$x_{n+1} = r x_n (1 - x_n)$$

- $0 < r < 1$：收斂到 0
- $1 < r < 3$：收斂到固定點 $\frac{r-1}{r}$
- $3 < r < 3.57$：週期倍增，出現分岔
- $r > 3.57$：混沌

## 分岔圖 (Bifurcation Diagram)

展示系統行為隨參數變化而突然變化的現象，横軸為參數 $r$，縱軸為長時間行為的取值。

# 實作細節

## RK4
```python
def runge_kutta_4(f, y0, t):
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        dt = t[i] - t[i - 1]
        k1 = f(y[i-1], t[i-1])
        k2 = f(y[i-1] + dt*k1/2, t[i-1] + dt/2)
        k3 = f(y[i-1] + dt*k2/2, t[i-1] + dt/2)
        k4 = f(y[i-1] + dt*k3, t[i-1] + dt)
        y[i] = y[i-1] + dt/6*(k1 + 2*k2 + 2*k3 + k4)
    return y
```

## 不動點分析
```python
def fixed_point_analysis(f, y0, tol=1e-6, max_iter=10000):
    y = y0.copy()
    for _ in range(max_iter):
        fy = f(y, 0.0)
        if np.linalg.norm(fy) < tol:
            return y
        # 牛頓法迭代
        y = y - fy / df
    return y
```

## 邏輯斯蒂映射
```python
def logistic_map(r, x0, n=1000):
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i-1] * (1 - x[i-1])
    return x
```

## 分岔圖
```python
def bifurcation_diagram(r_range, n_r=100, n_transient=100, n_plot=100):
    r_vals = np.linspace(r_range[0], r_range[1], n_r)
    bifurcation_data = []
    for r in r_vals:
        x = 0.5
        for _ in range(n_transient):
            x = r * x * (1 - x)
        for _ in range(n_plot):
            x = r * x * (1 - x)
            bifurcation_data.append((r, x))
    return r_points, x_points
```

# 使用方式

```python
from math4py.dynamical_systems.function import (
    runge_kutta_4, phase_space_trajectory, fixed_point_analysis,
    linear_stability_analysis, lyapunov_exponent,
    lorenz_system, logistic_map, bifurcation_diagram
)
import numpy as np

# 解微分方程
f = lambda y, t: np.array([-y[1], y[0]])
y0 = np.array([1.0, 0.0])
t = np.linspace(0, 10, 1000)
sol = runge_kutta_4(f, y0, t)

# 相空間軌跡
t, y = phase_space_trajectory(f, y0, (0, 10), n_steps=1000)

# 穩定性分析
A = np.array([[-1, 0], [0, -2]])
eigvals = linear_stability_analysis(A)  # 穩定

# Lorenz 系統
y0 = np.array([1.0, 1.0, 1.0])
t, sol = phase_space_trajectory(lorenz_system, y0, (0, 50))

# 邏輯斯蒂映射
x = logistic_map(r=3.9, x0=0.5, n=1000)

# 分岔圖
r_pts, x_pts = bifurcation_diagram((2.5, 4.0), n_r=100)
```