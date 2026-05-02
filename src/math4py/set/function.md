# set/function.md

## 概述

集合論運算函數，實現集合的聯集、交集、差集、冪集、笛卡爾積等基本操作。

## 數學原理

### 集合基本運算
| 運算 | 符號 | 定義 |
|------|------|------|
| 聯集 | A ∪ B | 屬於 A 或 B 的元素 |
| 交集 | A ∩ B | 同時屬於 A 和 B 的元素 |
| 差集 | A - B | 屬於 A 但不屬於 B 的元素 |
| 對稱差 | A Δ B | 僅屬於 A 或 B 之一的元素 |
| 補集 | A' | 全集中不屬於 A 的元素 |

### 冪集 (Power Set)
P(A) 包含 A 的所有子集，|P(A)| = 2^|A|。

### 笛卡爾積 (Cartesian Product)
A × B = {(a, b) | a ∈ A, b ∈ B}。

## 實作細節

| 函數 | 說明 |
|------|------|
| `union(set1, set2)` | 聯集 A ∪ B |
| `intersection(set1, set2)` | 交集 A ∩ B |
| `difference(set1, set2)` | 差集 A - B |
| `symmetric_difference(set1, set2)` | 對稱差 A Δ B |
| `complement(set1, universal)` | 補集 |
| `is_subset(set1, set2)` | 子集判斷 ⊆ |
| `is_proper_subset(set1, set2)` | 真子集 ⊂ |
| `cartesian_product(set1, set2)` | 笛卡爾積 A × B |
| `power_set(set1)` | 冪集 P(A) |
| `cardinality(set1)` | 基數 \|A\| |
| `is_disjoint(set1, set2)` | 不相交 (A ∩ B = ∅) |
| `union_all(sets)` | 多集合聯集 ⋃Aᵢ |
| `intersection_all(sets)` | 多集合交集 ⋂Aᵢ |
| `partition_set(set1, predicate)` | 按述詞分割集合 |

## 使用方式

```python
from math4py.set import union, intersection, power_set, cartesian_product

A = {1, 2, 3}
B = {2, 3, 4}
union(A, B)                    # {1, 2, 3, 4}
intersection(A, B)            # {2, 3}
power_set({1, 2})             # {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})}
cartesian_product({1, 2}, {'a', 'b'})  # {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}
```