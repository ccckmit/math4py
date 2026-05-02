# test_la_theorems.py

## 概述 (Overview)

測試線性代數定理模組，驗證秩-零化度定理、特徵值定理、奇異值分解（SVD）定理、行列式定理、線性獨立性定理。

## 測試內容 (Test Coverage)

### 秩-零化度定理 (TestRankNullity)

| 測試 | 描述 |
|------|------|
| `test_full_rank_square` | 滿秩方陣（單位矩陣，rank=2） |
| `test_rank_deficient` | 秩虧缺矩陣（rank=1, nullity=1） |

### 特徵值定理 (TestEigenvalues)

| 測試 | 描述 |
|------|------|
| `test_diagonal_matrix` | 對角矩陣特徵值為對角元素 |
| `test_identity` | 單位矩陣 trace=2, det=1 |

### SVD 定理 (TestSVD)

| 測試 | 描述 |
|------|------|
| `test_reconstruction` | SVD 重構誤差 < 1e-8 |

### 行列式定理 (TestDeterminant)

| 測試 | 描述 |
|------|------|
| `test_det_product` | det(AB) = det(A)det(B) |

### 線性獨立性 (TestLinearIndependence)

| 測試 | 描述 |
|------|------|
| `test_independent` | 線性無關向量（單位向量） |
| `test_dependent` | 線性相關向量（[1,2] 與 [2,4]） |

## 測試原理 (Testing Principles)

- **秩-零化度定理**：rank(A) + nullity(A) = n（列數）
- **特徵值之和（trace）**：等於對角線元素之和
- **特徵值之積（det）**：等於行列式
- **SVD 重構**：A = UΣVᵀ，重構後誤差應極小
- **行列式乘法**：det(AB) = det(A) · det(B)
- **線性獨立**：不存在不全為零的係數使得 c₁v₁ + ... + cₙvₙ = 0