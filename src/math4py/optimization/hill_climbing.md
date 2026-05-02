# optimization/hill_climbing.md

## 概述

爬山演算法實現，包含貪婪局部搜索、隨機重啟、模擬退火等策略。

## 數學原理

### 爬山演算法 (Hill Climbing)
局部搜索的核心思想：
1. 從初始點 x₀ 出發
2. 在鄰域 N(x) 中找更好的候選點
3. 若找到則移動，否則停止（達到局部極值）

下山版（minimize）選擇 `f(x') < f(x)` 的點。

### 確定性 vs 隨機鄰域
- **確定性**：沿每維度的 ± 方向探索
- **隨機**：添加高斯擾動，避免陷入狹窄的山谷

### 隨機重啟爬山
多次從隨機初始點重啟，緩解局部極值問題。

### 模擬退火 (Simulated Annealing)
Metropolis 準則：
- 若 Δ = f(x') - f(x) > 0（更好的解），則接受
- 若 Δ < 0（更差的解），以機率 exp(Δ/T) 接受

溫度 T 逐漸降低（冷卻），初期探索廣，后期收斂。

## 實作細節

| 函數 | 說明 |
|------|------|
| `hill_climbing(f, x0)` | 混合鄰域搜索 + 隨機擾動 + 重啟 |
| `hill_climbing_simple(f, x0)` | 純確定性鄰域搜索 |
| `random_restart_hill_climbing(f, bounds)` | 隨機重啟，指定邊界 |
| `simulated_annealing(f, x0, bounds)` | 模擬退火，含冷卻率參數 |

## 使用方式

```python
from math4py.optimization.hill_climbing import hill_climbing, simulated_annealing
import numpy as np

# Rosenbrock 函數
f = lambda x: (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

# 爬山
x_opt, f_opt, _ = hill_climbing(f, [0.0, 0.0], maximize=False)
print(f_opt)  # 趨近於 0

# 模擬退火
x_opt, f_opt, _ = simulated_annealing(f, [0.0, 0.0], bounds=[(-5,5), (-5,5)])
```