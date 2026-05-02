# 泛函分析定理測試 (test_functional_theorem.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.functional.theorem` 模組中的泛函分析定理，包括：
- 柯西-施瓦茨不等式
- 三角不等式
- 貝塞爾不等式
- 帕塞瓦爾恆等式
- 里斯表示定理
- 譜半徑定理
- 弱收斂刻劃

## 測試內容 (Test Coverage)

### 1. 柯西-施瓦茨不等式 (TestCauchySchwarz)
- `test_inequality_holds`: |<f,g>| ≤ ||f|| ||g||
- `test_equality_case`: 線性相關時取等號

### 2. 三角不等式 (TestTriangleInequality)
- `test_inequality_holds`: Σ|<f,e_i>|² ≤ ||f||²
- `test_equality_case`: f 在基底張成空間中時取等號

### 3. 貝塞爾不等式 (TestBesselInequality)
- `test_inequality_holds`: Σ|<f,e_i>|² ≤ ||f||²

### 4. 帕塞瓦爾恆等式 (TestParseval)
- `test_identity_complete_basis`: 完整正交基底的帕塞瓦爾恆等式

### 5. 里斯表示定理 (TestRieszRepresentation)
- `test_linear_functional`: φ(f) = ∫f(x)dx = <f, 1>

### 6. 譜半徑定理 (TestSpectralRadius)
- `test_diagonal_matrix`: 譜半徑等於最大特徵值
- `test_identity`: ρ(I) = 1

### 7. 弱收斂 (TestWeakConvergence)
- `test_constant_sequence`: 常數序列弱收斂
- `test_divergent_not_weak`: 震盪序列

## 測試原理 (Testing Principles)

- **柯西-施瓦茨**: |<f,g>|² ≤ <f,f><g,g>
- **貝塞爾**: 正交基底的能量不等式
- **帕塞瓦爾**: 完整基底時貝塞爾變等號
- **里斯**: H → H* 的等距同構
- **譜半徑**: ρ(A) = sup{|λ|: λ ∈ σ(A)}