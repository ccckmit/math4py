# Non-Euclidean Geometry Tests

## 概述 (Overview)

測試雙曲幾何、球面幾何、橢圓幾何的點建立、距離計算、以及核心定理。

## 測試內容 (Test Coverage)

### TestHyperbolicPoint
- `test_creation` - 雙曲點 (y > 0 上半平面)
- `test_invalid_y` - y ≤ 0 拋出錯誤

### TestSphericalPoint
- `test_creation` - 球面點 (θ, φ) 球座標
- `test_to_cartesian` - 轉換直角座標 (單位球上)
- `test_from_cartesian` - 從直角座標建立

### TestHyperbolicDistance
- `test_same_point` - 同點距離 = 0
- `test_symmetry` - d(p,q) = d(q,p)

### TestSphericalDistance
- `test_same_point` - 同點距離 = 0
- `test_antipodal` - 對蹠點距離 = π
- `test_quarter_circle` - 90° 弧距離 = π/2

### TestEllipticDistance
- `test_same_point` - 同點距離 = 0
- `test_antipodal_elliptic` - 對蹠點被識別為同點 (距離 = 0)
- `test_quarter_elliptic` - 90° 角距離 = π/2
- `test_small_angle_elliptic` - 小角度時趨近球面距離

### TestHyperbolicParallelPostulate
- `test_parallel_postulate` - 雙曲幾何中三角形內角和 < π

### TestSphericalTriangleAngleSum
- `test_spherical_exceeds_pi` - 球面三角形內角和 > π

### TestSphericalTriangleArea
- `test_area_positive` - 球面三角形面積 > 0
- `test_octant_area` - 八分圓面積 = π/2

## 測試原理 (Testing Principles)

- **雙曲幾何 (Poincaré 上半平面)**：平行公設不成立，三角形內角和 < π
- **球面幾何**：地球上大圓弧為「直線」，內角和 > π
- **橢圓幾何**：對蹠點被識別為同一點 ( projective 識別)
- **距離公式**：依幾何類型使用不同的度量公式
- **球面三角形面積**：與球面剩餘 (spherical excess) E = A+B+C-π 成正比