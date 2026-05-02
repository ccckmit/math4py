# 範疇論（Category Theory）基礎函數

## 概述

本模組提供範疇論的核心資料結構和運算，包括物件、態射、函子、自然變換、極限等範疇論基礎概念。

## 數學原理

### 核心定義

1. **範疇 C = (Obj, Hom, ∘, id)**：
   - Obj: 物件集合
   - Hom(A, B): A 到 B 的態射集合
   - ∘: 態射複合
   - id: 恆等態射

2. **函子 F: C → D**：
   - F(id_A) = id_{F(A)}
   - F(g ∘ f) = F(g) ∘ F(f)

3. **自然變換 η: F ⇒ G**：
   - 對每個物件 A 有 η_A: F(A) → G(A)
   - η_B ∘ F(f) = G(f) ∘ η_A

4. **米田引理**：Nat(Hom(A, -), F) ≅ F(A)

## 實作細節

### 類別

| 類別 | 數學含義 |
|------|----------|
| `Object` | 範疇中的物件 |
| `Morphism` | 態射 f: source → target |
| `Category` | 範疇 C = (Obj, Hom, ∘, id) |

### 主要函數

| 函數 | 數學含義 |
|------|----------|
| `functor_map(F, C, D, obj_map, morph_map)` | 函子映射 |
| `natural_transformation(F, G, components)` | 自然變換 η: F ⇒ G |
| `limit_product(objects, projections)` | 極限：乘積 ∏ A_i |
| `colimit_coproduct(objects, injections)` | 餘極限：餘乘積 ∐ A_i |
| `adjoint_functors(F, G, unit, counit)` | 伴隨函子 F ⊣ G |
| `yoneda_lemma(C, F, A)` | Nat(Hom(A,-), F) ≅ F(A) |
| `initial_object(objects, morphisms)` | 始物件 |
| `terminal_object(objects, morphisms)` | 終物件 |

## 使用方式

```python
from math4py.category_theory.function import (
    Object, Morphism, Category,
    functor_map, yoneda_lemma, initial_object
)

# 建立範疇
C = Category("C")
a = Object("A")
b = Object("B")
C.add_object(a)
C.add_object(b)

# 添加態射
f = Morphism("A", "B", "f")
C.add_morphism(f)

# 檢查範疇公理
C.is_valid()  # True

# 函子映射
F = functor_map("F", C, C, {"A": "A", "B": "B"}, {"f": "f"})

# 米田引理
result = yoneda_lemma(C, {"value_at_A": 42}, "A")
```