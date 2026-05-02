# 傅立葉轉換 (Fourier Transform)

## 概述

傅立葉轉換模組提供傅立葉分析的核心函數，包括連續傅立葉轉換、離散傅立葉變換 (DFT/IDFT)、功率譜、傅立葉級數、摺積計算、加窗傅立葉轉換等。

## 數學原理

### 1. 連續傅立葉轉換
$$F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$$

### 2. 逆傅立葉轉換
$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega$$

### 3. 離散傅立葉變換 (DFT)
$$X[k] = \sum_{n=0}^{N-1} x[n] e^{-2\pi i kn/N}$$

### 4. 逆離散傅立葉變換 (IDFT)
$$x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] e^{2\pi i kn/N}$$

### 5. 功率譜
$$P(\omega) = |F(\omega)|^2$$

信號功率在頻率上的分布。

### 6. 傅立葉級數係數
$$a_n = \frac{2}{T}\int_0^T f(t)\cos\frac{2\pi n t}{T} dt$$
$$b_n = \frac{2}{T}\int_0^T f(t)\sin\frac{2\pi n t}{T} dt$$

### 7. 摺積定理
$$\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$$

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `fourier_transform()` | 數值傅立葉轉換 |
| `inverse_fourier_transform()` | 逆傅立葉轉換 |
| `power_spectrum()` | 功率譜計算 |
| `fourier_series_coeff()` | 傅立葉級數係數 |
| `reconstruct_fourier_series()` | 由係數重建信號 |
| `dft()` | 離散傅立葉變換（直接計算） |
| `idft()` | 逆離散傅立葉變換 |
| `convolution_fft()` | FFT 摺積 |
| `windowed_ft()` | 加窗傅立葉轉換 |

### 頻率軸計算
```python
freqs = fft.fftfreq(n, d=dt)  # n 為樣本數，dt 為採樣間隔
```

### DFT 矩陣形式
$$X = M \cdot x, \quad M_{kn} = e^{-2\pi i kn/N}$$

## 使用方式

```python
from math4py.transform.fourier import *
import numpy as np

# 傅立葉轉換
t = np.linspace(0, 1, 256, endpoint=False)
signal = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*25*t)
freqs, spectrum = fourier_transform(signal, dt=1/256)

# 功率譜
freqs, power = power_spectrum(signal, dt=1/256)

# 傅立葉級數
f = lambda t: np.where((t % 1) < 0.5, 1, -1)  # 方波
a0, an, bn = fourier_series_coeff(f, T=1.0, n_terms=20)
reconstructed = reconstruct_fourier_series(a0, an, bn, T=1.0, t=t)

# DFT（教學用直接計算）
X = dft(signal)
x_recon = idft(X)

# FFT 摺積
x = np.array([1, 2, 3, 4])
h = np.array([0.5, 0.5])
y = convolution_fft(x, h)

# 加窗傅立葉
freqs, spectrum = windowed_ft(signal, window="hann", dt=1/256)
```