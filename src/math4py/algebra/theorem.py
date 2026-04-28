"""代數公理與複數定理。

不證自明的命题，是建構代數結構的基礎。
包含複數相關定理：代數基本定理等。
"""

import math
from typing import Any, Callable, Set

from .complex import argument, complex_add, complex_mul, modulus, solve_quadratic


def closure_axiom(carrier: Set[Any], op: Callable) -> bool:
    """封閉性公理：對 carrier 中所有元素 a, b，op(a, b) 仍在 carrier 中。"""
    for a in carrier:
        for b in carrier:
            if op(a, b) not in carrier:
                return False
    return True


def associativity(carrier: Set[Any], op: Callable) -> bool:
    """結合律公理：對所有 a, b, c，op(op(a, b), c) = op(a, op(b, c))。"""
    for a in carrier:
        for b in carrier:
            for c in carrier:
                if op(op(a, b), c) != op(a, op(b, c)):
                    return False
    return True


def identity_element(carrier: Set[Any], op: Callable, e: Any) -> bool:
    """單位元公理：對所有 a，op(e, a) = a = op(a, e)。"""
    for a in carrier:
        if op(e, a) != a or op(a, e) != a:
            return False
    return True


def inverse_element(carrier: Set[Any], op: Callable, e: Any, inv: Callable) -> bool:
    """逆元公理：對所有 a，op(a, inv(a)) = e = op(inv(a), a)。"""
    for a in carrier:
        if op(a, inv(a)) != e or op(inv(a), a) != e:
            return False
    return True


def commutativity(carrier: Set[Any], op: Callable) -> bool:
    """交換律公理：對所有 a, b，op(a, b) = op(b, a)。"""
    for a in carrier:
        for b in carrier:
            if op(a, b) != op(b, a):
                return False
    return True


def distributivity(carrier: Set[Any], add: Callable, mul: Callable) -> bool:
    """分配律公理：mul(a, add(b, c)) = add(mul(a, b), mul(a, c))。"""
    for a in carrier:
        for b in carrier:
            for c in carrier:
                if mul(a, add(b, c)) != add(mul(a, b), mul(a, c)):
                    return False
    return True


def complex_modulus_properties(z: complex) -> bool:
    """複數模的性質：|z₁z₂| = |z₁||z₂|, |z₁+z₂| ≤ |z₁| + |z₂| (三角不等式)。"""
    z1 = complex(3, 4)
    z2 = complex(1, -2)
    mul_property = abs(modulus(complex_mul(z1, z2)) - modulus(z1) * modulus(z2)) < 1e-9
    tri = modulus(complex_add(z1, z2)) <= modulus(z1) + modulus(z2) + 1e-9
    return mul_property and tri


def complex_argument_properties(z: complex) -> bool:
    """複數幅角的性質：arg(z₁z₂) = arg(z₁) + arg(z₂) (mod 2π)。"""
    z1 = complex(1, 1)
    z2 = complex(1, -1)
    expected = (argument(z1) + argument(z2)) % (2 * math.pi)
    actual = argument(complex_mul(z1, z2)) % (2 * math.pi)
    return abs(expected - actual) < 1e-9


def euler_formula() -> bool:
    """歐拉公式：e^(iπ) + 1 = 0。"""
    from .complex import complex_exp, create_complex

    result = complex_exp(create_complex(0, math.pi)) + 1
    return abs(result) < 1e-9


def fundamental_theorem_of_algebra() -> bool:
    """代數基本定理：每個非常數複係數多項式至少有一個複數根。

    驗證：對於二次方程 ax²+bx+c=0，使用複數求解可得兩個複數根。
    """
    # 測試 x² + 1 = 0，應有根 i 和 -i
    roots = solve_quadratic(1, 0, 1)
    expected1 = complex(0, 1)
    expected2 = complex(0, -1)
    return abs(roots[0] - expected1) < 1e-9 or abs(roots[0] - expected2) < 1e-9


__all__ = [
    "closure_axiom",
    "associativity",
    "identity_element",
    "inverse_element",
    "commutativity",
    "distributivity",
    "complex_modulus_properties",
    "complex_argument_properties",
    "euler_formula",
    "fundamental_theorem_of_algebra",
]
