# 統計定理 (Statistics Theorems)

## 概述

本模組驗證統計學中的重要極限定理、不等式及資訊理論基礎，透過數值模擬確認這些定理的正確性。

## 數學原理

### 1. 中央極限定理 (Central Limit Theorem, CLT)

**定理**：當樣本數 n 夠大時，樣本平均數的分布收斂至常態分布：
$$\bar{X}_n \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

**驗證方法**：
- 產生 n_samples 組，每組 n 個樣本
- 計算每組的樣本平均數
- 比較觀察到的均值與理論均值、標準誤

### 2. 大數定律 (Law of Large Numbers, LLN)

**弱大數定律**：樣本平均數依概率收斂至真實均值：
$$\bar{X}_n \xrightarrow{P} \mu \quad \text{as } n \to \infty$$

### 3. Chebyshev 不等式

**定理**：對於任意隨機變數 X：
$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$

### 4. Markov 不等式

**定理**：若 X 為非負隨機變數：
$$P(X \geq k) \leq \frac{E[X]}{k}, \quad k > 0$$

### 5. 貝氏定理 (Bayes' Theorem)

**公式**：
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

### 6. Cramér-Rao 下界 (CRLB)

**定理**：對無偏估計量 $\hat{\theta}$：
$$\text{Var}(\hat{\theta}) \geq \frac{1}{n \cdot I(\theta)}$$

其中 $I(\theta)$ 為 Fisher 資訊量。

### 7. 資訊熵 (Information Entropy)

**Shannon 熵**：
$$H(X) = -\sum_{i} p(x_i) \log_2 p(x_i)$$

**互資訊 (Mutual Information)**：
$$I(X;Y) = H(X) + H(Y) - H(X,Y)$$

### 8. 二項分布 (Binomial Distribution)

**機率質量函數**：
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

**常態近似**：當 n 夠大時，$X \approx N(np, np(1-p))$

**卜瓦松近似**：當 n → ∞, p → 0 且 np = λ 時，$X \approx \text{Poisson}(\lambda)$

## 實作細節

### CLT 驗證
```python
def central_limit_theorem(sample_fn, true_mean, true_var, n, n_samples=1000):
    sample_means = [np.mean(sample_fn(n)) for _ in range(n_samples)]
    expected_se = np.sqrt(true_var / n)
    observed_se = np.std(sample_means)
    # 驗證均值誤差不超過 10%，標準誤誤差不超過 20%
    return {"pass": mean_error < threshold, ...}
```

### 熵計算
```python
def information_entropy(p, base=2.0):
    p = np.array(p, dtype=float)
    p = p[p > 0]  # 移除零機率
    entropy = -np.sum(p * np.log(p) / np.log(base))
    return {"entropy": entropy}
```

### 互資訊
```python
def mutual_information(x, y):
    px = x / x.sum()
    py = y / y.sum()
    h_x = -np.sum(px[px > 0] * np.log(px[px > 0]))
    h_y = -np.sum(py[py > 0] * np.log(py[py > 0]))
    mi = h_x + h_y  # 簡化版，未完全計算 H(X,Y)
    return {"mi": mi, "h_x": h_x, "h_y": h_y}
```

## 使用方式

```python
from math4py.statistics.theorem import (
    central_limit_theorem, law_of_large_numbers,
    chebyshev_inequality, chebyshev_verify,
    bayes_theorem, information_entropy
)

# 驗證中央極限定理
import numpy as np
sample_fn = lambda n: np.random.exponential(2, n)
result = central_limit_theorem(sample_fn, true_mean=2, true_var=4, n=30)
print(result["pass"])

# 貝氏定理
result = bayes_theorem(p_a=0.01, p_b_given_a=0.9, p_b=0.1)
print(result["posterior"])

# 資訊熵
result = information_entropy([0.5, 0.25, 0.25])
print(result["entropy"])  # 1.5 bits
```