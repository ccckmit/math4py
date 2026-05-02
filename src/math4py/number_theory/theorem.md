# number_theory/theorem.md

## 概述

數論定理驗證模組，以函數形式驗證數論中的重要定理與性質。

## 數學原理

### 貝祖等式 (Bézout's Identity)
對任意整數 a, b，存在整數 x, y 使 `ax + by = gcd(a, b)`。

### 算術基本定理 (Fundamental Theorem of Arithmetic)
每個大於 1 的整數可以唯一分解為質數的乘積（忽略次序）。

### 歐拉 φ 函數的積性
若 `gcd(m, n) = 1`，則 `φ(mn) = φ(m) · φ(n)`。

### 費馬小定理 (Fermat's Little Theorem)
若 p 為質數且 `gcd(a, p) = 1`，則 `a^(p-1) ≡ 1 (mod p)`。

### 歐拉定理 (Euler's Theorem)
若 `gcd(a, n) = 1`，則 `a^φ(n) ≡ 1 (mod n)`。費馬小定理是其特例（當 n 為質數）。

### 中國剩餘定理 (Chinese Remainder Theorem)
若模數兩兩互質，則同餘方程組有唯一解（模 M = m₁m₂...）。

### 費波那契數的 GCD 性質
$$\gcd(F_m, F_n) = F_{\gcd(m, n)}$$

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `bezout_identity(a, b)` | 貝祖等式 |
| `fundamental_theorem_of_arithmetic(n)` | 算術基本定理 |
| `euler_phi_multiplicative(m, n)` | φ 函數積性 |
| `fermat_little_theorem(p, a)` | 費馬小定理 |
| `euler_theorem(n, a)` | 歐拉定理 |
| `chinese_remainder_theorem(m, a)` | 中國剩餘定理 |
| `gcd_lcm_relation(a, b)` | gcd(a,b)·lcm(a,b) = \|ab\| |
| `fibonacci_gcd_property(m, n)` | F_m 和 F_n 的最大公因數 |

## 使用方式

```python
from math4py.number_theory.theorem import fermat_little_theorem, euler_theorem

fermat_little_theorem(7, 3)   # True (3^6 ≡ 1 mod 7)
euler_theorem(10, 3)          # True (3^4 ≡ 1 mod 10, φ(10)=4)
```