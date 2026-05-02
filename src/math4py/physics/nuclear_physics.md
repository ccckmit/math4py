# 核物理 (Nuclear Physics)

## 概述

核物理模組提供核物理基礎計算函數，包括質量虧損與結合能、放射性衰變、半衰期、核反應 Q 值等。

## 數學原理

### 1. 質量虧損
$$\Delta m = Z m_p + N m_n - m_{nucleus}$$

- $Z$: 質子數
- $N$: 中子數
- $A = Z + N$: 質量數

### 2. 結合能
$$E_B = \Delta m \cdot c^2$$

將核子結合成原子核所釋放的能量。

### 3. 放射性衰變定律
$$N(t) = N_0 e^{-\lambda t}$$

- $\lambda$: 衰變常數
- $T_{1/2}$: 半衰期 $= \ln 2 / \lambda$

### 4. 放射性活度
$$A = \lambda N = -\frac{dN}{dt}$$

單位時間的衰變次數。

### 5. 原子核半徑
$$R = R_0 \cdot A^{1/3}$$

- $R_0 \approx 1.2 \times 10^{-15}$ m

### 6. 核反應 Q 值
$$Q = (m_{initial} - m_{final})c^2$$

- $Q > 0$: 放能反應
- $Q < 0$: 吸能反應

### 7. 典型能量釋放
- 核裂變：約 0.9 MeV/核子
- 核聚變：約 6.7 MeV/核子

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `mass_defect()` | 計算質量虧損 |
| `binding_energy()` | 計算結合能 |
| `binding_energy_per_nucleon()` | 計算每核子結合能 |
| `radioactive_decay()` | 計算剩餘原子核數 |
| `decay_constant()` | 由半衰期計算衰變常數 |
| `half_life()` | 由衰變常數計算半衰期 |
| `activity()` | 計算放射性活度 |
| `nuclear_radius()` | 計算原子核半徑 |
| `q_value()` | 計算核反應 Q 值 |
| `fission_energy_per_nucleon()` | 裂變能量回傳 |
| `fusion_energy_per_nucleon()` | 聚變能量回傳 |

### 物理常數
- 原子品質單位 $1$ u $= 1.66053906660 \times 10^{-27}$ kg
- 亞佛加厥數 $N_A = 6.02214076 \times 10^{23}$ mol⁻¹
- 電子伏特 $1$ eV $= 1.602176634 \times 10^{-19}$ J
- 質子質量 $m_p = 1.007276466621$ u
- 中子質量 $m_n = 1.00866491588$ u

## 使用方式

```python
from math4py.physics.nuclear_physics import *
import numpy as np

# 質量虧損（鐵-56 核，假設實測質量精確已知）
dm = mass_defect(Z=26, N=30, A=56, m_nucleus=55.9349 * 1.66054e-27)

# 結合能
Eb = binding_energy(mass_defect=dm)

# 每核子結合能
Eb_A = binding_energy_per_nucleon(binding_energy=Eb, A=56)

# 放射性衰變
t = np.linspace(0, 1000, 100)
N = radioactive_decay(N0=1e6, lambda_=0.001, t=t)

# 半衰期與衰變常數
lambda_ = decay_constant(half_life=5730)  # 碳-14
T12 = half_life(lambda_=lambda_)

# 核半徑（鐵-56）
R = nuclear_radius(A=56)

# Q 值
Q = q_value(reaction_mass_initial=10, reaction_mass_final=9.9)
```