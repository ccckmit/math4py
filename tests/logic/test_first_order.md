# First-Order Logic Tests

## 概述 (Overview)

測試一階邏輯的核心構件：項 (terms)、原子公式 (atoms)、文字 (literals)、合一 (unification)、替換 (substitution)、以及前向鏈結 (forward chaining)。

## 測試內容 (Test Coverage)

### TestFOLTerms
- `test_variable_creation` - 變數建立 (名稱為大寫)
- `test_constant_creation` - 常數建立 (小寫原子)
- `test_predicate_creation` - 謂詞建立 (名稱+arity)
- `test_function_creation` - 函數建立

### TestAtom
- `test_atom_creation` - 原子公式：pred(arg1, arg2)
- `test_atom_equality` - 相同謂詞/引數則相等

### TestLiteral
- `test_literal_positive` - 正文字 (肯定)
- `test_literal_negative` - 負文字 (否定)

### TestUnification
- `test_unify_variable_constant` - 變數與常數合一
- `test_unify_same_terms` - 相同項合一 (空置換)
- `test_unify_not_unifiable` - 衝突常數無法合一

### TestSubstitution
- `test_substitute_variable` - 變數替換綁定

### TestResolution / TestForwardChaining
- `test_resolution` - 命題邏輯消解
- `test_forward_chaining` - 前向鏈結推理

### TestMakeAtom / TestMakeLiteral
- 工廠函數：快速創建 Atom/Literal

## 測試原理 (Testing Principles)

- **項 (Terms)**：變數、常數、函數應用
- **原子公式 (Atom)**：謂詞(項序列)
- **文字 (Literal)**：原子或其否定
- **合一 (Unification)**：找尋使兩式相等的置換
- **前向鏈結**：從事實出發應用規則推導新事實