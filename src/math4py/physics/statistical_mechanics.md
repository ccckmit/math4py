# 統計力學 (Statistical Mechanics)

## 概述

統計力學模組提供統計力學基礎計算函數，包括玻爾茲曼分布、配分函數、費米-狄拉克分布、玻色-愛因斯坦分布、麥克斯韋-玻爾茲曼速率分布等。

## 數學原理

### 1. 玻爾茲曼分布
$$P(E) \propto e^{-E/kT}$$

描述系統在能量 E 的機率分布。

### 2. 配分函數
$$Z = \sum_i e^{-E_i/kT}$$

連接微觀與巨觀性質的核心函數。

### 3. 平均能量
$$\langle E \rangle = \frac{\sum_i E_i e^{-E_i/kT}}{Z} = \frac{1}{Z}\sum_i E_i e^{-E_i/kT}$$

### 4. 統計熵
$$S = -k \sum_i p_i \ln(p_i)$$

或 $S = k \ln W$，其中 W 為微觀狀態數。

### 5. 費米-狄拉克分布
$$f(E) = \frac{1}{e^{(E-E_F)/kT} + 1}$$

描述費米子的分布（電子等）。

### 6. 玻色-愛因斯坦分布
$$n(E) = \frac{1}{e^{(E-\mu)/kT} - 1}$$

描述玻色子的分布（光子、聲子等）。

### 7. 麥克斯韋-玻爾茲曼速率分布
$$f(v) = 4\pi \left(\frac{m}{2\pi kT}\right)^{3/2} v^2 e^{-mv^2/2kT}$$

### 8. 化學勢（理想氣體）
$$\mu = kT \ln(n\lambda^3)$$

其中 $\lambda = \sqrt{\frac{2\pi\hbar^2}{mkT}}$ 為熱波長。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `boltzmann_distribution()` | 計算玻爾茲曼因子 |
| `partition_function()` | 計算配分函數 |
| `average_energy()` | 計算平均能量 |
| `entropy_statistical()` | 計算統計熵 |
| `fermi_dirac_distribution()` | 計算費米-狄拉克分布 |
| `bose_einstein_distribution()` | 計算玻色-愛因斯坦分布 |
| `maxwell_boltzmann_speed()` | 計算速率分布 |
| `chemical_potential_ideal_gas()` | 計算理想氣體化學勢 |

### 物理常數
- 波茲曼常數 $k_B = 1.380649 \times 10^{-23}$ J/K

## 使用方式

```python
from math4py.physics.statistical_mechanics import *
import numpy as np

# 配分函數
energies = np.array([0, 1e-21, 2e-21, 3e-21])  # Joules
Z = partition_function(energies, T=300)

# 平均能量
E_avg = average_energy(energies, T=300)

# 熵
S = entropy_statistical(energies, T=300)

# 費米-狄拉克分布
E = np.linspace(0, 10e-21, 100)
f = fermi_dirac_distribution(E, E_F=5e-21, T=300)

# 麥克斯韋-玻爾茲曼分布
v = np.linspace(0, 1000, 100)
f_v = maxwell_boltzmann_speed(v, m=28e-3, T=300)  # 氮氣分子
```