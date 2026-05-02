# algebra/complex.md

## 概述

複數運算函數模組，實現複數的創建、四則運算、極座標轉換、指数對數運算。

## 數學原理

### 複數基本運算
對 z₁ = a + bi, z₂ = c + di：
- 加法：z₁ + z₂ = (a+c) + (b+d)i
- 乘法：z₁ · z₂ = (ac-bd) + (ad+bc)i
- 除法：z₁ / z₂ = (ac+bd)/(c²+d²) + (bc-ad)/(c²+d²)i

### 極座標表示
$$z = re^{i\theta} = r(\cos\theta + i\sin\theta)$$
- r = |z| = √(a²+b²) （模）
- θ = arg(z) ∈ (-π, π] （幅角）

### 複數指數與對數
- e^z = e^(a+bi) = e^a (cos b + i sin b)
- log(z) = log|z| + i arg(z)

## 實作細節

| 函數 | 說明 |
|------|------|
| `create_complex(real, imag)` | 建立 a+bi |
| `real_part(z)`, `imag_part(z)` | 取實部/虛部 |
| `conjugate(z)` | 共軛複數 a-bi |
| `modulus(z)` | 模 \|z\| |
| `argument(z)` | 幅角 θ ∈ (-π, π] |
| `to_polar(z)` | 轉極座標 (r, θ) |
| `from_polar(r, theta)` | 從極座標建立複數 |
| `complex_exp(z)` | e^z |
| `complex_log(z)` | 複數對數 |
| `complex_pow(z, w)` | z^w |
| `solve_quadratic(a, b, c)` | 解 ax²+bx+c=0（返回兩個根） |

## 使用方式

```python
from math4py.algebra.complex import modulus, argument, from_polar, solve_quadratic

z = 3 + 4j
modulus(z)           # 5.0
argument(z)          # 0.927295... (arctan 4/3)

solve_quadratic(1, -3, 2)  # (2.0, 1.0) — x²-3x+2=0 的根
```