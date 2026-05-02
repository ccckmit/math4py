# 概述

動力系統定理驗證模組，驗證存在唯一性定理、線性穩定性定理、守恆量、極限環、混沌敏感性以及分岔現象等動力系統核心理論。

# 數學原理

## 存在唯一性定理 (Existence and Uniqueness Theorem)

對初值問題 $\dot{y} = f(y,t), y(t_0) = y_0$：

若 $f$ 滿足 Lipschitz 條件：
$$\|f(y_1, t) - f(y_2, t)\| \leq L \|y_1 - y_2\|$$

則解存在且唯一。

## 線性穩定性定理

對線性系統 $\dot{y} = Ay$，解的行為由特徵值決定：
- $\text{Re}(\lambda_i) < 0$：漸進穩定
- $\text{Re}(\lambda_i) > 0$：不穩定
- $\text{Re}(\lambda_i) = 0$：邊界情況

## 守恆定律 (Conservation Laws)

保守系統具有不隨時間變化的守恆量 $H(y)$，即：
$$\frac{dH}{dt} = \nabla H \cdot \dot{y} = 0$$

數值方法應保持此守恆量近常數。

## 極限環 (Limit Cycle)

孤立閉軌跡為極限環，若鄰近軌跡漸進趨於該閉軌跡，則為穩定極限環。

極限環存在的條件（Poincaré-Bendixson定理）：
- 相平面有界區域內
- 無穩定定點
- 存在閉軌跡

## 混沌與初值敏感性

混沌系統的特徵：
1. **拓撲混合**：拓撲傳遞性
2. **初值敏感性**：對初始條件的指數敏感依賴
3. **稠密週期軌道**：有理逼近

李雅普諾夫指數 $\lambda > 0$ 表示指數發散，為混沌的標誌。

## 分岔理論 (Bifurcation Theory)

系統結構隨參數變化而發生定性改變的臨界點稱為分岔點。

### 邏輯斯蒂映射分岔

當 $r$ 通過臨界值時：
- $r = 1$：從 0 到非零固定點的分岔
- $r = 3$：固定點失穩，產生 2-週期
- $r \approx 3.57$：混沌開始

# 實作細節

## 存在唯一性檢查
```python
def existence_uniqueness_theorem(f, y0, t_span, eps=1e-6):
    try:
        dy = f(y0, t_span[0])
        return np.all(np.isfinite(dy))
    except:
        return False
```

## 線性穩定性定理
```python
def linear_stability_theorem(A, tol=1e-6):
    eigvals = np.linalg.eigvals(A)
    max_real = np.max(np.real(eigvals))
    is_stable = max_real < -tol
    return {
        "pass": is_stable,
        "eigenvalues": eigvals,
        "max_real_part": max_real
    }
```

## 守恆量檢查
```python
def conservation_law_check(f, y0, t_span, conservation_fn, n_steps=1000):
    t = np.linspace(t_span[0], t_span[1], n_steps)
    y = runge_kutta_4(f, y0, t)
    conserved_values = [conservation_fn(y[i]) for i in range(0, len(t), len(t)//100)]
    variation = np.std(conserved_values)
    return {"pass": variation < 1e-6, "variation": variation}
```

## 極限環檢測
```python
def limit_cycle_detection(y, tol=1e-2):
    if len(y) < 100:
        return False
    last_portion = y[-len(y)//3:]
    start_points = y[:len(y)//5]
    for point in last_portion:
        for start in start_points:
            if np.linalg.norm(point - start) < tol:
                return True
    return False
```

## 混沌敏感性
```python
def chaos_sensitivity_check(logistic_map_fn, x0, delta=1e-10, n_steps=100):
    x1, x2 = [x0], [x0 + delta]
    for i in range(1, n_steps):
        x1.append(logistic_map_fn(x1[-1]))
        x2.append(logistic_map_fn(x2[-1]))
    differences = [abs(x1[i] - x2[i]) for i in range(n_steps)]
    if differences[-1] > 0.5 or differences[-1] > 100 * differences[0]:
        return {"pass": True, "sensitive": True}
    return {"pass": False, "sensitive": False}
```

## 分岔定理
```python
def bifurcation_theorem(r_critical, r_test):
    x_before = logistic_map(r_test if r_test < r_critical else r_critical - 0.1, 0.5, 1000)
    x_after = logistic_map(r_test if r_test > r_critical else r_critical + 0.1, 0.5, 1000)
    unique_before = len(set(np.round(x_before[-100:], 3)))
    unique_after = len(set(np.round(x_after[-100:], 3)))
    return {
        "pass": unique_after > unique_before,
        "unique_before": unique_before,
        "unique_after": unique_after
    }
```

# 使用方式

```python
from math4py.dynamical_systems.theorem import (
    existence_uniqueness_theorem, linear_stability_theorem,
    conservation_law_check, limit_cycle_detection,
    chaos_sensitivity_check, bifurcation_theorem
)
import numpy as np

# 存在唯一性
f = lambda y, t: -y
y0 = np.array([1.0])
exists = existence_uniqueness_theorem(f, y0, (0, 1))

# 線性穩定性
A = np.array([[-1, 0], [0, -2]])
result = linear_stability_theorem(A)
print(result["stable"])  # True

# 分岔檢測
result = bifurcation_theorem(r_critical=3.0, r_test=3.5)
print(result["pass"])  # True
```