# 流體動力學 (Fluid Dynamics)

## 概述

流體動力學模組提供基礎流體力學計算函數，包括連續方程式、白努利方程、雷諾數、阻力、靜水壓力、馬赫數等。

## 數學原理

### 1. 連續方程式
$$\rho_1 A_1 v_1 = \rho_2 A_2 v_2$$

質量守恆在流體中的表現。

### 2. 白努利方程
$$P_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2$$

能量守恆在不可壓縮流體中的表現。

### 3. 雷諾數
$$\text{Re} = \frac{\rho v L}{\mu} = \frac{v L}{\nu}$$

- $\mu$: 動力黏度
- $\nu = \mu/\rho$: 運動黏度
- Re < 2300: 層流
- Re > 4000: 紊流

### 4. 阻力係數
$$F_d = \frac{1}{2} C_d \rho A v^2$$

- $C_d$: 阻力係數（形狀決定）

### 5. 靜水壓力
$$P = \rho g h$$

### 6. 馬赫數
$$\text{Ma} = \frac{v}{c}$$

- Ma < 1: 亞音速
- Ma = 1: 音速
- Ma > 1: 超音速

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `continuity_equation()` | 驗證連續方程式 |
| `bernoulli_equation()` | 驗證白努利方程 |
| `reynolds_number()` | 計算雷諾數 |
| `drag_force()` | 計算阻力 |
| `hydrostatic_pressure()` | 計算靜水壓力 |
| `mach_number()` | 計算馬赫數 |

## 使用方式

```python
from math4py.physics.fluid_dynamics import *

# 連續方程驗證
valid = continuity_equation(rho1=1000, A1=0.1, v1=5, rho2=1000, A2=0.05, v2=10)

# 白努利方程驗證
valid = bernoulli_equation(P1=101325, rho=1.204, v1=0, h1=10, P2=None, v2=None, h2=0)

# 雷諾數
Re = reynolds_number(rho=1000, v=1, L=0.01, mu=1e-3)

# 阻力
Fd = drag_force(Cd=0.47, rho=1.225, A=0.1, v=30)

# 靜水壓力
P = hydrostatic_pressure(rho=1000, g=9.81, h=10)

# 馬赫數
Ma = mach_number(v=340, c=343)
```