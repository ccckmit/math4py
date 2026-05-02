# set/theorem.md

## 概述

集合論定理與公理驗證模組，驗證 Zermelo-Fraenkel 集合論的公理及集合運算定律。

## 數學原理

### ZF 公理系統

| 公理 | 內容 |
|------|------|
| 空集公理 | ∅ 存在 |
| 外延公理 | 兩集合相等當且僅當元素相同 |
| 配對公理 | 對任意 a, b，{a, b} 存在 |
| 併集公理 | 任意集合族的聯集存在 |
| 冪集公理 | 任意集合的冪集存在 |
| 基礎公理 | 每個非空集合有 ∈-極小元 |
| 置換公理 | 集合在函數下的像是集合 |
| 分離公理 | {x ∈ A | φ(x)} 是集合 |

### 集合代數定律

| 定律 | 內容 |
|------|------|
| 交換律 | A ∪ B = B ∪ A, A ∩ B = B ∩ A |
| 結合律 | (A ∪ B) ∪ C = A ∪ (B ∪ C) |
| 分配律 | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) |
| 德摩根律 | (A ∪ B)' = A' ∩ B', (A ∩ B)' = A' ∪ B' |
| 對合律 | (A')' = A |
| 同一律 | A ∪ ∅ = A, A ∩ U = A |
| 支配律 | A ∪ U = U, A ∩ ∅ = ∅ |
| 冪等律 | A ∪ A = A, A ∩ A = A |
| 吸收律 | A ∪ (A ∩ B) = A |

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `extensionality_axiom(set1, set2)` | 外延公理 |
| `pair_set_axiom(a, b)` | 配對公理 |
| `union_axiom(sets)` | 併集公理 |
| `power_set_axiom(set1)` | 冪集公理 |
| `foundation_axiom(set1)` | 基礎公理 |
| `replacement_axiom(set1, func)` | 置換公理 |
| `separation_axiom(set1, predicate)` | 分離公理 |
| `commutativity_union(set1, set2)` | 交換律 |
| `associativity_union(set1, set2, set3)` | 結合律 |
| `distributivity_union_intersection(set1, set2, set3)` | 分配律 |
| `demorgans_law_union(set1, set2, universal)` | 德摩根律 |
| `double_complement(set1, universal)` | 對合律 |
| `identity(set1)` | 同一律 |
| `domination(set1, universal)` | 支配律 |
| `idempotent(set1)` | 冪等律 |
| `absorption(set1, set2)` | 吸收律 |

## 使用方式

```python
from math4py.set.theorem import demorgans_law_union, distributivity_union_intersection

universal = {1, 2, 3, 4, 5}
A = {1, 2}
B = {2, 3, 4}
result = demorgans_law_union(A, B, universal)
print(result["pass"])  # True
```