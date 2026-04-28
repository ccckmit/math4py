"""複數運算函數。"""

import cmath


def create_complex(real: float, imag: float) -> complex:
    """建立複數。"""
    return complex(real, imag)


def real_part(z: complex) -> float:
    """回傳複數的實部。"""
    return z.real


def imag_part(z: complex) -> float:
    """回傳複數的虛部。"""
    return z.imag


def conjugate(z: complex) -> complex:
    """回傳複數的共轭複數。"""
    return z.conjugate()


def modulus(z: complex) -> float:
    """回傳複數的模 (绝对值)。"""
    return abs(z)


def argument(z: complex) -> float:
    """回傳複數的幅角 (主值，範圍 (-π, π])。"""
    return cmath.phase(z)


def to_polar(z: complex):
    """將複數轉為極座標 (r, θ)。"""
    return cmath.polar(z)


def from_polar(r: float, theta: float) -> complex:
    """從極座標建立複數。"""
    return cmath.rect(r, theta)


def complex_add(z1: complex, z2: complex) -> complex:
    """複數加法。"""
    return z1 + z2


def complex_sub(z1: complex, z2: complex) -> complex:
    """複數减法。"""
    return z1 - z2


def complex_mul(z1: complex, z2: complex) -> complex:
    """複數乘法。"""
    return z1 * z2


def complex_div(z1: complex, z2: complex) -> complex:
    """複數除法。"""
    return z1 / z2


def complex_exp(z: complex) -> complex:
    """複數指數函數 e^z。"""
    return cmath.exp(z)


def complex_log(z: complex) -> complex:
    """複數自然對數。"""
    return cmath.log(z)


def complex_pow(z: complex, w: complex) -> complex:
    """複數冪次 z^w。"""
    return z**w


def solve_quadratic(a: float, b: float, c: float):
    """解複數二次方程 ax² + bx + c = 0。"""
    discriminant = complex(b * b - 4 * a * c, 0)
    sqrt_d = cmath.sqrt(discriminant)
    return (-b + sqrt_d) / (2 * a), (-b - sqrt_d) / (2 * a)


__all__ = [
    "create_complex",
    "real_part",
    "imag_part",
    "conjugate",
    "modulus",
    "argument",
    "to_polar",
    "from_polar",
    "complex_add",
    "complex_sub",
    "complex_mul",
    "complex_div",
    "complex_exp",
    "complex_log",
    "complex_pow",
    "solve_quadratic",
]
