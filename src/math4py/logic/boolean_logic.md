# logic/boolean_logic.md

## 概述

布爾邏輯運算與化簡工具，包含基本門電路、真值表、卡諾圖、Quine-McCluskey。

## 數學原理

### 基本布爾運算
| 運算 | 符號 | 內容 |
|------|------|------|
| AND | ∧ | 兩者均為 True 時為 True |
| OR | ∨ | 任一者為 True 時為 True |
| NOT | ¬ | 反相 |
| XOR | ⊕ | 相異為 True |
| NAND | ↑ | NOT(A AND B) |
| NOR | ↓ | NOT(A OR B) |

### 蘊含 (Implication)
A → B = ¬A ∨ B

### 主析取範式 (PDNF) / 主合取範式 (PCNF)
- PDNF：為每個輸出為 1 的行構造 AND 項（積總和式）
- PCNF：為每個輸出為 0 的行構造 OR 項（和總積式）

### 卡諾圖 (Karnaugh Map)
將真值表排列為二維陣列，相鄰格子只差一個變數，用於手工化簡。

## 實作細節

| 函數 | 說明 |
|------|------|
| `boolean_and(a, b)`, `boolean_or(a, b)` | 基本 AND/OR |
| `boolean_xor(a, b)` | XOR（互斥或） |
| `boolean_implies(a, b)` | 蘊含 A→B |
| `create_truth_table(propositions, func)` | 生成真值表 |
| `is_tautology(propositions, func)` | 重言式判斷 |
| `boolean_to_minterm(vars, values)` | 積總和式的一項 |
| `boolean_to_maxterm(vars, values)` | 和總積式的一項 |
| `karnaugh_map(variables, values)` | 卡諾圖結構 |
| `quine_mccluskey(truth_table)` | Q-M 化簡（目前為框架） |

## 使用方式

```python
from math4py.logic.boolean_logic import boolean_xor, boolean_implies, create_truth_table

boolean_xor(True, False)    # True
boolean_implies(False, True)  # True (false implies anything is true)

def func(p, q): return p and q
table = create_truth_table(["P", "Q"], func)
# [('P', 'Q', 'result'), ...]
```