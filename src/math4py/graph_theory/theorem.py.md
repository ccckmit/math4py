# Graph Theory Theorems

## 概述

圖論定理驗證模組，驗證圖論中的重要定理和引理。

## 數學原理

### 歐拉路徑定理
圖有歐拉路徑 ( Eulerian path/circuit ) 當且僅當：
1. 恰好 0 或 2 個頂點有奇數度
2. 所有非零度頂點屬於同一連通分量

### 漢密爾頓路徑定理 (Dirac's 充分條件)
若 $n \geq 3$ 且每個頂點度 $\geq n/2$，則圖是漢密爾頓的。

### 四色定理
每個平面圖可以用 4 種顏色著色，使得相鄰區域顏色不同。

### 握手引理 (Handshaking Lemma)
$$\sum_{v \in V} \deg(v) = 2|E|$$

### 歐拉特徵公式
對於連通平面圖：
$$V - E + F = 2$$

### 樹的判定
圖是樹 (Tree) 當且僅當：
1. 連通
2. 有 $V-1$ 條邊

### 基爾霍夫定理 (Kirchhoff's Matrix-Tree Theorem)
圖的生成樹數量 = 拉普拉斯矩陣的餘因子行列式。

### 平面圖定理 (Kuratowski)
圖是平面圖當且僅當不包含 $K_5$ 或 $K_{3,3}$ 的細分。

### Brooks 定理
連通圖的色數 $\Delta$ (最大度) 或 $\Delta - 1$。

### 拉姆齊定理
存在 $R(m,n)$ 使得任意著色都有 $K_m$ 或 $K_n$。

### 最大流最小割定理
最大流量 = 最小割容量。

### 二分圖定理
圖是二分圖當且僅當沒有奇數環。

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `eulerian_path_theorem(num_odd_degree, connected)` | 歐拉路徑條件 |
| `hamiltonian_path_theorem(n, min_degree)` | Dirac 充分條件 |
| `four_color_theorem()` | 四色定理 |
| `handshaking_lemma(num_vertices, edges)` | 握手引理 |
| `euler_characteristic(vertices, edges, faces)` | 歐拉特徵 |
| `tree_theorem(num_vertices, num_edges)` | 樹的判定 |
| `kirchhoff_theorem()` | 矩陣-樹定理 |
| `planar_graph_theorem()` | Kuratowski 平面性 |
| `brooks_theorem()` | Brooks 定理 |
| `ramsey_theorem()` | 拉姆齊定理 |
| `mst_prim_theorem()` | Prim MST 最優性 |
| `shortest_path_theorem()` | 最短路徑定義 |
| `max_flow_min_cut_theorem()` | 最大流最小割 |
| `bipartite_graph_theorem()` | 二分圖判定 |

## 使用方式

```python
from math4py.graph_theory.theorem import (
    eulerian_path_theorem,
    hamiltonian_path_theorem,
    handshaking_lemma,
    euler_characteristic,
    tree_theorem
)

# 歐拉路徑判定
result = eulerian_path_theorem(num_odd_degree=0, connected=True)
# {"pass": True, "has_path": True}

# 漢密爾頓判定 (Dirac 條件)
result = hamiltonian_path_theorem(n=6, min_degree=3)
# {"pass": True, "is_hamiltonian": True}

# 握手引理
result = handshaking_lemma(num_vertices=4, edges=[(1,2), (2,3), (3,4), (4,1)])
# {"total_degree": 8, "twice_edges": 8, "pass": True}

# 歐拉特徵
result = euler_characteristic(vertices=4, edges=6, faces=4)
# {"chi": 2, "expected": 2, "is_eulerian": True}

# 樹判定
result = tree_theorem(num_vertices=5, num_edges=4)
# {"is_tree": True, "edges": 4, "vertices_1": 4}
```