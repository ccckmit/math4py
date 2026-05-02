# Graph Theory Functions

## 概述

圖論函數模組，使用 networkx 實現圖的創建與各種圖論算法。

## 數學原理

### 圖的表示
- 鄰接矩陣: $A_{ij} = 1$ 若邊 $(i,j)$ 存在
- 拉普拉斯矩陣: $L = D - A$ (度矩陣減鄰接矩陣)

### 度與度分佈
- 度: 節點相鄰邊的數量
- 度分佈: 各度的節點數量統計

### 最短路徑
- BFS: 無權圖最短路徑
- Dijkstra: 非負權圖最短路徑
- Bellman-Ford: 可處理負權邊

### 連通性
- 連通分量: 最大連通子圖
- 雙連通: 無割點
- 二分圖: 節點可分為兩集合，邊只在集合間

### 中心性
- 度中心性: $C_D(v) = \frac{\deg(v)}{n-1}$
- 緊密中心性: $C_C(v) = \frac{n-1}{\sum d(u,v)}$
- 介數中心性: 經過該點的最短路徑比例
- 特徵向量中心性: 鄰居中心性之和

### PageRank
$$PR(v) = \frac{1-d}{n} + d \sum_{u \in M(v)} \frac{PR(u)}{\deg(u)}$$

## 實作細節

### 圖創建

| 函數 | 說明 |
|------|------|
| `create_graph(edges, directed)` | 從邊列表創建圖 |
| `create_weighted_graph(edges, directed)` | 創建帶權圖 |

### 矩陣運算

| 函數 | 說明 |
|------|------|
| `adjacency_matrix(G)` | 鄰接矩陣 |
| `laplacian_matrix(G)` | 拉普拉斯矩陣 |

### 度與連通

| 函數 | 說明 |
|------|------|
| `degree_sequence(G)` | 度序列 |
| `degree_distribution(G)` | 度分佈 |
| `average_degree(G)` | 平均度 |
| `clustering_coefficient(G)` | 平均聚類係數 |
| `clustering_coefficients(G)` | 各節點聚類係數 |

### 路徑演算法

| 函數 | 說明 |
|------|------|
| `shortest_path(G, s, t)` | 最短路徑 |
| `shortest_path_length(G, s, t)` | 最短路徑長度 |
| `dijkstra_shortest_path(G, s, t)` | Dijkstra |
| `dijkstra_path_length(G, s, t)` | Dijkstra 路徑長度 |
| `bellman_ford_shortest_path(G, s, t)` | Bellman-Ford |

### 連通性

| 函數 | 說明 |
|------|------|
| `connected_components(G)` | 連通分量 |
| `number_of_connected_components(G)` | 連通分量數 |
| `is_connected(G)` | 是否連通 |
| `is_biconnected(G)` | 是否雙連通 |
| `articulation_points(G)` | 割點 |
| `is_bipartite(G)` | 是否二分圖 |
| `color_bipartite(G)` | 二分圖著色 |

### 圖屬性

| 函數 | 說明 |
|------|------|
| `graph_center(G)` | 圖中心 |
| `eccentricity(G, v)` | 離心率 |
| `radius(G)` | 半徑 |
| `diameter(G)` | 直徑 |

### 中心性

| 函數 | 說明 |
|------|------|
| `pagerank(G, alpha)` | PageRank |
| `hits_scores(G)` | HITS (hub/authority) |
| `betweenness_centrality(G)` | 介數中心性 |
| `degree_centrality(G)` | 度中心性 |
| `closeness_centrality(G)` | 緊密中心性 |
| `eigenvector_centrality(G)` | 特徵向量中心性 |

### 生成樹

| 函數 | 說明 |
|------|------|
| `minimum_spanning_tree(G)` | 最小生成樹 |
| `minimum_spanning_tree_edges(G)` | MST 邊 |

### 計數

| 函數 | 說明 |
|------|------|
| `number_of_edges(G)` | 邊數 |
| `number_of_nodes(G)` | 節點數 |
| `density(G)` | 密度 |

### 歐拉/漢密爾頓

| 函數 | 說明 |
|------|------|
| `is_eulerian(G)` | 是否有歐拉迴路 |
| `eulerian_path(G)` | 歐拉路徑 |
| `is_hamiltonian(G)` | 是否有漢密爾頓迴路 |
| `traveling_salesman(G)` | 旅行商問題近似 |

### 組合優化

| 函數 | 說明 |
|------|------|
| `max_clique(G)` | 最大團 |
| `graph_clique_number(G)` | 團數 |
| `independent_set(G)` | 最大獨立集 |
| `vertex_cover(G)` | 最小點覆蓋 |

## 使用方式

```python
from math4py.graph_theory.function import (
    create_graph, create_weighted_graph, 
    dijkstra_shortest_path, pagerank,
    connected_components, minimum_spanning_tree
)

# 創建無向圖
edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
G = create_graph(edges)

# 創建帶權圖
weighted_edges = [(1, 2, 0.5), (2, 3, 1.5), (3, 4, 2.0)]
WG = create_weighted_graph(weighted_edges)

# 最短路徑
path = dijkstra_shortest_path(WG, 1, 4)

# PageRank
pr = pagerank(G)

# 連通分量
components = connected_components(G)

# 最小生成樹
mst = minimum_spanning_tree(WG)
```