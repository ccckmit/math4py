# test_calculus_advanced.py

## 概述 (Overview)

測試 `math4py.calculus.analysis` 與 `math4py.calculus.series` 模組，實作高等微積分與級數理論，包括泰勒級數、傅里葉級數、極限、連續性、收斂性判斷等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestTaylorSeries` | 常數與線性函數的泰勒展開 |
| `TestFourierSeries` | 正弦波與常數函數的傅里葉係數 |
| `TestPowerSeries` | 冪級數計算 |
| `TestGeometricSeries` | 等比級數收斂與發散 |
| `TestHarmonicSeries` | 調和級數發散、交錯調和級數收斂 |
| `TestRatioTest` | 比值審斂法 |
| `TestLimit` | 多項式與 sin(x)/x 的極限 |
| `TestIsContinuous` | 連續性判斷 |
| `TestIntermediateValueTheorem` | 介值定理 |
| `TestExtremeValueTheorem` | 極值定理 |
| `TestSequenceLimit` | 數列極限與柯西數列 |
| `TestPointwiseConvergence` | 點態收斂 |
| `TestUniformConvergence` | 一致收斂 |

## 測試原理 (Testing Principles)

- **泰勒級數**：f(x) = Σ f⁽ⁿ⁾(a)/n! · (x-a)ⁿ
- **傅里葉級數**：將週期函數展開為正弦/餘弦級數
- **極限**：`lim_{x→0} sin(x)/x = 1`
- **級數收斂**：
  - 等比級數當 |r|<1 時收斂，和為 a/(1-r)
  - 調和級數發散，交錯調和級數收斂於 ln(2)
- **介值定理**：連續函數在端點異號時，中間必有根