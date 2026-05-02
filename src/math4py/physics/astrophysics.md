# 天體物理 (Astrophysics)

## 概述

天體物理模組提供宇宙學與天體物理基礎計算函數，包括史瓦西半徑、軌道速度、逃逸速度、哈勃定律、恆星光度、紅移、克卜勒定律、金斯質量等。

## 數學原理

### 1. 史瓦西半徑
$$R_s = \frac{2GM}{c^2}$$

黑洞的特徵半徑。

### 2. 軌道速度
$$v = \sqrt{\frac{GM}{r}}$$

圓形軌道的切向速度。

### 3. 逃逸速度
$$v_{esc} = \sqrt{\frac{2GM}{r}}$$

擺脫天體引力的最小速度。

### 4. 哈勃定律
$$v = H_0 \cdot d$$

- $H_0 \approx 70$ km/s/Mpc: 哈勃常數

### 5. 恆星光度
$$L = 4\pi R^2 \sigma T^4$$

- $\sigma = 5.670374419 \times 10^{-8}$ W/(m²·K⁴)

### 6. 宇宙學紅移
$$z = \frac{H_0 d}{c}$$

（近距離近似）

### 7. 克卜勒第三定律
$$P^2 = \frac{4\pi^2 a^3}{GM}$$

行星軌道週期與半長軸的關係。

### 8. 主序星壽命
$$t \propto M^{-2.5}$$

質量越大，壽命越短。

### 9. 金斯質量
$$M_J = \frac{\pi}{6}\left(\frac{\pi kT}{G\mu\rho}\right)^{3/2}\rho^{-1/2}$$

星雲塌縮形成星球的臨界質量。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `schwarzschild_radius()` | 計算史瓦西半徑 |
| `orbital_velocity()` | 計算軌道速度 |
| `escape_velocity()` | 計算逃逸速度 |
| `hubble_law()` | 哈勃定律（速度/距離互算） |
| `stefan_boltzmann_luminosity()` | 計算恆星光度 |
| `cosmological_redshift()` | 計算紅移參數 |
| `kepler_third_law()` | 克卜勒第三定律 |
| `tov_near_parsec()` | 托爾曼-歐本彩距離修正 |
| `main_sequence_lifetime()` | 估算主序星壽命 |
| `jeans_mass()` | 計算金斯質量 |

### 物理常數
- 重力常數 $G = 6.67430 \times 10^{-11}$ m³ kg⁻¹ s⁻²
- 太陽質量 $M_\odot = 1.9885 \times 10^{30}$ kg
- 太陽半徑 $R_\odot = 6.957 \times 10^8$ m
- 太陽光度 $L_\odot = 3.828 \times 10^{26}$ W
- 秒差距 $1$ pc $= 3.085677581 \times 10^{16}$ m

## 使用方式

```python
from math4py.physics.astrophysics import *

# 史瓦西半徑（太陽質量黑洞）
Rs = schwarzschild_radius(M=1.9885e30)

# 地球軌道速度
v = orbital_velocity(M=5.972e24, r=1.496e11)

# 逃逸速度（地球表面）
v_esc = escape_velocity(M=5.972e24, r=6.371e6)

# 哈勃定律
result = hubble_law(d=100)  # 100 Mpc 處的速度

# 恆星光度（太陽）
L = stefan_boltzmann_luminosity(R=6.957e8, T=5778)

# 主序星壽命（太陽質量）
t = main_sequence_lifetime(M=1.9885e30)

# 金斯質量
Mj = jeans_mass(T=100, rho=1e-20, mu=1.67e-27)
```