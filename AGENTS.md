# math4py

Wraps numpy/scipy for unified math API with R-style statistics.

## Commands

```bash
pip install -e ".[dev]"   # first-time setup
pytest                       # all tests
pytest tests/plot/            # outputs PDFs to out/
ruff check .                 # check code quality
ruff check . --fix           # auto-fix safe errors
ruff check . --fix --unsafe-fixes  # auto-fix more errors
ruff format .                # format code
ruff check . && ruff format .  # check + format (CI)
```

## Key facts

- R-style API: `import math4py as R` → `R.dnorm(...)`, `R.t_test(...)`, etc.
- `statistics` module also available as `math4py.R`
- `geometry`: `Point`, `Vector` (N-dim); `Line3D`, `Plane3D` (3D); `Line2D`/`Transform2D` in `geometry._2d`
- `plot` auto-detects CJK fonts by platform (macOS/Linux/Windows)
- Ruff: py38, double quotes, indent 4, line-length 100
- Plot tests: `filename="out/xxx.pdf"` saves; `filename=None` displays
- Test config: `pyproject.toml` → `testpaths = ["tests"]`

## Architecture

- **Numerical only**: no symbolic computation (use sympy directly for that)
- Each domain module has:
  - `function.py` — numerical calculation functions
  - `theorem.py` — pytest tests that verify definitions, axioms, or theorems
- `logic/` — Logic programming modules:
  - `rete_inference.py` — Rete algorithm inference engine (forward chaining)
  - `examples/logic/prolog.py` — Prolog-style interpreter (backward chaining)
  - `examples/logic/family.pl` — Family relations knowledge base
  - `examples/logic/math.pl` — Math inference knowledge base

## Logic Module

Two inference engines available:

### Rete Engine (Forward Chaining)
```python
from math4py.logic.rete_inference import Fact, Rule, ReteEngine

engine = ReteEngine()
engine.add_fact(Fact("mother", "alice", "bob"))
engine.add_rule(Rule("grandmother", ["X", "Z"],
                    [("mother", "X", "Y"), ("mother", "Y", "Z")]))
results = engine.query("grandmother", "alice", "charlie")
```

### Prolog Interpreter (Backward Chaining)
```bash
# Run from project root
python examples/logic/prolog.py examples/logic/family.pl "grandmother(X, Y)"
```

Features:
- Prolog-style syntax: facts (`pred(args).`) and rules (`head :- body.`)
- Unification algorithm with variable binding
- Backtracking search
- Variable renaming to avoid scoping conflicts
- Supports: variables (uppercase), atoms (lowercase), numbers, structures

Example queries:
- `grandmother(X, Y)` — find all grandmother relationships
- `grandfather(X, Y)` — find all grandfather relationships
- `great_grand_mother(X, Y)` — transitive relations

## Theorem.py 撰寫原則

theorem.py 的目的是驗證數學定理、公理和定義是否成立。撰寫時應遵循以下原則：

### 1. 函數應該接受參數進行驗證

不好：直接返回 `{"pass": True}`
```python
def commutativity():
    return {"pass": True}  # 不好！沒驗證什麼
```

好：接受參數並實際驗證
```python
def commutativity(a, b):
    left = a + b
    right = b + a
    return {"pass": left == right, "left": left, "right": right}
```

### 2. 用真值表驗證邏輯定理

```python
def de_morgan_theorem():
    # 遍歷所有 P, Q 的 True/False 組合
    for p in [True, False]:
        for q in [True, False]:
            # 驗證 ¬(P ∧ Q) = ¬P ∨ ¬Q
            if not (p and q) != ((not p) or (not q)):
                return {"pass": False}
    return {"pass": True}
```

### 3. 用抽樣驗證統計/隨機定理

```python
def central_limit_theorem(sample_fn, true_mean, true_var, n, n_samples):
    # 抽樣多次，驗證樣本均值的分布
    sample_means = [np.mean(sample_fn(n)) for _ in range(n_samples)]
    expected_se = np.sqrt(true_var / n)
    pass_mean = abs(np.mean(sample_means) - true_mean) < 0.1
    pass_se = abs(np.std(sample_means) - expected_se) < 0.2 * expected_se
    return {"pass": pass_mean and pass_se}
```

### 4. 驗證幾何/代數等式

```python
def pythagorean_theorem(a, b, c):
    left = c * c
    right = a * a + b * b
    return {"pass": abs(left - right) < 1e-10}
```

### 5. 參數化範例

- **set/theorem.py**:
  ```python
  def associativity_union(set1, set2, set3):
      left = (set1 | set2) | set3
      right = set1 | (set2 | set3)
      return {"pass": left == right}
  ```

- **geometry/theorem.py**:
  ```python
  def distance_formula(p1, p2):
      d_sq = (p2.x - p1.x)**2 + (p2.y - p1.y)**2
      return {"pass": True}  # 已在公式中驗證
  ```

- **logic/theorem.py** (真值表):
  ```python
  def modus_ponens_theorem():
      for p in [True, False]:
          for q in [True, False]:
              p_implies_q = not p or q
              if p and p_implies_q:
                  if not q: return {"pass": False}
      return {"pass": True}
  ```

### 6. 個案測試放在 tests/ 目錄

每個定理應該有對應的測試檔案：

```python
# tests/set/test_set_theorems.py
def test_associativity_union(self):
    from math4py.set.theorem import associativity_union
    result = associativity_union({1}, {2}, {3})
    assert result["pass"]
```

### 7. 什麼情況可以返回 {"pass": True}

僅限於無法用程式驗證的大型定理（如四色定理需要電腦輔助證明）：

```python
def four_color_theorem():
    return {"pass": True, "description": "4-color theorem holds"}
```

### 總結：theorem.py 應該是「可驗證的數學陳述」，不是單純返回 True 的函數。
