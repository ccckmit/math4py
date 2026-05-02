# test_physics_theorems.py - 物理定理測試文檔

## 概述 (Overview)

本測試文件驗證 math4py 物理定理模組的核心物理定律，包括牛頓第二定律、能量守恆、歐姆定律、斯涅爾定律、愛因斯坦質能關係、波以耳定律、熱力學第一定律。

## 測試內容 (Test Coverage)

### 測試類別

| 類別 | 測試內容 | 驗證原理 |
|------|----------|----------|
| `TestNewtonSecondLaw` | 牛頓第二定律 | $F = ma$ |
| `TestConservationEnergy` | 能量守恆 | $KE_i + PE_i = KE_f + PE_f$ |
| `TestOhmsLaw` | 歐姆定律 | $V = IR$ |
| `TestSnellsLaw` | 斯涅爾折射定律 | $n_1 \sin\theta_1 = n_2 \sin\theta_2$ |
| `TestEinsteinEnergy` | 愛因斯坦質能關係 | $E = mc^2$ |
| `TestBoyleLaw` | 波以耳定律 | $P_1 V_1 = P_2 V_2$ |
| `TestFirstLawThermodynamics` | 熱力學第一定律 | $\Delta U = Q - W$ |

## 測試原理 (Testing Principles)

### 牛頓第二定律
$$F = ma$$

加速度與力成正比，與質量成反比。

### 能量守恆
機械能守恆（無非保守力）：
$$KE_i + PE_i = KE_f + PE_f$$
$$\frac{1}{2}mv_i^2 + mgh_i = \frac{1}{2}mv_f^2 + mgh_f$$

### 歐姆定律
$$V = IR$$

電壓等於電流與電阻的乘積。

### 愛因斯坦質能關係
$$E = mc^2$$

質量與能量可互相轉換，$c$ 為光速。

### 波以耳定律（等溫過程）
$$PV = \text{const}$$

溫度不變時，壓力與體積成反比。

### 熱力學第一定律
$$\Delta U = Q - W$$

內能變化等於吸收熱量減去對外作功。