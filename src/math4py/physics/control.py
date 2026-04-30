"""控制理論（Control Theory）基礎函數。"""

import numpy as np


def transfer_function(num: list, den: list, dt: float = None):
    """建立傳遞函數 G(s) = num(s) / den(s)。"""
    return {"num": num, "den": den, "dt": dt}


def routh_hurwitz(char_poly: list) -> bool:
    """Routh-Hurwitz 穩定性判據。"""
    roots = np.roots(char_poly)
    return np.all(np.real(roots) < 0)


def controllability_matrix(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """能控性矩陣。"""
    n = A.shape[0]
    m = B.shape[1]
    Qc = np.zeros((n, n * m))
    for i in range(n):
        Qc[:, i * m : (i + 1) * m] = np.linalg.matrix_power(A, i) @ B
    return Qc


__all__ = [
    "transfer_function",
    "routh_hurwitz",
    "controllability_matrix",
]
