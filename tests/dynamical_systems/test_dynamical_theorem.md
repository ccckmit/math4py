# 動力系統定理測試 (test_dynamical_theorem.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.dynamical_systems.theorem` 模組中的動力系統定理，包括：
- 解的存在唯一性
- 線性穩定性定理
- 守恆律
- 極限環檢測
- 混沌敏感性
- 分岔定理

## 測試內容 (Test Coverage)

### 1. 存在唯一性 (TestExistenceUniqueness)
- `test_lipschitz_continuous`: Lipschitz 連續 → 存在唯一
- `test_discontinuous_false`: 不連續函數可能不滿足

### 2. 線性穩定性定理 (TestLinearStabilityTheorem)
- `test_stable_eigenvalues`: 負實部 → 穩定
- `test_unstable_eigenvalues`: 正實部 → 不穩定

### 3. 守恆律 (TestConservationLaw)
- `test_harmonic_oscillator_conservation`: 諧振子能量守恆

### 4. 極限環檢測 (TestLimitCycleDetection)
- `test_no_limit_cycle_linear`: 線性系統無極限環
- `test_van_der_pol_oscillator`: 范德波爾振盪器有極限環

### 5. 混沌敏感性 (TestChaosSensitivity)
- `test_logistic_non_chaos`: r = 2.5 時不混沌

### 6. 分岔定理 (TestBifurcationTheorem)
- `test_period_doubling_at_r3`: r = 3 處倍週期分岔

## 測試原理 (Testing Principles)

- **皮卡德-林德勒夫**: Lipschitz 條件保證 ODE 解存在唯一
- **穩定性判定**: 線性系統特徵值實部決定穩定性
- **極限環**: 閉軌跡吸引附近軌跡
- **混沌**: 對初始條件敏感性 + 混合性
- **分岔**: 參數臨界值處系統拓撲結構改變