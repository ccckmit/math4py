# test_vector.py

## 概述 (Overview)

測試線性代數向量函數模組，包括向量範數（norm）、點積（dot product）、叉積（cross product）的計算。

## 測試內容 (Test Coverage)

### 範數測試 (TestNormVector)

| 測試 | 描述 |
|------|------|
| `test_2d_vector` | 2D 向量範數 \| (3,4) \| = 5 |
| `test_zero_vector` | 零向量範數 = 0 |

### 點積測試 (TestDotProduct)

| 測試 | 描述 |
|------|------|
| `test_orthogonal` | 正交向量 (1,0)·(0,1) = 0 |
| `test_parallel` | 平行向量 (2,0)·(3,0) = 6 |

### 叉積測試 (TestCrossProduct)

| 測試 | 描述 |
|------|------|
| `test_standard_basis` | 標準基向量 i×j = k：(1,0,0)×(0,1,0)=(0,0,1) |

## 測試原理 (Testing Principles)

- **向量範數**：\|\|v\|\| = √(v₁² + v₂² + ... + vₙ²)，2D 為 √(x² + y²)
- **點積**：a·b = Σ aᵢbᵢ = |a||b|cos(θ)
  - 正交 → 點積 = 0
  - 平行同向 → 點積 = |a||b|
- **叉積**（3D）：a×b 垂直於 a 和 b，遵循右手定則
  - i×j = k, j×k = i, k×i = j
  - 平行向量 → 叉積 = 0