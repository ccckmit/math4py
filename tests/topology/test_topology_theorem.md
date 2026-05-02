# test_topology_theorem.py

## 概述 (Overview)

測試拓撲學定理，包含歐拉特徵數定理、豪斯多夫分離性、海涅-龐萊緊緻性等。

## 測試內容 (Test Coverage)

### TestEulerCharacteristicTheorem
- `test_sphere`: 球面 V=4, E=6, F=4, χ=2（g=0）
- `test_torus`: 環面 χ = 2 - 2g = 0（g=1）

### TestHausdorffSeparation
- `test_distinct_points`: 離散度量空間滿足豪斯多夫

### TestCompactnessHeineBorel
- `test_closed_bounded_compact`: 閉且有界 ⇒ 緊緻（Rn）
- `test_not_closed_not_compact`: 不閉則不緊緻

### TestConnectednessContinuum
- `test_path_connected_implies_connected`: 道路連通 ⇒ 連通
- `test_connected_not_path_connected`: 連通未必道路連通

### TestHomeomorphismInvariance
- `test_linear_map`: 同胚保持拓撲性質不變

### TestUreyLefschetzFixedPoint
- `test_sphere_map`: 球面映射的不動點定理

### TestBrouwerFixedPoint
- `test_dimension_zero`: 0 維空間必有不动点
- `test_positive_dimension`: 正維數封閉單位球映射有不动点

## 測試原理 (Testing Principles)

- **歐拉-龐加萊公式**: χ = Σ (-1)^i rank(H_i)，同胚不變量
- **海涅-龐萊定理**: Rn 中集合緊緻 ⟺ 閉且有界
- **Brouwer 不動點定理**: 單位球到自身的連續映射必有不动点
- **道路連通**: 存在連續路徑連接任意兩點
- **同倫與基本群**: 空間的代數描述工具