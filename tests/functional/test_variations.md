# 變分法測試 (test_variations.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.functional.variations` 模組中的變分法函數，包括：
- 最短路徑長度
- 平面測地線
- 最速降線時間
- 歐拉-拉格朗日方程

## 測試內容 (Test Coverage)

### 1. 最短路徑長度 (TestShortestPathLength)
- `test_straight_line_length`: 直線 y = x 長度為 √2
- `test_horizontal_line_length`: 水平線 y = 2 長度為 b-a

### 2. 平面測地線 (TestGeodesicPlane)
- `test_geodesic_straight_line`: 平面上最短路徑是直線

### 3. 最速降線時間 (TestBrachistochroneTime)
- `test_vertical_drop_time`: 垂直下落時間為 √(2h/g)

### 4. 歐拉-拉格朗日方程 (TestEulerLagrangeSimple)
- `test_constant_derivative`: y = x, y' = 1, y'' = 0
- `test_linear_derivative`: y = x², y' = 2x, y'' = 2

## 測試原理 (Testing Principles)

- **弧長公式**: L = ∫ √(1 + y'²) dx
- **測地線**: 曲面上的最短路徑
- **最速降線**: 使得質點從 A 到 B 時間最短的曲線
- **歐拉-拉格朗日**: d/dx(∂L/∂y') - ∂L/∂y = 0