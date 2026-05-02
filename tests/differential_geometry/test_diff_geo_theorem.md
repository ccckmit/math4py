# 微分幾何定理測試 (test_diff_geo_theorem.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.differential_geometry.theorem` 模組中的微分幾何定理，包括：
- 高斯-博內定理
- 斯托克斯定理
- 散度定理
- 黎曼張量對稱性
- 里奇張量 trace 性質

## 測試內容 (Test Coverage)

### 1. 高斯-博內定理 (TestGaussBonnetTheorem)
- `test_sphere`: 球面 ∫K dA = 4π = 2πχ, χ = 2
- `test_torus`: 環面 ∫K dA = 0 = 2πχ, χ = 0

### 2. 斯托克斯定理 (TestStokesTheorem)
- `test_simple_case`: 向量場 F = (-y/2, x/2), ∇×F = k

### 3. 散度定理 (TestDivergenceTheorem)
- `test_radial_field`: F = (x, y, z), ∇·F = 3

### 4. 黎曼張量對稱性 (TestRiemannTensorSymmetry)
- `test_antisymmetry`: R^i_{jkl} = -R^i_{jlk}

### 5. 里奇張量 trace (TestRicciTensorTrace)
- `test_trace_scalar_curvature`: g^{ij} Ric_{ij} = R (純量曲率)

## 測試原理 (Testing Principles)

- **高斯-博內定理**: ∫_M K dA + ∫_∂M κ_g ds = 2πχ(M)
- **斯托克斯定理**: ∫_Ω (∇×F)·n dS = ∮_∂Ω F·dr
- **散度定理**: ∫_V (∇·F) dV = ∮_∂V F·n dS
- **黎曼反對稱**: R^i_{jkl} = -R^i_{jlk} = -R^i_{jkl}