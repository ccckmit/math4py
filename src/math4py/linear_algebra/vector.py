"""向量運算函數。"""

import numpy as np


def norm_vector(v):
    """向量長度 (歐幾里得範數)。"""
    return np.sqrt(sum(x * x for x in v))


def dot_product(v1, v2):
    """向量內積。"""
    return sum(a * b for a, b in zip(v1, v2))


def cross_product(v1, v2):
    """三維向量外積。"""
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    ]


__all__ = [
    "norm_vector",
    "dot_product",
    "cross_product",
]
