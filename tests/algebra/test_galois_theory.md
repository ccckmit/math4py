# test_galois_theory.py

## 概述 (Overview)

測試 `math4py.algebra.galois_theory` 模組，此模組實作伽羅瓦理論的核心概念，包括多項式的可解性、判別式、群論性質等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestGaloisSolvability` | 二次、三次、四次可解，五次不可解 |
| `TestSeparablePolynomial` | 可分多項式判斷 |
| `TestDiscriminant` | 二次方程式判別式 |
| `TestGroupOrders` | 對稱群與交代群的階 |
| `TestCyclicGroup` | 循環群性質 |
| `TestFunctionAPI` | 多項式次數、判別式、伽羅瓦群等輔助函數 |

## 測試原理 (Testing Principles)

- **可解性**：次數 ≤ 4 的多項式可用根式解，五次及以上一般不可解
- **判別式**：Δ = b²-4ac，判斷根的性質
- **群論**：
  - 對稱群 Sₙ 的階為 n!
  - 交代群 Aₙ 的階為 n!/2
- **循環群**：若 |G|=n，則 G 為循環群當中存在階為 n 的元素