"""張量操作函數。"""

from typing import Optional, Tuple

import numpy as np

from .tensor import Tensor


def add(x: Tensor, y: Tensor) -> Tensor:
    """張量加法。"""
    return x + y


def multiply(x: Tensor, y: Tensor) -> Tensor:
    """張量逐元素乘法。"""
    return x * y


def matmul(x: Tensor, y: Tensor) -> Tensor:
    """矩陣乘法。"""
    return x @ y


def sum(x: Tensor, axis: Optional[int] = None, keepdims: bool = False) -> Tensor:
    """張量求和。"""
    return x.sum(axis=axis, keepdims=keepdims)


def mean(x: Tensor, axis: Optional[int] = None, keepdims: bool = False) -> Tensor:
    """張量平均值。"""
    result_data = np.mean(x.data, axis=axis, keepdims=keepdims)
    return Tensor(result_data)


def exp(x: Tensor) -> Tensor:
    """指數函數。"""
    return x.exp()


def log(x: Tensor) -> Tensor:
    """自然對數。"""
    return x.log()


def relu(x: Tensor) -> Tensor:
    """ReLU 激活函數。"""
    return x.relu()


def sigmoid(x: Tensor) -> Tensor:
    """Sigmoid 激活函數。"""
    return x.sigmoid()


def tanh(x: Tensor) -> Tensor:
    """Tanh 激活函數。"""
    result_data = np.tanh(x.data)
    return Tensor(result_data)


def softmax(x: Tensor, axis: int = -1) -> Tensor:
    """Softmax 函數。"""
    return x.softmax(axis=axis)


def cross_entropy(pred: Tensor, target: Tensor, axis: int = -1) -> Tensor:
    """交叉熵。

    Args:
        pred: 預測值（通常是 logits，會先經過 softmax）
        target: 目標值（one-hot 編碼或類別索引）
        axis: softmax 的維度
    """
    if target.data.ndim == pred.data.ndim - 1:
        target_one_hot = np.zeros_like(pred.data)
        if axis == -1 or axis == pred.data.ndim - 1:
            target_one_hot[np.arange(len(pred.data)), target.data.astype(int)] = 1
        else:
            indices = np.expand_dims(target.data.astype(int), axis)
            np.put_along_axis(target_one_hot, indices, 1, axis)
        target = Tensor(target_one_hot)

    probs = softmax(pred, axis=axis)

    eps = 1e-15
    log_probs = (probs + eps).log()
    result = -(target * log_probs).sum(axis=axis)

    return result


def mse_loss(pred: Tensor, target: Tensor) -> Tensor:
    """均方誤差損失。"""
    diff = pred - target
    return (diff * diff).mean()


def linear(x: Tensor, weight: Tensor, bias: Optional[Tensor] = None) -> Tensor:
    """線性變換：y = x @ W + b。"""
    result = x @ weight
    if bias is not None:
        result = result + bias
    return result


def reshape(x: Tensor, *shape) -> Tensor:
    """改變形狀。"""
    return x.reshape(*shape)


def transpose(x: Tensor, *axes) -> Tensor:
    """轉置。"""
    return x.transpose(*axes)


def flatten(x: Tensor, start_dim: int = 1) -> Tensor:
    """將張量展平（通常從第 start_dim 維開始）。"""
    shape = list(x.data.shape)
    if start_dim < 0:
        start_dim = len(shape) + start_dim

    new_shape = shape[:start_dim] + [-1]
    return x.reshape(*new_shape)


def cat(tensors: Tuple[Tensor, ...], dim: int = 0) -> Tensor:
    """沿著指定維度連接張量。"""
    data_list = [t.data for t in tensors]
    result_data = np.concatenate(data_list, axis=dim)
    return Tensor(result_data)


def stack(tensors: Tuple[Tensor, ...], dim: int = 0) -> Tensor:
    """在新維度上堆疊張量。"""
    data_list = [np.expand_dims(t.data, dim) for t in tensors]
    result_data = np.concatenate(data_list, axis=dim)
    return Tensor(result_data)
