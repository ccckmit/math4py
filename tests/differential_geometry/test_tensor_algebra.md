# 張量代數測試 (test_tensor_algebra.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.differential_geometry.tensor_algebra` 模組中的張量代數功能，包括：
- 張量創建與基本運算
- 張量積與收縮
- 指標升降
- 度規張量與克羅內克 δ

## 測試內容 (Test Coverage)

### 1. 張量創建 (TestTensorCreation)
- `test_scalar_tensor`: 純量 (rank 0) 張量
- `test_vector_tensor`: 向量 (rank 1) 張量
- `test_matrix_tensor`: 矩陣 (rank 2) 張量

### 2. 張量算術 (TestTensorArithmetic)
- `test_add_same_indices`: 同指標張量相加
- `test_sub_same_indices`: 同指標張量相減
- `test_mul_scalar`: 張量標量乘法

### 3. 張量積 (TestTensorProduct)
- `test_vector_tensor_product`: 兩向量張量積為 (1,1) 型張量

### 4. 收縮 (TestContraction)
- `test_contract_matrix`: (1,1) 型張量收縮為純量 (跡)
- `test_contract_invalid_indices`: 同類指標不能收縮

### 5. 指標升降 (TestIndexRaisingLowering)
- `test_raise_index`: 協變指標升為逆變
- `test_lower_index`: 逆變指標降為協變
- `test_raise_lower_inverse`: 升降互逆

### 6. 度規張量 (TestMetricTensor)
- `test_euclidean_metric`: 歐幾里得度規 g = diag(1,1,1)
- `test_minkowski_metric`: 閔考斯基度規 g = diag(-1,1,1,1)
- `test_inverse_metric`: 度規與其逆相乘為單位矩陣

### 7. 克羅內克 δ (TestKroneckerDelta)
- `test_kronecker_delta`: δ^i_j 在 i=j 時為 1，否則為 0

## 測試原理 (Testing Principles)

- **張量秩**: (p,q) 型張量有 p 個逆變指標、q 個協變指標
- **愛因斯坦約定**: 重複指標自動求和
- **指標升降**: V^i = g^{ij} V_j, V_i = g_{ij} V^j
- **度規性質**: g_{ij} g^{jk} = δ_i^k