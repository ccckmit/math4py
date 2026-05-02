# test_matrix.py

## 概述 (Overview)

測試線性代數矩陣（Matrix）類別的功能，包括創建、矩陣運算（加法、乘法、轉置）、行列式、逆矩陣、QR 分解、奇異值分解（SVD）。

## 測試內容 (Test Coverage)

### 創建測試 (TestMatrixCreation)

| 測試 | 描述 |
|------|------|
| `test_from_list` | 從列表創建矩陣，驗證 shape=(2,2) |
| `test_eye` | 單位矩陣 I₃（對角線為1） |

### 運算測試 (TestMatrixOperations)

| 測試 | 描述 |
|------|------|
| `test_add` | 矩陣加法 A+B |
| `test_multiply` | 矩陣乘法 A@B（驗證 [0,0]=19） |
| `test_transpose` | 轉置矩陣（2×3 → 3×2） |
| `test_det` | 行列式計算 det([[1,2],[3,4]]) = -2 |
| `test_inv` | 逆矩陣 A·A⁻¹ ≈ I |

### 分解測試 (TestMatrixDecomposition)

| 測試 | 描述 |
|------|------|
| `test_qr` | QR 分解（A = QR，Q、R 均為 2×2） |
| `test_svd` | SVD 分解（返回 U, S, Vh） |

## 測試原理 (Testing Principles)

- **矩陣乘法**：C[i,j] = Σ A[i,k]·B[k,j]
- **行列式**：det(A) = ad - bc（2×2）
- **逆矩陣**：A·A⁻¹ = I
- **QR 分解**：A = QR，Q 為正交矩陣，R 為上三角
- **SVD 分解**：A = UΣVᵀ，U、V 為正交矩陣，Σ 為奇異值對角矩陣