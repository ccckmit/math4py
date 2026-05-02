# test_complex.py

## 概述 (Overview)

測試 `math4py.algebra.complex` 模組，此模組實作複數的基本運算與函數，包括加減乘除、指數、對數、極座標轉換、二次方程式求解等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestComplexCreation` | 建立複數、取實部/虛部 |
| `TestComplexOperations` | 共軛、模長、幅角、極座標轉換 |
| `TestComplexArithmetic` | 加法、減法、乘法、除法 |
| `TestComplexFunctions` | 指數函數、對數函數、複數冪 |
| `TestQuadraticSolver` | 二次方程式求解（實根與複根） |

## 測試原理 (Testing Principles)

- **代數運算**：驗證複數加減乘除的計算正確性
  - 加法：(a+bi)+(c+di) = (a+c)+(b+d)i
  - 乘法：(a+bi)(c+di) = (ac-bd)+(ad+bc)i
- **極座標**：`|z| = √(a²+b²)`，arg(z) = arctan(b/a)
- **歐拉公式**：e^(iπ) = -1，驗證 exp(z) 當 z=iπ 時結果為 -1
- **二次方程式**：使用代數公式，驗證 x²+1=0 的根為 ±i