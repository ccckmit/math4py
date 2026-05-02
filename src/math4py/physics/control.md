# 控制理論 (Control Theory)

## 概述

控制理論模組提供控制系統基礎計算函數，包括傳遞函數、Routh-Hurwitz 穩定性判據、能控性矩陣等。

## 數學原理

### 1. 傳遞函數
$$G(s) = \frac{N(s)}{D(s)}$$

線性時不變系統輸入輸出的拉普拉斯轉換比。

### 2. Routh-Hurwitz 穩定性判據

系統穩定的必要條件：特徵多項式所有根的實部為負。
$$D(s) = a_n s^n + a_{n-1} s^{n-1} + \cdots + a_0$$

### 3. 能控性矩陣
$$Q_c = [B, AB, A^2B, \ldots, A^{n-1}B]$$

$n \times nm$ 矩陣，系統能控的充要條件是 $Q_c$ 秩為 $n$。

## 實作細節

### 關鍵函數

| 函數 | 功能 |
|------|------|
| `transfer_function()` | 建立傳遞函數結構 |
| `routh_hurwitz()` | 檢查系統穩定性 |
| `controllability_matrix()` | 計算能控性矩陣 |

## 使用方式

```python
from math4py.physics.control import *
import numpy as np

# 傳遞函數
G = transfer_function(num=[1, 2], den=[1, 3, 2])

# Routh-Hurwitz 穩定性
char_poly = [1, 2, 3, 2]  # s³ + 2s² + 3s + 2
stable = routh_hurwitz(char_poly)

# 能控性矩陣
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
Qc = controllability_matrix(A, B)
```