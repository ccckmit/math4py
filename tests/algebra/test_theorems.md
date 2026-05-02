# test_theorems.py

## 概述 (Overview)

測試 `math4py.algebra.theorem` 模組，驗證代數基本定理，特別是代數基本定理（ Fundamental Theorem of Algebra）。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestComplexProperties` | 複數幅角與模長性質 |
| `TestEulerFormula` | 歐拉公式 |
| `TestFundamentalTheoremAlgebra` | 代數基本定理（二次、三次多項式根的數量） |

## 測試原理 (Testing Principles)

- **代數基本定理**：n 次多項式恰有 n 個根（計入重根與虛根）
  - x²-2x+1 = (x-1)² 有 2 個根（其中 1 為二重根）
  - x²+1 有 2 個虛根 ±i
  - x³-1 有 3 個根