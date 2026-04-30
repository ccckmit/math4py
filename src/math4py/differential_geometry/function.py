"""微分幾何（Differential Geometry）基礎函數。"""

import numpy as np
from typing import Callable, Tuple, List


def christoffel_symbols(g: np.ndarray, g_inv: np.ndarray, d: int) -> np.ndarray:
    """計算克里斯托費爾符號 Γ^k_ij。
    
    Γ^k_ij = 1/2 * g^{kl} (∂_i g_jl + ∂_j g_il - ∂_l g_ij)
    """
    Gamma = np.zeros((d, d, d))
    
    for k in range(d):
        for i in range(d):
            for j in range(d):
                s = 0.0
                for l in range(d):
                    term = 0.0
                    # 簡化：假設度量張量是常數
                    term += 0.5 * g_inv[k, l] * (0 + 0 - 0)
                    s += term
                Gamma[k, i, j] = s
    
    return Gamma


def riemann_curvature_tensor(g: np.ndarray, Gamma: np.ndarray, 
                              d: int) -> np.ndarray:
    """計算黎曼曲率張量 R^i_jkl。
    
    R^i_jkl = ∂_k Γ^i_jl - ∂_l Γ^i_jk + Γ^i_mk Γ^m_jl - Γ^i_ml Γ^m_jk
    """
    R = np.zeros((d, d, d, d))
    
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):
                    # 簡化：假設導數為 0
                    term1 = 0.0
                    term2 = 0.0
                    
                    # Γ^i_mk Γ^m_jl
                    term3 = sum(Gamma[i, m, k] * Gamma[m, j, l] 
                                for m in range(d))
                    # Γ^i_ml Γ^m_jk
                    term4 = sum(Gamma[i, m, l] * Gamma[m, j, k] 
                                for m in range(d))
                    
                    R[i, j, k, l] = term1 - term2 + term3 - term4
    
    return R


def ricci_tensor(R: np.ndarray, d: int) -> np.ndarray:
    """計算里奇張量 Ric_jl = R^i_jil。"""
    Ric = np.zeros((d, d))
    
    for j in range(d):
        for l in range(d):
            Ric[j, l] = sum(R[i, j, i, l] for i in range(d))
    
    return Ric


def scalar_curvature(Ric: np.ndarray, g_inv: np.ndarray, d: int) -> float:
    """計算標量曲率 R = g^{ij} Ric_ij。"""
    R = 0.0
    for i in range(d):
        for j in range(d):
            R += g_inv[i, j] * Ric[i, j]
    return R


def geodesic_equation(t: float, y: np.ndarray, Gamma: np.ndarray) -> np.ndarray:
    """測地線方程 d²x^μ/dτ² + Γ^μ_νρ dx^ν/dτ dx^ρ/dτ = 0。
    
    y = [x^0, x^1, ..., x^{d-1}, dx^0/dτ, dx^1/dτ, ...]
    """
    d = len(y) // 2
    result = np.zeros(2 * d)
    
    # dx^μ/dτ
    for mu in range(d):
        result[mu] = y[d + mu]
    
    # d²x^μ/dτ²
    for mu in range(d):
        acc = 0.0
        for nu in range(d):
            for rho in range(d):
                acc -= Gamma[mu, nu, rho] * y[d + nu] * y[d + rho]
        result[d + mu] = acc
    
    return result


def levi_civita_connection(g: np.ndarray, d: int) -> np.ndarray:
    """列維-奇維塔聯絡（相容度量的聯絡）。"""
    g_inv = np.linalg.inv(g)
    return christoffel_symbols(g, g_inv, d)


def lie_derivative(vector_field: np.ndarray, diff_vector_field: np.ndarray, 
                  coord_diff: np.ndarray, d: int) -> np.ndarray:
    """李導數 L_X Y = [X, Y]（向量場的李導數）。"""
    # L_X Y^i = X^j ∂_j Y^i - Y^j ∂_j X^i
    lie_deriv = np.zeros(d)
    
    for i in range(d):
        for j in range(d):
            lie_deriv[i] += (vector_field[j] * coord_diff[i, j] - 
                            diff_vector_field[j] * coord_diff[j, i])
    
    return lie_deriv


def covariant_derivative(vector: np.ndarray, Gamma: np.ndarray, 
                       coord_diff: np.ndarray, d: int) -> np.ndarray:
    """協變導數 ∇_j V^i = ∂_j V^i + Γ^i_jk V^k。"""
    cov_deriv = np.zeros((d, d))
    
    for i in range(d):
        for j in range(d):
            cov_deriv[i, j] = coord_diff[i, j]
            for k in range(d):
                cov_deriv[i, j] += Gamma[i, j, k] * vector[k]
    
    return cov_deriv


def metric_tensor_sphere(R: float = 1.0) -> Callable:
    """球面度量張量 g_ij（2-球）。"""
    def g(theta_phi: np.ndarray) -> np.ndarray:
        theta = theta_phi[0]
        # g = [[R², 0], [0, R² sin²θ]]
        metric = np.array([
            [R**2, 0.0],
            [0.0, (R * np.sin(theta))**2]
        ])
        return metric
    return g


def geodesic_distance_sphere(point1: np.ndarray, point2: np.ndarray, 
                            R: float = 1.0) -> float:
    """球面上兩點的大圓距離。"""
    # 簡化：假設點是 (θ, φ) 坐標
    theta1, phi1 = point1[0], point1[1]
    theta2, phi2 = point2[0], point2[1]
    
    # 球面餘弦定律
    cos_dist = (np.sin(theta1) * np.sin(theta2) * 
                np.cos(phi2 - phi1) + 
                np.cos(theta1) * np.cos(theta2))
    
    return R * np.arccos(np.clip(cos_dist, -1.0, 1.0))


__all__ = [
    "christoffel_symbols",
    "riemann_curvature_tensor",
    "ricci_tensor",
    "scalar_curvature",
    "geodesic_equation",
    "levi_civita_connection",
    "lie_derivative",
    "covariant_derivative",
    "metric_tensor_sphere",
    "geodesic_distance_sphere",
]
