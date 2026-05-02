# 粒子物理 (Particle Physics)

## 概述

粒子物理模組提供粒子物理基礎計算函數，包括不變質量、衰變寬度與壽命、分支比、CKM 矩陣等。

## 數學原理

### 1. 不變質量（勞侖茲不變量）
$$m^2 c^4 = (E_{total})^2 - (p_{total} c)^2$$

由一組粒子的總能量與總動量計算其不變質量。

### 2. 衰變寬度與壽命
$$\tau = \frac{\hbar}{\Gamma}$$

- $\tau$: 平均壽命
- $\Gamma$: 總衰變寬度
- $\hbar = 6.582119569 \times 10^{-22}$ MeV·s

### 3. 分支比
$$BR_i = \frac{\Gamma_i}{\Gamma_{total}}$$

特定衰變道佔總衰變的比例。

### 4. 相對論動能
$$T = \sqrt{p^2c^2 + m_0^2c^4} - m_0c^2$$

### 5. 散射截面（點粒子近似）
$$\sigma \sim \frac{1}{s}$$

高能散射的簡化行為。

### 6. CKM 矩陣
$$V_{CKM} = \begin{pmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{pmatrix}$$

描述夸克混合的么正矩陣。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `lorentz_invariant_mass()` | 計算不變質量 |
| `decay_width_to_lifetime()` | 寬度 -> 壽命 |
| `branching_ratio()` | 計算分支比 |
| `center_of_mass_energy()` | 質心能量 |
| `relativistic_kinetic_energy()` | 相對論動能 |
| `cross_section_point_like()` | 點粒子截面近似 |
| `ckms_matrix_element()` | 計算 CKM 矩陣元素 |
| `particle_composition()` | 查詢粒子組成 |

### 基本粒子質量
- 電子：0.511 MeV/c²
- 緲子：105.7 MeV/c²
- τ 粒子：1776.86 MeV/c²
- 上夸克：2.2 MeV/c²
- 下夸克：4.7 MeV/c²
- 奇夸克：96.0 MeV/c²

## 使用方式

```python
from math4py.physics.particle_physics import *

# 不變質量（兩個光子的能量動量）
particles = [
    {"E": 100, "px": 50, "py": 0, "pz": 0},
    {"E": 100, "px": -50, "py": 0, "pz": 0}
]
m = lorentz_invariant_mass(particles)

# 衰變寬度 -> 壽命
tau = decay_width_to_lifetime(Gamma=1e12)  # eV

# 分支比
BR = branching_ratio(width_partial=0.3, width_total=1.0)

# CKM 矩陣
V = ckms_matrix_element(V_us=0.22, V_ub=0.003, V_cb=0.04, V_ud=0.974)

# 粒子組成
composition = particle_composition("proton")  # ["u", "u", "d"]
```