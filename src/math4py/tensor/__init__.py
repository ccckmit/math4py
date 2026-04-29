"""Tensor module - 張量運算。"""

from . import function as F
from . import differential_geometry as DG
from .tensor import Tensor

__all__ = ["Tensor", "F", "DG"]
