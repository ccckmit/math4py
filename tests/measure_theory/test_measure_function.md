# Measure Theory Function Tests

## 概述 (Overview)

測試測度論函數模組：σ-代數、勒貝格測度、積分、範數、以及重要不等式。

## 測試內容 (Test Coverage)

### TestSigmaAlgebra
- `test_valid_sigma_algebra` - 有效 σ-代數：封閉於補集與可數聯集
- `test_missing_complement` - 缺少補集則非 σ-代數

### TestMeasureAdditivity
- `test_additive` - 不相交集合的測度可加性

### TestLebesgueMeasure
- `test_interval_measure` - 區間 [a,b] 測度為 b-a
- `test_empty_interval` - 空區間測度為 0

### TestLebesgueIntegrable
- `test_continuous_function` - 閉區間連續函數 Lebesgue 可積

### TestLebesgueIntegral
- `test_constant_function` - 常數函數積分：∫2dx = 2
- `test_linear_function` - ∫x dx from 0 to 1 = 0.5

### TestSigmaFinite
- `test_finite_measure` - 有限測度必為 σ-有限

### TestLPNorm
- `test_l2_norm` - L² 範數：||f||₂ = √(∫|f|²)
- `test_l1_norm` - L¹ 範數

### TestHolderInequality
- `test_holder_p2_q2` - Hölder 不等式 (p=q=2 為柯西-施瓦茨)

### TestMinkowskiInequality
- `test_minkowski_p2` - Minkowski 不等式：||f+g||₂ ≤ ||f||₂ + ||g||₂

## 測試原理 (Testing Principles)

- **σ-代數**：對補集、可數聯集封閉的集合族
- **測度**：满足非負性、 空集測度為 0、可數可加性的函數
- **Lebesgue 積分**：比 Riemann 積分更廣泛的積分定義
- **Lp 空間**：p 次冪可積函數構成的 Banach 空間
- **Holder 不等式**：1/p + 1/q = 1 時，∫|fg| ≤ ||f||ₚ·||g||q
- **Minkowski 不等式**：||f+g||ₚ ≤ ||f||ₚ + ||g||ₚ