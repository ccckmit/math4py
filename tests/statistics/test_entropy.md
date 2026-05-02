# test_entropy.py

## 概述 (Overview)

測試資訊理論中的熵、交叉熵、KL 散度與互資訊等函數的正確性。

## 測試內容 (Test Coverage)

### TestEntropy
- `test_uniform_2`: 均勻分佈 [0.5, 0.5] 熵為 1 bit
- `test_uniform_4`: 均勻分佈 [0.25, 0.25, 0.25, 0.25] 熵為 2 bits
- `test_certain`: 確定事件 P=[1,0,0] 熵為 0
- `test_normalization`: 自動正規化未和為 1 的機率
- `test_base_e`: 自然對數底 base=e

### TestCrossEntropy
- `test_perfect_prediction`: p=q 時交叉熵等於熵 H(p,q) = H(p)
- `test_uniform`: 均勻分布的交叉熵計算
- `test_mismatched`: 不匹配分布的交叉熵大於熵

### TestKLDivergence
- `test_identical`: 相同分布 KL(p||p) = 0
- `test_different`: 不同分布 D(p||q) > 0
- `test_normalization`: 自動正規化輸入

### TestMutualInformation
- `test_independent`: 獨立變數互資訊為 0
- `test_perfect_correlation`: 完全相關時 MI > 0
- `test_marginal_entropy`: 驗證 MI = H(X) + H(Y) - H(X,Y)

## 測試原理 (Testing Principles)

- **資訊熵**: H(p) = -Σ p(x) log p(x)，衡量不確定性
- **交叉熵**: H(p,q) = -Σ p(x) log q(x)，衡量預測與真實分布的差異
- **KL 散度**: D(p||q) = Σ p(x) log(p(x)/q(x))，非對稱度量
- **互資訊**: I(X;Y) = H(X) + H(Y) - H(X,Y)，衡量變數間共享資訊量