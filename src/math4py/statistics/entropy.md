# 資訊理論 (Information Theory)

## 概述

本模組提供資訊理論的核心函數：Shannon 熵、交叉熵、KL 散度及互資訊。

## 數學原理

### 1. Shannon 熵 (Information Entropy)

**定義**：
$$H(X) = -\sum_{i} p(x_i) \log_2 p(x_i)$$

**性質**：
- $H(X) \geq 0$
- 均勻分布時最大化：$H_{\max} = \log_2 n$
- 確定分布時最小化：$H_{\min} = 0$

**常用基底**：
- Base 2：bits
- Base e：nats
- Base 10：dits

### 2. 交叉熵 (Cross-Entropy)

**定義**：
$$H(p, q) = -\sum_{i} p_i \log_2 q_i$$

**與熵的關係**：
$$H(p, q) = H(p) + D_{KL}(p \| q)$$

### 3. KL 散度 (Kullback-Leibler Divergence)

**定義**：
$$D_{KL}(p \| q) = \sum_{i} p_i \log_2 \frac{p_i}{q_i}$$

**性質**：
- 非負性：$D_{KL}(p \| q) \geq 0$
- 非對稱性：$D_{KL}(p \| q) \neq D_{KL}(q \| p)$
- 當 p = q 時，$D_{KL}(p \| q) = 0$

### 4. 互資訊 (Mutual Information)

**定義**：
$$I(X;Y) = H(X) + H(Y) - H(X,Y)$$

**等價形式**：
$$I(X;Y) = D_{KL}(P(X,Y) \| P(X)P(Y))$$

**物理意義**：觀測 Y 後對 X 不確定性的減少量。

## 實作細節

```python
def entropy(p, base=2):
    """Shannon 熵"""
    p = np.asarray(p, dtype=float)
    if not np.isclose(p.sum(), 1.0):
        p = p / p.sum()
    p = p[p > 0]  # 移除零機率（0 log 0 = 0）
    
    if base == 2:
        log = np.log2
    elif base == np.e:
        log = np.log
    else:
        log = lambda x: np.log(x) / np.log(base)
    
    return -np.sum(p * log(p))

def cross_entropy(p, q, base=2):
    """交叉熵 H(p,q)"""
    p, q = np.asarray(p), np.asarray(q)
    # 正規化
    p = p / p.sum()
    q = q / q.sum()
    # 只保留 q > 0 的項
    mask = q > 0
    return -np.sum(p[mask] * log(q[mask]))

def kl_divergence(p, q, base=2):
    """KL 散度 D(p||q)"""
    p, q = np.asarray(p), np.asarray(q)
    p, q = p / p.sum(), q / q.sum()
    mask = (p > 0) & (q > 0)
    return np.sum(p[mask] * log(p[mask] / q[mask]))

def mutual_information(joint, base=2):
    """從聯合分布計算互資訊"""
    joint = np.asarray(joint, dtype=float)
    joint = joint / joint.sum()
    
    p_x = joint.sum(axis=1)  # 邊際分布 P(X)
    p_y = joint.sum(axis=0)  # 邊際分布 P(Y)
    
    H_x = entropy(p_x, base)
    H_y = entropy(p_y, base)
    H_xy = entropy(joint.flatten(), base)
    
    return H_x + H_y - H_xy
```

## 使用方式

```python
from math4py.statistics.entropy import (
    entropy, cross_entropy, kl_divergence, mutual_information
)

# Shannon 熵
entropy([0.5, 0.5])           # 1.0 bit (硬幣)
entropy([0.25, 0.25, 0.25, 0.25])  # 2.0 bits (均勻分佈4類)
entropy([1.0, 0.0])           # 0.0 bits (確定性)

# 交叉熵
cross_entropy([0.5, 0.5], [0.5, 0.5])  # 1.0
cross_entropy([0.5, 0.5], [0.75, 0.25]) # > 1.0

# KL 散度
kl_divergence([0.5, 0.5], [0.5, 0.5])   # 0.0 (無差異)
kl_divergence([0.5, 0.5], [0.75, 0.25]) # > 0

# 互資訊
joint = [[0.25, 0.25],
          [0.25, 0.25]]  # 獨立分布
mutual_information(joint)  # ~0

joint = [[0.5, 0.0],
         [0.0, 0.5]]  # 完全相關
mutual_information(joint)  # 1.0
```