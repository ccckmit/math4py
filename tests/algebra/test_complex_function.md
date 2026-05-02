# test_complex_function.py

## 概述 (Overview)

測試 `math4py.algebra.complex_function` 模組，此模組實作複變函數論（複分析）的核心定理與函數，包括解析函數、全純函數、留數計算、黎曼 zeta 函數等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestComplexDerivative` | f(z)=z² 的導數、常數函數導數 |
| `TestIsAnalytic` | 解析函數判斷（z² 為解析，共軛函數不是） |
| `TestIsHolomorphic` | 全純函數判斷（多項式為全純，共軛不是） |
| `TestLineIntegral` | 複變積分計算 |
| `TestCauchyIntegralFormula` | 柯西積分公式 |
| `TestMobiusTransformation` | 莫比烏斯變換（恆等變換、反演） |
| `TestResidueSimplePole` | 留數計算（1/z 在 z=0） |
| `TestLiouvilleTheorem` |劉維爾定理（有界整函數為常數） |
| `TestMoreraTheorem` | 莫雷拉定理 |
| `TestGoursatsTheorem` | 古爾薩定理 |
| `TestRiemannZeta` | 黎曼 zeta 函數（ζ(2) 收斂性） |
| `TestRiemannHypothesis` | 黎曼假設零點驗證 |
| `TestXiFunction` | ξ(s) 對稱性 |

## 測試原理 (Testing Principles)

- **解析與全純**：利用 Cauchy-Riemann 方程式判斷函數是否解析/全純
- **留數定理**：f(z)=1/z 在極點處的留數為 1
- **劉維爾定理**：有界整函數必為常數
- **黎曼假設**：所有非平凡零點的實部為 1/2
- **泰勒/洛朗級數**：利用級數展開驗證函數性質