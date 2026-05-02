# test_line.py

## 概述 (Overview)

測試三維直線（Line3D）類別的功能，包括創建、點投影、距離計算、平行/垂直關係判斷等。

## 測試內容 (Test Coverage)

### 創建測試 (TestLineCreation)

| 測試 | 描述 |
|------|------|
| `test_create_line` | 由點和方向向量創建直線，驗證方向向量正規化 |
| `test_from_points` | 由兩點創建直線，驗證方向向量計算 |

### 方法測試 (TestLineMethods)

| 測試 | 描述 |
|------|------|
| `test_point_at` | 直線上參數化點計算（t=5 時得 Point(5,0,0)） |
| `test_distance_to_point` | 點到直線的垂直距離 |
| `test_closest_point` | 直線上最近的點（垂足） |

### 關係測試 (TestLineRelations)

| 測試 | 描述 |
|------|------|
| `test_is_parallel` | 平行線判斷（方向向量相同） |
| `test_is_perpendicular` | 垂直線判斷（方向向量點積為0） |

## 測試原理 (Testing Principles)

- **直線表示**：以一個起始點 Point 和方向 Vector 定義
- **參數化**：直線上的點可表示為 P = P₀ + t·d
- **距離計算**：使用向量投影公式求點到直線距離
- **平行/垂直**：通過方向向量的點積和叉積判斷