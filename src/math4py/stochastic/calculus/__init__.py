"""
calculus — Stochastic calculus module for math4py

Modules:
- ito : 伊藤積分與伊藤引理
- sde : 隨機微分方程求解器（Euler-Maruyama、Milstein）
- options : 期權定價（Black-Scholes，美式 / 歐式）
"""

from math4py.plot.rplot_stochastic import brownian_motion, ito_integral_plot, options_plot

from ..process import (
    BrownianBridge,
    BrownianMotion,
    GeometricBrownianMotion,
    OrnsteinUhlenbeck,
)
from .ito import ItoIntegral, ito_lemma_demo
from .options import AmericanOption, BlackScholes
from .sde import SDESolver

__all__ = [
    "BrownianMotion",
    "GeometricBrownianMotion",
    "OrnsteinUhlenbeck",
    "BrownianBridge",
    "ItoIntegral",
    "ito_lemma_demo",
    "SDESolver",
    "BlackScholes",
    "AmericanOption",
    "brownian_motion",
    "ito_integral_plot",
    "options_plot",
]
