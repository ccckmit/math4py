# Entropy Plotting Functions

## 概述

本模組提供資訊論相關的視覺化函數，包括熵（Entropy）和 KL 散度（KL Divergence）的長條圖。

## 數學原理

### 熵（Shannon Entropy）

```
H(P) = -Σ p_i · log(p_i)
```

- 使用不同的對數底數：
  - base=2: bits
  - base=e: nats
  - base=10: bans

### KL 散度（相對熵）

```
D_KL(P||Q) = Σ p_i · log(p_i / q_i)
```

- 非對稱：一般 D_KL(P||Q) ≠ D_KL(Q||P)
- 當 P=Q 時，D_KL = 0
- 不滿足三角不等式

## 實作細節

### 主要函數

| 函數 | 視覺化內容 |
|------|------------|
| `plot_entropy(p, base, main, ...)` | 機率分佈長條圖 + 熵值 |
| `plot_kl(p, q, base, main, ...)` | P 和 Q 並排長條圖 + KL 散度值 |

### 參數

| 參數 | 說明 |
|------|------|
| `p` | 機率分佈（會被歸一化） |
| `q` | 近似分佈 |
| `base` | 對數底數（預設 2） |
| `col`, `col1`, `col2` | 顏色 |

## 使用方式

```python
import numpy as np
from math4py.plot.rplot_entropy import plot_entropy, plot_kl

# 熵長條圖
p = [0.25, 0.25, 0.25, 0.25]  # 均勻分佈
plot_entropy(p, base=2, main="均勻分佈熵")

p = [0.5, 0.25, 0.15, 0.1]  # 非均勻
plot_entropy(p, base=2, main="非均勻分佈熵")

# KL 散度
p = [0.5, 0.5]  # 真實分佈
q = [0.6, 0.4]  # 近似分佈
plot_kl(p, q, main="KL 散度比較")

# 伯努利分佈
p_bern = [0.9, 0.1]
plot_entropy(p_bern, base=2, main="伯努利分佈 (p=0.9)")
```