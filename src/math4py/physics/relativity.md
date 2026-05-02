# 相對論 (Relativity)

## 概述

相對論模組提供特殊相對論與廣義相對論的基礎計算函數，包括勞侖茲因子、時間膨脹、長度收縮、質能方程、時空間隔、史瓦西度規等。

## 數學原理

### 1. 勞侖茲因子
$$\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}$$

- $c = 299792458$ m/s: 光速

### 2. 勞侖茲變換
$$\Lambda = \begin{pmatrix} \gamma & -\gamma\beta \\ -\gamma\beta & \gamma \end{pmatrix}$$

用於在不同慣性參考系間變換坐標。

### 3. 時間膨脹
$$\Delta t' = \gamma \Delta t$$

運動的時鐘走得較慢。

### 4. 長度收縮
$$L' = \frac{L}{\gamma}$$

運動方向上的長度收縮。

### 5. 相對論動量
$$p = \gamma m v$$

### 6. 相對論能量
$$E = \gamma m c^2$$

### 7. 質能方程
$$E = mc^2$$

愛因斯坦最著名的方程式。

### 8. 時空間隔（號差 -+++）
$$ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$$

在所有慣性參考系中保持不變。

### 9. 史瓦西度規
$$ds^2 = -\left(1-\frac{R_s}{r}\right)c^2dt^2 + \frac{1}{1-R_s/r}dr^2 + r^2d\theta^2 + r^2\sin^2\theta d\phi^2$$

其中 $R_s = 2GM/c^2$ 為史瓦西半徑。

### 10. 弗里德曼-勒梅特-羅伯遜-沃克 (FLRW) 度規
$$ds^2 = -c^2dt^2 + a(t)^2(dx^2 + dy^2 + dz^2)$$

描述膨脹宇宙的時空幾何。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `lorentz_factor()` | 計算勞侖茲因子 γ |
| `lorentz_transformation()` | 計算勞侖茲變換矩陣 |
| `time_dilation()` | 計算時間膨脹因子 |
| `length_contraction()` | 計算長度收縮因子 |
| `relativistic_momentum()` | 計算相對論動量 |
| `relativistic_energy()` | 計算相對論能量 |
| `mass_energy_equivalence()` | 計算 E = mc² |
| `spacetime_interval()` | 計算時空間隔 |
| `schwarzschild_metric()` | 計算史瓦西度規 |
| `friedmann_metric()` | 計算 FLRW 度規 |

## 使用方式

```python
from math4py.physics.relativity import *
import numpy as np

# 勞侖茲因子
v = np.array([0.8 * 299792458, 0, 0])  # 0.8c
gamma = lorentz_factor(v)

# 質能方程
E = mass_energy_equivalence(m=1.0)  # kg -> Joules

# 時空間隔
x1 = [0, 0, 0, 0]
x2 = [1, 1, 0, 0]  # ct, x, y, z
s2 = spacetime_interval(x1, x2)

# 史瓦西度規
g = schwarzschild_metric(r=1e10, theta=np.pi/2)
```