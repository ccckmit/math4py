"""光學（Optics）基礎函數。"""

import numpy as np
from typing import Tuple


def snells_law(n1: float, n2: float, theta1: float) -> float:
    """斯涅爾定律 n1 sin(θ1) = n2 sin(θ2)。"""
    sin_theta2 = n1 * np.sin(theta1) / n2
    if abs(sin_theta2) > 1:
        return float('inf')  # 全反射
    return np.arcsin(sin_theta2)


def critical_angle(n1: float, n2: float) -> float:
    """臨界角 θ_c = arcsin(n2/n1)（當 n1 > n2）。"""
    if n1 <= n2:
        return float('inf')  # 無全反射
    return np.arcsin(n2 / n1)


def lensmaker_equation(f: float = None, n: float = None, 
                      R1: float = None, R2: float = None) -> float:
    """透鏡製造者公式 1/f = (n-1)(1/R1 - 1/R2)。"""
    if f is None and all([n, R1, R2]):
        return 1.0 / ((n - 1.0) * (1.0/R1 - 1.0/R2))
    return 0.0


def magnification(d_i: float, d_o: float) -> float:
    """放大率 M = -d_i/d_o。"""
    if d_o == 0:
        return float('inf')
    return -d_i / d_o


__all__ = [
    "snells_law",
    "critical_angle",
    "lensmaker_equation",
    "magnification",
]
