# math4py

Wraps numpy/scipy for unified math API with R-style statistics.

## Commands

```bash
pip install -e ".[dev]"   # first-time setup
pytest                       # all tests
pytest tests/plot/            # outputs PDFs to out/
ruff check . && ruff format .
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

## Tensor Module

Gradient-enabled tensor operations with automatic differentiation:

```python
from math4py.tensor import Tensor
import math4py.tensor.function as F

# Create tensors
x = Tensor([1.0, 2.0, 3.0], requires_grad=True)
w = Tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)

# Operations
y = F.linear(x, w)  # Linear transformation
z = y.relu()          # ReLU activation
loss = z.sum()
loss.backward()        # Backpropagation

print(x.grad)  # Gradient w.r.t. x
```

Features:
- NumPy-based tensor operations
- Automatic gradient computation (backpropagation)
- Supports: addition, multiplication, matmul, reshape, transpose
- Activation functions: ReLU, Sigmoid, Tanh
- Loss functions: MSE, Cross-Entropy with Softmax
- Neural network operations: linear layers, softmax

Module structure:
- `tensor.py` — Tensor class with autograd
- `function.py` — Neural network functions and operations
- `theorem.py` — 30 pytest tests verifying tensor operations and gradients
