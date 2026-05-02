# algebra/theorem.md

## 概述

代數定理與公理驗證模組，驗證代數結構的基本公理和定理。

## 數學原理

### 代數公理

| 公理 | 內容 |
|------|------|
| 封閉公理 | a, b ∈ S ⇒ a ⊕ b ∈ S |
| 結合律 | (a ⊕ b) ⊕ c = a ⊕ (b ⊕ c) |
| 單位元 | e ⊕ a = a ⊕ e = a |
| 逆元 | a ⊕ a⁻¹ = e |
| 交換律 | a ⊕ b = b ⊕ a |
| 分配律 | a ⊗ (b ⊕ c) = a⊗b ⊕ a⊗c |

### 代數基本定理 (Fundamental Theorem of Algebra)
每個非常數複係數多項式至少有一個複根，因此 n 次多項式恰好有 n 個複根（按代數重數計算）。

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `closure_axiom(op, a, b)` | 封閉公理 |
| `associativity(op, a, b, c)` | 結合律 |
| `identity_element(op, e, a)` | 單位元 |
| `inverse_element(op, a, inverse)` | 逆元 |
| `commutativity(op, a, b)` | 交換律 |
| `distributivity(op1, op2, a, b, c)` | 分配律 |
| `fundamental_theorem_of_algebra(coefficients)` | 代數基本定理（用 numpy.roots） |

## 使用方式

```python
from math4py.algebra.theorem import associativity, distributivity, fundamental_theorem_of_algebra

# 驗證加法結合律
associativity(lambda a, b: a + b, 1, 2, 3)  # True

# 驗證乘法對加法的分配律
distributivity(lambda a, b: a * b, lambda a, b: a + b, 2, 3, 4)  # True

# 代數基本定理：x² + 1 = 0 有 2 個複根
fundamental_theorem_of_algebra([1, 0, 1])  # degree=2, num_roots=2
```