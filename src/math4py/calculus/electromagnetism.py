"""電磁學數學函數。

基於向量微積分實現電磁學核心公式與馬克士威方程組驗證。
"""

from typing import Callable, Tuple
import numpy as np
from .vector_calculus import divergence, curl_3d, laplacian


# 真空常數 (簡化取 ε0=1, μ0=1, 故 c=1)
_EPS0 = 1.0
_MU0 = 1.0
_C = 1.0 / np.sqrt(_EPS0 * _MU0)


def coulomb_electric_field(q: float, r_obs: np.ndarray, r_src: np.ndarray) -> np.ndarray:
    """點電荷的電場 (庫侖定律)。"""
    r_vec = r_obs.astype(float) - r_src.astype(float)
    r = np.linalg.norm(r_vec)
    if r < 1e-12:
        return np.zeros(3)
    return q * r_vec / (4.0 * np.pi * _EPS0 * r ** 3)


def biot_savart_field(I: float, dl: np.ndarray, r_obs: np.ndarray, r_src: np.ndarray) -> np.ndarray:
    """電流元的磁場 (畢奧-薩伐爾定律)。"""
    r_vec = r_obs.astype(float) - r_src.astype(float)
    r = np.linalg.norm(r_vec)
    if r < 1e-12:
        return np.zeros(3)
    return _MU0 / (4.0 * np.pi) * I * np.cross(dl, r_vec) / (r ** 3)


def gauss_electric_law(E: Callable, point: np.ndarray, h: float = 1e-5) -> float:
    """高斯電場定律 ∇·E = ρ/ε0。"""
    return divergence(E, point, h)


def gauss_magnetic_law(B: Callable, point: np.ndarray, h: float = 1e-5) -> float:
    """高斯磁場定律 ∇·B = 0。"""
    return divergence(B, point, h)


def faraday_law(E: Callable, B: Callable, point: np.ndarray, dt: float = 1e-5, h: float = 1e-5) -> np.ndarray:
    """法拉第感應定律 ∇×E = -∂B/∂t。

    Args:
        E: 電場函數 (x,y,z) -> (Ex,Ey,Ez)
        B: 磁場函數 (x,y,z) -> (Bx,By,Bz)
        point: 觀察點
        dt: 時間步長
        h: 空間步長

    Returns:
        ∇×E + ∂B/∂t 應接近零
    """
    curl_E = curl_3d(E, point, h)
    B_now = np.array(B(*point))
    B_future = np.array(B(point[0], point[1], point[2] + dt))
    dB_dt = (B_future - B_now) / dt
    return curl_E + dB_dt


def ampere_maxwell_law(B: Callable, E: Callable, point: np.ndarray, dt: float = 1e-5, h: float = 1e-5) -> np.ndarray:
    """安培-馬克士威定律 ∇×B = μ0 J + μ0 ε0 ∂E/∂t。

    真空無電流時：∇×B = μ0 ε0 ∂E/∂t

    Args:
        B: 磁場函數
        E: 電場函數
        point: 觀察點
        dt: 時間步長
        h: 空間步長

    Returns:
        ∇×B - μ0 ε0 ∂E/∂t 應接近零
    """
    curl_B = curl_3d(B, point, h)
    E_now = np.array(E(*point))
    E_future = np.array(E(point[0], point[1], point[2] + dt))
    dE_dt = (E_future - E_now) / dt
    return curl_B - _MU0 * _EPS0 * dE_dt


def electromagnetic_wave_equation(E: Callable, point: np.ndarray, dt: float = 1e-5, h: float = 1e-5) -> np.ndarray:
    """電磁波波動方程 ∇²E = μ0 ε0 ∂²E/∂t²。

    Args:
        E: 電場函數
        point: 觀察點
        dt: 時間步長
        h: 空間步長

    Returns:
        ∇²E - μ0 ε0 ∂²E/∂t² 應接近零
    """
    lap_E = laplacian(E, point, h)
    E_now = np.array(E(*point))
    E_future = np.array(E(point[0], point[1], point[2] + dt))
    E_past = np.array(E(point[0], point[1], point[2] - dt))
    d2E_dt2 = (E_future - 2*E_now + E_past) / (dt ** 2)
    return lap_E - _MU0 * _EPS0 * d2E_dt2


def electromagnetic_wave_speed() -> float:
    """電磁波在真空中的速度 c = 1/√(ε0 μ0)。

    Returns:
        光速 c
    """
    return 1.0 / np.sqrt(_EPS0 * _MU0)


def plane_wave_E(k: np.ndarray, omega: float, r: np.ndarray, t: float) -> np.ndarray:
    """平面電磁波電場 E = E0 cos(k·r - ωt)。

    Args:
        k: 波向量
        omega: 角頻率
        r: 位置向量
        t: 時間

    Returns:
        電場向量
    """
    phase = np.dot(k, r) - omega * t
    E0 = np.array([1.0, 0.0, 0.0])
    return E0 * np.cos(phase)


def plane_wave_B(k: np.ndarray, omega: float, r: np.ndarray, t: float) -> np.ndarray:
    """平面電磁波磁場 B = (k/|k|) × E / c。

    Args:
        k: 波向量
        omega: 角頻率
        r: 位置向量
        t: 時間

    Returns:
        磁場向量
    """
    k_hat = k / np.linalg.norm(k)
    E = plane_wave_E(k, omega, r, t)
    return np.cross(k_hat, E) / _C


def dispersion_relation(k: np.ndarray, omega: float) -> float:
    """色散關係 ω = c|k|。

    Args:
        k: 波向量
        omega: 角頻率

    Returns:
        ω - c|k| 應接近零
    """
    return omega - _C * np.linalg.norm(k)


def lorentz_force(q: float, E: np.ndarray, v: np.ndarray, B: np.ndarray) -> np.ndarray:
    """洛倫茲力 F = q(E + v × B)。"""
    return q * (E + np.cross(v, B))


def poynting_vector(E: np.ndarray, B: np.ndarray) -> np.ndarray:
    """坡印廷矢量 S = (1/μ0) E × B。"""
    return np.cross(E, B) / _MU0


__all__ = [
    "coulomb_electric_field",
    "biot_savart_field",
    "gauss_electric_law",
    "gauss_magnetic_law",
    "faraday_law",
    "ampere_maxwell_law",
    "electromagnetic_wave_equation",
    "electromagnetic_wave_speed",
    "plane_wave_E",
    "plane_wave_B",
    "dispersion_relation",
    "lorentz_force",
    "poynting_vector",
]
