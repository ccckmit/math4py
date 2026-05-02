# 聲學 (Acoustics)

## 概述

聲學模組提供基礎聲學計算函數，包括聲速、多普勒效應、聲強、分貝、拍頻等。

## 數學原理

### 1. 聲速
$$c = \sqrt{\frac{\gamma RT}{M}}$$

- $\gamma$: 絕熱指數（空氣約 1.4）
- $R = 8.314462618$ J/(mol·K): 氣體常數
- $T$: 絕對溫度 (K)
- $M$: 莫爾質量 (kg/mol)

### 2. 多普勒效應
$$f' = f_0 \frac{c + v_o}{c - v_s}$$

- $f_0$: 原始頻率
- $v_o$: 觀察者速度（面向聲源為正）
- $v_s$: 聲源速度（遠離觀察者為正）

### 3. 聲強
$$I = \frac{P^2}{\rho c}$$

- $P$: 聲壓振幅
- $\rho$: 介質密度
- $c$: 聲速

### 4. 分貝等級
$$L = 10 \log_{10}\left(\frac{I}{I_0}\right)$$

或聲壓級 $L_p = 20 \log_{10}(p/p_0)$
- $I_0 = 10^{-12}$ W/m²: 參考強度
- $p_0 = 20$ μPa: 參考聲壓

### 5. 聲波波長
$$\lambda = \frac{c}{f}$$

### 6. 開管共振頻率
$$f_n = \frac{n c}{2L}, \quad n = 1, 2, 3, \ldots$$

### 7. 拍頻
$$f_{beat} = |f_1 - f_2|$$

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `sound_speed()` | 計算聲速 |
| `doppler_shift()` | 計算多普勒效應頻率 |
| `sound_intensity()` | 計算聲強 |
| `decibel_level()` | 計算分貝等級 |
| `sound_wavelength()` | 計算波長 |
| `resonant_frequency()` | 計算共振頻率 |
| `beat_frequency()` | 計算拍頻 |
| `sound_pressure_level()` | 計算聲壓級 |

### 物理常數
- 空氣中聲速 $c = 343$ m/s（20°C）
- 標準大氣壓 $P_0 = 101325$ Pa

## 使用方式

```python
from math4py.physics.acoustics import *

# 聲速
c = sound_speed(gamma=1.4, M=0.02897, T=293.15)

# 多普勒效應
f_prime = doppler_shift(f0=440, v_observer=10, v_source=0)

# 分貝
dB = decibel_level(I=1e-6)

# 開管共振
f1 = resonant_frequency(L=0.5, n=1)  # 基頻
f2 = resonant_frequency(L=0.5, n=2)  # 第二諧波

# 拍頻
f_beat = beat_frequency(256, 260)
```