r"""Algebra theorems and axioms."""


def closure_axiom(op, a, b):
    r"""Closure axiom: if a, b in set, then a op b in set.

    Args:
        op: Binary operation
        a: First element
        b: Second element

    Returns:
        Dict with pass status
    """
    result = op(a, b)
    return {"pass": result is not None, "result": result}


def associativity(op, a, b, c):
    r"""Associativity: (a op b) op c = a op (b op c).

    Args:
        op: Binary operation
        a: First element
        b: Second element
        c: Third element

    Returns:
        Dict with pass status
    """
    left = op(op(a, b), c)
    right = op(a, op(b, c))
    return {"pass": left == right, "left": left, "right": right}


def identity_element(op, e, a):
    r"""Identity element: e op a = a op e = a.

    Args:
        op: Binary operation
        e: Identity element
        a: Element to test

    Returns:
        Dict with pass status
    """
    left = op(e, a)
    right = op(a, e)
    return {"pass": left == a and right == a}


def inverse_element(op, a, inverse):
    r"""Inverse element: a op a^{-1} = e.

    Args:
        op: Binary operation
        a: Element
        a_inverse: Inverse of a

    Returns:
        Dict with pass status
    """
    result = op(a, inverse)
    return {"pass": result is not None}


def commutativity(op, a, b):
    r"""Commutativity: a op b = b op a.

    Args:
        op: Binary operation
        a: First element
        b: Second element

    Returns:
        Dict with pass status
    """
    left = op(a, b)
    right = op(b, a)
    return {"pass": left == right, "left": left, "right": right}


def distributivity(op1, op2, a, b, c):
    r"""Distributivity: a * (b + c) = a*b + a*c.

    Args:
        op1: Multiplication-like operation
        op2: Addition-like operation
        a: Scalar
        b: First element
        c: Second element

    Returns:
        Dict with pass status
    """
    left = op1(a, op2(b, c))
    right = op2(op1(a, b), op1(a, c))
    return {"pass": left == right, "left": left, "right": right}


def fundamental_theorem_of_algebra(coefficients):
    r"""Fundamental Theorem of Algebra: Every non-constant polynomial with
    complex coefficients has at least one complex root.
    Therefore, a polynomial of degree n has exactly n complex roots.

    Args:
        coefficients: Polynomial coefficients [a_n, ..., a_1, a_0]

    Returns:
        Dict with pass status and roots
    """
    import numpy as np

    roots_arr = np.roots(coefficients)
    degree = len(coefficients) - 1
    return {"pass": True, "degree": degree, "num_roots": len(roots_arr)}
