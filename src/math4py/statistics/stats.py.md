# 描述統計 (Descriptive Statistics)

## 概述

本模組提供純 Python 實現的描述統計函數，不依賴 numpy，用於基本資料分析。

## 數學原理

### 1. 集中趨勢

**平均值 (Mean)**
$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**中位數 (Median)**
- 排序後取值：`sorted(x)[n//2]`
- 偶數個時取兩中點平均

### 2. 變異數與標準差

**樣本變異數**：
$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

**標準差**：
$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

### 3. 共變異數與相關係數

**共變異數**：
$$\text{Cov}(X,Y) = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

**Pearson 相關係數**：
$$r = \frac{\text{Cov}(X,Y)}{s_X \cdot s_Y}$$

### 4. 分位數 (Quantile)

使用線性插值法計算：
$$Q_p = (1 - \delta) \cdot x_{\lfloor m \rfloor} + \delta \cdot x_{\lceil m \rceil}$$

其中 $m = p(n-1)$，$\delta = m - \lfloor m \rfloor$

## 實作細節

```python
def mean(x):
    return sum(x) / len(x)

def median(x):
    s = sorted(x)
    n = len(s)
    if n % 2 == 0:
        return (s[n//2 - 1] + s[n//2]) / 2
    return s[n//2]

def var(x, ddof=1):
    m = mean(x)
    return sum((xi - m)**2 for xi in x) / (len(x) - ddof)

def quantile(x, p):
    s = sorted(x)
    idx = p * (len(s) - 1)
    lo, hi = int(math.floor(idx)), int(math.ceil(idx))
    if lo == hi:
        return s[lo]
    return s[lo] * (hi - idx) + s[hi] * (idx - lo)
```

## 使用方式

```python
from math4py.statistics.stats import (
    mean, median, var, sd, cov, cor, quantile, summary
)

data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

mean(data)        # 11.0
median(data)      # 11.0
var(data)         # 36.67 (樣本變異數)
sd(data)          # 6.06
quantile(data, 0.25)  # 6.5
quantile(data, 0.75)  # 15.5

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
cov(x, y)         # 2.0
cor(x, y)         # 0.878

summary(data)     # 完整統計摘要
```