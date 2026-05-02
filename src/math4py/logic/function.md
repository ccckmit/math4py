# logic/function.md

## 概述

命題邏輯與一階邏輯運算函數，包含真值表生成、重言式/矛盾式判斷、歸一算法。

## 數學原理

### 命題聯結詞
| 聯結詞 | 符號 | Python |
|--------|------|--------|
| 否定 | ¬P | not p |
| 合取 | P∧Q | p and q |
| 析取 | P∨Q | p or q |
| 蘊含 | P→Q | not p or q |
| 雙條件 | P↔Q | (p and q) or (not p and not q) |

### 重言式、矛盾式、偶然命題
- **重言式 (Tautology)**：所有賦值均為 True
- **矛盾式 (Contradiction)**：所有賦值均為 False
- **偶然命題 (Contingent)**：部分為 True，部分為 False

### 歸一算法 (Resolution)
對兩個子句，找出互補文字 L 和 ¬L，產生新子句 (C₁-{L}) ∪ (C₂-{¬L})。

### 歸一向化 (Unification)
兩個項若存在置換 σ 使 t₁σ = t₂σ，則稱可歸一，σ 為歸一子 (unifier)。最廣歸一子 (MGU) 唯一存在（到變數重新命名）。

## 實作細節

| 函數 | 說明 |
|------|------|
| `modus_ponens(p_implies_q, p)` | 肯定前件 |
| `implication(p, q)` | 蘊含 P→Q |
| `truth_table(propositions, function)` | 生成真值表 |
| `is_tautology(propositions, function)` | 判斷重言式 |
| `is_contradiction(propositions, function)` | 判斷矛盾式 |
| `resolve(clause1, clause2)` | 命題邏輯歸一 |
| `unify(term1, term2, bindings)` | 一階邏輯歸一（MGU 算法） |

## 使用方式

```python
from math4py.logic.function import is_tautology, truth_table, unify

# P → P 為重言式
is_tautology(["P"], lambda vals: not vals[0] or vals[0])  # True

# 歸一
unify("X", "a")              # {'X': 'a'}
unify(("f", "X"), ("f", "b"))  # {'X': 'b'}
```