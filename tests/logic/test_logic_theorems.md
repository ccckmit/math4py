# Logic Theorems Tests

## 概述 (Overview)

使用真值表枚舉法驗證命題邏輯的基本定理和等價律。

## 測試內容 (Test Coverage)

### 推理規則 (Inference Rules)
- `TestModusPonens` - 肯定前件：P, P→Q ├ Q
- `TestModusTollens` - 否定後件：¬Q, P→Q ├ ¬P
- `TestHypotheticalSyllogism` - 假言三段論：P→Q, Q→R ├ P→R
- `TestDisjunctiveSyllogism` - 選言三段論：P∨Q, ¬P ├ Q

### 等價律 (Equivalence Laws)
- `TestDeMorgan` - 德摩根定律：¬(P∧Q) = ¬P∨¬Q, ¬(P∨Q) = ¬P∧¬Q
- `TestDistributive` - 分配律：P∧(Q∨R) = (P∧Q)∨(P∧R)
- `TestIdentity` - 同一律：P∧T = P, P∨F = P
- `TestDomination` - 支配律：P∨T = T, P∧F = F
- `TestIdempotent` - 冪等律：P∧P = P, P∨P = P
- `TestComplement` - 補餘律：P∨¬P = T, P∧¬P = F
- `TestAbsorption` - 吸收律：P∧(P∨Q) = P, P∨(P∧Q) = P
- `TestDoubleNegation` - 雙重否定：¬¬P = P
- `TestCommutative` - 交換律
- `TestAssociative` - 結合律
- `TestImplication` - 蘊含消除：P→Q = ¬P∨Q
- `TestResolution` - 消解原理
- `TestUnification` - 合一算法

## 測試原理 (Testing Principles)

對每條定理，遍历所有 P, Q 的 True/False 組合，驗證左式與右式在所有情況下皆相等 (或推理規則在所有情況下有效)。

```python
for p in [True, False]:
    for q in [True, False]:
        # 驗證 ¬(P ∧ Q) = ¬P ∨ ¬Q
```