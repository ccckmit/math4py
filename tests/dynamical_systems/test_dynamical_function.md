# 動力系統函數測試 (test_dynamical_function.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.dynamical_systems.function` 模組中的動力系統數值方法，包括：
- ODE 數值積分
- 相空間軌跡計算
- 定點分析
- 線性穩定性
- 洛倫茲系統與邏輯斯蒂映射
- 分岔圖

## 測試內容 (Test Coverage)

### 1. Euler 法 (TestEulerMethod)
- `test_linear_ode`: dy/dt = -y, y(0) = 1 → y = e^{-t}
- `test_constant_ode`: dy/dt = 0, y(0) = 1 → y = 1

### 2. RK4 法 (TestRungeKutta4)
- `test_linear_ode_rk4`: RK4 精度優於 Euler

### 3. 相空間軌跡 (TestPhaseSpaceTrajectory)
- `test_harmonic_oscillator`: 諧振子能量守恆

### 4. 定點分析 (TestFixedPointAnalysis)
- `test_stable_fixed_point`: f(y) = y - 0.5 不動點在 y = 0.5
- `test_unstable_fixed_point`: f(y) = y 不動點在 y = 0

### 5. 線性穩定性 (TestLinearStability)
- `test_stable_matrix`: 負實部特徵值 → 穩定
- `test_unstable_matrix`: 正實部特徵值 → 不穩定

### 6. 洛倫茲系統 (TestLorenzSystem)
- `test_lorenz_derivative`: 洛倫茲導數計算
- `test_lorenz_trajectory`: 吸引子軌跡

### 7. 邏輯斯蒂映射 (TestLogisticMap)
- `test_logistic_fixed_point`: r = 2 時收斂到 0.5
- `test_logistic_period_doubling`: r = 3.2 時出現週期 2

### 8. 分岔圖 (TestBifurcationDiagram)
- `test_bifurcation_data_shape`: 數據形狀正確

## 測試原理 (Testing Principles)

- **能量守恆**: 諧振子 E = ½(x² + v²) 恆定
- **定點條件**: f(x*) = 0
- **穩定性**: df/dx|_{x*} < 0 → 穩定
- **分岔**: 參數變化導致定性行為改變