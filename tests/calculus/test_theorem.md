# test_theorem.py (Calculus)

## 概述 (Overview)

測試 `math4py.calculus.theorem` 模組，驗證微積分的基本定理。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestFundamentalTheorem` | 微積分基本定理 |
| `TestMeanValue` | 均值定理 |
| `TestRolle` | 羅爾定理 |
| `TestIntermediateValue` | 介值定理 |
| `TestTaylor` | 泰勒定理 |

## 測試原理 (Testing Principles)

- **微積分基本定理**：若 F'(x) = f(x)，則 ∫ₐᵇ f(x)dx = F(b)-F(a)
- **均值定理**：若 f 在 [a,b] 連續，在 (a,b) 可導，則存在 c 使得 f'(c) = (f(b)-f(a))/(b-a)
- **羅爾定理**：若 f(a)=f(b)，則存在 c 使得 f'(c)=0
- **介值定理**：連續函數必取到端點間的所有值
- **泰勒定理**：f(x) = Σ f⁽ⁿ⁾(a)/n! · (x-a)ⁿ + Rₙ