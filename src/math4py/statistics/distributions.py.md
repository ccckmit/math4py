# 機率分布 (Probability Distributions)

## 概述

本模組提供常用機率分布的機率密度函數/機率質量函數、累積分布函數、分位數函數及隨機變數生成器，採用 R 風格的命名慣例。

## 數學原理

### 1. 常態分布 (Normal Distribution)

**PDF**：
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

**CDF**：
$$\Phi(x) = \int_{-\infty}^{x} f(t) dt$$

### 2. 學生 t 分布 (Student's t Distribution)

**PDF**：
$$f(t) = \frac{\Gamma((df+1)/2)}{\sqrt{df\pi}\,\Gamma(df/2)}\left(1+\frac{t^2}{df}\right)^{-(df+1)/2}$$

當樣本數較小時用於估計均值信賴區間。

### 3. 卡方分布 (Chi-Square Distribution)

**PDF**：
$$f(x) = \frac{x^{df/2-1} e^{-x/2}}{2^{df/2} \Gamma(df/2)}$$

用於變異數估計及類別資料分析。

### 4. F 分布

兩個卡方分布的比值：
$$F = \frac{\chi^2_1 / df_1}{\chi^2_2 / df_2}$$

用於變異數分析 (ANOVA)。

### 5. 二項分布 (Binomial Distribution)

**PMF**：
$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

### 6. 卜瓦松分布 (Poisson Distribution)

**PMF**：
$$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

## 函數命名慣例

| 前綴 | 意義 |
|------|------|
| `d` | 機率密度/質量函數 (PDF/PMF) |
| `p` | 累積分布函數 (CDF) |
| `q` | 分位數函數 (Quantile,  inverse CDF) |
| `r` | 隨機變數生成 (Random) |

## 實作細節

```python
from scipy.stats import norm, t, chi2, f, binom, poisson

# 常態分布
def dnorm(x, mean=0, sd=1):
    return norm.pdf(x, loc=mean, scale=sd)

def pnorm(q, mean=0, sd=1, lower_tail=True):
    p = norm.cdf(q, loc=mean, scale=sd)
    return p if lower_tail else 1 - p

def qnorm(p, mean=0, sd=1, lower_tail=True):
    if not lower_tail: p = 1 - p
    return norm.ppf(p, loc=mean, scale=sd)

def rnorm(n, mean=0, sd=1):
    return list(norm.rvs(loc=mean, scale=sd, size=n))
```

## 使用方式

```python
from math4py.statistics import distributions as dist

# 常態分布
dist.dnorm(0)           # PDF at x=0, μ=0, σ=1 → 0.3989
dist.pnorm(0)           # CDF at x=0 → 0.5
dist.qnorm(0.975)       # 97.5th percentile → 1.96
dist.rnorm(5)           # 5 random samples

# t 分布
dist.dt(2.0, df=10)     # PDF at t=2, df=10
dist.pt(2.0, df=10)     # CDF
dist.qt(0.975, df=10)   # 分位數

# 卡方分布
dist.dchisq(5, df=3)    # PDF at x=5, df=3
dist.pchisq(5, df=3)    # CDF

# F 分布
dist.df(2.5, df1=5, df2=10)
dist.pf(2.5, df1=5, df2=10)

# 二項分布 (n=10, p=0.5)
dist.dbinom(5, 10, 0.5)  # P(X=5)
dist.pbinom(5, 10, 0.5)  # P(X≤5)

# 卜瓦松分布 (λ=3)
dist.dpois(3, 3)        # P(X=3)
dist.ppois(3, 3)        # P(X≤3)
```