# test_graph.py

## 概述 (Overview)

使用 networkx 測試圖論函數模組，包括圖的創建、矩陣運算、度性質、連通性、最短路徑、中心性、特徵值性質、生成樹、二部圖、特殊圖形等。

## 測試內容 (Test Coverage)

### 圖創建 (TestGraphCreation)

| 測試 | 描述 |
|------|------|
| `test_create_simple_graph` | 無向圖創建（4節點、3邊） |
| `test_create_directed_graph` | 有向圖創建（3節點、3邊） |
| `test_create_weighted_graph` | 加權圖創建（邊有权重） |

### 矩陣運算 (TestGraphMatrices)

| 測試 | 描述 |
|------|------|
| `test_adjacency_matrix` | 鄰接矩陣（3×3，對角線為0，有邊為1） |
| `test_laplacian_matrix` | 拉普拉斯矩陣 L = D - A |

### 度性質 (TestDegreeProperties)

| 測試 | 描述 |
|------|------|
| `test_degree_sequence` | 度序列（路徑圖 [1,2,2,1]） |
| `test_degree_distribution` | 度分布統計 |
| `test_average_degree` | 平均度 = 2E/V |

### 連通性 (TestConnectivity)

| 測試 | 描述 |
|------|------|
| `test_connected_components` | 連通分量數量 |
| `test_is_connected` | 連通性判斷 |
| `test_articulation_points` | 割點/關節點 |
| `test_is_biconnected` | 雙連通判斷（三角形） |

### 最短路徑 (TestShortestPath)

| 測試 | 描述 |
|------|------|
| `test_shortest_path` | 最短路徑搜索 |
| `test_shortest_path_length` | 最短路徑長度 |
| `test_no_path_same_node` | 相同節點路徑長度為0 |
| `test_dijkstra_weighted` | Dijkstra 加權最短路徑 |
| `test_dijkstra_path_length` | Dijkstra 路徑長度 |

### 中心性 (TestCentralityMeasures)

| 測試 | 描述 |
|------|------|
| `test_degree_centrality` | 度中心性 |
| `test_closeness_centrality` | 接近中心性（星形圖中心最高） |
| `test_betweenness_centrality` | 介數中心性（路徑中間節點>0） |

### 特徵值性質 (TestEigenvectorProperties)

| 測試 | 描述 |
|------|------|
| `test_clustering_coefficient` | 聚類係數（三角形=1.0） |
| `test_pagerank` | PageRank 分數（和為1） |

### 生成樹 (TestSpanningTree)

| 測試 | 描述 |
|------|------|
| `test_minimum_spanning_tree` | 最小生成樹（2條邊） |

### 二部圖 (TestBipartite)

| 測試 | 描述 |
|------|------|
| `test_is_bipartite` | 二部圖判斷（完整二部圖 K_{2,2}） |
| `test_not_bipartite` | 三角形不是二部圖 |

### 特殊圖形 (TestSpecialGraphs)

| 測試 | 描述 |
|------|------|
| `test_radius` | 圖半徑（星形圖 r=1） |
| `test_diameter` | 圖直徑（路徑圖長度3） |
| `test_density` | 圖密度（完全圖=1.0） |
| `test_number_of_nodes_edges` | 節點和邊計數 |

### 完全圖性質 (TestCompleteGraphProperties)

| 測試 | 描述 |
|------|------|
| `test_complete_graph` | K₄（4節點、6邊、密度1.0） |
| `test_cycle_graph` | C₅（5節點、5邊、連通） |
| `test_path_graph` | P₄（1個連通分量、非雙連通） |

## 測試原理 (Testing Principles)

- **鄰接矩陣**：A[i,j] = 1 表示有邊
- **拉普拉斯矩陣**：L = D - A（D為度矩陣）
- **中心性**：衡量節點在圖中重要性的指標
- **MST**：加權圖中權重最小的生成樹
- **PageRank**：基於隨機遊走的節點重要性算法