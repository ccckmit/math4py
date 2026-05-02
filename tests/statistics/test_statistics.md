# test_statistics.py

## 概述 (Overview)

測試統計分佈函數、描述統計與假設檢定等核心統計功能。

## 測試內容 (Test Coverage)

### TestNormalDistribution
- `test_dnorm`: 常態分布機率密度 dnorm(0,0,1) ≈ 0.3989
- `test_pnorm`: 常態分布累積分布 P(X≤0) = 0.5
- `test_qnorm`: 常態分布分位數 qnorm(0.5) = 0
- `test_rnorm`: 常態分布隨機抽樣

### TestTDistribution
- `test_dt`: t 分布密度函數
- `test_pt`: t 分布累積分布
- `test_qt`: t 分布分位數

### TestChiSquare
- `test_dchisq`: 卡方分布密度
- `test_pchisq`: 卡方分布累積分布
- `test_qchisq`: 卡方分布分位數

### TestFDistribution
- `test_df`: F 分布密度
- `test_pf`: F 分布累積分布
- `test_qf`: F 分布分位數

### TestBinomial
- `test_dbinom`: 二項分布機率質量
- `test_pbinom`: 二項分布累積分布

### TestPoisson
- `test_dpois`: Poisson 分布機率質量
- `test_ppois`: Poisson 分布累積分布

### TestDescriptiveStats
- `test_mean`: 算術平均數
- `test_median_odd/even`: 中位數（奇數/偶數個樣本）
- `test_var`: 方差
- `test_sd`: 標準差
- `test_quantile`: 分位數
- `test_summary`: 描述統計摘要

### TestTTest
- `test_t_test_one_sample`: 單一樣本 t 檢定
- `test_t_test_two_sample`: 獨立樣本 t 檢定
- `test_t_test_paired`: 配對樣本 t 檢定

### TestZTest
- `test_z_test`: 單一樣本 Z 檢定

### TestChiSquareTest
- `test_chisq_test`: 卡方獨立性檢定

### TestAnova
- `test_anova`: 單因子變異數分析

### TestConfInterval
- `test_conf_interval`: 信賴區間估計

## 測試原理 (Testing Principles)

- **機率分布**: 常態、t、卡方、F、二項、Poisson 等常見分布
- **描述統計**: 中心趨勢與散布程度度量
- **假設檢定**: 根據資料特性選擇適當檢定方法
- **信賴區間**: 基於抽樣分布的區間估計