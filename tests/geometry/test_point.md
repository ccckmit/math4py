# test_point.py

## 概述 (Overview)

測試三維點（Point）類別的基本功能，包括創建、運算（加減向量）、方法（距離計算、轉向量）及相等性比較。

## 測試內容 (Test Coverage)

### 創建測試 (TestPointCreation)

| 測試 | 描述 |
|------|------|
| `test_create_point` | 創建 Point(1,2,3)，驗證 x,y,z 屬性 |
| `test_point_repr` | 驗證字串表示為 "Point(1.0, 2.0, 3.0)" |

### 運算測試 (TestPointOperations)

| 測試 | 描述 |
|------|------|
| `test_add_vector` | Point + Vector = Point（平移） |
| `test_sub_point` | Point - Point = Vector（位移向量） |
| `test_sub_vector` | Point - Vector = Point（反向平移） |

### 方法測試 (TestPointMethods)

| 測試 | 描述 |
|------|------|
| `test_distance_to` | 兩點間歐氏距離（3-4-5 三角形得距離 5） |
| `test_to_vector` | Point 轉換為 Vector（原點到該點的向量） |
| `test_equality` | 兩 Point 相等性比較 |

## 測試原理 (Testing Principles)

- **點的表示**：三維座標 (x, y, z)
- **平移運算**：Point + Vector 產生新 Point
- **位移向量**：兩 Point 相減產生連接向量
- **歐氏距離**：√((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²)