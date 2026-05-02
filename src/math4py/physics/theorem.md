# 物理定理驗證 (Physics Theorems)

## 概述

物理定理驗證模組提供物理學基本定律的數值驗證函數，包括牛頓第二定律、能量守恆、歐姆定律、斯涅爾定律、質能方程、波以爾定律、熱力學第一定律等。

## 數學原理

### 1. 牛頓第二定律
$$F = ma$$

力等於品質與加速度的乘積。

### 2. 機械能守恆
$$E_{initial} = E_{final}$$
$$KE_i + PE_i = KE_f + PE_f$$

### 3. 歐姆定律
$$V = IR$$

電壓等於電流與電阻的乘積。

### 4. 斯涅爾定律
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

### 5. 愛因斯坦質能方程
$$E = mc^2$$

### 6. 波以爾定律
$$P_1 V_1 = P_2 V_2$$

（恆溫條件下）

### 7. 熱力學第一定律
$$\Delta U = Q - W$$

## 實作細節

### 關鍵函數

| 函數 | 驗證內容 |
|------|----------|
| `newton_second_law()` | F = ma |
| `conservation_energy()` | 機械能守恆 |
| `ohms_law()` | V = IR |
| `snells_law()` | n₁ sin θ₁ = n₂ sin θ₂ |
| `einstein_energy()` | E = mc² |
| `boyle_law()` | P₁V₁ = P₂V₂ |
| `first_law_thermodynamics()` | ΔU = Q - W |

### 驗證方式

每個函數接受實際測量值作為參數，返回包含以下鍵的字典：
- `pass`: 布爾值，驗證是否通過
- `expected`: 理論預測值
- `actual`: 實際輸入值

## 使用方式

```python
from math4py.physics.theorem import *
import numpy as np

# 牛頓第二定律驗證
result = newton_second_law(mass=2.0, acceleration=9.8, force=19.6)
print(result)  # {'pass': True, 'expected': 19.6, 'actual': 19.6}

# 能量守恆驗證
result = conservation_energy(ke_initial=100, pe_initial=50, ke_final=80, pe_final=70)

# 歐姆定律驗證
result = ohms_law(voltage=12.0, current=0.5, resistance=24.0)

# 斯涅爾定律驗證
result = snells_law(n1=1.0, theta1=np.pi/6, n2=1.5, theta2=np.arcsin(1/1.5*np.sin(np.pi/6)))

# 愛因斯坦質能方程驗證
result = einstein_energy(mass=1.0, energy=9e16)  # c = 3e8 m/s

# 波以爾定律驗證
result = boyle_law(p1=101325, v1=1.0, p2=202650, v2=0.5)

# 熱力學第一定律驗證
result = first_law_thermodynamics(q=1000, delta_u=600, w=400)
```