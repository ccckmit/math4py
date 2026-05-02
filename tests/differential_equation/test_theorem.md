# 微分方程定理驗證測試 (test_theorem.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.differential_equation.theorem` 模組中的定理與數學性質，包括：
- 數值方法的收斂階數
- 穩定性條件
- 能量守恆特性

## 測試內容 (Test Coverage)

### 1. Euler 收斂階數 (TestEulerConvergenceOrder)
- `test_convergence_order_near_one`: Euler 法收斂階 ≈ 1
- `test_zero_slope`: 零斜率時誤差極小

### 2. RK4 優於 Euler (TestRK4SuperiorToEuler)
- `test_rk4_more_accurate`: RK4 精度顯著高於 Euler

### 3. 熱方程衰減率 (TestHeatEquationDecayRate)
- `test_decay_rate_positive`: 衰減率為正
- `test_decay_rate_increases_with_alpha`: α 增大則衰減加快

### 4. 波動方程能量守恆 (TestWaveEquationEnergyConservation)
- `test_energy_conservation_low`: 能量變異小
- `test_energy_conservation_higher_c`: 不同波速下皆守恆

### 5. 熱方程穩定性條件 (TestStabilityCriterionHeat)
- `test_stable_case`: r = 0.25 穩定
- `test_unstable_case`: r = 0.6 不穩定

### 6. 波動方程穩定性條件 (TestStabilityCriterionWave)
- `test_stable_case`: r² = 0.81 穩定
- `test_unstable_case`: r² = 1.2 不穩定

### 7. 李雅普諾夫穩定定點 (TestLyapunovNegativeStableFixedPoint)
- `test_stable_lyapunov_negative`: 負指數 → 穩定

### 8. 李雅普諾夫不穩定螺旋 (TestLyapunovPositiveUnstableSpiral)
- `test_unstable_lyapunov_positive`: 正指數 → 不穩定

## 測試原理 (Testing Principles)

- **收斂階**: 數值方法誤差不隨網格細化而收斂的速率
- **CFL 條件**: 顯式有限差分法的穩定性要求
- **能量守恆**: 波動方程總能量應恆定
- **特徵值分析**: 矩陣穩定性由譜半徑決定