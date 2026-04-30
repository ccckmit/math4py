"""differential_geometry - 微分幾何模組。"""

from .function import (
    christoffel_symbols,
    covariant_derivative,
    geodesic_distance_sphere,
    geodesic_equation,
    levi_civita_connection,
    lie_derivative,
    metric_tensor_sphere,
    ricci_tensor,
    riemann_curvature_tensor,
    scalar_curvature,
)
from .tensor_algebra import (
    Tensor,
    contract,
    inverse_metric,
    kronecker_delta,
    lower_index,
    metric_tensor,
    raise_index,
    tensor_product,
)
from .theorem import (
    divergence_theorem_check,
    gauss_bonnet_theorem,
    ricci_tensor_trace,
    riemann_tensor_symmetry,
    stokes_theorem_check,
)

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
    "Tensor",
    "tensor_product",
    "contract",
    "raise_index",
    "lower_index",
    "metric_tensor",
    "inverse_metric",
    "kronecker_delta",
    "gauss_bonnet_theorem",
    "stokes_theorem_check",
    "divergence_theorem_check",
    "riemann_tensor_symmetry",
    "ricci_tensor_trace",
]
