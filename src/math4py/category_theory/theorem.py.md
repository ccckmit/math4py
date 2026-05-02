# 範疇論定理驗證

## 概述

本模組驗證範疇論中的核心公理和定理，包括範疇公理、函子定律、米田嵌入定理等。

## 數學原理

### 核心公理

1. **範疇公理**：
   - 恆等律：id_B ∘ f = f = f ∘ id_A
   - 結合律：(h ∘ g) ∘ f = h ∘ (g ∘ f)

2. **函子定律**：
   - F(id_A) = id_{F(A)}
   - F(g ∘ f) = F(g) ∘ F(f)

3. **米田嵌入定理**：
   - C → [C^op, Set] 是全且忠實的

4. **伴隨函子定理**：
   - 若存在單位與餘單位滿足三角等式，則為伴隨

## 實作細節

### 定理驗證函數

| 函數 | 驗證內容 |
|------|----------|
| `category_axioms(category)` | 恆等律、結合律 |
| `functor_laws(F)` | F(id_A) = id_{F(A)}, F(g∘f) = F(g)∘F(f) |
| `yoneda_embedding_theorem(C)` | C → [C^op, Set] 全且忠實 |
| `adjoint_functor_theorem(unit, counit)` | 三角等式 |
| `limit_uniqueness(limit1, limit2)` | 極限唯一性（相差同構） |
| `initial_object_uniqueness(obj1, obj2)` | 始物件唯一性 |
| `terminal_object_uniqueness(obj1, obj2)` | 終物件唯一性 |

## 使用方式

```python
from math4py.category_theory.function import Category, Object, Morphism
from math4py.category_theory.theorem import (
    category_axioms, functor_laws, yoneda_embedding_theorem
)

# 建立範疇
C = Category("Set")
C.add_object(Object("A"))
C.add_morphism(Morphism("A", "A", "id_A"))

# 驗證範疇公理
result = category_axioms(C)
# result["pass"] = True

# 驗證函子定律
F = {"preserves_identity": True, "preserves_composition": True}
result = functor_laws(F)
# result["pass"] = True
```