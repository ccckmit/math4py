# algebra/complex_function.md

## 概述

複變函數（Complex Analysis）基礎函數，實現全純函數判定、線積分、留數、莫比烏斯變換、黎曼ζ函數等。

## 數學原理

### 柯西-黎曼方程 (Cauchy-Riemann Equations)
若 f(z) = u(x,y) + iv(x,y) 在 z 點可微，則：
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

### 全純函數 (Holomorphic Function)
在開集上處處滿足 C-R 方程的函數， equivalent to complex analytic。

### 柯西積分公式
$$f(a) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z-a} dz$$

### 留數定理
若 f 在封閉路徑 C 內有孤立奇點，則：
$$\oint_C f(z) dz = 2\pi i \sum \text{Res}(f, a_k)$$

### 莫比烏斯變換
$$w = \frac{az+b}{cz+d}, \quad ad-bc \neq 0$$
將圓/直線映射為圓/直線，構成保角變換。

### 劉維爾定理
有界的整函數必為常數。

### 黎曼ζ函數
$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}, \quad \text{Re}(s) > 1$$

### 黎曼猜想
ζ(s) 的所有非平凡零點都在臨界線 Re(s) = 1/2 上。

## 實作細節

| 函數 | 說明 |
|------|------|
| `complex_derivative(f, z)` | 數值導數 f'(z) ≈ (f(z+h)-f(z))/h |
| `is_analytic(f, z)` | 驗證 C-R 方程（數值版） |
| `is_holomorphic(f, domain)` | 檢查定義域上是否全純 |
| `line_integral(f, z0, z1)` | 路徑積分 ∫_C f(z) dz（直線段） |
| `cauchy_integral_formula(f, a, r)` | 柯西積分公式 |
| `residue_simple_pole(f, a)` | 簡單極點留數 lim_{z→a} (z-a)f(z) |
| `mobius_transformation(a,b,c,d,z)` | 莫比烏斯變換 |
| `riemann_zeta(s, n_terms)` | ζ(s) 的有限項近似 |
| `riemann_hypothesis_check_zeros()` | 驗證零點在 Re(s)=1/2 |
| `liouville_theorem_check(f)` | 劉維爾定理數值驗證 |
| `morera_theorem_check(f)` | 莫雷拉定理數值驗證 |

## 使用方式

```python
from math4py.algebra.complex_function import is_analytic, mobius_transformation, riemann_zeta

# 檢查 f(z) = z^2 在 z=1 是否解析
f = lambda z: z**2
is_analytic(f, 1+0j)  # True

# 莫比烏斯變換
mobius_transformation(1, 0, 0, 1, 2+0j)  # 2+0j (恆等變換)

# 黎曼ζ函數
riemann_zeta(2)  # ≈ π²/6
```