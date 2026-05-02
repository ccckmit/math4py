# 希爾伯特空間測試 (test_hilbert_space.py)

## 概述 (Overview)

本測試檔案驗證 `math4py.functional.hilbert_space` 模組中的希爾伯特空間性質，包括：
- 內積與範數
- 距離與正交投影
- Gram-Schmidt 正交化
- 傅立葉基底與勒讓德多項式
- 完整性與里斯表示
- 平行四邊形律與 Jordan-von Neumann 定理

## 測試內容 (Test Coverage)

### 1. 內積 (TestInnerProductH)
- `test_symmetry`: <f,g> = <g,f>
- `test_linearity`: <af+bg, h> = a<f,h> + b<g,h>

### 2. 範數 (TestNormH)
- `test_positive_definiteness`: ||f|| ≥ 0, = 0 ⟺ f = 0
- `test_zero_function`: 零函數範數為零
- `test_scaling`: ||cf|| = |c| ||f||

### 3. 距離 (TestDistanceH)
- `test_zero_distance`: d(f,f) = 0
- `test_symmetry`: d(f,g) = d(g,f)

### 4. 正交投影 (TestProjOrthogonalH)
- `test_proj_coefficient`: proj(f,e) = <f,e>/||e||²

### 5. Gram-Schmidt (TestGramSchmidtH)
- `test_orthogonal_output`: 正交化後函數互相正交

### 6. 傅立葉基底 (TestFourierBasisH)
- `test_basis_length`: {1, cos(nx), sin(nx)} 基底長度

### 7. 勒讓德多項式 (TestLegendrePolynomials)
- `test_orthogonality`: P_n 與 P_m (n≠m) 正交
- `test_norm`: ||P_n||² = 2/(2n+1)

### 8. 完整性 (TestCompleteBasisH)
- `test_constant_basis_incomplete`: 單一函數不是完整基底

### 9. 里斯表示 (TestRieszRepresentation)
- `test_linear_functional`: φ(f) = ∫f 由 g = 1 表示

### 10. 平行四邊形律 (TestParallelogramLaw)
- `test_law_holds`: ||f+g||² + ||f-g||² = 2(||f||² + ||g||²)

### 11. Jordan-von Neumann 定理 (TestJordanVonNeumann)
- `test_theorem_holds`: <f,g> = (||f+g||² - ||f-g||²)/4

## 測試原理 (Testing Principles)

- **內積空間**: 滿足對稱性、線性性、正定性的二元運算
- **希爾伯特空間**: 完整的內積空間
- **正交投影**: 最近點投影定理
- **正交多項式**: 勒讓德多項式在 [-1,1] 上正交
- **Jordan-von Neumann**: 範數可決定內積