# 假設檢定 (Hypothesis Testing)

## 概述

本模組提供常見的統計假設檢定方法：t 檢定、Z 檢定、卡方檢定及 ANOVA。

## 數學原理

### 1. t 檢定 (t-Test)

#### 單樣本 t 檢定
$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$

其中 $s = \sqrt{\frac{1}{n-1}\sum(x_i - \bar{x})^2}$，自由度 df = n-1。

#### 兩樣本 t 檢定（獨立）
$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

自由度（Welch 近似）：
$$df = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{\frac{(s_1^2/n_1)^2}{n_1-1} + \frac{(s_2^2/n_2)^2}{n_2-1}}$$

#### 配對 t 檢定
差值 $d_i = x_i - y_i$ 的單樣本檢定：
$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$

**信賴區間**：
$$\bar{x} \pm t_{\alpha/2, df} \cdot \frac{s}{\sqrt{n}}$$

### 2. Z 檢定 (Z-Test)

已知母體標準差時：
$$z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$

**信賴區間**：
$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

### 3. 卡方檢定 (Chi-Square Test)

#### 適合度檢定
$$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$

自由度 df = k - 1（類別數減 1）。

#### 獨立性檢定
$$\chi^2 = \sum_{i=1}^{r}\sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

自由度 df = (r-1)(c-1)。

### 4. ANOVA (變異數分析)

**組間變異**：
$$SS_{between} = \sum_{i=1}^{k} n_i(\bar{x}_i - \bar{x}_{grand})^2$$

**組內變異**：
$$SS_{within} = \sum_{i=1}^{k}\sum_{j=1}^{n_i} (x_{ij} - \bar{x}_i)^2$$

**F 統計量**：
$$F = \frac{SS_{between} / (k-1)}{SS_{within} / (N-k)}$$

## 實作細節

```python
def t_test(x, y=None, mu=0, alpha=0.05, alternative="two.sided", paired=False):
    """t 檢定主函數"""
    if y is None:
        return _t_test_one_sample(x, mu, alpha, alternative)
    elif paired:
        diff = [x[i] - y[i] for i in range(len(x))]
        return _t_test_one_sample(diff, 0, alpha, alternative)
    else:
        return _t_test_two_sample(x, y, alpha, alternative)

def _t_test_one_sample(x, mu, alpha, alternative):
    n = len(x)
    x_mean = mean(x)
    x_sd = sd(x)
    se = x_sd / math.sqrt(n)
    t_stat = (x_mean - mu) / se
    df = n - 1
    
    if alternative == "two.sided":
        p_value = 2 * (1 - pt(abs(t_stat), df))
    elif alternative == "greater":
        p_value = 1 - pt(t_stat, df)
    else:
        p_value = pt(t_stat, df)
    
    # 信賴區間
    t_crit = pt(1 - alpha/2, df)
    ci = (x_mean - t_crit * se, x_mean + t_crit * se)
    
    return {"statistic": t_stat, "df": df, "p_value": p_value, 
            "estimate": x_mean, "ci": ci}

def anova(*groups):
    """單因子 ANOVA"""
    all_data = [x for g in groups for x in g]
    grand_mean = mean(all_data)
    
    ss_between = sum(len(g) * (mean(g) - grand_mean)**2 for g in groups)
    df_between = len(groups) - 1
    
    ss_within = sum(sum((x - mean(g))**2 for x in g) for g in groups)
    df_within = len(all_data) - len(groups)
    
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    f_stat = ms_between / ms_within
    
    p_value = 1 - pf(f_stat, df_between, df_within)
    
    return {"statistic": f_stat, "df1": df_between, "df2": df_within,
            "p_value": p_value, "ss_between": ss_between, "ss_within": ss_within}
```

## 使用方式

```python
from math4py.statistics.tests import t_test, z_test, chisq_test, anova

# 單樣本 t 檢定
x = [98, 102, 100, 99, 101, 97, 103, 100, 101, 99]
result = t_test(x, mu=100)
print(result["statistic"], result["p_value"])

# 兩樣本 t 檢定
group1 = [85, 90, 88, 92, 87]
group2 = [78, 82, 80, 76, 79]
result = t_test(group1, group2)
print(result["p_value"])

# 配對 t 檢定
before = [10, 12, 11, 13, 14]
after = [12, 14, 13, 15, 16]
result = t_test(before, after, paired=True)

# Z 檢定（已知母體標準差）
result = z_test(x, sigma=3, mu=100)

# 卡方檢定
observed = [[30, 10], [15, 25]]  # 2x2 列聯表
result = chisq_test(observed)

# ANOVA
result = anova(group1, group2, [90, 92, 88, 91, 89])
print(result["p_value"])
```