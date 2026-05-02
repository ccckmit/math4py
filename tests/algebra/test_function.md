# test_function.py

## 概述 (Overview)

測試 `math4py.algebra.polynomial` 與 `math4py.algebra.vector` 模組，實作多項式運算（求值、加法、乘法）與向量運算（範數、點積、叉積）。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestVectorFunctions` | 向量範數、點積、叉積 |
| `TestPolynomialFunctions` | 多項式求值、加法、乘法 |

## 測試原理 (Testing Principles)

- **向量範數**：`‖v‖ = √(v₁² + v₂² + ...)`，如 [3,4] 的範數為 5
- **點積**：`v·w = Σ vᵢwᵢ`，如 [1,2,3]·[4,5,6] = 32
- **叉積**：三維向量外積，結果為垂直於兩向量的向量
- **多項式求值**：代入社區計算，如 2x²+3x+1 當 x=2 時為 15
- **多項式乘法**：利用卷積展開