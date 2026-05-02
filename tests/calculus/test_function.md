# test_function.py (Calculus)

## 概述 (Overview)

測試 `math4py.calculus` 模組的數值微分與積分函數，包括導數、積分、梯形法、辛普森法等數值計算方法。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestDerivative` | x² 在 x=2、sin 在 x=0、exp 在 x=0 的導數 |
| `TestIntegral` | x² 在 [0,1]、sin 在 [0,π]、exp 在 [0,1] 的積分 |
| `TestTrapezoidal` | 梯形法求 ∫₀¹ x² dx |
| `TestSimpson` | 辛普森法求 ∫₀¹ x² dx 與 ∫₀^π sin(x) dx |

## 測試原理 (Testing Principles)

- **數值導數**：利用極限定義 f'(x) = lim_{h→0} (f(x+h)-f(x))/h
- **數值積分**：
  - 梯形法：∫f(x)dx ≈ Σ (f(xᵢ)+f(xᵢ₊₁))/2 · Δx
  - 辛普森法：使用拋物線近似，更精確
- **精確值參考**：
  - ∫₀¹ x² dx = 1/3
  - ∫₀^π sin(x) dx = 2
  - ∫₀¹ eˣ dx = e-1