# 泛函分析函數測試 (test_functional_function.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.functional.function` 模組中的泛函分析函數，包括：
- L^p 範數與 L^2 範數
- 內積與正交性
- Gram-Schmidt 正交化
- 譜半徑
- 函數空間基底
- 弱收斂與緊算子

## 測試內容 (Test Coverage)

### 1. L^p 範數 (TestNormLp)
- `test_constant_function`: ||1||_p = (b-a)^{1/p}
- `test_zero_norm`: 零函數範數為零

### 2. L^2 範數 (TestNormL2)
- `test_sine_norm`: ||sin(πx)||₂ = 1/√2
- `test_polynomial_norm`: ||x||₂ = 1/√3

### 3. L^2 內積 (TestInnerProductL2)
- `test_orthogonal_sine_cosine`: sin 與 cos 正交
- `test_inner_product_symmetry`: <f,g> = <g,f>

### 4. Gram-Schmidt 正交化 (TestGramSchmidtL2)
- `test_orthogonal_output`: 輸出函數互相正交
- `test_preservation_norm`: 正交化後範數非零

### 5. 正交性檢測 (TestIsOrthogonalL2)
- `test_orthogonal_functions`: sin 與 cos 正交
- `test_non_orthogonal`: 1 與 x 不正交

### 6. 譜半徑 (TestSpectralRadius)
- `test_diagonal_matrix`: ρ(diag(1,2,3)) = 3
- `test_identity`: ρ(I) = 1

### 7. 函數空間基底 (TestFunctionSpaceBasis)
- `test_basis_length`: 基底長度正確
- `test_polynomial_basis`: x^k 為多項式

### 8. 弱收斂 (TestWeakConvergence)
- `test_constant_sequence`: 常數序列弱收斂到常數

### 9. 緊算子 (TestCompactOperator)
- `test_smooth_kernel`: 光滑核生成緊算子

## 測試原理 (Testing Principles)

- **範數定義**: ||f||_p = (∫|f|^p dx)^{1/p}
- **內積**: <f,g> = ∫ f(x)g(x) dx
- **正交性**: <f,g> = 0 表示正交
- **譜半徑**: ρ(A) = max|λ_i|
- **弱收斂**: <f_n, g> → <f, g> ∀ g ∈ H