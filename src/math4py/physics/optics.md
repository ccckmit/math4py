# 光學 (Optics)

## 概述

光學模組提供基礎光學計算函數，包括斯涅爾定律（全反射）、臨界角、透鏡製造者公式、放大率等。

## 數學原理

### 1. 斯涅爾定律（折射定律）
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

- $n_1, n_2$: 兩介質的折射率
- $\theta_1$: 入射角（從法線量起）
- $\theta_2$: 折射角

當 $\sin\theta_2 > 1$ 時發生全反射。

### 2. 臨界角
$$\theta_c = \arcsin\left(\frac{n_2}{n_1}\right), \quad n_1 > n_2$$

低折射率介質到高折射率介質的掠射極限。

### 3. 透鏡製造者公式
$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

- $f$: 焦距
- $n$: 透鏡折射率
- $R_1, R_2$: 透鏡兩面的曲率半徑

### 4. 放大率
$$M = -\frac{d_i}{d_o}$$

- $d_i$: 像距
- $d_o$: 物距
- 負號表示倒立實像

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `snells_law()` | 計算折射角或檢測全反射 |
| `critical_angle()` | 計算臨界角 |
| `lensmaker_equation()` | 計算透鏡焦距 |
| `magnification()` | 計算放大率 |

## 使用方式

```python
from math4py.physics.optics import *

# 斯涅爾定律
theta2 = snells_law(n1=1.0, n2=1.5, theta1=np.pi/6)

# 臨界角（玻璃到空氣）
theta_c = critical_angle(n1=1.5, n2=1.0)

# 透鏡製造者公式
f = lensmaker_equation(n=1.5, R1=0.5, R2=-0.5)

# 放大率
M = magnification(d_i=20, d_o=10)
```