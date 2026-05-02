# Rete Inference Engine Tests

## 概述 (Overview)

測試前向鏈結 (forward chaining) 推理引擎的核心功能，包括事實 (facts)、規則 (rules)、以及推理執行。

## 測試內容 (Test Coverage)

### TestFact
- `test_create_fact` - 建立帶屬性之事實
- `test_fact_matches` - 屬性匹配 (dict 條件)
- `test_fact_matches_with_callable` - 函數式匹配 (lambda)

### TestRule
- `test_create_rule` - 建立規則 (條件 + 動作)

### TestReteEngine
- `test_single_condition_rule` - 單條件規則觸發
- `test_multi_condition_rule` - 多條件規則 (家族關係推導)
- `test_no_duplicate_inference` - 防重複推論機制
- `test_query_facts` - 查詢符合條件之事實
- `test_clear_engine` - 清除引擎狀態

## 測試原理 (Testing Principles)

**Rete 演算法**：高效的前向鏈結推理
1. **事實 (Fact)**：帶屬性的斷言，如 `{"type": "even", "number": 2}`
2. **規則 (Rule)**：LHS 條件列表 + RHS 動作函數
3. **工作記憶 (Working Memory)**：儲存所有事實
4. **模式匹配**：根據條件找出符合之事實組合
5. **衝突解決**：多規則同時滿足時的處理

```
母親(Alice, Bob) + 父親(Bob, Charlie) → 祖母(Alice, Charlie)
```

引擎執行 `run()` 直到無新規則觸發或達到 `max_iterations` 上限。