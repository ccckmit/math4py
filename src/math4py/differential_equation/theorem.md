# 概述

微分方程定理驗證模組，驗證數值解法的收斂性、精度以及微分方程理論性質，包括歐拉法收斂階、RK4精度、熱方程衰減率、波動方程能量守恆等。

# 數學原理

## 數值方法收斂性

### 歐拉法收斂階
歐拉法為一階方法，誤差不超過 $C \cdot dt$：
$$|y_{numerical} - y_{exact}| \leq C \cdot dt$$

當步長減半時，誤差約減半。

### RK4 vs 歐拉法
RK4為四階方法，誤差為 $O(dt^5)$，遠比歐拉法精確。

## 熱傳導方程解的衰減

對熱傳導方程 $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$ with $u(0,t)=u(L,t)=0$：

初始條件 $u(x,0) = \sin(\pi x)$ 的解為：
$$u(x,t) = e^{-\alpha \pi^2 t} \sin(\pi x)$$

因此振幅以速率 $e^{-\alpha \pi^2 t}$ 指數衰減，衰減常數為 $\lambda = \alpha \pi^2$。

## 波動方程能量守恆

波動方程 $\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$ 的能量：
$$E = \int \left( u_t^2 + c^2 u_x^2 \right) dx$$

對於精確解，能量應保持常數。離散化後數值方法應保持能量近常數。

## 離散穩定性條件

### 熱方程
$$r = \frac{\alpha \Delta t}{\Delta x^2} \leq \frac{1}{2}$$

### 波動方程
$$r = \left(\frac{c \Delta t}{\Delta x}\right)^2 \leq 1$$

## 李雅普諾夫指數與穩定性

- 穩定固定點：李雅普諾夫指數 $< 0$
- 不穩定軌跡：李雅普諾夫指數 $> 0$

# 實作細節

## 歐拉法收斂階驗證
```python
def euler_convergence_order(f, y0, t_span):
    dts = [0.01, 0.005, 0.0025]
    errors = []
    for dt in dts:
        t, y = euler_method(f, y0, t_span[0], t_span[1], dt)
        exact = np.exp(-t[-1])
        errors.append(abs(y[-1, 0] - exact))
    # 收斂階 = log(e1/e2) / log(dt1/dt2)
    order = np.log(errors[0]/errors[1]) / np.log(dts[0]/dts[1])
    return order  # 應接近 1
```

## RK4 精度驗證
```python
def rk4_superior_to_euler(f, y0, t_span, dt=0.01):
    t_eu, y_eu = euler_method(f, y0, t_span[0], t_span[1], dt)
    t_rk, y_rk = rk4_method(f, y0, t_span[0], t_span[1], dt)
    err_eu = abs(y_eu[-1, 0] - np.exp(-t_eu[-1]))
    err_rk = abs(y_rk[-1, 0] - np.exp(-t_eu[-1]))
    return err_rk < err_eu
```

## 熱方程衰減率
```python
def heat_equation_decay_rate(alpha=0.01):
    x, t, u = heat_equation_explicit(L=1.0, T=1.0, alpha=alpha, nt=200)
    max_amplitudes = np.max(np.abs(u), axis=1)
    log_amplitudes = np.log(max_amplitudes + 1e-12)
    coeffs = np.polyfit(t, log_amplitudes, 1)
    return -coeffs[0]  # 應接近 alpha * pi^2
```

## 波動方程能量守恆
```python
def wave_equation_energy_conservation(c=1.0):
    x, t, u = wave_equation_explicit(L=1.0, T=0.5, c=c, nx=100, nt=200)
    energies = []
    for n in range(1, len(t) - 1):
        ut = (u[n+1] - u[n-1]) / (2*dt)
        ux = (u[n, 1:] - u[n, :-1]) / dx
        E = np.sum(ut**2) + c**2 * np.sum(ux**2)
        energies.append(E)
    return np.std(energies) / np.mean(energies)  # 應接近 0
```

## 李雅普諾夫指數驗證
```python
def lyapunov_negative_stable_fixed_point():
    t = np.linspace(0, 5, 200)
    traj = np.array([[np.exp(-t_i), 0.0] for t_i in t])
    lyap = lyapunov_exponent(traj, dt=0.025)
    return lyap < 0

def lyapunov_positive_unstable_spiral():
    t = np.linspace(0, 3, 300)
    traj = np.array([[np.exp(t_i)*np.cos(t_i), np.exp(t_i)*np.sin(t_i)] for t_i in t])
    lyap = lyapunov_exponent(traj, dt=0.01)
    return lyap > 0
```

# 使用方式

```python
from math4py.differential_equation.theorem import (
    euler_convergence_order, rk4_superior_to_euler,
    heat_equation_decay_rate, wave_equation_energy_conservation,
    stability_criterion_heat, lyapunov_negative_stable_fixed_point
)

# 驗證歐拉法收斂階
f = lambda t, y: -y
y0 = np.array([1.0])
order = euler_convergence_order(f, y0, (0, 2))
print(order)  # ≈ 1.0

# 驗證 RK4 比歐拉法精確
is_better = rk4_superior_to_euler(f, y0, (0, 2))

# 熱方程衰減率
decay = heat_equation_decay_rate(alpha=0.01)
print(decay)  # ≈ 0.0987 (≈ π² * 0.01)

# 波動方程能量守恆
variation = wave_equation_energy_conservation(c=1.0)
print(variation)  # 應很小
```