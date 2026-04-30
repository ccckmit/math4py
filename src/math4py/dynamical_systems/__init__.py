"""dynamical_systems - 動力系統模組。"""

from .function import (
    euler_method,
    runge_kutta_4,
    phase_space_trajectory,
    fixed_point_analysis,
    linear_stability_analysis,
    lyapunov_exponent,
    lorenz_system,
    logistic_map,
    bifurcation_diagram,
)
from .theorem import (
    existence_uniqueness_theorem,
    linear_stability_theorem,
    conservation_law_check,
    limit_cycle_detection,
    chaos_sensitivity_check,
    bifurcation_theorem,
)

__all__ = [
    "euler_method",
    "runge_kutta_4",
    "phase_space_trajectory",
    "fixed_point_analysis",
    "linear_stability_analysis",
    "lyapunov_exponent",
    "lorenz_system",
    "logistic_map",
    "bifurcation_diagram",
    "existence_uniqueness_theorem",
    "linear_stability_theorem",
    "conservation_law_check",
    "limit_cycle_detection",
    "chaos_sensitivity_check",
    "bifurcation_theorem",
]
