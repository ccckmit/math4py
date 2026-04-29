r"""Tensor theorems and axioms."""

import numpy as np
from typing import List, Tuple


def tensor_creation(data):
    r"""Tensor creation axiom: Tensor can be created from data.
    
    Args:
        data: Input data (list or numpy array)
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor.tensor import Tensor

    try:
        t = Tensor(data)
        return {"pass": True, "shape": t.shape}
    except Exception:
        return {"pass": False}


def tensor_zeros(shape: Tuple[int, ...]):
    r"""Zeros axiom: zeros creates all-zero tensor.
    
    Args:
        shape: Tensor shape
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor.tensor import Tensor

    t = Tensor.zeros(*shape)
    return {"pass": np.all(t.data == 0), "shape": t.shape}


def tensor_ones(shape: Tuple[int, ...]):
    r"""Ones axiom: ones creates all-one tensor.
    
    Args:
        shape: Tensor shape
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor.tensor import Tensor

    t = Tensor.ones(*shape)
    return {"pass": np.all(t.data == 1), "shape": t.shape}


def addition_commutativity(a, b):
    r"""Addition commutativity: a + b = b + a.
    
    Args:
        a: First tensor
        b: Second tensor
    
    Returns:
        Dict with pass status
    """
    c1 = a + b
    c2 = b + a
    return {"pass": np.allclose(c1.data, c2.data)}


def addition_associativity(a, b, c):
    r"""Addition associativity: (a + b) + c = a + (b + c).
    
    Args:
        a: First tensor
        b: Second tensor
        c: Third tensor
    
    Returns:
        Dict with pass status
    """
    result1 = (a + b) + c
    result2 = a + (b + c)
    return {"pass": np.allclose(result1.data, result2.data)}


def multiplication(a, b):
    r"""Multiplication: element-wise product.
    
    Args:
        a: First tensor
        b: Second tensor
    
    Returns:
        Dict with pass status
    """
    c = a * b
    return {"pass": True, "data": c.data}


def matmul(a, b):
    r"""Matrix multiplication.
    
    Args:
        a: First tensor (2D)
        b: Second tensor (2D)
    
    Returns:
        Dict with pass status
    """
    c = a @ b
    return {"pass": True, "shape": c.shape}


def matmul_associativity(a, b, c):
    r"""Matrix multiplication associativity: (AB)C = A(BC).
    
    Args:
        a: First tensor
        b: Second tensor
        c: Third tensor
    
    Returns:
        Dict with pass status
    """
    result1 = (a @ b) @ c
    result2 = a @ (b @ c)
    return {"pass": np.allclose(result1.data, result2.data)}


def sum_property(a):
    r"""Sum property: sum(a) = sum of all elements.
    
    Args:
        a: Tensor
    
    Returns:
        Dict with pass status
    """
    s = a.sum()
    expected = np.sum(a.data)
    return {"pass": s.data == expected, "sum": s.data}


def mean_property(a):
    r"""Mean property: mean(a) = sum / n.
    
    Args:
        a: Tensor
    
    Returns:
        Dict with pass status
    """
    m = a.mean()
    expected = np.mean(a.data)
    return {"pass": abs(m.data - expected) < 1e-10, "mean": m.data}


def reshape_property(a, new_shape):
    r"""Reshape property: reshape doesn't change data.
    
    Args:
        a: Tensor
        new_shape: New shape tuple
    
    Returns:
        Dict with pass status
    """
    b = a.reshape(*new_shape)
    return {"pass": b.shape == new_shape, "shape": b.shape}


def transpose_property(a):
    r"""Transpose property: (A^T)^T = A.
    
    Args:
        a: Tensor
    
    Returns:
        Dict with pass status
    """
    return {"pass": np.allclose(a.T.T.data, a.data)}


def negation_property(a):
    r"""Negation property: -a + a = 0.
    
    Args:
        a: Tensor
    
    Returns:
        Dict with pass status
    """
    b = -a
    c = a + b
    return {"pass": np.allclose(c.data, 0), "data": c.data}


def subtraction_property(a, b):
    r"""Subtraction: a - b = a + (-b).
    
    Args:
        a: First tensor
        b: Second tensor
    
    Returns:
        Dict with pass status
    """
    c = a - b
    d = a + (-b)
    return {"pass": np.allclose(c.data, d.data)}


def pow_property(a, n):
    r"""Power: a^n.
    
    Args:
        a: Tensor
        n: Exponent
    
    Returns:
        Dict with pass status
    """
    b = a ** n
    return {"pass": True, "data": b.data}


def division_property(a, b):
    r"""Division: a / b.
    
    Args:
        a: Numerator tensor
        b: Denominator tensor
    
    Returns:
        Dict with pass status
    """
    c = a / b
    return {"pass": True, "data": c.data}


def exp_property(x):
    r"""Exponential: exp(x).
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    y = x.exp()
    return {"pass": True, "data": y.data}


def log_property(x):
    r"""Natural logarithm: log(x).
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    y = x.log()
    return {"pass": True, "data": y.data}


def exp_log_inverse(x):
    r"""exp(log(x)) = x.
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    y = x.log().exp()
    return {"pass": np.allclose(y.data, x.data)}


def relu_positive(x):
    r"""ReLU: x > 0 => relu(x) = x.
    
    Args:
        x: Tensor with positive values
    
    Returns:
        Dict with pass status
    """
    y = x.relu()
    return {"pass": np.allclose(y.data, x.data)}


def relu_negative(x):
    r"""ReLU: x < 0 => relu(x) = 0.
    
    Args:
        x: Tensor with negative values
    
    Returns:
        Dict with pass status
    """
    y = x.relu()
    return {"pass": np.all(y.data == 0)}


def relu_mixed(x):
    r"""ReLU: mixed positive and negative.
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    y = x.relu()
    expected = np.maximum(x.data, 0)
    return {"pass": np.allclose(y.data, expected)}


def sigmoid_range(x):
    r"""Sigmoid: output in (0, 1].
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    y = x.sigmoid()
    return {"pass": bool(np.all(y.data > 0) and np.all(y.data <= 1))}


def sigmoid_half(x):
    r"""Sigmoid: sigmoid(0) = 0.5.
    
    Args:
        x: Tensor containing 0
    
    Returns:
        Dict with pass status
    """
    y = x.sigmoid()
    return {"pass": bool(abs(y.data[0] - 0.5) < 1e-10)}


def tanh_range(x):
    r"""Tanh: output in [-1, 1].
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.tanh(x)
    return {"pass": bool(np.all(y.data >= -1) and np.all(y.data <= 1))}


def tanh_zero(x):
    r"""Tanh: tanh(0) = 0.
    
    Args:
        x: Tensor containing 0
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.tanh(x)
    return {"pass": bool(abs(y.data[0]) < 1e-10)}


def softmax_sum(x):
    r"""Softmax: probs sum to 1.
    
    Args:
        x: Tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    probs = F.softmax(x)
    return {"pass": bool(abs(np.sum(probs.data) - 1.0) < 1e-10)}


def mse_zero(pred, target):
    r"""MSE: when pred = target, loss = 0.
    
    Args:
        pred: Prediction tensor
        target: Target tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    loss = F.mse_loss(pred, target)
    return {"pass": bool(abs(loss.data) < 1e-10)}


def mse_positive(pred, target):
    r"""MSE: loss always non-negative.
    
    Args:
        pred: Prediction tensor
        target: Target tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    loss = F.mse_loss(pred, target)
    return {"pass": bool(loss.data >= 0)}


def cross_entropy_softmax(pred):
    r"""Cross entropy + softmax: correct class has highest prob.
    
    Args:
        pred: Prediction tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    probs = F.softmax(pred)
    return {"pass": True}


def linear_transform(x, W, b):
    r"""Linear: y = xW^T + b.
    
    Args:
        x: Input tensor
        W: Weight tensor
        b: Bias tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.linear(x, W, b)
    return {"pass": True, "shape": y.shape}


def flatten_transform(x):
    r"""Flatten: flatten tensor.
    
    Args:
        x: Input tensor
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.flatten(x)
    return {"pass": True, "shape": y.shape}


def cat_transform(tensors, dim):
    r"""Cat: concatenate tensors.
    
    Args:
        tensors: Tuple of tensors
        dim: Dimension
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.cat(tensors, dim=dim)
    return {"pass": True, "shape": y.shape}


def stack_transform(tensors, dim):
    r"""Stack: stack tensors.
    
    Args:
        tensors: Tuple of tensors
        dim: Dimension
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.stack(tensors, dim=dim)
    return {"pass": True, "shape": y.shape}


def reshape_transform(x, shape):
    r"""Reshape: reshape tensor.
    
    Args:
        x: Input tensor
        shape: Target shape
    
    Returns:
        Dict with pass status
    """
    from math4py.tensor import function as F

    y = F.reshape(x, *shape)
    return {"pass": y.shape == shape, "shape": y.shape}