# test_stochastic.py

## 概述 (Overview)

測試隨機微積分與金融模型的數值實現，包含布朗運動、Black-Scholes 定價、美式期權等。

## 測試內容 (Test Coverage)

### TestBrownianMotion
- `test_simulate_returns_correct_shapes`: 模擬形狀正確 (n_steps+1, n_paths)
- `test_simulate_starts_at_zero`: 布朗運動從原點出發
- `test_quadratic_variation_converges_to_T`: 二次變異收斂至 T
- `test_autocorrelation`: 自相關函數 Cov(W(s),W(t)) = min(s,t)

### TestGeometricBrownianMotion
- `test_simulate_returns_correct_shapes`: 幾何布朗運動路徑形狀
- `test_positive_prices`: 價格始終為正
- `test_expected_value`: E[S(t)] = S(0)·e^{μt}
- `test_initial_price`: 初始價格 S(0) 正確

### TestOrnsteinUhlenbeck
- `test_simulate_returns_correct_shapes`: OU 過程路徑形狀
- `test_stationary_mean`: 穩態均值為 μ
- `test_stationary_variance`: 穩態方差為 σ²/(2θ)

### TestBrownianBridge
- `test_simulate_returns_correct_shapes`: 布朗橋路徑形狀
- `test_endpoints`: 端點約束滿足

### TestBlackScholes
- `test_call_price_positive`: 買權價格為正
- `test_put_price_positive`: 賣權價格為正
- `test_in_the_money_call`: 價內買權價格 > 內含價值
- `test_put_call_parity`: 買權賣權平價成立
- `test_monte_carlo_close_to_analytic`: 蒙地卡羅趨近解析解
- `test_delta_call_in_range`: 買權 Delta ∈ (0,1)
- `test_delta_put_in_range`: 賣權 Delta ∈ (-1,0)

### TestAmericanOption
- `test_lsm_call_less_than_or_equal_to_s`: LSM 買權價格 ≤ S
- `test_binomial_tree_put`: 二叉樹美式賣權價格
- `test_american_call_european_call_equal`: 無紅利美式買權等於歐式買權

### TestItoIntegral
- `test_martingale_property`: Itô 積分期望為零
- `test_zero_integrand`: 零被積函數結果為零
- `test_identity_integral`: Itô 積分數值驗證

## 測試原理 (Testing Principles)

- **隨機模擬**: 路徑生成與路徑依賴特性
- **解析 vs 數值**: 蒙地卡羅模擬收斂至解析解
- **美式期權**: 最佳執行時間的數值方法（LSM、二叉樹）
- **greeks**: 風險敏感度的解析計算