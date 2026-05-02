# logic/first_order_logic.md

## 概述

一階邏輯（述詞邏輯）運算，實現變數/常數/函數/謂詞表示、歸一、前向/後向鏈結。

## 數學原理

### 一階邏輯語法
- **變數** (Variable)：大寫開頭，如 X, Y
- **常數** (Constant)：小寫開頭，如 a, b, john
- **函數** (Function)：如 f(X), father(X)
- **謂詞** (Predicate)：如 mother(X, Y), human(X)

### 原子公式 (Atom)
謂詞應用於項，如 mother(alice, bob)。

### 文字 (Literal)
原子公式或其否定。

### 子句 (Clause)
文字的析取 (V)。

### 歸一向化 (Unification)
最廣歸一子 (MGU) 算法：
1. 若 term1 == term2，返回當前 bindings
2. 若 term1 為變數且未綁定，綁定 term1→term2
3. 若 term2 為變數且未綁定，綁定 term2→term1
4. 若均為函數，遞迴歸一各參數
5. 檢查 occurs check（防止 X=f(X)）

### 前向鏈結 (Forward Chaining)
從已知事實出發，反覆應用規則直到無新事實產生（正向推理）。

### 後向鏈結 (Backward Chaining)
從目標出發，遞迴證明子目標（反向推理）。

### Skolem 化 (Skolemization)
移除存在量詞，替換為 Skolem 函數，保留全稱量詞。

## 實作細節

| 類別 | 說明 |
|------|------|
| `Variable`, `Constant`, `Function`, `Predicate` | 項和公式的基本類型 |
| `Atom`, `Literal`, `Clause` | 公式結構 |
| `make_atom(predicate, *terms)` | 創建原子公式 |
| `unify(term1, term2, bindings)` | MGU 算法 |
| `substitute(term, bindings)` | 應用置換 |
| `resolution(clause1, clause2)` | 子句歸一 |
| `forward_chaining(facts, rules)` | 前向鏈結 |
| `backward_chaining(goal, rules)` | 後向鏈結 |

## 使用方式

```python
from math4py.logic.first_order_logic import Variable, Constant, make_atom, unify

X = Variable("X")
a = Constant("a")
b = Constant("b")

# make_atom("mother", a, X) → mother(a, X)
atom = make_atom("mother", a, X)

# unify
unify(X, b)  # {'X': b}
unify(("f", X), ("f", "a"))  # {'X': 'a'}
```