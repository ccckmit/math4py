# 轉換模組 (Transform Module)

## 概述

轉換模組是傅立葉、拉普拉斯、小波等積分轉換的統一入口，整合了信號處理與系統分析的核心功能。

## 數學原理

本模組包含三種主要的積分轉換：

### 1. 傅立葉轉換
$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$$

將時域信號轉換為頻域。

### 2. 拉普拉斯轉換
$$F(s) = \int_0^{\infty} f(t) e^{-st} dt$$

推廣傅立葉轉換到複平面，常用於微分方程求解。

### 3. 小波轉換
$$W(a,b) = \frac{1}{\sqrt{a}} \int_{-\infty}^{\infty} f(t) \psi^*\left(\frac{t-b}{a}\right) dt$$

時頻分析，彌補傅立葉轉換缺乏時間解析度的不足。

## 子模組

### fourier.py - 傅立葉分析
- 傅立葉轉換與逆轉換
- 離散傅立葉變換 (DFT/IDFT)
- 功率譜計算
- 傅立葉級數
- 摺積定理

### laplace.py - 拉普拉斯轉換
- 數值拉普拉斯轉換
- 逆拉普拉斯轉換 (Bromwich 積分)
- 轉換對查詢
- 微分性質
- ODE 求解
- 部分分式分解

### wavelet.py - 小波轉換
- Haar 小波
- Daubechies-4 小波
- 離散小波轉換 (DWT/IDWT)
- 多層分解
- 小波去雜訊
- 連續小波轉換 (CWT)

## 使用方式

```python
from math4py.transform.function import *

# 傅立葉轉換
freqs, spectrum = fourier_transform(signal, dt=0.01)
t, recovered = inverse_fourier_transform(spectrum, dt=0.01)

# 功率譜
freqs, power = power_spectrum(signal, dt=0.01)

# 離散傅立葉變換
X = dft(x)
x_recon = idft(X)

# 摺積
y = convolution_fft(x, h)

# 拉普拉斯轉換
F = laplace_transform(f, s=1+1j)

# 小波轉換
approx, detail = dwt(signal)
recovered = idwt(approx, detail)

# 多層小波
coeffs = multilevel_dwt(signal, levels=3)
```