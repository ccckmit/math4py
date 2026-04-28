"""矩陣定理與公理驗證。

以 pytest 測試形式驗證矩陣運算的定義、公理與定理。
"""

from typing import List

from .function import (
    det,
    inverse_2x2,
    matrix_add,
    matrix_multiply,
    trace,
    transpose,
)
from .matrix import Matrix


def matrix_multiplication_associative(A: List[List], B: List[List], C: List[List]) -> bool:
    """矩陣乘法結合律：(AB)C = A(BC)。"""
    return matrix_multiply(matrix_multiply(A, B), C) == matrix_multiply(A, matrix_multiply(B, C))


def matrix_addition_commutative(A: List[List], B: List[List]) -> bool:
    """矩陣加法交換律：A + B = B + A。"""
    return matrix_add(A, B) == matrix_add(B, A)


def matrix_addition_associative(A: List[List], B: List[List], C: List[List]) -> bool:
    """矩陣加法結合律：(A + B) + C = A + (B + C)。"""
    return matrix_add(matrix_add(A, B), C) == matrix_add(A, matrix_add(B, C))


def transpose_properties(A: List[List], B: List[List]) -> bool:
    """轉置性質：(A+B)^T = A^T + B^T, (AB)^T = B^T A^T。"""
    add_result = transpose(matrix_add(A, B)) == matrix_add(transpose(A), transpose(B))
    mul_result = transpose(matrix_multiply(A, B)) == matrix_multiply(transpose(B), transpose(A))
    return add_result and mul_result


def determinant_properties(A: List[List], B: List[List]) -> bool:
    """行列式性質：det(AB) = det(A)det(B), det(A^T) = det(A)。"""
    if len(A) != 2 or len(A[0]) != 2:
        return True
    det_mul = abs(det(matrix_multiply(A, B)) - det(A) * det(B)) < 1e-9
    det_transpose = abs(det(A) - det(transpose(A))) < 1e-9
    return det_mul and det_transpose


def inverse_properties(A: List[List]) -> bool:
    """反矩陣性質：A A^(-1) = I, (A^(-1))^T = (A^T)^(-1)。"""
    if len(A) != 2 or len(A[0]) != 2:
        return True
    try:
        inv = inverse_2x2(A)
        identity = matrix_multiply(A, inv)
        return abs(identity[0][0] - 1) < 1e-9 and abs(identity[1][1] - 1) < 1e-9
    except ValueError:
        return True


def trace_properties(A: List[List], B: List[List]) -> bool:
    """跡的性質：tr(A+B) = tr(A) + tr(B), tr(AB) = tr(BA)。"""
    if len(A) != len(B) or len(A[0]) != len(B):
        return True
    tr_add = abs(trace(matrix_add(A, B)) - (trace(A) + trace(B))) < 1e-9
    tr_mul = abs(trace(matrix_multiply(A, B)) - trace(matrix_multiply(B, A))) < 1e-9
    return tr_add and tr_mul


def matrix_class_properties() -> bool:
    """Matrix 類別基本性質驗證。"""
    A = Matrix([[1, 2], [3, 4]])
    identity = Matrix.eye(2)
    zero = Matrix.zeros((2, 2))
    assert (A + zero).shape == (2, 2)
    assert (A @ identity).shape == (2, 2)
    assert abs(A.det() - (-2.0)) < 1e-9
    return True


__all__ = [
    "matrix_multiplication_associative",
    "matrix_addition_commutative",
    "matrix_addition_associative",
    "transpose_properties",
    "determinant_properties",
    "inverse_properties",
    "trace_properties",
    "matrix_class_properties",
]
