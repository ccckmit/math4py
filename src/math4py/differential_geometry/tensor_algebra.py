"""張量代數（Tensor Algebra）運算。

提供帶指標的張量類別，實作張量積、縮並、指標升降等運算。
"""

from typing import List, Tuple

import numpy as np


class Tensor:
    """帶指標的張量類別。

    支援協變（covariant）與逆變（contravariant）指標，
    以及張量代數運算。

    Attributes:
        data: numpy 陣列，形狀為 (dim, dim, ...) 根據階數而定
        indices: 指標類型列表，'u' 表示逆變（上標），'d' 表示協變（下標）
        dim: 流形維度
    """

    def __init__(self, data, indices: List[str], dim: int):
        """初始化張量。

        Args:
            data: 張量數據（numpy 陣列或巢狀列表）
            indices: 指標類型，如 ['u', 'd'] 表示 (1,1) 型張量
                    'u' = 逆變（upper/contravariant）
                    'd' = 協變（lower/covariant）
            dim: 維度
        """
        self.data = np.array(data, dtype=np.float64)
        self.indices = indices
        self.dim = dim

    @property
    def rank(self) -> int:
        """張量階數（指標數量）。"""
        return len(self.indices)

    @property
    def shape(self) -> Tuple:
        """張量形狀。"""
        return self.data.shape

    def __repr__(self):
        return f"Tensor(indices={self.indices}, shape={self.shape})"

    def __add__(self, other: "Tensor") -> "Tensor":
        """張量加法（需相同指標類型）。"""
        if self.indices != other.indices:
            raise ValueError("Cannot add tensors with different index types")
        result_data = self.data + other.data
        return Tensor(result_data, self.indices.copy(), self.dim)

    def __sub__(self, other: "Tensor") -> "Tensor":
        """張量減法。"""
        if self.indices != other.indices:
            raise ValueError("Cannot subtract tensors with different index types")
        result_data = self.data - other.data
        return Tensor(result_data, self.indices.copy(), self.dim)

    def __mul__(self, scalar: float) -> "Tensor":
        """張量數乘。"""
        result_data = self.data * scalar
        return Tensor(result_data, self.indices.copy(), self.dim)

    def tensor_product(self, other: "Tensor") -> "Tensor":
        """張量積（Tensor Product）⊗。

        兩個張量的張量積，指標依序合併。

        Example:
            T1 為 (r1, s1) 型，T2 為 (r2, s2) 型
            T1 ⊗ T2 為 (r1+r2, s1+s2) 型

        Args:
            other: 另一個張量

        Returns:
            張量積結果
        """
        # 計算新形狀
        new_shape = self.shape + other.shape
        result_data = np.zeros(new_shape)

        # 外積
        result_data = np.tensordot(self.data, other.data, axes=0)

        # 合併指標
        new_indices = self.indices + other.indices

        return Tensor(result_data, new_indices, self.dim)

    def contract(self, index1: int, index2: int) -> "Tensor":
        """張量縮並（Contraction）。

        將一個上標（逆變）與一個下標（協變）縮並，
        即對該指標求和。

        Args:
            index1: 第一個縮並指標位置
            index2: 第二個縮並指標位置

        Returns:
            縮並後的張量
        """
        if self.indices[index1] == self.indices[index2]:
            raise ValueError("Can only contract upper with lower indices")

        ndim = self.data.ndim
        # 使用 einsum 進行縮並
        # 構造輸入下標字母
        letters = "abcdefghijklmnopqrstuvwxyz"[:ndim]
        input_str = list(letters)
        # 讓兩個縮並指標使用相同字母
        input_str[index2] = input_str[index1]
        input_str = "".join(input_str)

        # 輸出下標：排除被縮並的指標
        output_indices = [letters[i] for i in range(ndim) if i != index1 and i != index2]
        output_str = "".join(output_indices)

        if output_str:
            einsum_expr = f"{input_str}->{output_str}"
        else:
            einsum_expr = f"{input_str}->"

        result_data = np.einsum(einsum_expr, self.data)

        # 移除被縮並的指標
        new_indices = [self.indices[i] for i in range(ndim) if i != index1 and i != index2]

        return Tensor(result_data, new_indices, self.dim)

    def raise_index(self, index: int, metric: np.ndarray) -> "Tensor":
        """用度規張量昇指標（協變 → 逆變）。

        A^μ = g^{μν} A_ν

        Args:
            index: 要昇的指標位置（必須是協變 'd'）
            metric: 逆度規張量 g^{μν} (dim × dim)

        Returns:
            昇指標後的張量
        """
        if self.indices[index] != "d":
            raise ValueError("Can only raise covariant (lower) indices")

        # 構造新指標列表
        new_indices = self.indices.copy()
        new_indices[index] = "u"

        # 對指定指標做矩陣乘法
        axes = list(range(len(self.indices)))
        axes.remove(index)
        result_data = np.tensordot(metric, self.data, axes=(1, index))
        # 調整軸順序
        result_data = np.moveaxis(result_data, 0, index)

        return Tensor(result_data, new_indices, self.dim)

    def lower_index(self, index: int, metric: np.ndarray) -> "Tensor":
        """用度規張量降指標（逆變 → 協變）。

        A_μ = g_{μν} A^ν

        Args:
            index: 要降的指標位置（必須是逆變 'u'）
            metric: 度規張量 g_{μν} (dim × dim)

        Returns:
            降指標後的張量
        """
        if self.indices[index] != "u":
            raise ValueError("Can only lower contravariant (upper) indices")

        # 構造新指標列表
        new_indices = self.indices.copy()
        new_indices[index] = "d"

        # 對指定指標做矩陣乘法
        result_data = np.tensordot(metric, self.data, axes=(1, index))
        result_data = np.moveaxis(result_data, 0, index)

        return Tensor(result_data, new_indices, self.dim)

    def trace(self) -> float:
        """計算 (1,1) 型張量的跡。

        僅適用於有一個上標和一個下標的張量。

        Returns:
            跡（純量）
        """
        if self.rank != 2 or self.indices != ["u", "d"]:
            raise ValueError("Trace only defined for (1,1) tensors")

        return float(np.trace(self.data))


def tensor_product(t1: Tensor, t2: Tensor) -> Tensor:
    """張量積運算（便捷函數）。"""
    return t1.tensor_product(t2)


def contract(t: Tensor, index1: int, index2: int) -> Tensor:
    """張量縮並（便捷函數）。"""
    return t.contract(index1, index2)


def raise_index(t: Tensor, index: int, metric: np.ndarray) -> Tensor:
    """昇指標（便捷函數）。"""
    return t.raise_index(index, metric)


def lower_index(t: Tensor, index: int, metric: np.ndarray) -> Tensor:
    """降指標（便捷函數）。"""
    return t.lower_index(index, metric)


def metric_tensor(dim: int = 2, signature: str = "euclidean") -> np.ndarray:
    """建立度規張量 g_{μν}。

    Args:
        dim: 維度
        signature: 'euclidean' | 'minkowski' | 'custom'

    Returns:
        度規張量 (dim × dim)
    """
    g = np.eye(dim)
    if signature == "minkowski":
        g[0, 0] = -1.0  # 符號約定 (-, +, +, +)
    return g


def inverse_metric(g: np.ndarray) -> np.ndarray:
    """計算逆度規張量 g^{μν}。"""
    return np.linalg.inv(g)


def kronecker_delta(dim: int) -> np.ndarray:
    """Kronecker delta δ^μ_ν (單位矩陣)。"""
    return np.eye(dim)


__all__ = [
    "Tensor",
    "tensor_product",
    "contract",
    "raise_index",
    "lower_index",
    "metric_tensor",
    "inverse_metric",
    "kronecker_delta",
]
