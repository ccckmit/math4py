# 最佳化函數 (Optimization Functions)

## 概述

本模組提供無約束及約束最佳化的數值方法：梯度下降、牛頓法、共軛梯度法及拉格朗日乘數法。

## 數學原理

### 1. 梯度下降法 (Gradient Descent)

**迭代公式**：
$$x_{k+1} = x_k - \alpha \nabla f(x_k)$$

其中 $\alpha$ 為學習率。

**收斂條件**：
$$\|x_{k+1} - x_k\| < \text{tol}$$

### 2. 牛頓法 (Newton's Method)

**迭代公式**：
$$x_{k+1} = x_k - H^{-1}(x_k) \nabla f(x_k)$$

其中 $H = \nabla^2 f$ 為 Hessian 矩陣。

**優點**：二階收斂（若 Hessian 正定）
**缺點**：需計算/近似 Hessian

### 3. 共軛梯度法 (Conjugate Gradient Method)

求解對稱正定線性系統 $Ax = b$：

$$A x^* = b$$

**迭代公式**：
$$\alpha_k = \frac{r_k^T r_k}{p_k^T A p_k}$$
$$x_{k+1} = x_k + \alpha_k p_k$$
$$r_{k+1} = r_k - \alpha_k A p_k$$
$$\beta_k = \frac{r_{k+1}^T r_{k+1}}{r_k^T r_k}$$
$$p_{k+1} = r_{k+1} + \beta_k p_k$$

### 4. 凸函數判斷

**定義**：$f$ 為凸函數若：
$$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$

### 5. 拉格朗日乘數法

求解約束優化：
$$\min f(x) \quad \text{s.t.} \quad g_i(x) = 0$$

**KKT 條件**：
$$\nabla f(x) = \sum \lambda_i \nabla g_i(x)$$

### 6. Armijo 回溯線搜索

確保充分下降：
$$f(x + \alpha d) \leq f(x) + c \alpha \nabla f(x)^T d$$

其中 $c \in (0, 1)$，通常 $c = 10^{-4}$。

## 實作細節

```python
def gradient_descent(f, grad_f, x0, learning_rate=0.01, max_iter=1000, tol=1e-6):
    """梯度下降法"""
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        g = np.array(grad_f(x))
        x_new = x - learning_rate * g
        if np.linalg.norm(x_new - x) < tol:
            return x_new, f(x_new), i + 1
        x = x_new
    return x, f(x), max_iter

def newton_method(f, grad_f, hess_f, x0, max_iter=100, tol=1e-6):
    """牛頓法"""
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        g = np.array(grad_f(x))
        H = np.array(hess_f(x))
        try:
            delta = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            delta = g  # Fallback
        x_new = x - delta
        if np.linalg.norm(x_new - x) < tol:
            return x_new, f(x_new), i + 1
        x = x_new
    return x, f(x), max_iter

def conjugate_gradient(A, b, x0=None, max_iter=None, tol=1e-6):
    """共軛梯度法"""
    n = len(b)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    if max_iter is None:
        max_iter = n
    
    r = b - A @ x
    p = r.copy()
    
    for i in range(max_iter):
        Ap = A @ p
        alpha = np.dot(r, r) / np.dot(p, Ap)
        x = x + alpha * p
        r_new = r - alpha * Ap
        
        if np.linalg.norm(r_new) < tol:
            break
        
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p
        r = r_new
    
    return x

def is_convex_function(f, domain_bounds, n_samples=100):
    """數值檢查凸性"""
    for _ in range(n_samples):
        x = np.array([np.random.uniform(b[0], b[1]) for b in domain_bounds])
        y = np.array([np.random.uniform(b[0], b[1]) for b in domain_bounds])
        theta = np.random.random()
        
        z = theta * x + (1 - theta) * y
        
        if f(z) > theta * f(x) + (1 - theta) * f(y) + 1e-10:
            return False
    return True

def backtracking_line_search(f, x, direction, grad_f_x, alpha=1.0, beta=0.5, c=1e-4):
    """Armijo 回溯線搜索"""
    while f(x + alpha * direction) > f(x) + c * alpha * np.dot(grad_f_x, direction):
        alpha *= beta
    return alpha
```

## 使用方式

```python
from math4py.optimization import (
    gradient_descent, newton_method, conjugate_gradient,
    is_convex_function, backtracking_line_search
)

# 梯度下降：最小化 f(x) = (x-3)^2
f = lambda x: (x[0] - 3)**2
grad_f = lambda x: np.array([2*(x[0] - 3)])
x_opt, f_opt, n_iter = gradient_descent(f, grad_f, x0=[0.0])
print(f"x* = {x_opt}, f* = {f_opt}, iter = {n_iter}")

# 牛頓法
hess_f = lambda x: np.array([[2]])
x_opt, f_opt, n_iter = newton_method(f, grad_f, hess_f, x0=[0.0])

# 共軛梯度法：解 Ax = b
A = np.array([[4, 1], [1, 3]])
b = np.array([1, 2])
x = conjugate_gradient(A, b)
print(x)  # 近似解

# 凸性檢查
f = lambda x: x[0]**2 + x[1]**2
bounds = [(-10, 10), (-10, 10)]
is_convex = is_convex_function(f, bounds)
print(is_convex)  # True
```