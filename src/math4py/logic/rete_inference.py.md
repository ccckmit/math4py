# Rete 推論引擎

## 概述

本模組實作基於 Rete 算法的向前鏈結推論引擎，用於高效的模式匹配和規則推論。適用於專家系統、邏輯編程等場景。

## 數學原理

### Rete 算法核心概念

1. **工作記憶體**（Working Memory）：儲存事實（Facts）
2. **生產規則**（Production Rules）：IF-THEN 形式
3. **模式匹配**：找出滿足所有條件的事實組合
4. **議程**（Agenda）：待執行的規則實例

### 演算法特點

- **增量式匹配**：新事實加入時只更新受影響的節點
- **共享節點**：不同規則共享常見模式
- **避免重複**：記錄已激活的規則+事實組合

### 核心資料結構

| 類別 | 數學含義 |
|------|----------|
| `Fact` | 事實（Working Memory Element） |
| `Rule` | 生產規則 IF conditions THEN actions |
| `ReteEngine` | 推論引擎 |

## 實作細節

### ReteEngine 方法

| 方法 | 說明 |
|------|------|
| `add_fact(fact)` | 加入事實到工作記憶體 |
| `add_rule(rule)` | 加入規則 |
| `fire_all_rules()` | 執行所有待執行規則 |
| `fire_rule()` | 執行一個規則 |
| `run(max_iterations)` | 執行推論直到收斂 |
| `query_facts(pattern)` | 查詢匹配模式的事實 |
| `clear()` | 清除所有狀態 |

### 條件匹配

```python
# 支持精確匹配
Fact(name="alice", age=30)

# 支持函數條件
Fact(score=85)
# 模式 {"score": lambda x: x > 80}  # 匹配 score > 80
```

## 使用方式

```python
from math4py.logic.rete_inference import Fact, Rule, ReteEngine, create_fact

# 建立引擎
engine = ReteEngine()

# 添加事實
engine.add_fact(Fact(name="alice", mother="bob", father="charlie"))
engine.add_fact(Fact(name="bob", mother="diana", father="edward"))
engine.add_fact(Fact(name="charlie", mother="frank", father="gary"))

# 定義規則：祖母
def make_grandmother(match):
    return Fact(grandmother=match[0].attributes["name"], grandchild=match[1].attributes["name"])

grandmother_rule = Rule(
    name="grandmother",
    conditions=[
        {"mother": "$mid"},           # X 是母親
        {"name": "$mid"}              # Y 是 X 的母親 => X 是 Y 的母親
    ],
    actions=[make_grandmother]
)

# 或更簡單的多條件規則：
def grandmother_rule_fn(mother_fact, child_fact):
    return Fact(
        grandmother=child_fact.attributes.get("mother"),
        grandchild=mother_fact.attributes.get("name")
    )

engine.add_rule(Rule(
    name="grandmother",
    conditions=[
        {"name": "$X", "mother": "$Y"},  # X 的母親是 Y
        {"name": "$Y", "mother": "$Z"}   # Y 的母親是 Z => Z 是 X 的祖母
    ],
    actions=[lambda m1, m2: Fact(grandmother=m1.attributes["mother"], grandchild=m2.attributes["name"])]
))

# 執行推論
engine.run()

# 查詢結果
results = engine.query_facts({"grandmother": "frank"})
```