# Boolean Logic Tests

## 概述 (Overview)

測試布氏代數的基本運算、邏輯閘門、以及真值表生成功能。

## 測試內容 (Test Coverage)

### TestBooleanOperations
- `test_boolean_and` - AND 運算 (T∧T=T, 其餘為 F)
- `test_boolean_or` - OR 運算 (F∨F=F, 其餘為 T)
- `test_boolean_not` - NOT 運算 (¬T=F, ¬F=T)
- `test_boolean_xor` - XOR 運算 (相同為 F, 相異為 T)
- `test_boolean_nand` - NAND 運算 (AND 反相)
- `test_boolean_nor` - NOR 運算 (OR 反相)
- `test_boolean_implies` - 蘊含運算 (P→Q)

### TestLogicGates
- `test_and_gate` / `test_or_gate` / `test_not_gate` / `test_xor_gate`

### TestTruthTable
- `test_create_truth_table` - 生成 n 變數真值表 (2^n 列)
- `test_tautology` - 重言式：P ∨ ¬P
- `test_contradiction` - 矛盾式：P ∧ ¬P
- `test_contingent` - 或然式：視情況而真

## 測試原理 (Testing Principles)

- **布氏代數**：封閉於 AND/OR/NOT 的二值代數系統
- **真值表枚舉**：窮舉所有 2^n 輸入組合驗證輸出
- **重言式**：所有組合皆為 True
- **矛盾式**：所有組合皆為 False