# 電漿體物理 (Plasma Physics)

## 概述

電漿體物理模組提供電漿體物理基礎計算函數，包括德拜長度、電漿體頻率、迴旋頻率、拉莫爾半徑、阿爾芬速度、離子聲速、碰撞頻率等。

## 數學原理

### 1. 德拜長度
$$\lambda_D = \sqrt{\frac{\varepsilon_0 k T_e}{n_e e^2}}$$

電漿體中靜電屏蔽的特徵長度。

### 2. 電漿體頻率
$$\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}}$$

電子集體振盪的特徵頻率。

### 3. 迴旋頻率（拉莫頻率）
$$\omega_c = \frac{qB}{m}$$

帶電粒子在磁場中的螺旋運動頻率。

### 4. 拉莫爾半徑
$$r_L = \frac{m v_\perp}{qB}$$

帶電粒子垂直於磁場的迴旋半徑。

### 5. 阿爾芬速度
$$v_A = \frac{B}{\sqrt{\mu_0 \rho}}$$

磁流體中的波速。

### 6. 離子聲速
$$c_s = \sqrt{\frac{k(T_e + \gamma T_i)}{m_i}}$$

離子聲波傳播速度。

### 7. 碰撞頻率（電子-離子）
$$\nu_{ei} = \frac{n_e e^4}{4\varepsilon_0^2 \sqrt{k^3 T_e^3/m_e}} \cdot 4\sqrt{\pi}$$

### 8. 電漿體 β
$$\beta = \frac{n k T}{B^2/(2\mu_0)}$$

熱壓力與磁壓力的比值。

### 9. 德拜數
$$N_D = n_e \lambda_D^3$$

德拜球內的粒子數。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `debye_length()` | 計算德拜長度 |
| `plasma_frequency()` | 計算電漿體頻率 |
| `cyclotron_frequency()` | 計算迴旋頻率 |
| `larmor_radius()` | 計算拉莫爾半徑 |
| `alfven_speed()` | 計算阿爾芬速度 |
| `sound_speed_ionacoustic()` | 計算離子聲速 |
| `collision_frequency()` | 計算碰撞頻率 |
| `plasma_beta()` | 計算電漿體 β |
| `debye_number()` | 計算德拜數 |
| `two_stream_instability_growth()` | 計算雙流不穩定性增長率 |

### 物理常數
- 電子電荷 $e = 1.602176634 \times 10^{-19}$ C
- 電子質量 $m_e = 9.10938356 \times 10^{-31}$ kg
- 真空介電常數 $\varepsilon_0 = 8.8541878128 \times 10^{-12}$ F/m

## 使用方式

```python
from math4py.physics.plasma_physics import *

# 德拜長度
lambda_D = debye_length(T_e=1e7, n_e=1e20)

# 電漿體頻率
omega_p = plasma_frequency(n_e=1e20)

# 迴旋頻率
omega_c = cyclotron_frequency(B=1.0)

# 拉莫爾半徑
r_L = larmor_radius(v_perp=1e6, B=0.1)

# 阿爾芬速度
v_A = alfven_speed(B=0.01, mu0=4e-7*np.pi, rho=1e-7)

# 離子聲速
c_s = sound_speed_ionacoustic(T_e=1e7, T_i=1e6, m_i=3.35e-27)

# 電漿體 β
beta = plasma_beta(B=0.1, n_e=1e20, T_e=1e7)
```