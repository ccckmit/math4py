# test_stochastic_theorems.py

## 概述 (Overview)

測試隨機過程與金融數學定理，包括布朗運動、Black-Scholes 模型、Itô 積分等。

## 測試內容 (Test Coverage)

### TestBrownianMotion
- `test_brownian_properties`: 布朗運動的基本性質（W(0)=0, 獨立增量）
- `test_brownian_increment`: 增量 W(t) - W(s) ~ N(0, t-s)
- `test_quadratic_variation`: 二次變異收斂至時間區間長度

### TestGeometricBrownianMotion
- `test_gbm`: 幾何布朗運動 S(t) = S(0)·exp((μ-σ²/2)t + σW(t))

### TestItoIntegral
- `test_ito_martingale`: Itô 積分的鞅性質 E[∫f dW] = 0

### TestBlackScholes
- `test_call_put_parity`: 買權賣權平價 C - P = S - K·e^{-rT}
- `test_greeks`: Black-Scholes 希臘字母（Delta, Gamma, Vega, Theta, Rho）

### TestItoLemma
- `test_ito_lemma`: Itô 引理驗證 d(f(W)) = f'(W)dW + ½f''(W)dt

### TestMartingale
- `test_martingale`: 鞅性質 E[M(t)|F(s)] = M(s)

## 測試原理 (Testing Principles)

- **布朗運動**: 連續時間隨機過程的基本構建模組
- **幾何布朗運動**: 描述股價動態的隨機微分方程
- **Itô 積分**: 針對布朗運動路徑的積分，非黎曼-斯蒂爾傑斯積分
- **Itô 引理**: 隨機微積分中的鏈式法則
- **Black-Scholes**: 無套利市場中期權定價公式
- **二次變異**: 量化路徑波動程度的關鍵概念