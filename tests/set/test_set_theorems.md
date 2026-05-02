# test_set_theorems.py

## 概述 (Overview)

測試集合論定理與公理的驗證模組，確保集合運算符合數學公理系統。

## 測試內容 (Test Coverage)

### TestSetAxioms
- `test_extensionality_true`: 擴延性公理：相同元素的集合相等
- `test_extensionality_false`: 擴延性公理：不同元素的集合不相等
- `test_pair_set`: 配對公理
- `test_power_set_size`: 冪集公理：驗證 |P(S)| = 2^|S|
- `test_foundation_empty`: 空集合的基礎公理

### TestCommutativity
- `test_commutativity_union`: 聯集交換律 A ∪ B = B ∪ A
- `test_commutativity_intersection`: 交集交換律 A ∩ B = B ∩ A

### TestAssociativity
- `test_associativity_union`: 聯集結合律 (A ∪ B) ∪ C = A ∪ (B ∪ C)
- `test_associativity_intersection`: 交集結合律 (A ∩ B) ∩ C = A ∩ (B ∩ C)

### TestDistributivity
- `test_distributivity_union_over_intersection`: 分配律 A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- `test_distributivity_intersection_over_union`: 分配律 A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

### TestDeMorgan
- `test_demorgans_union`: 德摩根定律 (A ∪ B)' = A' ∩ B'
- `test_demorgans_intersection`: 德摩根定律 (A ∩ B)' = A' ∪ B'

### TestComplement
- `test_double_complement`: 雙補集 (A')' = A

### TestIdentity
- `test_identity_union`: 單位元 A ∪ ∅ = A

### TestDomination
- `test_domination`: 支配律 A ∪ U = U

### TestIdempotent
- `test_idempotent`: 冪等律 A ∪ A = A

### TestAbsorption
- `test_absorption`: 吸收律 A ∪ (A ∩ B) = A

### TestReplacementAxiom
- `test_replacement`: 置換公理：映射後的像構成集合

### TestSeparationAxiom
- `test_separation`: 分離公理：滿足條件的元素構成子集

## 測試原理 (Testing Principles)

- **公理化集合論**: 驗證 ZF 公理系統的核心性質
- **集合代數**: 透過具體集合運算驗證代數定律
- **封閉性**: 確認集合運算結果仍在集合論域內