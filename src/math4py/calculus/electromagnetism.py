"""電磁學數學函數。

基於向量微積分實現電磁學核心公式與馬克士威方程組驗證。
"""

from typing import Callable, Tuple
import numpy as np
from .vector_calculus import divergence, curl_3d


# 簡化常數 (取 k=1/(4πε0)=1, μ0/(4π)=1)
_K_E = 1.0
_K_B = 1.0


def coulomb_electric_field(q: float, r_obs: np.ndarray, r_src: np.ndarray) -> np.ndarray:
    """點電荷的電場 (庫侖定律)。

    Args:
        q: 電荷量
        r_obs: 觀察點座標 (x, y, z)
        r_src: 電荷位置座標 (x, y, z)

    Returns:
        電場向量 E
    """
    r_vec = r_obs.astype(float) - r_src.astype(float)
    r = np.linalg.norm(r_vec)
    if r < 1e-12:
        return np.zeros(3)
    return _K_E * q * r_vec / (r ** 3)


def biot_savart_field(I: float, dl: np.ndarray, r_obs: np.ndarray, r_src: np.ndarray) -> np.ndarray:
    """電流元的磁場 (畢奧-薩伐爾定律)。

    Args:
        I: 電流強度
        dl: 電流元向量 (dx, dy, dz)
        r_obs: 觀察點座標 (x, y, z)
        r_src: 電流元位置座標 (x, y, z)

    Returns:
        磁場向量 B
    """
    r_vec = r_obs.astype(float) - r_src.astype(float)
    r = np.linalg.norm(r_vec)
    if r < 1e-12:
        return np.zeros(3)
    return _K_B * I * np.cross(dl, r_vec) / (r ** 3)


def gauss_electric_law(E: Callable, point: np.ndarray, h: float = 1e-5) -> float:
    """驗證高斯電場定律 ∇·E = ρ/ε0。

    Args:
        E: 電場函數 (x,y,z) -> (Ex,Ey,Ez)
        point: 觀察點
        h: 步長

    Returns:
        電場散度值
    """
    return divergence(E, point, h)


def gauss_magnetic_law(B: Callable, point: np.ndarray, h: float = 1e-5) -> float:
    """驗證高斯磁場定律 ∇·B = 0。

    Args:
        B: 磁場函數 (x,y,z) -> (Bx,By,Bz)
        point: 觀察點
        h: 步長

    Returns:
        磁場散度值
    """
    return divergence(B, point, h)


def faraday_law(E: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """驗證法拉第感應定律 ∇×E = -∂B/∂t。

    靜電場下 ∂B/∂t=0，旋度應為零。

    Args:
        E: 電場函數 (x,y,z) -> (Ex,Ey,Ez)
        point: 觀察點
        h: 步長

    Returns:
        電場旋度值
    """
    return curl_3d(E, point, h)


def ampere_law(B: Callable, point: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """驗證安培环路定律 ∇×B = μ0(J + ε0∂E/∂t)。

    穩恆電流下 ∂E/∂t=0，旋度與電流密度相關。

    Args:
        B: 磁場函數 (x,y,z) -> (Bx,By,Bz)
        point: 觀察點
        h: 步長

    Returns:
        磁場旋度值
    """
    return curl_3d(B, point, h)


def lorentz_force(q: float, E: np.ndarray, v: np.ndarray, B: np.ndarray) -> np.ndarray:
    """洛倫茲力 F = q(E + v × B)。

    Args:
        q: 電荷量
        E: 電場向量
        v: 速度向量
        B: 磁場向量

    Returns:
        力向量 F
    """
    return q * (E + np.cross(v, B))


def poynting_vector(E: np.ndarray, B: np.ndarray) -> np.ndarray:
    """坡印廷矢量 S = (1/μ0) E × B (簡化取 1/μ0=1)。

    Args:
        E: 電場向量
        B: 磁場向量

    Returns:
        能流密度向量 S
    """
    return np.cross(E, B)


__all__ = [
    "coulomb_electric_field",
    "biot_savart_field",
    "gauss_electric_law",
    "gauss_magnetic_law",
    "faraday_law",
    "ampere_law",
    "lorentz_force",
    "poynting_vector",
]
