# test_vector.py

## 概述 (Overview)

測試三維向量（Vector）類別的完整功能，包括創建、算術運算（加減乘除、負向量）、點積/叉積、範數/正規化、角度計算、平行/垂直關係判斷。

## 測試內容 (Test Coverage)

### 創建測試 (TestVectorCreation)

| 測試 | 描述 |
|------|------|
| `test_create_vector` | 創建 Vector(1,2,3)，驗證 x,y,z 屬性 |
| `test_vector_repr` | 驗證字串表示為 "Vector(1.0, 2.0, 3.0)" |

### 運算測試 (TestVectorOperations)

| 測試 | 描述 |
|------|------|
| `test_add` | 向量加法 (1,0,0)+(0,1,0)=(1,1,0) |
| `test_sub` | 向量減法 (1,1,0)-(0,1,0)=(1,0,0) |
| `test_mul` | 向量乘法（標量積） (1,2,3)*2=(2,4,6) |
| `test_rmul` | 右乘支援 2*(1,2,3)=(2,4,6) |
| `test_div` | 向量除法 (2,4,6)/2=(1,2,3) |
| `test_neg` | 負向量 (-1,-2,-3) |

### 乘積測試 (TestVectorProducts)

| 測試 | 描述 |
|------|------|
| `test_dot` | 點積 (1,0,0)·(0,1,0)=0（垂直） |
| `test_dot_nonzero` | 點積 (1,2,3)·(1,1,1)=6 |
| `test_cross` | 叉積 (1,0,0)×(0,1,0)=(0,0,1)（右手定則） |
| `test_cross_parallel` | 平行向量叉積為零向量 |

### 度量測試 (TestVectorMetrics)

| 測試 | 描述 |
|------|------|
| `test_norm` | 範數/長度 \| (3,4,0) \|=5 |
| `test_normalize` | 正規化後長度為1 |
| `test_normalize_zero_error` | 零向量正規化拋出 ValueError |
| `test_angle` | 夾角計算 (1,0,0) 與 (0,1,0) 夾角為 π/2 |

### 關係測試 (TestVectorRelations)

| 測試 | 描述 |
|------|------|
| `test_parallel` | 平行向量判斷 |
| `test_perpendicular` | 垂直向量判斷 |
| `test_equality` | 向量相等性比較 |

## 測試原理 (Testing Principles)

- **點積**：a·b = |a||b|cos(θ)，可用於判斷垂直（a·b=0）
- **叉積**：a×b 垂直於 a 和 b，模長為 |a||b|sin(θ)
- **範數**：||v|| = √(v·v)
- **正規化**：v/||v|| 產生單位向量
- **平行**：叉積為零向量
- **垂直**：點積為零