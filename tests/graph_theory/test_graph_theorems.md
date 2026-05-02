# test_graph_theorems.py

## 概述 (Overview)

測試圖論定理模組，驗證歐拉路徑、漢密爾頓路徑、四色定理、握手引理、尤拉特徵數、樹定理、基爾霍夫定理、平面圖定理、布魯克斯定理、拉姆齊定理、Prim 最小生成樹定理、最大流最小割定理、二部圖定理等。

## 測試內容 (Test Coverage)

| 定理 | 測試內容 |
|------|----------|
| `test_eulerian_path_theorem_valid` | 零個奇度頂點 → 有歐拉回路 |
| `test_eulerian_path_theorem_two_odd` | 兩個奇度頂點 → 有歐拉路徑 |
| `test_eulerian_path_theorem_invalid` | 四個奇度頂點 → 無歐拉路徑 |
| `test_hamiltonian_path_theorem_sufficient` | 最小度≥3 → 存在漢密爾頓路徑（充分條件） |
| `test_hamiltonian_path_theorem_insufficient` | 最小度=1 → 不存在漢密爾頓路徑 |
| `test_four_color_theorem` | 平面地圖可用四色著色 |
| `test_handshaking_lemma` | 度數總和 = 2×邊數（握手引理） |
| `test_euler_characteristic_cube` | 立方體 V=8, E=12, F=6, χ=2 |
| `test_tree_theorem_valid` | 樹：V-1 = E |
| `test_tree_theorem_invalid` | 5頂點6邊 → 不是樹 |
| `test_kirchhoff_theorem` | 圖的生成樹數量（矩陣樹定理） |
| `test_planar_graph_theorem` | 平面圖相關定理 |
| `test_brooks_theorem` | 連通圖的色數≤最大度（除非是完全圖或奇環） |
| `test_ramsey_theorem` | 拉姆齊數相關定理 |
| `test_mst_prim_theorem` | Prim 算法的最小生成樹定理 |
| `test_max_flow_min_cut_theorem` | 最大流 = 最小割 |
| `test_bipartite_graph_theorem` | 二部圖判定定理 |

## 測試原理 (Testing Principles)

- **歐拉路徑**：奇度頂點數為0（有回路）或2（有路徑）
- **漢密爾頓路徑**：經過每個頂點恰好一次
- **握手引理**：∑deg(v) = 2|E|
- **尤拉特徵數**：χ = V - E + F（凸多面體為2）
- **樹的性質**：連通無圈 → E = V - 1
- **二部圖**：無奇環的圖