"""泛函分析基礎函數。"""

import numpy as np


def norm_Lp(f, a, b, p=2.0, n=1000):
    """L^p 範數 ||f||_p = (∫_a^b |f(x)|^p dx)^(1/p)。

    Args:
        f: 函數 f(x)
        a, b: 積分區間
        p: 範數階數
        n: 取樣點數

    Returns:
        L^p 範數
    """
    x = np.linspace(a, b, n)
    y = np.abs(f(x)) ** p
    integral = np.trapezoid(y, x)
    return integral ** (1.0 / p)


def norm_L2(f, a, b, n=1000):
    """L² 範數 ||f||₂ = sqrt(∫ |f|² dx)。"""
    return norm_Lp(f, a, b, p=2.0, n=n)


def inner_product_L2(f, g, a, b, n=1000):
    """L² 內積 ⟨f,g⟩ = ∫_a^b f(x) g(x) dx。"""
    x = np.linspace(a, b, n)
    integrand = f(x) * g(x)
    return np.trapezoid(integrand, x)


def gram_schmidt_L2(functions, a, b, n=1000):
    """L² 空間的 Gram-Schmidt 正交化。

    Args:
        functions: 線性獨立函數列表
        a, b: 區間
        n: 取樣點數

    Returns:
        正交化後的函數列表
    """
    ortho = []
    for f in functions:
        new_f = f
        np.linspace(a, b, n)
        for g, norm_sq in ortho:
            proj_coeff = inner_product_L2(lambda x: new_f(x), lambda x: g(x), a, b, n)

            def new_f(x, coeff=proj_coeff, g=g, nf=new_f):
                return nf(x) - coeff * g(x)

        norm_sq = inner_product_L2(new_f, new_f, a, b, n)
        ortho.append((new_f, norm_sq))
    return [lambda x, g=g, ns=norm_sq: g(x) / np.sqrt(ns) for g, ns in ortho]


def is_orthogonal_L2(f, g, a, b, n=1000):
    """檢查 L² 正交性 ⟨f,g⟩ ≈ 0。"""
    inner = inner_product_L2(f, g, a, b, n)
    return abs(inner) < 1e-3


def linear_operator_apply(K, f, x, a, b, n=1000):
    """線性算子 Tf(x) = ∫_a^b K(x,y) f(y) dy。

    Args:
        K: 核函數 K(x, y)
        f: 輸入函數
        x: 輸出點
        a, b: 積分區間
        n: 取樣點數

    Returns:
        Tf(x) 數組
    """
    y = np.linspace(a, b, n)
    fy = f(y)
    result = np.zeros_like(x)
    for i, xi in enumerate(x):
        integrand = K(xi, y) * fy
        result[i] = np.trapezoid(integrand, y)
    return result


def spectral_radius(A):
    """線性算子（矩陣）的譜半徑 ρ(A) = max|λ_i|。"""
    eigvals = np.linalg.eigvals(A)
    return np.max(np.abs(eigvals))


def resolvent_set(A, z):
    """解集 (A - zI)^{-1}。"""
    n = A.shape[0]
    return np.linalg.inv(A - z * np.eye(n))


def function_space_basis(n_terms=5):
    """生成函數空間的一組基（多項式基）。

    Returns:
        [1, x, x², ..., x^{n-1}]
    """
    return [lambda x, k=k: x**k for k in range(n_terms)]


def weak_convergence_test(f_n, f, a, b, test_functions=None, n=1000):
    """弱收斂測試：∫ (f_n - f) φ dx → 0 ∀φ ∈ C_c。

    Args:
        f_n: 函數序列
        f: 極限函數
        a, b: 區間
        test_functions: 測試函數列表（預設用多項式）
        n: 取樣點數

    Returns:
        最大誤差
    """
    if test_functions is None:
        test_functions = function_space_basis(3)

    max_error = 0.0
    np.linspace(a, b, n)
    for phi in test_functions:
        integral_f = inner_product_L2(f, phi, a, b, n)
        for fn in f_n:
            integral_fn = inner_product_L2(fn, phi, a, b, n)
            error = abs(integral_fn - integral_f)
            max_error = max(max_error, error)
    return max_error


def compact_operator_test(K, a, b, n=50):
    """檢查積分算子是否為緊緻算子（近似有限秩）。

    使用奇異值的快速衰減來判斷。

    Returns:
        第 n 個奇異值（應很小）
    """
    x = np.linspace(a, b, n)
    y = np.linspace(a, b, n)
    K_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            K_matrix[i, j] = K(x[i], y[j])

    _, s, _ = np.linalg.svd(K_matrix, full_matrices=False)
    return s[-1]  # 最小的奇異值


__all__ = [
    "norm_Lp",
    "norm_L2",
    "inner_product_L2",
    "gram_schmidt_L2",
    "is_orthogonal_L2",
    "linear_operator_apply",
    "spectral_radius",
    "resolvent_set",
    "function_space_basis",
    "weak_convergence_test",
    "compact_operator_test",
]
