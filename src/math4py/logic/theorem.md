# logic/theorem.md

## 概述

邏輯定理驗證模組，以真值表遍歷驗證命題邏輯的定理與定律。

## 數學原理

### 基本推理規則

| 規則 | 內容 |
|------|------|
| 肯定前件 (Modus Ponens) | (P→Q, P) ⊨ Q |
| 否定後件 (Modus Tollens) | (P→Q, ¬Q) ⊨ ¬P |
| 假言三段論 | (P→Q, Q→R) ⊨ P→R |
| 選言三段論 | (P∨Q, ¬P) ⊨ Q |

### 邏輯等價定律

| 名稱 | 內容 |
|------|------|
| 德摩根律 | ¬(P∧Q) = ¬P∨¬Q, ¬(P∨Q) = ¬P∧¬Q |
| 分配律 | P∧(Q∨R) = (P∧Q)∨(P∧R), P∨(Q∧R) = (P∨Q)∧(P∨R) |
| 雙重否定 | ¬¬P = P |
| 蘊含消除 | P→Q = ¬P∨Q |

### 同一律/支配律/冪等律
- 同一律：A∧T = A, A∨F = A
- 支配律：A∨T = T, A∧F = F
- 冪等律：A∧A = A, A∨A = A

### 歸一向化 (Resolution)
選言子句的推理規則：
$$\frac{P \vee Q, \neg P \vee R}{Q \vee R}$$

### 一階邏輯歸一向化
若兩個文字可歸一，則.Resolve 得到新子句。

## 實作細節

| 函數 | 驗證內容 |
|------|----------|
| `modus_ponens_theorem()` | 遍歷所有 P, Q 組合驗證 MP |
| `modus_tollens_theorem()` | MT 推理規則 |
| `hypothetical_syllogism_theorem()` | 假言三段論 |
| `disjunctive_syllogism_theorem()` | 選言三段論 |
| `de_morgan_theorem()` | 德摩根律 |
| `distributive_theorem()` | 分配律 |
| `unification_theorem()` | MGU 存在性驗證 |

## 使用方式

```python
from math4py.logic.theorem import (
    modus_ponens_theorem, de_morgan_theorem, double_negation_theorem
)

modus_ponens_theorem()   # {'pass': True}
de_morgan_theorem()      # {'pass': True, 'law1': True, 'law2': True}
double_negation_theorem()  # {'pass': True}
```