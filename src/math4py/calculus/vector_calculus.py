"""向量微積分函數。

包含梯度、散度、旋度、拉普拉斯算子等向量微積分運算。
"""

from typing import Callable, Tuple
import numpy as np


def gradient(f: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """數值梯度 ∇f。

    Args:
        f: 純量函數 f(x, y, ...)
        point: 點座標
        h: 步長

    Returns:
        梯度向量
    """
    n = len(point)
    grad = np.zeros(n)
    for i in range(n):
        point_plus = point.copy().astype(float)
        point_minus = point.copy().astype(float)
        point_plus[i] += h
        point_minus[i] -= h
        grad[i] = (f(*point_plus) - f(*point_minus)) / (2 * h)
    return grad


def divergence(F: Callable, point: np.ndarray, h: float = 1e-5) -> float:
    """數值散度 ∇ · F。

    Args:
        F: 向量場 F(x, y, ...) = (F1, F2, ...)
        point: 點座標
        h: 步長

    Returns:
        散度值
    """
    n = len(point)
    div = 0.0
    for i in range(n):
        point_plus = point.copy().astype(float)
        point_minus = point.copy().astype(float)
        point_plus[i] += h
        point_minus[i] -= h
        Fi_plus = F(*point_plus)[i]
        Fi_minus = F(*point_minus)[i]
        div += (Fi_plus - Fi_minus) / (2 * h)
    return div


def curl_3d(F: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """三維數值旋度 ∇ × F。

    Args:
        F: 向量場 F = (F1, F2, F3)
        point: 點座標 (x, y, z)
        h: 步長

    Returns:
        旋度向量 (curl_x, curl_y, curl_z)
    """
    x, y, z = point.astype(float)
    F1 = lambda x, y, z: F(x, y, z)[0]
    F2 = lambda x, y, z: F(x, y, z)[1]
    F3 = lambda x, y, z: F(x, y, z)[2]

    curl = np.zeros(3)
    curl[0] = (F3(x, y + h, z) - F3(x, y - h, z) - F2(x, y, z + h) + F2(x, y, z - h)) / (2 * h)
    curl[1] = (F1(x, y, z + h) - F1(x, y, z - h) - F3(x + h, y, z) + F3(x - h, y, z)) / (2 * h)
    curl[2] = (F2(x + h, y, z) - F2(x - h, y, z) - F1(x, y + h, z) + F1(x, y - h, z)) / (2 * h)
    return curl


def laplacian(f: Callable, point: np.ndarray, h: float = 1e-5) -> float:
    """數值拉普拉斯算子 Δf。

    Args:
        f: 純量函數
        point: 點座標
        h: 步長

    Returns:
        拉普拉斯值
    """
    n = len(point)
    lap = 0.0
    center = f(*point)
    for i in range(n):
        point_plus = point.copy().astype(float)
        point_minus = point.copy().astype(float)
        point_plus[i] += h
        point_minus[i] -= h
        lap += (f(*point_plus) + f(*point_minus) - 2 * center) / (h ** 2)
    return lap


def directional_derivative(
    f: Callable,
    point: np.ndarray,
    direction: np.ndarray,
    h: float = 1e-5
) -> float:
    """方向導數 D_u f。

    Args:
        f: 純量函數
        point: 點座標
        direction: 方向向量
        h: 步長

    Returns:
        方向導數值
    """
    u = direction / np.linalg.norm(direction)
    return (f(*(point.astype(float) + h * u)) - f(*(point.astype(float) - h * u))) / (2 * h)


def vector_laplacian(F: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """向量拉普拉斯 ΔF。

    Args:
        F: 向量場
        point: 點座標
        h: 步長

    Returns:
        向量拉普拉斯值
    """
    n = len(point)
    result = np.zeros(n)
    for i in range(n):
        point_plus = point.copy().astype(float)
        point_minus = point.copy().astype(float)
        point_plus[i] += h
        point_minus[i] -= h
        Fi_plus = F(*point_plus)[i]
        Fi_minus = F(*point_minus)[i]
        Fi_center = F(*point)[i]
        result[i] = (Fi_plus + Fi_minus - 2 * Fi_center) / (h ** 2)
    return result


def jacobian(F: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """雅可比矩陣 J_F。

    Args:
        F: 向量場 F: R^n -> R^m
        point: 點座標
        h: 步長

    Returns:
        m x n 雅可比矩陣
    """
    m = len(F(*point))
    n = len(point)
    J = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            point_plus = point.copy().astype(float)
            point_minus = point.copy().astype(float)
            point_plus[j] += h
            point_minus[j] -= h
            Fi_plus = F(*point_plus)[i]
            Fi_minus = F(*point_minus)[i]
            J[i, j] = (Fi_plus - Fi_minus) / (2 * h)
    return J


def hessian(f: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """Hessian 矩陣。

    Args:
        f: 純量函數
        point: 點座標
        h: 步長

    Returns:
        n x n Hessian 矩陣
    """
    n = len(point)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            x_pp = point.copy().astype(float); x_pp[i] += h; x_pp[j] += h
            x_pm = point.copy().astype(float); x_pm[i] += h; x_pm[j] -= h
            x_mp = point.copy().astype(float); x_mp[i] -= h; x_mp[j] += h
            x_mm = point.copy().astype(float); x_mm[i] -= h; x_mm[j] -= h
            H[i, j] = (f(*x_pp) - f(*x_pm) - f(*x_mp) + f(*x_mm)) / (4 * h * h)
            H[j, i] = H[i, j]
    return H


def divergence_free_2d(F: Callable, point: np.ndarray, h: float = 1e-5) -> bool:
    """檢查二維向量場是否為無源場 (散度為零)。"""
    return abs(divergence(F, point, h)) < 1e-6


def curl_free_3d(F: Callable, point: np.ndarray, h: float = 1e-5) -> bool:
    """檢查三維向量場是否為保守場 (旋度為零)。"""
    return np.allclose(curl_3d(F, point, h), 0, atol=1e-6)


def potential_function_2d(F: Callable, h: float = 1e-5) -> Tuple[bool, float]:
    """檢查二維向量場是否有勢函數。"""
    test_point = np.array([1.0, 1.0])

    def F1(x, y): return F(x, y)[0]
    def F2(x, y): return F(x, y)[1]

    dF1_dy = (F1(1.0, 1.0 + h) - F1(1.0, 1.0 - h)) / (2 * h)
    dF2_dx = (F2(1.0 + h, 1.0) - F2(1.0 - h, 1.0)) / (2 * h)

    is_conservative = abs(dF1_dy - dF2_dx) < 1e-4
    phi = test_point[0] * test_point[1]
    return (is_conservative, phi)


__all__ = [
    "gradient",
    "divergence",
    "curl_3d",
    "laplacian",
    "directional_derivative",
    "vector_laplacian",
    "jacobian",
    "hessian",
    "divergence_free_2d",
    "curl_free_3d",
    "potential_function_2d",
]
