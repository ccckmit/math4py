# 概述

微分方程數值解法模組，提供常微分方程（ODE）與偏微分方程（PDE）的數值解法，包括歐拉法、龍格-庫塔法以及熱傳導方程和波動方程的有限差分法。

# 數學原理

## 常微分方程 (ODE) 數值解法

### 歐拉法 (Euler Method)
$$y_{n+1} = y_n + dt \cdot f(t_n, y_n)$$

局部截斷誤差為 $O(dt^2)$，為一階方法。

### 二階龍格-庫塔法 (RK2 / Midpoint Method)
$$k_1 = f(t_n, y_n)$$
$$k_2 = f(t_n + \frac{dt}{2}, y_n + \frac{dt}{2} k_1)$$
$$y_{n+1} = y_n + dt \cdot k_2$$

局部截斷誤差為 $O(dt^3)$。

### 四階龍格-庫塔法 (RK4)
$$k_1 = f(t_n, y_n)$$
$$k_2 = f(t_n + \frac{dt}{2}, y_n + \frac{dt}{2} k_1)$$
$$k_3 = f(t_n + \frac{dt}{2}, y_n + \frac{dt}{2} k_2)$$
$$k_4 = f(t_n + dt, y_n + dt \cdot k_3)$$
$$y_{n+1} = y_n + \frac{dt}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

局部截斷誤差為 $O(dt^5)$。

## 偏微分方程 (PDE) 數值解法

### 熱傳導方程 (Heat Equation)
$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

顯式有限差分：
$$u_i^{n+1} = u_i^n + r(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$$

其中 $r = \frac{\alpha \Delta t}{\Delta x^2}$

穩定條件：$r \leq \frac{1}{2}$

### 波動方程 (Wave Equation)
$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$

顯式有限差分：
$$u_i^{n+1} = 2u_i^n - u_i^{n-1} + r(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$$

其中 $r = (\frac{c \Delta t}{\Delta x})^2$

穩定條件：$r \leq 1$

## 線性系統穩定性

對線性系統 $\frac{dy}{dt} = Ay$，穩定條件為：
$$\text{Re}(\lambda_i(A)) < 0 \quad \forall i$$

## 李雅普諾夫指數 (Lyapunov Exponent)

混沌系統中，軌跡的指數發散速率：
$$\lambda = \lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^{n} \ln \frac{|\delta_i|}{dt}$$

# 實作細節

## RK4 方法
```python
def rk4_method(f, y0, t0, tf, dt=0.01):
    n_steps = int((tf - t0) / dt)
    t_arr = np.linspace(t0, tf, n_steps + 1)
    y_arr = np.zeros((n_steps + 1, len(y0)))
    y_arr[0] = y0
    for i in range(n_steps):
        k1 = f(t_arr[i], y_arr[i])
        k2 = f(t_arr[i] + dt/2, y_arr[i] + dt/2*k1)
        k3 = f(t_arr[i] + dt/2, y_arr[i] + dt/2*k2)
        k4 = f(t_arr[i] + dt, y_arr[i] + dt*k3)
        y_arr[i+1] = y_arr[i] + dt/6*(k1 + 2*k2 + 2*k3 + k4)
    return t_arr, y_arr
```

## 熱傳導方程
```python
def heat_equation_explicit(L=1.0, T=1.0, nx=50, nt=100, alpha=0.01):
    dx = L / (nx - 1)
    dt = T / nt
    r = alpha * dt / (dx**2)
    # u[n+1, i] = u[n, i] + r * (u[n, i+1] - 2*u[n, i] + u[n, i-1])
```

## 穩定性分析
```python
def stability_matrix(A):
    eigvals = np.linalg.eigvals(A)
    is_stable = np.all(np.real(eigvals) < 0)
    return eigvals, is_stable
```

# 使用方式

```python
from math4py.differential_equation.function import (
    euler_method, rk4_method, solve_ivp,
    heat_equation_explicit, wave_equation_explicit,
    stability_matrix, lyapunov_exponent
)
import numpy as np

# 解 ODE: dy/dt = -y
f = lambda t, y: -y
y0 = np.array([1.0])
t, y = rk4_method(f, y0, 0, 5, dt=0.01)

# 統一介面
t, y = solve_ivp(f, y0, (0, 5), method="rk4", dt=0.01)

# 熱傳導方程
x, t_grid, u = heat_equation_explicit(L=1.0, T=1.0, alpha=0.01)

# 穩定性分析
A = np.array([[-1, 0], [0, -2]])
eigvals, is_stable = stability_matrix(A)
```

# 穩定性條件

| 方法 | 穩定性條件 |
|------|-----------|
| 歐拉法（熱方程）| $r \leq 0.5$ |
| 歐拉法（波動方程）| $r \leq 1$ |
| RK4 | 無條件穩定（線性問題）|