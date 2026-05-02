# 賽局理論定理驗證

## 概述

本模組驗證賽局理論中的核心定理，包括 Nash 均衡定理、Minimax 定理、優勢策略定理等。

## 數學原理

### 核心定理

1. **Nash 均衡定理**：每個有限雙人賽局至少存在一個 Nash 均衡（混合策略）

2. **Minimax 定理**：零和遊戲中 maximin = minimax

3. **優勢策略**：若策略 A 對所有情況都不劣於 B，則 A 為優勢策略

4. **Folk 定理**：重複遊戲中，任何可實現的報酬向量都可能是均衡結果

## 實作細節

### 定理驗證函數

| 函數 | 驗證內容 |
|------|----------|
| `nash_equilibrium_theorem(p1, p2)` | Nash 均衡存在性 |
| `minimax_theorem(payoffs)` | maximin = minimax |
| `dominant_strategy_theorem(payoffs)` | 優勢策略存在 |
| `zero_sum_value_theorem(payoffs)` | 零和遊戲有值 |
| `prisoner_dilemma_equilibrium()` | 囚徒困境：雙方 defect 是均衡 |
| `battle_sex_equilibria()` | 性別大戰：兩個純策略均衡 + 混合 |
| `mixed_strategy_sum(payoffs)` | 混合策略機率和 = 1 |
| `iterated_dominance_theorem(payoffs)` | 迭代優勢收斂 |

## 使用方式

```python
from math4py.game_theory.theorem import (
    nash_equilibrium_theorem,
    minimax_theorem,
    prisoner_dilemma_equilibrium,
    battle_sex_equilibria
)

# Nash 均衡定理驗證
p1 = [[2, 0], [0, 1]]
p2 = [[1, 0], [0, 2]]
result = nash_equilibrium_theorem(p1, p2)
# result["equilibria"] = [(0,0), (1,1)]

# Minimax 定理
minimax_theorem([[1, -1], [-1, 1]])

# 囚徒困境
prisoner_dilemma_equilibrium()
# {"pass": True, "equilibrium": "both defect"}

# 性別大戰
battle_sex_equilibria()
# {"pass": True, "equilibria": [(0,0), (1,1)], "count": 2}
```