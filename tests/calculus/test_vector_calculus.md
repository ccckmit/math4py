# test_vector_calculus.py

## 概述 (Overview)

測試 `math4py.calculus.vector_calculus` 模組，實作向量微積分運算，包括梯度、散度、旋度、拉普拉斯算子、雅可比矩陣、海森矩陣等。

## 測試內容 (Test Coverage)

| 類別 | 測試項目 |
|------|----------|
| `TestGradient` | 2D/3D 函數的梯度計算 |
| `TestDivergence` | 2D/3D 向量場的散度 |
| `TestCurl3D` | 3D 向量場的旋度 |
| `TestLaplacian` | 2D/3D 純量函數的拉普拉斯算子 |
| `TestDirectionalDerivative` | 方向導數 |
| `TestVectorLaplacian` | 向量場的拉普拉斯算子 |
| `TestJacobian` | 雅可比矩陣 |
| `TestHessian` | 海森矩陣 |
| `TestDivergenceFree2D` | 無散場判斷 |
| `TestCurlFree3D` | 無旋場判斷 |
| `TestPotentialFunction2D` | 保守場與位勢函數 |

## 測試原理 (Testing Principles)

- **梯度**：∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)
- **散度**：∇·F = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z
- **旋度**：∇×F = (∂F₃/∂y - ∂F₂/∂z, ∂F₁/∂z - ∂F₃/∂x, ∂F₂/∂x - ∂F₁/∂y)
- **拉普拉斯算子**：∇²f = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²
- **方向導數**：D_u f = ∇f · u
- **海森矩陣**：Hᵢⱼ = ∂²f/∂xᵢ∂xⱼ
- **保守場**：旋度為零，存在位勢函數