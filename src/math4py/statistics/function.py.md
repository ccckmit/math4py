# 統計函數 (Statistics Function)

## 概述

本模組提供描述統計、機率分布計算、假設檢定輔助函數等基本統計運算工具。

## 數學原理

### 1. 集中趨勢量數

**算術平均數 (Arithmetic Mean)**
$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**中位數 (Median)**
- 將資料排序後，取中間值
- n 為奇數：中間值為第 `(n+1)/2` 個
- n 為偶數：中間值為第 `n/2` 和 `n/2 + 1` 個的平均

### 2. 離散趨勢量數

**變異數 (Variance)**
$$\sigma^2 = \frac{1}{n - \text{ddof}}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

其中 ddof 為自由度調整（樣本變異數取 ddof=1）。

**標準差 (Standard Deviation)**
$$\sigma = \sqrt{\sigma^2}$$

**四分位距 (IQR)**
$$\text{IQR} = Q_{0.75} - Q_{0.25}$$

### 3. 關聯量數

**共變異數 (Covariance)**
$$\text{Cov}(X,Y) = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

**Pearson 相關係數**
$$r = \frac{\text{Cov}(X,Y)}{\sigma_X \cdot \sigma_Y} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \cdot \sum(y_i - \bar{y})^2}}$$

### 4. Z-Score 標準化
$$z = \frac{x - \mu}{\sigma}$$

標準化後的資料均值為 0，標準差為 1。

### 5. Bootstrap 信賴區間
從原始資料中有放回抽樣 n_bootstrap 次，計算統計量的分位數：
$$[\alpha/2, 1-\alpha/2]$$

### 6. 模型選擇準則

**AIC (Akaike Information Criterion)**
$$\text{AIC} = 2k - 2\ln(\hat{L})$$

**BIC (Bayesian Information Criterion)**
$$\text{BIC} = k\ln(n) - 2\ln(\hat{L})$$

其中 k 為參數數目，n 為樣本數。

## 實作細節

### 核心函數

```python
def mean(x: List[float]) -> float:
    return np.mean(x)

def variance(x: List[float], ddof: int = 1) -> float:
    return np.var(x, ddof=ddof)

def covariance(x: List[float], y: List[float], ddof: int = 1) -> float:
    return np.cov(x, y, ddof=ddof)[0, 1]

def correlation(x: List[float], y: List[float]) -> float:
    return np.corrcoef(x, y)[0, 1]
```

### Bootstrap CI
```python
def bootstrap_ci(x, statistic_fn, n_bootstrap=1000, alpha=0.05):
    stats = [statistic_fn(np.random.choice(x, size=len(x), replace=True)) 
             for _ in range(n_bootstrap)]
    lower = np.quantile(stats, alpha / 2)
    upper = np.quantile(stats, 1 - alpha / 2)
    return lower, upper
```

## 使用方式

```python
from math4py.statistics import function as stats

# 基本統計量
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats.mean(data)          # 5.5
stats.variance(data)      # 9.1667 (樣本變異數)
stats.std(data)           # 3.027 (樣本標準差)

# 關聯量數
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
stats.covariance(x, y)    # 共變異數
stats.correlation(x, y)  # Pearson r

# Bootstrap 信賴區間
stats.bootstrap_ci(data, np.mean, n_bootstrap=1000)
```