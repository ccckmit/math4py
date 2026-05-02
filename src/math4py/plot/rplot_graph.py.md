# Graph Plotting Functions

## 概述

本模組提供網絡圖（Graph）的視覺化功能，基於 networkx 和 matplotlib，支援不同圖類型和圖論性質的可視化。

## 數學原理

### 圖論基礎

1. **圖的表示**：
   - 鄰接矩陣 A[i,j] = 1 若 (i,j) 是邊
   - 拉普拉斯矩陣 L = D - A（D 為度矩陣）

2. **中心性指標**：
   - 度中心性：節點度數 / (n-1)
   - 介數中心性：經過節點的最短路徑比例
   - 接近中心性：倒數平均路徑長
   - 特徵向量中心性：鄰接矩陣主特徵向量

3. **圖布局演算法**：
   - Spring layout：彈簧模型
   - Spectral layout：譜方法
   - Shell layout：層次結構

## 實作細節

### 主要函數

| 函數 | 視覺化內容 |
|------|------------|
| `plot_graph(G, pos, ...)` | 無向圖 |
| `plot_directed_graph(G, pos, ...)` | 有向圖（帶箭頭） |
| `plot_weighted_graph(G, pos, ...)` | 加權圖（顯示權重） |
| `plot_graph_properties(G, centrality, ...)` | 中心性著色圖 |
| `plot_degree_distribution(G, ...)` | 度分布直方圖 |
| `plot_adjacency_heatmap(G, ...)` | 鄰接矩陣熱圖 |
| `plot_laplacian_heatmap(G, ...)` | 拉普拉斯矩陣熱圖 |
| `plot_spectral_embedding(G, ...)` | 譜嵌入圖 |
| `plot_shell(G, ...)` | 殼層布局圖 |

### 中心性類型

- `"degree"`: 度中心性
- `"betweenness"`: 介數中心性
- `"closeness"`: 接近中心性
- `"eigenvector"`: 特徵向量中心性

## 使用方式

```python
import networkx as nx
from math4py.plot.rplot_graph import (
    plot_graph, plot_directed_graph, plot_weighted_graph,
    plot_degree_distribution, plot_adjacency_heatmap
)

# 建立圖
G = nx.Graph()
G.add_edges_from([(0,1), (1,2), (2,0), (2,3)])

# 基本圖
plot_graph(G, filename="out/graph.pdf")

# 有向圖
DG = nx.DiGraph()
DG.add_edges_from([(0,1), (1,2), (2,0)])
plot_directed_graph(DG, filename="out/digraph.pdf")

# 加權圖
WG = nx.Graph()
WG.add_edge(0, 1, weight=0.5)
WG.add_edge(1, 2, weight=1.5)
plot_weighted_graph(WG, filename="out/weighted.pdf", show_weights=True)

# 度分布
plot_degree_distribution(G, filename="out/degree_hist.pdf")

# 鄰接矩陣熱圖
plot_adjacency_heatmap(G, filename="out/adjacency.pdf")

# 中心性著色圖
plot_graph_properties(G, centrality="betweenness", filename="out/centrality.pdf")
```