"""多項式運算函數。"""


def polynomial_eval(coeffs, x):
    """多項式求值 (Horner's method)。"""
    result = 0
    for c in coeffs:
        result = result * x + c
    return result


def polynomial_add(coeffs1, coeffs2):
    """多項式加法。"""
    len1 = len(coeffs1)
    len2 = len(coeffs2)
    n = max(len1, len2)
    result = [0.0] * n
    for i in range(len1):
        result[n - len1 + i] += coeffs1[i]
    for i in range(len2):
        result[n - len2 + i] += coeffs2[i]
    return result


def polynomial_multiply(coeffs1, coeffs2):
    """多項式乘法。"""
    n = len(coeffs1) + len(coeffs2) - 1
    result = [0] * n
    for i in range(len(coeffs1)):
        for j in range(len(coeffs2)):
            result[i + j] += coeffs1[i] * coeffs2[j]
    return result


__all__ = [
    "polynomial_eval",
    "polynomial_add",
    "polynomial_multiply",
]
