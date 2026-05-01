"""向量空間 (Vector Space) 定義。"""

from typing import List, Optional


class VectorSpace:
    """向量空間基礎類別。

    定義向量空間的基本操作：加法、純量乘法、
    零向量、加法逆元。
    """

    def __init__(
        self,
        dimension: int,
        field: str = "real",
        vectors: Optional[List[List[float]]] = None,
    ):
        self.dimension = dimension
        self.field = field
        self.vectors = vectors or []

    def add(self, u: List[float], v: List[float]) -> List[float]:
        """向量加法。"""
        return [ui + vi for ui, vi in zip(u, v)]

    def scalar_mul(self, c: float, v: List[float]) -> List[float]:
        """純量乘法。"""
        return [c * vi for vi in v]

    def zero(self) -> List[float]:
        """零向量。"""
        return [0.0] * self.dimension

    def neg(self, v: List[float]) -> List[float]:
        """加法逆元 (負向量)。"""
        return [-vi for vi in v]

    def linear_combination(self, scalars: List[float], vectors: List[List[float]]) -> List[float]:
        """線性組合。"""
        result = self.zero()
        for c, v in zip(scalars, vectors):
            result = self.add(result, self.scalar_mul(c, v))
        return result

    def is_linearly_independent(self, vectors: List[List[float]]) -> bool:
        """檢查向量是否線性獨立 (簡化版)。"""
        if not vectors:
            return True
        import numpy as np

        try:
            mat = np.array(vectors).T
            rank = np.linalg.matrix_rank(mat)
            return rank == len(vectors)
        except (np.linalg.LinAlgError, ValueError):
            return True

    def basis(self) -> List[List[float]]:
        """返回向量空間的一組基 (標準基)。"""
        return [
            [1.0 if i == j else 0.0 for j in range(self.dimension)] for i in range(self.dimension)
        ]

    def dimension_of_subspace(self, vectors: List[List[float]]) -> int:
        """計算子空間維度。"""
        if not vectors:
            return 0
        import numpy as np

        try:
            mat = np.array(vectors).T
            return int(np.linalg.matrix_rank(mat))
        except (np.linalg.LinAlgError, ValueError):
            return len(vectors)

    def __repr__(self):
        return f"VectorSpace(dim={self.dimension}, field={self.field})"


__all__ = ["VectorSpace"]
