# 電磁學 (Electromagnetism)

## 概述

電磁學模組提供電磁學基礎計算函數，包括庫侖定律、電場、比奧-沙瓦定律、安培定律、法拉第定律、坡印廷向量等。

## 數學原理

### 1. 庫侖定律
$$\vec{F} = k \frac{q_1 q_2}{r^2} \hat{r}$$

$$k = \frac{1}{4\pi\varepsilon_0} = 8.9875517923 \times 10^9 \text{ N·m²/C²}$$

### 2. 點電荷電場
$$\vec{E} = k \frac{q}{r^2} \hat{r}$$

### 3. 比奧-沙瓦定律
$$d\vec{B} = \frac{\mu_0}{4\pi} \frac{I d\vec{l} \times \vec{r}}{r^3}$$

- $\mu_0 = 4\pi \times 10^{-7}$ H/m: 真空磁導率

### 4. 無限長直導線磁場
$$B = \frac{\mu_0 I}{2\pi r}$$

### 5. 安培定律
$$\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{enclosed}$$

### 6. 法拉第電磁感應定律
$$\varepsilon = -\frac{d\Phi_B}{dt}$$

### 7. 坡印廷向量
$$\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}$$

描述電磁能量流密度。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `coulomb_law()` | 計算兩電荷間的庫侖力 |
| `electric_field_point_charge()` | 計算點電荷電場 |
| `biot_savart_law()` | 計算電流元素產生的磁場 |
| `magnetic_field_wire()` | 計算直導線磁場 |
| `ampere_law()` | 計算閉合路徑的磁場環積分 |
| `faraday_law()` | 計算感應電動勢 |
| `maxwell_equations_check()` | 驗證麥克斯韋方程組 |
| `poynting_vector()` | 計算坡印廷向量 |

### 物理常數
- 真空介電常數 $\varepsilon_0 = 8.8541878128 \times 10^{-12}$ F/m
- 真空磁導率 $\mu_0 = 4\pi \times 10^{-7}$ H/m
- 光速 $c = 299792458$ m/s

## 使用方式

```python
from math4py.physics.electromagnetism import *
import numpy as np

# 庫侖力
r = np.array([1, 0, 0])  # 方向
F = coulomb_law(q1=1e-9, q2=-1e-9, r=r)

# 點電荷電場
E = electric_field_point_charge(q=1e-9, r=r)

# 磁場（直導線）
B = magnetic_field_wire(I=10, r=0.1)

# 坡印廷向量
E_vec = np.array([100, 0, 0])
B_vec = np.array([0, 1e-6, 0])
S = poynting_vector(E_vec, B_vec)
```