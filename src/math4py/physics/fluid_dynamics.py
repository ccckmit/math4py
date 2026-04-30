"""流體動力學（Fluid Dynamics）基礎函數。"""

import numpy as np


def continuity_equation(rho1: float, A1: float, v1: float,
                       rho2: float, A2: float, v2: float) -> bool:
    """連續方程式 ρ1 A1 v1 = ρ2 A2 v2。"""
    return abs(rho1 * A1 * v1 - rho2 * A2 * v2) < 1e-10


def bernoulli_equation(P1: float, rho: float, v1: float, h1: float,
                       P2: float, v2: float, h2: float, g: float = 9.81) -> bool:
    """白努利方程 P1 + ½ρv1² + ρgh1 = P2 + ½ρv2² + ρgh2。"""
    left = P1 + 0.5 * rho * v1**2 + rho * g * h1
    right = P2 + 0.5 * rho * v2**2 + rho * g * h2
    return abs(left - right) < 1e-10


def reynolds_number(rho: float, v: float, L: float, mu: float) -> float:
    """雷諾數 Re = ρvL/μ。"""
    if mu == 0:
        return float('inf')
    return rho * v * L / mu


def drag_force(Cd: float, rho: float, A: float, v: float) -> float:
    """阻力 Fd = ½ Cd ρ A v²。"""
    return 0.5 * Cd * rho * A * v**2


def hydrostatic_pressure(rho: float, g: float, h: float) -> float:
    """靜水壓力 P = ρgh。"""
    return rho * g * h


def mach_number(v: float, c: float) -> float:
    """馬赫數 Ma = v/c。"""
    if c == 0:
        return float('inf')
    return v / c


__all__ = [
    "continuity_equation",
    "bernoulli_equation",
    "reynolds_number",
    "drag_force",
    "hydrostatic_pressure",
    "mach_number",
]
