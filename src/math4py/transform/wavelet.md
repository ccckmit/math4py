# 小波轉換 (Wavelet Transform)

## 概述

小波轉換模組提供時頻分析工具，包括 Haar 小波、Daubechies 小波、離散小波轉換 (DWT/IDWT)、多層分解、小波去噪、連續小波轉換 (CWT) 等。

## 數學原理

### 1. Haar 小波母函數
$$\psi(t) = \begin{cases} 1 & 0 \leq t < 0.5 \\ -1 & 0.5 \leq t < 1 \\ 0 & \text{otherwise} \end{cases}$$

最簡單的小波，支援高頻訊號檢測。

### 2. 離散小波轉換 (DWT)
$$cA[n] = \frac{1}{\sqrt{2}}(x[2n] + x[2n+1]) \quad \text{（近似係數）}$$
$$cD[n] = \frac{1}{\sqrt{2}}(x[2n] - x[2n+1]) \quad \text{（細節係數）}$$

使用低通與高通濾波器對信號進行二分。

### 3. 逆離散小波轉換 (IDWT)
$$x[2n] = \frac{1}{\sqrt{2}}(cA[n] + cD[n])$$
$$x[2n+1] = \frac{1}{\sqrt{2}}(cA[n] - cD[n])$$

### 4. 多層 DWT
每次分解後的近似係數再次分解，產生多層尺度：
$$[cA_N, cD_N, cD_{N-1}, \ldots, cD_1]$$

### 5. 小波去噪（閾值法）
$$cD_{new}[i] = \begin{cases} cD[i] & |cD[i]| > \threshold \\ 0 & |cD[i]| \leq \threshold \end{cases}$$

軟閾值或硬閾值處理細節係數。

### 6. 連續小波轉換 (CWT)
$$W(a,b) = \frac{1}{\sqrt{a}}\int_{-\infty}^{\infty} f(t)\psi^*\left(\frac{t-b}{a}\right)dt$$

- $a$: 尺度參數
- $b$: 平移參數

### 7. Daubechies-4 濾波器係數
$$c = [0.483, 0.837, 0.224, -0.129]$$

具有更好的平滑性與緊支撐性。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `haar_wavelet()` | 生成 Haar 小波函數 |
| `daubechies4_coefficients()` | 返回 db4 濾波器係數 |
| `dwt()` | 單層離散小波轉換 |
| `idwt()` | 逆離散小波轉換 |
| `multilevel_dwt()` | 多層 DWT |
| `wavelet_denoise()` | 小波閾值去噪 |
| `continuous_wavelet_transform()` | 連續小波轉換 |

### 重構完整性
$$\text{IDWT}(\text{DWT}(x)) = x$$

誤差來源於浮點數運算。

## 使用方式

```python
from math4py.transform.wavelet import *
import numpy as np

# Haar 小波
t = np.linspace(0, 1, 100)
psi = haar_wavelet(t)

# Daubechies-4 係數
c = daubechies4_coefficients()

# 單層 DWT
signal = np.random.randn(128)
approx, detail = dwt(signal, wavelet="haar")

# 重構
recovered = idwt(approx, detail, wavelet="haar")

# 多層 DWT
coeffs = multilevel_dwt(signal, levels=3)
# coeffs[0] = cA_N, coeffs[1] = cD_N, ..., coeffs[N] = cD_1

# 小波去噪
noisy = signal + 0.5*np.random.randn(128)
denoised = wavelet_denoise(noisy, threshold=0.3)

# 連續小波轉換
scales = np.linspace(1, 10, 20)
cwt_matrix = continuous_wavelet_transform(signal, scales, haar_wavelet)
```