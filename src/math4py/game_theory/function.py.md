# 賽局理論（Game Theory）基礎函數

## 概述

本模組提供賽局理論的核心運算，包括報酬矩陣、Nash 均衡、混合策略、零和遊戲等。

## 數學原理

### 核心概念

1. **報酬矩陣**：雙人正常形遊戲
   - Player 1: m × n 矩陣
   - Player 2: m × n 矩陣
   - 矩陣元素為各策略組合的報酬

2. **Nash 均衡**：無玩家能單方面改變策略而獲利
   - 純策略均衡：(i*, j*) 滿足 p1[i*, j*] 最大且 p2[i*, j*] 最大

3. **混合策略**：以機率分布選擇策略
   - Σp_i = 1, p_i ≥ 0

4. **零和遊戲**：一方的收益為另一方的損失
   - maximin = minimax（Minimax 定理）

## 實作細節

### 主要函數

| 函數 | 數學含義 |
|------|----------|
| `payoff_matrix(p1, p2)` | 建立報酬矩陣 |
| `best_response(payoffs, player)` | 最佳回應策略 |
| `nash_equilibrium(p1, p2)` | 純策略 Nash 均衡 |
| `mixed_strategy(payoffs)` | 混合策略求解 |
| `expected_payoff(s1, s2, payoff)` | E[s₁ · payoff · s₂] |
| `zero_sum_value(p1)` | 零和遊戲值 (maximin + minimax)/2 |
| `dominant_strategy(payoffs)` | 嚴格優勢策略 |
| `iterated_dominance(payoffs)` | 迭代優勢（嚴格被支配策略消除） |

### 經典遊戲

```python
prisoner_dilemma()   # 囚徒困境
matching_pennies()   # 硬幣配對
battle_sex()         # 性別大戰
```

## 使用方式

```python
import numpy as np
from math4py.game_theory.function import (
    payoff_matrix, nash_equilibrium, mixed_strategy,
    expected_payoff, zero_sum_value, prisoner_dilemma
)

# 囚徒困境
game = prisoner_dilemma()
p1, p2 = game["p1"], game["p2"]

# 找 Nash 均衡
eq = nash_equilibrium(p1, p2)
# 均衡為雙方都選擇 defect

# 混合策略
probs = mixed_strategy(np.array([[1, 0], [0, 1]]))

# 期望報酬
s1 = np.array([0.5, 0.5])
s2 = np.array([0.5, 0.5])
payoff = np.array([[2, 0], [0, 1]])
E = expected_payoff(s1, s2, payoff)

# 零和遊戲值
value = zero_sum_value([[1, -1], [-1, 1]])  # matching pennies
```