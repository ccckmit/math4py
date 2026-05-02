# 量子力學 (Quantum Mechanics)

## 概述

量子力學模組提供量子力學基礎計算函數，包括普朗克常數、德布羅意波長、量子穿隧、薛丁格方程、氫原子波函數等核心量子力學公式。

## 數學原理

### 1. 普朗克關係
$$E = hf = \hbar \omega$$

- $h = 6.62607015 \times 10^{-34}$ J·s: 普朗克常數
- $\hbar = h/(2\pi)$: 約化普朗克常數

### 2. 德布羅意波長
$$\lambda = \frac{h}{p}$$

描述粒子的波粒二象性。

### 3. 自由粒子波函數
$$\psi(x,t) = A \cdot e^{i(kx - \omega t)}$$

其中 $\omega = E/\hbar = \hbar k^2/(2m)$（非相對論）。

### 4. 概率密度
$$P(x) = |\psi(x)|^2$$

波函數的 Born 解釋。

### 5. 海森堡不確定性原理
$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

位置與動量的測量不確定性下限。

### 6. 含時薛丁格方程
$$i\hbar \frac{\partial \psi}{\partial t} = H\psi = \left(-\frac{\hbar^2}{2m}\nabla^2 + V\right)\psi$$

### 7. 一維無限深方阱
$$\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right), \quad 0 < x < L$$

$$E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}$$

### 8. 量子穿隧
$$T \approx \exp\left(-2a\sqrt{\frac{2m(V_0-E)}{\hbar^2}}\right)$$

穿越方勢壘的機率。

### 9. 泡利矩陣
$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `de_broglie_wavelength()` | 計算粒子的德布羅意波長 |
| `energy_photon()` | 計算光子能量 |
| `wave_function_free_particle()` | 計算自由粒子波函數 |
| `probability_density()` | 計算概率密度 |
| `uncertainty_position()` | 計算位置不確定性 Δx |
| `uncertainty_momentum()` | 計算動量不確定性 Δp |
| `heisenberg_uncertainty_check()` | 驗證不確定性原理 |
| `schrodinger_equation_time_dependent()` | 數值求解含時薛丁格方程 |
| `particle_in_box_wave_function()` | 無限深方阱波函數 |
| `energy_levels_particle_in_box()` | 能級計算 |
| `tunneling_probability()` | 量子穿隧機率 |
| `pauli_matrices()` | 返回泡利矩陣 |

## 使用方式

```python
from math4py.physics.quantum import *
import numpy as np

# 德布羅意波長
lam = de_broglie_wavelength(p=1e-24)

# 計算波函數
x = np.linspace(0, 10, 100)
psi = wave_function_free_particle(x, k=1.0, t=0.0)

# 概率密度
prob = probability_density(psi)

# 不確定性原理驗證
satisfied, product = heisenberg_uncertainty_check(delta_x=0.5, delta_p=1e-34)

# 無限深方阱
psi_n = particle_in_box_wave_function(n=1, L=10, x=x)
E = energy_levels_particle_in_box(n=1, L=1e-9, m=9.11e-31)

# 量子穿隧
T = tunneling_probability(V0=1e-19, E=5e-20, a=1e-10)
```