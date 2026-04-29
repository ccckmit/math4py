"""Hilbert 空間理論。"""

from typing import Callable, List, Tuple
import numpy as np


def inner_product_H(f: Callable, g: Callable, a: float, b: float, weight: Callable = None,
                     n: int = 1000) -> float:
    """Hilbert 空間內積 ⟨f,g⟩ = ∫_a^b w(x) f(x) g(x) dx。

    Args:
        f, g: 函數
        a, b: 區間
        weight: 權函數 w(x)，預設為 1
        n: 取樣點數

    Returns:
        內積值
    """
    x = np.linspace(a, b, n)
    fx = f(x)
    gx = g(x)
    if weight is not None:
        wx = weight(x)
    else:
        wx = np.ones_like(x)
    integrand = fx * gx * wx
    return np.trapezoid(integrand, x)


def norm_H(f: Callable, a: float, b: float, weight: Callable = None, n: int = 1000) -> float:
    """Hilbert 空間範數 ||f|| = √⟨f,f⟩。"""
    return np.sqrt(inner_product_H(f, f, a, b, weight, n))


def distance_H(f: Callable, g: Callable, a: float, b: float, weight: Callable = None, 
                  n: int = 1000) -> float:
    """Hilbert 空間距離 d(f,g) = ||f-g||。"""
    def diff(x):
        return f(x) - g(x)
    return norm_H(diff, a, b, weight, n)


def proj_orthogonal_H(f: Callable, e: Callable, a: float, b: float, weight: Callable = None,
                      n: int = 1000) -> float:
    """Hilbert 空間正交投影係數 pf = ⟨f,e⟩/||e||²。"""
    inner = inner_product_H(f, e, a, b, weight, n)
    norm_e_sq = inner_product_H(e, e, a, b, weight, n)
    return inner / norm_e_sq


def gram_schmidt_H(functions: List[Callable], a: float, b: float, weight: Callable = None,
                       n: int = 1000) -> List[Tuple[Callable, float]]:
    """Hilbert 空間 Gram-Schmidt 正交化。

    Returns:
        正交化函數列表 [(e1, ||e1||²), (e2, ||e2||²), ...]
    """
    ortho = []
    for f in functions:
        new_f = f
        for e, norm_sq in ortho:
            coeff = proj_orthogonal_H(lambda x: new_f(x), lambda x: e(x), a, b, weight, n)
            def subtract(x, c=coeff, e=e, nf=new_f):
                return nf(x) - c * e(x)
            new_f = subtract
        norm_sq = inner_product_H(lambda x: new_f(x), lambda x: new_f(x), a, b, weight, n)
        ortho.append((new_f, norm_sq))
    return ortho


def fourier_basis_H(n_max: int, a: float = -np.pi, b: float = np.pi) -> List[Callable]:
    """L²([-π,π]) 的 Fourier 基 {1/√(2π), cos(nx)/√π, sin(nx)/√π}。"""
    basis = [lambda x: 1.0 / np.sqrt(2.0 * np.pi)]
    for n in range(1, n_max + 1):
        basis.append(lambda x, k=n: np.cos(k * x) / np.sqrt(np.pi))
        basis.append(lambda x, k=n: np.sin(k * x) / np.sqrt(np.pi))
    return basis


def legendre_polynomials(n_max: int) -> List[Callable]:
    """Legendre 多項式 P_n(x) 在 [-1,1] 上正交。"""
    polys = [lambda x: np.ones_like(x),
             lambda x: x.copy()]
    for n in range(2, n_max + 1):
        def Pn(x, n=n, polys=polys):
            return ((2*n - 1) / n * x * polys[n-1](x) - 
                    (n - 1) / n * polys[n-2](x))
        polys.append(Pn)
    return polys[:n_max + 1]


def is_complete_basis_H(basis: List[Callable], test_fns: List[Callable],
                          a: float, b: float, weight: Callable = None,
                          n: int = 1000, tol: float = 0.1) -> bool:
    """檢查基是否完備（簡化：測試函數能否被逼近）。
    
    Returns True if basis is complete (small residual), False otherwise.
    """
    for f in test_fns:
        # Project f onto the basis
        f_proj = lambda x: np.zeros_like(x)
        for e in basis:
            coeff = proj_orthogonal_H(f, e, a, b, weight, n)
            def add_proj(x, c=coeff, e=e):
                return c * e(x)
            old_f_proj = f_proj
            f_proj = lambda x, old=old_f_proj, add=add_proj: old(x) + add(x)
        # Compute residual
        def residual(x):
            return f(x) - f_proj(x)
        error = norm_H(residual, a, b, weight, n)
        if error > tol:
            return False  # Not complete
    return True  # Complete


def riesz_representation(phi: Callable, basis: List[Callable], 
                         a: float, b: float) -> Callable:
    """Riesz 表示定理：φ(f) = ⟨f,g_φ⟩。

    給定連續線性泛函 φ，返回表示函數 g_φ。

    Args:
        phi: 線性泛函 φ(f)
        basis: 正交基

    Returns:
        表示函數 g_φ
    """
    coeffs = []
    for e in basis:
        coeffs.append(phi(e))
    def g_phi(x):
        result = np.zeros_like(x)
        for e, c in zip(basis, coeffs):
            result += c * e(x)
        return result / inner_product_H(e, e, a, b)
    return g_phi


def check_parallelogram_law(f: Callable, g: Callable, a: float, b: float) -> float:
    """平行四邊形法則 ||f+g||² + ||f-g||² = 2(||f||² + ||g||²)。

    Returns:
        殘差（應接近 0）
    """
    def f_plus_g(x): return f(x) + g(x)
    def f_minus_g(x): return f(x) - g(x)
    left = norm_H(f_plus_g, a, b)**2 + norm_H(f_minus_g, a, b)**2
    right = 2 * (norm_H(f, a, b)**2 + norm_H(g, a, b)**2)
    return abs(left - right)


def check_jordan_vonneumann_theorem(f: Callable, g: Callable, a: float, b: float) -> float:
    """Jordan-von Neumann 定理：內積可由範數表示。

    ⟨f,g⟩ = (||f+g||² - ||f-g||²)/4

    Returns:
        殘差（應接近 0）
    """
    def f_plus_g(x): return f(x) + g(x)
    def f_minus_g(x): return f(x) - g(x)
    inner_from_norm = (norm_H(f_plus_g, a, b)**2 - norm_H(f_minus_g, a, b)**2) / 4.0
    real_inner = inner_product_H(f, g, a, b)
    return abs(inner_from_norm - real_inner)


__all__ = [
    "inner_product_H",
    "norm_H",
    "distance_H",
    "proj_orthogonal_H",
    "gram_schmidt_H",
    "fourier_basis_H",
    "legendre_polynomials",
    "is_complete_basis_H",
    "riesz_representation",
    "check_parallelogram_law",
    "check_jordan_vonneumann_theorem",
]
