# test_measure.py

## 概述 (Overview)

測試 `math4py.calculus.measure` 模組，實作測度論基礎概念，包括勒貝格測度、計數測度、狄拉克測度、σ-代數等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestLebesgueMeasure1D` | 區間測度、單點測度、空集測度 |
| `TestLebesgueMeasure2D` | 矩形面積、單位正方形 |
| `TestIsLebesgueMeasurable` | 可測集合判斷 |
| `TestOuterMeasure1D` | 外測度計算 |
| `TestCountingMeasure` | 有限集合的計數測度 |
| `TestDiracMeasure` | 狄拉克測度 |
| `TestSigmaAlgebra` | σ-代數生成 |
| `TestIsMeasure` | 測度合法性驗證 |
| `TestMeasureSpace` | 測度空間檢查 |
| `TestLebesgueIntegral` | 簡單函數的勒貝格積分 |
| `TestIntegrableIndicator` | 指示函數可積性 |

## 測試原理 (Testing Principles)

- **勒貝格測度**：區間 [a,b] 的測度為 b-a
- **單點測度**：任何單點集的測度為 0
- **計數測度**：有限集合的測度等於元素個數
- **狄拉克測度**：δₓ₀(A) = 1 當 x₀ ∈ A，否則為 0
- **σ-代數**：對補運算與可數聯集封閉
- **測度公理**：非負性、空集測度為 0、可數可加性