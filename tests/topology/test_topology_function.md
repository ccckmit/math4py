# test_topology_function.py

## 概述 (Overview)

測試拓撲學函數模組，包含開集、閉集、連通性、緊緻性、歐拉特徵數等。

## 測試內容 (Test Coverage)

### TestOpenSet
- `test_trivial_open`: 空集合與全集是開集
- `test_non_open`: 非開集的判定

### TestClosedSet
- `test_complement_open`: 開集的補集為閉集

### TestConnected
- `test_connected_space`: 只有平凡開集的空間是連通的
- `test_disconnected_space`: 存在非平凡既開又閉集合則不連通

### TestEulerCharacteristic
- `test_tetrahedron`: 四面體 V=4, E=6, F=4, χ=2
- `test_cube`: 立方體 V=8, E=12, F=6, χ=2

### TestCompact
- `test_finite_cover`: 有限覆蓋可提取有限子覆蓋

### TestHausdorff
- `test_distinct_points`: 不同點可由不相交開集分離

### TestClosure
- `test_closure_with_limit`: 閉包 = 集合 ∪ 極限點

### TestInterior
- `test_interior_subset`: 內部是最大開子集

### TestBoundary
- `test_boundary_empty_interior`: 內部為空時邊界等於閉包

### TestHomeomorphism
- `test_identity_map`: 恆等映射是同胚

### TestFundamentalGroup
- `test_simply_connected`: 單連通空間的基本群平凡

### TestTopologicalSort
- `test_dag_sort`: 有向無環圖的拓撲排序

## 測試原理 (Testing Principles)

- **開集**: 拓撲結構的基礎定義
- **連通性**: 空間不能分裂為兩個非空開集
- **緊緻性**: 任意開覆蓋有有限子覆蓋
- **豪斯多夫**: T2 空間中任意兩點可分離
- **歐拉特徵數**: χ = V - E + F，拓扑不變量
- **同胚**: 保持拓撲結構的雙連續雙射