# 張量代數（Tensor Algebra）

## 概述

本模組提供帶指標標記的張量類別，支援協變（下標）與逆變（上標）指標的張量運算，包括張量積、縮併、指標升降等。

## 數學原理

### 張量基礎

1. **張量階數**：指標的數量
   - (r, s) 型張量：r 個逆變指標、s 個協變指標
   - 形狀 = (dim, dim, ..., dim)

2. **張量積**：
   ```
   (T ⊗ S)^{i_1...i_r j_1...j_s}_{k_1...k_t l_1...l_u} = T^{i_1...i_r}_{k_1...k_t} S^{j_1...j_s}_{l_1...l_u}
   ```

3. **縮併**：上標與下標配對求和
   ```
   contraction_{i}(T^{i}_{j}) = Σ_i T^{i}_{j}
   ```

4. **指標升降**（用度規張量）：
   ```
   A^μ = g^{μν} A_ν    (昇指標)
   A_μ = g_{μν} A^ν    (降指標)
   ```

5. **Kronecker Delta**：
   ```
   δ^μ_ν = 1 if μ = ν, else 0
   ```

## 實作細節

### Tensor 類別

| 方法 | 數學運算 |
|------|----------|
| `tensor_product(other)` | 張量積 T ⊗ S |
| `contract(index1, index2)` | 縮併（上標與下標配對） |
| `raise_index(index, metric)` | g^{μν} 昇指標 |
| `lower_index(index, metric)` | g_{μν} 降指標 |
| `trace()` | (1,1) 型張量跡 |

### 指標約定

- `'u'`: 逆變指標（上標）
- `'d'`: 協變指標（下標）

### 便捷函數

| 函數 | 說明 |
|------|------|
| `metric_tensor(dim, signature)` | 建立度規張量（歐氏或閔可夫斯基） |
| `inverse_metric(g)` | 逆度規 g^{μν} |
| `kronecker_delta(dim)` | δ^μ_ν |

## 使用方式

```python
import numpy as np
from math4py.differential_geometry.tensor_algebra import (
    Tensor, tensor_product, contract,
    raise_index, lower_index, metric_tensor
)

# 建立 (1,1) 型張量
T = Tensor([[1, 2], [3, 4]], indices=['u', 'd'], dim=2)

# 張量積：與另一個 (0,1) 型張量
S = Tensor([1, 0], indices=['d'], dim=2)
result = T.tensor_product(S)  # (1,2) 型

# 縮併：contract(0, 1) 對第 0 和第 1 指標
result = T.contract(0, 1)  # 跡 = 1 + 4 = 5

# 指標升降
g = metric_tensor(2, "euclidean")
g_inv = np.linalg.inv(g)

A = Tensor([1, 2], indices=['d'], dim=2)  # 協變
A_raised = raise_index(A, 0, g_inv)  # 逆變

# 度規張量
g_2d = metric_tensor(2, "euclidean")  # [[1,0],[0,1]]
g_minkowski = metric_tensor(4, "minkowski")  # diag(-1,1,1,1)
```