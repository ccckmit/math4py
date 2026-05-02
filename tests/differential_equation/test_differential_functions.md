# 微分方程函數測試 (test_differential_functions.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.differential_equation.function` 模組中的數值方法實現，包括：
- 常微分方程 (ODE) 數值積分法
- 偏微分方程 (PDE) 數值解法
- 穩定性分析與李雅普諾夫指數計算

## 測試內容 (Test Coverage)

### 1. Euler 法 (TestEulerMethod)
- `test_linear_ode`: dy/dt = -y 指數衰減
- `test_zero_derivative`: dy/dt = 0 恆定解
- `test_constant_slope`: dy/dt = 2 線性增長

### 2. RK2 法 (TestRK2Method)
- `test_linear_ode`: 精確度優於 Euler 法
- `test_polynomial`: dy/dt = 2t → y = t²

### 3. RK4 法 (TestRK4Method)
- `test_linear_ode`: 高精度指數衰減
- `test_harmonic_oscillator`: 諧振子能量守恆驗證
- `test_exponential_growth`: dy/dt = y

### 4. 熱方程 (TestHeatEquation)
- `test_heat_decay`: 熱量隨時間衰減
- `test_boundary_conditions`: 邊界條件保持為零
- `test_initial_condition`: 初始條件 sin(πx) 正確

### 5. 波動方程 (TestWaveEquation)
- `test_wave_boundary_conditions`: 邊界條件保持為零
- `test_wave_symmetry`: sin(πx) 對稱性保持

### 6. 穩定性矩陣 (TestStabilityMatrix)
- `test_stable_system`: 負特徵值 → 穩定
- `test_unstable_system`: 正實部特徵值 → 不穩定
- `test_neutral_stability`: 純虛數特徵值 → 臨界穩定

### 7. 李雅普諾夫指數 (TestLyapunovExponent)
- `test_negative_exponent_stable`: 穩定軌跡指數為負
- `test_positive_exponent_divergence`: 發散軌跡指數為正

### 8. IVP 求解器 (TestSolveIVP)
- `test_solve_ivp_euler`: Euler 方法介面
- `test_solve_ivp_rk4`: RK4 方法介面
- `test_solve_ivp_invalid_method`: 錯誤方法拋出異常

## 測試原理 (Testing Principles)

- **數值積分**: 使用泰勒展開逼近，RK4 達到 4 階精度
- **能量守恆**: 諧振子總能量 E = ½(x² + v²) 應恆定
- **穩定性判定**: 矩陣特徵值實部決定系統穩定性
- **PDE 顯式法**: 熱方程 CFL 條件，波動方程穩定性條件