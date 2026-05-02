# 概述

向量微積分函數模組，計算梯度、散度、旋度、拉普拉斯算子、雅可比矩陣與Hessian矩陣等向量微積分運算。

# 數學原理

## 梯度 (Gradient)
$$\nabla f = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \ldots, \frac{\partial f}{\partial x_n} \right)$$

梯度指向函數值增加最快的方向。

## 散度 (Divergence)
$$\nabla \cdot \mathbf{F} = \frac{\partial F_1}{\partial x_1} + \frac{\partial F_2}{\partial x_2} + \cdots + \frac{\partial F_n}{\partial x_n}$$

## 旋度 (Curl, 3D)
$$\nabla \times \mathbf{F} = \begin{pmatrix} \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z} \\ \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x} \\ \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \end{pmatrix}$$

## 拉普拉斯算子 (Laplacian)
$$\Delta f = \nabla \cdot \nabla f = \sum_{i=1}^n \frac{\partial^2 f}{\partial x_i^2}$$

## 雅可比矩陣 (Jacobian)
$$J_F = \begin{pmatrix} \frac{\partial F_1}{\partial x_1} & \cdots & \frac{\partial F_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial F_m}{\partial x_1} & \cdots & \frac{\partial F_m}{\partial x_n} \end{pmatrix}$$

## Hessian 矩陣
$$H = \begin{pmatrix} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots \\ \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}$$

## 方向導數 (Directional Derivative)
$$D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \lim_{h \to 0} \frac{f(\mathbf{x} + h\mathbf{u}) - f(\mathbf{x} - h\mathbf{u})}{2h}$$

# 實作細節

所有函數使用中央差分法進行數值計算：
$$\frac{\partial f}{\partial x_i} \approx \frac{f(\ldots, x_i+h, \ldots) - f(\ldots, x_i-h, \ldots)}{2h}$$

## 梯度計算
```python
def gradient(f, point, h=1e-5):
    n = len(point)
    grad = np.zeros(n)
    for i in range(n):
        point_plus = point.copy()
        point_minus = point.copy()
        point_plus[i] += h
        point_minus[i] -= h
        grad[i] = (f(*point_plus) - f(*point_minus)) / (2 * h)
    return grad
```

## 三維旋度計算
```python
def curl_3d(F, point, h=1e-5):
    x, y, z = point.astype(float)
    curl = np.zeros(3)
    curl[0] = (F3(x, y+h, z) - F3(x, y-h, z) - F2(x, y, z+h) + F2(x, y, z-h)) / (2*h)
    # ...
    return curl
```

## 保守場判斷
```python
def curl_free_3d(F, point, h=1e-5):
    return np.allclose(curl_3d(F, point, h), 0, atol=1e-6)
```

# 使用方式

```python
from math4py.calculus.vector_calculus import gradient, divergence, curl_3d, jacobian, hessian
import numpy as np

# 梯度
f = lambda x, y: x**2 + y**2
grad = gradient(f, np.array([1.0, 1.0]))  # [2, 2]

# 散度
F = lambda x, y: (x, y)
div = divergence(F, np.array([1.0, 1.0]))  # 2

# 旋度
F3d = lambda x, y, z: (y, -x, 0)
curl = curl_3d(F3d, np.array([0.0, 0.0, 0.0]))  # [0, 0, -2]

# 雅可比矩陣
F_vec = lambda x: np.array([x[0]**2, x[1]**2])
J = jacobian(F_vec, np.array([1.0, 2.0]))
```