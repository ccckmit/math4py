# 熱力學 (Thermodynamics)

## 概述

熱力學模組提供熱力學基礎計算函數，包括理想氣體狀態方程、熱力學定律、熵計算、卡諾效率等核心熱力學公式。

## 數學原理

### 1. 理想氣體狀態方程
$$PV = nRT$$

- $P$: 壓力 (Pa)
- $V$: 體積 (m³)
- $n$: 莫爾數
- $R = 8.314462618$ J/(mol·K): 氣體常數
- $T$: 溫度 (K)

### 2. 熱力學第一定律
$$\Delta U = Q - W$$

- $\Delta U$: 內能變化
- $Q$: 吸熱（正為吸熱）
- $W$: 對外做功（正為對外做功）

### 3. 卡諾熱機效率
$$\eta = 1 - \frac{T_c}{T_h}$$

理論最大效率，取決於高低溫源的絕對溫度比。

### 4. 熵變
$$\Delta S = \frac{Q_{rev}}{T}$$

可逆過程的熵變化。

### 5. 斯特藩-玻爾茲曼定律
$$P = \varepsilon \sigma A T^4$$

- $\sigma = 5.670374419 \times 10^{-8}$ W/(m²·K⁴)
- $\varepsilon$: 發射率

### 6. 絕熱過程
$$TV^{\gamma-1} = \text{常數}$$

理想氣體的絕熱過程，$\gamma = C_p/C_v$。

### 7. 吉布斯與亥姆霍茲自由能
$$G = H - TS$$
$$F = U - TS$$

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `ideal_gas_law()` | 根據任意兩個已知變數計算第三或第四個變數 |
| `first_law()` | 計算熱力學第一定律中的任一未知量 |
| `carnot_efficiency()` | 計算卡諾熱機效率 |
| `entropy_change()` | 計算可逆過程的熵變 |
| `stefan_boltzmann_law()` | 計算黑體輻射功率 |

### 物理常數
- 波茲曼常數 $k_B = 1.380649 \times 10^{-23}$ J/K
- 氣體常數 $R = 8.314462618$ J/(mol·K)
- 斯特藩-玻爾茲曼常數 $\sigma = 5.670374419 \times 10^{-8}$ W/(m²·K⁴)

## 使用方式

```python
from math4py.physics.thermodynamics import *

# 理想氣體定律
result = ideal_gas_law(P=101325, V=0.0224, n=1, T=None)  # 計算 T
print(result)  # {'T': 273.15}

# 熱力學第一定律
result = first_law(Q=1000, delta_U=600, W=None)  # 計算 W
print(result)  # {'W': 400}

# 卡諾效率
eta = carnot_efficiency(T_hot=600, T_cold=300)
print(eta)  # 0.5

# 斯特藩-玻爾茲曼定律
power = stefan_boltzmann_law(T=1000, epsilon=1.0, A=1.0)
```