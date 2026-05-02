# 微分幾何函數測試 (test_diff_geo_function.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.differential_geometry.function` 模組中的微分幾何計算函數，包括：
- 克里斯托費爾符號
- 黎曼曲率張量
- 里奇張量與純量曲率
- 測地線方程
- 球面度量與測地線距離

## 測試內容 (Test Coverage)

### 1. 克里斯托費爾符號 (TestChristoffelSymbols)
- `test_flat_metric_zero`: 平坦度量 Γ = 0
- `test_nonflat_metric`: 非平坦度量 Γ ≠ 0

### 2. 黎曼曲率張量 (TestRiemannCurvatureTensor)
- `test_flat_space_zero`: 平坦空間 R = 0

### 3. 里奇張量 (TestRicciTensor)
- `test_flat_space_zero`: 平坦空間 Ric = 0

### 4. 純量曲率 (TestScalarCurvature)
- `test_flat_space_zero`: 平坦空間 R = 0

### 5. 測地線方程 (TestGeodesicEquation)
- `test_straight_line`: 平坦空間測地線為直線

### 6. 列維-奇維塔聯絡 (TestLeviCivitaConnection)
- `test_flat_metric`: 平坦度量聯絡為零

### 7. 李導數 (TestLieDerivative)
- `test_lie_derivative_zero`: 相同向量場導數為零

### 8. 協變導數 (TestCovariantDerivative)
- `test_flat_space`: 平坦空間協變導數為普通導數

### 9. 球面度量張量 (TestMetricTensorSphere)
- `test_sphere_metric_shape`: 形狀正確 (2×2)
- `test_sphere_metric_diagonal`: 球面度量为對角矩陣

### 10. 球面測地線距離 (TestGeodesicDistanceSphere)
- `test_distance_identity`: 同點距離為 0
- `test_distance_antipodal`: 對拓點距離為 πR

## 測試原理 (Testing Principles)

- **克里斯托費爾符號**: Γ^k_{ij} = ½ g^{kl}(∂_i g_{jl} + ∂_j g_{il} - ∂_l g_{ij})
- **黎曼曲率**: R^i_{jkl} 表曲率反對稱性
- **測地線**: d²x^i/dτ² + Γ^i_{jk} dx^j/dτ dx^k/dτ = 0
- **球面距離**: 大圓弧長度公式