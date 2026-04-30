"""複變函數（Complex Analysis）基礎函數。"""

from typing import Callable, List, Tuple

import numpy as np


def complex_derivative(f: Callable, z: complex, h: float = 1e-6) -> complex:
    """複變函數的導數 f'(z) ≈ (f(z+h) - f(z))/h。"""
    return (f(z + h) - f(z)) / h


def is_analytic(f: Callable, z: complex, h: float = 1e-6) -> bool:
    """檢查函數在 z 點是否解析（簡化版）。"""
    x, y = z.real, z.imag

    # 數值偏導數
    f_x_plus = f(complex(x + h, y))
    f_x_minus = f(complex(x - h, y))
    du_dx = (f_x_plus.real - f_x_minus.real) / (2 * h)
    dv_dx = (f_x_plus.imag - f_x_minus.imag) / (2 * h)

    f_y_plus = f(complex(x, y + h))
    f_y_minus = f(complex(x, y - h))
    du_dy = (f_y_plus.real - f_y_minus.real) / (2 * h)
    dv_dy = (f_y_plus.imag - f_y_minus.imag) / (2 * h)

    # 柯西-黎曼方程: du/dx = dv/dy, du/dy = -dv/dx
    return abs(du_dx - dv_dy) < 1e-4 and abs(du_dy + dv_dx) < 1e-4


def is_holomorphic(f: Callable, domain: List[complex] = None) -> bool:
    """檢查函數是否在整個定義域上全純（holomorphic）。

    全純函數 = 在開集上處處解析的函數。
    簡化版：檢查幾個點是否都解析。
    """
    if domain is None:
        # 預設檢查幾個點
        domain = [0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j, -1 + 0j, 0 - 1j]

    return all(is_analytic(f, z) for z in domain)


def line_integral(f: Callable, z0: complex, z1: complex, n: int = 1000) -> complex:
    """複平面上的線積分 ∫_C f(z) dz。"""
    t = np.linspace(0, 1, n)
    z_path = z0 + t * (z1 - z0)

    integral = 0j
    for i in range(n - 1):
        dt = t[i + 1] - t[i]
        z_mid = (z_path[i] + z_path[i + 1]) / 2
        dz = z1 - z0
        integral += f(z_mid) * dz * dt

    return integral


def cauchy_integral_formula(f: Callable, a: complex, r: float, n: int = 1000) -> complex:
    """柯西積分公式 f(a) = (1/2πi) ∮ f(z)/(z-a) dz。"""
    theta = np.linspace(0, 2 * np.pi, n)
    z = a + r * np.exp(1j * theta)
    dz = r * 1j * np.exp(1j * theta)

    integrand = f(z) / (z - a) * dz
    integral = np.trapezoid(integrand, theta) / (2j * np.pi)
    return integral


def residue_simple_pole(f: Callable, a: complex, h: float = 1e-6) -> complex:
    """簡單極點的留數 Res(f, a) = lim_{z→a} (z-a)f(z)。"""
    return f(a + h) * h


def mobius_transformation(a: complex, b: complex, c: complex, d: complex, z: complex) -> complex:
    """莫比烏斯變換 w = (az + b)/(cz + d)。"""
    denominator = c * z + d
    if abs(denominator) < 1e-15:
        return complex("inf")
    return (a * z + b) / denominator


def complex_line_integral_path(f: Callable, path: np.ndarray) -> complex:
    """沿著給定路徑的線積分 ∫_C f(z) dz。"""
    integral = 0j
    for i in range(len(path) - 1):
        z_mid = (path[i] + path[i + 1]) / 2
        dz = path[i + 1] - path[i]
        integral += f(z_mid) * dz
    return integral


def liouville_theorem_check(f: Callable, R_values: List[float] = None) -> bool:
    """檢查劉維爾定理：有界的整函數必為常數。

    簡化版：檢查函數在大圓上的值是否接近常數。
    """
    if R_values is None:
        R_values = [1.0, 10.0, 100.0]

    values = []
    for R in R_values:
        z = R * np.exp(1j * 0)  # 實軸上的點
        values.append(f(z))

    # 如果函數值變化很小，可能是常數
    max_diff = max(
        abs(values[i] - values[j]) for i in range(len(values)) for j in range(i + 1, len(values))
    )
    return max_diff < 1e-6


def morera_theorem_check(f: Callable, triangle_vertices: List[complex] = None) -> bool:
    """檢查莫雷拉定理：若 ∫_Δ f(z) dz = 0 對所有三角形 Δ，則 f 解析。

    簡化版：檢查幾個三角形的積分是否為 0。
    """
    if triangle_vertices is None:
        triangle_vertices = [
            [0 + 0j, 1 + 0j, 0 + 1j],  # 直角三角形
            [0 + 0j, 2 + 0j, 1 + 1j],  # 另一個三角形
        ]

    for vertices in triangle_vertices:
        # 沿三角形積分
        integral = 0j
        n = 1000
        for i in range(3):
            z0 = vertices[i]
            z1 = vertices[(i + 1) % 3]
            integral += line_integral(f, z0, z1, n)

        if abs(integral) > 1e-4:  # 調整容差
            return False
    return True


def goursat_theorem_check(f: Callable, rectangle: Tuple[complex, complex] = None) -> bool:
    """檢查古爾薩定理：若 f 在閉矩形上解析，則沿矩形邊界的積分為 0。"""
    if rectangle is None:
        rectangle = (0 + 0j, 1 + 1j)  # 單位正方形

    z0, z1 = rectangle
    # 定義矩形的四個頂點
    vertices = [z0, complex(z1.real, z0.imag), z1, complex(z0.real, z1.imag), z0]

    integral = 0j
    n = 100
    for i in range(4):
        integral += line_integral(f, vertices[i], vertices[i + 1], n)

    return abs(integral) < 1e-6


def riemann_zeta(s: complex, n_terms: int = 10000) -> complex:
    """黎曼ζ函數 ζ(s) = Σ_{n=1}^{∞} 1/n^s（Re(s) > 1）。

    簡化版：只計算有限項。
    """
    if s.real <= 1:
        # 對於 Re(s) ≤ 1，使用解析延拓的簡化版（僅示意）
        return complex("nan")

    result = 0j
    for n in range(1, n_terms + 1):
        result += 1.0 / (n**s)
    return result


def riemann_hypothesis_check_zeros(zeros: List[complex] = None) -> bool:
    """檢查給定的零點是否都在臨界線 Re(s) = 1/2 上。

    黎曼猜想：所有非平凡零點的實部都是 1/2。
    """
    if zeros is None:
        # 已知的前幾個非平凡零點（虚部）
        known_zeros_imag = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
        zeros = [complex(0.5, t) for t in known_zeros_imag]

    # 檢查每個零點的實部是否接近 0.5
    return all(abs(z.real - 0.5) < 1e-6 for z in zeros)


def critical_line_zero_count(n: int = 10) -> List[complex]:
    """返回前 n 個臨界線上的零點（已知值）。"""
    # 黎曼ζ函數在臨界線上的前幾個零點（虚部）
    known_zeros = [
        (0.5, 14.134725),
        (0.5, 21.022040),
        (0.5, 25.010858),
        (0.5, 30.424876),
        (0.5, 32.935062),
        (0.5, 37.586178),
        (0.5, 40.918719),
        (0.5, 43.327073),
        (0.5, 48.005151),
        (0.5, 49.773832),
    ]
    return [complex(re, im) for re, im in known_zeros[:n]]


def xi_function(s: complex) -> complex:
    """黎曼≡函數 ξ(s) = 1/2 s(s-1) π^{-s/2} Γ(s/2) ζ(s)。

    簡化版：只計算 s 為實數且 > 1 的情況。
    """
    if s.imag != 0 or s.real <= 1:
        return complex("nan")

    # 簡化：只返回 ζ(s) 的近似
    return riemann_zeta(complex(s.real, 0))


__all__ = [
    "complex_derivative",
    "is_analytic",
    "is_holomorphic",
    "line_integral",
    "cauchy_integral_formula",
    "residue_simple_pole",
    "mobius_transformation",
    "complex_line_integral_path",
    "liouville_theorem_check",
    "morera_theorem_check",
    "goursat_theorem_check",
    "riemann_zeta",
    "riemann_hypothesis_check_zeros",
    "critical_line_zero_count",
    "xi_function",
]


def cauchy_integral_formula(f: Callable, a: complex, r: float, n: int = 1000) -> complex:
    """柯西積分公式 f(a) = (1/2πi) ∮ f(z)/(z-a) dz。

    沿著圓 |z-a| = r 積分。
    """
    theta = np.linspace(0, 2 * np.pi, n)
    z = a + r * np.exp(1j * theta)
    dz = r * 1j * np.exp(1j * theta)

    integrand = f(z) / (z - a) * dz
    integral = np.trapezoid(integrand, theta) / (2j * np.pi)
    return integral


def residue_simple_pole(f: Callable, a: complex, h: float = 1e-6) -> complex:
    """簡單極點的留數 Res(f, a) = lim_{z→a} (z-a)f(z)。"""
    return f(a + h) * h


def mobius_transformation(a: complex, b: complex, c: complex, d: complex, z: complex) -> complex:
    """莫比烏斯變換 w = (az + b)/(cz + d)。"""
    denominator = c * z + d
    if abs(denominator) < 1e-15:
        return complex("inf")
    return (a * z + b) / denominator


def complex_line_integral_path(f: Callable, path: np.ndarray) -> complex:
    """沿著給定路徑的線積分 ∫_C f(z) dz。"""
    integral = 0j
    for i in range(len(path) - 1):
        z_mid = (path[i] + path[i + 1]) / 2
        dz = path[i + 1] - path[i]
        integral += f(z_mid) * dz
    return integral


__all__ = [
    "complex_derivative",
    "is_analytic",
    "line_integral",
    "cauchy_integral_formula",
    "residue_simple_pole",
    "mobius_transformation",
    "complex_line_integral_path",
]
