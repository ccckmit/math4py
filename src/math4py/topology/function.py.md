# 拓撲學（Topology）基礎函數

## 概述

本模組提供拓撲學的基礎運算函數，包括開集/閉集判斷、連通性、緊緻性、同胚檢查等核心拓撲概念。

## 數學原理

### 核心定義

1. **拓撲空間**：集合 X 配上拓撲 τ，滿足：
   - ∅ 和 X 在 τ 中
   - 任意並封閉
   - 有限交封閉

2. **開集與閉集**：
   - 開集的補集為閉集
   - 閉集的補集為開集

3. **歐拉示性數**：χ = V - E + F（適用於多面體）

4. **豪斯多夫空間**：任意兩不同點存在不相交的开鄰域

5. **同胚**：雙射 f: X → Y 滿足 f 和 f⁻¹ 都連續

## 實作細節

### 主要函數

| 函數 | 數學含義 |
|------|----------|
| `is_open_set(points, topology)` | 檢查是否為開集 |
| `is_closed_set(points, topology)` | 檢查是否為閉集（補集為開集） |
| `is_connected(topology)` | 檢查連通性（非平凡既開又閉的集合不存在） |
| `euler_characteristic(v, e, f)` | χ = V - E + F |
| `is_compact(topology, covering)` | 緊緻性（有限子覆蓋） |
| `is_hausdorff(points, distance_fn)` | 豪斯多夫分離公理 |
| `closure(set_A, limit_points)` | Ā = A ∪ A'（閉包） |
| `interior(set_A, open_sets)` | 內部（最大開子集） |
| `boundary(set_A, closure_A, interior_A)` | ∂A = Ā - A°（邊界） |
| `homeomorphism_check(f, f_inv, domain, codomain)` | 同胚驗證 |
| `topological_sort(graph)` | 拓撲排序（Kahn 演算法） |

## 使用方式

```python
from math4py.topology.function import (
    is_open_set, is_closed_set, is_connected,
    euler_characteristic, closure, interior, boundary
)

# 檢查開集
topology = {"open_sets": {frozenset({1,2}), frozenset({2,3})}, "universal": {1,2,3}}
is_open_set({1, 2}, topology)  # True

# 歐拉示性數
chi = euler_characteristic(vertices=8, edges=12, faces=6)  # 立方體: 8-12+6=2

# 閉包、內部、邊界
A = {1, 2, 3}
limit_pts = {4, 5}
cl = closure(A, limit_pts)  # {1,2,3,4,5}

# 拓撲排序
graph = {0: [1, 2], 1: [3], 2: [3]}
result = topological_sort(graph)  # [0, 1, 2, 3] 或類似順序
```