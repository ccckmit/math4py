# logic/zfc.md

## 概述

ZFC 公理系統（Zermelo-Fraenkel + Choice）實現，構造集合、驗證公理、構建自然數。

## 數學原理

### ZFC 公理系統

| 公理 | 內容 |
|------|------|
| 外延公理 | 兩集合相等當且僅當元素相同 |
| 空集公理 | ∅ 存在 |
| 配對公理 | 對任意 a, b，{a, b} 存在 |
| 併集公理 | 集合族的聯集存在 |
| 冪集公理 | 每個集合的冪集存在 |
| 無窮公理 | 歸納集合存在（保證 ℕ 存在） |
| 正則公理 | 每個非空集合有 ∈-極小元（防止 x ∈ x） |
| 替換公理模式 | 函數下的像仍是集合 |
| 分離公理模式 | {x ∈ A | φ(x)} 是集合 |
| 選擇公理 | 任意非空集合族存在選擇函數 |

### 馮·諾伊曼自然數構造
$$0 = \emptyset$$
$$1 = \{0\} = \{\emptyset\}$$
$$2 = \{0, 1\} = \{\emptyset, \{\emptyset\}\}$$
$$n+1 = n \cup \{n\}$$

### 有序對
(a, b) = {{a}, {a, b}}（庫拉托夫斯基定義）

## 實作細節

| 函數 | 說明 |
|------|------|
| `extensionality_axiom(A, B)` | 驗證外延公理 |
| `pair_set_axiom(a, b)` | 構造 {a, b} |
| `union_axiom(sets)` | 構造 ⋃S |
| `foundation_axiom(s)` | 驗證正則公理 |
| `choice_axiom(sets)` | 選擇函數（返回每集合選中的元素） |
| `construct_natural_numbers()` | 馮·諾伊曼自然數構造 |
| `ordered_pair(a, b)` | 構造有序對 |
| `verify_zfc_axioms()` | ZFC 公理系統驗證 |

## 使用方式

```python
from math4py.logic.zfc import (
    Set, EMPTY_SET, pair_set_axiom, union_axiom,
    construct_natural_numbers, choice_axiom
)

# 有序對
p = ordered_pair(1, 2)  # {{1}, {1, 2}}

# 構造自然數
nats = construct_natural_numbers()
# nats[0] = ∅, nats[1] = {∅}, nats[2] = {∅, {∅}}, ...

# 選擇公理
sets = [Set({1, 2}), Set({3, 4})]
success, choice = choice_axiom(sets)  # 返回選擇結果
```