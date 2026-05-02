# 凝聚態物理 (Condensed Matter Physics)

## 概述

凝聚態物理模組提供固態物理基礎計算函數，包括能隙與波長轉換、費米能、態密度、德魯德電導率、倫敦穿透深度、霍爾電阻、布洛赫波函數、晶體結構因子等。

## 數學原理

### 1. 能隙與波長轉換
$$\lambda = \frac{hc}{E_g}$$

將半導體能隙轉換為對應波長。

### 2. 費米能
$$E_F = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$

- $n$: 電子濃度

### 3. 3D 態密度
$$g(E) = \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E}$$

單位能量間隔的量子態數目。

### 4. 德魯德電導率
$$\sigma = \frac{n e^2 \tau}{m}$$

描述金屬中電子的傳導。

### 5. 倫敦穿透深度
$$\lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}$$

超導體中磁場衰減的特徵長度。

### 6. 庫珀對相干長度
$$\xi = \frac{\hbar v_F}{\pi \Delta}$$

### 7. 霍爾電阻
$$R_H = \frac{B}{n e t}$$

### 8. 布洛赫波函數
$$\psi_k(\vec{r}) = e^{i\vec{k}\cdot\vec{r}} u_k(\vec{r})$$

固體中電子波函數的一般形式。

### 9. 晶體結構因子
$$S_{hkl} = \sum_j f_j e^{-2\pi i(hx_j + ky_j + lz_j)}$$

X射線繞射強度取決於此因子。

### 10. 邁斯納效應
$$B(x) = B_0 e^{-x/\lambda_L}$$

磁場在超導體內的指數衰減。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `band_gap_to_wavelength()` | 能隙(J) -> 波長 |
| `band_gap_ev_to_wavelength()` | 能隙(eV) -> 波長 |
| `fermi_energy()` | 計算費米能 |
| `density_of_states_3d()` | 計算3D態密度 |
| `drude_conductivity()` | 計算德魯德電導率 |
| `london_penetration_depth()` | 計算倫敦穿透深度 |
| `cooper_pair_size()` | 計算庫珀對大小 |
| `hall_resistance()` | 計算霍爾電阻 |
| `bloch_theorem_wavefunction()` | 計算布洛赫波函數 |
| `crystal_structure_factor()` | 計算晶體結構因子 |
| `meissner_effect_penetration()` | 計算磁場衰減 |

## 使用方式

```python
from math4py.physics.condensed_matter import *
import numpy as np

# 能隙->波長（矽的能隙約 1.1 eV）
lam = band_gap_ev_to_wavelength(1.1)

# 費米能（電子濃度 10^28 m^-3）
Ef = fermi_energy(n=1e28)

# 態密度
E = np.linspace(0, 10e-19, 100)
gE = density_of_states_3d(E)

# 德魯德電導率
sigma = drude_conductivity(tau=1e-14, n=1e28)

# 霍爾電阻
Rh = hall_resistance(B=1, n=1e28, t=1e-3)

# 布洛赫波
x = np.linspace(0, 10e-10, 100)
psi = bloch_theorem_wavefunction(k=1e10, x=x)
```