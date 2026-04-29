r"""Differential geometry and relativity tensor operations."""

from typing import Optional

import numpy as np

from ..tensor.tensor import Tensor


def metric_inverse(g: Tensor) -> Tensor:
    r"""Compute inverse metric tensor.
    
    g^{ij} = (g_{ij})^{-1}
    """
    g_inv = np.linalg.inv(g.data)
    return Tensor(g_inv)


def metric_determinant(g: Tensor) -> Tensor:
    r"""Compute metric determinant.
    
    g = det(g_{ij})
    """
    det = np.linalg.det(g.data)
    return Tensor(det)


def sqrt_metric_det(g: Tensor) -> Tensor:
    r"""Compute sqrt(|g|) for volume element.
    
    Lorentzian: sqrt(-g)
    Riemannian: sqrt(g)
    """
    det = np.linalg.det(g.data)
    return Tensor(np.sqrt(abs(det)))


def christoffel(g: Tensor, coords: Optional[Tensor] = None) -> Tensor:
    r"""Compute Christoffel symbols (Levi-Civita connection).
    
    Gamma^k_{ij} = (1/2) g^{ks} (g_{js,i} + g_{si,j} - g_{ij,s})
    
    For Cartesian coordinates (identity metric),Christoffel symbols vanish.
    """
    n = g.shape[0]
    g_inv = np.linalg.inv(g.data)
    g_data = g.data

    christoffel_symbols = np.zeros((n, n, n))

    if coords is None:
        return Tensor(christoffel_symbols)

    coord_data = coords.data
    for rho in range(n):
        for mu in range(n):
            for nu in range(n):
                sum_val = 0.0
                for sigma in range(n):
                    dg_jsigma = 0.0
                    dg_sigma_i = 0.0
                    dg_ij = 0.0

                    if mu + 1 < n and sigma + 1 < n:
                        dg_jsigma = (g_data[nu, sigma] - 0) / 1.0
                    if sigma + 1 < n and mu + 1 < n:
                        dg_sigma_i = (g_data[sigma, mu] - 0) / 1.0
                    if mu + 1 < n and nu + 1 < n:
                        dg_ij = (g_data[mu, nu] - 0) / 1.0

                    sum_val += g_inv[rho, sigma] * (dg_jsigma + dg_sigma_i - dg_ij)
                christoffel_symbols[rho, mu, nu] = 0.5 * sum_val

    return Tensor(christoffel_symbols)


def covariant_derivative(v: Tensor, g: Tensor, coord: Optional[Tensor] = None) -> Tensor:
    r"""Compute covariant derivative.
    
    (nabla_i v)^j = v^j_{|i} = v^j_{,i} + Gamma^j_{ik} v^k
    """
    gamma = christoffel(g, coord)
    result = v.data + np.einsum("ijk,k->ij", gamma.data, v.data)
    return Tensor(result)


def riemann_curvature(g: Tensor, coord: Optional[Tensor] = None) -> Tensor:
    r"""Compute Riemann curvature tensor.
    
    R^i_{jkl} = Gamma^i_{jl,k} - Gamma^i_{jk,l}
                          + Gamma^i_{mk} Gamma^m_{jl} - Gamma^i_{ml} Gamma^m_{jk}
    """
    n = g.shape[0]
    gamma = christoffel(g, coord)

    R = np.zeros((n, n, n, n))

    for rho in range(n):
        for mu in range(n):
            for nu in range(n):
                for sigma in range(n):
                    term3 = 0.0
                    term4 = 0.0
                    for lam in range(n):
                        term3 += gamma.data[rho, nu, lam] * gamma.data[lam, mu, sigma]
                        term4 += gamma.data[rho, sigma, lam] * gamma.data[lam, mu, nu]
                    R[rho, mu, nu, sigma] = term3 - term4

    return Tensor(R)


def ricci_tensor(R: Tensor) -> Tensor:
    r"""Compute Ricci tensor (contraction of Riemann).
    
    R_{ij} = R^k_{ikj}
    """
    R_data = R.data
    n = R_data.shape[1]
    ricci = np.zeros((n, n))
    for mu in range(n):
        for nu in range(n):
            ricci[mu, nu] = R_data[mu, nu, mu, nu]
    return Tensor(ricci)


def ricci_scalar(R: Tensor, g: Tensor) -> Tensor:
    r"""Compute Ricci scalar.
    
    R = g^{ij} R_{ij}
    """
    g_inv = np.linalg.inv(g.data)
    R_data = R.data
    R_scalar = np.sum(g_inv * R_data)
    return Tensor(R_scalar)


def einstein_tensor(R: Tensor, g: Tensor) -> Tensor:
    r"""Compute Einstein tensor.
    
    G_{ij} = R_{ij} - (1/2) g_{ij} R
    """
    R_scalar = ricci_tensor(R).data
    g_data = g.data
    n = g.shape[0]
    G = np.zeros((n, n))
    for mu in range(n):
        for nu in range(n):
            G[mu, nu] = R.data[mu, nu] - 0.5 * g_data[mu, nu] * R_scalar
    return Tensor(G)


def einstein_equation(G: Tensor, k: float = 8 * np.pi, T: Optional[Tensor] = None) -> Tensor:
    r"""Einstein field equation.
    
    G_{ij} = k T_{ij}
    """
    if T is None:
        return G
    return G - Tensor(k * T.data)


def schwarzschild_metric(M: float, r: Tensor) -> Tensor:
    r"""Schwarzschild metric (spherically symmetric static black hole).
    
    ds^2 = -(1-2GM/r)c^2dt^2 + (1-2GM/r)^{-1}dr^2 + r^2 dOmega^2
    """
    G = 1.0
    c = 1.0
    rs = 2 * G * M / c**2

    factor = 1 - rs / r.data[0]
    old_settings = np.seterr(divide="ignore", invalid="ignore")
    g = np.diag([-1/factor, 1/factor, r.data[0]**2, r.data[0]**2])
    np.seterr(**old_settings)
    return Tensor(g)


def friedmann_metric(t: Tensor, k: float = 0, lambda_: float = 0) -> Tensor:
    r"""FLRW metric (Friedmann-Lemaitre-Robertson-Walker).
    
    Standard cosmological metric.
    """
    a = t.data[0]
    if k == 0:
        g = np.diag([-1, a**2, a**2, a**2])
    elif k == 1:
        g = np.diag([-1, a**2/(1-a.data[0]**2), a**2, a**2])
    else:
        g = np.diag([-1, a**2/(1+a.data[0]**2), a**2, a**2])
    return Tensor(g)


def energy_momentum_perfect_fluid(rho: float, p: float, u: Tensor) -> Tensor:
    r"""Energy-momentum tensor for perfect fluid.
    
    T_{ij} = (rho + p) u_i u_j + p g_{ij}
    """
    g = np.diag([-1, 1, 1, 1])
    u_u = np.outer(u.data, u.data)
    T = (rho + p) * u_u + p * g
    return Tensor(T)


def geodesic_equation(x: Tensor, gamma: Tensor) -> Tensor:
    r"""Geodesic equation.
    
    d^2x^i/dlambda^2 + Gamma^i_{jk} dx^j/dlambda dx^k/dlambda = 0
    """
    dx = x.data
    gamma_data = gamma.data

    accel = np.einsum("ijk,ij->k", gamma_data, np.outer(dx, dx))
    return Tensor(-accel)


def Weyl_tensor(g: Tensor, R: Tensor) -> Tensor:
    r"""Weyl curvature tensor (conformal curvature).
    
    C_{ijkl} = R_{ijkl} - (g_{i[k}R_{j]l} + (1/3)R g_{i[k}g_{j]l})
    """
    n = g.shape[0]
    g_data = g.data
    R_data = R.data

    C = np.zeros((n, n, n, n))

    for mu in range(n):
        for nu in range(n):
            for rho in range(n):
                for sigma in range(n):
                    term1 = R_data[mu, nu, rho, sigma]

                    g_mr = g_data[mu, rho]
                    g_ns = g_data[nu, sigma]
                    g_ms = g_data[mu, sigma]
                    g_nr = g_data[nu, rho]

                    term2 = 0.5 * (g_mr * R_data[nu, sigma] - g_ms * R_data[nu, rho])
                    term3 = 0.5 * (g_ns * R_data[mu, rho] - g_nr * R_data[mu, sigma])

                    term4 = (1.0/3.0) * R_data[mu, nu] * (g_mr * g_ns - g_ms * g_nr)

                    C[mu, nu, rho, sigma] = term1 + term2 + term3 + term4

    return Tensor(C)


def kretschmann_scalar(R: Tensor) -> Tensor:
    r"""Kretschmann scalar.
    
    K = R_{ijkl} R^{ijkl}
    
    Measure of spacetime curvature.
    """
    R_data = R.data
    K = np.sum(R_data * R_data)
    return Tensor(K)


def ADM_energy(g: Tensor) -> Tensor:
    r"""ADM energy (Arnowitt-Deser-Misner).
    
    Total energy in asymptotically flat spacetime.
    """
    g_inv = np.linalg.inv(g.data)
    div_term = np.sum(g_inv * np.gradient(g.data))
    E = (1.0 / (16 * np.pi)) * np.sum(div_term)
    return Tensor(E)
