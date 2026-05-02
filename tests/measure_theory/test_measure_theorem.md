# Measure Theory Theorem Tests

## 概述 (Overview)

測試測度論核心定理：Carathéodory 延拓、控制收斂、單調收斂、富比尼定理、以及 Lp 空間完备性。

## 測試內容 (Test Coverage)

### TestCaratheodoryExtension
- `test_extension_exists` - 卡拉西奧多利延拓定理

### TestDominatedConvergence
- `test_convergence` - Lebesgue 控制收斂定理

### TestMonotoneConvergence
- `test_monotone` - 單調收斂定理

### TestFubiniTheorem
- `test_fubini` - 富比尼定理：重積分可交換次序

### TestLpCompleteness
- `test_l2_complete` - L² 空間是完備的 (即希爾伯特空間)

## 測試原理 (Testing Principles)

- **Carathéodory 延拓**：外測度在 σ-代數上可延拓為測度
- **控制收斂定理**：若 fn → f 且 |fn| ≤ g (g 可積)，則 ∫fn → ∫f
- **單調收斂定理**：單調遞增非負函數序列，极限積分等於積分極限
- **富比尼定理**：可測函數在矩形區域上，重積分相等
- **Lp 完备性**：所有柯西序列收斂於空間內 (Banach 空間)