# ZFC Set Theory Tests

## 概述 (Overview)

測試 Zermelo-Fraenkel 集合論 (含選擇公理) 的核心公理和構造。

## 測試內容 (Test Coverage)

### TestSet
- `test_creation` - 建立集合
- `test_empty_set` - 空集 ∅
- `test_equality` - 外延性相等

### TestExtensionalityAxiom
- `test_equal_sets` - 相同元素⇒相等
- `test_different_sets` - 不同元素⇒不相等

### TestPairSetAxiom
- `test_pair_creation` - 無序對 {a, b}
- `test_pair_with_same_element` - {a, a} = {a}

### TestUnionAxiom
- `test_union_of_sets` - 併集：{1,2} ∪ {3,4} = {1,2,3,4}
- `test_union_with_empty` - 與空集之併

### TestFoundationAxiom
- `test_regular_set` - 正則集合滿足正則公理
- `test_empty_set` - 空集滿足正則公理

### TestChoiceAxiom
- `test_choice_exists` - 非空集合族存在選擇函數
- `test_with_empty_set` - 含空集則失敗

### TestSubset
- `test_is_subset` / `test_not_subset`

### TestConstructNaturalNumbers
- `test_first_few` - 構造自然數 (0=∅, 1={∅}, ...)
- `test_names` - 自然數有名稱

### TestSeparationSchema
- `test_filter_even` - 分離公理：依性質抽取子集
- `test_empty_result` - 分離結果可為空

### TestOrderedPair
- `test_pair_creation` - 有序對 (a, b) = {{a}, {a, b}}
- `test_pair_representation`

### TestVerifyZFC
- `test_all_axioms` - 驗證所有 ZFC 公理

## 測試原理 (Testing Principles)

ZFC 公理系統構成現代數學的基礎：
- **外延性**：集合由其元素唯一確定
- **配對**：對任意 a,b 存在 {a,b}
- **併集**：任意集合族的聯集存在
- **正則性**：無集合包含自身
- **選擇公理**：非空集合族存在選擇函數
- **分離模式**：依性質從集合中抽取子集