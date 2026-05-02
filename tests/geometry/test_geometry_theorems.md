# test_geometry_theorems.py

## 概述 (Overview)

測試幾何定理模組，驗證平面幾何和立體幾何的核心數學定理，包括畢氏定理、距離公式、中點公式、希羅公式、餘弦定理、正弦定理、尤拉公式等。

## 測試內容 (Test Coverage)

| 測試類別 | 測試內容 |
|----------|----------|
| `TestPythagorean` | 畢氏定理 a² + b² = c²（3-4-5, 5-12-13） |
| `TestDistance` | 兩點間距離公式 |
| `TestMidpoint` | 中點公式驗證 |
| `TestSlope` | 直線斜率公式 |
| `TestHeron` | 希羅公式（三角形面積） |
| `TestLawOfCosine` | 餘弦定理 c² = a² + b² - 2ab·cos(C) |
| `TestLawOfSine` | 正弦定理 a/sin(A) = b/sin(B) |
| `TestAngleSum` | 三角形/多邊形內角和、內角公式 |
| `TestEuler` | 尤拉公式 V - E + F = 2（立方體、四面體） |
| `TestCollinearity` | 共線性檢驗（三點共線、點在線上） |
| `TestVector` | 向量平行、垂直、模長驗證 |

## 測試原理 (Testing Principles)

- **畢氏定理**：直角三角形中，兩股平方和等於斜邊平方
- **距離公式**：平面上兩點 (x₁,y₁) 與 (x₂,y₂) 距離為 √((x₂-x₁)² + (y₂-y₁)²)
- **希羅公式**：已知三邊長求三角形面積 A = √(s(s-a)(s-b)(s-c))，其中 s = (a+b+c)/2
- **餘弦定理**：描述三角形邊長與角度關係
- **尤拉公式**：凸多面體頂點數 - 邊數 + 面數 = 2