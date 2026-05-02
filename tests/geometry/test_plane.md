# test_plane.py

## 概述 (Overview)

測試三維平面（Plane3D）類別的功能，包括創建、點包含判斷、距離計算、投影、直線交點、平面關係等。

## 測試內容 (Test Coverage)

### 創建測試 (TestPlaneCreation)

| 測試 | 描述 |
|------|------|
| `test_create_plane` | 由點和法向量創建平面，驗證法向量正規化 |
| `test_from_points` | 由三點創建平面，驗證法向量計算（結果為 (0,0,1)） |

### 方法測試 (TestPlaneMethods)

| 測試 | 描述 |
|------|------|
| `test_contains_point` | 點是否在平面上的判斷 |
| `test_distance_to_point` | 點到平面的垂直距離 |
| `test_project_point` | 點在平面上的投影 |
| `test_line_intersection` | 直線與平面的交點計算 |

### 關係測試 (TestPlaneRelations)

| 測試 | 描述 |
|------|------|
| `test_is_parallel` | 兩平面平行（法向量平行） |
| `test_is_perpendicular` | 兩平面垂直（法向量垂直） |

## 測試原理 (Testing Principles)

- **平面表示**：以一個起始點 Point 和法向量 Normal 定義
- **點在平面上**：將點代入平面方程驗證
- **距離計算**：|ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²)
- **投影**：沿法向量方向映射點到平面
- **線面交點**：參數化直線代入平面方程求解 t