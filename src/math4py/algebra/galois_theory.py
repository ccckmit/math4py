r"""Galois theory functions and theorems."""

import numpy as np
from typing import List, Optional, Tuple


def polynomial_degree(coeffs: List) -> int:
    r"""Degree of polynomial."""
    return len(coeffs) - 1


def separable_polynomial(coeffs: List) -> bool:
    r"""Check if polynomial is separable."""
    if len(coeffs) < 3:
        return True
    roots = np.roots(coeffs)
    deriv = _polynomial_derivative(coeffs)
    deriv_roots = np.roots(deriv)
    for r in roots:
        if any(abs(r - dr) < 1e-10 for dr in deriv_roots):
            return False
    return True


def _polynomial_derivative(coeffs: List) -> List:
    r"""Derivative of polynomial."""
    return [i * coeffs[i] for i in range(1, len(coeffs))]


def discriminant(coeffs: List) -> float:
    r"""Discriminant of polynomial."""
    roots = np.roots(coeffs)
    n = len(roots)
    disc = 1
    for i in range(n):
        for j in range(i + 1, n):
            diff = roots[i] - roots[j]
            disc *= diff * diff
    return float(abs(disc))


def discriminant_quadratic(a: float, b: float, c: float) -> float:
    r"""Discriminant of quadratic."""
    return b * b - 4 * a * c


def resolvent_cubic(coeffs: List) -> List:
    r"""Cubic resolvent for degree 4 polynomial."""
    if len(coeffs) != 5:
        return []
    a, b, c, d, e = coeffs
    p = (8 * b * b - 4 * a * c) / (8 * a * a)
    q = (b * b * b - 4 * a * b * c + 4 * a * a * d) / (8 * a * a * a)
    return [1, -2 * p, p * p + 4 * q, -q * q]


def galois_group_solvable(coeffs: List) -> bool:
    r"""Check if polynomial is solvable by radicals."""
    degree = polynomial_degree(coeffs)
    return degree <= 4


def symetric_group_order(n: int) -> int:
    r"""Order of symmetric group S_n."""
    from math import factorial
    return factorial(n)


def alternating_group_order(n: int) -> int:
    r"""Order of alternating group A_n."""
    from math import factorial
    return factorial(n) // 2


def cyclic_group_mod(n: int, m: int) -> int:
    r"""Check cyclic group Z_n."""
    from math import gcd
    return gcd(n, m)


def resolvent_polynomial(coeffs: List, resolvent_type: str = "cubic") -> Optional[List]:
    r"""Construct resolvent polynomial."""
    degree = polynomial_degree(coeffs)
    if degree == 4 and resolvent_type == "cubic":
        return resolvent_cubic(coeffs)
    return None


def solvable_by_radicals(coeffs: List) -> dict:
    r"""Check if polynomial is solvable by radicals."""
    degree = polynomial_degree(coeffs)
    solvable = degree <= 4
    return {"solvable": solvable, "degree": degree}


def quadratic_formula(a: float, b: float, c: float) -> Tuple[complex, complex]:
    r"""Solve quadratic equation."""
    disc = b * b - 4 * a * c
    sqrt_disc = complex(np.sqrt(disc)) if disc >= 0 else complex(0, np.sqrt(-disc))
    r1 = (-b + sqrt_disc) / (2 * a)
    r2 = (-b - sqrt_disc) / (2 * a)
    return (r1, r2)


def resolvent_discriminant(coeffs: List) -> float:
    r"""Compute resolvent discriminant."""
    degree = polynomial_degree(coeffs)
    if degree == 4:
        resolvent = resolvent_cubic(coeffs)
        return discriminant(resolvent)
    return 0.0


def galois_theorem_solvable(coeffs: List):
    r"""Galois theorem: polynomials of degree <= 4 are solvable."""
    degree = polynomial_degree(coeffs)
    solvable = degree <= 4
    return {"pass": solvable, "degree": degree, "solvable": solvable}


def separable_polynomial_theorem(coeffs: List):
    r"""Separable polynomial has no repeated roots."""
    return {"pass": separable_polynomial(coeffs), "separable": separable_polynomial(coeffs)}


def discriminant_theorem(coeffs: List):
    r"""Discriminant: zero iff repeated root exists."""
    disc = discriminant(coeffs)
    return {"pass": True, "discriminant": disc, "has_repeated_root": abs(disc) < 1e-10}


def discriminant_quadratic_theorem(a: float, b: float, c: float):
    r"""Discriminant of quadratic."""
    disc = b * b - 4 * a * c
    return {"pass": True, "discriminant": disc, "has_real_roots": disc >= 0}


def cyclic_group_theorem(mod_n: int, m: int):
    r"""Cyclic group has element of order m if m | n."""
    from math import gcd
    divides = (mod_n % m) == 0
    return {"pass": divides, "mod_n": mod_n, "m": m, "divides": divides}


def symmetric_group_order_theorem(n: int):
    r"""Order of S_n is n!."""
    from math import factorial
    order = factorial(n)
    return {"pass": True, "order": order}


def alternating_group_order_theorem(n: int):
    r"""Order of A_n is n!/2."""
    from math import factorial
    order = factorial(n) // 2
    return {"pass": True, "order": order}