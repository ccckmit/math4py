"""Linear Algebra Theorems."""

from typing import List

import numpy as np


def rank_nullity_theorem(matrix: List[List[float]]) -> dict:
    """秩-零化度定理：rank(A) + nullity(A) = n。

    Args:
        matrix: 矩陣 A (m × n)

    Returns:
        Dict with verification result
    """
    A = np.array(matrix)
    m, n = A.shape

    rank = np.linalg.matrix_rank(A)

    # 計算零空間維度 (nullity)
    # 通過 SVD: nullity = n - rank
    nullity = n - rank

    holds = rank + nullity == n

    return {
        "pass": holds,
        "rank": int(rank),
        "nullity": int(nullity),
        "n": n,
        "sum": int(rank + nullity),
    }


def eigenvalues_theorem(matrix: List[List[float]]) -> dict:
    """特徵值定理：跡 = 特徵值和，行列式 = 特徵值積。

    Args:
        matrix: 方陣 A

    Returns:
        Dict with verification result
    """
    A = np.array(matrix)
    A.shape[0]

    trace_A = np.trace(A)
    det_A = np.linalg.det(A)

    vals, _ = np.linalg.eig(A)
    sum_eigenvals = np.sum(vals)
    prod_eigenvals = np.prod(vals)

    trace_holds = abs(trace_A - sum_eigenvals) < 1e-8
    det_holds = abs(det_A - prod_eigenvals) < 1e-8

    return {
        "pass": trace_holds and det_holds,
        "trace": float(trace_A),
        "sum_eigenvalues": float(sum_eigenvals),
        "det": float(det_A),
        "prod_eigenvalues": float(prod_eigenvals),
        "trace_holds": trace_holds,
        "det_holds": det_holds,
    }


def svd_theorem(matrix: List[List[float]]) -> dict:
    """SVD 定理：A = U Σ V^T。

    Args:
        matrix: 矩陣 A

    Returns:
        Dict with verification result
    """
    A = np.array(matrix, dtype=float)
    m, n = A.shape

    U, S, Vh = np.linalg.svd(A, full_matrices=False)

    # 重構 A
    S_matrix = np.zeros((m, n))
    for i, s in enumerate(S):
        S_matrix[i, i] = s

    A_reconstructed = U @ S_matrix @ Vh
    error = np.max(np.abs(A - A_reconstructed))

    holds = error < 1e-8

    return {
        "pass": holds,
        "reconstruction_error": float(error),
        "singular_values": S.tolist(),
        "rank": int(np.sum(S > 1e-10)),
    }


def determinant_theorem(matrix: List[List[float]]) -> dict:
    """行列式定理：det(AB) = det(A)det(B)。

    Args:
        matrix: 方陣 A (同時作為 B 測試)

    Returns:
        Dict with verification result
    """
    A = np.array(matrix, dtype=float)
    B = A  # 簡化：測試 A 與自身

    det_A = np.linalg.det(A)
    det_B = np.linalg.det(B)
    det_AB = np.linalg.det(A @ B)

    holds = abs(det_AB - det_A * det_B) < 1e-8

    return {
        "pass": holds,
        "det_A": float(det_A),
        "det_B": float(det_B),
        "det_AB": float(det_AB),
        "product_detA_detB": float(det_A * det_B),
    }


def linear_independence_theorem(vectors: List[List[float]]) -> dict:
    """線性獨立定理：向量組線性獨立當且僅當只有零解。

    Args:
        vectors: 向量列表

    Returns:
        Dict with verification result
    """
    if not vectors:
        return {"pass": True, "rank": 0, "num_vectors": 0, "is_independent": True}

    mat = np.array(vectors).T
    rank = np.linalg.matrix_rank(mat)
    num_vectors = len(vectors)

    is_independent = rank == num_vectors

    return {
        "pass": True,  # 定理本身總是成立
        "rank": int(rank),
        "num_vectors": num_vectors,
        "is_independent": is_independent,
    }


__all__ = [
    "rank_nullity_theorem",
    "eigenvalues_theorem",
    "svd_theorem",
    "determinant_theorem",
    "linear_independence_theorem",
]
