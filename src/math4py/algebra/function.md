# algebra/function.md

## 概述

代數結構模組，實現抽象代數的核心結構：群 (Group)、環 (Ring)、域 (Field)、向量空間 (VectorSpace)。

## 數學原理

### 群 (Group)
帶有一個二元運算的代數結構，滿足：
- **封閉性**：封閉
- **結合律**：封閉
- **單位元**：存在 identity
- **逆元**：每個元素都有 inverse

若還滿足**交換律**，則為**阿貝爾群 (Abelian Group)**。

### 環 (Ring)
帶有兩個二元運算（加法、乘法）的代數結構：
- (R, +) 是阿貝爾群
- 乘法封閉且滿足結合律
- 乘法對加法滿足分配律

若乘法有單位元，則為**含單位元環**。

### 域 (Field)
滿足：
- (F, +) 是阿貝爾群
- (F \ {0}, ·) 是阿貝爾群
- 乘法對加法分配

有理數 ℚ、實數 ℝ、複數 ℂ 都是域。

### 向量空間 (VectorSpace)
定義在域上的向量集合，配備向量加法和標量乘法：
- (V, +) 是阿貝爾群
- 標量乘法與域乘法兼容

## 實作細節

| 類別 | 關鍵方法 |
|------|----------|
| `AlgebraicStructure` | `is_closed()` 驗證封閉性 |
| `Group` | `is_group()` 驗證群公理, `is_abelian()` 驗證交換性 |
| `Ring` | `is_ring()` 驗證環公理 |
| `Field` | `is_field()` 驗證域公理（額外要求乘法逆元） |
| `VectorSpace` | `is_vector_space()` 驗證向量空間公理 |

## 使用方式

```python
from math4py.algebra import Group, Field

# 整數加法群 (Z, +)
int_add_group = Group("Z", set(range(-10, 11)), lambda a, b: a + b, 0, lambda a: -a)
int_add_group.is_group()   # True
int_add_group.is_abelian()  # True

# 有理數域
Q = Field("Q", ..., add, 0, lambda a: -a, mul, 1, lambda a: 1/a)
```