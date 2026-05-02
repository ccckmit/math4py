# algebra/galois_theory.md

## 概述

伽羅瓦理論函數，實現多項式可解性判斷、判別式計算、古典作圖不可能問題。

## 數學原理

### 多項式的基本概念
- **次數 (Degree)**：最高冪係數的指數
- **可分多項式 (Separable)**：無重根，即 gcd(f, f') = 1
- **判別式 (Discriminant)**：Δ = ∏_{i<j}(rᵢ - rⱼ)²，Δ=0 表示有重根

### 伽羅瓦群與可解性
- n 次一般多項式的伽羅瓦群是 S_n
- \|S_n\| = n!，\|A_n\| = n!/2
- **伽羅瓦定理**：多項式可用根式求解當且僅當其伽羅瓦群是可解群
- S_n 對 n ≥ 5 是不可解群，因此一般五次方程無根式解

### 古典不可能作圖問題

| 問題 | 數學表述 | 證明思路 |
|------|----------|----------|
| 化圓為方 | 構造 √π | π 超越數（林德曼-魏爾斯特拉斯定理） |
| 倍立方 | 構造 ∛2 | ∛2 是三次代數數，不可由二次無理數構造 |
| 三等分任意角 | 解 8x³-6x-1=0 | 该三次方程不可約，根不能由二次根式表示 |

## 實作細節

| 函數 | 說明 |
|------|------|
| `polynomial_degree(coeffs)` | 多項式次數 |
| `separable_polynomial(coeffs)` | 檢查是否可分（無重根） |
| `discriminant(coeffs)` | 判別式 Δ = ∏_{i<j}(rᵢ-rⱼ)² |
| `discriminant_quadratic(a, b, c)` | 二次方程判別式 b²-4ac |
| `resolvent_cubic(coeffs)` | 四次方程的立方預解式 |
| `galois_group_solvable(coeffs)` | 伽羅瓦群是否可解（n≤4 可解） |
| `solvable_by_radicals(coeffs)` | 多項式是否可用根式求解 |
| `classical_impossibility_theorems()` | 三個古典不可能問題總結 |

## 使用方式

```python
from math4py.algebra.galois_theory import solvable_by_radicals, discriminant

# x⁴ - 1 可用根式求解
solvable_by_radicals([1, 0, 0, 0, -1])  # {solvable: True, degree: 4}

# 判別式：Δ < 0 表示有複根
discriminant_quadratic(1, 0, 1)  # -4 （兩個複根）
```