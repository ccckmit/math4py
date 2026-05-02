# 轉換定理驗證 (Transform Theorems)

## 概述

轉換定理驗證模組提供傅立葉、拉普拉斯、小波轉換相關定理的數值驗證。

## 數學原理

### 1. 傅立葉逆轉換定理
$$f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega) e^{i\omega t} d\omega$$

驗證：$\mathcal{F}^{-1}(\mathcal{F}(f)) = f$

### 2. DFT 逆變換
$$\text{IDFT}(\text{DFT}(x)) = x$$

離散版本的可逆性。

### 3. 傅立葉級數收斂性
$$f(t) = a_0 + \sum_{n=1}^{\infty} \left(a_n \cos\frac{2\pi n t}{T} + b_n \sin\frac{2\pi n t}{T}\right)$$

項數越多，近似誤差越小。

### 4. 摺積定理
$$\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}$$

時域摺積等於頻域乘積。

### 5. 小波重建定理
$$\text{IDWT}(\text{DWT}(x)) = x$$

DWT 的可逆性。

### 6. 拉普拉斯轉換對驗證
常見轉換對：
- $u(t) \leftrightarrow \frac{1}{s}$
- $e^{-at} \leftrightarrow \frac{1}{s+a}$
- $\sin(\omega t) \leftrightarrow \frac{\omega}{s^2+\omega^2}$

### 7. 拉普拉斯導數定理
$$\mathcal{L}\{f'(t)\} = s \mathcal{L}\{f(t)\} - f(0)$$

## 實作細節

### 關鍵函數

| 函數 | 驗證內容 |
|------|----------|
| `fourier_inversion_theorem()` | $\mathcal{F}^{-1}(\mathcal{F}(f)) = f$ |
| `dft_idft_theorem()` | IDFT(DFT(x)) = x |
| `fourier_series_convergence()` | 級數收斂性 |
| `convolution_theorem_fourier()` | $\mathcal{F}(f*g) = \mathcal{F}(f) \cdot \mathcal{F}(g)$ |
| `wavelet_reconstruction_theorem()` | IDWT(DWT(x)) = x |
| `multilevel_reconstruction()` | 多層小波重建 |
| `wavelet_denoising_effect()` | 去雜訊效果 |
| `laplace_transform_pairs_verification()` | 轉換對正確性 |
| `laplace_derivative_theorem()` | $\mathcal{L}(f') = s\mathcal{L}(f) - f(0)$ |
| `laplace_ode_solution()` | ODE 求解正確性 |

## 使用方式

```python
from math4py.transform.theorem import *
import numpy as np

# 傅立葉逆轉換定理驗證
signal = np.sin(2*np.pi*5*np.linspace(0, 1, 100))
error = fourier_inversion_theorem(signal, dt=0.01)

# DFT 可逆性
x = np.random.randn(64)
error = dft_idft_theorem(x)

# 摺積定理
x = np.array([1, 2, 3, 4])
h = np.array([0.5, 0.5])
error = convolution_theorem_fourier(x, h)

# 小波重建
signal = np.random.randn(128)
error = wavelet_reconstruction_theorem(signal)

# 拉普拉斯轉換對
errors = laplace_transform_pairs_verification(s=1+1j)
```