"""Tensor module - 支援梯度的張量運算。"""

from .tensor import Tensor
from . import function as F

__all__ = ["Tensor", "F"]
