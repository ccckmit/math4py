# test_statistics_theorems.py

## 概述 (Overview)

測試統計學核心定理的數值驗證，包含中央極限定理、大數定律、機率不等式等。

## 測試內容 (Test Coverage)

### TestCentralLimitTheorem
- `test_clt_normal`: 常態分布樣本均值趨近常態分布
- `test_clt_uniform`: 均勻分布樣本均值趨近常態分布
- `test_clt_exponential`: 指數分布樣本均值趨近常態分布

### TestLawOfLargeNumbers
- `test_lln_normal`: 常態分布的大數定律
- `test_lln_uniform`: 均勻分布的大數定律

### TestChebyshev
- `test_chebyshev_bound`: Chebyshev 不等式 P(|X-μ|≥kσ) ≤ 1/k²
- `test_chebyshev_verify`: 透過抽樣驗證 Chebyshev 界

### TestMarkov
- `test_markov_verify`: Markov 不等式驗證（非負變數）

### TestBernoulli
- `test_bernoulli`: Bernoulli 試驗機率計算
- `test_bernoulli_verify`: 大量 Bernoulli 試驗驗證

### TestBayes
- `test_bayes`: 貝氏定理 P(A|B) = P(B|A)P(A)/P(B)
- `test_bayes_verify`: 多重假設的貝氏更新驗證

### TestCRLB
- `test_crlb`: Cramér-Rao 下界 Var(θ̂) ≥ 1/(n·I(θ))

### TestEntropy
- `test_entropy`: 資訊熵計算
- `test_entropy_verify`: 熵的範圍驗證 0 ≤ H ≤ log(n)

### TestMutualInformation
- `test_mutual_information`: 互資訊計算

## 測試原理 (Testing Principles)

- **中央極限定理**: 大量獨立同分布隨機變數的樣本均值趨近常態分布
- **大數定律**: 樣本均值收斂至期望值
- **Chebyshev 不等式**: 提供距期望值k個標準差內的機率上界
- **貝氏定理**: 結合先驗機率與似然估計更新後驗機率
- **Cramér-Rao 下界**: 估計量的方差下限